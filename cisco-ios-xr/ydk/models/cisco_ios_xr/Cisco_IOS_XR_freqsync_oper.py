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
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagClockIntfClass']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagDampingState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagEsmcPeerState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagForwardtraceNode']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagQlO1Value']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagQlO2G1Value']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagQlO2G2Value']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagQlOption']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagSourceClass']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagSourceState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagStreamInput']


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

    .. data:: stream_acquiring = 3

    	Stream acquiring

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

    stream_acquiring = Enum.YLeaf(3, "stream-acquiring")

    stream_locked = Enum.YLeaf(4, "stream-locked")

    stream_holdover = Enum.YLeaf(5, "stream-holdover")

    stream_freerun = Enum.YLeaf(6, "stream-freerun")

    stream_failed = Enum.YLeaf(7, "stream-failed")

    stream_unmonitored = Enum.YLeaf(8, "stream-unmonitored")

    stream_error = Enum.YLeaf(9, "stream-error")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncBagStreamState']


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

    .. data:: gnss = 8

    	A GNSS receiver

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    sonet = Enum.YLeaf(2, "sonet")

    clock = Enum.YLeaf(3, "clock")

    internal = Enum.YLeaf(4, "internal")

    ptp = Enum.YLeaf(5, "ptp")

    satellite_access = Enum.YLeaf(6, "satellite-access")

    ntp = Enum.YLeaf(7, "ntp")

    gnss = Enum.YLeaf(8, "gnss")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncSource']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FsyncStream']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['ImStateEnum']



