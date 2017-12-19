""" Cisco_IOS_XR_ptp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ptp package operational data.

This module contains definitions
for the following management objects\:
  ptp\: PTP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PtpBagClockLeapSeconds(Enum):
    """
    PtpBagClockLeapSeconds

    Leap Seconds

    .. data:: none = 0

    	No leap seconds

    .. data:: leap59 = 1

    	The last minute of the day has 59 seconds

    .. data:: leap61 = 2

    	The last minute of the day has 61 seconds

    """

    none = Enum.YLeaf(0, "none")

    leap59 = Enum.YLeaf(1, "leap59")

    leap61 = Enum.YLeaf(2, "leap61")


class PtpBagClockTimeSource(Enum):
    """
    PtpBagClockTimeSource

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


class PtpBagClockTimescale(Enum):
    """
    PtpBagClockTimescale

    Timescale

    .. data:: ptp = 0

    	PTP timescale

    .. data:: arb = 1

    	ARB timescale

    """

    ptp = Enum.YLeaf(0, "ptp")

    arb = Enum.YLeaf(1, "arb")


class PtpBagCommunicationModel(Enum):
    """
    PtpBagCommunicationModel

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


class PtpBagDelayMechanism(Enum):
    """
    PtpBagDelayMechanism

    Delay Mechanism

    .. data:: e2e = 0

    	End to end delay mechanism

    .. data:: p2p = 1

    	Peer to peer delay mechanism

    """

    e2e = Enum.YLeaf(0, "e2e")

    p2p = Enum.YLeaf(1, "p2p")


class PtpBagEncap(Enum):
    """
    PtpBagEncap

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


class PtpBagPortState(Enum):
    """
    PtpBagPortState

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


class PtpBagProfile(Enum):
    """
    PtpBagProfile

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


class PtpBagRestrictPortState(Enum):
    """
    PtpBagRestrictPortState

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


class PtpBagTelecomClock(Enum):
    """
    PtpBagTelecomClock

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



