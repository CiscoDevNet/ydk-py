""" Cisco_IOS_XR_ptp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ptp package operational data.

This module contains definitions
for the following management objects\:
  ptp\: PTP operational data

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['ImStateEnum']


class PtpBagClockLeapSeconds(Enum):
    """
    PtpBagClockLeapSeconds (Enum Class)

    Leap Seconds

    .. data:: none = 0

    	No leap second

    .. data:: leap59 = 1

    	The last minute of the day has 59 seconds

    .. data:: leap61 = 2

    	The last minute of the day has 61 seconds

    """

    none = Enum.YLeaf(0, "none")

    leap59 = Enum.YLeaf(1, "leap59")

    leap61 = Enum.YLeaf(2, "leap61")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagClockLeapSeconds']


class PtpBagClockTimeSource(Enum):
    """
    PtpBagClockTimeSource (Enum Class)

    Time source

    .. data:: unknown = 0

    	Unknown

    .. data:: atomic = 16

    	Atomic clock

    .. data:: gps = 32

    	GPS clock

    .. data:: terrestrial_radio = 48

    	Terrestrial Radio

    .. data:: ptp = 64

    	Precision Time Protocol

    .. data:: ntp = 80

    	Network Time Protocol

    .. data:: hand_set = 96

    	Hand set

    .. data:: other = 144

    	Other Time Source

    .. data:: internal_oscillator = 160

    	Internal Oscillator

    """

    unknown = Enum.YLeaf(0, "unknown")

    atomic = Enum.YLeaf(16, "atomic")

    gps = Enum.YLeaf(32, "gps")

    terrestrial_radio = Enum.YLeaf(48, "terrestrial-radio")

    ptp = Enum.YLeaf(64, "ptp")

    ntp = Enum.YLeaf(80, "ntp")

    hand_set = Enum.YLeaf(96, "hand-set")

    other = Enum.YLeaf(144, "other")

    internal_oscillator = Enum.YLeaf(160, "internal-oscillator")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagClockTimeSource']


class PtpBagClockTimescale(Enum):
    """
    PtpBagClockTimescale (Enum Class)

    Timescale

    .. data:: ptp = 0

    	PTP timescale

    .. data:: arb = 1

    	ARB timescale

    """

    ptp = Enum.YLeaf(0, "ptp")

    arb = Enum.YLeaf(1, "arb")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagClockTimescale']


class PtpBagCommunicationModel(Enum):
    """
    PtpBagCommunicationModel (Enum Class)

    Communication Model

    .. data:: unicast = 0

    	Unication communication

    .. data:: mixed_mode = 1

    	Mixed-mode communication

    .. data:: multicast = 2

    	Multicast communication

    """

    unicast = Enum.YLeaf(0, "unicast")

    mixed_mode = Enum.YLeaf(1, "mixed-mode")

    multicast = Enum.YLeaf(2, "multicast")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagCommunicationModel']


class PtpBagDelayMechanism(Enum):
    """
    PtpBagDelayMechanism (Enum Class)

    Delay Mechanism

    .. data:: e2e = 0

    	End to end delay mechanism

    .. data:: p2p = 1

    	Peer to peer delay mechanism

    """

    e2e = Enum.YLeaf(0, "e2e")

    p2p = Enum.YLeaf(1, "p2p")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagDelayMechanism']


class PtpBagEncap(Enum):
    """
    PtpBagEncap (Enum Class)

    Encapsulation

    .. data:: unknown = 0

    	Unknown encapsulation

    .. data:: ethernet = 1

    	Ethernet encapsulation

    .. data:: ipv4 = 2

    	IPv4 encapsulation

    .. data:: ipv6 = 3

    	IPv6 encapsulation

    """

    unknown = Enum.YLeaf(0, "unknown")

    ethernet = Enum.YLeaf(1, "ethernet")

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(3, "ipv6")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagEncap']


class PtpBagPortState(Enum):
    """
    PtpBagPortState (Enum Class)

    Port State

    .. data:: initializing = 0

    	Initializing state

    .. data:: listen = 1

    	Listen state

    .. data:: passive = 2

    	Passive state

    .. data:: pre_master = 3

    	Pre-Master state

    .. data:: master = 4

    	Master state

    .. data:: uncalibrated = 5

    	Uncalibrated state

    .. data:: slave = 6

    	Slave state

    .. data:: faulty = 7

    	Faulty state

    """

    initializing = Enum.YLeaf(0, "initializing")

    listen = Enum.YLeaf(1, "listen")

    passive = Enum.YLeaf(2, "passive")

    pre_master = Enum.YLeaf(3, "pre-master")

    master = Enum.YLeaf(4, "master")

    uncalibrated = Enum.YLeaf(5, "uncalibrated")

    slave = Enum.YLeaf(6, "slave")

    faulty = Enum.YLeaf(7, "faulty")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagPortState']


class PtpBagProfile(Enum):
    """
    PtpBagProfile (Enum Class)

    Profile

    .. data:: default = 0

    	1588v2 profile (default)

    .. data:: g82651 = 1

    	G.8265.1 profile

    .. data:: g82751 = 2

    	G.8275.1 profile

    .. data:: g82752 = 3

    	G.8275.2 profile

    """

    default = Enum.YLeaf(0, "default")

    g82651 = Enum.YLeaf(1, "g82651")

    g82751 = Enum.YLeaf(2, "g82751")

    g82752 = Enum.YLeaf(3, "g82752")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagProfile']


class PtpBagRestrictPortState(Enum):
    """
    PtpBagRestrictPortState (Enum Class)

    Restrict Port State

    .. data:: any = 0

    	Any

    .. data:: slave_only = 1

    	Slave only

    .. data:: master_only = 2

    	Master only

    """

    any = Enum.YLeaf(0, "any")

    slave_only = Enum.YLeaf(1, "slave-only")

    master_only = Enum.YLeaf(2, "master-only")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagRestrictPortState']


class PtpBagTelecomClock(Enum):
    """
    PtpBagTelecomClock (Enum Class)

    Telecom Clock

    .. data:: grandmaster = 0

    	Grandmaster

    .. data:: boundary = 1

    	Boundary

    .. data:: slave = 2

    	Slave

    """

    grandmaster = Enum.YLeaf(0, "grandmaster")

    boundary = Enum.YLeaf(1, "boundary")

    slave = Enum.YLeaf(2, "slave")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['PtpBagTelecomClock']



class Ptp(_Entity_):
    """
    PTP operational data
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes>`
    
    	**config**\: False
    
    .. attribute:: summary
    
    	Summary operational data
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Summary>`
    
    	**config**\: False
    
    .. attribute:: interface_configuration_errors
    
    	Table for interface configuration error operational data
    	**type**\:  :py:class:`InterfaceConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors>`
    
    	**config**\: False
    
    .. attribute:: interface_foreign_masters
    
    	Table for interface foreign master clock operational data
    	**type**\:  :py:class:`InterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters>`
    
    	**config**\: False
    
    .. attribute:: interface_interops
    
    	Table for interface interop operational data
    	**type**\:  :py:class:`InterfaceInterops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops>`
    
    	**config**\: False
    
    .. attribute:: local_clock
    
    	Local clock operational data
    	**type**\:  :py:class:`LocalClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock>`
    
    	**config**\: False
    
    .. attribute:: interface_packet_counters
    
    	Table for interface packet counter operational data
    	**type**\:  :py:class:`InterfacePacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters>`
    
    	**config**\: False
    
    .. attribute:: advertised_clock
    
    	Advertised clock operational data
    	**type**\:  :py:class:`AdvertisedClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock>`
    
    	**config**\: False
    
    .. attribute:: interfaces
    
    	Table for interface operational data
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces>`
    
    	**config**\: False
    
    .. attribute:: dataset
    
    	Global PTP datasets
    	**type**\:  :py:class:`Dataset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset>`
    
    	**config**\: False
    
    .. attribute:: global_configuration_error
    
    	Global configuration error operational data
    	**type**\:  :py:class:`GlobalConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError>`
    
    	**config**\: False
    
    .. attribute:: grandmaster
    
    	Grandmaster clock operational data
    	**type**\:  :py:class:`Grandmaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster>`
    
    	**config**\: False
    
    .. attribute:: interface_unicast_peers
    
    	Table for interface unicast peers operational data
    	**type**\:  :py:class:`InterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers>`
    
    	**config**\: False
    
    .. attribute:: utc_offset_info
    
    	UTC offset information
    	**type**\:  :py:class:`UtcOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ptp-oper'
    _revision = '2017-02-02'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ptp, self).__init__()
        self._top_entity = None

        self.yang_name = "ptp"
        self.yang_parent_name = "Cisco-IOS-XR-ptp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ptp.Nodes)), ("summary", ("summary", Ptp.Summary)), ("interface-configuration-errors", ("interface_configuration_errors", Ptp.InterfaceConfigurationErrors)), ("interface-foreign-masters", ("interface_foreign_masters", Ptp.InterfaceForeignMasters)), ("interface-interops", ("interface_interops", Ptp.InterfaceInterops)), ("local-clock", ("local_clock", Ptp.LocalClock)), ("interface-packet-counters", ("interface_packet_counters", Ptp.InterfacePacketCounters)), ("advertised-clock", ("advertised_clock", Ptp.AdvertisedClock)), ("interfaces", ("interfaces", Ptp.Interfaces)), ("dataset", ("dataset", Ptp.Dataset)), ("global-configuration-error", ("global_configuration_error", Ptp.GlobalConfigurationError)), ("grandmaster", ("grandmaster", Ptp.Grandmaster)), ("interface-unicast-peers", ("interface_unicast_peers", Ptp.InterfaceUnicastPeers)), ("utc-offset-info", ("utc_offset_info", Ptp.UtcOffsetInfo))])
        self._leafs = OrderedDict()

        self.nodes = Ptp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.summary = Ptp.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.interface_configuration_errors = Ptp.InterfaceConfigurationErrors()
        self.interface_configuration_errors.parent = self
        self._children_name_map["interface_configuration_errors"] = "interface-configuration-errors"

        self.interface_foreign_masters = Ptp.InterfaceForeignMasters()
        self.interface_foreign_masters.parent = self
        self._children_name_map["interface_foreign_masters"] = "interface-foreign-masters"

        self.interface_interops = Ptp.InterfaceInterops()
        self.interface_interops.parent = self
        self._children_name_map["interface_interops"] = "interface-interops"

        self.local_clock = Ptp.LocalClock()
        self.local_clock.parent = self
        self._children_name_map["local_clock"] = "local-clock"

        self.interface_packet_counters = Ptp.InterfacePacketCounters()
        self.interface_packet_counters.parent = self
        self._children_name_map["interface_packet_counters"] = "interface-packet-counters"

        self.advertised_clock = Ptp.AdvertisedClock()
        self.advertised_clock.parent = self
        self._children_name_map["advertised_clock"] = "advertised-clock"

        self.interfaces = Ptp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.dataset = Ptp.Dataset()
        self.dataset.parent = self
        self._children_name_map["dataset"] = "dataset"

        self.global_configuration_error = Ptp.GlobalConfigurationError()
        self.global_configuration_error.parent = self
        self._children_name_map["global_configuration_error"] = "global-configuration-error"

        self.grandmaster = Ptp.Grandmaster()
        self.grandmaster.parent = self
        self._children_name_map["grandmaster"] = "grandmaster"

        self.interface_unicast_peers = Ptp.InterfaceUnicastPeers()
        self.interface_unicast_peers.parent = self
        self._children_name_map["interface_unicast_peers"] = "interface-unicast-peers"

        self.utc_offset_info = Ptp.UtcOffsetInfo()
        self.utc_offset_info.parent = self
        self._children_name_map["utc_offset_info"] = "utc-offset-info"
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ptp, [], name, value)


    class Nodes(_Entity_):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific operational data for a given node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ptp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node\-specific operational data for a given node
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: node_interface_foreign_masters
            
            	Table for node foreign master clock operational data
            	**type**\:  :py:class:`NodeInterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters>`
            
            	**config**\: False
            
            .. attribute:: summary
            
            	Node summary operational data
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.Summary>`
            
            	**config**\: False
            
            .. attribute:: node_interfaces
            
            	Table for node interface operational data
            	**type**\:  :py:class:`NodeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces>`
            
            	**config**\: False
            
            .. attribute:: node_interface_unicast_peers
            
            	Table for node unicast peers operational data
            	**type**\:  :py:class:`NodeInterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers>`
            
            	**config**\: False
            
            .. attribute:: packet_counters
            
            	Node packet counter operational data
            	**type**\:  :py:class:`PacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("node-interface-foreign-masters", ("node_interface_foreign_masters", Ptp.Nodes.Node.NodeInterfaceForeignMasters)), ("summary", ("summary", Ptp.Nodes.Node.Summary)), ("node-interfaces", ("node_interfaces", Ptp.Nodes.Node.NodeInterfaces)), ("node-interface-unicast-peers", ("node_interface_unicast_peers", Ptp.Nodes.Node.NodeInterfaceUnicastPeers)), ("packet-counters", ("packet_counters", Ptp.Nodes.Node.PacketCounters))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.node_interface_foreign_masters = Ptp.Nodes.Node.NodeInterfaceForeignMasters()
                self.node_interface_foreign_masters.parent = self
                self._children_name_map["node_interface_foreign_masters"] = "node-interface-foreign-masters"

                self.summary = Ptp.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.node_interfaces = Ptp.Nodes.Node.NodeInterfaces()
                self.node_interfaces.parent = self
                self._children_name_map["node_interfaces"] = "node-interfaces"

                self.node_interface_unicast_peers = Ptp.Nodes.Node.NodeInterfaceUnicastPeers()
                self.node_interface_unicast_peers.parent = self
                self._children_name_map["node_interface_unicast_peers"] = "node-interface-unicast-peers"

                self.packet_counters = Ptp.Nodes.Node.PacketCounters()
                self.packet_counters.parent = self
                self._children_name_map["packet_counters"] = "packet-counters"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Nodes.Node, ['node_name'], name, value)


            class NodeInterfaceForeignMasters(_Entity_):
                """
                Table for node foreign master clock
                operational data
                
                .. attribute:: node_interface_foreign_master
                
                	Node interface foreign master clock operational data
                	**type**\: list of  		 :py:class:`NodeInterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters, self).__init__()

                    self.yang_name = "node-interface-foreign-masters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-interface-foreign-master", ("node_interface_foreign_master", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster))])
                    self._leafs = OrderedDict()

                    self.node_interface_foreign_master = YList(self)
                    self._segment_path = lambda: "node-interface-foreign-masters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters, [], name, value)


                class NodeInterfaceForeignMaster(_Entity_):
                    """
                    Node interface foreign master clock
                    operational data
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: foreign_clock
                    
                    	Foreign clocks received on this interface
                    	**type**\: list of  		 :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster, self).__init__()

                        self.yang_name = "node-interface-foreign-master"
                        self.yang_parent_name = "node-interface-foreign-masters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("foreign-clock", ("foreign_clock", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                        ])
                        self.interface_name = None
                        self.port_number = None

                        self.foreign_clock = YList(self)
                        self._segment_path = lambda: "node-interface-foreign-master" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster, ['interface_name', 'port_number'], name, value)


                    class ForeignClock(_Entity_):
                        """
                        Foreign clocks received on this interface
                        
                        .. attribute:: foreign_clock
                        
                        	Foreign clock information
                        	**type**\:  :py:class:`ForeignClock_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_>`
                        
                        	**config**\: False
                        
                        .. attribute:: address
                        
                        	The address of the clock
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address>`
                        
                        	**config**\: False
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                        
                        	**config**\: False
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant>`
                        
                        	**config**\: False
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_qualified
                        
                        	The clock is qualified for best master clock selection
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_grandmaster
                        
                        	This clock is the currently selected grand master clock
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: communication_model
                        
                        	The communication model configured on this clock
                        	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_known
                        
                        	This clock is known by this router
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: time_known_for
                        
                        	How long the clock has been known by this router for, in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: foreign_domain
                        
                        	The PTP domain that the foreign clock is in
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: configured_priority
                        
                        	Priority configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: configured_clock_class
                        
                        	Clock class configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: delay_asymmetry
                        
                        	Delay asymmetry configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_dnu
                        
                        	The clock has clock class corresponding to QL\-DNU
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, self).__init__()

                            self.yang_name = "foreign-clock"
                            self.yang_parent_name = "node-interface-foreign-master"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("foreign-clock", ("foreign_clock", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_)), ("address", ("address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address)), ("announce-grant", ("announce_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant)), ("sync-grant", ("sync_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant)), ("delay-response-grant", ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant))])
                            self._leafs = OrderedDict([
                                ('is_qualified', (YLeaf(YType.boolean, 'is-qualified'), ['bool'])),
                                ('is_grandmaster', (YLeaf(YType.boolean, 'is-grandmaster'), ['bool'])),
                                ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                                ('is_known', (YLeaf(YType.boolean, 'is-known'), ['bool'])),
                                ('time_known_for', (YLeaf(YType.uint32, 'time-known-for'), ['int'])),
                                ('foreign_domain', (YLeaf(YType.uint8, 'foreign-domain'), ['int'])),
                                ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                                ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                                ('delay_asymmetry', (YLeaf(YType.int32, 'delay-asymmetry'), ['int'])),
                                ('ptsf_loss_announce', (YLeaf(YType.boolean, 'ptsf-loss-announce'), ['bool'])),
                                ('ptsf_loss_sync', (YLeaf(YType.boolean, 'ptsf-loss-sync'), ['bool'])),
                                ('is_dnu', (YLeaf(YType.boolean, 'is-dnu'), ['bool'])),
                            ])
                            self.is_qualified = None
                            self.is_grandmaster = None
                            self.communication_model = None
                            self.is_known = None
                            self.time_known_for = None
                            self.foreign_domain = None
                            self.configured_priority = None
                            self.configured_clock_class = None
                            self.delay_asymmetry = None
                            self.ptsf_loss_announce = None
                            self.ptsf_loss_sync = None
                            self.is_dnu = None

                            self.foreign_clock = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_()
                            self.foreign_clock.parent = self
                            self._children_name_map["foreign_clock"] = "foreign-clock"

                            self.address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._segment_path = lambda: "foreign-clock"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, ['is_qualified', 'is_grandmaster', 'communication_model', 'is_known', 'time_known_for', 'foreign_domain', 'configured_priority', 'configured_clock_class', 'delay_asymmetry', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_dnu'], name, value)


                        class ForeignClock_(_Entity_):
                            """
                            Foreign clock information
                            
                            .. attribute:: utc_offset
                            
                            	UTC offset
                            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset>`
                            
                            	**config**\: False
                            
                            .. attribute:: receiver
                            
                            	Receiver
                            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver>`
                            
                            	**config**\: False
                            
                            .. attribute:: sender
                            
                            	Sender
                            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender>`
                            
                            	**config**\: False
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: priority1
                            
                            	Priority 1
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: priority2
                            
                            	Priority 2
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: class_
                            
                            	Class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: accuracy
                            
                            	Accuracy
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: offset_log_variance
                            
                            	Offset log variance
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: steps_removed
                            
                            	Steps removed
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: time_source
                            
                            	Time source
                            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                            
                            	**config**\: False
                            
                            .. attribute:: frequency_traceable
                            
                            	The clock is frequency traceable
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: time_traceable
                            
                            	The clock is time traceable
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: timescale
                            
                            	Timescale
                            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                            
                            	**config**\: False
                            
                            .. attribute:: leap_seconds
                            
                            	Leap Seconds
                            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                            
                            	**config**\: False
                            
                            	**units**\: second
                            
                            .. attribute:: local
                            
                            	The clock is the local clock
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: configured_clock_class
                            
                            	The configured clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: configured_priority
                            
                            	The configured priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_, self).__init__()

                                self.yang_name = "foreign-clock"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("utc-offset", ("utc_offset", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset)), ("receiver", ("receiver", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver)), ("sender", ("sender", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender))])
                                self._leafs = OrderedDict([
                                    ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                                    ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                                    ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                                    ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                                    ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                                    ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                                    ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                                    ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                                    ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
                                    ('leap_seconds', (YLeaf(YType.enumeration, 'leap-seconds'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockLeapSeconds', '')])),
                                    ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                                    ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                                    ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                                ])
                                self.clock_id = None
                                self.priority1 = None
                                self.priority2 = None
                                self.class_ = None
                                self.accuracy = None
                                self.offset_log_variance = None
                                self.steps_removed = None
                                self.time_source = None
                                self.frequency_traceable = None
                                self.time_traceable = None
                                self.timescale = None
                                self.leap_seconds = None
                                self.local = None
                                self.configured_clock_class = None
                                self.configured_priority = None

                                self.utc_offset = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset()
                                self.utc_offset.parent = self
                                self._children_name_map["utc_offset"] = "utc-offset"

                                self.receiver = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver()
                                self.receiver.parent = self
                                self._children_name_map["receiver"] = "receiver"

                                self.sender = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender()
                                self.sender.parent = self
                                self._children_name_map["sender"] = "sender"
                                self._segment_path = lambda: "foreign-clock"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


                            class UtcOffset(_Entity_):
                                """
                                UTC offset
                                
                                .. attribute:: current_offset
                                
                                	Current offset
                                	**type**\: int
                                
                                	**range:** \-32768..32767
                                
                                	**config**\: False
                                
                                .. attribute:: offset_valid
                                
                                	The current offset is valid
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset, self).__init__()

                                    self.yang_name = "utc-offset"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('current_offset', (YLeaf(YType.int16, 'current-offset'), ['int'])),
                                        ('offset_valid', (YLeaf(YType.boolean, 'offset-valid'), ['bool'])),
                                    ])
                                    self.current_offset = None
                                    self.offset_valid = None
                                    self._segment_path = lambda: "utc-offset"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset, ['current_offset', 'offset_valid'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset']['meta_info']


                            class Receiver(_Entity_):
                                """
                                Receiver
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver, self).__init__()

                                    self.yang_name = "receiver"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                                    ])
                                    self.clock_id = None
                                    self.port_number = None
                                    self._segment_path = lambda: "receiver"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver, ['clock_id', 'port_number'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver']['meta_info']


                            class Sender(_Entity_):
                                """
                                Sender
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender, self).__init__()

                                    self.yang_name = "sender"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                                    ])
                                    self.clock_id = None
                                    self.port_number = None
                                    self._segment_path = lambda: "sender"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender, ['clock_id', 'port_number'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_.Sender']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock_']['meta_info']


                        class Address(_Entity_):
                            """
                            The address of the clock
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                            
                            	**config**\: False
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address))])
                                self._leafs = OrderedDict([
                                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                                    ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ])
                                self.encapsulation = None
                                self.address_unknown = None
                                self.ipv4_address = None

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(_Entity_):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                                    ])
                                    self.macaddr = None
                                    self._segment_path = lambda: "mac-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress, ['macaddr'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress']['meta_info']


                            class Ipv6Address(_Entity_):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ])
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "ipv6-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address, ['ipv6_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address']['meta_info']


                        class AnnounceGrant(_Entity_):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant, self).__init__()

                                self.yang_name = "announce-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "announce-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant']['meta_info']


                        class SyncGrant(_Entity_):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant, self).__init__()

                                self.yang_name = "sync-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "sync-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant']['meta_info']


                        class DelayResponseGrant(_Entity_):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant, self).__init__()

                                self.yang_name = "delay-response-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "delay-response-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceForeignMasters']['meta_info']


            class Summary(_Entity_):
                """
                Node summary operational data
                
                .. attribute:: port_state_init_count
                
                	Number of interfaces in 'Init' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_listening_count
                
                	Number of interfaces in 'Listening' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_passive_count
                
                	Number of interfaces in 'Passive' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_pre_master_count
                
                	Number of interfaces in 'Pre\-Master' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_master_count
                
                	Number of interfaces in 'Master' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_slave_count
                
                	Number of interfaces in 'Slave' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_uncalibrated_count
                
                	Number of interfaces in 'Uncalibrated port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_state_faulty_count
                
                	Number of interfaces in 'Faulty' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_interfaces
                
                	Total number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_interfaces_valid_port_num
                
                	Total number of interfaces with a valid port number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port_state_init_count', (YLeaf(YType.uint32, 'port-state-init-count'), ['int'])),
                        ('port_state_listening_count', (YLeaf(YType.uint32, 'port-state-listening-count'), ['int'])),
                        ('port_state_passive_count', (YLeaf(YType.uint32, 'port-state-passive-count'), ['int'])),
                        ('port_state_pre_master_count', (YLeaf(YType.uint32, 'port-state-pre-master-count'), ['int'])),
                        ('port_state_master_count', (YLeaf(YType.uint32, 'port-state-master-count'), ['int'])),
                        ('port_state_slave_count', (YLeaf(YType.uint32, 'port-state-slave-count'), ['int'])),
                        ('port_state_uncalibrated_count', (YLeaf(YType.uint32, 'port-state-uncalibrated-count'), ['int'])),
                        ('port_state_faulty_count', (YLeaf(YType.uint32, 'port-state-faulty-count'), ['int'])),
                        ('total_interfaces', (YLeaf(YType.uint32, 'total-interfaces'), ['int'])),
                        ('total_interfaces_valid_port_num', (YLeaf(YType.uint32, 'total-interfaces-valid-port-num'), ['int'])),
                    ])
                    self.port_state_init_count = None
                    self.port_state_listening_count = None
                    self.port_state_passive_count = None
                    self.port_state_pre_master_count = None
                    self.port_state_master_count = None
                    self.port_state_slave_count = None
                    self.port_state_uncalibrated_count = None
                    self.port_state_faulty_count = None
                    self.total_interfaces = None
                    self.total_interfaces_valid_port_num = None
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.Summary, ['port_state_init_count', 'port_state_listening_count', 'port_state_passive_count', 'port_state_pre_master_count', 'port_state_master_count', 'port_state_slave_count', 'port_state_uncalibrated_count', 'port_state_faulty_count', 'total_interfaces', 'total_interfaces_valid_port_num'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Nodes.Node.Summary']['meta_info']


            class NodeInterfaces(_Entity_):
                """
                Table for node interface operational data
                
                .. attribute:: node_interface
                
                	Node interface operational data
                	**type**\: list of  		 :py:class:`NodeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Nodes.Node.NodeInterfaces, self).__init__()

                    self.yang_name = "node-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-interface", ("node_interface", Ptp.Nodes.Node.NodeInterfaces.NodeInterface))])
                    self._leafs = OrderedDict()

                    self.node_interface = YList(self)
                    self._segment_path = lambda: "node-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces, [], name, value)


                class NodeInterface(_Entity_):
                    """
                    Node interface operational data
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address_array
                    
                    	List of Ipv6 addresses, if IPv6 encapsulation is being used. If a source address is configured, this is the only item in the list
                    	**type**\:  :py:class:`Ipv6AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address_array
                    
                    	List of IPv4 addresses, if IPv4 encapsulation is being used. The first address is the primary address. If a source address is configured, this is the only item in the list
                    	**type**\:  :py:class:`Ipv4AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray>`
                    
                    	**config**\: False
                    
                    .. attribute:: mac_address
                    
                    	MAC address, if Ethernet encapsulation is being used
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ingress_conversion
                    
                    	Details of any ingress conversion
                    	**type**\:  :py:class:`IngressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion>`
                    
                    	**config**\: False
                    
                    .. attribute:: egress_conversion
                    
                    	Details of any egress conversion
                    	**type**\:  :py:class:`EgressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion>`
                    
                    	**config**\: False
                    
                    .. attribute:: port_state
                    
                    	Port state
                    	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                    
                    	**config**\: False
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: line_state
                    
                    	Line state
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.ImStateEnum>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	Ipv6 address, if IPv6 encapsulation is being used
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address, if IPv4 encapsulation is being used
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: two_step
                    
                    	Two step delay\-request mechanism is being used
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: communication_model
                    
                    	Communication model configured on the interface
                    	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                    
                    	**config**\: False
                    
                    .. attribute:: log_sync_interval
                    
                    	Log of the interface's sync interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: log_announce_interval
                    
                    	Log of the interface's announce interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: announce_timeout
                    
                    	Announce timeout
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: log_min_delay_request_interval
                    
                    	Log of the interface's Minimum delay\-request interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: configured_port_state
                    
                    	The configured port state
                    	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
                    
                    	**config**\: False
                    
                    .. attribute:: supports_unicast
                    
                    	The interface supports unicast
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_master
                    
                    	The interface supports operation in master mode
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_one_step
                    
                    	The interface supports one\-step operation
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_two_step
                    
                    	The interface supports two\-step operation
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_ethernet
                    
                    	The interface supports ethernet transport
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_multicast
                    
                    	The interface supports multicast
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_ipv4
                    
                    	The interface supports IPv4 transport
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_ipv6
                    
                    	The interface supports IPv6 transport
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_slave
                    
                    	The interface supports operation in slave mode
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: supports_source_ip
                    
                    	The interface supports source ip configuration
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: max_sync_rate
                    
                    	The maximum rate of sync packets on the interface
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: event_cos
                    
                    	The class of service used on the interface for event messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: general_cos
                    
                    	The class of service used on the interface for general messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: event_dscp
                    
                    	The DSCP class used on the interface for event messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: general_dscp
                    
                    	The DSCP class used on the interface for general messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unicast_peers
                    
                    	The number of unicast peers known by the interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_priority
                    
                    	Local priority, for the G.8275.1 PTP profile
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: signal_fail
                    
                    	Signal fail status of the interface
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: profile_interop
                    
                    	Indicate whether profile interop is in use
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: interop_domain
                    
                    	The PTP domain that is being interoperated with
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: interop_profile
                    
                    	Profile that is being interoperated with
                    	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
                    
                    	**config**\: False
                    
                    .. attribute:: master_table
                    
                    	The interface's master table
                    	**type**\: list of  		 :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface, self).__init__()

                        self.yang_name = "node-interface"
                        self.yang_parent_name = "node-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("ipv6-address-array", ("ipv6_address_array", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray)), ("ipv4-address-array", ("ipv4_address_array", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray)), ("mac-address", ("mac_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress)), ("ingress-conversion", ("ingress_conversion", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion)), ("egress-conversion", ("egress_conversion", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion)), ("master-table", ("master_table", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('port_state', (YLeaf(YType.enumeration, 'port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagPortState', '')])),
                            ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                            ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'ImStateEnum', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('two_step', (YLeaf(YType.boolean, 'two-step'), ['bool'])),
                            ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                            ('log_sync_interval', (YLeaf(YType.int32, 'log-sync-interval'), ['int'])),
                            ('log_announce_interval', (YLeaf(YType.int32, 'log-announce-interval'), ['int'])),
                            ('announce_timeout', (YLeaf(YType.uint32, 'announce-timeout'), ['int'])),
                            ('log_min_delay_request_interval', (YLeaf(YType.int32, 'log-min-delay-request-interval'), ['int'])),
                            ('configured_port_state', (YLeaf(YType.enumeration, 'configured-port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagRestrictPortState', '')])),
                            ('supports_unicast', (YLeaf(YType.boolean, 'supports-unicast'), ['bool'])),
                            ('supports_master', (YLeaf(YType.boolean, 'supports-master'), ['bool'])),
                            ('supports_one_step', (YLeaf(YType.boolean, 'supports-one-step'), ['bool'])),
                            ('supports_two_step', (YLeaf(YType.boolean, 'supports-two-step'), ['bool'])),
                            ('supports_ethernet', (YLeaf(YType.boolean, 'supports-ethernet'), ['bool'])),
                            ('supports_multicast', (YLeaf(YType.boolean, 'supports-multicast'), ['bool'])),
                            ('supports_ipv4', (YLeaf(YType.boolean, 'supports-ipv4'), ['bool'])),
                            ('supports_ipv6', (YLeaf(YType.boolean, 'supports-ipv6'), ['bool'])),
                            ('supports_slave', (YLeaf(YType.boolean, 'supports-slave'), ['bool'])),
                            ('supports_source_ip', (YLeaf(YType.boolean, 'supports-source-ip'), ['bool'])),
                            ('max_sync_rate', (YLeaf(YType.uint8, 'max-sync-rate'), ['int'])),
                            ('event_cos', (YLeaf(YType.uint32, 'event-cos'), ['int'])),
                            ('general_cos', (YLeaf(YType.uint32, 'general-cos'), ['int'])),
                            ('event_dscp', (YLeaf(YType.uint32, 'event-dscp'), ['int'])),
                            ('general_dscp', (YLeaf(YType.uint32, 'general-dscp'), ['int'])),
                            ('unicast_peers', (YLeaf(YType.uint32, 'unicast-peers'), ['int'])),
                            ('local_priority', (YLeaf(YType.uint8, 'local-priority'), ['int'])),
                            ('signal_fail', (YLeaf(YType.boolean, 'signal-fail'), ['bool'])),
                            ('profile_interop', (YLeaf(YType.boolean, 'profile-interop'), ['bool'])),
                            ('interop_domain', (YLeaf(YType.uint8, 'interop-domain'), ['int'])),
                            ('interop_profile', (YLeaf(YType.enumeration, 'interop-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                        ])
                        self.interface_name = None
                        self.port_state = None
                        self.port_number = None
                        self.line_state = None
                        self.encapsulation = None
                        self.ipv6_address = None
                        self.ipv4_address = None
                        self.two_step = None
                        self.communication_model = None
                        self.log_sync_interval = None
                        self.log_announce_interval = None
                        self.announce_timeout = None
                        self.log_min_delay_request_interval = None
                        self.configured_port_state = None
                        self.supports_unicast = None
                        self.supports_master = None
                        self.supports_one_step = None
                        self.supports_two_step = None
                        self.supports_ethernet = None
                        self.supports_multicast = None
                        self.supports_ipv4 = None
                        self.supports_ipv6 = None
                        self.supports_slave = None
                        self.supports_source_ip = None
                        self.max_sync_rate = None
                        self.event_cos = None
                        self.general_cos = None
                        self.event_dscp = None
                        self.general_dscp = None
                        self.unicast_peers = None
                        self.local_priority = None
                        self.signal_fail = None
                        self.profile_interop = None
                        self.interop_domain = None
                        self.interop_profile = None

                        self.ipv6_address_array = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray()
                        self.ipv6_address_array.parent = self
                        self._children_name_map["ipv6_address_array"] = "ipv6-address-array"

                        self.ipv4_address_array = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray()
                        self.ipv4_address_array.parent = self
                        self._children_name_map["ipv4_address_array"] = "ipv4-address-array"

                        self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ingress_conversion = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion()
                        self.ingress_conversion.parent = self
                        self._children_name_map["ingress_conversion"] = "ingress-conversion"

                        self.egress_conversion = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion()
                        self.egress_conversion.parent = self
                        self._children_name_map["egress_conversion"] = "egress-conversion"

                        self.master_table = YList(self)
                        self._segment_path = lambda: "node-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface, ['interface_name', 'port_state', 'port_number', 'line_state', 'encapsulation', 'ipv6_address', 'ipv4_address', 'two_step', 'communication_model', 'log_sync_interval', 'log_announce_interval', 'announce_timeout', 'log_min_delay_request_interval', 'configured_port_state', 'supports_unicast', 'supports_master', 'supports_one_step', 'supports_two_step', 'supports_ethernet', 'supports_multicast', 'supports_ipv4', 'supports_ipv6', 'supports_slave', 'supports_source_ip', 'max_sync_rate', 'event_cos', 'general_cos', 'event_dscp', 'general_dscp', 'unicast_peers', 'local_priority', 'signal_fail', 'profile_interop', 'interop_domain', 'interop_profile'], name, value)


                    class Ipv6AddressArray(_Entity_):
                        """
                        List of Ipv6 addresses, if IPv6 encapsulation is
                        being used. If a source address is configured,
                        this is the only item in the list
                        
                        .. attribute:: addr
                        
                        	List of IPv6 addresses
                        	**type**\: list of str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray, self).__init__()

                            self.yang_name = "ipv6-address-array"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                            ])
                            self.addr = []
                            self._segment_path = lambda: "ipv6-address-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray, ['addr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv6AddressArray']['meta_info']


                    class Ipv4AddressArray(_Entity_):
                        """
                        List of IPv4 addresses, if IPv4 encapsulation is
                        being used. The first address is the primary
                        address. If a source address is configured, this
                        is the only item in the list.
                        
                        .. attribute:: addr
                        
                        	List of IPv4 addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray, self).__init__()

                            self.yang_name = "ipv4-address-array"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                            ])
                            self.addr = []
                            self._segment_path = lambda: "ipv4-address-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray, ['addr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.Ipv4AddressArray']['meta_info']


                    class MacAddress(_Entity_):
                        """
                        MAC address, if Ethernet encapsulation is being
                        used
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress']['meta_info']


                    class IngressConversion(_Entity_):
                        """
                        Details of any ingress conversion
                        
                        .. attribute:: priority1
                        
                        	Priority 1
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: priority2
                        
                        	Priority 2
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: accuracy
                        
                        	Accuracy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: class_default
                        
                        	Class Default
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: offset_log_variance
                        
                        	Offset log variance
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: class_mapping
                        
                        	Class Mapping
                        	**type**\: list of  		 :py:class:`ClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion.ClassMapping>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion, self).__init__()

                            self.yang_name = "ingress-conversion"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class-mapping", ("class_mapping", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion.ClassMapping))])
                            self._leafs = OrderedDict([
                                ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                                ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                                ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                                ('class_default', (YLeaf(YType.uint8, 'class-default'), ['int'])),
                                ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                            ])
                            self.priority1 = None
                            self.priority2 = None
                            self.accuracy = None
                            self.class_default = None
                            self.offset_log_variance = None

                            self.class_mapping = YList(self)
                            self._segment_path = lambda: "ingress-conversion"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion, ['priority1', 'priority2', 'accuracy', 'class_default', 'offset_log_variance'], name, value)


                        class ClassMapping(_Entity_):
                            """
                            Class Mapping
                            
                            .. attribute:: from_clock_class
                            
                            	From clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: to_clock_class
                            
                            	To clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion.ClassMapping, self).__init__()

                                self.yang_name = "class-mapping"
                                self.yang_parent_name = "ingress-conversion"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                                    ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                                ])
                                self.from_clock_class = None
                                self.to_clock_class = None
                                self._segment_path = lambda: "class-mapping"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion.ClassMapping, ['from_clock_class', 'to_clock_class'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion.ClassMapping']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.IngressConversion']['meta_info']


                    class EgressConversion(_Entity_):
                        """
                        Details of any egress conversion
                        
                        .. attribute:: priority1
                        
                        	Priority 1
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: priority2
                        
                        	Priority 2
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: accuracy
                        
                        	Accuracy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: class_default
                        
                        	Class Default
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: offset_log_variance
                        
                        	Offset log variance
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: class_mapping
                        
                        	Class Mapping
                        	**type**\: list of  		 :py:class:`ClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion.ClassMapping>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion, self).__init__()

                            self.yang_name = "egress-conversion"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class-mapping", ("class_mapping", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion.ClassMapping))])
                            self._leafs = OrderedDict([
                                ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                                ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                                ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                                ('class_default', (YLeaf(YType.uint8, 'class-default'), ['int'])),
                                ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                            ])
                            self.priority1 = None
                            self.priority2 = None
                            self.accuracy = None
                            self.class_default = None
                            self.offset_log_variance = None

                            self.class_mapping = YList(self)
                            self._segment_path = lambda: "egress-conversion"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion, ['priority1', 'priority2', 'accuracy', 'class_default', 'offset_log_variance'], name, value)


                        class ClassMapping(_Entity_):
                            """
                            Class Mapping
                            
                            .. attribute:: from_clock_class
                            
                            	From clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: to_clock_class
                            
                            	To clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion.ClassMapping, self).__init__()

                                self.yang_name = "class-mapping"
                                self.yang_parent_name = "egress-conversion"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                                    ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                                ])
                                self.from_clock_class = None
                                self.to_clock_class = None
                                self._segment_path = lambda: "class-mapping"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion.ClassMapping, ['from_clock_class', 'to_clock_class'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion.ClassMapping']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.EgressConversion']['meta_info']


                    class MasterTable(_Entity_):
                        """
                        The interface's master table
                        
                        .. attribute:: address
                        
                        	The address of the master clock
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address>`
                        
                        	**config**\: False
                        
                        .. attribute:: communication_model
                        
                        	The configured communication model of the master clock
                        	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        	**config**\: False
                        
                        .. attribute:: priority
                        
                        	The priority of the master clock, if it is set
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: known
                        
                        	Whether the interface is receiving messages from this master
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: qualified
                        
                        	The master is qualified for best master clock selection
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_grandmaster
                        
                        	Whether this is the grandmaster
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_nonnegotiated
                        
                        	Whether this master uses non\-negotiated unicast
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable, self).__init__()

                            self.yang_name = "master-table"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address))])
                            self._leafs = OrderedDict([
                                ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                                ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                                ('known', (YLeaf(YType.boolean, 'known'), ['bool'])),
                                ('qualified', (YLeaf(YType.boolean, 'qualified'), ['bool'])),
                                ('is_grandmaster', (YLeaf(YType.boolean, 'is-grandmaster'), ['bool'])),
                                ('ptsf_loss_announce', (YLeaf(YType.uint8, 'ptsf-loss-announce'), ['int'])),
                                ('ptsf_loss_sync', (YLeaf(YType.uint8, 'ptsf-loss-sync'), ['int'])),
                                ('is_nonnegotiated', (YLeaf(YType.boolean, 'is-nonnegotiated'), ['bool'])),
                            ])
                            self.communication_model = None
                            self.priority = None
                            self.known = None
                            self.qualified = None
                            self.is_grandmaster = None
                            self.ptsf_loss_announce = None
                            self.ptsf_loss_sync = None
                            self.is_nonnegotiated = None

                            self.address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "master-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable, ['communication_model', 'priority', 'known', 'qualified', 'is_grandmaster', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_nonnegotiated'], name, value)


                        class Address(_Entity_):
                            """
                            The address of the master clock
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address>`
                            
                            	**config**\: False
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "master-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address))])
                                self._leafs = OrderedDict([
                                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                                    ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ])
                                self.encapsulation = None
                                self.address_unknown = None
                                self.ipv4_address = None

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(_Entity_):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                                    ])
                                    self.macaddr = None
                                    self._segment_path = lambda: "mac-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress, ['macaddr'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress']['meta_info']


                            class Ipv6Address(_Entity_):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ])
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "ipv6-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address, ['ipv6_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces.NodeInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaces']['meta_info']


            class NodeInterfaceUnicastPeers(_Entity_):
                """
                Table for node unicast peers operational data
                
                .. attribute:: node_interface_unicast_peer
                
                	Node interface unicast peers operational data
                	**type**\: list of  		 :py:class:`NodeInterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers, self).__init__()

                    self.yang_name = "node-interface-unicast-peers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-interface-unicast-peer", ("node_interface_unicast_peer", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer))])
                    self._leafs = OrderedDict()

                    self.node_interface_unicast_peer = YList(self)
                    self._segment_path = lambda: "node-interface-unicast-peers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers, [], name, value)


                class NodeInterfaceUnicastPeer(_Entity_):
                    """
                    Node interface unicast peers operational data
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: peers
                    
                    	Unicast Peers
                    	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer, self).__init__()

                        self.yang_name = "node-interface-unicast-peer"
                        self.yang_parent_name = "node-interface-unicast-peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("peers", ("peers", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                        ])
                        self.interface_name = None
                        self.name = None
                        self.port_number = None

                        self.peers = YList(self)
                        self._segment_path = lambda: "node-interface-unicast-peer" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer, ['interface_name', 'name', 'port_number'], name, value)


                    class Peers(_Entity_):
                        """
                        Unicast Peers
                        
                        .. attribute:: address
                        
                        	The address of the unicast peer
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address>`
                        
                        	**config**\: False
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant>`
                        
                        	**config**\: False
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant>`
                        
                        	**config**\: False
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers, self).__init__()

                            self.yang_name = "peers"
                            self.yang_parent_name = "node-interface-unicast-peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address)), ("announce-grant", ("announce_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant)), ("sync-grant", ("sync_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant)), ("delay-response-grant", ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant))])
                            self._leafs = OrderedDict()

                            self.address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._segment_path = lambda: "peers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers, [], name, value)


                        class Address(_Entity_):
                            """
                            The address of the unicast peer
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                            
                            	**config**\: False
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address))])
                                self._leafs = OrderedDict([
                                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                                    ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ])
                                self.encapsulation = None
                                self.address_unknown = None
                                self.ipv4_address = None

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(_Entity_):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                                    ])
                                    self.macaddr = None
                                    self._segment_path = lambda: "mac-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress, ['macaddr'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress']['meta_info']


                            class Ipv6Address(_Entity_):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ])
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "ipv6-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address, ['ipv6_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address']['meta_info']


                        class AnnounceGrant(_Entity_):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant, self).__init__()

                                self.yang_name = "announce-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "announce-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant']['meta_info']


                        class SyncGrant(_Entity_):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant, self).__init__()

                                self.yang_name = "sync-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "sync-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant']['meta_info']


                        class DelayResponseGrant(_Entity_):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            	**config**\: False
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant, self).__init__()

                                self.yang_name = "delay-response-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                                    ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                                ])
                                self.log_grant_interval = None
                                self.grant_duration = None
                                self._segment_path = lambda: "delay-response-grant"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                                return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Nodes.Node.NodeInterfaceUnicastPeers']['meta_info']


            class PacketCounters(_Entity_):
                """
                Node packet counter operational data
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.Counters>`
                
                	**config**\: False
                
                .. attribute:: drop_reasons
                
                	Drop reasons
                	**type**\:  :py:class:`DropReasons <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.DropReasons>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Nodes.Node.PacketCounters, self).__init__()

                    self.yang_name = "packet-counters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("counters", ("counters", Ptp.Nodes.Node.PacketCounters.Counters)), ("drop-reasons", ("drop_reasons", Ptp.Nodes.Node.PacketCounters.DropReasons))])
                    self._leafs = OrderedDict()

                    self.counters = Ptp.Nodes.Node.PacketCounters.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"

                    self.drop_reasons = Ptp.Nodes.Node.PacketCounters.DropReasons()
                    self.drop_reasons.parent = self
                    self._children_name_map["drop_reasons"] = "drop-reasons"
                    self._segment_path = lambda: "packet-counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.PacketCounters, [], name, value)


                class Counters(_Entity_):
                    """
                    Packet counters
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Nodes.Node.PacketCounters.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "packet-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('announce_sent', (YLeaf(YType.uint32, 'announce-sent'), ['int'])),
                            ('announce_received', (YLeaf(YType.uint32, 'announce-received'), ['int'])),
                            ('announce_dropped', (YLeaf(YType.uint32, 'announce-dropped'), ['int'])),
                            ('sync_sent', (YLeaf(YType.uint32, 'sync-sent'), ['int'])),
                            ('sync_received', (YLeaf(YType.uint32, 'sync-received'), ['int'])),
                            ('sync_dropped', (YLeaf(YType.uint32, 'sync-dropped'), ['int'])),
                            ('follow_up_sent', (YLeaf(YType.uint32, 'follow-up-sent'), ['int'])),
                            ('follow_up_received', (YLeaf(YType.uint32, 'follow-up-received'), ['int'])),
                            ('follow_up_dropped', (YLeaf(YType.uint32, 'follow-up-dropped'), ['int'])),
                            ('delay_request_sent', (YLeaf(YType.uint32, 'delay-request-sent'), ['int'])),
                            ('delay_request_received', (YLeaf(YType.uint32, 'delay-request-received'), ['int'])),
                            ('delay_request_dropped', (YLeaf(YType.uint32, 'delay-request-dropped'), ['int'])),
                            ('delay_response_sent', (YLeaf(YType.uint32, 'delay-response-sent'), ['int'])),
                            ('delay_response_received', (YLeaf(YType.uint32, 'delay-response-received'), ['int'])),
                            ('delay_response_dropped', (YLeaf(YType.uint32, 'delay-response-dropped'), ['int'])),
                            ('peer_delay_request_sent', (YLeaf(YType.uint32, 'peer-delay-request-sent'), ['int'])),
                            ('peer_delay_request_received', (YLeaf(YType.uint32, 'peer-delay-request-received'), ['int'])),
                            ('peer_delay_request_dropped', (YLeaf(YType.uint32, 'peer-delay-request-dropped'), ['int'])),
                            ('peer_delay_response_sent', (YLeaf(YType.uint32, 'peer-delay-response-sent'), ['int'])),
                            ('peer_delay_response_received', (YLeaf(YType.uint32, 'peer-delay-response-received'), ['int'])),
                            ('peer_delay_response_dropped', (YLeaf(YType.uint32, 'peer-delay-response-dropped'), ['int'])),
                            ('peer_delay_response_follow_up_sent', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-sent'), ['int'])),
                            ('peer_delay_response_follow_up_received', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-received'), ['int'])),
                            ('peer_delay_response_follow_up_dropped', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-dropped'), ['int'])),
                            ('signaling_sent', (YLeaf(YType.uint32, 'signaling-sent'), ['int'])),
                            ('signaling_received', (YLeaf(YType.uint32, 'signaling-received'), ['int'])),
                            ('signaling_dropped', (YLeaf(YType.uint32, 'signaling-dropped'), ['int'])),
                            ('management_sent', (YLeaf(YType.uint32, 'management-sent'), ['int'])),
                            ('management_received', (YLeaf(YType.uint32, 'management-received'), ['int'])),
                            ('management_dropped', (YLeaf(YType.uint32, 'management-dropped'), ['int'])),
                            ('other_packets_sent', (YLeaf(YType.uint32, 'other-packets-sent'), ['int'])),
                            ('other_packets_received', (YLeaf(YType.uint32, 'other-packets-received'), ['int'])),
                            ('other_packets_dropped', (YLeaf(YType.uint32, 'other-packets-dropped'), ['int'])),
                            ('total_packets_sent', (YLeaf(YType.uint32, 'total-packets-sent'), ['int'])),
                            ('total_packets_received', (YLeaf(YType.uint32, 'total-packets-received'), ['int'])),
                            ('total_packets_dropped', (YLeaf(YType.uint32, 'total-packets-dropped'), ['int'])),
                        ])
                        self.announce_sent = None
                        self.announce_received = None
                        self.announce_dropped = None
                        self.sync_sent = None
                        self.sync_received = None
                        self.sync_dropped = None
                        self.follow_up_sent = None
                        self.follow_up_received = None
                        self.follow_up_dropped = None
                        self.delay_request_sent = None
                        self.delay_request_received = None
                        self.delay_request_dropped = None
                        self.delay_response_sent = None
                        self.delay_response_received = None
                        self.delay_response_dropped = None
                        self.peer_delay_request_sent = None
                        self.peer_delay_request_received = None
                        self.peer_delay_request_dropped = None
                        self.peer_delay_response_sent = None
                        self.peer_delay_response_received = None
                        self.peer_delay_response_dropped = None
                        self.peer_delay_response_follow_up_sent = None
                        self.peer_delay_response_follow_up_received = None
                        self.peer_delay_response_follow_up_dropped = None
                        self.signaling_sent = None
                        self.signaling_received = None
                        self.signaling_dropped = None
                        self.management_sent = None
                        self.management_received = None
                        self.management_dropped = None
                        self.other_packets_sent = None
                        self.other_packets_received = None
                        self.other_packets_dropped = None
                        self.total_packets_sent = None
                        self.total_packets_received = None
                        self.total_packets_dropped = None
                        self._segment_path = lambda: "counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Nodes.Node.PacketCounters.Counters']['meta_info']


                class DropReasons(_Entity_):
                    """
                    Drop reasons
                    
                    .. attribute:: not_ready
                    
                    	Not ready for packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: wrong_domain
                    
                    	Wrong domain number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: too_short
                    
                    	Packet too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: looped_same_port
                    
                    	Local packet received, same port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: looped_higher_port
                    
                    	Local packet received, higher port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: looped_lower_port
                    
                    	Local packet received, lower port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_timestamp
                    
                    	No timestamp received with packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: zero_timestamp
                    
                    	Zero timestamp received with packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_tl_vs
                    
                    	Invalid TLVs received in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_for_us
                    
                    	Packet not for us
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_listening
                    
                    	Not listening for packets on this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: wrong_master
                    
                    	Packet from incorrect master
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unknown_master
                    
                    	Packet from unknown master
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_master
                    
                    	Packet only handled in Master state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_slave
                    
                    	Packet only handled in Slave state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_granted
                    
                    	Packet from peer not granted unicast
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: too_slow
                    
                    	Packet received too late
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_packet
                    
                    	Invalid packet or packet metadata
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: wrong_sequence_id
                    
                    	Unexpected sequence ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_offload_session
                    
                    	No offload session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: not_supported
                    
                    	PTP packet type not supported
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: min_clock_class
                    
                    	Clock class below minimum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: bad_clock_class
                    
                    	Illegal clock class (255) in announce messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reserved_clock_id
                    
                    	Reserved Clock ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: steps_removed
                    
                    	Steps removed too high
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: g8265_1_incompatible
                    
                    	Packet not compatible with G.8265.1 profile
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: g8275_1_incompatible
                    
                    	Packet not compatible with G.8275.1 profile
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: g8275_2_incompatible
                    
                    	Packet not compatible with G.8275.2 profile
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: incorrect_address
                    
                    	Packet sent to incorrect address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Nodes.Node.PacketCounters.DropReasons, self).__init__()

                        self.yang_name = "drop-reasons"
                        self.yang_parent_name = "packet-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('not_ready', (YLeaf(YType.uint32, 'not-ready'), ['int'])),
                            ('wrong_domain', (YLeaf(YType.uint32, 'wrong-domain'), ['int'])),
                            ('too_short', (YLeaf(YType.uint32, 'too-short'), ['int'])),
                            ('looped_same_port', (YLeaf(YType.uint32, 'looped-same-port'), ['int'])),
                            ('looped_higher_port', (YLeaf(YType.uint32, 'looped-higher-port'), ['int'])),
                            ('looped_lower_port', (YLeaf(YType.uint32, 'looped-lower-port'), ['int'])),
                            ('no_timestamp', (YLeaf(YType.uint32, 'no-timestamp'), ['int'])),
                            ('zero_timestamp', (YLeaf(YType.uint32, 'zero-timestamp'), ['int'])),
                            ('invalid_tl_vs', (YLeaf(YType.uint32, 'invalid-tl-vs'), ['int'])),
                            ('not_for_us', (YLeaf(YType.uint32, 'not-for-us'), ['int'])),
                            ('not_listening', (YLeaf(YType.uint32, 'not-listening'), ['int'])),
                            ('wrong_master', (YLeaf(YType.uint32, 'wrong-master'), ['int'])),
                            ('unknown_master', (YLeaf(YType.uint32, 'unknown-master'), ['int'])),
                            ('not_master', (YLeaf(YType.uint32, 'not-master'), ['int'])),
                            ('not_slave', (YLeaf(YType.uint32, 'not-slave'), ['int'])),
                            ('not_granted', (YLeaf(YType.uint32, 'not-granted'), ['int'])),
                            ('too_slow', (YLeaf(YType.uint32, 'too-slow'), ['int'])),
                            ('invalid_packet', (YLeaf(YType.uint32, 'invalid-packet'), ['int'])),
                            ('wrong_sequence_id', (YLeaf(YType.uint32, 'wrong-sequence-id'), ['int'])),
                            ('no_offload_session', (YLeaf(YType.uint32, 'no-offload-session'), ['int'])),
                            ('not_supported', (YLeaf(YType.uint32, 'not-supported'), ['int'])),
                            ('min_clock_class', (YLeaf(YType.uint32, 'min-clock-class'), ['int'])),
                            ('bad_clock_class', (YLeaf(YType.uint32, 'bad-clock-class'), ['int'])),
                            ('reserved_clock_id', (YLeaf(YType.uint32, 'reserved-clock-id'), ['int'])),
                            ('steps_removed', (YLeaf(YType.uint32, 'steps-removed'), ['int'])),
                            ('g8265_1_incompatible', (YLeaf(YType.uint32, 'g8265-1-incompatible'), ['int'])),
                            ('g8275_1_incompatible', (YLeaf(YType.uint32, 'g8275-1-incompatible'), ['int'])),
                            ('g8275_2_incompatible', (YLeaf(YType.uint32, 'g8275-2-incompatible'), ['int'])),
                            ('incorrect_address', (YLeaf(YType.uint32, 'incorrect-address'), ['int'])),
                        ])
                        self.not_ready = None
                        self.wrong_domain = None
                        self.too_short = None
                        self.looped_same_port = None
                        self.looped_higher_port = None
                        self.looped_lower_port = None
                        self.no_timestamp = None
                        self.zero_timestamp = None
                        self.invalid_tl_vs = None
                        self.not_for_us = None
                        self.not_listening = None
                        self.wrong_master = None
                        self.unknown_master = None
                        self.not_master = None
                        self.not_slave = None
                        self.not_granted = None
                        self.too_slow = None
                        self.invalid_packet = None
                        self.wrong_sequence_id = None
                        self.no_offload_session = None
                        self.not_supported = None
                        self.min_clock_class = None
                        self.bad_clock_class = None
                        self.reserved_clock_id = None
                        self.steps_removed = None
                        self.g8265_1_incompatible = None
                        self.g8275_1_incompatible = None
                        self.g8275_2_incompatible = None
                        self.incorrect_address = None
                        self._segment_path = lambda: "drop-reasons"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.DropReasons, ['not_ready', 'wrong_domain', 'too_short', 'looped_same_port', 'looped_higher_port', 'looped_lower_port', 'no_timestamp', 'zero_timestamp', 'invalid_tl_vs', 'not_for_us', 'not_listening', 'wrong_master', 'unknown_master', 'not_master', 'not_slave', 'not_granted', 'too_slow', 'invalid_packet', 'wrong_sequence_id', 'no_offload_session', 'not_supported', 'min_clock_class', 'bad_clock_class', 'reserved_clock_id', 'steps_removed', 'g8265_1_incompatible', 'g8275_1_incompatible', 'g8275_2_incompatible', 'incorrect_address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Nodes.Node.PacketCounters.DropReasons']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Nodes.Node.PacketCounters']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.Nodes']['meta_info']


    class Summary(_Entity_):
        """
        Summary operational data
        
        .. attribute:: port_state_init_count
        
        	Number of interfaces in 'Init' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_listening_count
        
        	Number of interfaces in 'Listening' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_passive_count
        
        	Number of interfaces in 'Passive' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_pre_master_count
        
        	Number of interfaces in 'Pre\-Master' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_master_count
        
        	Number of interfaces in 'Master' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_slave_count
        
        	Number of interfaces in 'Slave' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_uncalibrated_count
        
        	Number of interfaces in 'Uncalibrated port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: port_state_faulty_count
        
        	Number of interfaces in 'Faulty' port state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_interfaces
        
        	Total number of interfaces
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_interfaces_valid_port_num
        
        	Total number of interfaces with a valid port number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('port_state_init_count', (YLeaf(YType.uint32, 'port-state-init-count'), ['int'])),
                ('port_state_listening_count', (YLeaf(YType.uint32, 'port-state-listening-count'), ['int'])),
                ('port_state_passive_count', (YLeaf(YType.uint32, 'port-state-passive-count'), ['int'])),
                ('port_state_pre_master_count', (YLeaf(YType.uint32, 'port-state-pre-master-count'), ['int'])),
                ('port_state_master_count', (YLeaf(YType.uint32, 'port-state-master-count'), ['int'])),
                ('port_state_slave_count', (YLeaf(YType.uint32, 'port-state-slave-count'), ['int'])),
                ('port_state_uncalibrated_count', (YLeaf(YType.uint32, 'port-state-uncalibrated-count'), ['int'])),
                ('port_state_faulty_count', (YLeaf(YType.uint32, 'port-state-faulty-count'), ['int'])),
                ('total_interfaces', (YLeaf(YType.uint32, 'total-interfaces'), ['int'])),
                ('total_interfaces_valid_port_num', (YLeaf(YType.uint32, 'total-interfaces-valid-port-num'), ['int'])),
            ])
            self.port_state_init_count = None
            self.port_state_listening_count = None
            self.port_state_passive_count = None
            self.port_state_pre_master_count = None
            self.port_state_master_count = None
            self.port_state_slave_count = None
            self.port_state_uncalibrated_count = None
            self.port_state_faulty_count = None
            self.total_interfaces = None
            self.total_interfaces_valid_port_num = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Summary, ['port_state_init_count', 'port_state_listening_count', 'port_state_passive_count', 'port_state_pre_master_count', 'port_state_master_count', 'port_state_slave_count', 'port_state_uncalibrated_count', 'port_state_faulty_count', 'total_interfaces', 'total_interfaces_valid_port_num'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.Summary']['meta_info']


    class InterfaceConfigurationErrors(_Entity_):
        """
        Table for interface configuration error
        operational data
        
        .. attribute:: interface_configuration_error
        
        	Interface configuration error operational data
        	**type**\: list of  		 :py:class:`InterfaceConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.InterfaceConfigurationErrors, self).__init__()

            self.yang_name = "interface-configuration-errors"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-configuration-error", ("interface_configuration_error", Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError))])
            self._leafs = OrderedDict()

            self.interface_configuration_error = YList(self)
            self._segment_path = lambda: "interface-configuration-errors"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceConfigurationErrors, [], name, value)


        class InterfaceConfigurationError(_Entity_):
            """
            Interface configuration error operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: configuration_errors
            
            	Configuration Errors
            	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors>`
            
            	**config**\: False
            
            .. attribute:: configuration_profile_name
            
            	Configuration profile name, if a profile is selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: clock_profile
            
            	The clock profile
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            	**config**\: False
            
            .. attribute:: telecom_clock_type
            
            	The telecom clock type
            	**type**\:  :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
            
            	**config**\: False
            
            .. attribute:: restrict_port_state
            
            	Restriction on the port state
            	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            	**config**\: False
            
            .. attribute:: interop_profile
            
            	The clock profile to interoperate with, if interoperation is configured
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError, self).__init__()

                self.yang_name = "interface-configuration-error"
                self.yang_parent_name = "interface-configuration-errors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("configuration-errors", ("configuration_errors", Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('configuration_profile_name', (YLeaf(YType.str, 'configuration-profile-name'), ['str'])),
                    ('clock_profile', (YLeaf(YType.enumeration, 'clock-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                    ('telecom_clock_type', (YLeaf(YType.enumeration, 'telecom-clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagTelecomClock', '')])),
                    ('restrict_port_state', (YLeaf(YType.enumeration, 'restrict-port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagRestrictPortState', '')])),
                    ('interop_profile', (YLeaf(YType.enumeration, 'interop-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                ])
                self.interface_name = None
                self.configuration_profile_name = None
                self.clock_profile = None
                self.telecom_clock_type = None
                self.restrict_port_state = None
                self.interop_profile = None

                self.configuration_errors = Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors()
                self.configuration_errors.parent = self
                self._children_name_map["configuration_errors"] = "configuration-errors"
                self._segment_path = lambda: "interface-configuration-error" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-configuration-errors/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError, ['interface_name', 'configuration_profile_name', 'clock_profile', 'telecom_clock_type', 'restrict_port_state', 'interop_profile'], name, value)


            class ConfigurationErrors(_Entity_):
                """
                Configuration Errors
                
                .. attribute:: global_ptp
                
                	PTP enabled on interface but not globally
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ethernet_transport
                
                	Ethernet transport configured but not supported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: one_step
                
                	One step clock operation configured but not supported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: slave
                
                	Slave\-operation configured but not supported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv6
                
                	IPv6 transport configured but not supported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: multicast
                
                	Multicast configured but not supported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_not_global
                
                	Profile is referenced but not globally configured
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: local_priority
                
                	Local priority configuration is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_ethernet
                
                	Ethernet transport is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_ipv4
                
                	IPv6 transport is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_ipv6
                
                	IPv6 transport is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_unicast
                
                	Unicast is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_multicast
                
                	Multicast is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_mixed
                
                	Mixed\-mode multicast is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_master_unicast
                
                	Unicast master is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_master_multicast
                
                	Multicast master is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_master_mixed
                
                	Mixed\-mode multicast master is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: target_address_ipv4
                
                	Ethernet multicast target\-address is configured, but transport is IPv4
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: target_address_ipv6
                
                	Ethernet multicast target\-address is configured, but transport is IPv6
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv4ttl
                
                	IPv4 TTL value configured but transport is not IPv4
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv6_hop_limit
                
                	IPv6 hop limit value configured but transport is not IPv6
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_port_state
                
                	Port state restriction is not compatible with telecom clock type
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_announce_interval
                
                	Announce interval is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_sync_interval
                
                	Sync interval is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_delay_req_interval
                
                	Delay request interval is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_sync_timeout
                
                	Sync timeout configuration is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: profile_delay_resp_timeout
                
                	Delay response timeout configuration is not compatible with profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_grant_reduction
                
                	Reducing invalid unicast grants is not compatible with configured profile
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_domain
                
                	Domain is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_clock_class_default
                
                	Ingress conversion clock class default is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_priority1
                
                	Ingress conversion priority1 is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_clock_accuracy
                
                	Ingress conversion clock\-accuracy is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_oslv
                
                	Ingress conversion OSLV not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_clock_class_default
                
                	Egress conversion clock class default is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_priority1
                
                	Egress conversion priority1 is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_priority2
                
                	Egress conversion priority2 is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_clock_accuracy
                
                	Egress conversion clock\-accuracy is not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_oslv
                
                	Egress conversion OSLV not compatible with configured profile interop
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_master_config
                
                	Master configuration is not compatible with configured clock\-type
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_slave_config
                
                	Slave configuration is not compatible with configured clock\-type
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_clock_class_map_from_val
                
                	List of ingress conversion clock class mapping 'from values' that are not compatible with the configure profile interop
                	**type**\: list of int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: invalid_interop_ingress_clock_class_map_to_val
                
                	List of ingress conversion clock class mapping 'to values' that are not compatible with the configure profile interop
                	**type**\: list of int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_clock_class_map_from_val
                
                	List of egress conversion clock class mapping 'from values' that are not compatible with the configure profile interop
                	**type**\: list of int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: invalid_interop_egress_clock_class_map_to_val
                
                	List of egress conversion clock class mapping 'to values' that are not compatible with the configure profile interop
                	**type**\: list of int
                
                	**range:** 0..255
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors, self).__init__()

                    self.yang_name = "configuration-errors"
                    self.yang_parent_name = "interface-configuration-error"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('global_ptp', (YLeaf(YType.boolean, 'global-ptp'), ['bool'])),
                        ('ethernet_transport', (YLeaf(YType.boolean, 'ethernet-transport'), ['bool'])),
                        ('one_step', (YLeaf(YType.boolean, 'one-step'), ['bool'])),
                        ('slave', (YLeaf(YType.boolean, 'slave'), ['bool'])),
                        ('ipv6', (YLeaf(YType.boolean, 'ipv6'), ['bool'])),
                        ('multicast', (YLeaf(YType.boolean, 'multicast'), ['bool'])),
                        ('profile_not_global', (YLeaf(YType.boolean, 'profile-not-global'), ['bool'])),
                        ('local_priority', (YLeaf(YType.boolean, 'local-priority'), ['bool'])),
                        ('profile_ethernet', (YLeaf(YType.boolean, 'profile-ethernet'), ['bool'])),
                        ('profile_ipv4', (YLeaf(YType.boolean, 'profile-ipv4'), ['bool'])),
                        ('profile_ipv6', (YLeaf(YType.boolean, 'profile-ipv6'), ['bool'])),
                        ('profile_unicast', (YLeaf(YType.boolean, 'profile-unicast'), ['bool'])),
                        ('profile_multicast', (YLeaf(YType.boolean, 'profile-multicast'), ['bool'])),
                        ('profile_mixed', (YLeaf(YType.boolean, 'profile-mixed'), ['bool'])),
                        ('profile_master_unicast', (YLeaf(YType.boolean, 'profile-master-unicast'), ['bool'])),
                        ('profile_master_multicast', (YLeaf(YType.boolean, 'profile-master-multicast'), ['bool'])),
                        ('profile_master_mixed', (YLeaf(YType.boolean, 'profile-master-mixed'), ['bool'])),
                        ('target_address_ipv4', (YLeaf(YType.boolean, 'target-address-ipv4'), ['bool'])),
                        ('target_address_ipv6', (YLeaf(YType.boolean, 'target-address-ipv6'), ['bool'])),
                        ('ipv4ttl', (YLeaf(YType.boolean, 'ipv4ttl'), ['bool'])),
                        ('ipv6_hop_limit', (YLeaf(YType.boolean, 'ipv6-hop-limit'), ['bool'])),
                        ('profile_port_state', (YLeaf(YType.boolean, 'profile-port-state'), ['bool'])),
                        ('profile_announce_interval', (YLeaf(YType.boolean, 'profile-announce-interval'), ['bool'])),
                        ('profile_sync_interval', (YLeaf(YType.boolean, 'profile-sync-interval'), ['bool'])),
                        ('profile_delay_req_interval', (YLeaf(YType.boolean, 'profile-delay-req-interval'), ['bool'])),
                        ('profile_sync_timeout', (YLeaf(YType.boolean, 'profile-sync-timeout'), ['bool'])),
                        ('profile_delay_resp_timeout', (YLeaf(YType.boolean, 'profile-delay-resp-timeout'), ['bool'])),
                        ('invalid_grant_reduction', (YLeaf(YType.boolean, 'invalid-grant-reduction'), ['bool'])),
                        ('invalid_interop_domain', (YLeaf(YType.boolean, 'invalid-interop-domain'), ['bool'])),
                        ('invalid_interop_ingress_clock_class_default', (YLeaf(YType.boolean, 'invalid-interop-ingress-clock-class-default'), ['bool'])),
                        ('invalid_interop_ingress_priority1', (YLeaf(YType.boolean, 'invalid-interop-ingress-priority1'), ['bool'])),
                        ('invalid_interop_ingress_clock_accuracy', (YLeaf(YType.boolean, 'invalid-interop-ingress-clock-accuracy'), ['bool'])),
                        ('invalid_interop_ingress_oslv', (YLeaf(YType.boolean, 'invalid-interop-ingress-oslv'), ['bool'])),
                        ('invalid_interop_egress_clock_class_default', (YLeaf(YType.boolean, 'invalid-interop-egress-clock-class-default'), ['bool'])),
                        ('invalid_interop_egress_priority1', (YLeaf(YType.boolean, 'invalid-interop-egress-priority1'), ['bool'])),
                        ('invalid_interop_egress_priority2', (YLeaf(YType.boolean, 'invalid-interop-egress-priority2'), ['bool'])),
                        ('invalid_interop_egress_clock_accuracy', (YLeaf(YType.boolean, 'invalid-interop-egress-clock-accuracy'), ['bool'])),
                        ('invalid_interop_egress_oslv', (YLeaf(YType.boolean, 'invalid-interop-egress-oslv'), ['bool'])),
                        ('invalid_master_config', (YLeaf(YType.boolean, 'invalid-master-config'), ['bool'])),
                        ('invalid_slave_config', (YLeaf(YType.boolean, 'invalid-slave-config'), ['bool'])),
                        ('invalid_interop_ingress_clock_class_map_from_val', (YLeafList(YType.uint8, 'invalid-interop-ingress-clock-class-map-from-val'), ['int'])),
                        ('invalid_interop_ingress_clock_class_map_to_val', (YLeafList(YType.uint8, 'invalid-interop-ingress-clock-class-map-to-val'), ['int'])),
                        ('invalid_interop_egress_clock_class_map_from_val', (YLeafList(YType.uint8, 'invalid-interop-egress-clock-class-map-from-val'), ['int'])),
                        ('invalid_interop_egress_clock_class_map_to_val', (YLeafList(YType.uint8, 'invalid-interop-egress-clock-class-map-to-val'), ['int'])),
                    ])
                    self.global_ptp = None
                    self.ethernet_transport = None
                    self.one_step = None
                    self.slave = None
                    self.ipv6 = None
                    self.multicast = None
                    self.profile_not_global = None
                    self.local_priority = None
                    self.profile_ethernet = None
                    self.profile_ipv4 = None
                    self.profile_ipv6 = None
                    self.profile_unicast = None
                    self.profile_multicast = None
                    self.profile_mixed = None
                    self.profile_master_unicast = None
                    self.profile_master_multicast = None
                    self.profile_master_mixed = None
                    self.target_address_ipv4 = None
                    self.target_address_ipv6 = None
                    self.ipv4ttl = None
                    self.ipv6_hop_limit = None
                    self.profile_port_state = None
                    self.profile_announce_interval = None
                    self.profile_sync_interval = None
                    self.profile_delay_req_interval = None
                    self.profile_sync_timeout = None
                    self.profile_delay_resp_timeout = None
                    self.invalid_grant_reduction = None
                    self.invalid_interop_domain = None
                    self.invalid_interop_ingress_clock_class_default = None
                    self.invalid_interop_ingress_priority1 = None
                    self.invalid_interop_ingress_clock_accuracy = None
                    self.invalid_interop_ingress_oslv = None
                    self.invalid_interop_egress_clock_class_default = None
                    self.invalid_interop_egress_priority1 = None
                    self.invalid_interop_egress_priority2 = None
                    self.invalid_interop_egress_clock_accuracy = None
                    self.invalid_interop_egress_oslv = None
                    self.invalid_master_config = None
                    self.invalid_slave_config = None
                    self.invalid_interop_ingress_clock_class_map_from_val = []
                    self.invalid_interop_ingress_clock_class_map_to_val = []
                    self.invalid_interop_egress_clock_class_map_from_val = []
                    self.invalid_interop_egress_clock_class_map_to_val = []
                    self._segment_path = lambda: "configuration-errors"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors, ['global_ptp', 'ethernet_transport', 'one_step', 'slave', 'ipv6', 'multicast', 'profile_not_global', 'local_priority', 'profile_ethernet', 'profile_ipv4', 'profile_ipv6', 'profile_unicast', 'profile_multicast', 'profile_mixed', 'profile_master_unicast', 'profile_master_multicast', 'profile_master_mixed', 'target_address_ipv4', 'target_address_ipv6', 'ipv4ttl', 'ipv6_hop_limit', 'profile_port_state', 'profile_announce_interval', 'profile_sync_interval', 'profile_delay_req_interval', 'profile_sync_timeout', 'profile_delay_resp_timeout', 'invalid_grant_reduction', 'invalid_interop_domain', 'invalid_interop_ingress_clock_class_default', 'invalid_interop_ingress_priority1', 'invalid_interop_ingress_clock_accuracy', 'invalid_interop_ingress_oslv', 'invalid_interop_egress_clock_class_default', 'invalid_interop_egress_priority1', 'invalid_interop_egress_priority2', 'invalid_interop_egress_clock_accuracy', 'invalid_interop_egress_oslv', 'invalid_master_config', 'invalid_slave_config', 'invalid_interop_ingress_clock_class_map_from_val', 'invalid_interop_ingress_clock_class_map_to_val', 'invalid_interop_egress_clock_class_map_from_val', 'invalid_interop_egress_clock_class_map_to_val'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.InterfaceConfigurationErrors']['meta_info']


    class InterfaceForeignMasters(_Entity_):
        """
        Table for interface foreign master clock
        operational data
        
        .. attribute:: interface_foreign_master
        
        	Interface foreign master clock operational data
        	**type**\: list of  		 :py:class:`InterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.InterfaceForeignMasters, self).__init__()

            self.yang_name = "interface-foreign-masters"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-foreign-master", ("interface_foreign_master", Ptp.InterfaceForeignMasters.InterfaceForeignMaster))])
            self._leafs = OrderedDict()

            self.interface_foreign_master = YList(self)
            self._segment_path = lambda: "interface-foreign-masters"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceForeignMasters, [], name, value)


        class InterfaceForeignMaster(_Entity_):
            """
            Interface foreign master clock operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: foreign_clock
            
            	Foreign clocks received on this interface
            	**type**\: list of  		 :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster, self).__init__()

                self.yang_name = "interface-foreign-master"
                self.yang_parent_name = "interface-foreign-masters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("foreign-clock", ("foreign_clock", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                ])
                self.interface_name = None
                self.port_number = None

                self.foreign_clock = YList(self)
                self._segment_path = lambda: "interface-foreign-master" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-foreign-masters/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster, ['interface_name', 'port_number'], name, value)


            class ForeignClock(_Entity_):
                """
                Foreign clocks received on this interface
                
                .. attribute:: foreign_clock
                
                	Foreign clock information
                	**type**\:  :py:class:`ForeignClock_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_>`
                
                	**config**\: False
                
                .. attribute:: address
                
                	The address of the clock
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address>`
                
                	**config**\: False
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                
                	**config**\: False
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant>`
                
                	**config**\: False
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                
                	**config**\: False
                
                .. attribute:: is_qualified
                
                	The clock is qualified for best master clock selection
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_grandmaster
                
                	This clock is the currently selected grand master clock
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: communication_model
                
                	The communication model configured on this clock
                	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                	**config**\: False
                
                .. attribute:: is_known
                
                	This clock is known by this router
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: time_known_for
                
                	How long the clock has been known by this router for, in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: second
                
                .. attribute:: foreign_domain
                
                	The PTP domain that the foreign clock is in
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: configured_priority
                
                	Priority configured for the clock, if any
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: configured_clock_class
                
                	Clock class configured for the clock, if any
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: delay_asymmetry
                
                	Delay asymmetry configured for the clock, if any
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**config**\: False
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_dnu
                
                	The clock has clock class corresponding to QL\-DNU
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, self).__init__()

                    self.yang_name = "foreign-clock"
                    self.yang_parent_name = "interface-foreign-master"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("foreign-clock", ("foreign_clock", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_)), ("address", ("address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address)), ("announce-grant", ("announce_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant)), ("sync-grant", ("sync_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant)), ("delay-response-grant", ("delay_response_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant))])
                    self._leafs = OrderedDict([
                        ('is_qualified', (YLeaf(YType.boolean, 'is-qualified'), ['bool'])),
                        ('is_grandmaster', (YLeaf(YType.boolean, 'is-grandmaster'), ['bool'])),
                        ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                        ('is_known', (YLeaf(YType.boolean, 'is-known'), ['bool'])),
                        ('time_known_for', (YLeaf(YType.uint32, 'time-known-for'), ['int'])),
                        ('foreign_domain', (YLeaf(YType.uint8, 'foreign-domain'), ['int'])),
                        ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                        ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                        ('delay_asymmetry', (YLeaf(YType.int32, 'delay-asymmetry'), ['int'])),
                        ('ptsf_loss_announce', (YLeaf(YType.boolean, 'ptsf-loss-announce'), ['bool'])),
                        ('ptsf_loss_sync', (YLeaf(YType.boolean, 'ptsf-loss-sync'), ['bool'])),
                        ('is_dnu', (YLeaf(YType.boolean, 'is-dnu'), ['bool'])),
                    ])
                    self.is_qualified = None
                    self.is_grandmaster = None
                    self.communication_model = None
                    self.is_known = None
                    self.time_known_for = None
                    self.foreign_domain = None
                    self.configured_priority = None
                    self.configured_clock_class = None
                    self.delay_asymmetry = None
                    self.ptsf_loss_announce = None
                    self.ptsf_loss_sync = None
                    self.is_dnu = None

                    self.foreign_clock = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_()
                    self.foreign_clock.parent = self
                    self._children_name_map["foreign_clock"] = "foreign-clock"

                    self.address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"

                    self.announce_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"

                    self.sync_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"

                    self.delay_response_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._segment_path = lambda: "foreign-clock"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, ['is_qualified', 'is_grandmaster', 'communication_model', 'is_known', 'time_known_for', 'foreign_domain', 'configured_priority', 'configured_clock_class', 'delay_asymmetry', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_dnu'], name, value)


                class ForeignClock_(_Entity_):
                    """
                    Foreign clock information
                    
                    .. attribute:: utc_offset
                    
                    	UTC offset
                    	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset>`
                    
                    	**config**\: False
                    
                    .. attribute:: receiver
                    
                    	Receiver
                    	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver>`
                    
                    	**config**\: False
                    
                    .. attribute:: sender
                    
                    	Sender
                    	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender>`
                    
                    	**config**\: False
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: priority1
                    
                    	Priority 1
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: priority2
                    
                    	Priority 2
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: class_
                    
                    	Class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: accuracy
                    
                    	Accuracy
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: offset_log_variance
                    
                    	Offset log variance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: steps_removed
                    
                    	Steps removed
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: time_source
                    
                    	Time source
                    	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                    
                    	**config**\: False
                    
                    .. attribute:: frequency_traceable
                    
                    	The clock is frequency traceable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: time_traceable
                    
                    	The clock is time traceable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: timescale
                    
                    	Timescale
                    	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                    
                    	**config**\: False
                    
                    .. attribute:: leap_seconds
                    
                    	Leap Seconds
                    	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: local
                    
                    	The clock is the local clock
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: configured_clock_class
                    
                    	The configured clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: configured_priority
                    
                    	The configured priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_, self).__init__()

                        self.yang_name = "foreign-clock"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("utc-offset", ("utc_offset", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset)), ("receiver", ("receiver", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver)), ("sender", ("sender", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender))])
                        self._leafs = OrderedDict([
                            ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                            ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                            ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                            ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                            ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                            ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                            ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                            ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                            ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                            ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                            ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
                            ('leap_seconds', (YLeaf(YType.enumeration, 'leap-seconds'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockLeapSeconds', '')])),
                            ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                            ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                            ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                        ])
                        self.clock_id = None
                        self.priority1 = None
                        self.priority2 = None
                        self.class_ = None
                        self.accuracy = None
                        self.offset_log_variance = None
                        self.steps_removed = None
                        self.time_source = None
                        self.frequency_traceable = None
                        self.time_traceable = None
                        self.timescale = None
                        self.leap_seconds = None
                        self.local = None
                        self.configured_clock_class = None
                        self.configured_priority = None

                        self.utc_offset = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset()
                        self.utc_offset.parent = self
                        self._children_name_map["utc_offset"] = "utc-offset"

                        self.receiver = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver()
                        self.receiver.parent = self
                        self._children_name_map["receiver"] = "receiver"

                        self.sender = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender()
                        self.sender.parent = self
                        self._children_name_map["sender"] = "sender"
                        self._segment_path = lambda: "foreign-clock"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


                    class UtcOffset(_Entity_):
                        """
                        UTC offset
                        
                        .. attribute:: current_offset
                        
                        	Current offset
                        	**type**\: int
                        
                        	**range:** \-32768..32767
                        
                        	**config**\: False
                        
                        .. attribute:: offset_valid
                        
                        	The current offset is valid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset, self).__init__()

                            self.yang_name = "utc-offset"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('current_offset', (YLeaf(YType.int16, 'current-offset'), ['int'])),
                                ('offset_valid', (YLeaf(YType.boolean, 'offset-valid'), ['bool'])),
                            ])
                            self.current_offset = None
                            self.offset_valid = None
                            self._segment_path = lambda: "utc-offset"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset, ['current_offset', 'offset_valid'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.UtcOffset']['meta_info']


                    class Receiver(_Entity_):
                        """
                        Receiver
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver, self).__init__()

                            self.yang_name = "receiver"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                                ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                            ])
                            self.clock_id = None
                            self.port_number = None
                            self._segment_path = lambda: "receiver"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver, ['clock_id', 'port_number'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Receiver']['meta_info']


                    class Sender(_Entity_):
                        """
                        Sender
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender, self).__init__()

                            self.yang_name = "sender"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                                ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                            ])
                            self.clock_id = None
                            self.port_number = None
                            self._segment_path = lambda: "sender"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender, ['clock_id', 'port_number'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_.Sender']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock_']['meta_info']


                class Address(_Entity_):
                    """
                    The address of the clock
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address))])
                        self._leafs = OrderedDict([
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ])
                        self.encapsulation = None
                        self.address_unknown = None
                        self.ipv4_address = None

                        self.mac_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ipv6_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._segment_path = lambda: "address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(_Entity_):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress']['meta_info']


                    class Ipv6Address(_Entity_):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "ipv6-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address, ['ipv6_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address']['meta_info']


                class AnnounceGrant(_Entity_):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant, self).__init__()

                        self.yang_name = "announce-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "announce-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant']['meta_info']


                class SyncGrant(_Entity_):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant, self).__init__()

                        self.yang_name = "sync-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "sync-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant']['meta_info']


                class DelayResponseGrant(_Entity_):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant, self).__init__()

                        self.yang_name = "delay-response-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "delay-response-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.InterfaceForeignMasters.InterfaceForeignMaster']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.InterfaceForeignMasters']['meta_info']


    class InterfaceInterops(_Entity_):
        """
        Table for interface interop operational data
        
        .. attribute:: interface_interop
        
        	Interface interop operational data
        	**type**\: list of  		 :py:class:`InterfaceInterop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.InterfaceInterops, self).__init__()

            self.yang_name = "interface-interops"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-interop", ("interface_interop", Ptp.InterfaceInterops.InterfaceInterop))])
            self._leafs = OrderedDict()

            self.interface_interop = YList(self)
            self._segment_path = lambda: "interface-interops"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceInterops, [], name, value)


        class InterfaceInterop(_Entity_):
            """
            Interface interop operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: egress_interop
            
            	Egress interop information
            	**type**\:  :py:class:`EgressInterop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.EgressInterop>`
            
            	**config**\: False
            
            .. attribute:: local_domain
            
            	The PTP domain configured for this interface
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: interop_domain
            
            	The PTP domain that is being interoperated with
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: local_profile
            
            	The PTP Profile configured for this interface
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            	**config**\: False
            
            .. attribute:: interop_profile
            
            	The PTP profile that is being interoperated with
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            	**config**\: False
            
            .. attribute:: ingress_interop
            
            	Per\-peer ingress interop information
            	**type**\: list of  		 :py:class:`IngressInterop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.IngressInterop>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.InterfaceInterops.InterfaceInterop, self).__init__()

                self.yang_name = "interface-interop"
                self.yang_parent_name = "interface-interops"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("egress-interop", ("egress_interop", Ptp.InterfaceInterops.InterfaceInterop.EgressInterop)), ("ingress-interop", ("ingress_interop", Ptp.InterfaceInterops.InterfaceInterop.IngressInterop))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('local_domain', (YLeaf(YType.uint8, 'local-domain'), ['int'])),
                    ('interop_domain', (YLeaf(YType.uint8, 'interop-domain'), ['int'])),
                    ('local_profile', (YLeaf(YType.enumeration, 'local-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                    ('interop_profile', (YLeaf(YType.enumeration, 'interop-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                ])
                self.interface_name = None
                self.local_domain = None
                self.interop_domain = None
                self.local_profile = None
                self.interop_profile = None

                self.egress_interop = Ptp.InterfaceInterops.InterfaceInterop.EgressInterop()
                self.egress_interop.parent = self
                self._children_name_map["egress_interop"] = "egress-interop"

                self.ingress_interop = YList(self)
                self._segment_path = lambda: "interface-interop" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-interops/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop, ['interface_name', 'local_domain', 'interop_domain', 'local_profile', 'interop_profile'], name, value)


            class EgressInterop(_Entity_):
                """
                Egress interop information
                
                .. attribute:: from_priority1
                
                	From Priority 1
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: to_priority1
                
                	To Priority 1
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: from_priority2
                
                	From Priority 2
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: to_priority2
                
                	To Priority 2
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: from_accuracy
                
                	From Accuracy
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: to_accuracy
                
                	To Accuracy
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: from_clock_class
                
                	From Clock Class
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: to_clock_class
                
                	To Clock Class
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: from_offset_log_variance
                
                	From Offset log variance
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: to_offset_log_variance
                
                	To Offset log variance
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfaceInterops.InterfaceInterop.EgressInterop, self).__init__()

                    self.yang_name = "egress-interop"
                    self.yang_parent_name = "interface-interop"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('from_priority1', (YLeaf(YType.uint8, 'from-priority1'), ['int'])),
                        ('to_priority1', (YLeaf(YType.uint8, 'to-priority1'), ['int'])),
                        ('from_priority2', (YLeaf(YType.uint8, 'from-priority2'), ['int'])),
                        ('to_priority2', (YLeaf(YType.uint8, 'to-priority2'), ['int'])),
                        ('from_accuracy', (YLeaf(YType.uint8, 'from-accuracy'), ['int'])),
                        ('to_accuracy', (YLeaf(YType.uint8, 'to-accuracy'), ['int'])),
                        ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                        ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                        ('from_offset_log_variance', (YLeaf(YType.uint16, 'from-offset-log-variance'), ['int'])),
                        ('to_offset_log_variance', (YLeaf(YType.uint16, 'to-offset-log-variance'), ['int'])),
                    ])
                    self.from_priority1 = None
                    self.to_priority1 = None
                    self.from_priority2 = None
                    self.to_priority2 = None
                    self.from_accuracy = None
                    self.to_accuracy = None
                    self.from_clock_class = None
                    self.to_clock_class = None
                    self.from_offset_log_variance = None
                    self.to_offset_log_variance = None
                    self._segment_path = lambda: "egress-interop"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.EgressInterop, ['from_priority1', 'to_priority1', 'from_priority2', 'to_priority2', 'from_accuracy', 'to_accuracy', 'from_clock_class', 'to_clock_class', 'from_offset_log_variance', 'to_offset_log_variance'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.EgressInterop']['meta_info']


            class IngressInterop(_Entity_):
                """
                Per\-peer ingress interop information
                
                .. attribute:: address
                
                	Peer address
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address>`
                
                	**config**\: False
                
                .. attribute:: interop
                
                	Interop information
                	**type**\:  :py:class:`Interop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop, self).__init__()

                    self.yang_name = "ingress-interop"
                    self.yang_parent_name = "interface-interop"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address", ("address", Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address)), ("interop", ("interop", Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop))])
                    self._leafs = OrderedDict()

                    self.address = Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"

                    self.interop = Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop()
                    self.interop.parent = self
                    self._children_name_map["interop"] = "interop"
                    self._segment_path = lambda: "ingress-interop"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop, [], name, value)


                class Address(_Entity_):
                    """
                    Peer address
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "ingress-interop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address))])
                        self._leafs = OrderedDict([
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ])
                        self.encapsulation = None
                        self.address_unknown = None
                        self.ipv4_address = None

                        self.mac_address = Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ipv6_address = Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._segment_path = lambda: "address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(_Entity_):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.MacAddress']['meta_info']


                    class Ipv6Address(_Entity_):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "ipv6-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address, ['ipv6_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address.Ipv6Address']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Address']['meta_info']


                class Interop(_Entity_):
                    """
                    Interop information
                    
                    .. attribute:: from_priority1
                    
                    	From Priority 1
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_priority1
                    
                    	To Priority 1
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: from_priority2
                    
                    	From Priority 2
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_priority2
                    
                    	To Priority 2
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: from_accuracy
                    
                    	From Accuracy
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_accuracy
                    
                    	To Accuracy
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: from_clock_class
                    
                    	From Clock Class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_clock_class
                    
                    	To Clock Class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: from_offset_log_variance
                    
                    	From Offset log variance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: to_offset_log_variance
                    
                    	To Offset log variance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop, self).__init__()

                        self.yang_name = "interop"
                        self.yang_parent_name = "ingress-interop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('from_priority1', (YLeaf(YType.uint8, 'from-priority1'), ['int'])),
                            ('to_priority1', (YLeaf(YType.uint8, 'to-priority1'), ['int'])),
                            ('from_priority2', (YLeaf(YType.uint8, 'from-priority2'), ['int'])),
                            ('to_priority2', (YLeaf(YType.uint8, 'to-priority2'), ['int'])),
                            ('from_accuracy', (YLeaf(YType.uint8, 'from-accuracy'), ['int'])),
                            ('to_accuracy', (YLeaf(YType.uint8, 'to-accuracy'), ['int'])),
                            ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                            ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                            ('from_offset_log_variance', (YLeaf(YType.uint16, 'from-offset-log-variance'), ['int'])),
                            ('to_offset_log_variance', (YLeaf(YType.uint16, 'to-offset-log-variance'), ['int'])),
                        ])
                        self.from_priority1 = None
                        self.to_priority1 = None
                        self.from_priority2 = None
                        self.to_priority2 = None
                        self.from_accuracy = None
                        self.to_accuracy = None
                        self.from_clock_class = None
                        self.to_clock_class = None
                        self.from_offset_log_variance = None
                        self.to_offset_log_variance = None
                        self._segment_path = lambda: "interop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop, ['from_priority1', 'to_priority1', 'from_priority2', 'to_priority2', 'from_accuracy', 'to_accuracy', 'from_clock_class', 'to_clock_class', 'from_offset_log_variance', 'to_offset_log_variance'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.IngressInterop.Interop']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop.IngressInterop']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.InterfaceInterops.InterfaceInterop']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.InterfaceInterops']['meta_info']


    class LocalClock(_Entity_):
        """
        Local clock operational data
        
        .. attribute:: clock_properties
        
        	Local clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties>`
        
        	**config**\: False
        
        .. attribute:: virtual_port
        
        	Virtual port
        	**type**\:  :py:class:`VirtualPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.VirtualPort>`
        
        	**config**\: False
        
        .. attribute:: domain
        
        	The PTP domain of the local clock
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: grandmaster
        
        	Whether the local clock is the grandmaster
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.LocalClock, self).__init__()

            self.yang_name = "local-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clock-properties", ("clock_properties", Ptp.LocalClock.ClockProperties)), ("virtual-port", ("virtual_port", Ptp.LocalClock.VirtualPort))])
            self._leafs = OrderedDict([
                ('domain', (YLeaf(YType.uint8, 'domain'), ['int'])),
                ('grandmaster', (YLeaf(YType.boolean, 'grandmaster'), ['bool'])),
            ])
            self.domain = None
            self.grandmaster = None

            self.clock_properties = Ptp.LocalClock.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"

            self.virtual_port = Ptp.LocalClock.VirtualPort()
            self.virtual_port.parent = self
            self._children_name_map["virtual_port"] = "virtual-port"
            self._segment_path = lambda: "local-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.LocalClock, ['domain', 'grandmaster'], name, value)


        class ClockProperties(_Entity_):
            """
            Local clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.UtcOffset>`
            
            	**config**\: False
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Receiver>`
            
            	**config**\: False
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Sender>`
            
            	**config**\: False
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            	**config**\: False
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            	**config**\: False
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.LocalClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "local-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("utc-offset", ("utc_offset", Ptp.LocalClock.ClockProperties.UtcOffset)), ("receiver", ("receiver", Ptp.LocalClock.ClockProperties.Receiver)), ("sender", ("sender", Ptp.LocalClock.ClockProperties.Sender))])
                self._leafs = OrderedDict([
                    ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                    ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                    ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                    ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                    ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                    ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                    ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                    ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
                    ('leap_seconds', (YLeaf(YType.enumeration, 'leap-seconds'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockLeapSeconds', '')])),
                    ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                    ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                    ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                ])
                self.clock_id = None
                self.priority1 = None
                self.priority2 = None
                self.class_ = None
                self.accuracy = None
                self.offset_log_variance = None
                self.steps_removed = None
                self.time_source = None
                self.frequency_traceable = None
                self.time_traceable = None
                self.timescale = None
                self.leap_seconds = None
                self.local = None
                self.configured_clock_class = None
                self.configured_priority = None

                self.utc_offset = Ptp.LocalClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"

                self.receiver = Ptp.LocalClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"

                self.sender = Ptp.LocalClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LocalClock.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(_Entity_):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.LocalClock.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('current_offset', (YLeaf(YType.int16, 'current-offset'), ['int'])),
                        ('offset_valid', (YLeaf(YType.boolean, 'offset-valid'), ['bool'])),
                    ])
                    self.current_offset = None
                    self.offset_valid = None
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.LocalClock.ClockProperties.UtcOffset']['meta_info']


            class Receiver(_Entity_):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.LocalClock.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.LocalClock.ClockProperties.Receiver']['meta_info']


            class Sender(_Entity_):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.LocalClock.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.LocalClock.ClockProperties.Sender']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.LocalClock.ClockProperties']['meta_info']


        class VirtualPort(_Entity_):
            """
            Virtual port
            
            .. attribute:: configured
            
            	Configured
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: connected
            
            	Connected
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: local_priority
            
            	The local priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.LocalClock.VirtualPort, self).__init__()

                self.yang_name = "virtual-port"
                self.yang_parent_name = "local-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                    ('connected', (YLeaf(YType.boolean, 'connected'), ['bool'])),
                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                    ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                    ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                    ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ('local_priority', (YLeaf(YType.uint8, 'local-priority'), ['int'])),
                ])
                self.configured = None
                self.connected = None
                self.priority1 = None
                self.priority2 = None
                self.class_ = None
                self.accuracy = None
                self.offset_log_variance = None
                self.local_priority = None
                self._segment_path = lambda: "virtual-port"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LocalClock.VirtualPort, ['configured', 'connected', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'local_priority'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.LocalClock.VirtualPort']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.LocalClock']['meta_info']


    class InterfacePacketCounters(_Entity_):
        """
        Table for interface packet counter operational
        data
        
        .. attribute:: interface_packet_counter
        
        	Interface packet counter operational data
        	**type**\: list of  		 :py:class:`InterfacePacketCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.InterfacePacketCounters, self).__init__()

            self.yang_name = "interface-packet-counters"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-packet-counter", ("interface_packet_counter", Ptp.InterfacePacketCounters.InterfacePacketCounter))])
            self._leafs = OrderedDict()

            self.interface_packet_counter = YList(self)
            self._segment_path = lambda: "interface-packet-counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfacePacketCounters, [], name, value)


        class InterfacePacketCounter(_Entity_):
            """
            Interface packet counter operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: counters
            
            	Packet counters
            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters>`
            
            	**config**\: False
            
            .. attribute:: peer_counter
            
            	Packet counters for each peer on this interface
            	**type**\: list of  		 :py:class:`PeerCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.InterfacePacketCounters.InterfacePacketCounter, self).__init__()

                self.yang_name = "interface-packet-counter"
                self.yang_parent_name = "interface-packet-counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("counters", ("counters", Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters)), ("peer-counter", ("peer_counter", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.counters = Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"

                self.peer_counter = YList(self)
                self._segment_path = lambda: "interface-packet-counter" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-packet-counters/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter, ['interface_name'], name, value)


            class Counters(_Entity_):
                """
                Packet counters
                
                .. attribute:: announce_sent
                
                	Number of announce packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: announce_received
                
                	Number of announce packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: announce_dropped
                
                	Number of announce packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sync_sent
                
                	Number of sync packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sync_received
                
                	Number of sync packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sync_dropped
                
                	Number of sync packetsdropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: follow_up_sent
                
                	Number of follow\-up packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: follow_up_received
                
                	Number of follow\-up packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: follow_up_dropped
                
                	Number of follow\-up packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_request_sent
                
                	Number of delay\-request packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_request_received
                
                	Number of delay\-request packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_request_dropped
                
                	Number of delay\-request packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_response_sent
                
                	Number of delay\-response packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_response_received
                
                	Number of delay\-response packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: delay_response_dropped
                
                	Number of delay\-response packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_request_sent
                
                	Number of peer\-delay\-request packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_request_received
                
                	Number of peer\-delay\-request packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_request_dropped
                
                	Number of peer\-delay\-request packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_sent
                
                	Number of peer\-delay\-response packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_received
                
                	Number of peer\-delay\-response packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_dropped
                
                	Number of peer\-delay\-response packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_follow_up_sent
                
                	Number of peer\-delay\-response follow\-up packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_follow_up_received
                
                	Number of peer\-delay\-response follow\-up packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peer_delay_response_follow_up_dropped
                
                	Number of peer\-delay\-response follow\-up packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: signaling_sent
                
                	Number of signaling packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: signaling_received
                
                	Number of signaling packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: signaling_dropped
                
                	Number of signaling packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: management_sent
                
                	Number of management messages sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: management_received
                
                	Number of management messages received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: management_dropped
                
                	Number of management messages dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: other_packets_sent
                
                	Number of other packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: other_packets_received
                
                	Number of other packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: other_packets_dropped
                
                	Number of other packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_packets_sent
                
                	Total number of packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_packets_received
                
                	Total number of packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_packets_dropped
                
                	Total number of packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "interface-packet-counter"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('announce_sent', (YLeaf(YType.uint32, 'announce-sent'), ['int'])),
                        ('announce_received', (YLeaf(YType.uint32, 'announce-received'), ['int'])),
                        ('announce_dropped', (YLeaf(YType.uint32, 'announce-dropped'), ['int'])),
                        ('sync_sent', (YLeaf(YType.uint32, 'sync-sent'), ['int'])),
                        ('sync_received', (YLeaf(YType.uint32, 'sync-received'), ['int'])),
                        ('sync_dropped', (YLeaf(YType.uint32, 'sync-dropped'), ['int'])),
                        ('follow_up_sent', (YLeaf(YType.uint32, 'follow-up-sent'), ['int'])),
                        ('follow_up_received', (YLeaf(YType.uint32, 'follow-up-received'), ['int'])),
                        ('follow_up_dropped', (YLeaf(YType.uint32, 'follow-up-dropped'), ['int'])),
                        ('delay_request_sent', (YLeaf(YType.uint32, 'delay-request-sent'), ['int'])),
                        ('delay_request_received', (YLeaf(YType.uint32, 'delay-request-received'), ['int'])),
                        ('delay_request_dropped', (YLeaf(YType.uint32, 'delay-request-dropped'), ['int'])),
                        ('delay_response_sent', (YLeaf(YType.uint32, 'delay-response-sent'), ['int'])),
                        ('delay_response_received', (YLeaf(YType.uint32, 'delay-response-received'), ['int'])),
                        ('delay_response_dropped', (YLeaf(YType.uint32, 'delay-response-dropped'), ['int'])),
                        ('peer_delay_request_sent', (YLeaf(YType.uint32, 'peer-delay-request-sent'), ['int'])),
                        ('peer_delay_request_received', (YLeaf(YType.uint32, 'peer-delay-request-received'), ['int'])),
                        ('peer_delay_request_dropped', (YLeaf(YType.uint32, 'peer-delay-request-dropped'), ['int'])),
                        ('peer_delay_response_sent', (YLeaf(YType.uint32, 'peer-delay-response-sent'), ['int'])),
                        ('peer_delay_response_received', (YLeaf(YType.uint32, 'peer-delay-response-received'), ['int'])),
                        ('peer_delay_response_dropped', (YLeaf(YType.uint32, 'peer-delay-response-dropped'), ['int'])),
                        ('peer_delay_response_follow_up_sent', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-sent'), ['int'])),
                        ('peer_delay_response_follow_up_received', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-received'), ['int'])),
                        ('peer_delay_response_follow_up_dropped', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-dropped'), ['int'])),
                        ('signaling_sent', (YLeaf(YType.uint32, 'signaling-sent'), ['int'])),
                        ('signaling_received', (YLeaf(YType.uint32, 'signaling-received'), ['int'])),
                        ('signaling_dropped', (YLeaf(YType.uint32, 'signaling-dropped'), ['int'])),
                        ('management_sent', (YLeaf(YType.uint32, 'management-sent'), ['int'])),
                        ('management_received', (YLeaf(YType.uint32, 'management-received'), ['int'])),
                        ('management_dropped', (YLeaf(YType.uint32, 'management-dropped'), ['int'])),
                        ('other_packets_sent', (YLeaf(YType.uint32, 'other-packets-sent'), ['int'])),
                        ('other_packets_received', (YLeaf(YType.uint32, 'other-packets-received'), ['int'])),
                        ('other_packets_dropped', (YLeaf(YType.uint32, 'other-packets-dropped'), ['int'])),
                        ('total_packets_sent', (YLeaf(YType.uint32, 'total-packets-sent'), ['int'])),
                        ('total_packets_received', (YLeaf(YType.uint32, 'total-packets-received'), ['int'])),
                        ('total_packets_dropped', (YLeaf(YType.uint32, 'total-packets-dropped'), ['int'])),
                    ])
                    self.announce_sent = None
                    self.announce_received = None
                    self.announce_dropped = None
                    self.sync_sent = None
                    self.sync_received = None
                    self.sync_dropped = None
                    self.follow_up_sent = None
                    self.follow_up_received = None
                    self.follow_up_dropped = None
                    self.delay_request_sent = None
                    self.delay_request_received = None
                    self.delay_request_dropped = None
                    self.delay_response_sent = None
                    self.delay_response_received = None
                    self.delay_response_dropped = None
                    self.peer_delay_request_sent = None
                    self.peer_delay_request_received = None
                    self.peer_delay_request_dropped = None
                    self.peer_delay_response_sent = None
                    self.peer_delay_response_received = None
                    self.peer_delay_response_dropped = None
                    self.peer_delay_response_follow_up_sent = None
                    self.peer_delay_response_follow_up_received = None
                    self.peer_delay_response_follow_up_dropped = None
                    self.signaling_sent = None
                    self.signaling_received = None
                    self.signaling_dropped = None
                    self.management_sent = None
                    self.management_received = None
                    self.management_dropped = None
                    self.other_packets_sent = None
                    self.other_packets_received = None
                    self.other_packets_dropped = None
                    self.total_packets_sent = None
                    self.total_packets_received = None
                    self.total_packets_dropped = None
                    self._segment_path = lambda: "counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters']['meta_info']


            class PeerCounter(_Entity_):
                """
                Packet counters for each peer on this interface
                
                .. attribute:: address
                
                	Peer address
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address>`
                
                	**config**\: False
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter, self).__init__()

                    self.yang_name = "peer-counter"
                    self.yang_parent_name = "interface-packet-counter"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address", ("address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address)), ("counters", ("counters", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters))])
                    self._leafs = OrderedDict()

                    self.address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"

                    self.counters = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"
                    self._segment_path = lambda: "peer-counter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter, [], name, value)


                class Address(_Entity_):
                    """
                    Peer address
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peer-counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address))])
                        self._leafs = OrderedDict([
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ])
                        self.encapsulation = None
                        self.address_unknown = None
                        self.ipv4_address = None

                        self.mac_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ipv6_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._segment_path = lambda: "address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(_Entity_):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress']['meta_info']


                    class Ipv6Address(_Entity_):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "ipv6-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address, ['ipv6_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address']['meta_info']


                class Counters(_Entity_):
                    """
                    Packet counters
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "peer-counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('announce_sent', (YLeaf(YType.uint32, 'announce-sent'), ['int'])),
                            ('announce_received', (YLeaf(YType.uint32, 'announce-received'), ['int'])),
                            ('announce_dropped', (YLeaf(YType.uint32, 'announce-dropped'), ['int'])),
                            ('sync_sent', (YLeaf(YType.uint32, 'sync-sent'), ['int'])),
                            ('sync_received', (YLeaf(YType.uint32, 'sync-received'), ['int'])),
                            ('sync_dropped', (YLeaf(YType.uint32, 'sync-dropped'), ['int'])),
                            ('follow_up_sent', (YLeaf(YType.uint32, 'follow-up-sent'), ['int'])),
                            ('follow_up_received', (YLeaf(YType.uint32, 'follow-up-received'), ['int'])),
                            ('follow_up_dropped', (YLeaf(YType.uint32, 'follow-up-dropped'), ['int'])),
                            ('delay_request_sent', (YLeaf(YType.uint32, 'delay-request-sent'), ['int'])),
                            ('delay_request_received', (YLeaf(YType.uint32, 'delay-request-received'), ['int'])),
                            ('delay_request_dropped', (YLeaf(YType.uint32, 'delay-request-dropped'), ['int'])),
                            ('delay_response_sent', (YLeaf(YType.uint32, 'delay-response-sent'), ['int'])),
                            ('delay_response_received', (YLeaf(YType.uint32, 'delay-response-received'), ['int'])),
                            ('delay_response_dropped', (YLeaf(YType.uint32, 'delay-response-dropped'), ['int'])),
                            ('peer_delay_request_sent', (YLeaf(YType.uint32, 'peer-delay-request-sent'), ['int'])),
                            ('peer_delay_request_received', (YLeaf(YType.uint32, 'peer-delay-request-received'), ['int'])),
                            ('peer_delay_request_dropped', (YLeaf(YType.uint32, 'peer-delay-request-dropped'), ['int'])),
                            ('peer_delay_response_sent', (YLeaf(YType.uint32, 'peer-delay-response-sent'), ['int'])),
                            ('peer_delay_response_received', (YLeaf(YType.uint32, 'peer-delay-response-received'), ['int'])),
                            ('peer_delay_response_dropped', (YLeaf(YType.uint32, 'peer-delay-response-dropped'), ['int'])),
                            ('peer_delay_response_follow_up_sent', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-sent'), ['int'])),
                            ('peer_delay_response_follow_up_received', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-received'), ['int'])),
                            ('peer_delay_response_follow_up_dropped', (YLeaf(YType.uint32, 'peer-delay-response-follow-up-dropped'), ['int'])),
                            ('signaling_sent', (YLeaf(YType.uint32, 'signaling-sent'), ['int'])),
                            ('signaling_received', (YLeaf(YType.uint32, 'signaling-received'), ['int'])),
                            ('signaling_dropped', (YLeaf(YType.uint32, 'signaling-dropped'), ['int'])),
                            ('management_sent', (YLeaf(YType.uint32, 'management-sent'), ['int'])),
                            ('management_received', (YLeaf(YType.uint32, 'management-received'), ['int'])),
                            ('management_dropped', (YLeaf(YType.uint32, 'management-dropped'), ['int'])),
                            ('other_packets_sent', (YLeaf(YType.uint32, 'other-packets-sent'), ['int'])),
                            ('other_packets_received', (YLeaf(YType.uint32, 'other-packets-received'), ['int'])),
                            ('other_packets_dropped', (YLeaf(YType.uint32, 'other-packets-dropped'), ['int'])),
                            ('total_packets_sent', (YLeaf(YType.uint32, 'total-packets-sent'), ['int'])),
                            ('total_packets_received', (YLeaf(YType.uint32, 'total-packets-received'), ['int'])),
                            ('total_packets_dropped', (YLeaf(YType.uint32, 'total-packets-dropped'), ['int'])),
                        ])
                        self.announce_sent = None
                        self.announce_received = None
                        self.announce_dropped = None
                        self.sync_sent = None
                        self.sync_received = None
                        self.sync_dropped = None
                        self.follow_up_sent = None
                        self.follow_up_received = None
                        self.follow_up_dropped = None
                        self.delay_request_sent = None
                        self.delay_request_received = None
                        self.delay_request_dropped = None
                        self.delay_response_sent = None
                        self.delay_response_received = None
                        self.delay_response_dropped = None
                        self.peer_delay_request_sent = None
                        self.peer_delay_request_received = None
                        self.peer_delay_request_dropped = None
                        self.peer_delay_response_sent = None
                        self.peer_delay_response_received = None
                        self.peer_delay_response_dropped = None
                        self.peer_delay_response_follow_up_sent = None
                        self.peer_delay_response_follow_up_received = None
                        self.peer_delay_response_follow_up_dropped = None
                        self.signaling_sent = None
                        self.signaling_received = None
                        self.signaling_dropped = None
                        self.management_sent = None
                        self.management_received = None
                        self.management_dropped = None
                        self.other_packets_sent = None
                        self.other_packets_received = None
                        self.other_packets_dropped = None
                        self.total_packets_sent = None
                        self.total_packets_received = None
                        self.total_packets_dropped = None
                        self._segment_path = lambda: "counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.InterfacePacketCounters.InterfacePacketCounter']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.InterfacePacketCounters']['meta_info']


    class AdvertisedClock(_Entity_):
        """
        Advertised clock operational data
        
        .. attribute:: clock_properties
        
        	Advertised Clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties>`
        
        	**config**\: False
        
        .. attribute:: domain
        
        	The PTP domain of that the advertised clock is in
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: time_source_configured
        
        	Whether the advertised time source is configured
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: received_time_source
        
        	The time source received from the parent clock
        	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
        
        	**config**\: False
        
        .. attribute:: timescale_configured
        
        	Whether the advertised timescale is configured
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: received_timescale
        
        	The timescale received from the parent clock
        	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.AdvertisedClock, self).__init__()

            self.yang_name = "advertised-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clock-properties", ("clock_properties", Ptp.AdvertisedClock.ClockProperties))])
            self._leafs = OrderedDict([
                ('domain', (YLeaf(YType.uint8, 'domain'), ['int'])),
                ('time_source_configured', (YLeaf(YType.boolean, 'time-source-configured'), ['bool'])),
                ('received_time_source', (YLeaf(YType.enumeration, 'received-time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                ('timescale_configured', (YLeaf(YType.boolean, 'timescale-configured'), ['bool'])),
                ('received_timescale', (YLeaf(YType.enumeration, 'received-timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
            ])
            self.domain = None
            self.time_source_configured = None
            self.received_time_source = None
            self.timescale_configured = None
            self.received_timescale = None

            self.clock_properties = Ptp.AdvertisedClock.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._segment_path = lambda: "advertised-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.AdvertisedClock, ['domain', 'time_source_configured', 'received_time_source', 'timescale_configured', 'received_timescale'], name, value)


        class ClockProperties(_Entity_):
            """
            Advertised Clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.UtcOffset>`
            
            	**config**\: False
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Receiver>`
            
            	**config**\: False
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Sender>`
            
            	**config**\: False
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            	**config**\: False
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            	**config**\: False
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.AdvertisedClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "advertised-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("utc-offset", ("utc_offset", Ptp.AdvertisedClock.ClockProperties.UtcOffset)), ("receiver", ("receiver", Ptp.AdvertisedClock.ClockProperties.Receiver)), ("sender", ("sender", Ptp.AdvertisedClock.ClockProperties.Sender))])
                self._leafs = OrderedDict([
                    ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                    ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                    ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                    ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                    ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                    ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                    ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                    ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
                    ('leap_seconds', (YLeaf(YType.enumeration, 'leap-seconds'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockLeapSeconds', '')])),
                    ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                    ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                    ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                ])
                self.clock_id = None
                self.priority1 = None
                self.priority2 = None
                self.class_ = None
                self.accuracy = None
                self.offset_log_variance = None
                self.steps_removed = None
                self.time_source = None
                self.frequency_traceable = None
                self.time_traceable = None
                self.timescale = None
                self.leap_seconds = None
                self.local = None
                self.configured_clock_class = None
                self.configured_priority = None

                self.utc_offset = Ptp.AdvertisedClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"

                self.receiver = Ptp.AdvertisedClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"

                self.sender = Ptp.AdvertisedClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.AdvertisedClock.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(_Entity_):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.AdvertisedClock.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('current_offset', (YLeaf(YType.int16, 'current-offset'), ['int'])),
                        ('offset_valid', (YLeaf(YType.boolean, 'offset-valid'), ['bool'])),
                    ])
                    self.current_offset = None
                    self.offset_valid = None
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.AdvertisedClock.ClockProperties.UtcOffset']['meta_info']


            class Receiver(_Entity_):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.AdvertisedClock.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.AdvertisedClock.ClockProperties.Receiver']['meta_info']


            class Sender(_Entity_):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.AdvertisedClock.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.AdvertisedClock.ClockProperties.Sender']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.AdvertisedClock.ClockProperties']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.AdvertisedClock']['meta_info']


    class Interfaces(_Entity_):
        """
        Table for interface operational data
        
        .. attribute:: interface
        
        	Interface operational data
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Ptp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            Interface operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: ipv6_address_array
            
            	List of Ipv6 addresses, if IPv6 encapsulation is being used. If a source address is configured, this is the only item in the list
            	**type**\:  :py:class:`Ipv6AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.Ipv6AddressArray>`
            
            	**config**\: False
            
            .. attribute:: ipv4_address_array
            
            	List of IPv4 addresses, if IPv4 encapsulation is being used. The first address is the primary address. If a source address is configured, this is the only item in the list
            	**type**\:  :py:class:`Ipv4AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.Ipv4AddressArray>`
            
            	**config**\: False
            
            .. attribute:: mac_address
            
            	MAC address, if Ethernet encapsulation is being used
            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MacAddress>`
            
            	**config**\: False
            
            .. attribute:: ingress_conversion
            
            	Details of any ingress conversion
            	**type**\:  :py:class:`IngressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.IngressConversion>`
            
            	**config**\: False
            
            .. attribute:: egress_conversion
            
            	Details of any egress conversion
            	**type**\:  :py:class:`EgressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.EgressConversion>`
            
            	**config**\: False
            
            .. attribute:: port_state
            
            	Port state
            	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
            
            	**config**\: False
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: line_state
            
            	Line state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.ImStateEnum>`
            
            	**config**\: False
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            	**config**\: False
            
            .. attribute:: ipv6_address
            
            	Ipv6 address, if IPv6 encapsulation is being used
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ipv4_address
            
            	IPv4 address, if IPv4 encapsulation is being used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: two_step
            
            	Two step delay\-request mechanism is being used
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: communication_model
            
            	Communication model configured on the interface
            	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
            
            	**config**\: False
            
            .. attribute:: log_sync_interval
            
            	Log of the interface's sync interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: log_announce_interval
            
            	Log of the interface's announce interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: announce_timeout
            
            	Announce timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: log_min_delay_request_interval
            
            	Log of the interface's Minimum delay\-request interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: configured_port_state
            
            	The configured port state
            	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            	**config**\: False
            
            .. attribute:: supports_unicast
            
            	The interface supports unicast
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_master
            
            	The interface supports operation in master mode
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_one_step
            
            	The interface supports one\-step operation
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_two_step
            
            	The interface supports two\-step operation
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_ethernet
            
            	The interface supports ethernet transport
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_multicast
            
            	The interface supports multicast
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_ipv4
            
            	The interface supports IPv4 transport
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_ipv6
            
            	The interface supports IPv6 transport
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_slave
            
            	The interface supports operation in slave mode
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: supports_source_ip
            
            	The interface supports source ip configuration
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: max_sync_rate
            
            	The maximum rate of sync packets on the interface
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: event_cos
            
            	The class of service used on the interface for event messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: general_cos
            
            	The class of service used on the interface for general messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: event_dscp
            
            	The DSCP class used on the interface for event messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: general_dscp
            
            	The DSCP class used on the interface for general messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: unicast_peers
            
            	The number of unicast peers known by the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: local_priority
            
            	Local priority, for the G.8275.1 PTP profile
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: signal_fail
            
            	Signal fail status of the interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: profile_interop
            
            	Indicate whether profile interop is in use
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: interop_domain
            
            	The PTP domain that is being interoperated with
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: interop_profile
            
            	Profile that is being interoperated with
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            	**config**\: False
            
            .. attribute:: master_table
            
            	The interface's master table
            	**type**\: list of  		 :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("ipv6-address-array", ("ipv6_address_array", Ptp.Interfaces.Interface.Ipv6AddressArray)), ("ipv4-address-array", ("ipv4_address_array", Ptp.Interfaces.Interface.Ipv4AddressArray)), ("mac-address", ("mac_address", Ptp.Interfaces.Interface.MacAddress)), ("ingress-conversion", ("ingress_conversion", Ptp.Interfaces.Interface.IngressConversion)), ("egress-conversion", ("egress_conversion", Ptp.Interfaces.Interface.EgressConversion)), ("master-table", ("master_table", Ptp.Interfaces.Interface.MasterTable))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('port_state', (YLeaf(YType.enumeration, 'port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagPortState', '')])),
                    ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'ImStateEnum', '')])),
                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                    ('two_step', (YLeaf(YType.boolean, 'two-step'), ['bool'])),
                    ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                    ('log_sync_interval', (YLeaf(YType.int32, 'log-sync-interval'), ['int'])),
                    ('log_announce_interval', (YLeaf(YType.int32, 'log-announce-interval'), ['int'])),
                    ('announce_timeout', (YLeaf(YType.uint32, 'announce-timeout'), ['int'])),
                    ('log_min_delay_request_interval', (YLeaf(YType.int32, 'log-min-delay-request-interval'), ['int'])),
                    ('configured_port_state', (YLeaf(YType.enumeration, 'configured-port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagRestrictPortState', '')])),
                    ('supports_unicast', (YLeaf(YType.boolean, 'supports-unicast'), ['bool'])),
                    ('supports_master', (YLeaf(YType.boolean, 'supports-master'), ['bool'])),
                    ('supports_one_step', (YLeaf(YType.boolean, 'supports-one-step'), ['bool'])),
                    ('supports_two_step', (YLeaf(YType.boolean, 'supports-two-step'), ['bool'])),
                    ('supports_ethernet', (YLeaf(YType.boolean, 'supports-ethernet'), ['bool'])),
                    ('supports_multicast', (YLeaf(YType.boolean, 'supports-multicast'), ['bool'])),
                    ('supports_ipv4', (YLeaf(YType.boolean, 'supports-ipv4'), ['bool'])),
                    ('supports_ipv6', (YLeaf(YType.boolean, 'supports-ipv6'), ['bool'])),
                    ('supports_slave', (YLeaf(YType.boolean, 'supports-slave'), ['bool'])),
                    ('supports_source_ip', (YLeaf(YType.boolean, 'supports-source-ip'), ['bool'])),
                    ('max_sync_rate', (YLeaf(YType.uint8, 'max-sync-rate'), ['int'])),
                    ('event_cos', (YLeaf(YType.uint32, 'event-cos'), ['int'])),
                    ('general_cos', (YLeaf(YType.uint32, 'general-cos'), ['int'])),
                    ('event_dscp', (YLeaf(YType.uint32, 'event-dscp'), ['int'])),
                    ('general_dscp', (YLeaf(YType.uint32, 'general-dscp'), ['int'])),
                    ('unicast_peers', (YLeaf(YType.uint32, 'unicast-peers'), ['int'])),
                    ('local_priority', (YLeaf(YType.uint8, 'local-priority'), ['int'])),
                    ('signal_fail', (YLeaf(YType.boolean, 'signal-fail'), ['bool'])),
                    ('profile_interop', (YLeaf(YType.boolean, 'profile-interop'), ['bool'])),
                    ('interop_domain', (YLeaf(YType.uint8, 'interop-domain'), ['int'])),
                    ('interop_profile', (YLeaf(YType.enumeration, 'interop-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                ])
                self.interface_name = None
                self.port_state = None
                self.port_number = None
                self.line_state = None
                self.encapsulation = None
                self.ipv6_address = None
                self.ipv4_address = None
                self.two_step = None
                self.communication_model = None
                self.log_sync_interval = None
                self.log_announce_interval = None
                self.announce_timeout = None
                self.log_min_delay_request_interval = None
                self.configured_port_state = None
                self.supports_unicast = None
                self.supports_master = None
                self.supports_one_step = None
                self.supports_two_step = None
                self.supports_ethernet = None
                self.supports_multicast = None
                self.supports_ipv4 = None
                self.supports_ipv6 = None
                self.supports_slave = None
                self.supports_source_ip = None
                self.max_sync_rate = None
                self.event_cos = None
                self.general_cos = None
                self.event_dscp = None
                self.general_dscp = None
                self.unicast_peers = None
                self.local_priority = None
                self.signal_fail = None
                self.profile_interop = None
                self.interop_domain = None
                self.interop_profile = None

                self.ipv6_address_array = Ptp.Interfaces.Interface.Ipv6AddressArray()
                self.ipv6_address_array.parent = self
                self._children_name_map["ipv6_address_array"] = "ipv6-address-array"

                self.ipv4_address_array = Ptp.Interfaces.Interface.Ipv4AddressArray()
                self.ipv4_address_array.parent = self
                self._children_name_map["ipv4_address_array"] = "ipv4-address-array"

                self.mac_address = Ptp.Interfaces.Interface.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"

                self.ingress_conversion = Ptp.Interfaces.Interface.IngressConversion()
                self.ingress_conversion.parent = self
                self._children_name_map["ingress_conversion"] = "ingress-conversion"

                self.egress_conversion = Ptp.Interfaces.Interface.EgressConversion()
                self.egress_conversion.parent = self
                self._children_name_map["egress_conversion"] = "egress-conversion"

                self.master_table = YList(self)
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Interfaces.Interface, ['interface_name', 'port_state', 'port_number', 'line_state', 'encapsulation', 'ipv6_address', 'ipv4_address', 'two_step', 'communication_model', 'log_sync_interval', 'log_announce_interval', 'announce_timeout', 'log_min_delay_request_interval', 'configured_port_state', 'supports_unicast', 'supports_master', 'supports_one_step', 'supports_two_step', 'supports_ethernet', 'supports_multicast', 'supports_ipv4', 'supports_ipv6', 'supports_slave', 'supports_source_ip', 'max_sync_rate', 'event_cos', 'general_cos', 'event_dscp', 'general_dscp', 'unicast_peers', 'local_priority', 'signal_fail', 'profile_interop', 'interop_domain', 'interop_profile'], name, value)


            class Ipv6AddressArray(_Entity_):
                """
                List of Ipv6 addresses, if IPv6 encapsulation is
                being used. If a source address is configured,
                this is the only item in the list
                
                .. attribute:: addr
                
                	List of IPv6 addresses
                	**type**\: list of str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.Ipv6AddressArray, self).__init__()

                    self.yang_name = "ipv6-address-array"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                    ])
                    self.addr = []
                    self._segment_path = lambda: "ipv6-address-array"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.Ipv6AddressArray, ['addr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.Ipv6AddressArray']['meta_info']


            class Ipv4AddressArray(_Entity_):
                """
                List of IPv4 addresses, if IPv4 encapsulation is
                being used. The first address is the primary
                address. If a source address is configured, this
                is the only item in the list.
                
                .. attribute:: addr
                
                	List of IPv4 addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.Ipv4AddressArray, self).__init__()

                    self.yang_name = "ipv4-address-array"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                    ])
                    self.addr = []
                    self._segment_path = lambda: "ipv4-address-array"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.Ipv4AddressArray, ['addr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.Ipv4AddressArray']['meta_info']


            class MacAddress(_Entity_):
                """
                MAC address, if Ethernet encapsulation is being
                used
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.MacAddress, self).__init__()

                    self.yang_name = "mac-address"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                    ])
                    self.macaddr = None
                    self._segment_path = lambda: "mac-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.MacAddress, ['macaddr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.MacAddress']['meta_info']


            class IngressConversion(_Entity_):
                """
                Details of any ingress conversion
                
                .. attribute:: priority1
                
                	Priority 1
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: priority2
                
                	Priority 2
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: accuracy
                
                	Accuracy
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: class_default
                
                	Class Default
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: offset_log_variance
                
                	Offset log variance
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: class_mapping
                
                	Class Mapping
                	**type**\: list of  		 :py:class:`ClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.IngressConversion.ClassMapping>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.IngressConversion, self).__init__()

                    self.yang_name = "ingress-conversion"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class-mapping", ("class_mapping", Ptp.Interfaces.Interface.IngressConversion.ClassMapping))])
                    self._leafs = OrderedDict([
                        ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                        ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                        ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                        ('class_default', (YLeaf(YType.uint8, 'class-default'), ['int'])),
                        ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ])
                    self.priority1 = None
                    self.priority2 = None
                    self.accuracy = None
                    self.class_default = None
                    self.offset_log_variance = None

                    self.class_mapping = YList(self)
                    self._segment_path = lambda: "ingress-conversion"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.IngressConversion, ['priority1', 'priority2', 'accuracy', 'class_default', 'offset_log_variance'], name, value)


                class ClassMapping(_Entity_):
                    """
                    Class Mapping
                    
                    .. attribute:: from_clock_class
                    
                    	From clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_clock_class
                    
                    	To clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Interfaces.Interface.IngressConversion.ClassMapping, self).__init__()

                        self.yang_name = "class-mapping"
                        self.yang_parent_name = "ingress-conversion"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                            ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                        ])
                        self.from_clock_class = None
                        self.to_clock_class = None
                        self._segment_path = lambda: "class-mapping"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Interfaces.Interface.IngressConversion.ClassMapping, ['from_clock_class', 'to_clock_class'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Interfaces.Interface.IngressConversion.ClassMapping']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.IngressConversion']['meta_info']


            class EgressConversion(_Entity_):
                """
                Details of any egress conversion
                
                .. attribute:: priority1
                
                	Priority 1
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: priority2
                
                	Priority 2
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: accuracy
                
                	Accuracy
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: class_default
                
                	Class Default
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: offset_log_variance
                
                	Offset log variance
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: class_mapping
                
                	Class Mapping
                	**type**\: list of  		 :py:class:`ClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.EgressConversion.ClassMapping>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.EgressConversion, self).__init__()

                    self.yang_name = "egress-conversion"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class-mapping", ("class_mapping", Ptp.Interfaces.Interface.EgressConversion.ClassMapping))])
                    self._leafs = OrderedDict([
                        ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                        ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                        ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                        ('class_default', (YLeaf(YType.uint8, 'class-default'), ['int'])),
                        ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ])
                    self.priority1 = None
                    self.priority2 = None
                    self.accuracy = None
                    self.class_default = None
                    self.offset_log_variance = None

                    self.class_mapping = YList(self)
                    self._segment_path = lambda: "egress-conversion"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.EgressConversion, ['priority1', 'priority2', 'accuracy', 'class_default', 'offset_log_variance'], name, value)


                class ClassMapping(_Entity_):
                    """
                    Class Mapping
                    
                    .. attribute:: from_clock_class
                    
                    	From clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: to_clock_class
                    
                    	To clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Interfaces.Interface.EgressConversion.ClassMapping, self).__init__()

                        self.yang_name = "class-mapping"
                        self.yang_parent_name = "egress-conversion"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('from_clock_class', (YLeaf(YType.uint8, 'from-clock-class'), ['int'])),
                            ('to_clock_class', (YLeaf(YType.uint8, 'to-clock-class'), ['int'])),
                        ])
                        self.from_clock_class = None
                        self.to_clock_class = None
                        self._segment_path = lambda: "class-mapping"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Interfaces.Interface.EgressConversion.ClassMapping, ['from_clock_class', 'to_clock_class'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Interfaces.Interface.EgressConversion.ClassMapping']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.EgressConversion']['meta_info']


            class MasterTable(_Entity_):
                """
                The interface's master table
                
                .. attribute:: address
                
                	The address of the master clock
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address>`
                
                	**config**\: False
                
                .. attribute:: communication_model
                
                	The configured communication model of the master clock
                	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                	**config**\: False
                
                .. attribute:: priority
                
                	The priority of the master clock, if it is set
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: known
                
                	Whether the interface is receiving messages from this master
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: qualified
                
                	The master is qualified for best master clock selection
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_grandmaster
                
                	Whether this is the grandmaster
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: is_nonnegotiated
                
                	Whether this master uses non\-negotiated unicast
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Interfaces.Interface.MasterTable, self).__init__()

                    self.yang_name = "master-table"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address", ("address", Ptp.Interfaces.Interface.MasterTable.Address))])
                    self._leafs = OrderedDict([
                        ('communication_model', (YLeaf(YType.enumeration, 'communication-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagCommunicationModel', '')])),
                        ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                        ('known', (YLeaf(YType.boolean, 'known'), ['bool'])),
                        ('qualified', (YLeaf(YType.boolean, 'qualified'), ['bool'])),
                        ('is_grandmaster', (YLeaf(YType.boolean, 'is-grandmaster'), ['bool'])),
                        ('ptsf_loss_announce', (YLeaf(YType.uint8, 'ptsf-loss-announce'), ['int'])),
                        ('ptsf_loss_sync', (YLeaf(YType.uint8, 'ptsf-loss-sync'), ['int'])),
                        ('is_nonnegotiated', (YLeaf(YType.boolean, 'is-nonnegotiated'), ['bool'])),
                    ])
                    self.communication_model = None
                    self.priority = None
                    self.known = None
                    self.qualified = None
                    self.is_grandmaster = None
                    self.ptsf_loss_announce = None
                    self.ptsf_loss_sync = None
                    self.is_nonnegotiated = None

                    self.address = Ptp.Interfaces.Interface.MasterTable.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._segment_path = lambda: "master-table"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.MasterTable, ['communication_model', 'priority', 'known', 'qualified', 'is_grandmaster', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_nonnegotiated'], name, value)


                class Address(_Entity_):
                    """
                    The address of the master clock
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.Interfaces.Interface.MasterTable.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "master-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.Interfaces.Interface.MasterTable.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address))])
                        self._leafs = OrderedDict([
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ])
                        self.encapsulation = None
                        self.address_unknown = None
                        self.ipv4_address = None

                        self.mac_address = Ptp.Interfaces.Interface.MasterTable.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ipv6_address = Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._segment_path = lambda: "address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(_Entity_):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Interfaces.Interface.MasterTable.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Interfaces.Interface.MasterTable.Address.MacAddress']['meta_info']


                    class Ipv6Address(_Entity_):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "ipv6-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address, ['ipv6_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.Interfaces.Interface.MasterTable.Address']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Interfaces.Interface.MasterTable']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.Interfaces']['meta_info']


    class Dataset(_Entity_):
        """
        Global PTP datasets
        
        .. attribute:: default_ds
        
        	defaultDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`DefaultDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.DefaultDs>`
        
        	**config**\: False
        
        .. attribute:: current_ds
        
        	currentDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`CurrentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.CurrentDs>`
        
        	**config**\: False
        
        .. attribute:: parent_ds
        
        	parentDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`ParentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.ParentDs>`
        
        	**config**\: False
        
        .. attribute:: port_dses
        
        	Table for portDS information
        	**type**\:  :py:class:`PortDses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses>`
        
        	**config**\: False
        
        .. attribute:: time_properties_ds
        
        	timePropertiesDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`TimePropertiesDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.TimePropertiesDs>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.Dataset, self).__init__()

            self.yang_name = "dataset"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-ds", ("default_ds", Ptp.Dataset.DefaultDs)), ("current-ds", ("current_ds", Ptp.Dataset.CurrentDs)), ("parent-ds", ("parent_ds", Ptp.Dataset.ParentDs)), ("port-dses", ("port_dses", Ptp.Dataset.PortDses)), ("time-properties-ds", ("time_properties_ds", Ptp.Dataset.TimePropertiesDs))])
            self._leafs = OrderedDict()

            self.default_ds = Ptp.Dataset.DefaultDs()
            self.default_ds.parent = self
            self._children_name_map["default_ds"] = "default-ds"

            self.current_ds = Ptp.Dataset.CurrentDs()
            self.current_ds.parent = self
            self._children_name_map["current_ds"] = "current-ds"

            self.parent_ds = Ptp.Dataset.ParentDs()
            self.parent_ds.parent = self
            self._children_name_map["parent_ds"] = "parent-ds"

            self.port_dses = Ptp.Dataset.PortDses()
            self.port_dses.parent = self
            self._children_name_map["port_dses"] = "port-dses"

            self.time_properties_ds = Ptp.Dataset.TimePropertiesDs()
            self.time_properties_ds.parent = self
            self._children_name_map["time_properties_ds"] = "time-properties-ds"
            self._segment_path = lambda: "dataset"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Dataset, [], name, value)


        class DefaultDs(_Entity_):
            """
            defaultDS information as described in IEEE
            1588\-2008
            
            .. attribute:: two_step_flag
            
            	Is the twoStepFlag set for this clock
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: clock_id
            
            	The local\-clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: number_ports
            
            	The number of active PTP ports on this clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: clock_class
            
            	The clock class of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: clock_accuracy
            
            	The accuracy of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: oslv
            
            	The offset scaled log variance of the local\-clock
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: priority1
            
            	The priority1 of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: priority2
            
            	The priority2 of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: domain_number
            
            	The domain of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: slave_only
            
            	Whether the local\-clock is globally configured as slave\-only
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: local_priority
            
            	Local priority of the local clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: signal_fail
            
            	Signal fail status of the local clock
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Dataset.DefaultDs, self).__init__()

                self.yang_name = "default-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('two_step_flag', (YLeaf(YType.boolean, 'two-step-flag'), ['bool'])),
                    ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                    ('number_ports', (YLeaf(YType.uint32, 'number-ports'), ['int'])),
                    ('clock_class', (YLeaf(YType.uint8, 'clock-class'), ['int'])),
                    ('clock_accuracy', (YLeaf(YType.uint8, 'clock-accuracy'), ['int'])),
                    ('oslv', (YLeaf(YType.uint16, 'oslv'), ['int'])),
                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                    ('domain_number', (YLeaf(YType.uint8, 'domain-number'), ['int'])),
                    ('slave_only', (YLeaf(YType.boolean, 'slave-only'), ['bool'])),
                    ('local_priority', (YLeaf(YType.uint32, 'local-priority'), ['int'])),
                    ('signal_fail', (YLeaf(YType.boolean, 'signal-fail'), ['bool'])),
                ])
                self.two_step_flag = None
                self.clock_id = None
                self.number_ports = None
                self.clock_class = None
                self.clock_accuracy = None
                self.oslv = None
                self.priority1 = None
                self.priority2 = None
                self.domain_number = None
                self.slave_only = None
                self.local_priority = None
                self.signal_fail = None
                self._segment_path = lambda: "default-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.DefaultDs, ['two_step_flag', 'clock_id', 'number_ports', 'clock_class', 'clock_accuracy', 'oslv', 'priority1', 'priority2', 'domain_number', 'slave_only', 'local_priority', 'signal_fail'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Dataset.DefaultDs']['meta_info']


        class CurrentDs(_Entity_):
            """
            currentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: steps_removed
            
            	How many steps removed this clock is from the GM
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: offset_from_master
            
            	The UTC offset of the local\-clock from the GM
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            	**config**\: False
            
            .. attribute:: mean_path_delay
            
            	The mean path delay bewteen the foreign\-master and the local\-clock
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Dataset.CurrentDs, self).__init__()

                self.yang_name = "current-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                    ('offset_from_master', (YLeaf(YType.int64, 'offset-from-master'), ['int'])),
                    ('mean_path_delay', (YLeaf(YType.int64, 'mean-path-delay'), ['int'])),
                ])
                self.steps_removed = None
                self.offset_from_master = None
                self.mean_path_delay = None
                self._segment_path = lambda: "current-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.CurrentDs, ['steps_removed', 'offset_from_master', 'mean_path_delay'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Dataset.CurrentDs']['meta_info']


        class ParentDs(_Entity_):
            """
            parentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: parent_clock_id
            
            	The Clock ID of the parent clock
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: parent_port_number
            
            	The port number on which the parent clock is received
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: parent_stats
            
            	Whether the parentStats is valid
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: observed_parent_oslv
            
            	The observed parent offset scaled log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: observed_parent_clock_phase_change_rate
            
            	The observed rate of change of phase of the parent clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: gm_clock_id
            
            	The Clock ID of the GM
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: gm_clock_class
            
            	The clock class of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: gm_clock_accuracy
            
            	The clock accuracy of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: gmoslv
            
            	The offset scaled log variance of the GM
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: gm_priority1
            
            	The priority1 of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: gm_priority2
            
            	The priority2 of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Dataset.ParentDs, self).__init__()

                self.yang_name = "parent-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('parent_clock_id', (YLeaf(YType.uint64, 'parent-clock-id'), ['int'])),
                    ('parent_port_number', (YLeaf(YType.uint16, 'parent-port-number'), ['int'])),
                    ('parent_stats', (YLeaf(YType.boolean, 'parent-stats'), ['bool'])),
                    ('observed_parent_oslv', (YLeaf(YType.uint16, 'observed-parent-oslv'), ['int'])),
                    ('observed_parent_clock_phase_change_rate', (YLeaf(YType.uint32, 'observed-parent-clock-phase-change-rate'), ['int'])),
                    ('gm_clock_id', (YLeaf(YType.uint64, 'gm-clock-id'), ['int'])),
                    ('gm_clock_class', (YLeaf(YType.uint8, 'gm-clock-class'), ['int'])),
                    ('gm_clock_accuracy', (YLeaf(YType.uint8, 'gm-clock-accuracy'), ['int'])),
                    ('gmoslv', (YLeaf(YType.uint16, 'gmoslv'), ['int'])),
                    ('gm_priority1', (YLeaf(YType.uint8, 'gm-priority1'), ['int'])),
                    ('gm_priority2', (YLeaf(YType.uint8, 'gm-priority2'), ['int'])),
                ])
                self.parent_clock_id = None
                self.parent_port_number = None
                self.parent_stats = None
                self.observed_parent_oslv = None
                self.observed_parent_clock_phase_change_rate = None
                self.gm_clock_id = None
                self.gm_clock_class = None
                self.gm_clock_accuracy = None
                self.gmoslv = None
                self.gm_priority1 = None
                self.gm_priority2 = None
                self._segment_path = lambda: "parent-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.ParentDs, ['parent_clock_id', 'parent_port_number', 'parent_stats', 'observed_parent_oslv', 'observed_parent_clock_phase_change_rate', 'gm_clock_id', 'gm_clock_class', 'gm_clock_accuracy', 'gmoslv', 'gm_priority1', 'gm_priority2'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Dataset.ParentDs']['meta_info']


        class PortDses(_Entity_):
            """
            Table for portDS information
            
            .. attribute:: port_ds
            
            	PortDS information
            	**type**\: list of  		 :py:class:`PortDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses.PortDs>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Dataset.PortDses, self).__init__()

                self.yang_name = "port-dses"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("port-ds", ("port_ds", Ptp.Dataset.PortDses.PortDs))])
                self._leafs = OrderedDict()

                self.port_ds = YList(self)
                self._segment_path = lambda: "port-dses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.PortDses, [], name, value)


            class PortDs(_Entity_):
                """
                PortDS information
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: clock_id
                
                	The ID of the local\-clock
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	The port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: port_state
                
                	The port state
                	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                
                	**config**\: False
                
                .. attribute:: log_min_delay_req_interval
                
                	The log (base 2) of the minimum delay\-request interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: peer_mean_path_delay
                
                	The mean path delay between peers
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: log_announce_interval
                
                	The log (base 2) of the announce interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: annoucne_receipt_timeout
                
                	The announce timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: log_sync_interval
                
                	The log (base 2) of the sync interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: delay_mechanism
                
                	The delay mechanism being used on this port
                	**type**\:  :py:class:`PtpBagDelayMechanism <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagDelayMechanism>`
                
                	**config**\: False
                
                .. attribute:: log_min_p_delay_req_interval
                
                	The log (base 2) of the minimum peer\-delay\-request interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: version_number
                
                	The version of IEEE 1588 being run
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: local_priority
                
                	Local priority of the local clock
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: master_only
                
                	Is the port master\-only?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: signal_fail
                
                	Signal fail status of the port
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Dataset.PortDses.PortDs, self).__init__()

                    self.yang_name = "port-ds"
                    self.yang_parent_name = "port-dses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                        ('port_state', (YLeaf(YType.enumeration, 'port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagPortState', '')])),
                        ('log_min_delay_req_interval', (YLeaf(YType.int16, 'log-min-delay-req-interval'), ['int'])),
                        ('peer_mean_path_delay', (YLeaf(YType.int64, 'peer-mean-path-delay'), ['int'])),
                        ('log_announce_interval', (YLeaf(YType.int16, 'log-announce-interval'), ['int'])),
                        ('annoucne_receipt_timeout', (YLeaf(YType.uint32, 'annoucne-receipt-timeout'), ['int'])),
                        ('log_sync_interval', (YLeaf(YType.int16, 'log-sync-interval'), ['int'])),
                        ('delay_mechanism', (YLeaf(YType.enumeration, 'delay-mechanism'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagDelayMechanism', '')])),
                        ('log_min_p_delay_req_interval', (YLeaf(YType.int16, 'log-min-p-delay-req-interval'), ['int'])),
                        ('version_number', (YLeaf(YType.uint8, 'version-number'), ['int'])),
                        ('local_priority', (YLeaf(YType.uint32, 'local-priority'), ['int'])),
                        ('master_only', (YLeaf(YType.boolean, 'master-only'), ['bool'])),
                        ('signal_fail', (YLeaf(YType.boolean, 'signal-fail'), ['bool'])),
                    ])
                    self.interface_name = None
                    self.clock_id = None
                    self.port_number = None
                    self.port_state = None
                    self.log_min_delay_req_interval = None
                    self.peer_mean_path_delay = None
                    self.log_announce_interval = None
                    self.annoucne_receipt_timeout = None
                    self.log_sync_interval = None
                    self.delay_mechanism = None
                    self.log_min_p_delay_req_interval = None
                    self.version_number = None
                    self.local_priority = None
                    self.master_only = None
                    self.signal_fail = None
                    self._segment_path = lambda: "port-ds" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/port-dses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Dataset.PortDses.PortDs, ['interface_name', 'clock_id', 'port_number', 'port_state', 'log_min_delay_req_interval', 'peer_mean_path_delay', 'log_announce_interval', 'annoucne_receipt_timeout', 'log_sync_interval', 'delay_mechanism', 'log_min_p_delay_req_interval', 'version_number', 'local_priority', 'master_only', 'signal_fail'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Dataset.PortDses.PortDs']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Dataset.PortDses']['meta_info']


        class TimePropertiesDs(_Entity_):
            """
            timePropertiesDS information as described in
            IEEE 1588\-2008
            
            .. attribute:: current_utc_offset
            
            	The current UTC offset
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: current_utc_offset_valid
            
            	Whether the current UTC offset is valid
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: leap59
            
            	Whether the last minute of the day has 59 seconds
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: leap61
            
            	Whether the last minute of the day has 61 seconds
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: time_traceable
            
            	Whether the time\-of\-day source is traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: frequency_traceable
            
            	Whther the frequency source is traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: ptp_timescale
            
            	Whether the timescale being used is the PTP timescale
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: time_source
            
            	The physical time\-source of the GM clock
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Dataset.TimePropertiesDs, self).__init__()

                self.yang_name = "time-properties-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('current_utc_offset', (YLeaf(YType.int16, 'current-utc-offset'), ['int'])),
                    ('current_utc_offset_valid', (YLeaf(YType.boolean, 'current-utc-offset-valid'), ['bool'])),
                    ('leap59', (YLeaf(YType.boolean, 'leap59'), ['bool'])),
                    ('leap61', (YLeaf(YType.boolean, 'leap61'), ['bool'])),
                    ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                    ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                    ('ptp_timescale', (YLeaf(YType.boolean, 'ptp-timescale'), ['bool'])),
                    ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                ])
                self.current_utc_offset = None
                self.current_utc_offset_valid = None
                self.leap59 = None
                self.leap61 = None
                self.time_traceable = None
                self.frequency_traceable = None
                self.ptp_timescale = None
                self.time_source = None
                self._segment_path = lambda: "time-properties-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.TimePropertiesDs, ['current_utc_offset', 'current_utc_offset_valid', 'leap59', 'leap61', 'time_traceable', 'frequency_traceable', 'ptp_timescale', 'time_source'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Dataset.TimePropertiesDs']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.Dataset']['meta_info']


    class GlobalConfigurationError(_Entity_):
        """
        Global configuration error operational data
        
        .. attribute:: configuration_errors
        
        	Configuration Errors
        	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError.ConfigurationErrors>`
        
        	**config**\: False
        
        .. attribute:: clock_profile
        
        	The clock profile
        	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
        
        	**config**\: False
        
        .. attribute:: clock_profile_set
        
        	Is the clock profile set
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: telecom_clock_type
        
        	Configured telecom clock type
        	**type**\:  :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
        
        	**config**\: False
        
        .. attribute:: domain_number
        
        	The PTP domain
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: priority2
        
        	The configured priority2 value
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: virtual_port_priority2
        
        	The configured priority2 value of the virtual port
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: virtual_port_clock_class
        
        	The configured clock class of the virtual port
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: virtual_port_clock_accuracy
        
        	The configured clock accuracy of the virtual port
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: virtual_port_oslv
        
        	The configured oslv of the virtual port
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.GlobalConfigurationError, self).__init__()

            self.yang_name = "global-configuration-error"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("configuration-errors", ("configuration_errors", Ptp.GlobalConfigurationError.ConfigurationErrors))])
            self._leafs = OrderedDict([
                ('clock_profile', (YLeaf(YType.enumeration, 'clock-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagProfile', '')])),
                ('clock_profile_set', (YLeaf(YType.boolean, 'clock-profile-set'), ['bool'])),
                ('telecom_clock_type', (YLeaf(YType.enumeration, 'telecom-clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagTelecomClock', '')])),
                ('domain_number', (YLeaf(YType.uint8, 'domain-number'), ['int'])),
                ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                ('virtual_port_priority2', (YLeaf(YType.uint8, 'virtual-port-priority2'), ['int'])),
                ('virtual_port_clock_class', (YLeaf(YType.uint8, 'virtual-port-clock-class'), ['int'])),
                ('virtual_port_clock_accuracy', (YLeaf(YType.uint8, 'virtual-port-clock-accuracy'), ['int'])),
                ('virtual_port_oslv', (YLeaf(YType.uint16, 'virtual-port-oslv'), ['int'])),
            ])
            self.clock_profile = None
            self.clock_profile_set = None
            self.telecom_clock_type = None
            self.domain_number = None
            self.priority2 = None
            self.virtual_port_priority2 = None
            self.virtual_port_clock_class = None
            self.virtual_port_clock_accuracy = None
            self.virtual_port_oslv = None

            self.configuration_errors = Ptp.GlobalConfigurationError.ConfigurationErrors()
            self.configuration_errors.parent = self
            self._children_name_map["configuration_errors"] = "configuration-errors"
            self._segment_path = lambda: "global-configuration-error"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.GlobalConfigurationError, ['clock_profile', 'clock_profile_set', 'telecom_clock_type', 'domain_number', 'priority2', 'virtual_port_priority2', 'virtual_port_clock_class', 'virtual_port_clock_accuracy', 'virtual_port_oslv'], name, value)


        class ConfigurationErrors(_Entity_):
            """
            Configuration Errors
            
            .. attribute:: domain
            
            	Domain not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: profile_priority1_config
            
            	Priority1 configuration is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: profile_priority2_value
            
            	Priority2 value is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: utc_offset_change
            
            	Leap seconds configuration contains an invalid UTC offset change
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: physical_layer_frequency
            
            	Physical Layer Frequency configuration is not compatible with G.8265.1 profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: profile_virtual_port
            
            	Virtual Port configuration is not compatible with default profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_priority1_config
            
            	Virtual Port priority1 configuration is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_priority2_value
            
            	Virtual Port priority2 value is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_profile_clock_class
            
            	Virtual port clock class is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_clock_accuracy
            
            	Virtual port clock accuracy is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_oslv
            
            	Virtual port OSLV is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: virtual_port_local_priority
            
            	Virtual port local priority configuration is not compatible with configured profile
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.GlobalConfigurationError.ConfigurationErrors, self).__init__()

                self.yang_name = "configuration-errors"
                self.yang_parent_name = "global-configuration-error"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('domain', (YLeaf(YType.boolean, 'domain'), ['bool'])),
                    ('profile_priority1_config', (YLeaf(YType.boolean, 'profile-priority1-config'), ['bool'])),
                    ('profile_priority2_value', (YLeaf(YType.boolean, 'profile-priority2-value'), ['bool'])),
                    ('utc_offset_change', (YLeaf(YType.boolean, 'utc-offset-change'), ['bool'])),
                    ('physical_layer_frequency', (YLeaf(YType.boolean, 'physical-layer-frequency'), ['bool'])),
                    ('profile_virtual_port', (YLeaf(YType.boolean, 'profile-virtual-port'), ['bool'])),
                    ('virtual_port_priority1_config', (YLeaf(YType.boolean, 'virtual-port-priority1-config'), ['bool'])),
                    ('virtual_port_priority2_value', (YLeaf(YType.boolean, 'virtual-port-priority2-value'), ['bool'])),
                    ('virtual_port_profile_clock_class', (YLeaf(YType.boolean, 'virtual-port-profile-clock-class'), ['bool'])),
                    ('virtual_port_clock_accuracy', (YLeaf(YType.boolean, 'virtual-port-clock-accuracy'), ['bool'])),
                    ('virtual_port_oslv', (YLeaf(YType.boolean, 'virtual-port-oslv'), ['bool'])),
                    ('virtual_port_local_priority', (YLeaf(YType.boolean, 'virtual-port-local-priority'), ['bool'])),
                ])
                self.domain = None
                self.profile_priority1_config = None
                self.profile_priority2_value = None
                self.utc_offset_change = None
                self.physical_layer_frequency = None
                self.profile_virtual_port = None
                self.virtual_port_priority1_config = None
                self.virtual_port_priority2_value = None
                self.virtual_port_profile_clock_class = None
                self.virtual_port_clock_accuracy = None
                self.virtual_port_oslv = None
                self.virtual_port_local_priority = None
                self._segment_path = lambda: "configuration-errors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/global-configuration-error/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.GlobalConfigurationError.ConfigurationErrors, ['domain', 'profile_priority1_config', 'profile_priority2_value', 'utc_offset_change', 'physical_layer_frequency', 'profile_virtual_port', 'virtual_port_priority1_config', 'virtual_port_priority2_value', 'virtual_port_profile_clock_class', 'virtual_port_clock_accuracy', 'virtual_port_oslv', 'virtual_port_local_priority'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.GlobalConfigurationError.ConfigurationErrors']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.GlobalConfigurationError']['meta_info']


    class Grandmaster(_Entity_):
        """
        Grandmaster clock operational data
        
        .. attribute:: clock_properties
        
        	Grandmaster clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties>`
        
        	**config**\: False
        
        .. attribute:: address
        
        	The grandmaster's address information
        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address>`
        
        	**config**\: False
        
        .. attribute:: used_for_time
        
        	Whether the grandmaster is setting time\-of\-day on the system
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: used_for_frequency
        
        	Whether the grandmaster is setting frequency on the system
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: known_for_time
        
        	How long the clock has been grandmaster for, in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: second
        
        .. attribute:: domain
        
        	The PTP domain that the grandmaster is in
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.Grandmaster, self).__init__()

            self.yang_name = "grandmaster"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clock-properties", ("clock_properties", Ptp.Grandmaster.ClockProperties)), ("address", ("address", Ptp.Grandmaster.Address))])
            self._leafs = OrderedDict([
                ('used_for_time', (YLeaf(YType.boolean, 'used-for-time'), ['bool'])),
                ('used_for_frequency', (YLeaf(YType.boolean, 'used-for-frequency'), ['bool'])),
                ('known_for_time', (YLeaf(YType.uint32, 'known-for-time'), ['int'])),
                ('domain', (YLeaf(YType.uint8, 'domain'), ['int'])),
            ])
            self.used_for_time = None
            self.used_for_frequency = None
            self.known_for_time = None
            self.domain = None

            self.clock_properties = Ptp.Grandmaster.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"

            self.address = Ptp.Grandmaster.Address()
            self.address.parent = self
            self._children_name_map["address"] = "address"
            self._segment_path = lambda: "grandmaster"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Grandmaster, ['used_for_time', 'used_for_frequency', 'known_for_time', 'domain'], name, value)


        class ClockProperties(_Entity_):
            """
            Grandmaster clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.UtcOffset>`
            
            	**config**\: False
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Receiver>`
            
            	**config**\: False
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Sender>`
            
            	**config**\: False
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            	**config**\: False
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            	**config**\: False
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Grandmaster.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("utc-offset", ("utc_offset", Ptp.Grandmaster.ClockProperties.UtcOffset)), ("receiver", ("receiver", Ptp.Grandmaster.ClockProperties.Receiver)), ("sender", ("sender", Ptp.Grandmaster.ClockProperties.Sender))])
                self._leafs = OrderedDict([
                    ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                    ('priority1', (YLeaf(YType.uint8, 'priority1'), ['int'])),
                    ('priority2', (YLeaf(YType.uint8, 'priority2'), ['int'])),
                    ('class_', (YLeaf(YType.uint8, 'class'), ['int'])),
                    ('accuracy', (YLeaf(YType.uint8, 'accuracy'), ['int'])),
                    ('offset_log_variance', (YLeaf(YType.uint16, 'offset-log-variance'), ['int'])),
                    ('steps_removed', (YLeaf(YType.uint16, 'steps-removed'), ['int'])),
                    ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimeSource', '')])),
                    ('frequency_traceable', (YLeaf(YType.boolean, 'frequency-traceable'), ['bool'])),
                    ('time_traceable', (YLeaf(YType.boolean, 'time-traceable'), ['bool'])),
                    ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockTimescale', '')])),
                    ('leap_seconds', (YLeaf(YType.enumeration, 'leap-seconds'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagClockLeapSeconds', '')])),
                    ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                    ('configured_clock_class', (YLeaf(YType.uint8, 'configured-clock-class'), ['int'])),
                    ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                ])
                self.clock_id = None
                self.priority1 = None
                self.priority2 = None
                self.class_ = None
                self.accuracy = None
                self.offset_log_variance = None
                self.steps_removed = None
                self.time_source = None
                self.frequency_traceable = None
                self.time_traceable = None
                self.timescale = None
                self.leap_seconds = None
                self.local = None
                self.configured_clock_class = None
                self.configured_priority = None

                self.utc_offset = Ptp.Grandmaster.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"

                self.receiver = Ptp.Grandmaster.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"

                self.sender = Ptp.Grandmaster.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(_Entity_):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                	**config**\: False
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Grandmaster.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('current_offset', (YLeaf(YType.int16, 'current-offset'), ['int'])),
                        ('offset_valid', (YLeaf(YType.boolean, 'offset-valid'), ['bool'])),
                    ])
                    self.current_offset = None
                    self.offset_valid = None
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Grandmaster.ClockProperties.UtcOffset']['meta_info']


            class Receiver(_Entity_):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Grandmaster.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Grandmaster.ClockProperties.Receiver']['meta_info']


            class Sender(_Entity_):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Grandmaster.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('clock_id', (YLeaf(YType.uint64, 'clock-id'), ['int'])),
                        ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                    ])
                    self.clock_id = None
                    self.port_number = None
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Grandmaster.ClockProperties.Sender']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Grandmaster.ClockProperties']['meta_info']


        class Address(_Entity_):
            """
            The grandmaster's address information
            
            .. attribute:: mac_address
            
            	Ethernet MAC address
            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.MacAddress>`
            
            	**config**\: False
            
            .. attribute:: ipv6_address
            
            	IPv6 address
            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.Ipv6Address>`
            
            	**config**\: False
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            	**config**\: False
            
            .. attribute:: address_unknown
            
            	Unknown address type
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: ipv4_address
            
            	IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.Grandmaster.Address, self).__init__()

                self.yang_name = "address"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.Grandmaster.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.Grandmaster.Address.Ipv6Address))])
                self._leafs = OrderedDict([
                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                    ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                ])
                self.encapsulation = None
                self.address_unknown = None
                self.ipv4_address = None

                self.mac_address = Ptp.Grandmaster.Address.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"

                self.ipv6_address = Ptp.Grandmaster.Address.Ipv6Address()
                self.ipv6_address.parent = self
                self._children_name_map["ipv6_address"] = "ipv6-address"
                self._segment_path = lambda: "address"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


            class MacAddress(_Entity_):
                """
                Ethernet MAC address
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Grandmaster.Address.MacAddress, self).__init__()

                    self.yang_name = "mac-address"
                    self.yang_parent_name = "address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                    ])
                    self.macaddr = None
                    self._segment_path = lambda: "mac-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/address/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.Address.MacAddress, ['macaddr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Grandmaster.Address.MacAddress']['meta_info']


            class Ipv6Address(_Entity_):
                """
                IPv6 address
                
                .. attribute:: ipv6_address
                
                	IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.Grandmaster.Address.Ipv6Address, self).__init__()

                    self.yang_name = "ipv6-address"
                    self.yang_parent_name = "address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                    ])
                    self.ipv6_address = None
                    self._segment_path = lambda: "ipv6-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/address/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.Address.Ipv6Address, ['ipv6_address'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.Grandmaster.Address.Ipv6Address']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.Grandmaster.Address']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.Grandmaster']['meta_info']


    class InterfaceUnicastPeers(_Entity_):
        """
        Table for interface unicast peers operational
        data
        
        .. attribute:: interface_unicast_peer
        
        	Interface unicast peers operational data
        	**type**\: list of  		 :py:class:`InterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.InterfaceUnicastPeers, self).__init__()

            self.yang_name = "interface-unicast-peers"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-unicast-peer", ("interface_unicast_peer", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer))])
            self._leafs = OrderedDict()

            self.interface_unicast_peer = YList(self)
            self._segment_path = lambda: "interface-unicast-peers"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceUnicastPeers, [], name, value)


        class InterfaceUnicastPeer(_Entity_):
            """
            Interface unicast peers operational data
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: name
            
            	Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: peers
            
            	Unicast Peers
            	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer, self).__init__()

                self.yang_name = "interface-unicast-peer"
                self.yang_parent_name = "interface-unicast-peers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("peers", ("peers", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                ])
                self.interface_name = None
                self.name = None
                self.port_number = None

                self.peers = YList(self)
                self._segment_path = lambda: "interface-unicast-peer" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-unicast-peers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer, ['interface_name', 'name', 'port_number'], name, value)


            class Peers(_Entity_):
                """
                Unicast Peers
                
                .. attribute:: address
                
                	The address of the unicast peer
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address>`
                
                	**config**\: False
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant>`
                
                	**config**\: False
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant>`
                
                	**config**\: False
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "interface-unicast-peer"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address", ("address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address)), ("announce-grant", ("announce_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant)), ("sync-grant", ("sync_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant)), ("delay-response-grant", ("delay_response_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant))])
                    self._leafs = OrderedDict()

                    self.address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"

                    self.announce_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"

                    self.sync_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"

                    self.delay_response_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._segment_path = lambda: "peers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers, [], name, value)


                class Address(_Entity_):
                    """
                    The address of the unicast peer
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac-address", ("mac_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress)), ("ipv6-address", ("ipv6_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address))])
                        self._leafs = OrderedDict([
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper', 'PtpBagEncap', '')])),
                            ('address_unknown', (YLeaf(YType.boolean, 'address-unknown'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ])
                        self.encapsulation = None
                        self.address_unknown = None
                        self.ipv4_address = None

                        self.mac_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"

                        self.ipv6_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._segment_path = lambda: "address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(_Entity_):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "mac-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress']['meta_info']


                    class Ipv6Address(_Entity_):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "ipv6-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address, ['ipv6_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                            return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address']['meta_info']


                class AnnounceGrant(_Entity_):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant, self).__init__()

                        self.yang_name = "announce-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "announce-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant']['meta_info']


                class SyncGrant(_Entity_):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant, self).__init__()

                        self.yang_name = "sync-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "sync-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant']['meta_info']


                class DelayResponseGrant(_Entity_):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant, self).__init__()

                        self.yang_name = "delay-response-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_grant_interval', (YLeaf(YType.int8, 'log-grant-interval'), ['int'])),
                            ('grant_duration', (YLeaf(YType.uint32, 'grant-duration'), ['int'])),
                        ])
                        self.log_grant_interval = None
                        self.grant_duration = None
                        self._segment_path = lambda: "delay-response-grant"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                        return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                    return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.InterfaceUnicastPeers']['meta_info']


    class UtcOffsetInfo(_Entity_):
        """
        UTC offset information
        
        .. attribute:: current_offset_info
        
        	The current UTC offset information
        	**type**\:  :py:class:`CurrentOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.CurrentOffsetInfo>`
        
        	**config**\: False
        
        .. attribute:: current_gm_offset_info
        
        	The UTC offset information recovered from the current grandmaster
        	**type**\:  :py:class:`CurrentGmOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.CurrentGmOffsetInfo>`
        
        	**config**\: False
        
        .. attribute:: configured_offset_info
        
        	The currently configured UTC offset information
        	**type**\:  :py:class:`ConfiguredOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.ConfiguredOffsetInfo>`
        
        	**config**\: False
        
        .. attribute:: previous_gm_offset_info
        
        	The UTC offset information recovered from the prevous grandmaster
        	**type**\:  :py:class:`PreviousGmOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.PreviousGmOffsetInfo>`
        
        	**config**\: False
        
        .. attribute:: hardware_offset_info
        
        	The UTC offset information taken from the hardware
        	**type**\:  :py:class:`HardwareOffsetInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.HardwareOffsetInfo>`
        
        	**config**\: False
        
        .. attribute:: gm_leap_second
        
        	The upcoming leap second advertised by the grandmaster (if there is one)
        	**type**\:  :py:class:`GmLeapSecond <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.GmLeapSecond>`
        
        	**config**\: False
        
        .. attribute:: source_type
        
        	The current source of the UTC offset information
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: source_file
        
        	The URL of the file containing leap second information
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: source_expiry_date
        
        	Source file expiry timestamp, in seconds since UNIX epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: second
        
        .. attribute:: polling_frequency
        
        	Source file polling frequency, in days
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: day
        
        .. attribute:: configured_leap_second
        
        	The list of upcoming configured leap second updates
        	**type**\: list of  		 :py:class:`ConfiguredLeapSecond <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.UtcOffsetInfo.ConfiguredLeapSecond>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ptp.UtcOffsetInfo, self).__init__()

            self.yang_name = "utc-offset-info"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("current-offset-info", ("current_offset_info", Ptp.UtcOffsetInfo.CurrentOffsetInfo)), ("current-gm-offset-info", ("current_gm_offset_info", Ptp.UtcOffsetInfo.CurrentGmOffsetInfo)), ("configured-offset-info", ("configured_offset_info", Ptp.UtcOffsetInfo.ConfiguredOffsetInfo)), ("previous-gm-offset-info", ("previous_gm_offset_info", Ptp.UtcOffsetInfo.PreviousGmOffsetInfo)), ("hardware-offset-info", ("hardware_offset_info", Ptp.UtcOffsetInfo.HardwareOffsetInfo)), ("gm-leap-second", ("gm_leap_second", Ptp.UtcOffsetInfo.GmLeapSecond)), ("configured-leap-second", ("configured_leap_second", Ptp.UtcOffsetInfo.ConfiguredLeapSecond))])
            self._leafs = OrderedDict([
                ('source_type', (YLeaf(YType.uint8, 'source-type'), ['int'])),
                ('source_file', (YLeaf(YType.str, 'source-file'), ['str'])),
                ('source_expiry_date', (YLeaf(YType.uint32, 'source-expiry-date'), ['int'])),
                ('polling_frequency', (YLeaf(YType.uint32, 'polling-frequency'), ['int'])),
            ])
            self.source_type = None
            self.source_file = None
            self.source_expiry_date = None
            self.polling_frequency = None

            self.current_offset_info = Ptp.UtcOffsetInfo.CurrentOffsetInfo()
            self.current_offset_info.parent = self
            self._children_name_map["current_offset_info"] = "current-offset-info"

            self.current_gm_offset_info = Ptp.UtcOffsetInfo.CurrentGmOffsetInfo()
            self.current_gm_offset_info.parent = self
            self._children_name_map["current_gm_offset_info"] = "current-gm-offset-info"

            self.configured_offset_info = Ptp.UtcOffsetInfo.ConfiguredOffsetInfo()
            self.configured_offset_info.parent = self
            self._children_name_map["configured_offset_info"] = "configured-offset-info"

            self.previous_gm_offset_info = Ptp.UtcOffsetInfo.PreviousGmOffsetInfo()
            self.previous_gm_offset_info.parent = self
            self._children_name_map["previous_gm_offset_info"] = "previous-gm-offset-info"

            self.hardware_offset_info = Ptp.UtcOffsetInfo.HardwareOffsetInfo()
            self.hardware_offset_info.parent = self
            self._children_name_map["hardware_offset_info"] = "hardware-offset-info"

            self.gm_leap_second = Ptp.UtcOffsetInfo.GmLeapSecond()
            self.gm_leap_second.parent = self
            self._children_name_map["gm_leap_second"] = "gm-leap-second"

            self.configured_leap_second = YList(self)
            self._segment_path = lambda: "utc-offset-info"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.UtcOffsetInfo, ['source_type', 'source_file', 'source_expiry_date', 'polling_frequency'], name, value)


        class CurrentOffsetInfo(_Entity_):
            """
            The current UTC offset information
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: valid
            
            	Is the UTC offset valid?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: flag
            
            	Indicates the duration of the final minute of the current day
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.CurrentOffsetInfo, self).__init__()

                self.yang_name = "current-offset-info"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                    ('flag', (YLeaf(YType.uint8, 'flag'), ['int'])),
                ])
                self.offset = None
                self.valid = None
                self.flag = None
                self._segment_path = lambda: "current-offset-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.CurrentOffsetInfo, ['offset', 'valid', 'flag'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.CurrentOffsetInfo']['meta_info']


        class CurrentGmOffsetInfo(_Entity_):
            """
            The UTC offset information recovered from the
            current grandmaster
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: valid
            
            	Is the UTC offset valid?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: flag
            
            	Indicates the duration of the final minute of the current day
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.CurrentGmOffsetInfo, self).__init__()

                self.yang_name = "current-gm-offset-info"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                    ('flag', (YLeaf(YType.uint8, 'flag'), ['int'])),
                ])
                self.offset = None
                self.valid = None
                self.flag = None
                self._segment_path = lambda: "current-gm-offset-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.CurrentGmOffsetInfo, ['offset', 'valid', 'flag'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.CurrentGmOffsetInfo']['meta_info']


        class ConfiguredOffsetInfo(_Entity_):
            """
            The currently configured UTC offset information
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: valid
            
            	Is the UTC offset valid?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: flag
            
            	Indicates the duration of the final minute of the current day
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.ConfiguredOffsetInfo, self).__init__()

                self.yang_name = "configured-offset-info"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                    ('flag', (YLeaf(YType.uint8, 'flag'), ['int'])),
                ])
                self.offset = None
                self.valid = None
                self.flag = None
                self._segment_path = lambda: "configured-offset-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.ConfiguredOffsetInfo, ['offset', 'valid', 'flag'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.ConfiguredOffsetInfo']['meta_info']


        class PreviousGmOffsetInfo(_Entity_):
            """
            The UTC offset information recovered from the
            prevous grandmaster
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: valid
            
            	Is the UTC offset valid?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: flag
            
            	Indicates the duration of the final minute of the current day
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.PreviousGmOffsetInfo, self).__init__()

                self.yang_name = "previous-gm-offset-info"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                    ('flag', (YLeaf(YType.uint8, 'flag'), ['int'])),
                ])
                self.offset = None
                self.valid = None
                self.flag = None
                self._segment_path = lambda: "previous-gm-offset-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.PreviousGmOffsetInfo, ['offset', 'valid', 'flag'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.PreviousGmOffsetInfo']['meta_info']


        class HardwareOffsetInfo(_Entity_):
            """
            The UTC offset information taken from the
            hardware
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: valid
            
            	Is the UTC offset valid?
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: flag
            
            	Indicates the duration of the final minute of the current day
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.HardwareOffsetInfo, self).__init__()

                self.yang_name = "hardware-offset-info"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                    ('flag', (YLeaf(YType.uint8, 'flag'), ['int'])),
                ])
                self.offset = None
                self.valid = None
                self.flag = None
                self._segment_path = lambda: "hardware-offset-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.HardwareOffsetInfo, ['offset', 'valid', 'flag'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.HardwareOffsetInfo']['meta_info']


        class GmLeapSecond(_Entity_):
            """
            The upcoming leap second advertised by the
            grandmaster (if there is one)
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: offset_start_date
            
            	The UNIX timestamp at which the offset becomes valid
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: offset_change
            
            	The change in UTC offset on applying this offset
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: offset_applied
            
            	Indicates whether the offset has been applied
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.GmLeapSecond, self).__init__()

                self.yang_name = "gm-leap-second"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('offset_start_date', (YLeaf(YType.uint64, 'offset-start-date'), ['int'])),
                    ('offset_change', (YLeaf(YType.int16, 'offset-change'), ['int'])),
                    ('offset_applied', (YLeaf(YType.boolean, 'offset-applied'), ['bool'])),
                ])
                self.offset = None
                self.offset_start_date = None
                self.offset_change = None
                self.offset_applied = None
                self._segment_path = lambda: "gm-leap-second"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.GmLeapSecond, ['offset', 'offset_start_date', 'offset_change', 'offset_applied'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.GmLeapSecond']['meta_info']


        class ConfiguredLeapSecond(_Entity_):
            """
            The list of upcoming configured leap second
            updates
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: offset_start_date
            
            	The UNIX timestamp at which the offset becomes valid
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: offset_change
            
            	The change in UTC offset on applying this offset
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: offset_applied
            
            	Indicates whether the offset has been applied
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ptp.UtcOffsetInfo.ConfiguredLeapSecond, self).__init__()

                self.yang_name = "configured-leap-second"
                self.yang_parent_name = "utc-offset-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('offset', (YLeaf(YType.int16, 'offset'), ['int'])),
                    ('offset_start_date', (YLeaf(YType.uint64, 'offset-start-date'), ['int'])),
                    ('offset_change', (YLeaf(YType.int16, 'offset-change'), ['int'])),
                    ('offset_applied', (YLeaf(YType.boolean, 'offset-applied'), ['bool'])),
                ])
                self.offset = None
                self.offset_start_date = None
                self.offset_change = None
                self.offset_applied = None
                self._segment_path = lambda: "configured-leap-second"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/utc-offset-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffsetInfo.ConfiguredLeapSecond, ['offset', 'offset_start_date', 'offset_change', 'offset_applied'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
                return meta._meta_table['Ptp.UtcOffsetInfo.ConfiguredLeapSecond']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
            return meta._meta_table['Ptp.UtcOffsetInfo']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ptp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ptp_oper as meta
        return meta._meta_table['Ptp']['meta_info']