class FrequencySynchronization(_Entity_):
    """
    Frequency Synchronization operational data
    
    .. attribute:: global_nodes
    
    	Table for global node\-specific operational data
    	**type**\:  :py:class:`GlobalNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes>`
    
    	**config**\: False
    
    .. attribute:: global_interfaces
    
    	Table for global interface operational data
    	**type**\:  :py:class:`GlobalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces>`
    
    	**config**\: False
    
    .. attribute:: summary
    
    	Summary operational data
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary>`
    
    	**config**\: False
    
    .. attribute:: interface_datas
    
    	Table for interface operational data
    	**type**\:  :py:class:`InterfaceDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas>`
    
    	**config**\: False
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'freqsync-oper'
    _revision = '2017-10-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class GlobalNodes(_Entity_):
        """
        Table for global node\-specific operational data
        
        .. attribute:: global_node
        
        	Global node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`GlobalNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode>`
        
        	**config**\: False
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class GlobalNode(_Entity_):
            """
            Global node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: clock_interface_selection_back_traces
            
            	Selection backtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionBackTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces>`
            
            	**config**\: False
            
            .. attribute:: clock_interface_selection_forward_traces
            
            	Selection forwardtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionForwardTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces>`
            
            	**config**\: False
            
            .. attribute:: time_of_day_back_trace
            
            	Selection backtrace operational data for time\-of\-day on a particular node
            	**type**\:  :py:class:`TimeOfDayBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace>`
            
            	**config**\: False
            
            .. attribute:: ntp_selection_forward_trace
            
            	Selection forwardtrace operational data for a NTP clock
            	**type**\:  :py:class:`NtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace>`
            
            	**config**\: False
            
            .. attribute:: ptp_selection_forward_trace
            
            	Selection forwardtrace operational data for a PTP clock
            	**type**\:  :py:class:`PtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace>`
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class ClockInterfaceSelectionBackTraces(_Entity_):
                """
                Selection backtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_back_trace
                
                	Selection backtrace operational data for a particular clock\-interface or GNSS receiver
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ClockInterfaceSelectionBackTrace(_Entity_):
                    """
                    Selection backtrace operational data for a
                    particular clock\-interface or GNSS receiver
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    	**config**\: False
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: selected_source
                    
                    	Source which has been selected for output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point
                    
                    	List of selection points in the backtrace
                    	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class SelectedSource(_Entity_):
                        """
                        Source which has been selected for output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock-interface-selection-back-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource']['meta_info']


                    class SelectionPoint(_Entity_):
                        """
                        List of selection points in the backtrace
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces']['meta_info']


            class ClockInterfaceSelectionForwardTraces(_Entity_):
                """
                Selection forwardtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_forward_trace
                
                	Selection forwardtrace operational data for a particular clock\-interface
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ClockInterfaceSelectionForwardTrace(_Entity_):
                    """
                    Selection forwardtrace operational data for a
                    particular clock\-interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    	**config**\: False
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: forward_trace
                    
                    	Selection ForwardTrace
                    	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class ForwardTrace(_Entity_):
                        """
                        Selection ForwardTrace
                        
                        .. attribute:: forward_trace_node
                        
                        	The source or selection point at this point in the forwardtrace
                        	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class ForwardTraceNode(_Entity_):
                            """
                            The source or selection point at this point in
                            the forwardtrace
                            
                            .. attribute:: selection_point
                            
                            	Selection Point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                            
                            	**config**\: False
                            
                            .. attribute:: source
                            
                            	Timing Source
                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                            
                            	**config**\: False
                            
                            .. attribute:: node_type
                            
                            	NodeType
                            	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                            class SelectionPoint(_Entity_):
                                """
                                Selection Point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint']['meta_info']


                            class Source(_Entity_):
                                """
                                Timing Source
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                                
                                	**config**\: False
                                
                                .. attribute:: internal_clock_id
                                
                                	Internal Clock ID
                                	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId>`
                                
                                	**config**\: False
                                
                                .. attribute:: gnss_receiver_id
                                
                                	GNSS Receiver ID
                                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                                
                                	**config**\: False
                                
                                .. attribute:: source_class
                                
                                	SourceClass
                                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                                
                                	**config**\: False
                                
                                .. attribute:: ethernet_interface
                                
                                	Ethernet interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: sonet_interface
                                
                                	SONET interfaces
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: ptp_node
                                
                                	PTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: satellite_access_interface
                                
                                	Satellite Access Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: ntp_node
                                
                                	NTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                    self.yang_name = "source"
                                    self.yang_parent_name = "forward-trace-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                    self._leafs = OrderedDict([
                                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                    ])
                                    self.source_class = None
                                    self.ethernet_interface = None
                                    self.sonet_interface = None
                                    self.ptp_node = None
                                    self.satellite_access_interface = None
                                    self.ntp_node = None

                                    self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                    self.clock_id.parent = self
                                    self._children_name_map["clock_id"] = "clock-id"

                                    self.internal_clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId()
                                    self.internal_clock_id.parent = self
                                    self._children_name_map["internal_clock_id"] = "internal-clock-id"

                                    self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                    self.gnss_receiver_id.parent = self
                                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                    self._segment_path = lambda: "source"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                                class ClockId(_Entity_):
                                    """
                                    Clock ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: id
                                    
                                    	ID (port number for clock interface, receiver number for GNSS receiver)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: clock_name
                                    
                                    	Name
                                    	**type**\: str
                                    
                                    	**length:** 0..144
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2017-10-20'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId']['meta_info']


                                class InternalClockId(_Entity_):
                                    """
                                    Internal Clock ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: id
                                    
                                    	ID (port number for clock interface, receiver number for GNSS receiver)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: clock_name
                                    
                                    	Name
                                    	**type**\: str
                                    
                                    	**length:** 0..144
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2017-10-20'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, self).__init__()

                                        self.yang_name = "internal-clock-id"
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
                                        self._segment_path = lambda: "internal-clock-id"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId']['meta_info']


                                class GnssReceiverId(_Entity_):
                                    """
                                    GNSS Receiver ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: id
                                    
                                    	ID (port number for clock interface, receiver number for GNSS receiver)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: clock_name
                                    
                                    	Name
                                    	**type**\: str
                                    
                                    	**length:** 0..144
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2017-10-20'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces']['meta_info']


            class TimeOfDayBackTrace(_Entity_):
                """
                Selection backtrace operational data for
                time\-of\-day on a particular node
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource>`
                
                	**config**\: False
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class SelectedSource(_Entity_):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId>`
                    
                    	**config**\: False
                    
                    .. attribute:: internal_clock_id
                    
                    	Internal Clock ID
                    	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId>`
                    
                    	**config**\: False
                    
                    .. attribute:: gnss_receiver_id
                    
                    	GNSS Receiver ID
                    	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId>`
                    
                    	**config**\: False
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "time-of-day-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId))])
                        self._leafs = OrderedDict([
                            ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                            ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                            ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                            ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                            ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                            ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                        ])
                        self.source_class = None
                        self.ethernet_interface = None
                        self.sonet_interface = None
                        self.ptp_node = None
                        self.satellite_access_interface = None
                        self.ntp_node = None

                        self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"

                        self.internal_clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId()
                        self.internal_clock_id.parent = self
                        self._children_name_map["internal_clock_id"] = "internal-clock-id"

                        self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId()
                        self.gnss_receiver_id.parent = self
                        self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                        self._segment_path = lambda: "selected-source"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                    class ClockId(_Entity_):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId']['meta_info']


                    class InternalClockId(_Entity_):
                        """
                        Internal Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId, self).__init__()

                            self.yang_name = "internal-clock-id"
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
                            self._segment_path = lambda: "internal-clock-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.InternalClockId']['meta_info']


                    class GnssReceiverId(_Entity_):
                        """
                        GNSS Receiver ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.GnssReceiverId']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource']['meta_info']


                class SelectionPoint(_Entity_):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace']['meta_info']


            class NtpSelectionForwardTrace(_Entity_):
                """
                Selection forwardtrace operational data for a
                NTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ForwardTrace(_Entity_):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class ForwardTraceNode(_Entity_):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        	**config**\: False
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(_Entity_):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint']['meta_info']


                        class Source(_Entity_):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: internal_clock_id
                            
                            	Internal Clock ID
                            	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            	**config**\: False
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            	**config**\: False
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.internal_clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId()
                                self.internal_clock_id.parent = self
                                self._children_name_map["internal_clock_id"] = "internal-clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(_Entity_):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId']['meta_info']


                            class InternalClockId(_Entity_):
                                """
                                Internal Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, self).__init__()

                                    self.yang_name = "internal-clock-id"
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
                                    self._segment_path = lambda: "internal-clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId']['meta_info']


                            class GnssReceiverId(_Entity_):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace']['meta_info']


            class PtpSelectionForwardTrace(_Entity_):
                """
                Selection forwardtrace operational data for a
                PTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ForwardTrace(_Entity_):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class ForwardTraceNode(_Entity_):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        	**config**\: False
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(_Entity_):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint']['meta_info']


                        class Source(_Entity_):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: internal_clock_id
                            
                            	Internal Clock ID
                            	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            	**config**\: False
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            	**config**\: False
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.internal_clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId()
                                self.internal_clock_id.parent = self
                                self._children_name_map["internal_clock_id"] = "internal-clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(_Entity_):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId']['meta_info']


                            class InternalClockId(_Entity_):
                                """
                                Internal Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, self).__init__()

                                    self.yang_name = "internal-clock-id"
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
                                    self._segment_path = lambda: "internal-clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId']['meta_info']


                            class GnssReceiverId(_Entity_):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.GlobalNodes.GlobalNode']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
            return meta._meta_table['FrequencySynchronization.GlobalNodes']['meta_info']


    class GlobalInterfaces(_Entity_):
        """
        Table for global interface operational data
        
        .. attribute:: global_interface
        
        	Global interface information for a particular interface
        	**type**\: list of  		 :py:class:`GlobalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class GlobalInterface(_Entity_):
            """
            Global interface information for a particular
            interface
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: interface_selection_forward_trace
            
            	Selection forwardtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace>`
            
            	**config**\: False
            
            .. attribute:: interface_selection_back_trace
            
            	Selection backtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace>`
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class InterfaceSelectionForwardTrace(_Entity_):
                """
                Selection forwardtrace operational data for a
                particular interface
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ForwardTrace(_Entity_):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class ForwardTraceNode(_Entity_):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        	**config**\: False
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(_Entity_):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint']['meta_info']


                        class Source(_Entity_):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: internal_clock_id
                            
                            	Internal Clock ID
                            	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId>`
                            
                            	**config**\: False
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            	**config**\: False
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.internal_clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId()
                                self.internal_clock_id.parent = self
                                self._children_name_map["internal_clock_id"] = "internal-clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(_Entity_):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId']['meta_info']


                            class InternalClockId(_Entity_):
                                """
                                Internal Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, self).__init__()

                                    self.yang_name = "internal-clock-id"
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
                                    self._segment_path = lambda: "internal-clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.InternalClockId']['meta_info']


                            class GnssReceiverId(_Entity_):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.GnssReceiverId']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace']['meta_info']


            class InterfaceSelectionBackTrace(_Entity_):
                """
                Selection backtrace operational data for a
                particular interface
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource>`
                
                	**config**\: False
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class SelectedSource(_Entity_):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId>`
                    
                    	**config**\: False
                    
                    .. attribute:: internal_clock_id
                    
                    	Internal Clock ID
                    	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId>`
                    
                    	**config**\: False
                    
                    .. attribute:: gnss_receiver_id
                    
                    	GNSS Receiver ID
                    	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId>`
                    
                    	**config**\: False
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "interface-selection-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId))])
                        self._leafs = OrderedDict([
                            ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                            ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                            ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                            ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                            ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                            ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                        ])
                        self.source_class = None
                        self.ethernet_interface = None
                        self.sonet_interface = None
                        self.ptp_node = None
                        self.satellite_access_interface = None
                        self.ntp_node = None

                        self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"

                        self.internal_clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId()
                        self.internal_clock_id.parent = self
                        self._children_name_map["internal_clock_id"] = "internal-clock-id"

                        self.gnss_receiver_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId()
                        self.gnss_receiver_id.parent = self
                        self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                        self._segment_path = lambda: "selected-source"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                    class ClockId(_Entity_):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId']['meta_info']


                    class InternalClockId(_Entity_):
                        """
                        Internal Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId, self).__init__()

                            self.yang_name = "internal-clock-id"
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
                            self._segment_path = lambda: "internal-clock-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.InternalClockId']['meta_info']


                    class GnssReceiverId(_Entity_):
                        """
                        GNSS Receiver ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: id
                        
                        	ID (port number for clock interface, receiver number for GNSS receiver)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: clock_name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..144
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.GnssReceiverId']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource']['meta_info']


                class SelectionPoint(_Entity_):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.GlobalInterfaces.GlobalInterface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
            return meta._meta_table['FrequencySynchronization.GlobalInterfaces']['meta_info']


    class Summary(_Entity_):
        """
        Summary operational data
        
        .. attribute:: frequency_summary
        
        	Summary of sources selected for frequency
        	**type**\: list of  		 :py:class:`FrequencySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary>`
        
        	**config**\: False
        
        .. attribute:: time_of_day_summary
        
        	Summary of sources selected for time\-of\-day
        	**type**\: list of  		 :py:class:`TimeOfDaySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class FrequencySummary(_Entity_):
            """
            Summary of sources selected for frequency
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source>`
            
            	**config**\: False
            
            .. attribute:: clock_count
            
            	The number of clock\-interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ethernet_count
            
            	The number of Ethernet interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sonet_count
            
            	The number of SONET/SDH interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary, ['clock_count', 'ethernet_count', 'sonet_count'], name, value)


            class Source(_Entity_):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.ClockId>`
                
                	**config**\: False
                
                .. attribute:: internal_clock_id
                
                	Internal Clock ID
                	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId>`
                
                	**config**\: False
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId>`
                
                	**config**\: False
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                	**config**\: False
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(FrequencySynchronization.Summary.FrequencySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "frequency-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Summary.FrequencySummary.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.Summary.FrequencySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.internal_clock_id = FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId()
                    self.internal_clock_id.parent = self
                    self._children_name_map["internal_clock_id"] = "internal-clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(_Entity_):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.FrequencySummary.Source.ClockId']['meta_info']


                class InternalClockId(_Entity_):
                    """
                    Internal Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId, self).__init__()

                        self.yang_name = "internal-clock-id"
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
                        self._segment_path = lambda: "internal-clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.FrequencySummary.Source.InternalClockId']['meta_info']


                class GnssReceiverId(_Entity_):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.FrequencySummary.Source.GnssReceiverId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Summary.FrequencySummary.Source']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.Summary.FrequencySummary']['meta_info']


        class TimeOfDaySummary(_Entity_):
            """
            Summary of sources selected for time\-of\-day
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source>`
            
            	**config**\: False
            
            .. attribute:: node_count
            
            	The number of cards having their time\-of\-day set by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary, ['node_count'], name, value)


            class Source(_Entity_):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId>`
                
                	**config**\: False
                
                .. attribute:: internal_clock_id
                
                	Internal Clock ID
                	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId>`
                
                	**config**\: False
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId>`
                
                	**config**\: False
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                	**config**\: False
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(FrequencySynchronization.Summary.TimeOfDaySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "time-of-day-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.internal_clock_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId()
                    self.internal_clock_id.parent = self
                    self._children_name_map["internal_clock_id"] = "internal-clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(_Entity_):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId']['meta_info']


                class InternalClockId(_Entity_):
                    """
                    Internal Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId, self).__init__()

                        self.yang_name = "internal-clock-id"
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
                        self._segment_path = lambda: "internal-clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/source/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.TimeOfDaySummary.Source.InternalClockId']['meta_info']


                class GnssReceiverId(_Entity_):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Summary.TimeOfDaySummary.Source.GnssReceiverId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Summary.TimeOfDaySummary.Source']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.Summary.TimeOfDaySummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
            return meta._meta_table['FrequencySynchronization.Summary']['meta_info']


    class InterfaceDatas(_Entity_):
        """
        Table for interface operational data
        
        .. attribute:: interface_data
        
        	Operational data for a particular interface
        	**type**\: list of  		 :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData>`
        
        	**config**\: False
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class InterfaceData(_Entity_):
            """
            Operational data for a particular interface
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: source
            
            	The source ID for the interface
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source>`
            
            	**config**\: False
            
            .. attribute:: selected_source
            
            	Timing source selected for interface output
            	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource>`
            
            	**config**\: False
            
            .. attribute:: quality_level_received
            
            	Received quality level
            	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived>`
            
            	**config**\: False
            
            .. attribute:: quality_level_damped
            
            	Quality level after damping has been applied
            	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped>`
            
            	**config**\: False
            
            .. attribute:: quality_level_effective_input
            
            	The effective input quality level
            	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput>`
            
            	**config**\: False
            
            .. attribute:: quality_level_effective_output
            
            	The effective output quality level
            	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput>`
            
            	**config**\: False
            
            .. attribute:: quality_level_selected_source
            
            	The quality level of the source driving this interface
            	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource>`
            
            	**config**\: False
            
            .. attribute:: ethernet_peer_information
            
            	Ethernet peer information
            	**type**\:  :py:class:`EthernetPeerInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation>`
            
            	**config**\: False
            
            .. attribute:: esmc_statistics
            
            	ESMC Statistics
            	**type**\:  :py:class:`EsmcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics>`
            
            	**config**\: False
            
            .. attribute:: name
            
            	Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: state
            
            	Interface state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.ImStateEnum>`
            
            	**config**\: False
            
            .. attribute:: ssm_enabled
            
            	SSM is enabled on the interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: squelched
            
            	The interface output is squelched
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: selection_input
            
            	The interface is an input for selection
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: priority
            
            	Priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: time_of_day_priority
            
            	Time\-of\-day priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: damping_state
            
            	Damping state
            	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
            
            	**config**\: False
            
            .. attribute:: damping_time
            
            	Time until damping state changes in ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: wait_to_restore_time
            
            	Wait\-to\-restore time for the interface
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: supports_frequency
            
            	The PTP clock supports frequency
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_time_of_day
            
            	The PTP clock supports time
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: spa_selection_point
            
            	Spa selection points
            	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint>`
            
            	**config**\: False
            
            .. attribute:: node_selection_point
            
            	Node selection points
            	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint>`
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData, ['interface_name', 'name', 'state', 'ssm_enabled', 'squelched', 'selection_input', 'priority', 'time_of_day_priority', 'damping_state', 'damping_time', 'wait_to_restore_time', 'supports_frequency', 'supports_time_of_day'], name, value)


            class Source(_Entity_):
                """
                The source ID for the interface
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId>`
                
                	**config**\: False
                
                .. attribute:: internal_clock_id
                
                	Internal Clock ID
                	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId>`
                
                	**config**\: False
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId>`
                
                	**config**\: False
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                	**config**\: False
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.internal_clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId()
                    self.internal_clock_id.parent = self
                    self._children_name_map["internal_clock_id"] = "internal-clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(_Entity_):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.Source.ClockId']['meta_info']


                class InternalClockId(_Entity_):
                    """
                    Internal Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId, self).__init__()

                        self.yang_name = "internal-clock-id"
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
                        self._segment_path = lambda: "internal-clock-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.Source.InternalClockId']['meta_info']


                class GnssReceiverId(_Entity_):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.Source.GnssReceiverId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.Source']['meta_info']


            class SelectedSource(_Entity_):
                """
                Timing source selected for interface output
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId>`
                
                	**config**\: False
                
                .. attribute:: internal_clock_id
                
                	Internal Clock ID
                	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId>`
                
                	**config**\: False
                
                .. attribute:: gnss_receiver_id
                
                	GNSS Receiver ID
                	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId>`
                
                	**config**\: False
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                	**config**\: False
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource, self).__init__()

                    self.yang_name = "selected-source"
                    self.yang_parent_name = "interface-data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId))])
                    self._leafs = OrderedDict([
                        ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                        ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                        ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                        ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                        ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                        ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                    ])
                    self.source_class = None
                    self.ethernet_interface = None
                    self.sonet_interface = None
                    self.ptp_node = None
                    self.satellite_access_interface = None
                    self.ntp_node = None

                    self.clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"

                    self.internal_clock_id = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId()
                    self.internal_clock_id.parent = self
                    self._children_name_map["internal_clock_id"] = "internal-clock-id"

                    self.gnss_receiver_id = FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId()
                    self.gnss_receiver_id.parent = self
                    self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                    self._segment_path = lambda: "selected-source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(_Entity_):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.ClockId']['meta_info']


                class InternalClockId(_Entity_):
                    """
                    Internal Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId, self).__init__()

                        self.yang_name = "internal-clock-id"
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
                        self._segment_path = lambda: "internal-clock-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.InternalClockId']['meta_info']


                class GnssReceiverId(_Entity_):
                    """
                    GNSS Receiver ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	ID (port number for clock interface, receiver number for GNSS receiver)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: clock_name
                    
                    	Name
                    	**type**\: str
                    
                    	**length:** 0..144
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource.GnssReceiverId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.SelectedSource']['meta_info']


            class QualityLevelReceived(_Entity_):
                """
                Received quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                	**config**\: False
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelReceived']['meta_info']


            class QualityLevelDamped(_Entity_):
                """
                Quality level after damping has been applied
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                	**config**\: False
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelDamped']['meta_info']


            class QualityLevelEffectiveInput(_Entity_):
                """
                The effective input quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                	**config**\: False
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveInput']['meta_info']


            class QualityLevelEffectiveOutput(_Entity_):
                """
                The effective output quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                	**config**\: False
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelEffectiveOutput']['meta_info']


            class QualityLevelSelectedSource(_Entity_):
                """
                The quality level of the source driving this
                interface
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                	**config**\: False
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                	**config**\: False
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.QualityLevelSelectedSource']['meta_info']


            class EthernetPeerInformation(_Entity_):
                """
                Ethernet peer information
                
                .. attribute:: peer_state_time
                
                	Time of last peer state transition
                	**type**\:  :py:class:`PeerStateTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime>`
                
                	**config**\: False
                
                .. attribute:: last_ssm
                
                	Time of last SSM received
                	**type**\:  :py:class:`LastSsm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm>`
                
                	**config**\: False
                
                .. attribute:: peer_state
                
                	Peer state
                	**type**\:  :py:class:`FsyncBagEsmcPeerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagEsmcPeerState>`
                
                	**config**\: False
                
                .. attribute:: peer_up_count
                
                	Number of times the peer has come up
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: peer_timeout_count
                
                	Number of times the peer has timed out
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation, ['peer_state', 'peer_up_count', 'peer_timeout_count'], name, value)


                class PeerStateTime(_Entity_):
                    """
                    Time of last peer state transition
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime, ['seconds', 'nanoseconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.PeerStateTime']['meta_info']


                class LastSsm(_Entity_):
                    """
                    Time of last SSM received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm, ['seconds', 'nanoseconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation.LastSsm']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.EthernetPeerInformation']['meta_info']


            class EsmcStatistics(_Entity_):
                """
                ESMC Statistics
                
                .. attribute:: esmc_events_sent
                
                	Number of event SSMs sent
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: esmc_events_received
                
                	Number of event SSMs received
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: esmc_infos_sent
                
                	Number of info SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: esmc_infos_received
                
                	Number of info SSms received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: esmc_dn_us_sent
                
                	Number of SSMs with DNU QL sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: esmc_dn_us_received
                
                	Number of SSMs with DNU QL received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: esmc_malformed_received
                
                	Number of malformed packets received
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: esmc_received_error
                
                	Number of received packets that failed to be handled
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics, ['esmc_events_sent', 'esmc_events_received', 'esmc_infos_sent', 'esmc_infos_received', 'esmc_dn_us_sent', 'esmc_dn_us_received', 'esmc_malformed_received', 'esmc_received_error'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.EsmcStatistics']['meta_info']


            class SpaSelectionPoint(_Entity_):
                """
                Spa selection points
                
                .. attribute:: selection_point
                
                	Selection point ID
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: selection_point_description
                
                	Selection point description
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.SpaSelectionPoint']['meta_info']


            class NodeSelectionPoint(_Entity_):
                """
                Node selection points
                
                .. attribute:: selection_point
                
                	Selection point ID
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: selection_point_description
                
                	Selection point description
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData.NodeSelectionPoint']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.InterfaceDatas.InterfaceData']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
            return meta._meta_table['FrequencySynchronization.InterfaceDatas']['meta_info']


    class Nodes(_Entity_):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2017-10-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Node(_Entity_):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: ntp_data
            
            	NTP operational data
            	**type**\:  :py:class:`NtpData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData>`
            
            	**config**\: False
            
            .. attribute:: selection_point_datas
            
            	Selection point data table
            	**type**\:  :py:class:`SelectionPointDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas>`
            
            	**config**\: False
            
            .. attribute:: configuration_errors
            
            	Configuration error operational data
            	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors>`
            
            	**config**\: False
            
            .. attribute:: ptp_data
            
            	PTP operational data
            	**type**\:  :py:class:`PtpData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData>`
            
            	**config**\: False
            
            .. attribute:: ssm_summary
            
            	SSM operational data
            	**type**\:  :py:class:`SsmSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SsmSummary>`
            
            	**config**\: False
            
            .. attribute:: detailed_clock_datas
            
            	Table for detailed clock operational data
            	**type**\:  :py:class:`DetailedClockDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas>`
            
            	**config**\: False
            
            .. attribute:: clock_datas
            
            	Table for clock operational data
            	**type**\:  :py:class:`ClockDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas>`
            
            	**config**\: False
            
            .. attribute:: selection_point_inputs
            
            	Table for selection point input operational data
            	**type**\:  :py:class:`SelectionPointInputs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs>`
            
            	**config**\: False
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2017-10-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class NtpData(_Entity_):
                """
                NTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	NTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                	**config**\: False
                
                .. attribute:: supports_frequency
                
                	The NTP clock supports frequency
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: supports_time_of_day
                
                	The NTP clock supports time
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: frequency_priority
                
                	The priority of the NTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: time_of_day_priority
                
                	The priority of the NTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint>`
                
                	**config**\: False
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData, ['state', 'supports_frequency', 'supports_time_of_day', 'frequency_priority', 'time_of_day_priority'], name, value)


                class QualityLevelEffectiveInput(_Entity_):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    	**config**\: False
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    	**config**\: False
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    	**config**\: False
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.NtpData.QualityLevelEffectiveInput']['meta_info']


                class SpaSelectionPoint(_Entity_):
                    """
                    Spa selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.NtpData.SpaSelectionPoint']['meta_info']


                class NodeSelectionPoint(_Entity_):
                    """
                    Node selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.NtpData.NodeSelectionPoint']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.NtpData']['meta_info']


            class SelectionPointDatas(_Entity_):
                """
                Selection point data table
                
                .. attribute:: selection_point_data
                
                	Operational data for a given selection point
                	**type**\: list of  		 :py:class:`SelectionPointData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class SelectionPointData(_Entity_):
                    """
                    Operational data for a given selection point
                    
                    .. attribute:: selection_point  (key)
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: output
                    
                    	Information about the output of the selection point
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_programmed
                    
                    	Time the SP was last programmed
                    	**type**\:  :py:class:`LastProgrammed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_selection
                    
                    	Time the last selection was made
                    	**type**\:  :py:class:`LastSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection>`
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_type
                    
                    	Selection Point Type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: inputs
                    
                    	Number of inputs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: inputs_selected
                    
                    	Number of inputs that are selected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: time_of_day_selection
                    
                    	The selection point is a time\-of\-day selection point
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData, ['selection_point', 'selection_point_type', 'description', 'inputs', 'inputs_selected', 'time_of_day_selection'], name, value)


                    class Output(_Entity_):
                        """
                        Information about the output of the selection
                        point
                        
                        .. attribute:: local_clock_ouput
                        
                        	Used for local clock output
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: local_line_output
                        
                        	Used for local line interface output
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: local_time_of_day_output
                        
                        	Used for local time\-of\-day output
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: spa_selection_point
                        
                        	SPA selection points
                        	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: node_selection_point
                        
                        	Node selection points
                        	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: chassis_selection_point
                        
                        	Chassis selection points
                        	**type**\: list of  		 :py:class:`ChassisSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint>`
                        
                        	**config**\: False
                        
                        .. attribute:: router_selection_point
                        
                        	Router selection points
                        	**type**\: list of  		 :py:class:`RouterSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output, ['local_clock_ouput', 'local_line_output', 'local_time_of_day_output'], name, value)


                        class SpaSelectionPoint(_Entity_):
                            """
                            SPA selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.SpaSelectionPoint']['meta_info']


                        class NodeSelectionPoint(_Entity_):
                            """
                            Node selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.NodeSelectionPoint']['meta_info']


                        class ChassisSelectionPoint(_Entity_):
                            """
                            Chassis selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.ChassisSelectionPoint']['meta_info']


                        class RouterSelectionPoint(_Entity_):
                            """
                            Router selection points
                            
                            .. attribute:: selection_point
                            
                            	Selection point ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output.RouterSelectionPoint']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.Output']['meta_info']


                    class LastProgrammed(_Entity_):
                        """
                        Time the SP was last programmed
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed, ['seconds', 'nanoseconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastProgrammed']['meta_info']


                    class LastSelection(_Entity_):
                        """
                        Time the last selection was made
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection, ['seconds', 'nanoseconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData.LastSelection']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas.SelectionPointData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointDatas']['meta_info']


            class ConfigurationErrors(_Entity_):
                """
                Configuration error operational data
                
                .. attribute:: error_source
                
                	Configuration errors
                	**type**\: list of  		 :py:class:`ErrorSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ErrorSource(_Entity_):
                    """
                    Configuration errors
                    
                    .. attribute:: source
                    
                    	Source
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source>`
                    
                    	**config**\: False
                    
                    .. attribute:: input_min_ql
                    
                    	Configured minimum input QL
                    	**type**\:  :py:class:`InputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: input_exact_ql
                    
                    	Configured exact input QL
                    	**type**\:  :py:class:`InputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: input_max_ql
                    
                    	Configured maximum input QL
                    	**type**\:  :py:class:`InputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: output_min_ql
                    
                    	Configured mininum output QL
                    	**type**\:  :py:class:`OutputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: output_exact_ql
                    
                    	Configured exact output QL
                    	**type**\:  :py:class:`OutputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: output_max_ql
                    
                    	Configured exact maximum QL
                    	**type**\:  :py:class:`OutputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl>`
                    
                    	**config**\: False
                    
                    .. attribute:: enable_error
                    
                    	Frequency Synchronization enable error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: input_min_error
                    
                    	Minimum input QL config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: input_exact_error
                    
                    	Exact input QL config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: input_max_error
                    
                    	Maximum input Ql config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ouput_min_error
                    
                    	Minimum output QL config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: output_exact_error
                    
                    	Exact output QL config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: output_max_error
                    
                    	Maximum output QL config error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: input_output_mismatch
                    
                    	Input/Output mismatch error
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource, ['enable_error', 'input_min_error', 'input_exact_error', 'input_max_error', 'ouput_min_error', 'output_exact_error', 'output_max_error', 'input_output_mismatch'], name, value)


                    class Source(_Entity_):
                        """
                        Source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source']['meta_info']


                    class InputMinQl(_Entity_):
                        """
                        Configured minimum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl']['meta_info']


                    class InputExactQl(_Entity_):
                        """
                        Configured exact input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl']['meta_info']


                    class InputMaxQl(_Entity_):
                        """
                        Configured maximum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl']['meta_info']


                    class OutputMinQl(_Entity_):
                        """
                        Configured mininum output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl']['meta_info']


                    class OutputExactQl(_Entity_):
                        """
                        Configured exact output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl']['meta_info']


                    class OutputMaxQl(_Entity_):
                        """
                        Configured exact maximum QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.ConfigurationErrors']['meta_info']


            class PtpData(_Entity_):
                """
                PTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	PTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                	**config**\: False
                
                .. attribute:: supports_frequency
                
                	The PTP clock supports frequency
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: supports_time_of_day
                
                	The PTP clock supports time
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: frequency_priority
                
                	The priority of the PTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: time_of_day_priority
                
                	The priority of the PTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint>`
                
                	**config**\: False
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData, ['state', 'supports_frequency', 'supports_time_of_day', 'frequency_priority', 'time_of_day_priority'], name, value)


                class QualityLevelEffectiveInput(_Entity_):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    	**config**\: False
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    	**config**\: False
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    	**config**\: False
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.PtpData.QualityLevelEffectiveInput']['meta_info']


                class SpaSelectionPoint(_Entity_):
                    """
                    Spa selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.PtpData.SpaSelectionPoint']['meta_info']


                class NodeSelectionPoint(_Entity_):
                    """
                    Node selection points
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.PtpData.NodeSelectionPoint']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.PtpData']['meta_info']


            class SsmSummary(_Entity_):
                """
                SSM operational data
                
                .. attribute:: ethernet_sources
                
                	Number of ethernet interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ethernet_sources_select
                
                	Number of ethernet interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ethernet_sources_enabled
                
                	Number of ethernet interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sonet_sources
                
                	Number of SONET interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sonet_sources_select
                
                	Number of SONET interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sonet_sources_enabled
                
                	Number of SONET interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: events_sent
                
                	Total event SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: events_received
                
                	Total event SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: infos_sent
                
                	Total information SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: infos_received
                
                	Total information SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dn_us_sent
                
                	Total DNU SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dn_us_received
                
                	Total DNU SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SsmSummary, ['ethernet_sources', 'ethernet_sources_select', 'ethernet_sources_enabled', 'sonet_sources', 'sonet_sources_select', 'sonet_sources_enabled', 'events_sent', 'events_received', 'infos_sent', 'infos_received', 'dn_us_sent', 'dn_us_received'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SsmSummary']['meta_info']


            class DetailedClockDatas(_Entity_):
                """
                Table for detailed clock operational data
                
                .. attribute:: detailed_clock_data
                
                	Detailed operational data for a particular clock
                	**type**\: list of  		 :py:class:`DetailedClockData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class DetailedClockData(_Entity_):
                    """
                    Detailed operational data for a particular
                    clock
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    	**config**\: False
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: source
                    
                    	The source ID for the clock
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source>`
                    
                    	**config**\: False
                    
                    .. attribute:: selected_source
                    
                    	Timing source selected for clock output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_received
                    
                    	Received quality level
                    	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_damped
                    
                    	Quality level after damping has been applied
                    	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_effective_input
                    
                    	The effective input quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_effective_output
                    
                    	The effective output quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_selected_source
                    
                    	The quality level of the source driving this interface
                    	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Clock state
                    	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: down_reason
                    
                    	Why the clock is down
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Clock description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: ssm_support
                    
                    	The clock supports SSMs
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ssm_enabled
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: loopback
                    
                    	The clock is looped back
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: selection_input
                    
                    	The clock is an input for selection
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: squelched
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: damping_state
                    
                    	Damping state
                    	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
                    
                    	**config**\: False
                    
                    .. attribute:: damping_time
                    
                    	Time until damping state changes in ms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: input_disabled
                    
                    	Timing input is disabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: output_disabled
                    
                    	Timing output is disabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: wait_to_restore_time
                    
                    	Wait\-to\-restore time for the clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: clock_type_xr
                    
                    	The type of clock
                    	**type**\:  :py:class:`FsyncBagClockIntfClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagClockIntfClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: supports_frequency
                    
                    	The PTP clock supports frequency
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_time_of_day
                    
                    	The PTP clock supports time
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: spa_selection_point
                    
                    	Spa selection points
                    	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_selection_point
                    
                    	Node selection points
                    	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData, ['clock_type', 'id', 'state', 'down_reason', 'description', 'priority', 'time_of_day_priority', 'ssm_support', 'ssm_enabled', 'loopback', 'selection_input', 'squelched', 'damping_state', 'damping_time', 'input_disabled', 'output_disabled', 'wait_to_restore_time', 'clock_type_xr', 'supports_frequency', 'supports_time_of_day'], name, value)


                    class Source(_Entity_):
                        """
                        The source ID for the clock
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.Source']['meta_info']


                    class SelectedSource(_Entity_):
                        """
                        Timing source selected for clock output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "detailed-clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SelectedSource']['meta_info']


                    class QualityLevelReceived(_Entity_):
                        """
                        Received quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelReceived']['meta_info']


                    class QualityLevelDamped(_Entity_):
                        """
                        Quality level after damping has been applied
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelDamped']['meta_info']


                    class QualityLevelEffectiveInput(_Entity_):
                        """
                        The effective input quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveInput']['meta_info']


                    class QualityLevelEffectiveOutput(_Entity_):
                        """
                        The effective output quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelEffectiveOutput']['meta_info']


                    class QualityLevelSelectedSource(_Entity_):
                        """
                        The quality level of the source driving this
                        interface
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.QualityLevelSelectedSource']['meta_info']


                    class SpaSelectionPoint(_Entity_):
                        """
                        Spa selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.SpaSelectionPoint']['meta_info']


                    class NodeSelectionPoint(_Entity_):
                        """
                        Node selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData.NodeSelectionPoint']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas.DetailedClockData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.DetailedClockDatas']['meta_info']


            class ClockDatas(_Entity_):
                """
                Table for clock operational data
                
                .. attribute:: clock_data
                
                	Operational data for a particular clock
                	**type**\: list of  		 :py:class:`ClockData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class ClockData(_Entity_):
                    """
                    Operational data for a particular clock
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    	**config**\: False
                    
                    .. attribute:: id  (key)
                    
                    	Clock ID (port number for clock interfaces, receiver number for GNSS receivers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: source
                    
                    	The source ID for the clock
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source>`
                    
                    	**config**\: False
                    
                    .. attribute:: selected_source
                    
                    	Timing source selected for clock output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_received
                    
                    	Received quality level
                    	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_damped
                    
                    	Quality level after damping has been applied
                    	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_effective_input
                    
                    	The effective input quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_effective_output
                    
                    	The effective output quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level_selected_source
                    
                    	The quality level of the source driving this interface
                    	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Clock state
                    	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: down_reason
                    
                    	Why the clock is down
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Clock description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: ssm_support
                    
                    	The clock supports SSMs
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ssm_enabled
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: loopback
                    
                    	The clock is looped back
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: selection_input
                    
                    	The clock is an input for selection
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: squelched
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: damping_state
                    
                    	Damping state
                    	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
                    
                    	**config**\: False
                    
                    .. attribute:: damping_time
                    
                    	Time until damping state changes in ms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: input_disabled
                    
                    	Timing input is disabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: output_disabled
                    
                    	Timing output is disabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: wait_to_restore_time
                    
                    	Wait\-to\-restore time for the clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: clock_type_xr
                    
                    	The type of clock
                    	**type**\:  :py:class:`FsyncBagClockIntfClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagClockIntfClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: supports_frequency
                    
                    	The PTP clock supports frequency
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_time_of_day
                    
                    	The PTP clock supports time
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: spa_selection_point
                    
                    	Spa selection points
                    	**type**\: list of  		 :py:class:`SpaSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint>`
                    
                    	**config**\: False
                    
                    .. attribute:: node_selection_point
                    
                    	Node selection points
                    	**type**\: list of  		 :py:class:`NodeSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData, ['clock_type', 'id', 'state', 'down_reason', 'description', 'priority', 'time_of_day_priority', 'ssm_support', 'ssm_enabled', 'loopback', 'selection_input', 'squelched', 'damping_state', 'damping_time', 'input_disabled', 'output_disabled', 'wait_to_restore_time', 'clock_type_xr', 'supports_frequency', 'supports_time_of_day'], name, value)


                    class Source(_Entity_):
                        """
                        The source ID for the clock
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.Source']['meta_info']


                    class SelectedSource(_Entity_):
                        """
                        Timing source selected for clock output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "selected-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SelectedSource']['meta_info']


                    class QualityLevelReceived(_Entity_):
                        """
                        Received quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelReceived']['meta_info']


                    class QualityLevelDamped(_Entity_):
                        """
                        Quality level after damping has been applied
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelDamped']['meta_info']


                    class QualityLevelEffectiveInput(_Entity_):
                        """
                        The effective input quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveInput']['meta_info']


                    class QualityLevelEffectiveOutput(_Entity_):
                        """
                        The effective output quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelEffectiveOutput']['meta_info']


                    class QualityLevelSelectedSource(_Entity_):
                        """
                        The quality level of the source driving this
                        interface
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.QualityLevelSelectedSource']['meta_info']


                    class SpaSelectionPoint(_Entity_):
                        """
                        Spa selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.SpaSelectionPoint']['meta_info']


                    class NodeSelectionPoint(_Entity_):
                        """
                        Node selection points
                        
                        .. attribute:: selection_point
                        
                        	Selection point ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint, ['selection_point', 'selection_point_description'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData.NodeSelectionPoint']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas.ClockData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.ClockDatas']['meta_info']


            class SelectionPointInputs(_Entity_):
                """
                Table for selection point input operational
                data
                
                .. attribute:: selection_point_input
                
                	Operational data for a particular selection point input
                	**type**\: list of  		 :py:class:`SelectionPointInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput>`
                
                	**config**\: False
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2017-10-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class SelectionPointInput(_Entity_):
                    """
                    Operational data for a particular selection
                    point input
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stream_type
                    
                    	Type of stream
                    	**type**\:  :py:class:`FsyncStream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncStream>`
                    
                    	**config**\: False
                    
                    .. attribute:: source_type
                    
                    	Type of source
                    	**type**\:  :py:class:`FsyncSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: clock_port
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: last_node
                    
                    	Last node for a selection point stream
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: last_selection_point
                    
                    	Last selection point for a selection point stream
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: output_id
                    
                    	Output ID for a selection point stream
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: input_selection_point
                    
                    	The selection point the input is for
                    	**type**\:  :py:class:`InputSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint>`
                    
                    	**config**\: False
                    
                    .. attribute:: stream
                    
                    	Stream
                    	**type**\:  :py:class:`Stream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream>`
                    
                    	**config**\: False
                    
                    .. attribute:: original_source
                    
                    	Original source
                    	**type**\:  :py:class:`OriginalSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: quality_level
                    
                    	Quality Level
                    	**type**\:  :py:class:`QualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel>`
                    
                    	**config**\: False
                    
                    .. attribute:: supports_frequency
                    
                    	The selection point input supports frequency
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_time_of_day
                    
                    	The selection point input supports time\-of\-day
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: selected
                    
                    	The selection point input is selected
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: output_id_xr
                    
                    	Platform output ID, if the input is selected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: platform_status
                    
                    	Platform status
                    	**type**\:  :py:class:`FsyncBagStreamState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamState>`
                    
                    	**config**\: False
                    
                    .. attribute:: platform_failed_reason
                    
                    	Why the stream has failed
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2017-10-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput, ['selection_point', 'stream_type', 'source_type', 'interface', 'clock_port', 'last_node', 'last_selection_point', 'output_id', 'supports_frequency', 'supports_time_of_day', 'priority', 'time_of_day_priority', 'selected', 'output_id_xr', 'platform_status', 'platform_failed_reason'], name, value)


                    class InputSelectionPoint(_Entity_):
                        """
                        The selection point the input is for
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint']['meta_info']


                    class Stream(_Entity_):
                        """
                        Stream
                        
                        .. attribute:: source_id
                        
                        	Source ID
                        	**type**\:  :py:class:`SourceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId>`
                        
                        	**config**\: False
                        
                        .. attribute:: selection_point_id
                        
                        	Selection point ID
                        	**type**\:  :py:class:`SelectionPointId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId>`
                        
                        	**config**\: False
                        
                        .. attribute:: stream_input
                        
                        	StreamInput
                        	**type**\:  :py:class:`FsyncBagStreamInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamInput>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream, ['stream_input'], name, value)


                        class SourceId(_Entity_):
                            """
                            Source ID
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: internal_clock_id
                            
                            	Internal Clock ID
                            	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId>`
                            
                            	**config**\: False
                            
                            .. attribute:: gnss_receiver_id
                            
                            	GNSS Receiver ID
                            	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId>`
                            
                            	**config**\: False
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            	**config**\: False
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, self).__init__()

                                self.yang_name = "source-id"
                                self.yang_parent_name = "stream"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId))])
                                self._leafs = OrderedDict([
                                    ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                    ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                    ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                    ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                    ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                    ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                                ])
                                self.source_class = None
                                self.ethernet_interface = None
                                self.sonet_interface = None
                                self.ptp_node = None
                                self.satellite_access_interface = None
                                self.ntp_node = None

                                self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"

                                self.internal_clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId()
                                self.internal_clock_id.parent = self
                                self._children_name_map["internal_clock_id"] = "internal-clock-id"

                                self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId()
                                self.gnss_receiver_id.parent = self
                                self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                                self._segment_path = lambda: "source-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(_Entity_):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId']['meta_info']


                            class InternalClockId(_Entity_):
                                """
                                Internal Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId, self).__init__()

                                    self.yang_name = "internal-clock-id"
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
                                    self._segment_path = lambda: "internal-clock-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.InternalClockId']['meta_info']


                            class GnssReceiverId(_Entity_):
                                """
                                GNSS Receiver ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                .. attribute:: id
                                
                                	ID (port number for clock interface, receiver number for GNSS receiver)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: clock_name
                                
                                	Name
                                	**type**\: str
                                
                                	**length:** 0..144
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.GnssReceiverId']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId']['meta_info']


                        class SelectionPointId(_Entity_):
                            """
                            Selection point ID
                            
                            .. attribute:: selection_point
                            
                            	Last selection point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint>`
                            
                            	**config**\: False
                            
                            .. attribute:: output_id
                            
                            	Output ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId, ['output_id'], name, value)


                            class SelectionPoint(_Entity_):
                                """
                                Last selection point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2017-10-20'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream']['meta_info']


                    class OriginalSource(_Entity_):
                        """
                        Original source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_clock_id
                        
                        	Internal Clock ID
                        	**type**\:  :py:class:`InternalClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId>`
                        
                        	**config**\: False
                        
                        .. attribute:: gnss_receiver_id
                        
                        	GNSS Receiver ID
                        	**type**\:  :py:class:`GnssReceiverId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        	**config**\: False
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, self).__init__()

                            self.yang_name = "original-source"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-id", ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId)), ("internal-clock-id", ("internal_clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId)), ("gnss-receiver-id", ("gnss_receiver_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId))])
                            self._leafs = OrderedDict([
                                ('source_class', (YLeaf(YType.enumeration, 'source-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper', 'FsyncBagSourceClass', '')])),
                                ('ethernet_interface', (YLeaf(YType.str, 'ethernet-interface'), ['str'])),
                                ('sonet_interface', (YLeaf(YType.str, 'sonet-interface'), ['str'])),
                                ('ptp_node', (YLeaf(YType.str, 'ptp-node'), ['str'])),
                                ('satellite_access_interface', (YLeaf(YType.str, 'satellite-access-interface'), ['str'])),
                                ('ntp_node', (YLeaf(YType.str, 'ntp-node'), ['str'])),
                            ])
                            self.source_class = None
                            self.ethernet_interface = None
                            self.sonet_interface = None
                            self.ptp_node = None
                            self.satellite_access_interface = None
                            self.ntp_node = None

                            self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"

                            self.internal_clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId()
                            self.internal_clock_id.parent = self
                            self._children_name_map["internal_clock_id"] = "internal-clock-id"

                            self.gnss_receiver_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId()
                            self.gnss_receiver_id.parent = self
                            self._children_name_map["gnss_receiver_id"] = "gnss-receiver-id"
                            self._segment_path = lambda: "original-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(_Entity_):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId']['meta_info']


                        class InternalClockId(_Entity_):
                            """
                            Internal Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId, self).__init__()

                                self.yang_name = "internal-clock-id"
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
                                self._segment_path = lambda: "internal-clock-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.InternalClockId']['meta_info']


                        class GnssReceiverId(_Entity_):
                            """
                            GNSS Receiver ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: id
                            
                            	ID (port number for clock interface, receiver number for GNSS receiver)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: clock_name
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 0..144
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2017-10-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId, ['node', 'id', 'clock_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                                return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.GnssReceiverId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource']['meta_info']


                    class QualityLevel(_Entity_):
                        """
                        Quality Level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        	**config**\: False
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        	**config**\: False
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2017-10-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                            return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                        return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                    return meta._meta_table['FrequencySynchronization.Nodes.Node.SelectionPointInputs']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
                return meta._meta_table['FrequencySynchronization.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
            return meta._meta_table['FrequencySynchronization.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = FrequencySynchronization()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_freqsync_oper as meta
        return meta._meta_table['FrequencySynchronization']['meta_info']


