""" Cisco_IOS_XR_freqsync_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR freqsync package operational data.

This module contains definitions
for the following management objects\:
  frequency\-synchronization\: Frequency Synchronization
    operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsyncBagClockIntfClass(Enum):
    """
    FsyncBagClockIntfClass (Enum Class)

    Clock\-interface class

    .. data:: clock_class_bitst1 = 0

    	BITS T1

    .. data:: clock_class_bitse1 = 1

    	BITS E1

    .. data:: clock_class_bits2m = 2

    	BITS 2M

    .. data:: clock_class_bits6m = 3

    	BITS 6M

    .. data:: clock_class_bits64k = 4

    	BITS 64K

    .. data:: clock_class_dti = 5

    	DTI

    .. data:: clock_class_gps = 6

    	GPS

    .. data:: clock_class_chassis_sync = 7

    	Inter-Chassis Sync

    .. data:: clock_class_bitsj1 = 8

    	Bits J1

    .. data:: clock_class_unknown = 255

    	Unknown

    """

    clock_class_bitst1 = Enum.YLeaf(0, "clock-class-bitst1")

    clock_class_bitse1 = Enum.YLeaf(1, "clock-class-bitse1")

    clock_class_bits2m = Enum.YLeaf(2, "clock-class-bits2m")

    clock_class_bits6m = Enum.YLeaf(3, "clock-class-bits6m")

    clock_class_bits64k = Enum.YLeaf(4, "clock-class-bits64k")

    clock_class_dti = Enum.YLeaf(5, "clock-class-dti")

    clock_class_gps = Enum.YLeaf(6, "clock-class-gps")

    clock_class_chassis_sync = Enum.YLeaf(7, "clock-class-chassis-sync")

    clock_class_bitsj1 = Enum.YLeaf(8, "clock-class-bitsj1")

    clock_class_unknown = Enum.YLeaf(255, "clock-class-unknown")


class FsyncBagDampingState(Enum):
    """
    FsyncBagDampingState (Enum Class)

    Damping state

    .. data:: damping_state_down = 0

    	Down

    .. data:: damping_state_coming_up = 1

    	Coming up

    .. data:: damping_state_up = 2

    	Up

    .. data:: damping_state_going_down = 3

    	Going down

    """

    damping_state_down = Enum.YLeaf(0, "damping-state-down")

    damping_state_coming_up = Enum.YLeaf(1, "damping-state-coming-up")

    damping_state_up = Enum.YLeaf(2, "damping-state-up")

    damping_state_going_down = Enum.YLeaf(3, "damping-state-going-down")


class FsyncBagEsmcPeerState(Enum):
    """
    FsyncBagEsmcPeerState (Enum Class)

    ESMC peer state

    .. data:: peer_down = 1808240398

    	Peer state down

    .. data:: peer_up = 1808240399

    	Peer state up

    .. data:: peer_timed_out = 1808240400

    	Peer state timed out

    .. data:: peer_unknown = 1808240401

    	Peer state unknown

    """

    peer_down = Enum.YLeaf(1808240398, "peer-down")

    peer_up = Enum.YLeaf(1808240399, "peer-up")

    peer_timed_out = Enum.YLeaf(1808240400, "peer-timed-out")

    peer_unknown = Enum.YLeaf(1808240401, "peer-unknown")


class FsyncBagForwardtraceNode(Enum):
    """
    FsyncBagForwardtraceNode (Enum Class)

    Selection forwardtrace node information

    .. data:: forward_trace_node_selection_point = 0

    	A selection point forwardtrace node

    .. data:: forward_trace_node_source = 1

    	A timing source forwardtrace node

    """

    forward_trace_node_selection_point = Enum.YLeaf(0, "forward-trace-node-selection-point")

    forward_trace_node_source = Enum.YLeaf(1, "forward-trace-node-source")


class FsyncBagQlO1Value(Enum):
    """
    FsyncBagQlO1Value (Enum Class)

    Quality level option 1 values

    .. data:: option1_invalid = 0

    	Invalid

    .. data:: option1_do_not_use = 1

    	Do not use

    .. data:: option1_failed = 2

    	Failed

    .. data:: option1_none = 3

    	Interface does not support SSMs or no QL has

    	been received

    .. data:: option1prc = 10

    	Primary reference clock

    .. data:: option1ssu_a = 11

    	Type I or V slave clock

    .. data:: option1ssu_b = 12

    	Type VI slave clock

    .. data:: option1sec = 13

    	SONET equipment clock

    """

    option1_invalid = Enum.YLeaf(0, "option1-invalid")

    option1_do_not_use = Enum.YLeaf(1, "option1-do-not-use")

    option1_failed = Enum.YLeaf(2, "option1-failed")

    option1_none = Enum.YLeaf(3, "option1-none")

    option1prc = Enum.YLeaf(10, "option1prc")

    option1ssu_a = Enum.YLeaf(11, "option1ssu-a")

    option1ssu_b = Enum.YLeaf(12, "option1ssu-b")

    option1sec = Enum.YLeaf(13, "option1sec")


class FsyncBagQlO2G1Value(Enum):
    """
    FsyncBagQlO2G1Value (Enum Class)

    Quality level option 2, generation 1 values

    .. data:: option2_generation1_invalid = 0

    	Invalid

    .. data:: option2_generation1_do_not_use = 1

    	Do not use

    .. data:: option2_generation1_failed = 2

    	Failed

    .. data:: option2_generation1_none = 3

    	Interface does not support SSMs or no QL has

    	been received

    .. data:: option2_generation1prs = 20

    	Primary reference source

    .. data:: option2_generation1stu = 21

    	Synchronized - traceability unknown

    .. data:: option2_generation1_stratum2 = 22

    	Stratum 2

    .. data:: option2_generation1_stratum3 = 23

    	Stratum 3

    .. data:: option2_generation1smc = 24

    	SONET clock self timed

    .. data:: option2_generation1_stratum4 = 25

    	Stratum 4 freerun

    """

    option2_generation1_invalid = Enum.YLeaf(0, "option2-generation1-invalid")

    option2_generation1_do_not_use = Enum.YLeaf(1, "option2-generation1-do-not-use")

    option2_generation1_failed = Enum.YLeaf(2, "option2-generation1-failed")

    option2_generation1_none = Enum.YLeaf(3, "option2-generation1-none")

    option2_generation1prs = Enum.YLeaf(20, "option2-generation1prs")

    option2_generation1stu = Enum.YLeaf(21, "option2-generation1stu")

    option2_generation1_stratum2 = Enum.YLeaf(22, "option2-generation1-stratum2")

    option2_generation1_stratum3 = Enum.YLeaf(23, "option2-generation1-stratum3")

    option2_generation1smc = Enum.YLeaf(24, "option2-generation1smc")

    option2_generation1_stratum4 = Enum.YLeaf(25, "option2-generation1-stratum4")


class FsyncBagQlO2G2Value(Enum):
    """
    FsyncBagQlO2G2Value (Enum Class)

    Quality level option 2, generation 2 values

    .. data:: option2_generation2_invalid = 0

    	Invalid

    .. data:: option2_generation2_do_not_use = 1

    	Do not use

    .. data:: option2_generation2_failed = 2

    	Failed

    .. data:: option2_generation2_none = 3

    	Interface does not support SSMs or no QL has

    	been received

    .. data:: option2_generation2prs = 30

    	Primary reference source

    .. data:: option2_generation2stu = 31

    	Synchronized - traceability unknown

    .. data:: option2_generation2_stratum2 = 32

    	Stratum 2

    .. data:: option2_generation2_stratum3 = 33

    	Stratum 3

    .. data:: option2_generation2tnc = 34

    	Transit node clock

    .. data:: option2_generation2_stratum3e = 35

    	Stratum 3E

    .. data:: option2_generation2smc = 36

    	SONET clock self timed

    .. data:: option2_generation2_stratum4 = 37

    	Stratum 4 freerun

    """

    option2_generation2_invalid = Enum.YLeaf(0, "option2-generation2-invalid")

    option2_generation2_do_not_use = Enum.YLeaf(1, "option2-generation2-do-not-use")

    option2_generation2_failed = Enum.YLeaf(2, "option2-generation2-failed")

    option2_generation2_none = Enum.YLeaf(3, "option2-generation2-none")

    option2_generation2prs = Enum.YLeaf(30, "option2-generation2prs")

    option2_generation2stu = Enum.YLeaf(31, "option2-generation2stu")

    option2_generation2_stratum2 = Enum.YLeaf(32, "option2-generation2-stratum2")

    option2_generation2_stratum3 = Enum.YLeaf(33, "option2-generation2-stratum3")

    option2_generation2tnc = Enum.YLeaf(34, "option2-generation2tnc")

    option2_generation2_stratum3e = Enum.YLeaf(35, "option2-generation2-stratum3e")

    option2_generation2smc = Enum.YLeaf(36, "option2-generation2smc")

    option2_generation2_stratum4 = Enum.YLeaf(37, "option2-generation2-stratum4")


class FsyncBagQlOption(Enum):
    """
    FsyncBagQlOption (Enum Class)

    Quality level option

    .. data:: no_quality_level_option = 0

    	Interface does not support SSMs or no QL has

    	been received

    .. data:: option1 = 1

    	ITU-T Quality level option 1

    .. data:: option2_generation1 = 2

    	ITU-T Quality level option 2, generation 1

    .. data:: option2_generation2 = 3

    	ITU-T Quality level option 2, generation 2

    .. data:: invalid_quality_level_option = 4

    	Invalid quality level option

    """

    no_quality_level_option = Enum.YLeaf(0, "no-quality-level-option")

    option1 = Enum.YLeaf(1, "option1")

    option2_generation1 = Enum.YLeaf(2, "option2-generation1")

    option2_generation2 = Enum.YLeaf(3, "option2-generation2")

    invalid_quality_level_option = Enum.YLeaf(4, "invalid-quality-level-option")


class FsyncBagSourceClass(Enum):
    """
    FsyncBagSourceClass (Enum Class)

    Source class

    .. data:: invalid_source = 0

    	Invalid source class

    .. data:: ethernet_interface_source = 1

    	Ethernet interface

    .. data:: sonet_interface_source = 2

    	SONET interface

    .. data:: clock_interface_source = 3

    	Clock interface

    .. data:: internal_clock_source = 4

    	Internal clock

    .. data:: ptp_source = 5

    	PTP clock

    .. data:: satellite_access_interface_source = 6

    	Satellite Access Interface

    .. data:: ntp_source = 7

    	NTP clock

    .. data:: gnss_receiver = 8

    	GNSS Receiver

    """

    invalid_source = Enum.YLeaf(0, "invalid-source")

    ethernet_interface_source = Enum.YLeaf(1, "ethernet-interface-source")

    sonet_interface_source = Enum.YLeaf(2, "sonet-interface-source")

    clock_interface_source = Enum.YLeaf(3, "clock-interface-source")

    internal_clock_source = Enum.YLeaf(4, "internal-clock-source")

    ptp_source = Enum.YLeaf(5, "ptp-source")

    satellite_access_interface_source = Enum.YLeaf(6, "satellite-access-interface-source")

    ntp_source = Enum.YLeaf(7, "ntp-source")

    gnss_receiver = Enum.YLeaf(8, "gnss-receiver")


class FsyncBagSourceState(Enum):
    """
    FsyncBagSourceState (Enum Class)

    Source state

    .. data:: source_state_unknown = 0

    	Unknown

    .. data:: source_state_up = 1

    	Up

    .. data:: source_state_down = 2

    	Down

    .. data:: source_state_unavailable = 3

    	Unvailable

    """

    source_state_unknown = Enum.YLeaf(0, "source-state-unknown")

    source_state_up = Enum.YLeaf(1, "source-state-up")

    source_state_down = Enum.YLeaf(2, "source-state-down")

    source_state_unavailable = Enum.YLeaf(3, "source-state-unavailable")


class FsyncBagStreamInput(Enum):
    """
    FsyncBagStreamInput (Enum Class)

    Stream input type

    .. data:: invalid_input = 0

    	Invalid stream input

    .. data:: source_input = 1

    	Source stream input

    .. data:: selection_point_input = 2

    	Selection point stream input

    """

    invalid_input = Enum.YLeaf(0, "invalid-input")

    source_input = Enum.YLeaf(1, "source-input")

    selection_point_input = Enum.YLeaf(2, "selection-point-input")


class FsyncBagStreamState(Enum):
    """
    FsyncBagStreamState (Enum Class)

    Platform stream status

    .. data:: stream_invalid = 0

    	Invalid stream

    .. data:: stream_unqualified = 1

    	Unqualified stream

    .. data:: stream_available = 2

    	Stream available

    .. data:: stream_available_acquiring = 3

    	Stream available acquiring

    .. data:: stream_locked = 4

    	Stream locked

    .. data:: stream_holdover = 5

    	Stream in holdover

    .. data:: stream_freerun = 6

    	Stream free running

    .. data:: stream_failed = 7

    	Stream failed

    .. data:: stream_unmonitored = 8

    	Unmonitored stream

    .. data:: stream_error = 9

    	Stream error

    """

    stream_invalid = Enum.YLeaf(0, "stream-invalid")

    stream_unqualified = Enum.YLeaf(1, "stream-unqualified")

    stream_available = Enum.YLeaf(2, "stream-available")

    stream_available_acquiring = Enum.YLeaf(3, "stream-available-acquiring")

    stream_locked = Enum.YLeaf(4, "stream-locked")

    stream_holdover = Enum.YLeaf(5, "stream-holdover")

    stream_freerun = Enum.YLeaf(6, "stream-freerun")

    stream_failed = Enum.YLeaf(7, "stream-failed")

    stream_unmonitored = Enum.YLeaf(8, "stream-unmonitored")

    stream_error = Enum.YLeaf(9, "stream-error")


class FsyncSource(Enum):
    """
    FsyncSource (Enum Class)

    Fsync source

    .. data:: ethernet = 1

    	An ethernet interface

    .. data:: sonet = 2

    	A SONET interface

    .. data:: clock = 3

    	A clock interface

    .. data:: internal = 4

    	An internal clock

    .. data:: ptp = 5

    	A PTP clock

    .. data:: satellite_access = 6

    	A satellite access interface clock

    .. data:: ntp = 7

    	An NTP clock

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    sonet = Enum.YLeaf(2, "sonet")

    clock = Enum.YLeaf(3, "clock")

    internal = Enum.YLeaf(4, "internal")

    ptp = Enum.YLeaf(5, "ptp")

    satellite_access = Enum.YLeaf(6, "satellite-access")

    ntp = Enum.YLeaf(7, "ntp")