class Ptp(Entity):
    """
    PTP operational data
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes>`
    
    .. attribute:: interface_configuration_errors
    
    	Table for interface configuration error operational data
    	**type**\:  :py:class:`InterfaceConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors>`
    
    .. attribute:: interface_foreign_masters
    
    	Table for interface foreign master clock operational data
    	**type**\:  :py:class:`InterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters>`
    
    .. attribute:: local_clock
    
    	Local clock operational data
    	**type**\:  :py:class:`LocalClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock>`
    
    .. attribute:: interface_packet_counters
    
    	Table for interface packet counter operational data
    	**type**\:  :py:class:`InterfacePacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters>`
    
    .. attribute:: advertised_clock
    
    	Advertised clock operational data
    	**type**\:  :py:class:`AdvertisedClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock>`
    
    .. attribute:: leap_seconds
    
    	Upcoming leap\-seconds information
    	**type**\:  :py:class:`LeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LeapSeconds>`
    
    .. attribute:: interfaces
    
    	Table for interface operational data
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces>`
    
    .. attribute:: dataset
    
    	Global PTP datasets
    	**type**\:  :py:class:`Dataset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset>`
    
    .. attribute:: global_configuration_error
    
    	Global configuration error operational data
    	**type**\:  :py:class:`GlobalConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError>`
    
    .. attribute:: grandmaster
    
    	Grandmaster clock operational data
    	**type**\:  :py:class:`Grandmaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster>`
    
    .. attribute:: interface_unicast_peers
    
    	Table for interface unicast peers operational data
    	**type**\:  :py:class:`InterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers>`
    
    .. attribute:: platform
    
    	PTP platform specific data
    	**type**\:  :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform>`
    
    

    """

    _prefix = 'ptp-oper'
    _revision = '2017-02-02'

    def __init__(self):
        super(Ptp, self).__init__()
        self._top_entity = None

        self.yang_name = "ptp"
        self.yang_parent_name = "Cisco-IOS-XR-ptp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", Ptp.Nodes), "interface-configuration-errors" : ("interface_configuration_errors", Ptp.InterfaceConfigurationErrors), "interface-foreign-masters" : ("interface_foreign_masters", Ptp.InterfaceForeignMasters), "local-clock" : ("local_clock", Ptp.LocalClock), "interface-packet-counters" : ("interface_packet_counters", Ptp.InterfacePacketCounters), "advertised-clock" : ("advertised_clock", Ptp.AdvertisedClock), "leap-seconds" : ("leap_seconds", Ptp.LeapSeconds), "interfaces" : ("interfaces", Ptp.Interfaces), "dataset" : ("dataset", Ptp.Dataset), "global-configuration-error" : ("global_configuration_error", Ptp.GlobalConfigurationError), "grandmaster" : ("grandmaster", Ptp.Grandmaster), "interface-unicast-peers" : ("interface_unicast_peers", Ptp.InterfaceUnicastPeers), "Cisco-IOS-XR-ptp-pd-oper:platform" : ("platform", Ptp.Platform)}
        self._child_list_classes = {}

        self.nodes = Ptp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.interface_configuration_errors = Ptp.InterfaceConfigurationErrors()
        self.interface_configuration_errors.parent = self
        self._children_name_map["interface_configuration_errors"] = "interface-configuration-errors"
        self._children_yang_names.add("interface-configuration-errors")

        self.interface_foreign_masters = Ptp.InterfaceForeignMasters()
        self.interface_foreign_masters.parent = self
        self._children_name_map["interface_foreign_masters"] = "interface-foreign-masters"
        self._children_yang_names.add("interface-foreign-masters")

        self.local_clock = Ptp.LocalClock()
        self.local_clock.parent = self
        self._children_name_map["local_clock"] = "local-clock"
        self._children_yang_names.add("local-clock")

        self.interface_packet_counters = Ptp.InterfacePacketCounters()
        self.interface_packet_counters.parent = self
        self._children_name_map["interface_packet_counters"] = "interface-packet-counters"
        self._children_yang_names.add("interface-packet-counters")

        self.advertised_clock = Ptp.AdvertisedClock()
        self.advertised_clock.parent = self
        self._children_name_map["advertised_clock"] = "advertised-clock"
        self._children_yang_names.add("advertised-clock")

        self.leap_seconds = Ptp.LeapSeconds()
        self.leap_seconds.parent = self
        self._children_name_map["leap_seconds"] = "leap-seconds"
        self._children_yang_names.add("leap-seconds")

        self.interfaces = Ptp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.dataset = Ptp.Dataset()
        self.dataset.parent = self
        self._children_name_map["dataset"] = "dataset"
        self._children_yang_names.add("dataset")

        self.global_configuration_error = Ptp.GlobalConfigurationError()
        self.global_configuration_error.parent = self
        self._children_name_map["global_configuration_error"] = "global-configuration-error"
        self._children_yang_names.add("global-configuration-error")

        self.grandmaster = Ptp.Grandmaster()
        self.grandmaster.parent = self
        self._children_name_map["grandmaster"] = "grandmaster"
        self._children_yang_names.add("grandmaster")

        self.interface_unicast_peers = Ptp.InterfaceUnicastPeers()
        self.interface_unicast_peers.parent = self
        self._children_name_map["interface_unicast_peers"] = "interface-unicast-peers"
        self._children_yang_names.add("interface-unicast-peers")

        self.platform = Ptp.Platform()
        self.platform.parent = self
        self._children_name_map["platform"] = "platform"
        self._children_yang_names.add("platform")
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp"


    class Nodes(Entity):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific operational data for a given node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Ptp.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific operational data for a given node
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: node_interface_foreign_masters
            
            	Table for node foreign master clock operational data
            	**type**\:  :py:class:`NodeInterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters>`
            
            .. attribute:: summary
            
            	Node summary operational data
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.Summary>`
            
            .. attribute:: node_interfaces
            
            	Table for node interface operational data
            	**type**\:  :py:class:`NodeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces>`
            
            .. attribute:: node_interface_unicast_peers
            
            	Table for node unicast peers operational data
            	**type**\:  :py:class:`NodeInterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers>`
            
            .. attribute:: packet_counters
            
            	Node packet counter operational data
            	**type**\:  :py:class:`PacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-interface-foreign-masters" : ("node_interface_foreign_masters", Ptp.Nodes.Node.NodeInterfaceForeignMasters), "summary" : ("summary", Ptp.Nodes.Node.Summary), "node-interfaces" : ("node_interfaces", Ptp.Nodes.Node.NodeInterfaces), "node-interface-unicast-peers" : ("node_interface_unicast_peers", Ptp.Nodes.Node.NodeInterfaceUnicastPeers), "packet-counters" : ("packet_counters", Ptp.Nodes.Node.PacketCounters)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.node_interface_foreign_masters = Ptp.Nodes.Node.NodeInterfaceForeignMasters()
                self.node_interface_foreign_masters.parent = self
                self._children_name_map["node_interface_foreign_masters"] = "node-interface-foreign-masters"
                self._children_yang_names.add("node-interface-foreign-masters")

                self.summary = Ptp.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

                self.node_interfaces = Ptp.Nodes.Node.NodeInterfaces()
                self.node_interfaces.parent = self
                self._children_name_map["node_interfaces"] = "node-interfaces"
                self._children_yang_names.add("node-interfaces")

                self.node_interface_unicast_peers = Ptp.Nodes.Node.NodeInterfaceUnicastPeers()
                self.node_interface_unicast_peers.parent = self
                self._children_name_map["node_interface_unicast_peers"] = "node-interface-unicast-peers"
                self._children_yang_names.add("node-interface-unicast-peers")

                self.packet_counters = Ptp.Nodes.Node.PacketCounters()
                self.packet_counters.parent = self
                self._children_name_map["packet_counters"] = "packet-counters"
                self._children_yang_names.add("packet-counters")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Nodes.Node, ['node_name'], name, value)


            class NodeInterfaceForeignMasters(Entity):
                """
                Table for node foreign master clock
                operational data
                
                .. attribute:: node_interface_foreign_master
                
                	Node interface foreign master clock operational data
                	**type**\: list of  		 :py:class:`NodeInterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters, self).__init__()

                    self.yang_name = "node-interface-foreign-masters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-interface-foreign-master" : ("node_interface_foreign_master", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster)}

                    self.node_interface_foreign_master = YList(self)
                    self._segment_path = lambda: "node-interface-foreign-masters"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters, [], name, value)


                class NodeInterfaceForeignMaster(Entity):
                    """
                    Node interface foreign master clock
                    operational data
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: foreign_clock
                    
                    	Foreign clocks received on this interface
                    	**type**\: list of  		 :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster, self).__init__()

                        self.yang_name = "node-interface-foreign-master"
                        self.yang_parent_name = "node-interface-foreign-masters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"foreign-clock" : ("foreign_clock", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.port_number = YLeaf(YType.uint16, "port-number")

                        self.foreign_clock = YList(self)
                        self._segment_path = lambda: "node-interface-foreign-master" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster, ['interface_name', 'port_number'], name, value)


                    class ForeignClock(Entity):
                        """
                        Foreign clocks received on this interface
                        
                        .. attribute:: foreign_clock
                        
                        	Foreign clock information
                        	**type**\:  :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock>`
                        
                        .. attribute:: address
                        
                        	The address of the clock
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address>`
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant>`
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                        
                        .. attribute:: is_qualified
                        
                        	The clock is qualified for best master clock selection
                        	**type**\: bool
                        
                        .. attribute:: is_grandmaster
                        
                        	This clock is the currently selected grand master clock
                        	**type**\: bool
                        
                        .. attribute:: communication_model
                        
                        	The communication model configured on this clock
                        	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        .. attribute:: is_known
                        
                        	This clock is known by this router
                        	**type**\: bool
                        
                        .. attribute:: time_known_for
                        
                        	How long the clock has been known by this router for, in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: foreign_domain
                        
                        	The PTP domain that the foreign clock is in
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: configured_priority
                        
                        	Priority configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: configured_clock_class
                        
                        	Clock class configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: delay_asymmetry
                        
                        	Delay asymmetry configured for the clock, if any
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\: bool
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, self).__init__()

                            self.yang_name = "foreign-clock"
                            self.yang_parent_name = "node-interface-foreign-master"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"foreign-clock" : ("foreign_clock", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock), "address" : ("address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address), "announce-grant" : ("announce_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant), "sync-grant" : ("sync_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant), "delay-response-grant" : ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant)}
                            self._child_list_classes = {}

                            self.is_qualified = YLeaf(YType.boolean, "is-qualified")

                            self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                            self.communication_model = YLeaf(YType.enumeration, "communication-model")

                            self.is_known = YLeaf(YType.boolean, "is-known")

                            self.time_known_for = YLeaf(YType.uint32, "time-known-for")

                            self.foreign_domain = YLeaf(YType.uint8, "foreign-domain")

                            self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                            self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                            self.delay_asymmetry = YLeaf(YType.int32, "delay-asymmetry")

                            self.ptsf_loss_announce = YLeaf(YType.boolean, "ptsf-loss-announce")

                            self.ptsf_loss_sync = YLeaf(YType.boolean, "ptsf-loss-sync")

                            self.foreign_clock = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock()
                            self.foreign_clock.parent = self
                            self._children_name_map["foreign_clock"] = "foreign-clock"
                            self._children_yang_names.add("foreign-clock")

                            self.address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"
                            self._children_yang_names.add("announce-grant")

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"
                            self._children_yang_names.add("sync-grant")

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._children_yang_names.add("delay-response-grant")
                            self._segment_path = lambda: "foreign-clock"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, ['is_qualified', 'is_grandmaster', 'communication_model', 'is_known', 'time_known_for', 'foreign_domain', 'configured_priority', 'configured_clock_class', 'delay_asymmetry', 'ptsf_loss_announce', 'ptsf_loss_sync'], name, value)


                        class ForeignClock(Entity):
                            """
                            Foreign clock information
                            
                            .. attribute:: utc_offset
                            
                            	UTC offset
                            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset>`
                            
                            .. attribute:: receiver
                            
                            	Receiver
                            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver>`
                            
                            .. attribute:: sender
                            
                            	Sender
                            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender>`
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: priority1
                            
                            	Priority 1
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority2
                            
                            	Priority 2
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: class_
                            
                            	Class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: accuracy
                            
                            	Accuracy
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: offset_log_variance
                            
                            	Offset log variance
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: steps_removed
                            
                            	Steps removed
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: time_source
                            
                            	Time source
                            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                            
                            .. attribute:: frequency_traceable
                            
                            	The clock is frequency traceable
                            	**type**\: bool
                            
                            .. attribute:: time_traceable
                            
                            	The clock is time traceable
                            	**type**\: bool
                            
                            .. attribute:: timescale
                            
                            	Timescale
                            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                            
                            .. attribute:: leap_seconds
                            
                            	Leap Seconds
                            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                            
                            	**units**\: second
                            
                            .. attribute:: local
                            
                            	The clock is the local clock
                            	**type**\: bool
                            
                            .. attribute:: configured_clock_class
                            
                            	The configured clock class
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: configured_priority
                            
                            	The configured priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock, self).__init__()

                                self.yang_name = "foreign-clock"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"utc-offset" : ("utc_offset", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset), "receiver" : ("receiver", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver), "sender" : ("sender", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender)}
                                self._child_list_classes = {}

                                self.clock_id = YLeaf(YType.uint64, "clock-id")

                                self.priority1 = YLeaf(YType.uint8, "priority1")

                                self.priority2 = YLeaf(YType.uint8, "priority2")

                                self.class_ = YLeaf(YType.uint8, "class")

                                self.accuracy = YLeaf(YType.uint8, "accuracy")

                                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                                self.time_source = YLeaf(YType.enumeration, "time-source")

                                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                                self.timescale = YLeaf(YType.enumeration, "timescale")

                                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                                self.local = YLeaf(YType.boolean, "local")

                                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                                self.utc_offset = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset()
                                self.utc_offset.parent = self
                                self._children_name_map["utc_offset"] = "utc-offset"
                                self._children_yang_names.add("utc-offset")

                                self.receiver = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver()
                                self.receiver.parent = self
                                self._children_name_map["receiver"] = "receiver"
                                self._children_yang_names.add("receiver")

                                self.sender = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender()
                                self.sender.parent = self
                                self._children_name_map["sender"] = "sender"
                                self._children_yang_names.add("sender")
                                self._segment_path = lambda: "foreign-clock"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


                            class UtcOffset(Entity):
                                """
                                UTC offset
                                
                                .. attribute:: current_offset
                                
                                	Current offset
                                	**type**\: int
                                
                                	**range:** \-32768..32767
                                
                                .. attribute:: offset_valid
                                
                                	The current offset is valid
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset, self).__init__()

                                    self.yang_name = "utc-offset"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.current_offset = YLeaf(YType.int16, "current-offset")

                                    self.offset_valid = YLeaf(YType.boolean, "offset-valid")
                                    self._segment_path = lambda: "utc-offset"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset, ['current_offset', 'offset_valid'], name, value)


                            class Receiver(Entity):
                                """
                                Receiver
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver, self).__init__()

                                    self.yang_name = "receiver"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                                    self.port_number = YLeaf(YType.uint16, "port-number")
                                    self._segment_path = lambda: "receiver"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver, ['clock_id', 'port_number'], name, value)


                            class Sender(Entity):
                                """
                                Sender
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender, self).__init__()

                                    self.yang_name = "sender"
                                    self.yang_parent_name = "foreign-clock"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                                    self.port_number = YLeaf(YType.uint16, "port-number")
                                    self._segment_path = lambda: "sender"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender, ['clock_id', 'port_number'], name, value)


                        class Address(Entity):
                            """
                            The address of the clock
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address)}
                                self._child_list_classes = {}

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.macaddr = YLeaf(YType.str, "macaddr")
                                    self._segment_path = lambda: "mac-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress, ['macaddr'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "ipv6-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address, ['ipv6_address'], name, value)


                        class AnnounceGrant(Entity):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant, self).__init__()

                                self.yang_name = "announce-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "announce-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)


                        class SyncGrant(Entity):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant, self).__init__()

                                self.yang_name = "sync-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "sync-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)


                        class DelayResponseGrant(Entity):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant, self).__init__()

                                self.yang_name = "delay-response-grant"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "delay-response-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)


            class Summary(Entity):
                """
                Node summary operational data
                
                .. attribute:: port_state_init_count
                
                	Number of interfaces in 'Init' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_listening_count
                
                	Number of interfaces in 'Listening' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_passive_count
                
                	Number of interfaces in 'Passive' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_pre_master_count
                
                	Number of interfaces in 'Pre\-Master' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_master_count
                
                	Number of interfaces in 'Master' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_slave_count
                
                	Number of interfaces in 'Slave' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_uncalibrated_count
                
                	Number of interfaces in 'Uncalibrated port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_faulty_count
                
                	Number of interfaces in 'Faulty' port state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_interfaces
                
                	Total number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_interfaces_valid_port_num
                
                	Total number of interfaces with a valid port number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.port_state_init_count = YLeaf(YType.uint32, "port-state-init-count")

                    self.port_state_listening_count = YLeaf(YType.uint32, "port-state-listening-count")

                    self.port_state_passive_count = YLeaf(YType.uint32, "port-state-passive-count")

                    self.port_state_pre_master_count = YLeaf(YType.uint32, "port-state-pre-master-count")

                    self.port_state_master_count = YLeaf(YType.uint32, "port-state-master-count")

                    self.port_state_slave_count = YLeaf(YType.uint32, "port-state-slave-count")

                    self.port_state_uncalibrated_count = YLeaf(YType.uint32, "port-state-uncalibrated-count")

                    self.port_state_faulty_count = YLeaf(YType.uint32, "port-state-faulty-count")

                    self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                    self.total_interfaces_valid_port_num = YLeaf(YType.uint32, "total-interfaces-valid-port-num")
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.Summary, ['port_state_init_count', 'port_state_listening_count', 'port_state_passive_count', 'port_state_pre_master_count', 'port_state_master_count', 'port_state_slave_count', 'port_state_uncalibrated_count', 'port_state_faulty_count', 'total_interfaces', 'total_interfaces_valid_port_num'], name, value)


            class NodeInterfaces(Entity):
                """
                Table for node interface operational data
                
                .. attribute:: node_interface
                
                	Node interface operational data
                	**type**\: list of  		 :py:class:`NodeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Nodes.Node.NodeInterfaces, self).__init__()

                    self.yang_name = "node-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-interface" : ("node_interface", Ptp.Nodes.Node.NodeInterfaces.NodeInterface)}

                    self.node_interface = YList(self)
                    self._segment_path = lambda: "node-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces, [], name, value)


                class NodeInterface(Entity):
                    """
                    Node interface operational data
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: mac_address
                    
                    	MAC address, if Ethernet encapsulation is being used
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress>`
                    
                    .. attribute:: port_state
                    
                    	Port state
                    	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: line_state
                    
                    	Line state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: ipv6_address
                    
                    	Ipv6 address, if IPv6 encapsulation is being used
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address, if IPv4 encapsulation is being used
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: two_step
                    
                    	Two step delay\-request mechanism is being used
                    	**type**\: bool
                    
                    .. attribute:: communication_model
                    
                    	Communication model configured on the interface
                    	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                    
                    .. attribute:: log_sync_interval
                    
                    	Log of the interface's sync interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: log_announce_interval
                    
                    	Log of the interface's announce interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: announce_timeout
                    
                    	Announce timeout
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_min_delay_request_interval
                    
                    	Log of the interface's Minimum delay\-request interval
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: configured_port_state
                    
                    	The configured port state
                    	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
                    
                    .. attribute:: supports_one_step
                    
                    	The interface supports one\-step operation
                    	**type**\: bool
                    
                    .. attribute:: supports_two_step
                    
                    	The interface supports two\-step operation
                    	**type**\: bool
                    
                    .. attribute:: supports_ethernet
                    
                    	The interface supports ethernet transport
                    	**type**\: bool
                    
                    .. attribute:: supports_multicast
                    
                    	The interface supports multicast
                    	**type**\: bool
                    
                    .. attribute:: supports_ipv6
                    
                    	The interface supports IPv6 transport
                    	**type**\: bool
                    
                    .. attribute:: supports_slave
                    
                    	The interface supports operation in slave mode
                    	**type**\: bool
                    
                    .. attribute:: supports_source_ip
                    
                    	The interface supports source ip configuration
                    	**type**\: bool
                    
                    .. attribute:: max_sync_rate
                    
                    	The maximum rate of sync packets on the interface
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: event_cos
                    
                    	The class of service used on the interface for event messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: general_cos
                    
                    	The class of service used on the interface for general messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_dscp
                    
                    	The DSCP class used on the interface for event messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: general_dscp
                    
                    	The DSCP class used on the interface for general messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unicast_peers
                    
                    	The number of unicast peers known by the interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_priority
                    
                    	Local priority, for the G.8275.1 PTP profile
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: signal_fail
                    
                    	Signal fail status of the interface
                    	**type**\: bool
                    
                    .. attribute:: master_table
                    
                    	The interface's master table
                    	**type**\: list of  		 :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface, self).__init__()

                        self.yang_name = "node-interface"
                        self.yang_parent_name = "node-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress)}
                        self._child_list_classes = {"master-table" : ("master_table", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.port_state = YLeaf(YType.enumeration, "port-state")

                        self.port_number = YLeaf(YType.uint16, "port-number")

                        self.line_state = YLeaf(YType.uint32, "line-state")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.two_step = YLeaf(YType.boolean, "two-step")

                        self.communication_model = YLeaf(YType.enumeration, "communication-model")

                        self.log_sync_interval = YLeaf(YType.int32, "log-sync-interval")

                        self.log_announce_interval = YLeaf(YType.int32, "log-announce-interval")

                        self.announce_timeout = YLeaf(YType.uint32, "announce-timeout")

                        self.log_min_delay_request_interval = YLeaf(YType.int32, "log-min-delay-request-interval")

                        self.configured_port_state = YLeaf(YType.enumeration, "configured-port-state")

                        self.supports_one_step = YLeaf(YType.boolean, "supports-one-step")

                        self.supports_two_step = YLeaf(YType.boolean, "supports-two-step")

                        self.supports_ethernet = YLeaf(YType.boolean, "supports-ethernet")

                        self.supports_multicast = YLeaf(YType.boolean, "supports-multicast")

                        self.supports_ipv6 = YLeaf(YType.boolean, "supports-ipv6")

                        self.supports_slave = YLeaf(YType.boolean, "supports-slave")

                        self.supports_source_ip = YLeaf(YType.boolean, "supports-source-ip")

                        self.max_sync_rate = YLeaf(YType.uint8, "max-sync-rate")

                        self.event_cos = YLeaf(YType.uint32, "event-cos")

                        self.general_cos = YLeaf(YType.uint32, "general-cos")

                        self.event_dscp = YLeaf(YType.uint32, "event-dscp")

                        self.general_dscp = YLeaf(YType.uint32, "general-dscp")

                        self.unicast_peers = YLeaf(YType.uint32, "unicast-peers")

                        self.local_priority = YLeaf(YType.uint8, "local-priority")

                        self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                        self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.master_table = YList(self)
                        self._segment_path = lambda: "node-interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface, ['interface_name', 'port_state', 'port_number', 'line_state', 'encapsulation', 'ipv6_address', 'ipv4_address', 'two_step', 'communication_model', 'log_sync_interval', 'log_announce_interval', 'announce_timeout', 'log_min_delay_request_interval', 'configured_port_state', 'supports_one_step', 'supports_two_step', 'supports_ethernet', 'supports_multicast', 'supports_ipv6', 'supports_slave', 'supports_source_ip', 'max_sync_rate', 'event_cos', 'general_cos', 'event_dscp', 'general_dscp', 'unicast_peers', 'local_priority', 'signal_fail'], name, value)


                    class MacAddress(Entity):
                        """
                        MAC address, if Ethernet encapsulation is being
                        used
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "mac-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress, ['macaddr'], name, value)


                    class MasterTable(Entity):
                        """
                        The interface's master table
                        
                        .. attribute:: address
                        
                        	The address of the master clock
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address>`
                        
                        .. attribute:: communication_model
                        
                        	The configured communication model of the master clock
                        	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        .. attribute:: priority
                        
                        	The priority of the master clock, if it is set
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: known
                        
                        	Whether the interface is receiving messages from this master
                        	**type**\: bool
                        
                        .. attribute:: qualified
                        
                        	The master is qualified for best master clock selection
                        	**type**\: bool
                        
                        .. attribute:: is_grandmaster
                        
                        	Whether this is the grandmaster
                        	**type**\: bool
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_nonnegotiated
                        
                        	Whether this master uses non\-negotiated unicast
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable, self).__init__()

                            self.yang_name = "master-table"
                            self.yang_parent_name = "node-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address" : ("address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address)}
                            self._child_list_classes = {}

                            self.communication_model = YLeaf(YType.enumeration, "communication-model")

                            self.priority = YLeaf(YType.uint8, "priority")

                            self.known = YLeaf(YType.boolean, "known")

                            self.qualified = YLeaf(YType.boolean, "qualified")

                            self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                            self.ptsf_loss_announce = YLeaf(YType.uint8, "ptsf-loss-announce")

                            self.ptsf_loss_sync = YLeaf(YType.uint8, "ptsf-loss-sync")

                            self.is_nonnegotiated = YLeaf(YType.boolean, "is-nonnegotiated")

                            self.address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")
                            self._segment_path = lambda: "master-table"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable, ['communication_model', 'priority', 'known', 'qualified', 'is_grandmaster', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_nonnegotiated'], name, value)


                        class Address(Entity):
                            """
                            The address of the master clock
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress>`
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address>`
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "master-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address)}
                                self._child_list_classes = {}

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.macaddr = YLeaf(YType.str, "macaddr")
                                    self._segment_path = lambda: "mac-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress, ['macaddr'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "ipv6-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address, ['ipv6_address'], name, value)


            class NodeInterfaceUnicastPeers(Entity):
                """
                Table for node unicast peers operational data
                
                .. attribute:: node_interface_unicast_peer
                
                	Node interface unicast peers operational data
                	**type**\: list of  		 :py:class:`NodeInterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers, self).__init__()

                    self.yang_name = "node-interface-unicast-peers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-interface-unicast-peer" : ("node_interface_unicast_peer", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer)}

                    self.node_interface_unicast_peer = YList(self)
                    self._segment_path = lambda: "node-interface-unicast-peers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers, [], name, value)


                class NodeInterfaceUnicastPeer(Entity):
                    """
                    Node interface unicast peers operational data
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: peers
                    
                    	Unicast Peers
                    	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer, self).__init__()

                        self.yang_name = "node-interface-unicast-peer"
                        self.yang_parent_name = "node-interface-unicast-peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peers" : ("peers", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.name = YLeaf(YType.str, "name")

                        self.port_number = YLeaf(YType.uint16, "port-number")

                        self.peers = YList(self)
                        self._segment_path = lambda: "node-interface-unicast-peer" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer, ['interface_name', 'name', 'port_number'], name, value)


                    class Peers(Entity):
                        """
                        Unicast Peers
                        
                        .. attribute:: address
                        
                        	The address of the unicast peer
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address>`
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant>`
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant>`
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant>`
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers, self).__init__()

                            self.yang_name = "peers"
                            self.yang_parent_name = "node-interface-unicast-peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address" : ("address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address), "announce-grant" : ("announce_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant), "sync-grant" : ("sync_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant), "delay-response-grant" : ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant)}
                            self._child_list_classes = {}

                            self.address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"
                            self._children_yang_names.add("announce-grant")

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"
                            self._children_yang_names.add("sync-grant")

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._children_yang_names.add("delay-response-grant")
                            self._segment_path = lambda: "peers"


                        class Address(Entity):
                            """
                            The address of the unicast peer
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress>`
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\: bool
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address)}
                                self._child_list_classes = {}

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress, self).__init__()

                                    self.yang_name = "mac-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.macaddr = YLeaf(YType.str, "macaddr")
                                    self._segment_path = lambda: "mac-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress, ['macaddr'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ptp-oper'
                                _revision = '2017-02-02'

                                def __init__(self):
                                    super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address, self).__init__()

                                    self.yang_name = "ipv6-address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "ipv6-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address, ['ipv6_address'], name, value)


                        class AnnounceGrant(Entity):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant, self).__init__()

                                self.yang_name = "announce-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "announce-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)


                        class SyncGrant(Entity):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant, self).__init__()

                                self.yang_name = "sync-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "sync-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)


                        class DelayResponseGrant(Entity):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\: int
                            
                            	**range:** \-128..127
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant, self).__init__()

                                self.yang_name = "delay-response-grant"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                                self._segment_path = lambda: "delay-response-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)


            class PacketCounters(Entity):
                """
                Node packet counter operational data
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.Counters>`
                
                .. attribute:: drop_reasons
                
                	Drop reasons
                	**type**\:  :py:class:`DropReasons <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.DropReasons>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Nodes.Node.PacketCounters, self).__init__()

                    self.yang_name = "packet-counters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"counters" : ("counters", Ptp.Nodes.Node.PacketCounters.Counters), "drop-reasons" : ("drop_reasons", Ptp.Nodes.Node.PacketCounters.DropReasons)}
                    self._child_list_classes = {}

                    self.counters = Ptp.Nodes.Node.PacketCounters.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"
                    self._children_yang_names.add("counters")

                    self.drop_reasons = Ptp.Nodes.Node.PacketCounters.DropReasons()
                    self.drop_reasons.parent = self
                    self._children_name_map["drop_reasons"] = "drop-reasons"
                    self._children_yang_names.add("drop-reasons")
                    self._segment_path = lambda: "packet-counters"


                class Counters(Entity):
                    """
                    Packet counters
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Nodes.Node.PacketCounters.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "packet-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                        self.announce_received = YLeaf(YType.uint32, "announce-received")

                        self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                        self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                        self.sync_received = YLeaf(YType.uint32, "sync-received")

                        self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                        self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                        self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                        self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                        self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                        self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                        self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                        self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                        self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                        self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                        self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                        self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                        self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                        self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                        self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                        self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                        self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                        self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                        self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                        self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                        self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                        self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                        self.management_sent = YLeaf(YType.uint32, "management-sent")

                        self.management_received = YLeaf(YType.uint32, "management-received")

                        self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                        self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                        self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                        self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                        self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")

                        self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                        self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)


                class DropReasons(Entity):
                    """
                    Drop reasons
                    
                    .. attribute:: not_ready
                    
                    	Not ready for packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_domain
                    
                    	Wrong domain number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: too_short
                    
                    	Packet too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_same_port
                    
                    	Local packet received, same port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_higher_port
                    
                    	Local packet received, higher port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_lower_port
                    
                    	Local packet received, lower port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_timestamp
                    
                    	No timestamp received with packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: zero_timestamp
                    
                    	Zero timestamp received with packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_tl_vs
                    
                    	Invalid TLVs received in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_for_us
                    
                    	Packet not for us
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_listening
                    
                    	Not listening for packets on this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_master
                    
                    	Packet from incorrect master
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_master
                    
                    	Packet from unknown master
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_master
                    
                    	Packet only handled in Master state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_slave
                    
                    	Packet only handled in Slave state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_granted
                    
                    	Packet from peer not granted unicast
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: too_slow
                    
                    	Packet received too late
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_packet
                    
                    	Invalid packet or packet metadata
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_sequence_id
                    
                    	Unexpected sequence ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_offload_session
                    
                    	No offload session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_supported
                    
                    	PTP packet type not supported
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_clock_class
                    
                    	Clock class below minimum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g8275_1_incompatible
                    
                    	Packet not compatible with G.8275.1 profile
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g8275_2_incompatible
                    
                    	Packet not compatible with G.8275.2 profile
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Nodes.Node.PacketCounters.DropReasons, self).__init__()

                        self.yang_name = "drop-reasons"
                        self.yang_parent_name = "packet-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.not_ready = YLeaf(YType.uint32, "not-ready")

                        self.wrong_domain = YLeaf(YType.uint32, "wrong-domain")

                        self.too_short = YLeaf(YType.uint32, "too-short")

                        self.looped_same_port = YLeaf(YType.uint32, "looped-same-port")

                        self.looped_higher_port = YLeaf(YType.uint32, "looped-higher-port")

                        self.looped_lower_port = YLeaf(YType.uint32, "looped-lower-port")

                        self.no_timestamp = YLeaf(YType.uint32, "no-timestamp")

                        self.zero_timestamp = YLeaf(YType.uint32, "zero-timestamp")

                        self.invalid_tl_vs = YLeaf(YType.uint32, "invalid-tl-vs")

                        self.not_for_us = YLeaf(YType.uint32, "not-for-us")

                        self.not_listening = YLeaf(YType.uint32, "not-listening")

                        self.wrong_master = YLeaf(YType.uint32, "wrong-master")

                        self.unknown_master = YLeaf(YType.uint32, "unknown-master")

                        self.not_master = YLeaf(YType.uint32, "not-master")

                        self.not_slave = YLeaf(YType.uint32, "not-slave")

                        self.not_granted = YLeaf(YType.uint32, "not-granted")

                        self.too_slow = YLeaf(YType.uint32, "too-slow")

                        self.invalid_packet = YLeaf(YType.uint32, "invalid-packet")

                        self.wrong_sequence_id = YLeaf(YType.uint32, "wrong-sequence-id")

                        self.no_offload_session = YLeaf(YType.uint32, "no-offload-session")

                        self.not_supported = YLeaf(YType.uint32, "not-supported")

                        self.min_clock_class = YLeaf(YType.uint32, "min-clock-class")

                        self.g8275_1_incompatible = YLeaf(YType.uint32, "g8275-1-incompatible")

                        self.g8275_2_incompatible = YLeaf(YType.uint32, "g8275-2-incompatible")
                        self._segment_path = lambda: "drop-reasons"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.DropReasons, ['not_ready', 'wrong_domain', 'too_short', 'looped_same_port', 'looped_higher_port', 'looped_lower_port', 'no_timestamp', 'zero_timestamp', 'invalid_tl_vs', 'not_for_us', 'not_listening', 'wrong_master', 'unknown_master', 'not_master', 'not_slave', 'not_granted', 'too_slow', 'invalid_packet', 'wrong_sequence_id', 'no_offload_session', 'not_supported', 'min_clock_class', 'g8275_1_incompatible', 'g8275_2_incompatible'], name, value)


    class InterfaceConfigurationErrors(Entity):
        """
        Table for interface configuration error
        operational data
        
        .. attribute:: interface_configuration_error
        
        	Interface configuration error operational data
        	**type**\: list of  		 :py:class:`InterfaceConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.InterfaceConfigurationErrors, self).__init__()

            self.yang_name = "interface-configuration-errors"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-configuration-error" : ("interface_configuration_error", Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError)}

            self.interface_configuration_error = YList(self)
            self._segment_path = lambda: "interface-configuration-errors"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceConfigurationErrors, [], name, value)


        class InterfaceConfigurationError(Entity):
            """
            Interface configuration error operational data
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: configuration_errors
            
            	Configuration Errors
            	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors>`
            
            .. attribute:: configuration_profile_name
            
            	Configuration profile name, if a profile is selected
            	**type**\: str
            
            .. attribute:: clock_profile
            
            	The clock profile
            	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            .. attribute:: telecom_clock_type
            
            	The telecom clock type
            	**type**\:  :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
            
            .. attribute:: restrict_port_state
            
            	Restriction on the port state
            	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError, self).__init__()

                self.yang_name = "interface-configuration-error"
                self.yang_parent_name = "interface-configuration-errors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"configuration-errors" : ("configuration_errors", Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.configuration_profile_name = YLeaf(YType.str, "configuration-profile-name")

                self.clock_profile = YLeaf(YType.enumeration, "clock-profile")

                self.telecom_clock_type = YLeaf(YType.enumeration, "telecom-clock-type")

                self.restrict_port_state = YLeaf(YType.enumeration, "restrict-port-state")

                self.configuration_errors = Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors()
                self.configuration_errors.parent = self
                self._children_name_map["configuration_errors"] = "configuration-errors"
                self._children_yang_names.add("configuration-errors")
                self._segment_path = lambda: "interface-configuration-error" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-configuration-errors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError, ['interface_name', 'configuration_profile_name', 'clock_profile', 'telecom_clock_type', 'restrict_port_state'], name, value)


            class ConfigurationErrors(Entity):
                """
                Configuration Errors
                
                .. attribute:: global_ptp
                
                	PTP enabled on interface but not globally
                	**type**\: bool
                
                .. attribute:: ethernet_transport
                
                	Ethernet transport configured but not supported
                	**type**\: bool
                
                .. attribute:: one_step
                
                	One step clock operation configured but not supported
                	**type**\: bool
                
                .. attribute:: slave
                
                	Slave\-operation configured but not supported
                	**type**\: bool
                
                .. attribute:: ipv6
                
                	IPv6 transport configured but not supported
                	**type**\: bool
                
                .. attribute:: multicast
                
                	Multicast configured but not supported
                	**type**\: bool
                
                .. attribute:: profile_not_global
                
                	Profile is referenced but not globally configured
                	**type**\: bool
                
                .. attribute:: local_priority
                
                	Local priority configuration is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_ethernet
                
                	Ethernet transport is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_ipv4
                
                	IPv6 transport is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_ipv6
                
                	IPv6 transport is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_unicast
                
                	Unicast is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_multicast
                
                	Multicast is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_mixed
                
                	Mixed\-mode multicast is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_master_unicast
                
                	Unicast master is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_master_multicast
                
                	Multicast master is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_master_mixed
                
                	Mixed\-mode multicast master is not compatible with profile
                	**type**\: bool
                
                .. attribute:: target_address_ipv4
                
                	Ethernet multicast target\-address is configured, but transport is IPv4
                	**type**\: bool
                
                .. attribute:: target_address_ipv6
                
                	Ethernet multicast target\-address is configured, but transport is IPv6
                	**type**\: bool
                
                .. attribute:: profile_port_state
                
                	Port state restriction is not compatible with telecom clock type
                	**type**\: bool
                
                .. attribute:: profile_announce_interval
                
                	Announce interval is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_sync_interval
                
                	Sync interval is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_delay_req_interval
                
                	Delay request interval is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_sync_timeout
                
                	Sync timeout configuration is not compatible with profile
                	**type**\: bool
                
                .. attribute:: profile_delay_resp_timeout
                
                	Delay response timeout configuration is not compatible with profile
                	**type**\: bool
                
                .. attribute:: invalid_grant_reduction
                
                	Reducing invalid unicast grants is not compatible with configured profile
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors, self).__init__()

                    self.yang_name = "configuration-errors"
                    self.yang_parent_name = "interface-configuration-error"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.global_ptp = YLeaf(YType.boolean, "global-ptp")

                    self.ethernet_transport = YLeaf(YType.boolean, "ethernet-transport")

                    self.one_step = YLeaf(YType.boolean, "one-step")

                    self.slave = YLeaf(YType.boolean, "slave")

                    self.ipv6 = YLeaf(YType.boolean, "ipv6")

                    self.multicast = YLeaf(YType.boolean, "multicast")

                    self.profile_not_global = YLeaf(YType.boolean, "profile-not-global")

                    self.local_priority = YLeaf(YType.boolean, "local-priority")

                    self.profile_ethernet = YLeaf(YType.boolean, "profile-ethernet")

                    self.profile_ipv4 = YLeaf(YType.boolean, "profile-ipv4")

                    self.profile_ipv6 = YLeaf(YType.boolean, "profile-ipv6")

                    self.profile_unicast = YLeaf(YType.boolean, "profile-unicast")

                    self.profile_multicast = YLeaf(YType.boolean, "profile-multicast")

                    self.profile_mixed = YLeaf(YType.boolean, "profile-mixed")

                    self.profile_master_unicast = YLeaf(YType.boolean, "profile-master-unicast")

                    self.profile_master_multicast = YLeaf(YType.boolean, "profile-master-multicast")

                    self.profile_master_mixed = YLeaf(YType.boolean, "profile-master-mixed")

                    self.target_address_ipv4 = YLeaf(YType.boolean, "target-address-ipv4")

                    self.target_address_ipv6 = YLeaf(YType.boolean, "target-address-ipv6")

                    self.profile_port_state = YLeaf(YType.boolean, "profile-port-state")

                    self.profile_announce_interval = YLeaf(YType.boolean, "profile-announce-interval")

                    self.profile_sync_interval = YLeaf(YType.boolean, "profile-sync-interval")

                    self.profile_delay_req_interval = YLeaf(YType.boolean, "profile-delay-req-interval")

                    self.profile_sync_timeout = YLeaf(YType.boolean, "profile-sync-timeout")

                    self.profile_delay_resp_timeout = YLeaf(YType.boolean, "profile-delay-resp-timeout")

                    self.invalid_grant_reduction = YLeaf(YType.boolean, "invalid-grant-reduction")
                    self._segment_path = lambda: "configuration-errors"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors, ['global_ptp', 'ethernet_transport', 'one_step', 'slave', 'ipv6', 'multicast', 'profile_not_global', 'local_priority', 'profile_ethernet', 'profile_ipv4', 'profile_ipv6', 'profile_unicast', 'profile_multicast', 'profile_mixed', 'profile_master_unicast', 'profile_master_multicast', 'profile_master_mixed', 'target_address_ipv4', 'target_address_ipv6', 'profile_port_state', 'profile_announce_interval', 'profile_sync_interval', 'profile_delay_req_interval', 'profile_sync_timeout', 'profile_delay_resp_timeout', 'invalid_grant_reduction'], name, value)


    class InterfaceForeignMasters(Entity):
        """
        Table for interface foreign master clock
        operational data
        
        .. attribute:: interface_foreign_master
        
        	Interface foreign master clock operational data
        	**type**\: list of  		 :py:class:`InterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.InterfaceForeignMasters, self).__init__()

            self.yang_name = "interface-foreign-masters"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-foreign-master" : ("interface_foreign_master", Ptp.InterfaceForeignMasters.InterfaceForeignMaster)}

            self.interface_foreign_master = YList(self)
            self._segment_path = lambda: "interface-foreign-masters"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceForeignMasters, [], name, value)


        class InterfaceForeignMaster(Entity):
            """
            Interface foreign master clock operational data
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: foreign_clock
            
            	Foreign clocks received on this interface
            	**type**\: list of  		 :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster, self).__init__()

                self.yang_name = "interface-foreign-master"
                self.yang_parent_name = "interface-foreign-masters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"foreign-clock" : ("foreign_clock", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.port_number = YLeaf(YType.uint16, "port-number")

                self.foreign_clock = YList(self)
                self._segment_path = lambda: "interface-foreign-master" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-foreign-masters/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster, ['interface_name', 'port_number'], name, value)


            class ForeignClock(Entity):
                """
                Foreign clocks received on this interface
                
                .. attribute:: foreign_clock
                
                	Foreign clock information
                	**type**\:  :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock>`
                
                .. attribute:: address
                
                	The address of the clock
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address>`
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant>`
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                
                .. attribute:: is_qualified
                
                	The clock is qualified for best master clock selection
                	**type**\: bool
                
                .. attribute:: is_grandmaster
                
                	This clock is the currently selected grand master clock
                	**type**\: bool
                
                .. attribute:: communication_model
                
                	The communication model configured on this clock
                	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                .. attribute:: is_known
                
                	This clock is known by this router
                	**type**\: bool
                
                .. attribute:: time_known_for
                
                	How long the clock has been known by this router for, in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: foreign_domain
                
                	The PTP domain that the foreign clock is in
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: configured_priority
                
                	Priority configured for the clock, if any
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: configured_clock_class
                
                	Clock class configured for the clock, if any
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: delay_asymmetry
                
                	Delay asymmetry configured for the clock, if any
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\: bool
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, self).__init__()

                    self.yang_name = "foreign-clock"
                    self.yang_parent_name = "interface-foreign-master"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"foreign-clock" : ("foreign_clock", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock), "address" : ("address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address), "announce-grant" : ("announce_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant), "sync-grant" : ("sync_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant), "delay-response-grant" : ("delay_response_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant)}
                    self._child_list_classes = {}

                    self.is_qualified = YLeaf(YType.boolean, "is-qualified")

                    self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                    self.communication_model = YLeaf(YType.enumeration, "communication-model")

                    self.is_known = YLeaf(YType.boolean, "is-known")

                    self.time_known_for = YLeaf(YType.uint32, "time-known-for")

                    self.foreign_domain = YLeaf(YType.uint8, "foreign-domain")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                    self.delay_asymmetry = YLeaf(YType.int32, "delay-asymmetry")

                    self.ptsf_loss_announce = YLeaf(YType.boolean, "ptsf-loss-announce")

                    self.ptsf_loss_sync = YLeaf(YType.boolean, "ptsf-loss-sync")

                    self.foreign_clock = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock()
                    self.foreign_clock.parent = self
                    self._children_name_map["foreign_clock"] = "foreign-clock"
                    self._children_yang_names.add("foreign-clock")

                    self.address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")

                    self.announce_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"
                    self._children_yang_names.add("announce-grant")

                    self.sync_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"
                    self._children_yang_names.add("sync-grant")

                    self.delay_response_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._children_yang_names.add("delay-response-grant")
                    self._segment_path = lambda: "foreign-clock"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, ['is_qualified', 'is_grandmaster', 'communication_model', 'is_known', 'time_known_for', 'foreign_domain', 'configured_priority', 'configured_clock_class', 'delay_asymmetry', 'ptsf_loss_announce', 'ptsf_loss_sync'], name, value)


                class ForeignClock(Entity):
                    """
                    Foreign clock information
                    
                    .. attribute:: utc_offset
                    
                    	UTC offset
                    	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset>`
                    
                    .. attribute:: receiver
                    
                    	Receiver
                    	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver>`
                    
                    .. attribute:: sender
                    
                    	Sender
                    	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender>`
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: priority1
                    
                    	Priority 1
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority2
                    
                    	Priority 2
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: class_
                    
                    	Class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: accuracy
                    
                    	Accuracy
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: offset_log_variance
                    
                    	Offset log variance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: steps_removed
                    
                    	Steps removed
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: time_source
                    
                    	Time source
                    	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                    
                    .. attribute:: frequency_traceable
                    
                    	The clock is frequency traceable
                    	**type**\: bool
                    
                    .. attribute:: time_traceable
                    
                    	The clock is time traceable
                    	**type**\: bool
                    
                    .. attribute:: timescale
                    
                    	Timescale
                    	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                    
                    .. attribute:: leap_seconds
                    
                    	Leap Seconds
                    	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                    
                    	**units**\: second
                    
                    .. attribute:: local
                    
                    	The clock is the local clock
                    	**type**\: bool
                    
                    .. attribute:: configured_clock_class
                    
                    	The configured clock class
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: configured_priority
                    
                    	The configured priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock, self).__init__()

                        self.yang_name = "foreign-clock"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"utc-offset" : ("utc_offset", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset), "receiver" : ("receiver", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver), "sender" : ("sender", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender)}
                        self._child_list_classes = {}

                        self.clock_id = YLeaf(YType.uint64, "clock-id")

                        self.priority1 = YLeaf(YType.uint8, "priority1")

                        self.priority2 = YLeaf(YType.uint8, "priority2")

                        self.class_ = YLeaf(YType.uint8, "class")

                        self.accuracy = YLeaf(YType.uint8, "accuracy")

                        self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                        self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                        self.time_source = YLeaf(YType.enumeration, "time-source")

                        self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                        self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                        self.timescale = YLeaf(YType.enumeration, "timescale")

                        self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                        self.local = YLeaf(YType.boolean, "local")

                        self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                        self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                        self.utc_offset = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset()
                        self.utc_offset.parent = self
                        self._children_name_map["utc_offset"] = "utc-offset"
                        self._children_yang_names.add("utc-offset")

                        self.receiver = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver()
                        self.receiver.parent = self
                        self._children_name_map["receiver"] = "receiver"
                        self._children_yang_names.add("receiver")

                        self.sender = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender()
                        self.sender.parent = self
                        self._children_name_map["sender"] = "sender"
                        self._children_yang_names.add("sender")
                        self._segment_path = lambda: "foreign-clock"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


                    class UtcOffset(Entity):
                        """
                        UTC offset
                        
                        .. attribute:: current_offset
                        
                        	Current offset
                        	**type**\: int
                        
                        	**range:** \-32768..32767
                        
                        .. attribute:: offset_valid
                        
                        	The current offset is valid
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset, self).__init__()

                            self.yang_name = "utc-offset"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.current_offset = YLeaf(YType.int16, "current-offset")

                            self.offset_valid = YLeaf(YType.boolean, "offset-valid")
                            self._segment_path = lambda: "utc-offset"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset, ['current_offset', 'offset_valid'], name, value)


                    class Receiver(Entity):
                        """
                        Receiver
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver, self).__init__()

                            self.yang_name = "receiver"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clock_id = YLeaf(YType.uint64, "clock-id")

                            self.port_number = YLeaf(YType.uint16, "port-number")
                            self._segment_path = lambda: "receiver"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver, ['clock_id', 'port_number'], name, value)


                    class Sender(Entity):
                        """
                        Sender
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender, self).__init__()

                            self.yang_name = "sender"
                            self.yang_parent_name = "foreign-clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clock_id = YLeaf(YType.uint64, "clock-id")

                            self.port_number = YLeaf(YType.uint16, "port-number")
                            self._segment_path = lambda: "sender"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender, ['clock_id', 'port_number'], name, value)


                class Address(Entity):
                    """
                    The address of the clock
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac-address" : ("mac_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address)}
                        self._child_list_classes = {}

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.ipv6_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "mac-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress, ['macaddr'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "ipv6-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address, ['ipv6_address'], name, value)


                class AnnounceGrant(Entity):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant, self).__init__()

                        self.yang_name = "announce-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "announce-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)


                class SyncGrant(Entity):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant, self).__init__()

                        self.yang_name = "sync-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "sync-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)


                class DelayResponseGrant(Entity):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant, self).__init__()

                        self.yang_name = "delay-response-grant"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "delay-response-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)


    class LocalClock(Entity):
        """
        Local clock operational data
        
        .. attribute:: clock_properties
        
        	Local clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties>`
        
        .. attribute:: domain
        
        	The PTP domain of the local clock
        	**type**\: int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.LocalClock, self).__init__()

            self.yang_name = "local-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"clock-properties" : ("clock_properties", Ptp.LocalClock.ClockProperties)}
            self._child_list_classes = {}

            self.domain = YLeaf(YType.uint8, "domain")

            self.clock_properties = Ptp.LocalClock.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._children_yang_names.add("clock-properties")
            self._segment_path = lambda: "local-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.LocalClock, ['domain'], name, value)


        class ClockProperties(Entity):
            """
            Local clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.UtcOffset>`
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Sender>`
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.LocalClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "local-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"utc-offset" : ("utc_offset", Ptp.LocalClock.ClockProperties.UtcOffset), "receiver" : ("receiver", Ptp.LocalClock.ClockProperties.Receiver), "sender" : ("sender", Ptp.LocalClock.ClockProperties.Sender)}
                self._child_list_classes = {}

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.class_ = YLeaf(YType.uint8, "class")

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.utc_offset = Ptp.LocalClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")

                self.receiver = Ptp.LocalClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.LocalClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LocalClock.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.LocalClock.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.current_offset = YLeaf(YType.int16, "current-offset")

                    self.offset_valid = YLeaf(YType.boolean, "offset-valid")
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.LocalClock.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)


            class Sender(Entity):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.LocalClock.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.LocalClock.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)


    class InterfacePacketCounters(Entity):
        """
        Table for interface packet counter operational
        data
        
        .. attribute:: interface_packet_counter
        
        	Interface packet counter operational data
        	**type**\: list of  		 :py:class:`InterfacePacketCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.InterfacePacketCounters, self).__init__()

            self.yang_name = "interface-packet-counters"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-packet-counter" : ("interface_packet_counter", Ptp.InterfacePacketCounters.InterfacePacketCounter)}

            self.interface_packet_counter = YList(self)
            self._segment_path = lambda: "interface-packet-counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfacePacketCounters, [], name, value)


        class InterfacePacketCounter(Entity):
            """
            Interface packet counter operational data
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: counters
            
            	Packet counters
            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters>`
            
            .. attribute:: peer_counter
            
            	Packet counters for each peer on this interface
            	**type**\: list of  		 :py:class:`PeerCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.InterfacePacketCounters.InterfacePacketCounter, self).__init__()

                self.yang_name = "interface-packet-counter"
                self.yang_parent_name = "interface-packet-counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"counters" : ("counters", Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters)}
                self._child_list_classes = {"peer-counter" : ("peer_counter", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.counters = Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"
                self._children_yang_names.add("counters")

                self.peer_counter = YList(self)
                self._segment_path = lambda: "interface-packet-counter" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-packet-counters/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter, ['interface_name'], name, value)


            class Counters(Entity):
                """
                Packet counters
                
                .. attribute:: announce_sent
                
                	Number of announce packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: announce_received
                
                	Number of announce packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: announce_dropped
                
                	Number of announce packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_sent
                
                	Number of sync packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_received
                
                	Number of sync packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_dropped
                
                	Number of sync packetsdropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_sent
                
                	Number of follow\-up packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_received
                
                	Number of follow\-up packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_dropped
                
                	Number of follow\-up packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_sent
                
                	Number of delay\-request packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_received
                
                	Number of delay\-request packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_dropped
                
                	Number of delay\-request packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_sent
                
                	Number of delay\-response packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_received
                
                	Number of delay\-response packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_dropped
                
                	Number of delay\-response packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_sent
                
                	Number of peer\-delay\-request packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_received
                
                	Number of peer\-delay\-request packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_dropped
                
                	Number of peer\-delay\-request packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_sent
                
                	Number of peer\-delay\-response packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_received
                
                	Number of peer\-delay\-response packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_dropped
                
                	Number of peer\-delay\-response packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_sent
                
                	Number of peer\-delay\-response follow\-up packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_received
                
                	Number of peer\-delay\-response follow\-up packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_dropped
                
                	Number of peer\-delay\-response follow\-up packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_sent
                
                	Number of signaling packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_received
                
                	Number of signaling packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_dropped
                
                	Number of signaling packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_sent
                
                	Number of management messages sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_received
                
                	Number of management messages received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_dropped
                
                	Number of management messages dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_sent
                
                	Number of other packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_received
                
                	Number of other packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_dropped
                
                	Number of other packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_sent
                
                	Total number of packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_received
                
                	Total number of packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_dropped
                
                	Total number of packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "interface-packet-counter"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                    self.announce_received = YLeaf(YType.uint32, "announce-received")

                    self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                    self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                    self.sync_received = YLeaf(YType.uint32, "sync-received")

                    self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                    self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                    self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                    self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                    self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                    self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                    self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                    self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                    self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                    self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                    self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                    self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                    self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                    self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                    self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                    self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                    self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                    self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                    self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                    self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                    self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                    self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                    self.management_sent = YLeaf(YType.uint32, "management-sent")

                    self.management_received = YLeaf(YType.uint32, "management-received")

                    self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                    self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                    self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                    self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                    self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")

                    self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                    self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")
                    self._segment_path = lambda: "counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)


            class PeerCounter(Entity):
                """
                Packet counters for each peer on this interface
                
                .. attribute:: address
                
                	Peer address
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address>`
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter, self).__init__()

                    self.yang_name = "peer-counter"
                    self.yang_parent_name = "interface-packet-counter"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"address" : ("address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address), "counters" : ("counters", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters)}
                    self._child_list_classes = {}

                    self.address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")

                    self.counters = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"
                    self._children_yang_names.add("counters")
                    self._segment_path = lambda: "peer-counter"


                class Address(Entity):
                    """
                    Peer address
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress>`
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peer-counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac-address" : ("mac_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address)}
                        self._child_list_classes = {}

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.ipv6_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "mac-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress, ['macaddr'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "ipv6-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address, ['ipv6_address'], name, value)


                class Counters(Entity):
                    """
                    Packet counters
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "peer-counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                        self.announce_received = YLeaf(YType.uint32, "announce-received")

                        self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                        self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                        self.sync_received = YLeaf(YType.uint32, "sync-received")

                        self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                        self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                        self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                        self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                        self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                        self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                        self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                        self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                        self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                        self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                        self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                        self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                        self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                        self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                        self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                        self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                        self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                        self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                        self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                        self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                        self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                        self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                        self.management_sent = YLeaf(YType.uint32, "management-sent")

                        self.management_received = YLeaf(YType.uint32, "management-received")

                        self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                        self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                        self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                        self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                        self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")

                        self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                        self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters, ['announce_sent', 'announce_received', 'announce_dropped', 'sync_sent', 'sync_received', 'sync_dropped', 'follow_up_sent', 'follow_up_received', 'follow_up_dropped', 'delay_request_sent', 'delay_request_received', 'delay_request_dropped', 'delay_response_sent', 'delay_response_received', 'delay_response_dropped', 'peer_delay_request_sent', 'peer_delay_request_received', 'peer_delay_request_dropped', 'peer_delay_response_sent', 'peer_delay_response_received', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_sent', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_dropped', 'signaling_sent', 'signaling_received', 'signaling_dropped', 'management_sent', 'management_received', 'management_dropped', 'other_packets_sent', 'other_packets_received', 'other_packets_dropped', 'total_packets_sent', 'total_packets_received', 'total_packets_dropped'], name, value)


    class AdvertisedClock(Entity):
        """
        Advertised clock operational data
        
        .. attribute:: clock_properties
        
        	Advertised Clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties>`
        
        .. attribute:: domain
        
        	The PTP domain of that the advertised clock is in
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: time_source_configured
        
        	Whether the advertised time source is configured
        	**type**\: bool
        
        .. attribute:: received_time_source
        
        	The time source received from the parent clock
        	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
        
        .. attribute:: timescale_configured
        
        	Whether the advertised timescale is configured
        	**type**\: bool
        
        .. attribute:: received_timescale
        
        	The timescale received from the parent clock
        	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.AdvertisedClock, self).__init__()

            self.yang_name = "advertised-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"clock-properties" : ("clock_properties", Ptp.AdvertisedClock.ClockProperties)}
            self._child_list_classes = {}

            self.domain = YLeaf(YType.uint8, "domain")

            self.time_source_configured = YLeaf(YType.boolean, "time-source-configured")

            self.received_time_source = YLeaf(YType.enumeration, "received-time-source")

            self.timescale_configured = YLeaf(YType.boolean, "timescale-configured")

            self.received_timescale = YLeaf(YType.enumeration, "received-timescale")

            self.clock_properties = Ptp.AdvertisedClock.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._children_yang_names.add("clock-properties")
            self._segment_path = lambda: "advertised-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.AdvertisedClock, ['domain', 'time_source_configured', 'received_time_source', 'timescale_configured', 'received_timescale'], name, value)


        class ClockProperties(Entity):
            """
            Advertised Clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.UtcOffset>`
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Sender>`
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.AdvertisedClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "advertised-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"utc-offset" : ("utc_offset", Ptp.AdvertisedClock.ClockProperties.UtcOffset), "receiver" : ("receiver", Ptp.AdvertisedClock.ClockProperties.Receiver), "sender" : ("sender", Ptp.AdvertisedClock.ClockProperties.Sender)}
                self._child_list_classes = {}

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.class_ = YLeaf(YType.uint8, "class")

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.utc_offset = Ptp.AdvertisedClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")

                self.receiver = Ptp.AdvertisedClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.AdvertisedClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.AdvertisedClock.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.AdvertisedClock.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.current_offset = YLeaf(YType.int16, "current-offset")

                    self.offset_valid = YLeaf(YType.boolean, "offset-valid")
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.AdvertisedClock.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)


            class Sender(Entity):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.AdvertisedClock.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.AdvertisedClock.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)


    class LeapSeconds(Entity):
        """
        Upcoming leap\-seconds information
        
        .. attribute:: current_offset
        
        	The current UTC offset, in seconds
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**units**\: second
        
        .. attribute:: offset_valid
        
        	Is the current UTC offset known to be valid?
        	**type**\: bool
        
        .. attribute:: source_file
        
        	The URL of the file containing upcoming leap seconds
        	**type**\: str
        
        	**units**\: second
        
        .. attribute:: source_expiry_date
        
        	Source file expiry timestamp, in seconds since UNIX epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: polling_frequency
        
        	Source file polling frequency, in days
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: day
        
        .. attribute:: leap_second
        
        	The list of upcoming leap second updates
        	**type**\: list of  		 :py:class:`LeapSecond <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LeapSeconds.LeapSecond>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.LeapSeconds, self).__init__()

            self.yang_name = "leap-seconds"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"leap-second" : ("leap_second", Ptp.LeapSeconds.LeapSecond)}

            self.current_offset = YLeaf(YType.int16, "current-offset")

            self.offset_valid = YLeaf(YType.boolean, "offset-valid")

            self.source_file = YLeaf(YType.str, "source-file")

            self.source_expiry_date = YLeaf(YType.uint32, "source-expiry-date")

            self.polling_frequency = YLeaf(YType.uint32, "polling-frequency")

            self.leap_second = YList(self)
            self._segment_path = lambda: "leap-seconds"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.LeapSeconds, ['current_offset', 'offset_valid', 'source_file', 'source_expiry_date', 'polling_frequency'], name, value)


        class LeapSecond(Entity):
            """
            The list of upcoming leap second updates
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**units**\: second
            
            .. attribute:: offset_start_date
            
            	The UNIX timestamp at which the offset becomes valid
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: offset_applied
            
            	Indicates whether the offset has been applied
            	**type**\: bool
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.LeapSeconds.LeapSecond, self).__init__()

                self.yang_name = "leap-second"
                self.yang_parent_name = "leap-seconds"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.offset = YLeaf(YType.int16, "offset")

                self.offset_start_date = YLeaf(YType.uint64, "offset-start-date")

                self.offset_applied = YLeaf(YType.boolean, "offset-applied")
                self._segment_path = lambda: "leap-second"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/leap-seconds/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LeapSeconds.LeapSecond, ['offset', 'offset_start_date', 'offset_applied'], name, value)


    class Interfaces(Entity):
        """
        Table for interface operational data
        
        .. attribute:: interface
        
        	Interface operational data
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Ptp.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface operational data
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: mac_address
            
            	MAC address, if Ethernet encapsulation is being used
            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MacAddress>`
            
            .. attribute:: port_state
            
            	Port state
            	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: line_state
            
            	Line state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            .. attribute:: ipv6_address
            
            	Ipv6 address, if IPv6 encapsulation is being used
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv4_address
            
            	IPv4 address, if IPv4 encapsulation is being used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: two_step
            
            	Two step delay\-request mechanism is being used
            	**type**\: bool
            
            .. attribute:: communication_model
            
            	Communication model configured on the interface
            	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
            
            .. attribute:: log_sync_interval
            
            	Log of the interface's sync interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: log_announce_interval
            
            	Log of the interface's announce interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: announce_timeout
            
            	Announce timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: log_min_delay_request_interval
            
            	Log of the interface's Minimum delay\-request interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: configured_port_state
            
            	The configured port state
            	**type**\:  :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            .. attribute:: supports_one_step
            
            	The interface supports one\-step operation
            	**type**\: bool
            
            .. attribute:: supports_two_step
            
            	The interface supports two\-step operation
            	**type**\: bool
            
            .. attribute:: supports_ethernet
            
            	The interface supports ethernet transport
            	**type**\: bool
            
            .. attribute:: supports_multicast
            
            	The interface supports multicast
            	**type**\: bool
            
            .. attribute:: supports_ipv6
            
            	The interface supports IPv6 transport
            	**type**\: bool
            
            .. attribute:: supports_slave
            
            	The interface supports operation in slave mode
            	**type**\: bool
            
            .. attribute:: supports_source_ip
            
            	The interface supports source ip configuration
            	**type**\: bool
            
            .. attribute:: max_sync_rate
            
            	The maximum rate of sync packets on the interface
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: event_cos
            
            	The class of service used on the interface for event messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: general_cos
            
            	The class of service used on the interface for general messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: event_dscp
            
            	The DSCP class used on the interface for event messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: general_dscp
            
            	The DSCP class used on the interface for general messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: unicast_peers
            
            	The number of unicast peers known by the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_priority
            
            	Local priority, for the G.8275.1 PTP profile
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: signal_fail
            
            	Signal fail status of the interface
            	**type**\: bool
            
            .. attribute:: master_table
            
            	The interface's master table
            	**type**\: list of  		 :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Interfaces.Interface.MacAddress)}
                self._child_list_classes = {"master-table" : ("master_table", Ptp.Interfaces.Interface.MasterTable)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.port_state = YLeaf(YType.enumeration, "port-state")

                self.port_number = YLeaf(YType.uint16, "port-number")

                self.line_state = YLeaf(YType.uint32, "line-state")

                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                self.two_step = YLeaf(YType.boolean, "two-step")

                self.communication_model = YLeaf(YType.enumeration, "communication-model")

                self.log_sync_interval = YLeaf(YType.int32, "log-sync-interval")

                self.log_announce_interval = YLeaf(YType.int32, "log-announce-interval")

                self.announce_timeout = YLeaf(YType.uint32, "announce-timeout")

                self.log_min_delay_request_interval = YLeaf(YType.int32, "log-min-delay-request-interval")

                self.configured_port_state = YLeaf(YType.enumeration, "configured-port-state")

                self.supports_one_step = YLeaf(YType.boolean, "supports-one-step")

                self.supports_two_step = YLeaf(YType.boolean, "supports-two-step")

                self.supports_ethernet = YLeaf(YType.boolean, "supports-ethernet")

                self.supports_multicast = YLeaf(YType.boolean, "supports-multicast")

                self.supports_ipv6 = YLeaf(YType.boolean, "supports-ipv6")

                self.supports_slave = YLeaf(YType.boolean, "supports-slave")

                self.supports_source_ip = YLeaf(YType.boolean, "supports-source-ip")

                self.max_sync_rate = YLeaf(YType.uint8, "max-sync-rate")

                self.event_cos = YLeaf(YType.uint32, "event-cos")

                self.general_cos = YLeaf(YType.uint32, "general-cos")

                self.event_dscp = YLeaf(YType.uint32, "event-dscp")

                self.general_dscp = YLeaf(YType.uint32, "general-dscp")

                self.unicast_peers = YLeaf(YType.uint32, "unicast-peers")

                self.local_priority = YLeaf(YType.uint8, "local-priority")

                self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                self.mac_address = Ptp.Interfaces.Interface.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"
                self._children_yang_names.add("mac-address")

                self.master_table = YList(self)
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Interfaces.Interface, ['interface_name', 'port_state', 'port_number', 'line_state', 'encapsulation', 'ipv6_address', 'ipv4_address', 'two_step', 'communication_model', 'log_sync_interval', 'log_announce_interval', 'announce_timeout', 'log_min_delay_request_interval', 'configured_port_state', 'supports_one_step', 'supports_two_step', 'supports_ethernet', 'supports_multicast', 'supports_ipv6', 'supports_slave', 'supports_source_ip', 'max_sync_rate', 'event_cos', 'general_cos', 'event_dscp', 'general_dscp', 'unicast_peers', 'local_priority', 'signal_fail'], name, value)


            class MacAddress(Entity):
                """
                MAC address, if Ethernet encapsulation is being
                used
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Interfaces.Interface.MacAddress, self).__init__()

                    self.yang_name = "mac-address"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.macaddr = YLeaf(YType.str, "macaddr")
                    self._segment_path = lambda: "mac-address"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.MacAddress, ['macaddr'], name, value)


            class MasterTable(Entity):
                """
                The interface's master table
                
                .. attribute:: address
                
                	The address of the master clock
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address>`
                
                .. attribute:: communication_model
                
                	The configured communication model of the master clock
                	**type**\:  :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                .. attribute:: priority
                
                	The priority of the master clock, if it is set
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: known
                
                	Whether the interface is receiving messages from this master
                	**type**\: bool
                
                .. attribute:: qualified
                
                	The master is qualified for best master clock selection
                	**type**\: bool
                
                .. attribute:: is_grandmaster
                
                	Whether this is the grandmaster
                	**type**\: bool
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_nonnegotiated
                
                	Whether this master uses non\-negotiated unicast
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Interfaces.Interface.MasterTable, self).__init__()

                    self.yang_name = "master-table"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"address" : ("address", Ptp.Interfaces.Interface.MasterTable.Address)}
                    self._child_list_classes = {}

                    self.communication_model = YLeaf(YType.enumeration, "communication-model")

                    self.priority = YLeaf(YType.uint8, "priority")

                    self.known = YLeaf(YType.boolean, "known")

                    self.qualified = YLeaf(YType.boolean, "qualified")

                    self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                    self.ptsf_loss_announce = YLeaf(YType.uint8, "ptsf-loss-announce")

                    self.ptsf_loss_sync = YLeaf(YType.uint8, "ptsf-loss-sync")

                    self.is_nonnegotiated = YLeaf(YType.boolean, "is-nonnegotiated")

                    self.address = Ptp.Interfaces.Interface.MasterTable.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")
                    self._segment_path = lambda: "master-table"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.MasterTable, ['communication_model', 'priority', 'known', 'qualified', 'is_grandmaster', 'ptsf_loss_announce', 'ptsf_loss_sync', 'is_nonnegotiated'], name, value)


                class Address(Entity):
                    """
                    The address of the master clock
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.MacAddress>`
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Interfaces.Interface.MasterTable.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "master-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Interfaces.Interface.MasterTable.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address)}
                        self._child_list_classes = {}

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = Ptp.Interfaces.Interface.MasterTable.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.ipv6_address = Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Interfaces.Interface.MasterTable.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "mac-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address.MacAddress, ['macaddr'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "ipv6-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address, ['ipv6_address'], name, value)


    class Dataset(Entity):
        """
        Global PTP datasets
        
        .. attribute:: default_ds
        
        	defaultDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`DefaultDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.DefaultDs>`
        
        .. attribute:: current_ds
        
        	currentDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`CurrentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.CurrentDs>`
        
        .. attribute:: parent_ds
        
        	parentDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`ParentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.ParentDs>`
        
        .. attribute:: port_dses
        
        	Table for portDS information
        	**type**\:  :py:class:`PortDses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses>`
        
        .. attribute:: time_properties_ds
        
        	timePropertiesDS information as described in IEEE 1588\-2008
        	**type**\:  :py:class:`TimePropertiesDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.TimePropertiesDs>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Dataset, self).__init__()

            self.yang_name = "dataset"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"default-ds" : ("default_ds", Ptp.Dataset.DefaultDs), "current-ds" : ("current_ds", Ptp.Dataset.CurrentDs), "parent-ds" : ("parent_ds", Ptp.Dataset.ParentDs), "port-dses" : ("port_dses", Ptp.Dataset.PortDses), "time-properties-ds" : ("time_properties_ds", Ptp.Dataset.TimePropertiesDs)}
            self._child_list_classes = {}

            self.default_ds = Ptp.Dataset.DefaultDs()
            self.default_ds.parent = self
            self._children_name_map["default_ds"] = "default-ds"
            self._children_yang_names.add("default-ds")

            self.current_ds = Ptp.Dataset.CurrentDs()
            self.current_ds.parent = self
            self._children_name_map["current_ds"] = "current-ds"
            self._children_yang_names.add("current-ds")

            self.parent_ds = Ptp.Dataset.ParentDs()
            self.parent_ds.parent = self
            self._children_name_map["parent_ds"] = "parent-ds"
            self._children_yang_names.add("parent-ds")

            self.port_dses = Ptp.Dataset.PortDses()
            self.port_dses.parent = self
            self._children_name_map["port_dses"] = "port-dses"
            self._children_yang_names.add("port-dses")

            self.time_properties_ds = Ptp.Dataset.TimePropertiesDs()
            self.time_properties_ds.parent = self
            self._children_name_map["time_properties_ds"] = "time-properties-ds"
            self._children_yang_names.add("time-properties-ds")
            self._segment_path = lambda: "dataset"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()


        class DefaultDs(Entity):
            """
            defaultDS information as described in IEEE
            1588\-2008
            
            .. attribute:: two_step_flag
            
            	Is the twoStepFlag set for this clock
            	**type**\: bool
            
            .. attribute:: clock_id
            
            	The local\-clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_ports
            
            	The number of active PTP ports on this clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: clock_class
            
            	The clock class of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: clock_accuracy
            
            	The accuracy of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: oslv
            
            	The offset scaled log variance of the local\-clock
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: priority1
            
            	The priority1 of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	The priority2 of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: domain_number
            
            	The domain of the local\-clock
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: slave_only
            
            	Whether the local\-clock is globally configured as slave\-only
            	**type**\: bool
            
            .. attribute:: local_priority
            
            	Local priority of the local clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: signal_fail
            
            	Signal fail status of the local clock
            	**type**\: bool
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Dataset.DefaultDs, self).__init__()

                self.yang_name = "default-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.two_step_flag = YLeaf(YType.boolean, "two-step-flag")

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.number_ports = YLeaf(YType.uint32, "number-ports")

                self.clock_class = YLeaf(YType.uint8, "clock-class")

                self.clock_accuracy = YLeaf(YType.uint8, "clock-accuracy")

                self.oslv = YLeaf(YType.uint16, "oslv")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.domain_number = YLeaf(YType.uint8, "domain-number")

                self.slave_only = YLeaf(YType.boolean, "slave-only")

                self.local_priority = YLeaf(YType.uint32, "local-priority")

                self.signal_fail = YLeaf(YType.boolean, "signal-fail")
                self._segment_path = lambda: "default-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.DefaultDs, ['two_step_flag', 'clock_id', 'number_ports', 'clock_class', 'clock_accuracy', 'oslv', 'priority1', 'priority2', 'domain_number', 'slave_only', 'local_priority', 'signal_fail'], name, value)


        class CurrentDs(Entity):
            """
            currentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: steps_removed
            
            	How many steps removed this clock is from the GM
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: offset_from_master
            
            	The UTC offset of the local\-clock from the GM
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: mean_path_delay
            
            	The mean path delay bewteen the foreign\-master and the local\-clock
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Dataset.CurrentDs, self).__init__()

                self.yang_name = "current-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.offset_from_master = YLeaf(YType.int64, "offset-from-master")

                self.mean_path_delay = YLeaf(YType.int64, "mean-path-delay")
                self._segment_path = lambda: "current-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.CurrentDs, ['steps_removed', 'offset_from_master', 'mean_path_delay'], name, value)


        class ParentDs(Entity):
            """
            parentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: parent_clock_id
            
            	The Clock ID of the parent clock
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: parent_port_number
            
            	The port number on which the parent clock is received
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: parent_stats
            
            	Whether the parentStats is valid
            	**type**\: bool
            
            .. attribute:: observed_parent_oslv
            
            	The observed parent offset scaled log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: observed_parent_clock_phase_change_rate
            
            	The observed rate of change of phase of the parent clock
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: gm_clock_id
            
            	The Clock ID of the GM
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: gm_clock_class
            
            	The clock class of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: gm_clock_accuracy
            
            	The clock accuracy of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: gmoslv
            
            	The offset scaled log variance of the GM
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: gm_priority1
            
            	The priority1 of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: gm_priority2
            
            	The priority2 of the GM
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Dataset.ParentDs, self).__init__()

                self.yang_name = "parent-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.parent_clock_id = YLeaf(YType.uint64, "parent-clock-id")

                self.parent_port_number = YLeaf(YType.uint16, "parent-port-number")

                self.parent_stats = YLeaf(YType.boolean, "parent-stats")

                self.observed_parent_oslv = YLeaf(YType.uint16, "observed-parent-oslv")

                self.observed_parent_clock_phase_change_rate = YLeaf(YType.uint32, "observed-parent-clock-phase-change-rate")

                self.gm_clock_id = YLeaf(YType.uint64, "gm-clock-id")

                self.gm_clock_class = YLeaf(YType.uint8, "gm-clock-class")

                self.gm_clock_accuracy = YLeaf(YType.uint8, "gm-clock-accuracy")

                self.gmoslv = YLeaf(YType.uint16, "gmoslv")

                self.gm_priority1 = YLeaf(YType.uint8, "gm-priority1")

                self.gm_priority2 = YLeaf(YType.uint8, "gm-priority2")
                self._segment_path = lambda: "parent-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.ParentDs, ['parent_clock_id', 'parent_port_number', 'parent_stats', 'observed_parent_oslv', 'observed_parent_clock_phase_change_rate', 'gm_clock_id', 'gm_clock_class', 'gm_clock_accuracy', 'gmoslv', 'gm_priority1', 'gm_priority2'], name, value)


        class PortDses(Entity):
            """
            Table for portDS information
            
            .. attribute:: port_ds
            
            	PortDS information
            	**type**\: list of  		 :py:class:`PortDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses.PortDs>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Dataset.PortDses, self).__init__()

                self.yang_name = "port-dses"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"port-ds" : ("port_ds", Ptp.Dataset.PortDses.PortDs)}

                self.port_ds = YList(self)
                self._segment_path = lambda: "port-dses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.PortDses, [], name, value)


            class PortDs(Entity):
                """
                PortDS information
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: clock_id
                
                	The ID of the local\-clock
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	The port number
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: port_state
                
                	The port state
                	**type**\:  :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                
                .. attribute:: log_min_delay_req_interval
                
                	The log (base 2) of the minimum delay\-request interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: peer_mean_path_delay
                
                	The mean path delay between peers
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: log_announce_interval
                
                	The log (base 2) of the announce interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: annoucne_receipt_timeout
                
                	The announce timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: log_sync_interval
                
                	The log (base 2) of the sync interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: delay_mechanism
                
                	The delay mechanism being used on this port
                	**type**\:  :py:class:`PtpBagDelayMechanism <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagDelayMechanism>`
                
                .. attribute:: log_min_p_delay_req_interval
                
                	The log (base 2) of the minimum peer\-delay\-request interval
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: version_number
                
                	The version of IEEE 1588 being run
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: local_priority
                
                	Local priority of the local clock
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: master_only
                
                	Is the port master\-only?
                	**type**\: bool
                
                .. attribute:: signal_fail
                
                	Signal fail status of the port
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Dataset.PortDses.PortDs, self).__init__()

                    self.yang_name = "port-ds"
                    self.yang_parent_name = "port-dses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")

                    self.port_state = YLeaf(YType.enumeration, "port-state")

                    self.log_min_delay_req_interval = YLeaf(YType.int16, "log-min-delay-req-interval")

                    self.peer_mean_path_delay = YLeaf(YType.int64, "peer-mean-path-delay")

                    self.log_announce_interval = YLeaf(YType.int16, "log-announce-interval")

                    self.annoucne_receipt_timeout = YLeaf(YType.uint32, "annoucne-receipt-timeout")

                    self.log_sync_interval = YLeaf(YType.int16, "log-sync-interval")

                    self.delay_mechanism = YLeaf(YType.enumeration, "delay-mechanism")

                    self.log_min_p_delay_req_interval = YLeaf(YType.int16, "log-min-p-delay-req-interval")

                    self.version_number = YLeaf(YType.uint8, "version-number")

                    self.local_priority = YLeaf(YType.uint32, "local-priority")

                    self.master_only = YLeaf(YType.boolean, "master-only")

                    self.signal_fail = YLeaf(YType.boolean, "signal-fail")
                    self._segment_path = lambda: "port-ds" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/port-dses/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Dataset.PortDses.PortDs, ['interface_name', 'clock_id', 'port_number', 'port_state', 'log_min_delay_req_interval', 'peer_mean_path_delay', 'log_announce_interval', 'annoucne_receipt_timeout', 'log_sync_interval', 'delay_mechanism', 'log_min_p_delay_req_interval', 'version_number', 'local_priority', 'master_only', 'signal_fail'], name, value)


        class TimePropertiesDs(Entity):
            """
            timePropertiesDS information as described in
            IEEE 1588\-2008
            
            .. attribute:: current_utc_offset
            
            	The current UTC offset
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: current_utc_offset_valid
            
            	Whether the current UTC offset is valid
            	**type**\: bool
            
            .. attribute:: leap59
            
            	Whether the last minute of the day has 59 seconds
            	**type**\: bool
            
            .. attribute:: leap61
            
            	Whether the last minute of the day has 61 seconds
            	**type**\: bool
            
            .. attribute:: time_traceable
            
            	Whether the time\-of\-day source is traceable
            	**type**\: bool
            
            .. attribute:: frequency_traceable
            
            	Whther the frequency source is traceable
            	**type**\: bool
            
            .. attribute:: ptp_timescale
            
            	Whether the timescale being used is the PTP timescale
            	**type**\: bool
            
            .. attribute:: time_source
            
            	The physical time\-source of the GM clock
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Dataset.TimePropertiesDs, self).__init__()

                self.yang_name = "time-properties-ds"
                self.yang_parent_name = "dataset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.current_utc_offset = YLeaf(YType.int16, "current-utc-offset")

                self.current_utc_offset_valid = YLeaf(YType.boolean, "current-utc-offset-valid")

                self.leap59 = YLeaf(YType.boolean, "leap59")

                self.leap61 = YLeaf(YType.boolean, "leap61")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.ptp_timescale = YLeaf(YType.boolean, "ptp-timescale")

                self.time_source = YLeaf(YType.enumeration, "time-source")
                self._segment_path = lambda: "time-properties-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.TimePropertiesDs, ['current_utc_offset', 'current_utc_offset_valid', 'leap59', 'leap61', 'time_traceable', 'frequency_traceable', 'ptp_timescale', 'time_source'], name, value)


    class GlobalConfigurationError(Entity):
        """
        Global configuration error operational data
        
        .. attribute:: configuration_errors
        
        	Configuration Errors
        	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError.ConfigurationErrors>`
        
        .. attribute:: clock_profile
        
        	The clock profile
        	**type**\:  :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
        
        .. attribute:: clock_profile_set
        
        	Is the clock profile set
        	**type**\: bool
        
        .. attribute:: telecom_clock_type
        
        	Configured telecom clock type
        	**type**\:  :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
        
        .. attribute:: domain_number
        
        	The PTP domain
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: priority2
        
        	The configured priority2 value
        	**type**\: int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.GlobalConfigurationError, self).__init__()

            self.yang_name = "global-configuration-error"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"configuration-errors" : ("configuration_errors", Ptp.GlobalConfigurationError.ConfigurationErrors)}
            self._child_list_classes = {}

            self.clock_profile = YLeaf(YType.enumeration, "clock-profile")

            self.clock_profile_set = YLeaf(YType.boolean, "clock-profile-set")

            self.telecom_clock_type = YLeaf(YType.enumeration, "telecom-clock-type")

            self.domain_number = YLeaf(YType.uint8, "domain-number")

            self.priority2 = YLeaf(YType.uint8, "priority2")

            self.configuration_errors = Ptp.GlobalConfigurationError.ConfigurationErrors()
            self.configuration_errors.parent = self
            self._children_name_map["configuration_errors"] = "configuration-errors"
            self._children_yang_names.add("configuration-errors")
            self._segment_path = lambda: "global-configuration-error"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.GlobalConfigurationError, ['clock_profile', 'clock_profile_set', 'telecom_clock_type', 'domain_number', 'priority2'], name, value)


        class ConfigurationErrors(Entity):
            """
            Configuration Errors
            
            .. attribute:: domain
            
            	Domain not compatible with configured profile
            	**type**\: bool
            
            .. attribute:: profile_priority1_config
            
            	Priority1 configuration is not compatible with configured profile
            	**type**\: bool
            
            .. attribute:: profile_priority2_value
            
            	Priority2 value is not compatible with configured profile
            	**type**\: bool
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.GlobalConfigurationError.ConfigurationErrors, self).__init__()

                self.yang_name = "configuration-errors"
                self.yang_parent_name = "global-configuration-error"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.domain = YLeaf(YType.boolean, "domain")

                self.profile_priority1_config = YLeaf(YType.boolean, "profile-priority1-config")

                self.profile_priority2_value = YLeaf(YType.boolean, "profile-priority2-value")
                self._segment_path = lambda: "configuration-errors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/global-configuration-error/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.GlobalConfigurationError.ConfigurationErrors, ['domain', 'profile_priority1_config', 'profile_priority2_value'], name, value)


    class Grandmaster(Entity):
        """
        Grandmaster clock operational data
        
        .. attribute:: clock_properties
        
        	Grandmaster clock
        	**type**\:  :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties>`
        
        .. attribute:: address
        
        	The grandmaster's address information
        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address>`
        
        .. attribute:: used_for_time
        
        	Whether the grandmaster is setting time\-of\-day on the system
        	**type**\: bool
        
        .. attribute:: used_for_frequency
        
        	Whether the grandmaster is setting frequency on the system
        	**type**\: bool
        
        .. attribute:: known_for_time
        
        	How long the clock has been grandmaster for, in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: domain
        
        	The PTP domain that the grandmaster is in
        	**type**\: int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Grandmaster, self).__init__()

            self.yang_name = "grandmaster"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"clock-properties" : ("clock_properties", Ptp.Grandmaster.ClockProperties), "address" : ("address", Ptp.Grandmaster.Address)}
            self._child_list_classes = {}

            self.used_for_time = YLeaf(YType.boolean, "used-for-time")

            self.used_for_frequency = YLeaf(YType.boolean, "used-for-frequency")

            self.known_for_time = YLeaf(YType.uint32, "known-for-time")

            self.domain = YLeaf(YType.uint8, "domain")

            self.clock_properties = Ptp.Grandmaster.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._children_yang_names.add("clock-properties")

            self.address = Ptp.Grandmaster.Address()
            self.address.parent = self
            self._children_name_map["address"] = "address"
            self._children_yang_names.add("address")
            self._segment_path = lambda: "grandmaster"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Grandmaster, ['used_for_time', 'used_for_frequency', 'known_for_time', 'domain'], name, value)


        class ClockProperties(Entity):
            """
            Grandmaster clock
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.UtcOffset>`
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:  :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:  :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Sender>`
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:  :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\: bool
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\: bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:  :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:  :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\: bool
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Grandmaster.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"utc-offset" : ("utc_offset", Ptp.Grandmaster.ClockProperties.UtcOffset), "receiver" : ("receiver", Ptp.Grandmaster.ClockProperties.Receiver), "sender" : ("sender", Ptp.Grandmaster.ClockProperties.Sender)}
                self._child_list_classes = {}

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.class_ = YLeaf(YType.uint8, "class")

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.utc_offset = Ptp.Grandmaster.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")

                self.receiver = Ptp.Grandmaster.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.Grandmaster.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.ClockProperties, ['clock_id', 'priority1', 'priority2', 'class_', 'accuracy', 'offset_log_variance', 'steps_removed', 'time_source', 'frequency_traceable', 'time_traceable', 'timescale', 'leap_seconds', 'local', 'configured_clock_class', 'configured_priority'], name, value)


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\: int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\: bool
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Grandmaster.ClockProperties.UtcOffset, self).__init__()

                    self.yang_name = "utc-offset"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.current_offset = YLeaf(YType.int16, "current-offset")

                    self.offset_valid = YLeaf(YType.boolean, "offset-valid")
                    self._segment_path = lambda: "utc-offset"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.UtcOffset, ['current_offset', 'offset_valid'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Grandmaster.ClockProperties.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "receiver"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.Receiver, ['clock_id', 'port_number'], name, value)


            class Sender(Entity):
                """
                Sender
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Grandmaster.ClockProperties.Sender, self).__init__()

                    self.yang_name = "sender"
                    self.yang_parent_name = "clock-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.port_number = YLeaf(YType.uint16, "port-number")
                    self._segment_path = lambda: "sender"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/clock-properties/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.ClockProperties.Sender, ['clock_id', 'port_number'], name, value)


        class Address(Entity):
            """
            The grandmaster's address information
            
            .. attribute:: mac_address
            
            	Ethernet MAC address
            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.MacAddress>`
            
            .. attribute:: ipv6_address
            
            	IPv6 address
            	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.Ipv6Address>`
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            .. attribute:: address_unknown
            
            	Unknown address type
            	**type**\: bool
            
            .. attribute:: ipv4_address
            
            	IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Grandmaster.Address, self).__init__()

                self.yang_name = "address"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"mac-address" : ("mac_address", Ptp.Grandmaster.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.Grandmaster.Address.Ipv6Address)}
                self._child_list_classes = {}

                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                self.mac_address = Ptp.Grandmaster.Address.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"
                self._children_yang_names.add("mac-address")

                self.ipv6_address = Ptp.Grandmaster.Address.Ipv6Address()
                self.ipv6_address.parent = self
                self._children_name_map["ipv6_address"] = "ipv6-address"
                self._children_yang_names.add("ipv6-address")
                self._segment_path = lambda: "address"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


            class MacAddress(Entity):
                """
                Ethernet MAC address
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Grandmaster.Address.MacAddress, self).__init__()

                    self.yang_name = "mac-address"
                    self.yang_parent_name = "address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.macaddr = YLeaf(YType.str, "macaddr")
                    self._segment_path = lambda: "mac-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/address/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.Address.MacAddress, ['macaddr'], name, value)


            class Ipv6Address(Entity):
                """
                IPv6 address
                
                .. attribute:: ipv6_address
                
                	IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Grandmaster.Address.Ipv6Address, self).__init__()

                    self.yang_name = "ipv6-address"
                    self.yang_parent_name = "address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                    self._segment_path = lambda: "ipv6-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/address/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Grandmaster.Address.Ipv6Address, ['ipv6_address'], name, value)


    class InterfaceUnicastPeers(Entity):
        """
        Table for interface unicast peers operational
        data
        
        .. attribute:: interface_unicast_peer
        
        	Interface unicast peers operational data
        	**type**\: list of  		 :py:class:`InterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.InterfaceUnicastPeers, self).__init__()

            self.yang_name = "interface-unicast-peers"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-unicast-peer" : ("interface_unicast_peer", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer)}

            self.interface_unicast_peer = YList(self)
            self._segment_path = lambda: "interface-unicast-peers"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.InterfaceUnicastPeers, [], name, value)


        class InterfaceUnicastPeer(Entity):
            """
            Interface unicast peers operational data
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: name
            
            	Interface name
            	**type**\: str
            
            .. attribute:: port_number
            
            	Port number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: peers
            
            	Unicast Peers
            	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer, self).__init__()

                self.yang_name = "interface-unicast-peer"
                self.yang_parent_name = "interface-unicast-peers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"peers" : ("peers", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.name = YLeaf(YType.str, "name")

                self.port_number = YLeaf(YType.uint16, "port-number")

                self.peers = YList(self)
                self._segment_path = lambda: "interface-unicast-peer" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-unicast-peers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer, ['interface_name', 'name', 'port_number'], name, value)


            class Peers(Entity):
                """
                Unicast Peers
                
                .. attribute:: address
                
                	The address of the unicast peer
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address>`
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:  :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant>`
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:  :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant>`
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:  :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "interface-unicast-peer"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"address" : ("address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address), "announce-grant" : ("announce_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant), "sync-grant" : ("sync_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant), "delay-response-grant" : ("delay_response_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant)}
                    self._child_list_classes = {}

                    self.address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")

                    self.announce_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"
                    self._children_yang_names.add("announce-grant")

                    self.sync_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"
                    self._children_yang_names.add("sync-grant")

                    self.delay_response_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._children_yang_names.add("delay-response-grant")
                    self._segment_path = lambda: "peers"


                class Address(Entity):
                    """
                    The address of the unicast peer
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress>`
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:  :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\: bool
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac-address" : ("mac_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress), "ipv6-address" : ("ipv6_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address)}
                        self._child_list_classes = {}

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.ipv6_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, ['encapsulation', 'address_unknown', 'ipv4_address'], name, value)


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress, self).__init__()

                            self.yang_name = "mac-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "mac-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress, ['macaddr'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address, self).__init__()

                            self.yang_name = "ipv6-address"
                            self.yang_parent_name = "address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "ipv6-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address, ['ipv6_address'], name, value)


                class AnnounceGrant(Entity):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant, self).__init__()

                        self.yang_name = "announce-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "announce-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant, ['log_grant_interval', 'grant_duration'], name, value)


                class SyncGrant(Entity):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant, self).__init__()

                        self.yang_name = "sync-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "sync-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant, ['log_grant_interval', 'grant_duration'], name, value)


                class DelayResponseGrant(Entity):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant, self).__init__()

                        self.yang_name = "delay-response-grant"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")
                        self._segment_path = lambda: "delay-response-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant, ['log_grant_interval', 'grant_duration'], name, value)


    class Platform(Entity):
        """
        PTP platform specific data
        
        .. attribute:: servo
        
        	PTP servo related parameters
        	**type**\:  :py:class:`Servo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo>`
        
        

        """

        _prefix = 'ptp-pd-oper'
        _revision = '2016-06-08'

        def __init__(self):
            super(Ptp.Platform, self).__init__()

            self.yang_name = "platform"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"servo" : ("servo", Ptp.Platform.Servo)}
            self._child_list_classes = {}

            self.servo = Ptp.Platform.Servo()
            self.servo.parent = self
            self._children_name_map["servo"] = "servo"
            self._children_yang_names.add("servo")
            self._segment_path = lambda: "Cisco-IOS-XR-ptp-pd-oper:platform"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()


        class Servo(Entity):
            """
            PTP servo related parameters
            
            .. attribute:: last_set_time
            
            	last input of setTime
            	**type**\:  :py:class:`LastSetTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastSetTime>`
            
            .. attribute:: last_received_t1
            
            	last T1 timestamp received
            	**type**\:  :py:class:`LastReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT1>`
            
            .. attribute:: last_received_t2
            
            	last T2 timestamp received
            	**type**\:  :py:class:`LastReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT2>`
            
            .. attribute:: last_received_t3
            
            	last T3 timestamp received
            	**type**\:  :py:class:`LastReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT3>`
            
            .. attribute:: last_received_t4
            
            	last T4 timestamp received
            	**type**\:  :py:class:`LastReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT4>`
            
            .. attribute:: pre_received_t1
            
            	pre T1 timestamp received
            	**type**\:  :py:class:`PreReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT1>`
            
            .. attribute:: pre_received_t2
            
            	pre T2 timestamp received
            	**type**\:  :py:class:`PreReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT2>`
            
            .. attribute:: pre_received_t3
            
            	pre T3 timestamp received
            	**type**\:  :py:class:`PreReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT3>`
            
            .. attribute:: pre_received_t4
            
            	pre T4 timestamp received
            	**type**\:  :py:class:`PreReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT4>`
            
            .. attribute:: lock_status
            
            	lock status of device
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: running
            
            	running status of apr
            	**type**\: bool
            
            .. attribute:: device_status
            
            	status of device
            	**type**\: str
            
            	**length:** 0..50
            
            .. attribute:: log_level
            
            	log level of apr
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: phase_accuracy_last
            
            	 last phase alignment accuracy
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: num_sync_timestamp
            
            	number of sync timestamp received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_delay_timestamp
            
            	number of delay timestamp received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_set_time
            
            	number of setTime() been called
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_step_time
            
            	number of stepTime() been called
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_adjust_freq
            
            	number of adjustFreq() been called
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_adjust_freq_time
            
            	number of adjustFreqTime() been called
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_adjust_freq
            
            	last input of adjustFreq
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: last_step_time
            
            	last input of stepTime
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: num_discard_sync_timestamp
            
            	number of sync timestamp discarded
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_discard_delay_timestamp
            
            	number of delay timestamp discarded
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: flagof_last_set_time
            
            	last input flag of setTime
            	**type**\: bool
            
            .. attribute:: offset_from_master
            
            	Time Offset From Master
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: mean_path_delay
            
            	Mean Path Delay
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            

            """

            _prefix = 'ptp-pd-oper'
            _revision = '2016-06-08'

            def __init__(self):
                super(Ptp.Platform.Servo, self).__init__()

                self.yang_name = "servo"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"last-set-time" : ("last_set_time", Ptp.Platform.Servo.LastSetTime), "last-received-t1" : ("last_received_t1", Ptp.Platform.Servo.LastReceivedT1), "last-received-t2" : ("last_received_t2", Ptp.Platform.Servo.LastReceivedT2), "last-received-t3" : ("last_received_t3", Ptp.Platform.Servo.LastReceivedT3), "last-received-t4" : ("last_received_t4", Ptp.Platform.Servo.LastReceivedT4), "pre-received-t1" : ("pre_received_t1", Ptp.Platform.Servo.PreReceivedT1), "pre-received-t2" : ("pre_received_t2", Ptp.Platform.Servo.PreReceivedT2), "pre-received-t3" : ("pre_received_t3", Ptp.Platform.Servo.PreReceivedT3), "pre-received-t4" : ("pre_received_t4", Ptp.Platform.Servo.PreReceivedT4)}
                self._child_list_classes = {}

                self.lock_status = YLeaf(YType.uint16, "lock-status")

                self.running = YLeaf(YType.boolean, "running")

                self.device_status = YLeaf(YType.str, "device-status")

                self.log_level = YLeaf(YType.uint16, "log-level")

                self.phase_accuracy_last = YLeaf(YType.int64, "phase-accuracy-last")

                self.num_sync_timestamp = YLeaf(YType.uint32, "num-sync-timestamp")

                self.num_delay_timestamp = YLeaf(YType.uint32, "num-delay-timestamp")

                self.num_set_time = YLeaf(YType.uint32, "num-set-time")

                self.num_step_time = YLeaf(YType.uint32, "num-step-time")

                self.num_adjust_freq = YLeaf(YType.uint32, "num-adjust-freq")

                self.num_adjust_freq_time = YLeaf(YType.uint32, "num-adjust-freq-time")

                self.last_adjust_freq = YLeaf(YType.int32, "last-adjust-freq")

                self.last_step_time = YLeaf(YType.int32, "last-step-time")

                self.num_discard_sync_timestamp = YLeaf(YType.uint32, "num-discard-sync-timestamp")

                self.num_discard_delay_timestamp = YLeaf(YType.uint32, "num-discard-delay-timestamp")

                self.flagof_last_set_time = YLeaf(YType.boolean, "flagof-last-set-time")

                self.offset_from_master = YLeaf(YType.int64, "offset-from-master")

                self.mean_path_delay = YLeaf(YType.int64, "mean-path-delay")

                self.last_set_time = Ptp.Platform.Servo.LastSetTime()
                self.last_set_time.parent = self
                self._children_name_map["last_set_time"] = "last-set-time"
                self._children_yang_names.add("last-set-time")

                self.last_received_t1 = Ptp.Platform.Servo.LastReceivedT1()
                self.last_received_t1.parent = self
                self._children_name_map["last_received_t1"] = "last-received-t1"
                self._children_yang_names.add("last-received-t1")

                self.last_received_t2 = Ptp.Platform.Servo.LastReceivedT2()
                self.last_received_t2.parent = self
                self._children_name_map["last_received_t2"] = "last-received-t2"
                self._children_yang_names.add("last-received-t2")

                self.last_received_t3 = Ptp.Platform.Servo.LastReceivedT3()
                self.last_received_t3.parent = self
                self._children_name_map["last_received_t3"] = "last-received-t3"
                self._children_yang_names.add("last-received-t3")

                self.last_received_t4 = Ptp.Platform.Servo.LastReceivedT4()
                self.last_received_t4.parent = self
                self._children_name_map["last_received_t4"] = "last-received-t4"
                self._children_yang_names.add("last-received-t4")

                self.pre_received_t1 = Ptp.Platform.Servo.PreReceivedT1()
                self.pre_received_t1.parent = self
                self._children_name_map["pre_received_t1"] = "pre-received-t1"
                self._children_yang_names.add("pre-received-t1")

                self.pre_received_t2 = Ptp.Platform.Servo.PreReceivedT2()
                self.pre_received_t2.parent = self
                self._children_name_map["pre_received_t2"] = "pre-received-t2"
                self._children_yang_names.add("pre-received-t2")

                self.pre_received_t3 = Ptp.Platform.Servo.PreReceivedT3()
                self.pre_received_t3.parent = self
                self._children_name_map["pre_received_t3"] = "pre-received-t3"
                self._children_yang_names.add("pre-received-t3")

                self.pre_received_t4 = Ptp.Platform.Servo.PreReceivedT4()
                self.pre_received_t4.parent = self
                self._children_name_map["pre_received_t4"] = "pre-received-t4"
                self._children_yang_names.add("pre-received-t4")
                self._segment_path = lambda: "servo"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Platform.Servo, ['lock_status', 'running', 'device_status', 'log_level', 'phase_accuracy_last', 'num_sync_timestamp', 'num_delay_timestamp', 'num_set_time', 'num_step_time', 'num_adjust_freq', 'num_adjust_freq_time', 'last_adjust_freq', 'last_step_time', 'num_discard_sync_timestamp', 'num_discard_delay_timestamp', 'flagof_last_set_time', 'offset_from_master', 'mean_path_delay'], name, value)


            class LastSetTime(Entity):
                """
                last input of setTime
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.LastSetTime, self).__init__()

                    self.yang_name = "last-set-time"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "last-set-time"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastSetTime, ['second', 'nano_second'], name, value)


            class LastReceivedT1(Entity):
                """
                last T1 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.LastReceivedT1, self).__init__()

                    self.yang_name = "last-received-t1"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "last-received-t1"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT1, ['second', 'nano_second'], name, value)


            class LastReceivedT2(Entity):
                """
                last T2 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.LastReceivedT2, self).__init__()

                    self.yang_name = "last-received-t2"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "last-received-t2"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT2, ['second', 'nano_second'], name, value)


            class LastReceivedT3(Entity):
                """
                last T3 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.LastReceivedT3, self).__init__()

                    self.yang_name = "last-received-t3"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "last-received-t3"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT3, ['second', 'nano_second'], name, value)


            class LastReceivedT4(Entity):
                """
                last T4 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.LastReceivedT4, self).__init__()

                    self.yang_name = "last-received-t4"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "last-received-t4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT4, ['second', 'nano_second'], name, value)


            class PreReceivedT1(Entity):
                """
                pre T1 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.PreReceivedT1, self).__init__()

                    self.yang_name = "pre-received-t1"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "pre-received-t1"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT1, ['second', 'nano_second'], name, value)


            class PreReceivedT2(Entity):
                """
                pre T2 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.PreReceivedT2, self).__init__()

                    self.yang_name = "pre-received-t2"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "pre-received-t2"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT2, ['second', 'nano_second'], name, value)


            class PreReceivedT3(Entity):
                """
                pre T3 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.PreReceivedT3, self).__init__()

                    self.yang_name = "pre-received-t3"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "pre-received-t3"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT3, ['second', 'nano_second'], name, value)


            class PreReceivedT4(Entity):
                """
                pre T4 timestamp received
                
                .. attribute:: second
                
                	value of second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ptp-pd-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(Ptp.Platform.Servo.PreReceivedT4, self).__init__()

                    self.yang_name = "pre-received-t4"
                    self.yang_parent_name = "servo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.second = YLeaf(YType.uint32, "second")

                    self.nano_second = YLeaf(YType.uint32, "nano-second")
                    self._segment_path = lambda: "pre-received-t4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT4, ['second', 'nano_second'], name, value)

    def clone_ptr(self):
        self._top_entity = Ptp()
        return self._top_entity