class FsyncStream(Enum):
    """
    FsyncStream (Enum Class)

    Fsync stream

    .. data:: local = 1

    	Stream input from a local source

    .. data:: selection_point = 2

    	Stream input from a selection point on a remote

    	node

    """

    local = Enum.YLeaf(1, "local")

    selection_point = Enum.YLeaf(2, "selection-point")


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



class FrequencySynchronization(Entity):
    """
    Frequency Synchronization operational data
    
    .. attribute:: global_nodes
    
    	Table for global node\-specific operational data
    	**type**\:  :py:class:`GlobalNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes>`
    
    .. attribute:: global_interfaces
    
    	Table for global interface operational data
    	**type**\:  :py:class:`GlobalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces>`
    
    .. attribute:: summary
    
    	Summary operational data
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary>`
    
    .. attribute:: interface_datas
    
    	Table for interface operational data
    	**type**\:  :py:class:`InterfaceDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas>`
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes>`
    
    

    """

    _prefix = 'freqsync-oper'
    _revision = '2017-10-20'

    def __init__(self):
        super(FrequencySynchronization, self).__init__()
        self._top_entity = None

        self.yang_name = "frequency-synchronization"
        self.yang_parent_name = "Cisco-IOS-XR-freqsync-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global-nodes", ("global_nodes", FrequencySynchronization.GlobalNodes)), ("global-interfaces", ("global_interfaces", FrequencySynchronization.GlobalInterfaces)), ("summary", ("summary", FrequencySynchronization.Summary)), ("interface-datas", ("interface_datas", FrequencySynchronization.InterfaceDatas)), ("nodes", ("nodes", FrequencySynchronization.Nodes))])
        self._leafs = OrderedDict()

        self.global_nodes = FrequencySynchronization.GlobalNodes()
        self.global_nodes.parent = self
        self._children_name_map["global_nodes"] = "global-nodes"

        self.global_interfaces = FrequencySynchronization.GlobalInterfaces()
        self.global_interfaces.parent = self
        self._children_name_map["global_interfaces"] = "global-interfaces"

        self.summary = FrequencySynchronization.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.interface_datas = FrequencySynchronization.InterfaceDatas()
        self.interface_datas.parent = self
        self._children_name_map["interface_datas"] = "interface-datas"

        self.nodes = FrequencySynchronization.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FrequencySynchronization, [], name, value)


    class GlobalNodes(Entity):
        """
        Table for global node\-specific operational data
        
        .. attribute:: global_node
        
        	Global node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`GlobalNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            super(FrequencySynchronization.GlobalNodes, self).__init__()

            self.yang_name = "global-nodes"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("global-node", ("global_node", FrequencySynchronization.GlobalNodes.GlobalNode))])
            self._leafs = OrderedDict()

            self.global_node = YList(self)
            self._segment_path = lambda: "global-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.GlobalNodes, [], name, value)


        class GlobalNode(Entity):
            """
            Global node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: clock_interface_selection_back_traces
            
            	Selection backtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionBackTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces>`
            
            .. attribute:: clock_interface_selection_forward_traces
            
            	Selection forwardtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionForwardTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces>`
            
            .. attribute:: time_of_day_back_trace
            
            	Selection backtrace operational data for time\-of\-day on a particular node
            	**type**\:  :py:class:`TimeOfDayBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace>`
            
            .. attribute:: ntp_selection_forward_trace
            
            	Selection forwardtrace operational data for a NTP clock
            	**type**\:  :py:class:`NtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace>`
            
            .. attribute:: ptp_selection_forward_trace
            
            	Selection forwardtrace operational data for a PTP clock
            	**type**\:  :py:class:`PtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.GlobalNodes.GlobalNode, self).__init__()

                self.yang_name = "global-node"
                self.yang_parent_name = "global-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("clock-interface-selection-back-traces", ("clock_interface_selection_back_traces", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces)), ("clock-interface-selection-forward-traces", ("clock_interface_selection_forward_traces", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces)), ("time-of-day-back-trace", ("time_of_day_back_trace", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace)), ("ntp-selection-forward-trace", ("ntp_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace)), ("ptp-selection-forward-trace", ("ptp_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.clock_interface_selection_back_traces = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces()
                self.clock_interface_selection_back_traces.parent = self
                self._children_name_map["clock_interface_selection_back_traces"] = "clock-interface-selection-back-traces"

                self.clock_interface_selection_forward_traces = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces()
                self.clock_interface_selection_forward_traces.parent = self
                self._children_name_map["clock_interface_selection_forward_traces"] = "clock-interface-selection-forward-traces"

                self.time_of_day_back_trace = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace()
                self.time_of_day_back_trace.parent = self
                self._children_name_map["time_of_day_back_trace"] = "time-of-day-back-trace"

                self.ntp_selection_forward_trace = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace()
                self.ntp_selection_forward_trace.parent = self
                self._children_name_map["ntp_selection_forward_trace"] = "ntp-selection-forward-trace"

                self.ptp_selection_forward_trace = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace()
                self.ptp_selection_forward_trace.parent = self
                self._children_name_map["ptp_selection_forward_trace"] = "ptp-selection-forward-trace"
                self._segment_path = lambda: "global-node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/global-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode, ['node'], name, value)


            class ClockInterfaceSelectionBackTraces(Entity):
                """
                Selection backtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_back_trace
                
                	Selection backtrace operational data for a particular clock\-interface or GNSS receiver
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces, self).__init__()

                    self.yang_name = "clock-interface-selection-back-traces"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-interface-selection-back-trace", ("clock_interface_selection_back_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace))])
                    self._leafs = OrderedDict()

                    self.clock_interface_selection_back_trace = YList(self)
                    self._segment_path = lambda: "clock-interface-selection-back-traces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces, [], name, value)


                class ClockInterfaceSelectionBackTrace(Entity):
                    """
                    Selection backtrace operational data for a
                    particular clock\-interface or GNSS receiver
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: selected_source
                    
                    	Source which has been selected for output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource>`
                    
                    .. attribute:: selection_point
                    
                    	List of selection points in the backtrace
                    	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace, self).__init__()

                        self.yang_name = "clock-interface-selection-back-trace"
                        self.yang_parent_name = "clock-interface-selection-back-traces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','id']
                        self._child_classes = OrderedDict([("selected-source", ("selected_source", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource)), ("selection-point", ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                        ])
                        self.clock_type = None
                        self.id = None

                        self.selected_source = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource()
                        self.selected_source.parent = self
                        self._children_name_map["selected_source"] = "selected-source"

                        self.selection_point = YList(self)
                        self._segment_path = lambda: "clock-interface-selection-back-trace" + "[clock-type='" + str(self.clock_type) + "']" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace, ['clock_type', 'id'], name, value)


                    class SelectedSource(Entity):
                        """
                        Source which has been selected for output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock-interface-selection-back-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class SelectionPoint(Entity):
                        """
                        List of selection points in the backtrace
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint, self).__init__()

                            self.yang_name = "selection-point"
                            self.yang_parent_name = "clock-interface-selection-back-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ])
                            self.selection_point_type = None
                            self.selection_point_description = None
                            self.node = None
                            self._segment_path = lambda: "selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


            class ClockInterfaceSelectionForwardTraces(Entity):
                """
                Selection forwardtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_forward_trace
                
                	Selection forwardtrace operational data for a particular clock\-interface
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces, self).__init__()

                    self.yang_name = "clock-interface-selection-forward-traces"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-interface-selection-forward-trace", ("clock_interface_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace))])
                    self._leafs = OrderedDict()

                    self.clock_interface_selection_forward_trace = YList(self)
                    self._segment_path = lambda: "clock-interface-selection-forward-traces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces, [], name, value)


                class ClockInterfaceSelectionForwardTrace(Entity):
                    """
                    Selection forwardtrace operational data for a
                    particular clock\-interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forward_trace
                    
                    	Selection ForwardTrace
                    	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace, self).__init__()

                        self.yang_name = "clock-interface-selection-forward-trace"
                        self.yang_parent_name = "clock-interface-selection-forward-traces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','port']
                        self._child_classes = OrderedDict([("forward-trace", ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ])
                        self.clock_type = None
                        self.port = None

                        self.forward_trace = YList(self)
                        self._segment_path = lambda: "clock-interface-selection-forward-trace" + "[clock-type='" + str(self.clock_type) + "']" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace, ['clock_type', 'port'], name, value)


                    class ForwardTrace(Entity):
                        """
                        Selection ForwardTrace
                        
                        .. attribute:: forward_trace_node
                        
                        	The source or selection point at this point in the forwardtrace
                        	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace, self).__init__()

                            self.yang_name = "forward-trace"
                            self.yang_parent_name = "clock-interface-selection-forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("forward-trace-node", ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode))])
                            self._leafs = OrderedDict()

                            self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                            self.forward_trace_node.parent = self
                            self._children_name_map["forward_trace_node"] = "forward-trace-node"
                            self._segment_path = lambda: "forward-trace"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace, [], name, value)


                        class ForwardTraceNode(Entity):
                            """
                            The source or selection point at this point in
                            the forwardtrace
                            
                            .. attribute:: selection_point
                            
                            	Selection Point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                            
                            .. attribute:: source
                            
                            	Timing Source
                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                            
                            .. attribute:: node_type
                            
                            	NodeType
                            	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                                self.yang_name = "forward-trace-node"
                                self.yang_parent_name = "forward-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("selection-point", ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint)), ("source", ("source", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source))])
                                self._leafs = OrderedDict([
                                    ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagForwardtraceNode', '')])),
                                ])
                                self.node_type = None

                                self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                                self.selection_point.parent = self
                                self._children_name_map["selection_point"] = "selection-point"

                                self.source = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                                self.source.parent = self
                                self._children_name_map["source"] = "source"
                                self._segment_path = lambda: "forward-trace-node"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, [u'node_type'], name, value)


                            class SelectionPoint(Entity):
                                """
                                Selection Point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                    self.yang_name = "selection-point"
                                    self.yang_parent_name = "forward-trace-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                        ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ])
                                    self.selection_point_type = None
                                    self.selection_point_description = None
                                    self.node = None
                                    self._segment_path = lambda: "selection-point"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                            class Source(Entity):
                                """
                                Timing Source
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                                
                                .. attribute:: gnss_receiver_id
                                
                                	GNSS Receiver ID
                                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                                
                                .. attribute:: source_class
                                
                                	SourceClass
                                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                                
                                .. attribute:: ethernet_interface
                                
                                	Ethernet interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: sonet_interface
                                
                                	SONET interfaces
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: node
                                
                                	Internal Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: ptp_node
                                
                                	PTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: satellite_access_interface
                                
                                	Satellite Access Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: ntp_node
                                
                                	NTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                    self.yang_name = "source"
                                    self.yang_parent_name = "forward-trace-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                    self._leafs = OrderedDict([
                                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                    ])
                                    self.source_class = None
                                    self.ethernet_interface = None
                                    self.sonet_interface = None
                                    self.node = None
                                    self.ptp_node = None
                                    self.satellite_access_interface = None
                                    self.ntp_node = None

                                    self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                    self.clock_id.parent = self
                                    self._children_name_map["clock_id"] = "clock-id"

                                    self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                    self.gnss_receiver_id.parent = self
                                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                    self._segment_path = lambda: "source"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                                class ClockId(Entity):
                                    """
                                    Clock ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    .. attribute:: id
                                    
                                    	ID (port number for clock interface, receiver number for GNSS receiver)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: clock_name
                                    
                                    	Name
                                    	**type**\: str
                                    
                                    	**length:** 0..144
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2017-10-20'

                                    def __init__(self):
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                        self.yang_name = "clock-id"
                                        self.yang_parent_name = "source"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                        ])
                                        self.node = None
                                        self.id = None
                                        self.clock_name = None
                                        self._segment_path = lambda: "clock-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                                class GnssReceiverId(Entity):
                                    """
                                    GNSS Receiver ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    .. attribute:: id
                                    
                                    	ID (port number for clock interface, receiver number for GNSS receiver)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: clock_name
                                    
                                    	Name
                                    	**type**\: str
                                    
                                    	**length:** 0..144
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2017-10-20'

                                    def __init__(self):
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, self).__init__()

                                        self.yang_name = "gnss-receiver-id"
                                        self.yang_parent_name = "source"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                        ])
                                        self.node = None
                                        self.id = None
                                        self.clock_name = None
                                        self._segment_path = lambda: "gnss-receiver-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


            class TimeOfDayBackTrace(Entity):
                """
                Selection backtrace operational data for
                time\-of\-day on a particular node
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource>`
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace, self).__init__()

                    self.yang_name = "time-of-day-back-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("selected-source", ("selected_source", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource)), ("selection-point", ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint))])
                    self._leafs = OrderedDict()

                    self.selected_source = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource()
                    self.selected_source.parent = self
                    self._children_name_map["selected_source"] = "selected-source"

                    self.selection_point = YList(self)
                    self._segment_path = lambda: "time-of-day-back-trace"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace, [], name, value)


                class SelectedSource(Entity):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId>`
                    
                    .. attribute:: gnss_receiver_id
                    
                    	GNSS Receiver ID
                    	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId>`
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: node
                    
                    	Internal Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "time-of-day-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId))])
                        self._leafs = OrderedDict([
                            ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                            ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                            ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                            ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                            ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                        ])
                        self.source_class = None
                        self.ethernet_interface = None
                        self.sonet_interface = None
                        self.node = None
                        self.ptp_node = None
                        self.satellite_access_interface = None
                        self.ntp_node = None

                        self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"

                        self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId()
                        self.gnss_receiver_id.parent = self
                        self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                        self._segment_path = lambda: "selected-source"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                    class ClockId(Entity):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId, self).__init__()

                            self.yang_name = "clock-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                            ])
                            self.node = None
                            self.id = None
                            self.clock_name = None
                            self._segment_path = lambda: "clock-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                    class GnssReceiverId(Entity):
                        """
                        GNSS Receiver ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId, self).__init__()

                            self.yang_name = "gnss-receiver-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                            ])
                            self.node = None
                            self.id = None
                            self.clock_name = None
                            self._segment_path = lambda: "gnss-receiver-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                class SelectionPoint(Entity):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint, self).__init__()

                        self.yang_name = "selection-point"
                        self.yang_parent_name = "time-of-day-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ])
                        self.selection_point_type = None
                        self.selection_point_description = None
                        self.node = None
                        self._segment_path = lambda: "selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


            class NtpSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                NTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace, self).__init__()

                    self.yang_name = "ntp-selection-forward-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("forward-trace", ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace))])
                    self._leafs = OrderedDict()

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "ntp-selection-forward-trace"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "ntp-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("forward-trace-node", ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode))])
                        self._leafs = OrderedDict()

                        self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._segment_path = lambda: "forward-trace"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace, [], name, value)


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("selection-point", ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint)), ("source", ("source", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source))])
                            self._leafs = OrderedDict([
                                ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagForwardtraceNode', '')])),
                            ])
                            self.node_type = None

                            self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"

                            self.source = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._segment_path = lambda: "forward-trace-node"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, [u'node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ])
                                self.selection_point_type = None
                                self.selection_point_description = None
                                self.node = None
                                self._segment_path = lambda: "selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.node = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                            class GnssReceiverId(Entity):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, self).__init__()

                                    self.yang_name = "gnss-receiver-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "gnss-receiver-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


            class PtpSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                PTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace, self).__init__()

                    self.yang_name = "ptp-selection-forward-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("forward-trace", ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace))])
                    self._leafs = OrderedDict()

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "ptp-selection-forward-trace"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "ptp-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("forward-trace-node", ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode))])
                        self._leafs = OrderedDict()

                        self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._segment_path = lambda: "forward-trace"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace, [], name, value)


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("selection-point", ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint)), ("source", ("source", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source))])
                            self._leafs = OrderedDict([
                                ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagForwardtraceNode', '')])),
                            ])
                            self.node_type = None

                            self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"

                            self.source = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._segment_path = lambda: "forward-trace-node"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, [u'node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ])
                                self.selection_point_type = None
                                self.selection_point_description = None
                                self.node = None
                                self._segment_path = lambda: "selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.node = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                            class GnssReceiverId(Entity):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, self).__init__()

                                    self.yang_name = "gnss-receiver-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "gnss-receiver-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


    class GlobalInterfaces(Entity):
        """
        Table for global interface operational data
        
        .. attribute:: global_interface
        
        	Global interface information for a particular interface
        	**type**\: list of  		 :py:class:`GlobalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            super(FrequencySynchronization.GlobalInterfaces, self).__init__()

            self.yang_name = "global-interfaces"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("global-interface", ("global_interface", FrequencySynchronization.GlobalInterfaces.GlobalInterface))])
            self._leafs = OrderedDict()

            self.global_interface = YList(self)
            self._segment_path = lambda: "global-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.GlobalInterfaces, [], name, value)


        class GlobalInterface(Entity):
            """
            Global interface information for a particular
            interface
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: interface_selection_forward_trace
            
            	Selection forwardtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace>`
            
            .. attribute:: interface_selection_back_trace
            
            	Selection backtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface, self).__init__()

                self.yang_name = "global-interface"
                self.yang_parent_name = "global-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("interface-selection-forward-trace", ("interface_selection_forward_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace)), ("interface-selection-back-trace", ("interface_selection_back_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.interface_selection_forward_trace = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace()
                self.interface_selection_forward_trace.parent = self
                self._children_name_map["interface_selection_forward_trace"] = "interface-selection-forward-trace"

                self.interface_selection_back_trace = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace()
                self.interface_selection_back_trace.parent = self
                self._children_name_map["interface_selection_back_trace"] = "interface-selection-back-trace"
                self._segment_path = lambda: "global-interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/global-interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface, ['interface_name'], name, value)


            class InterfaceSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                particular interface
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace, self).__init__()

                    self.yang_name = "interface-selection-forward-trace"
                    self.yang_parent_name = "global-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("forward-trace", ("forward_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace))])
                    self._leafs = OrderedDict()

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "interface-selection-forward-trace"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "interface-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("forward-trace-node", ("forward_trace_node", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode))])
                        self._leafs = OrderedDict()

                        self.forward_trace_node = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._segment_path = lambda: "forward-trace"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace, [], name, value)


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("selection-point", ("selection_point", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint)), ("source", ("source", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source))])
                            self._leafs = OrderedDict([
                                ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagForwardtraceNode', '')])),
                            ])
                            self.node_type = None

                            self.selection_point = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"

                            self.source = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._segment_path = lambda: "forward-trace-node"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, [u'node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ])
                                self.selection_point_type = None
                                self.selection_point_description = None
                                self.node = None
                                self._segment_path = lambda: "selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.node = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                            class GnssReceiverId(Entity):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, self).__init__()

                                    self.yang_name = "gnss-receiver-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "gnss-receiver-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


            class InterfaceSelectionBackTrace(Entity):
                """
                Selection backtrace operational data for a
                particular interface
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource>`
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace, self).__init__()

                    self.yang_name = "interface-selection-back-trace"
                    self.yang_parent_name = "global-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("selected-source", ("selected_source", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource)), ("selection-point", ("selection_point", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint))])
                    self._leafs = OrderedDict()

                    self.selected_source = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource()
                    self.selected_source.parent = self
                    self._children_name_map["selected_source"] = "selected-source"

                    self.selection_point = YList(self)
                    self._segment_path = lambda: "interface-selection-back-trace"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace, [], name, value)


                class SelectedSource(Entity):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId>`
                    
                    .. attribute:: gnss_receiver_id
                    
                    	GNSS Receiver ID
                    	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId>`
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: node
                    
                    	Internal Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "interface-selection-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId))])
                        self._leafs = OrderedDict([
                            ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                            ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                            ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                            ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                            ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                        ])
                        self.source_class = None
                        self.ethernet_interface = None
                        self.sonet_interface = None
                        self.node = None
                        self.ptp_node = None
                        self.satellite_access_interface = None
                        self.ntp_node = None

                        self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"

                        self.gnss_receiver_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId()
                        self.gnss_receiver_id.parent = self
                        self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                        self._segment_path = lambda: "selected-source"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                    class ClockId(Entity):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId, self).__init__()

                            self.yang_name = "clock-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                            ])
                            self.node = None
                            self.id = None
                            self.clock_name = None
                            self._segment_path = lambda: "clock-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                    class GnssReceiverId(Entity):
                        """
                        GNSS Receiver ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, self).__init__()

                            self.yang_name = "gnss-receiver-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                            ])
                            self.node = None
                            self.id = None
                            self.clock_name = None
                            self._segment_path = lambda: "gnss-receiver-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                class SelectionPoint(Entity):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint, self).__init__()

                        self.yang_name = "selection-point"
                        self.yang_parent_name = "interface-selection-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ])
                        self.selection_point_type = None
                        self.selection_point_description = None
                        self.node = None
                        self._segment_path = lambda: "selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


    class Summary(Entity):
        """
        Summary operational data
        
        .. attribute:: frequency_summary
        
        	Summary of sources selected for frequency
        	**type**\: list of  		 :py:class:`FrequencySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary>`
        
        .. attribute:: time_of_day_summary
        
        	Summary of sources selected for time\-of\-day
        	**type**\: list of  		 :py:class:`TimeOfDaySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            super(FrequencySynchronization.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("frequency-summary", ("frequency_summary", FrequencySynchronization.Summary.FrequencySummary)), ("time-of-day-summary", ("time_of_day_summary", FrequencySynchronization.Summary.TimeOfDaySummary))])
            self._leafs = OrderedDict()

            self.frequency_summary = YList(self)
            self.time_of_day_summary = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.Summary, [], name, value)


        class FrequencySummary(Entity):
            """
            Summary of sources selected for frequency
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source>`
            
            .. attribute:: clock_count
            
            	The number of clock\-interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ethernet_count
            
            	The number of Ethernet interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonet_count
            
            	The number of SONET/SDH interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.Summary.FrequencySummary, self).__init__()

                self.yang_name = "frequency-summary"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.Summary.FrequencySummary.Source))])
                self._leafs = OrderedDict([
                    ('clock_count', (YLeaf(YType.uint32, 'clock-count'), ['int'])),
                    ('ethernet_count', (YLeaf(YType.uint32, 'ethernet-count'), ['int'])),
                    ('sonet_count', (YLeaf(YType.uint32, 'sonet-count'), ['int'])),
                ])
                self.clock_count = None
                self.ethernet_count = None
                self.sonet_count = None

                self.source = FrequencySynchronization.Summary.FrequencySummary.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"
                self._segment_path = lambda: "frequency-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary, [u'clock_count', u'ethernet_count', u'sonet_count'], name, value)


            class Source(Entity):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.ClockId>`
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Summary.FrequencySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "frequency-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Summary.FrequencySummary.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.node = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.Summary.FrequencySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.FrequencySummary.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                class GnssReceiverId(Entity):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId, self).__init__()

                        self.yang_name = "gnss-receiver-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "gnss-receiver-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


        class TimeOfDaySummary(Entity):
            """
            Summary of sources selected for time\-of\-day
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source>`
            
            .. attribute:: node_count
            
            	The number of cards having their time\-of\-day set by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.Summary.TimeOfDaySummary, self).__init__()

                self.yang_name = "time-of-day-summary"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.Summary.TimeOfDaySummary.Source))])
                self._leafs = OrderedDict([
                    ('node_count', (YLeaf(YType.uint32, 'node-count'), ['int'])),
                ])
                self.node_count = None

                self.source = FrequencySynchronization.Summary.TimeOfDaySummary.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"
                self._segment_path = lambda: "time-of-day-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary, [u'node_count'], name, value)


            class Source(Entity):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId>`
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Summary.TimeOfDaySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "time-of-day-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.node = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                class GnssReceiverId(Entity):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId, self).__init__()

                        self.yang_name = "gnss-receiver-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "gnss-receiver-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


    class InterfaceDatas(Entity):
        """
        Table for interface operational data
        
        .. attribute:: interface_data
        
        	Operational data for a particular interface
        	**type**\: list of  		 :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            super(FrequencySynchronization.InterfaceDatas, self).__init__()

            self.yang_name = "interface-datas"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-data", ("interface_data", FrequencySynchronization.InterfaceDatas.InterfaceData))])
            self._leafs = OrderedDict()

            self.interface_data = YList(self)
            self._segment_path = lambda: "interface-datas"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.InterfaceDatas, [], name, value)


        class InterfaceData(Entity):
            """
            Operational data for a particular interface
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: source
            
            	The source ID for the interface
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source>`
            
            .. attribute:: selected_source
            
            	Timing source selected for interface output
            	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource>`
            
            .. attribute:: quality_level_received
            
            	Received quality level
            	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived>`
            
            .. attribute:: quality_level_damped
            
            	Quality level after damping has been applied
            	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped>`
            
            .. attribute:: quality_level_effective_input
            
            	The effective input quality level
            	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput>`
            
            .. attribute:: quality_level_effective_output
            
            	The effective output quality level
            	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput>`
            
            .. attribute:: quality_level_selected_source
            
            	The quality level of the source driving this interface
            	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource>`
            
            .. attribute:: ethernet_peer_information
            
            	Ethernet peer information
            	**type**\:  :py:class:`EthernetPeerInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation>`
            
            .. attribute:: esmc_statistics
            
            	ESMC Statistics
            	**type**\:  :py:class:`EsmcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics>`
            
            .. attribute:: name
            
            	Interface name
            	**type**\: str
            
            .. attribute:: state
            
            	Interface state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.ImStateEnum>`
            
            .. attribute:: ssm_enabled
            
            	SSM is enabled on the interface
            	**type**\: bool
            
            .. attribute:: squelched
            
            	The interface output is squelched
            	**type**\: bool
            
            .. attribute:: selection_input
            
            	The interface is an input for selection
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: time_of_day_priority
            
            	Time\-of\-day priority
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: damping_state
            
            	Damping state
            	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
            
            .. attribute:: damping_time
            
            	Time until damping state changes in ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: wait_to_restore_time
            
            	Wait\-to\-restore time for the interface
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: supports_frequency
            
            	The PTP clock supports frequency
            	**type**\: bool
            
            .. attribute:: supports_time_of_day
            
            	The PTP clock supports time
            	**type**\: bool
            
            .. attribute:: spa_selection_point
            
            	Spa selection points
            	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint>`
            
            .. attribute:: node_selection_point
            
            	Node selection points
            	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.InterfaceDatas.InterfaceData, self).__init__()

                self.yang_name = "interface-data"
                self.yang_parent_name = "interface-datas"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.InterfaceDatas.InterfaceData.Source)), ("selected-source", ("selected_source", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource)), ("quality-level-received", ("quality_level_received", FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived)), ("quality-level-damped", ("quality_level_damped", FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped)), ("quality-level-effective-input", ("quality_level_effective_input", FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput)), ("quality-level-effective-output", ("quality_level_effective_output", FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput)), ("quality-level-selected-source", ("quality_level_selected_source", FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource)), ("ethernet-peer-information", ("ethernet_peer_information", FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation)), ("esmc-statistics", ("esmc_statistics", FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics)), ("spa-selection-point", ("spa_selection_point", FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'ImStateEnum', '')])),
                    ('ssm_enabled', (YLeaf(YType.boolean, 'ssm-enabled'), ['bool'])),
                    ('squelched', (YLeaf(YType.boolean, 'squelched'), ['bool'])),
                    ('selection_input', (YLeaf(YType.boolean, 'selection-input'), ['bool'])),
                    ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                    ('damping_state', (YLeaf(YType.enumeration, 'damping-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagDampingState', '')])),
                    ('damping_time', (YLeaf(YType.uint32, 'damping-time'), ['int'])),
                    ('wait_to_restore_time', (YLeaf(YType.uint16, 'wait-to-restore-time'), ['int'])),
                    ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                    ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                ])
                self.interface_name = None
                self.name = None
                self.state = None
                self.ssm_enabled = None
                self.squelched = None
                self.selection_input = None
                self.priority = None
                self.time_of_day_priority = None
                self.damping_state = None
                self.damping_time = None
                self.wait_to_restore_time = None
                self.supports_frequency = None
                self.supports_time_of_day = None

                self.source = FrequencySynchronization.InterfaceDatas.InterfaceData.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"

                self.selected_source = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource()
                self.selected_source.parent = self
                self._children_name_map["selected_source"] = "selected-source"

                self.quality_level_received = FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived()
                self.quality_level_received.parent = self
                self._children_name_map["quality_level_received"] = "quality-level-received"

                self.quality_level_damped = FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped()
                self.quality_level_damped.parent = self
                self._children_name_map["quality_level_damped"] = "quality-level-damped"

                self.quality_level_effective_input = FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput()
                self.quality_level_effective_input.parent = self
                self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"

                self.quality_level_effective_output = FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput()
                self.quality_level_effective_output.parent = self
                self._children_name_map["quality_level_effective_output"] = "quality-level-effective-output"

                self.quality_level_selected_source = FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource()
                self.quality_level_selected_source.parent = self
                self._children_name_map["quality_level_selected_source"] = "quality-level-selected-source"

                self.ethernet_peer_information = FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation()
                self.ethernet_peer_information.parent = self
                self._children_name_map["ethernet_peer_information"] = "ethernet-peer-information"

                self.esmc_statistics = FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics()
                self.esmc_statistics.parent = self
                self._children_name_map["esmc_statistics"] = "esmc-statistics"

                self.spa_selection_point = YList(self)
                self.node_selection_point = YList(self)
                self._segment_path = lambda: "interface-data" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/interface-datas/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData, ['interface_name', u'name', u'state', u'ssm_enabled', u'squelched', u'selection_input', u'priority', u'time_of_day_priority', u'damping_state', u'damping_time', u'wait_to_restore_time', u'supports_frequency', u'supports_time_of_day'], name, value)


            class Source(Entity):
                """
                The source ID for the interface
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId>`
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.node = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "clock-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                class GnssReceiverId(Entity):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId, self).__init__()

                        self.yang_name = "gnss-receiver-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "gnss-receiver-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


            class SelectedSource(Entity):
                """
                Timing source selected for interface output
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId>`
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource, self).__init__()

                    self.yang_name = "selected-source"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.node = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "selected-source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "selected-source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "clock-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                class GnssReceiverId(Entity):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId, self).__init__()

                        self.yang_name = "gnss-receiver-id"
                        self.yang_parent_name = "selected-source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                        ])
                        self.node = None
                        self.id = None
                        self.clock_name = None
                        self._segment_path = lambda: "gnss-receiver-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


            class QualityLevelReceived(Entity):
                """
                Received quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived, self).__init__()

                    self.yang_name = "quality-level-received"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                        ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                        ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                        ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                    ])
                    self.quality_level_option = None
                    self.option1_value = None
                    self.option2_generation1_value = None
                    self.option2_generation2_value = None
                    self._segment_path = lambda: "quality-level-received"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class QualityLevelDamped(Entity):
                """
                Quality level after damping has been applied
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped, self).__init__()

                    self.yang_name = "quality-level-damped"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                        ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                        ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                        ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                    ])
                    self.quality_level_option = None
                    self.option1_value = None
                    self.option2_generation1_value = None
                    self.option2_generation2_value = None
                    self._segment_path = lambda: "quality-level-damped"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class QualityLevelEffectiveInput(Entity):
                """
                The effective input quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput, self).__init__()

                    self.yang_name = "quality-level-effective-input"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                        ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                        ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                        ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                    ])
                    self.quality_level_option = None
                    self.option1_value = None
                    self.option2_generation1_value = None
                    self.option2_generation2_value = None
                    self._segment_path = lambda: "quality-level-effective-input"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class QualityLevelEffectiveOutput(Entity):
                """
                The effective output quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput, self).__init__()

                    self.yang_name = "quality-level-effective-output"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                        ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                        ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                        ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                    ])
                    self.quality_level_option = None
                    self.option1_value = None
                    self.option2_generation1_value = None
                    self.option2_generation2_value = None
                    self._segment_path = lambda: "quality-level-effective-output"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class QualityLevelSelectedSource(Entity):
                """
                The quality level of the source driving this
                interface
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource, self).__init__()

                    self.yang_name = "quality-level-selected-source"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                        ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                        ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                        ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                    ])
                    self.quality_level_option = None
                    self.option1_value = None
                    self.option2_generation1_value = None
                    self.option2_generation2_value = None
                    self._segment_path = lambda: "quality-level-selected-source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class EthernetPeerInformation(Entity):
                """
                Ethernet peer information
                
                .. attribute:: peer_state_time
                
                	Time of last peer state transition
                	**type**\:  :py:class:`PeerStateTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime>`
                
                .. attribute:: last_ssm
                
                	Time of last SSM received
                	**type**\:  :py:class:`LastSsm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm>`
                
                .. attribute:: peer_state
                
                	Peer state
                	**type**\:  :py:class:`FsyncBagEsmcPeerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagEsmcPeerState>`
                
                .. attribute:: peer_up_count
                
                	Number of times the peer has come up
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: peer_timeout_count
                
                	Number of times the peer has timed out
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation, self).__init__()

                    self.yang_name = "ethernet-peer-information"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-state-time", ("peer_state_time", FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime)), ("last-ssm", ("last_ssm", FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm))])
                    self._leafs = OrderedDict([
                        ('peer_state', (YLeaf(YType.enumeration, 'peer-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagEsmcPeerState', '')])),
                        ('peer_up_count', (YLeaf(YType.uint16, 'peer-up-count'), ['int'])),
                        ('peer_timeout_count', (YLeaf(YType.uint16, 'peer-timeout-count'), ['int'])),
                    ])
                    self.peer_state = None
                    self.peer_up_count = None
                    self.peer_timeout_count = None

                    self.peer_state_time = FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime()
                    self.peer_state_time.parent = self
                    self._children_name_map["peer_state_time"] = "peer-state-time"

                    self.last_ssm = FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm()
                    self.last_ssm.parent = self
                    self._children_name_map["last_ssm"] = "last-ssm"
                    self._segment_path = lambda: "ethernet-peer-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation, [u'peer_state', u'peer_up_count', u'peer_timeout_count'], name, value)


                class PeerStateTime(Entity):
                    """
                    Time of last peer state transition
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime, self).__init__()

                        self.yang_name = "peer-state-time"
                        self.yang_parent_name = "ethernet-peer-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "peer-state-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime, [u'seconds', u'nanoseconds'], name, value)


                class LastSsm(Entity):
                    """
                    Time of last SSM received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm, self).__init__()

                        self.yang_name = "last-ssm"
                        self.yang_parent_name = "ethernet-peer-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "last-ssm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm, [u'seconds', u'nanoseconds'], name, value)


            class EsmcStatistics(Entity):
                """
                ESMC Statistics
                
                .. attribute:: esmc_events_sent
                
                	Number of event SSMs sent
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_events_received
                
                	Number of event SSMs received
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_infos_sent
                
                	Number of info SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_infos_received
                
                	Number of info SSms received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_dn_us_sent
                
                	Number of SSMs with DNU QL sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_dn_us_received
                
                	Number of SSMs with DNU QL received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_malformed_received
                
                	Number of malformed packets received
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_received_error
                
                	Number of received packets that failed to be handled
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics, self).__init__()

                    self.yang_name = "esmc-statistics"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('esmc_events_sent', (YLeaf(YType.uint16, 'esmc-events-sent'), ['int'])),
                        ('esmc_events_received', (YLeaf(YType.uint16, 'esmc-events-received'), ['int'])),
                        ('esmc_infos_sent', (YLeaf(YType.uint32, 'esmc-infos-sent'), ['int'])),
                        ('esmc_infos_received', (YLeaf(YType.uint32, 'esmc-infos-received'), ['int'])),
                        ('esmc_dn_us_sent', (YLeaf(YType.uint32, 'esmc-dn-us-sent'), ['int'])),
                        ('esmc_dn_us_received', (YLeaf(YType.uint32, 'esmc-dn-us-received'), ['int'])),
                        ('esmc_malformed_received', (YLeaf(YType.uint16, 'esmc-malformed-received'), ['int'])),
                        ('esmc_received_error', (YLeaf(YType.uint16, 'esmc-received-error'), ['int'])),
                    ])
                    self.esmc_events_sent = None
                    self.esmc_events_received = None
                    self.esmc_infos_sent = None
                    self.esmc_infos_received = None
                    self.esmc_dn_us_sent = None
                    self.esmc_dn_us_received = None
                    self.esmc_malformed_received = None
                    self.esmc_received_error = None
                    self._segment_path = lambda: "esmc-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics, [u'esmc_events_sent', u'esmc_events_received', u'esmc_infos_sent', u'esmc_infos_received', u'esmc_dn_us_sent', u'esmc_dn_us_received', u'esmc_malformed_received', u'esmc_received_error'], name, value)


            class SpaSelectionPoint(Entity):
                """
                Spa selection points
                
                .. attribute:: selection_point
                
                	Selection point ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: selection_point_description
                
                	Selection point description
                	**type**\: str
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint, self).__init__()

                    self.yang_name = "spa-selection-point"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                        ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                    ])
                    self.selection_point = None
                    self.selection_point_description = None
                    self._segment_path = lambda: "spa-selection-point"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


            class NodeSelectionPoint(Entity):
                """
                Node selection points
                
                .. attribute:: selection_point
                
                	Selection point ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: selection_point_description
                
                	Selection point description
                	**type**\: str
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint, self).__init__()

                    self.yang_name = "node-selection-point"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                        ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                    ])
                    self.selection_point = None
                    self.selection_point_description = None
                    self._segment_path = lambda: "node-selection-point"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


    class Nodes(Entity):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            super(FrequencySynchronization.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", FrequencySynchronization.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ntp_data
            
            	NTP operational data
            	**type**\:  :py:class:`NtpData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData>`
            
            .. attribute:: selection_point_datas
            
            	Selection point data table
            	**type**\:  :py:class:`SelectionPointDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas>`
            
            .. attribute:: configuration_errors
            
            	Configuration error operational data
            	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors>`
            
            .. attribute:: ptp_data
            
            	PTP operational data
            	**type**\:  :py:class:`PtpData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData>`
            
            .. attribute:: ssm_summary
            
            	SSM operational data
            	**type**\:  :py:class:`SsmSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SsmSummary>`
            
            .. attribute:: detailed_clock_datas
            
            	Table for detailed clock operational data
            	**type**\:  :py:class:`DetailedClockDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas>`
            
            .. attribute:: clock_datas
            
            	Table for clock operational data
            	**type**\:  :py:class:`ClockDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas>`
            
            .. attribute:: selection_point_inputs
            
            	Table for selection point input operational data
            	**type**\:  :py:class:`SelectionPointInputs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                super(FrequencySynchronization.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("ntp-data", ("ntp_data", FrequencySynchronization.Nodes.Node.NtpData)), ("selection-point-datas", ("selection_point_datas", FrequencySynchronization.Nodes.Node.SelectionPointDatas)), ("configuration-errors", ("configuration_errors", FrequencySynchronization.Nodes.Node.ConfigurationErrors)), ("ptp-data", ("ptp_data", FrequencySynchronization.Nodes.Node.PtpData)), ("ssm-summary", ("ssm_summary", FrequencySynchronization.Nodes.Node.SsmSummary)), ("detailed-clock-datas", ("detailed_clock_datas", FrequencySynchronization.Nodes.Node.DetailedClockDatas)), ("clock-datas", ("clock_datas", FrequencySynchronization.Nodes.Node.ClockDatas)), ("selection-point-inputs", ("selection_point_inputs", FrequencySynchronization.Nodes.Node.SelectionPointInputs))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.ntp_data = FrequencySynchronization.Nodes.Node.NtpData()
                self.ntp_data.parent = self
                self._children_name_map["ntp_data"] = "ntp-data"

                self.selection_point_datas = FrequencySynchronization.Nodes.Node.SelectionPointDatas()
                self.selection_point_datas.parent = self
                self._children_name_map["selection_point_datas"] = "selection-point-datas"

                self.configuration_errors = FrequencySynchronization.Nodes.Node.ConfigurationErrors()
                self.configuration_errors.parent = self
                self._children_name_map["configuration_errors"] = "configuration-errors"

                self.ptp_data = FrequencySynchronization.Nodes.Node.PtpData()
                self.ptp_data.parent = self
                self._children_name_map["ptp_data"] = "ptp-data"

                self.ssm_summary = FrequencySynchronization.Nodes.Node.SsmSummary()
                self.ssm_summary.parent = self
                self._children_name_map["ssm_summary"] = "ssm-summary"

                self.detailed_clock_datas = FrequencySynchronization.Nodes.Node.DetailedClockDatas()
                self.detailed_clock_datas.parent = self
                self._children_name_map["detailed_clock_datas"] = "detailed-clock-datas"

                self.clock_datas = FrequencySynchronization.Nodes.Node.ClockDatas()
                self.clock_datas.parent = self
                self._children_name_map["clock_datas"] = "clock-datas"

                self.selection_point_inputs = FrequencySynchronization.Nodes.Node.SelectionPointInputs()
                self.selection_point_inputs.parent = self
                self._children_name_map["selection_point_inputs"] = "selection-point-inputs"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Nodes.Node, ['node'], name, value)


            class NtpData(Entity):
                """
                NTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput>`
                
                .. attribute:: state
                
                	NTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                .. attribute:: supports_frequency
                
                	The NTP clock supports frequency
                	**type**\: bool
                
                .. attribute:: supports_time_of_day
                
                	The NTP clock supports time
                	**type**\: bool
                
                .. attribute:: frequency_priority
                
                	The priority of the NTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: time_of_day_priority
                
                	The priority of the NTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint>`
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.NtpData, self).__init__()

                    self.yang_name = "ntp-data"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("quality-level-effective-input", ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput)), ("spa-selection-point", ("spa_selection_point", FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint))])
                    self._leafs = OrderedDict([
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceState', '')])),
                        ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                        ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                        ('frequency_priority', (YLeaf(YType.uint8, 'frequency-priority'), ['int'])),
                        ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                    ])
                    self.state = None
                    self.supports_frequency = None
                    self.supports_time_of_day = None
                    self.frequency_priority = None
                    self.time_of_day_priority = None

                    self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput()
                    self.quality_level_effective_input.parent = self
                    self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"

                    self.spa_selection_point = YList(self)
                    self.node_selection_point = YList(self)
                    self._segment_path = lambda: "ntp-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData, [u'state', u'supports_frequency', u'supports_time_of_day', u'frequency_priority', u'time_of_day_priority'], name, value)


                class QualityLevelEffectiveInput(Entity):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput, self).__init__()

                        self.yang_name = "quality-level-effective-input"
                        self.yang_parent_name = "ntp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                            ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                            ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                            ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                        ])
                        self.quality_level_option = None
                        self.option1_value = None
                        self.option2_generation1_value = None
                        self.option2_generation2_value = None
                        self._segment_path = lambda: "quality-level-effective-input"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                class SpaSelectionPoint(Entity):
                    """
                    Spa selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint, self).__init__()

                        self.yang_name = "spa-selection-point"
                        self.yang_parent_name = "ntp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                        ])
                        self.selection_point = None
                        self.selection_point_description = None
                        self._segment_path = lambda: "spa-selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                class NodeSelectionPoint(Entity):
                    """
                    Node selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint, self).__init__()

                        self.yang_name = "node-selection-point"
                        self.yang_parent_name = "ntp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                        ])
                        self.selection_point = None
                        self.selection_point_description = None
                        self._segment_path = lambda: "node-selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


            class SelectionPointDatas(Entity):
                """
                Selection point data table
                
                .. attribute:: selection_point_data
                
                	Operational data for a given selection point
                	**type**\: list of  		 :py:class:`SelectionPointData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SelectionPointDatas, self).__init__()

                    self.yang_name = "selection-point-datas"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("selection-point-data", ("selection_point_data", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData))])
                    self._leafs = OrderedDict()

                    self.selection_point_data = YList(self)
                    self._segment_path = lambda: "selection-point-datas"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas, [], name, value)


                class SelectionPointData(Entity):
                    """
                    Operational data for a given selection point
                    
                    .. attribute:: selection_point  (key)
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output
                    
                    	Information about the output of the selection point
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output>`
                    
                    .. attribute:: last_programmed
                    
                    	Time the SP was last programmed
                    	**type**\:  :py:class:`LastProgrammed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed>`
                    
                    .. attribute:: last_selection
                    
                    	Time the last selection was made
                    	**type**\:  :py:class:`LastSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection>`
                    
                    .. attribute:: selection_point_type
                    
                    	Selection Point Type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: description
                    
                    	Description
                    	**type**\: str
                    
                    .. attribute:: inputs
                    
                    	Number of inputs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inputs_selected
                    
                    	Number of inputs that are selected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_of_day_selection
                    
                    	The selection point is a time\-of\-day selection point
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData, self).__init__()

                        self.yang_name = "selection-point-data"
                        self.yang_parent_name = "selection-point-datas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['selection_point']
                        self._child_classes = OrderedDict([("output", ("output", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output)), ("last-programmed", ("last_programmed", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed)), ("last-selection", ("last_selection", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection))])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint32, 'selection-point'), ['int'])),
                            ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('inputs', (YLeaf(YType.uint32, 'inputs'), ['int'])),
                            ('inputs_selected', (YLeaf(YType.uint32, 'inputs-selected'), ['int'])),
                            ('time_of_day_selection', (YLeaf(YType.boolean, 'time-of-day-selection'), ['bool'])),
                        ])
                        self.selection_point = None
                        self.selection_point_type = None
                        self.description = None
                        self.inputs = None
                        self.inputs_selected = None
                        self.time_of_day_selection = None

                        self.output = FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"

                        self.last_programmed = FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed()
                        self.last_programmed.parent = self
                        self._children_name_map["last_programmed"] = "last-programmed"

                        self.last_selection = FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection()
                        self.last_selection.parent = self
                        self._children_name_map["last_selection"] = "last-selection"
                        self._segment_path = lambda: "selection-point-data" + "[selection-point='" + str(self.selection_point) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData, ['selection_point', u'selection_point_type', u'description', u'inputs', u'inputs_selected', u'time_of_day_selection'], name, value)


                    class Output(Entity):
                        """
                        Information about the output of the selection
                        point
                        
                        .. attribute:: local_clock_ouput
                        
                        	Used for local clock output
                        	**type**\: bool
                        
                        .. attribute:: local_line_output
                        
                        	Used for local line interface output
                        	**type**\: bool
                        
                        .. attribute:: local_time_of_day_output
                        
                        	Used for local time\-of\-day output
                        	**type**\: bool
                        
                        .. attribute:: spa_selection_point
                        
                        	SPA selection points
                        	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint>`
                        
                        .. attribute:: node_selection_point
                        
                        	Node selection points
                        	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint>`
                        
                        .. attribute:: chassis_selection_point
                        
                        	Chassis selection points
                        	**type**\: list of  		 :py:class:`ChassisSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint>`
                        
                        .. attribute:: router_selection_point
                        
                        	Router selection points
                        	**type**\: list of  		 :py:class:`RouterSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "selection-point-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spa-selection-point", ("spa_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint)), ("chassis-selection-point", ("chassis_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint)), ("router-selection-point", ("router_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint))])
                            self._leafs = OrderedDict([
                                ('local_clock_ouput', (YLeaf(YType.boolean, 'local-clock-ouput'), ['bool'])),
                                ('local_line_output', (YLeaf(YType.boolean, 'local-line-output'), ['bool'])),
                                ('local_time_of_day_output', (YLeaf(YType.boolean, 'local-time-of-day-output'), ['bool'])),
                            ])
                            self.local_clock_ouput = None
                            self.local_line_output = None
                            self.local_time_of_day_output = None

                            self.spa_selection_point = YList(self)
                            self.node_selection_point = YList(self)
                            self.chassis_selection_point = YList(self)
                            self.router_selection_point = YList(self)
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output, [u'local_clock_ouput', u'local_line_output', u'local_time_of_day_output'], name, value)


                        class SpaSelectionPoint(Entity):
                            """
                            SPA selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint, self).__init__()

                                self.yang_name = "spa-selection-point"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ])
                                self.selection_point = None
                                self.selection_point_description = None
                                self._segment_path = lambda: "spa-selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                        class NodeSelectionPoint(Entity):
                            """
                            Node selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint, self).__init__()

                                self.yang_name = "node-selection-point"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ])
                                self.selection_point = None
                                self.selection_point_description = None
                                self._segment_path = lambda: "node-selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                        class ChassisSelectionPoint(Entity):
                            """
                            Chassis selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint, self).__init__()

                                self.yang_name = "chassis-selection-point"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ])
                                self.selection_point = None
                                self.selection_point_description = None
                                self._segment_path = lambda: "chassis-selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                        class RouterSelectionPoint(Entity):
                            """
                            Router selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint, self).__init__()

                                self.yang_name = "router-selection-point"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                    ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ])
                                self.selection_point = None
                                self.selection_point_description = None
                                self._segment_path = lambda: "router-selection-point"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                    class LastProgrammed(Entity):
                        """
                        Time the SP was last programmed
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed, self).__init__()

                            self.yang_name = "last-programmed"
                            self.yang_parent_name = "selection-point-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "last-programmed"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed, [u'seconds', u'nanoseconds'], name, value)


                    class LastSelection(Entity):
                        """
                        Time the last selection was made
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection, self).__init__()

                            self.yang_name = "last-selection"
                            self.yang_parent_name = "selection-point-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "last-selection"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection, [u'seconds', u'nanoseconds'], name, value)


            class ConfigurationErrors(Entity):
                """
                Configuration error operational data
                
                .. attribute:: error_source
                
                	Configuration errors
                	**type**\: list of  		 :py:class:`ErrorSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.ConfigurationErrors, self).__init__()

                    self.yang_name = "configuration-errors"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("error-source", ("error_source", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource))])
                    self._leafs = OrderedDict()

                    self.error_source = YList(self)
                    self._segment_path = lambda: "configuration-errors"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors, [], name, value)


                class ErrorSource(Entity):
                    """
                    Configuration errors
                    
                    .. attribute:: source
                    
                    	Source
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source>`
                    
                    .. attribute:: input_min_ql
                    
                    	Configured minimum input QL
                    	**type**\:  :py:class:`InputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl>`
                    
                    .. attribute:: input_exact_ql
                    
                    	Configured exact input QL
                    	**type**\:  :py:class:`InputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl>`
                    
                    .. attribute:: input_max_ql
                    
                    	Configured maximum input QL
                    	**type**\:  :py:class:`InputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl>`
                    
                    .. attribute:: output_min_ql
                    
                    	Configured mininum output QL
                    	**type**\:  :py:class:`OutputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl>`
                    
                    .. attribute:: output_exact_ql
                    
                    	Configured exact output QL
                    	**type**\:  :py:class:`OutputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl>`
                    
                    .. attribute:: output_max_ql
                    
                    	Configured exact maximum QL
                    	**type**\:  :py:class:`OutputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl>`
                    
                    .. attribute:: enable_error
                    
                    	Frequency Synchronization enable error
                    	**type**\: bool
                    
                    .. attribute:: input_min_error
                    
                    	Minimum input QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_exact_error
                    
                    	Exact input QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_max_error
                    
                    	Maximum input Ql config error
                    	**type**\: bool
                    
                    .. attribute:: ouput_min_error
                    
                    	Minimum output QL config error
                    	**type**\: bool
                    
                    .. attribute:: output_exact_error
                    
                    	Exact output QL config error
                    	**type**\: bool
                    
                    .. attribute:: output_max_error
                    
                    	Maximum output QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_output_mismatch
                    
                    	Input/Output mismatch error
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource, self).__init__()

                        self.yang_name = "error-source"
                        self.yang_parent_name = "configuration-errors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source)), ("input-min-ql", ("input_min_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl)), ("input-exact-ql", ("input_exact_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl)), ("input-max-ql", ("input_max_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl)), ("output-min-ql", ("output_min_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl)), ("output-exact-ql", ("output_exact_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl)), ("output-max-ql", ("output_max_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl))])
                        self._leafs = OrderedDict([
                            ('enable_error', (YLeaf(YType.boolean, 'enable-error'), ['bool'])),
                            ('input_min_error', (YLeaf(YType.boolean, 'input-min-error'), ['bool'])),
                            ('input_exact_error', (YLeaf(YType.boolean, 'input-exact-error'), ['bool'])),
                            ('input_max_error', (YLeaf(YType.boolean, 'input-max-error'), ['bool'])),
                            ('ouput_min_error', (YLeaf(YType.boolean, 'ouput-min-error'), ['bool'])),
                            ('output_exact_error', (YLeaf(YType.boolean, 'output-exact-error'), ['bool'])),
                            ('output_max_error', (YLeaf(YType.boolean, 'output-max-error'), ['bool'])),
                            ('input_output_mismatch', (YLeaf(YType.boolean, 'input-output-mismatch'), ['bool'])),
                        ])
                        self.enable_error = None
                        self.input_min_error = None
                        self.input_exact_error = None
                        self.input_max_error = None
                        self.ouput_min_error = None
                        self.output_exact_error = None
                        self.output_max_error = None
                        self.input_output_mismatch = None

                        self.source = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"

                        self.input_min_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl()
                        self.input_min_ql.parent = self
                        self._children_name_map["input_min_ql"] = "input-min-ql"

                        self.input_exact_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl()
                        self.input_exact_ql.parent = self
                        self._children_name_map["input_exact_ql"] = "input-exact-ql"

                        self.input_max_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl()
                        self.input_max_ql.parent = self
                        self._children_name_map["input_max_ql"] = "input-max-ql"

                        self.output_min_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl()
                        self.output_min_ql.parent = self
                        self._children_name_map["output_min_ql"] = "output-min-ql"

                        self.output_exact_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl()
                        self.output_exact_ql.parent = self
                        self._children_name_map["output_exact_ql"] = "output-exact-ql"

                        self.output_max_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl()
                        self.output_max_ql.parent = self
                        self._children_name_map["output_max_ql"] = "output-max-ql"
                        self._segment_path = lambda: "error-source"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource, [u'enable_error', u'input_min_error', u'input_exact_error', u'input_max_error', u'ouput_min_error', u'output_exact_error', u'output_max_error', u'input_output_mismatch'], name, value)


                    class Source(Entity):
                        """
                        Source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class InputMinQl(Entity):
                        """
                        Configured minimum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl, self).__init__()

                            self.yang_name = "input-min-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "input-min-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class InputExactQl(Entity):
                        """
                        Configured exact input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl, self).__init__()

                            self.yang_name = "input-exact-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "input-exact-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class InputMaxQl(Entity):
                        """
                        Configured maximum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl, self).__init__()

                            self.yang_name = "input-max-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "input-max-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class OutputMinQl(Entity):
                        """
                        Configured mininum output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl, self).__init__()

                            self.yang_name = "output-min-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "output-min-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class OutputExactQl(Entity):
                        """
                        Configured exact output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl, self).__init__()

                            self.yang_name = "output-exact-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "output-exact-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class OutputMaxQl(Entity):
                        """
                        Configured exact maximum QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl, self).__init__()

                            self.yang_name = "output-max-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "output-max-ql"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


            class PtpData(Entity):
                """
                PTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput>`
                
                .. attribute:: state
                
                	PTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                .. attribute:: supports_frequency
                
                	The PTP clock supports frequency
                	**type**\: bool
                
                .. attribute:: supports_time_of_day
                
                	The PTP clock supports time
                	**type**\: bool
                
                .. attribute:: frequency_priority
                
                	The priority of the PTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: time_of_day_priority
                
                	The priority of the PTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint>`
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.PtpData, self).__init__()

                    self.yang_name = "ptp-data"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("quality-level-effective-input", ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput)), ("spa-selection-point", ("spa_selection_point", FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint))])
                    self._leafs = OrderedDict([
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceState', '')])),
                        ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                        ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                        ('frequency_priority', (YLeaf(YType.uint8, 'frequency-priority'), ['int'])),
                        ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                    ])
                    self.state = None
                    self.supports_frequency = None
                    self.supports_time_of_day = None
                    self.frequency_priority = None
                    self.time_of_day_priority = None

                    self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput()
                    self.quality_level_effective_input.parent = self
                    self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"

                    self.spa_selection_point = YList(self)
                    self.node_selection_point = YList(self)
                    self._segment_path = lambda: "ptp-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData, [u'state', u'supports_frequency', u'supports_time_of_day', u'frequency_priority', u'time_of_day_priority'], name, value)


                class QualityLevelEffectiveInput(Entity):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput, self).__init__()

                        self.yang_name = "quality-level-effective-input"
                        self.yang_parent_name = "ptp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                            ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                            ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                            ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                        ])
                        self.quality_level_option = None
                        self.option1_value = None
                        self.option2_generation1_value = None
                        self.option2_generation2_value = None
                        self._segment_path = lambda: "quality-level-effective-input"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                class SpaSelectionPoint(Entity):
                    """
                    Spa selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint, self).__init__()

                        self.yang_name = "spa-selection-point"
                        self.yang_parent_name = "ptp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                        ])
                        self.selection_point = None
                        self.selection_point_description = None
                        self._segment_path = lambda: "spa-selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                class NodeSelectionPoint(Entity):
                    """
                    Node selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint, self).__init__()

                        self.yang_name = "node-selection-point"
                        self.yang_parent_name = "ptp-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                            ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                        ])
                        self.selection_point = None
                        self.selection_point_description = None
                        self._segment_path = lambda: "node-selection-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


            class SsmSummary(Entity):
                """
                SSM operational data
                
                .. attribute:: ethernet_sources
                
                	Number of ethernet interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_sources_select
                
                	Number of ethernet interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_sources_enabled
                
                	Number of ethernet interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources
                
                	Number of SONET interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources_select
                
                	Number of SONET interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources_enabled
                
                	Number of SONET interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: events_sent
                
                	Total event SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: events_received
                
                	Total event SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: infos_sent
                
                	Total information SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: infos_received
                
                	Total information SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dn_us_sent
                
                	Total DNU SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dn_us_received
                
                	Total DNU SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SsmSummary, self).__init__()

                    self.yang_name = "ssm-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ethernet_sources', (YLeaf(YType.uint32, 'ethernet-sources'), ['int'])),
                        ('ethernet_sources_select', (YLeaf(YType.uint32, 'ethernet-sources-select'), ['int'])),
                        ('ethernet_sources_enabled', (YLeaf(YType.uint32, 'ethernet-sources-enabled'), ['int'])),
                        ('sonet_sources', (YLeaf(YType.uint32, 'sonet-sources'), ['int'])),
                        ('sonet_sources_select', (YLeaf(YType.uint32, 'sonet-sources-select'), ['int'])),
                        ('sonet_sources_enabled', (YLeaf(YType.uint32, 'sonet-sources-enabled'), ['int'])),
                        ('events_sent', (YLeaf(YType.uint32, 'events-sent'), ['int'])),
                        ('events_received', (YLeaf(YType.uint32, 'events-received'), ['int'])),
                        ('infos_sent', (YLeaf(YType.uint32, 'infos-sent'), ['int'])),
                        ('infos_received', (YLeaf(YType.uint32, 'infos-received'), ['int'])),
                        ('dn_us_sent', (YLeaf(YType.uint32, 'dn-us-sent'), ['int'])),
                        ('dn_us_received', (YLeaf(YType.uint32, 'dn-us-received'), ['int'])),
                    ])
                    self.ethernet_sources = None
                    self.ethernet_sources_select = None
                    self.ethernet_sources_enabled = None
                    self.sonet_sources = None
                    self.sonet_sources_select = None
                    self.sonet_sources_enabled = None
                    self.events_sent = None
                    self.events_received = None
                    self.infos_sent = None
                    self.infos_received = None
                    self.dn_us_sent = None
                    self.dn_us_received = None
                    self._segment_path = lambda: "ssm-summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SsmSummary, [u'ethernet_sources', u'ethernet_sources_select', u'ethernet_sources_enabled', u'sonet_sources', u'sonet_sources_select', u'sonet_sources_enabled', u'events_sent', u'events_received', u'infos_sent', u'infos_received', u'dn_us_sent', u'dn_us_received'], name, value)


            class DetailedClockDatas(Entity):
                """
                Table for detailed clock operational data
                
                .. attribute:: detailed_clock_data
                
                	Detailed operational data for a particular clock
                	**type**\: list of  		 :py:class:`DetailedClockData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.DetailedClockDatas, self).__init__()

                    self.yang_name = "detailed-clock-datas"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("detailed-clock-data", ("detailed_clock_data", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData))])
                    self._leafs = OrderedDict()

                    self.detailed_clock_data = YList(self)
                    self._segment_path = lambda: "detailed-clock-datas"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas, [], name, value)


                class DetailedClockData(Entity):
                    """
                    Detailed operational data for a particular
                    clock
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source
                    
                    	The source ID for the clock
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source>`
                    
                    .. attribute:: selected_source
                    
                    	Timing source selected for clock output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource>`
                    
                    .. attribute:: quality_level_received
                    
                    	Received quality level
                    	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived>`
                    
                    .. attribute:: quality_level_damped
                    
                    	Quality level after damping has been applied
                    	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped>`
                    
                    .. attribute:: quality_level_effective_input
                    
                    	The effective input quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput>`
                    
                    .. attribute:: quality_level_effective_output
                    
                    	The effective output quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput>`
                    
                    .. attribute:: quality_level_selected_source
                    
                    	The quality level of the source driving this interface
                    	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource>`
                    
                    .. attribute:: state
                    
                    	Clock state
                    	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                    
                    .. attribute:: down_reason
                    
                    	Why the clock is down
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	Clock description
                    	**type**\: str
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ssm_support
                    
                    	The clock supports SSMs
                    	**type**\: bool
                    
                    .. attribute:: ssm_enabled
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: loopback
                    
                    	The clock is looped back
                    	**type**\: bool
                    
                    .. attribute:: selection_input
                    
                    	The clock is an input for selection
                    	**type**\: bool
                    
                    .. attribute:: squelched
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: damping_state
                    
                    	Damping state
                    	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
                    
                    .. attribute:: damping_time
                    
                    	Time until damping state changes in ms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_disabled
                    
                    	Timing input is disabled
                    	**type**\: bool
                    
                    .. attribute:: output_disabled
                    
                    	Timing output is disabled
                    	**type**\: bool
                    
                    .. attribute:: wait_to_restore_time
                    
                    	Wait\-to\-restore time for the clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: clock_type_xr
                    
                    	The type of clock
                    	**type**\:  :py:class:`FsyncBagClockIntfClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagClockIntfClass>`
                    
                    .. attribute:: supports_frequency
                    
                    	The PTP clock supports frequency
                    	**type**\: bool
                    
                    .. attribute:: supports_time_of_day
                    
                    	The PTP clock supports time
                    	**type**\: bool
                    
                    .. attribute:: spa_selection_point
                    
                    	Spa selection points
                    	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint>`
                    
                    .. attribute:: node_selection_point
                    
                    	Node selection points
                    	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData, self).__init__()

                        self.yang_name = "detailed-clock-data"
                        self.yang_parent_name = "detailed-clock-datas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','id']
                        self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source)), ("selected-source", ("selected_source", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource)), ("quality-level-received", ("quality_level_received", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived)), ("quality-level-damped", ("quality_level_damped", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped)), ("quality-level-effective-input", ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput)), ("quality-level-effective-output", ("quality_level_effective_output", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput)), ("quality-level-selected-source", ("quality_level_selected_source", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource)), ("spa-selection-point", ("spa_selection_point", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceState', '')])),
                            ('down_reason', (YLeaf(YType.str, 'down-reason'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                            ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                            ('ssm_support', (YLeaf(YType.boolean, 'ssm-support'), ['bool'])),
                            ('ssm_enabled', (YLeaf(YType.boolean, 'ssm-enabled'), ['bool'])),
                            ('loopback', (YLeaf(YType.boolean, 'loopback'), ['bool'])),
                            ('selection_input', (YLeaf(YType.boolean, 'selection-input'), ['bool'])),
                            ('squelched', (YLeaf(YType.boolean, 'squelched'), ['bool'])),
                            ('damping_state', (YLeaf(YType.enumeration, 'damping-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagDampingState', '')])),
                            ('damping_time', (YLeaf(YType.uint32, 'damping-time'), ['int'])),
                            ('input_disabled', (YLeaf(YType.boolean, 'input-disabled'), ['bool'])),
                            ('output_disabled', (YLeaf(YType.boolean, 'output-disabled'), ['bool'])),
                            ('wait_to_restore_time', (YLeaf(YType.uint16, 'wait-to-restore-time'), ['int'])),
                            ('clock_type_xr', (YLeaf(YType.enumeration, 'clock-type-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagClockIntfClass', '')])),
                            ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                            ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                        ])
                        self.clock_type = None
                        self.id = None
                        self.state = None
                        self.down_reason = None
                        self.description = None
                        self.priority = None
                        self.time_of_day_priority = None
                        self.ssm_support = None
                        self.ssm_enabled = None
                        self.loopback = None
                        self.selection_input = None
                        self.squelched = None
                        self.damping_state = None
                        self.damping_time = None
                        self.input_disabled = None
                        self.output_disabled = None
                        self.wait_to_restore_time = None
                        self.clock_type_xr = None
                        self.supports_frequency = None
                        self.supports_time_of_day = None

                        self.source = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"

                        self.selected_source = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource()
                        self.selected_source.parent = self
                        self._children_name_map["selected_source"] = "selected-source"

                        self.quality_level_received = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived()
                        self.quality_level_received.parent = self
                        self._children_name_map["quality_level_received"] = "quality-level-received"

                        self.quality_level_damped = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped()
                        self.quality_level_damped.parent = self
                        self._children_name_map["quality_level_damped"] = "quality-level-damped"

                        self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput()
                        self.quality_level_effective_input.parent = self
                        self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"

                        self.quality_level_effective_output = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput()
                        self.quality_level_effective_output.parent = self
                        self._children_name_map["quality_level_effective_output"] = "quality-level-effective-output"

                        self.quality_level_selected_source = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource()
                        self.quality_level_selected_source.parent = self
                        self._children_name_map["quality_level_selected_source"] = "quality-level-selected-source"

                        self.spa_selection_point = YList(self)
                        self.node_selection_point = YList(self)
                        self._segment_path = lambda: "detailed-clock-data" + "[clock-type='" + str(self.clock_type) + "']" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData, ['clock_type', 'id', u'state', u'down_reason', u'description', u'priority', u'time_of_day_priority', u'ssm_support', u'ssm_enabled', u'loopback', u'selection_input', u'squelched', u'damping_state', u'damping_time', u'input_disabled', u'output_disabled', u'wait_to_restore_time', u'clock_type_xr', u'supports_frequency', u'supports_time_of_day'], name, value)


                    class Source(Entity):
                        """
                        The source ID for the clock
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class SelectedSource(Entity):
                        """
                        Timing source selected for clock output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class QualityLevelReceived(Entity):
                        """
                        Received quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived, self).__init__()

                            self.yang_name = "quality-level-received"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-received"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelDamped(Entity):
                        """
                        Quality level after damping has been applied
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped, self).__init__()

                            self.yang_name = "quality-level-damped"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-damped"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveInput(Entity):
                        """
                        The effective input quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput, self).__init__()

                            self.yang_name = "quality-level-effective-input"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-effective-input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveOutput(Entity):
                        """
                        The effective output quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput, self).__init__()

                            self.yang_name = "quality-level-effective-output"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-effective-output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelSelectedSource(Entity):
                        """
                        The quality level of the source driving this
                        interface
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource, self).__init__()

                            self.yang_name = "quality-level-selected-source"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class SpaSelectionPoint(Entity):
                        """
                        Spa selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint, self).__init__()

                            self.yang_name = "spa-selection-point"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ])
                            self.selection_point = None
                            self.selection_point_description = None
                            self._segment_path = lambda: "spa-selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                    class NodeSelectionPoint(Entity):
                        """
                        Node selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint, self).__init__()

                            self.yang_name = "node-selection-point"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ])
                            self.selection_point = None
                            self.selection_point_description = None
                            self._segment_path = lambda: "node-selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


            class ClockDatas(Entity):
                """
                Table for clock operational data
                
                .. attribute:: clock_data
                
                	Operational data for a particular clock
                	**type**\: list of  		 :py:class:`ClockData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.ClockDatas, self).__init__()

                    self.yang_name = "clock-datas"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-data", ("clock_data", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData))])
                    self._leafs = OrderedDict()

                    self.clock_data = YList(self)
                    self._segment_path = lambda: "clock-datas"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas, [], name, value)


                class ClockData(Entity):
                    """
                    Operational data for a particular clock
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source
                    
                    	The source ID for the clock
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source>`
                    
                    .. attribute:: selected_source
                    
                    	Timing source selected for clock output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource>`
                    
                    .. attribute:: quality_level_received
                    
                    	Received quality level
                    	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived>`
                    
                    .. attribute:: quality_level_damped
                    
                    	Quality level after damping has been applied
                    	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped>`
                    
                    .. attribute:: quality_level_effective_input
                    
                    	The effective input quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput>`
                    
                    .. attribute:: quality_level_effective_output
                    
                    	The effective output quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput>`
                    
                    .. attribute:: quality_level_selected_source
                    
                    	The quality level of the source driving this interface
                    	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource>`
                    
                    .. attribute:: state
                    
                    	Clock state
                    	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                    
                    .. attribute:: down_reason
                    
                    	Why the clock is down
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	Clock description
                    	**type**\: str
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ssm_support
                    
                    	The clock supports SSMs
                    	**type**\: bool
                    
                    .. attribute:: ssm_enabled
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: loopback
                    
                    	The clock is looped back
                    	**type**\: bool
                    
                    .. attribute:: selection_input
                    
                    	The clock is an input for selection
                    	**type**\: bool
                    
                    .. attribute:: squelched
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: damping_state
                    
                    	Damping state
                    	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
                    
                    .. attribute:: damping_time
                    
                    	Time until damping state changes in ms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_disabled
                    
                    	Timing input is disabled
                    	**type**\: bool
                    
                    .. attribute:: output_disabled
                    
                    	Timing output is disabled
                    	**type**\: bool
                    
                    .. attribute:: wait_to_restore_time
                    
                    	Wait\-to\-restore time for the clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: clock_type_xr
                    
                    	The type of clock
                    	**type**\:  :py:class:`FsyncBagClockIntfClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagClockIntfClass>`
                    
                    .. attribute:: supports_frequency
                    
                    	The PTP clock supports frequency
                    	**type**\: bool
                    
                    .. attribute:: supports_time_of_day
                    
                    	The PTP clock supports time
                    	**type**\: bool
                    
                    .. attribute:: spa_selection_point
                    
                    	Spa selection points
                    	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint>`
                    
                    .. attribute:: node_selection_point
                    
                    	Node selection points
                    	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData, self).__init__()

                        self.yang_name = "clock-data"
                        self.yang_parent_name = "clock-datas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','id']
                        self._child_classes = OrderedDict([("source", ("source", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source)), ("selected-source", ("selected_source", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource)), ("quality-level-received", ("quality_level_received", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived)), ("quality-level-damped", ("quality_level_damped", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped)), ("quality-level-effective-input", ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput)), ("quality-level-effective-output", ("quality_level_effective_output", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput)), ("quality-level-selected-source", ("quality_level_selected_source", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource)), ("spa-selection-point", ("spa_selection_point", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint)), ("node-selection-point", ("node_selection_point", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceState', '')])),
                            ('down_reason', (YLeaf(YType.str, 'down-reason'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                            ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                            ('ssm_support', (YLeaf(YType.boolean, 'ssm-support'), ['bool'])),
                            ('ssm_enabled', (YLeaf(YType.boolean, 'ssm-enabled'), ['bool'])),
                            ('loopback', (YLeaf(YType.boolean, 'loopback'), ['bool'])),
                            ('selection_input', (YLeaf(YType.boolean, 'selection-input'), ['bool'])),
                            ('squelched', (YLeaf(YType.boolean, 'squelched'), ['bool'])),
                            ('damping_state', (YLeaf(YType.enumeration, 'damping-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagDampingState', '')])),
                            ('damping_time', (YLeaf(YType.uint32, 'damping-time'), ['int'])),
                            ('input_disabled', (YLeaf(YType.boolean, 'input-disabled'), ['bool'])),
                            ('output_disabled', (YLeaf(YType.boolean, 'output-disabled'), ['bool'])),
                            ('wait_to_restore_time', (YLeaf(YType.uint16, 'wait-to-restore-time'), ['int'])),
                            ('clock_type_xr', (YLeaf(YType.enumeration, 'clock-type-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagClockIntfClass', '')])),
                            ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                            ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                        ])
                        self.clock_type = None
                        self.id = None
                        self.state = None
                        self.down_reason = None
                        self.description = None
                        self.priority = None
                        self.time_of_day_priority = None
                        self.ssm_support = None
                        self.ssm_enabled = None
                        self.loopback = None
                        self.selection_input = None
                        self.squelched = None
                        self.damping_state = None
                        self.damping_time = None
                        self.input_disabled = None
                        self.output_disabled = None
                        self.wait_to_restore_time = None
                        self.clock_type_xr = None
                        self.supports_frequency = None
                        self.supports_time_of_day = None

                        self.source = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"

                        self.selected_source = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource()
                        self.selected_source.parent = self
                        self._children_name_map["selected_source"] = "selected-source"

                        self.quality_level_received = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived()
                        self.quality_level_received.parent = self
                        self._children_name_map["quality_level_received"] = "quality-level-received"

                        self.quality_level_damped = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped()
                        self.quality_level_damped.parent = self
                        self._children_name_map["quality_level_damped"] = "quality-level-damped"

                        self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput()
                        self.quality_level_effective_input.parent = self
                        self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"

                        self.quality_level_effective_output = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput()
                        self.quality_level_effective_output.parent = self
                        self._children_name_map["quality_level_effective_output"] = "quality-level-effective-output"

                        self.quality_level_selected_source = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource()
                        self.quality_level_selected_source.parent = self
                        self._children_name_map["quality_level_selected_source"] = "quality-level-selected-source"

                        self.spa_selection_point = YList(self)
                        self.node_selection_point = YList(self)
                        self._segment_path = lambda: "clock-data" + "[clock-type='" + str(self.clock_type) + "']" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData, ['clock_type', 'id', u'state', u'down_reason', u'description', u'priority', u'time_of_day_priority', u'ssm_support', u'ssm_enabled', u'loopback', u'selection_input', u'squelched', u'damping_state', u'damping_time', u'input_disabled', u'output_disabled', u'wait_to_restore_time', u'clock_type_xr', u'supports_frequency', u'supports_time_of_day'], name, value)


                    class Source(Entity):
                        """
                        The source ID for the clock
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class SelectedSource(Entity):
                        """
                        Timing source selected for clock output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class QualityLevelReceived(Entity):
                        """
                        Received quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived, self).__init__()

                            self.yang_name = "quality-level-received"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-received"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelDamped(Entity):
                        """
                        Quality level after damping has been applied
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped, self).__init__()

                            self.yang_name = "quality-level-damped"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-damped"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveInput(Entity):
                        """
                        The effective input quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput, self).__init__()

                            self.yang_name = "quality-level-effective-input"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-effective-input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveOutput(Entity):
                        """
                        The effective output quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput, self).__init__()

                            self.yang_name = "quality-level-effective-output"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-effective-output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class QualityLevelSelectedSource(Entity):
                        """
                        The quality level of the source driving this
                        interface
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource, self).__init__()

                            self.yang_name = "quality-level-selected-source"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level-selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)


                    class SpaSelectionPoint(Entity):
                        """
                        Spa selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint, self).__init__()

                            self.yang_name = "spa-selection-point"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ])
                            self.selection_point = None
                            self.selection_point_description = None
                            self._segment_path = lambda: "spa-selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


                    class NodeSelectionPoint(Entity):
                        """
                        Node selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint, self).__init__()

                            self.yang_name = "node-selection-point"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point', (YLeaf(YType.uint8, 'selection-point'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                            ])
                            self.selection_point = None
                            self.selection_point_description = None
                            self._segment_path = lambda: "node-selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint, [u'selection_point', u'selection_point_description'], name, value)


            class SelectionPointInputs(Entity):
                """
                Table for selection point input operational
                data
                
                .. attribute:: selection_point_input
                
                	Operational data for a particular selection point input
                	**type**\: list of  		 :py:class:`SelectionPointInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs, self).__init__()

                    self.yang_name = "selection-point-inputs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("selection-point-input", ("selection_point_input", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput))])
                    self._leafs = OrderedDict()

                    self.selection_point_input = YList(self)
                    self._segment_path = lambda: "selection-point-inputs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs, [], name, value)


                class SelectionPointInput(Entity):
                    """
                    Operational data for a particular selection
                    point input
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stream_type
                    
                    	Type of stream
                    	**type**\:  :py:class:`FsyncStream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncStream>`
                    
                    .. attribute:: source_type
                    
                    	Type of source
                    	**type**\:  :py:class:`FsyncSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncSource>`
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: clock_port
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_node
                    
                    	Last node for a selection point stream
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: last_selection_point
                    
                    	Last selection point for a selection point stream
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_id
                    
                    	Output ID for a selection point stream
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_selection_point
                    
                    	The selection point the input is for
                    	**type**\:  :py:class:`InputSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint>`
                    
                    .. attribute:: stream
                    
                    	Stream
                    	**type**\:  :py:class:`Stream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream>`
                    
                    .. attribute:: original_source
                    
                    	Original source
                    	**type**\:  :py:class:`OriginalSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource>`
                    
                    .. attribute:: quality_level
                    
                    	Quality Level
                    	**type**\:  :py:class:`QualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel>`
                    
                    .. attribute:: supports_frequency
                    
                    	The selection point input supports frequency
                    	**type**\: bool
                    
                    .. attribute:: supports_time_of_day
                    
                    	The selection point input supports time\-of\-day
                    	**type**\: bool
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selected
                    
                    	The selection point input is selected
                    	**type**\: bool
                    
                    .. attribute:: output_id_xr
                    
                    	Platform output ID, if the input is selected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: platform_status
                    
                    	Platform status
                    	**type**\:  :py:class:`FsyncBagStreamState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamState>`
                    
                    .. attribute:: platform_failed_reason
                    
                    	Why the stream has failed
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput, self).__init__()

                        self.yang_name = "selection-point-input"
                        self.yang_parent_name = "selection-point-inputs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("input-selection-point", ("input_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint)), ("stream", ("stream", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream)), ("original-source", ("original_source", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource)), ("quality-level", ("quality_level", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel))])
                        self._leafs = OrderedDict([
                            ('selection_point', (YLeaf(YType.uint32, 'selection-point'), ['int'])),
                            ('stream_type', (YLeaf(YType.enumeration, 'stream-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncStream', '')])),
                            ('source_type', (YLeaf(YType.enumeration, 'source-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncSource', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('clock_port', (YLeaf(YType.uint32, 'clock-port'), ['int'])),
                            ('last_node', (YLeaf(YType.str, 'last-node'), ['str'])),
                            ('last_selection_point', (YLeaf(YType.uint32, 'last-selection-point'), ['int'])),
                            ('output_id', (YLeaf(YType.uint32, 'output-id'), ['int'])),
                            ('supports_frequency', (YLeaf(YType.boolean, 'supports-frequency'), ['bool'])),
                            ('supports_time_of_day', (YLeaf(YType.boolean, 'supports-time-of-day'), ['bool'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                            ('time_of_day_priority', (YLeaf(YType.uint8, 'time-of-day-priority'), ['int'])),
                            ('selected', (YLeaf(YType.boolean, 'selected'), ['bool'])),
                            ('output_id_xr', (YLeaf(YType.uint8, 'output-id-xr'), ['int'])),
                            ('platform_status', (YLeaf(YType.enumeration, 'platform-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagStreamState', '')])),
                            ('platform_failed_reason', (YLeaf(YType.str, 'platform-failed-reason'), ['str'])),
                        ])
                        self.selection_point = None
                        self.stream_type = None
                        self.source_type = None
                        self.interface = None
                        self.clock_port = None
                        self.last_node = None
                        self.last_selection_point = None
                        self.output_id = None
                        self.supports_frequency = None
                        self.supports_time_of_day = None
                        self.priority = None
                        self.time_of_day_priority = None
                        self.selected = None
                        self.output_id_xr = None
                        self.platform_status = None
                        self.platform_failed_reason = None

                        self.input_selection_point = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint()
                        self.input_selection_point.parent = self
                        self._children_name_map["input_selection_point"] = "input-selection-point"

                        self.stream = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream()
                        self.stream.parent = self
                        self._children_name_map["stream"] = "stream"

                        self.original_source = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource()
                        self.original_source.parent = self
                        self._children_name_map["original_source"] = "original-source"

                        self.quality_level = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel()
                        self.quality_level.parent = self
                        self._children_name_map["quality_level"] = "quality-level"
                        self._segment_path = lambda: "selection-point-input"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput, ['selection_point', 'stream_type', 'source_type', 'interface', 'clock_port', 'last_node', 'last_selection_point', 'output_id', u'supports_frequency', u'supports_time_of_day', u'priority', u'time_of_day_priority', u'selected', u'output_id_xr', u'platform_status', u'platform_failed_reason'], name, value)


                    class InputSelectionPoint(Entity):
                        """
                        The selection point the input is for
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint, self).__init__()

                            self.yang_name = "input-selection-point"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ])
                            self.selection_point_type = None
                            self.selection_point_description = None
                            self.node = None
                            self._segment_path = lambda: "input-selection-point"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                    class Stream(Entity):
                        """
                        Stream
                        
                        .. attribute:: source_id
                        
                        	Source ID
                        	**type**\:  :py:class:`SourceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId>`
                        
                        .. attribute:: selection_point_id
                        
                        	Selection point ID
                        	**type**\:  :py:class:`SelectionPointId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId>`
                        
                        .. attribute:: stream_input
                        
                        	StreamInput
                        	**type**\:  :py:class:`FsyncBagStreamInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamInput>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream, self).__init__()

                            self.yang_name = "stream"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("source-id", ("source_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId)), ("selection-point-id", ("selection_point_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId))])
                            self._leafs = OrderedDict([
                                ('stream_input', (YLeaf(YType.enumeration, 'stream-input'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagStreamInput', '')])),
                            ])
                            self.stream_input = None

                            self.source_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId()
                            self.source_id.parent = self
                            self._children_name_map["source_id"] = "source-id"

                            self.selection_point_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId()
                            self.selection_point_id.parent = self
                            self._children_name_map["selection_point_id"] = "selection-point-id"
                            self._segment_path = lambda: "stream"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream, [u'stream_input'], name, value)


                        class SourceId(Entity):
                            """
                            Source ID
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId>`
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, self).__init__()

                                self.yang_name = "source-id"
                                self.yang_parent_name = "stream"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.node = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId, [u'node', u'id', u'clock_name'], name, value)


                            class GnssReceiverId(Entity):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId, self).__init__()

                                    self.yang_name = "gnss-receiver-id"
                                    self.yang_parent_name = "source-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                        ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                    ])
                                    self.node = None
                                    self.id = None
                                    self.clock_name = None
                                    self._segment_path = lambda: "gnss-receiver-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                        class SelectionPointId(Entity):
                            """
                            Selection point ID
                            
                            .. attribute:: selection_point
                            
                            	Last selection point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint>`
                            
                            .. attribute:: output_id
                            
                            	Output ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId, self).__init__()

                                self.yang_name = "selection-point-id"
                                self.yang_parent_name = "stream"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("selection-point", ("selection_point", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint))])
                                self._leafs = OrderedDict([
                                    ('output_id', (YLeaf(YType.uint8, 'output-id'), ['int'])),
                                ])
                                self.output_id = None

                                self.selection_point = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint()
                                self.selection_point.parent = self
                                self._children_name_map["selection_point"] = "selection-point"
                                self._segment_path = lambda: "selection-point-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId, [u'output_id'], name, value)


                            class SelectionPoint(Entity):
                                """
                                Last selection point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint, self).__init__()

                                    self.yang_name = "selection-point"
                                    self.yang_parent_name = "selection-point-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('selection_point_type', (YLeaf(YType.uint8, 'selection-point-type'), ['int'])),
                                        ('selection_point_description', (YLeaf(YType.str, 'selection-point-description'), ['str'])),
                                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ])
                                    self.selection_point_type = None
                                    self.selection_point_description = None
                                    self.node = None
                                    self._segment_path = lambda: "selection-point"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint, [u'selection_point_type', u'selection_point_description', u'node'], name, value)


                    class OriginalSource(Entity):
                        """
                        Original source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId>`
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, self).__init__()

                            self.yang_name = "original-source"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.node = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "original-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, [u'source_class', u'ethernet_interface', u'sonet_interface', u'node', u'ptp_node', u'satellite_access_interface', u'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "original-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId, [u'node', u'id', u'clock_name'], name, value)


                        class GnssReceiverId(Entity):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId, self).__init__()

                                self.yang_name = "gnss-receiver-id"
                                self.yang_parent_name = "original-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('clock_name', (YLeaf(YType.str, 'clock-name'), ['str'])),
                                ])
                                self.node = None
                                self.id = None
                                self.clock_name = None
                                self._segment_path = lambda: "gnss-receiver-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId, [u'node', u'id', u'clock_name'], name, value)


                    class QualityLevel(Entity):
                        """
                        Quality Level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel, self).__init__()

                            self.yang_name = "quality-level"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlOption', '')])),
                                ('option1_value', (YLeaf(YType.enumeration, 'option1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO1Value', '')])),
                                ('option2_generation1_value', (YLeaf(YType.enumeration, 'option2-generation1-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G1Value', '')])),
                                ('option2_generation2_value', (YLeaf(YType.enumeration, 'option2-generation2-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagQlO2G2Value', '')])),
                            ])
                            self.quality_level_option = None
                            self.option1_value = None
                            self.option2_generation1_value = None
                            self.option2_generation2_value = None
                            self._segment_path = lambda: "quality-level"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel, [u'quality_level_option', u'option1_value', u'option2_generation1_value', u'option2_generation2_value'], name, value)

    def clone_ptr(self):
        self._top_entity = FrequencySynchronization()
        return self._top_entity

