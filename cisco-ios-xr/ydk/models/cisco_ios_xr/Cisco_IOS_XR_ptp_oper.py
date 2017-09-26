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
    
    .. attribute:: advertised_clock
    
    	Advertised clock operational data
    	**type**\:   :py:class:`AdvertisedClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock>`
    
    .. attribute:: dataset
    
    	Global PTP datasets
    	**type**\:   :py:class:`Dataset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset>`
    
    .. attribute:: global_configuration_error
    
    	Global configuration error operational data
    	**type**\:   :py:class:`GlobalConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError>`
    
    .. attribute:: grandmaster
    
    	Grandmaster clock operational data
    	**type**\:   :py:class:`Grandmaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster>`
    
    .. attribute:: interface_configuration_errors
    
    	Table for interface configuration error operational data
    	**type**\:   :py:class:`InterfaceConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors>`
    
    .. attribute:: interface_foreign_masters
    
    	Table for interface foreign master clock operational data
    	**type**\:   :py:class:`InterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters>`
    
    .. attribute:: interface_packet_counters
    
    	Table for interface packet counter operational data
    	**type**\:   :py:class:`InterfacePacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters>`
    
    .. attribute:: interface_unicast_peers
    
    	Table for interface unicast peers operational data
    	**type**\:   :py:class:`InterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers>`
    
    .. attribute:: interfaces
    
    	Table for interface operational data
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces>`
    
    .. attribute:: leap_seconds
    
    	Upcoming leap\-seconds information
    	**type**\:   :py:class:`LeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LeapSeconds>`
    
    .. attribute:: local_clock
    
    	Local clock operational data
    	**type**\:   :py:class:`LocalClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock>`
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes>`
    
    .. attribute:: platform
    
    	PTP platform specific data
    	**type**\:   :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform>`
    
    

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
        self._child_container_classes = {"advertised-clock" : ("advertised_clock", Ptp.AdvertisedClock), "dataset" : ("dataset", Ptp.Dataset), "global-configuration-error" : ("global_configuration_error", Ptp.GlobalConfigurationError), "grandmaster" : ("grandmaster", Ptp.Grandmaster), "interface-configuration-errors" : ("interface_configuration_errors", Ptp.InterfaceConfigurationErrors), "interface-foreign-masters" : ("interface_foreign_masters", Ptp.InterfaceForeignMasters), "interface-packet-counters" : ("interface_packet_counters", Ptp.InterfacePacketCounters), "interface-unicast-peers" : ("interface_unicast_peers", Ptp.InterfaceUnicastPeers), "interfaces" : ("interfaces", Ptp.Interfaces), "leap-seconds" : ("leap_seconds", Ptp.LeapSeconds), "local-clock" : ("local_clock", Ptp.LocalClock), "nodes" : ("nodes", Ptp.Nodes), "platform" : ("platform", Ptp.Platform)}
        self._child_list_classes = {}

        self.advertised_clock = Ptp.AdvertisedClock()
        self.advertised_clock.parent = self
        self._children_name_map["advertised_clock"] = "advertised-clock"
        self._children_yang_names.add("advertised-clock")

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

        self.interface_configuration_errors = Ptp.InterfaceConfigurationErrors()
        self.interface_configuration_errors.parent = self
        self._children_name_map["interface_configuration_errors"] = "interface-configuration-errors"
        self._children_yang_names.add("interface-configuration-errors")

        self.interface_foreign_masters = Ptp.InterfaceForeignMasters()
        self.interface_foreign_masters.parent = self
        self._children_name_map["interface_foreign_masters"] = "interface-foreign-masters"
        self._children_yang_names.add("interface-foreign-masters")

        self.interface_packet_counters = Ptp.InterfacePacketCounters()
        self.interface_packet_counters.parent = self
        self._children_name_map["interface_packet_counters"] = "interface-packet-counters"
        self._children_yang_names.add("interface-packet-counters")

        self.interface_unicast_peers = Ptp.InterfaceUnicastPeers()
        self.interface_unicast_peers.parent = self
        self._children_name_map["interface_unicast_peers"] = "interface-unicast-peers"
        self._children_yang_names.add("interface-unicast-peers")

        self.interfaces = Ptp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.leap_seconds = Ptp.LeapSeconds()
        self.leap_seconds.parent = self
        self._children_name_map["leap_seconds"] = "leap-seconds"
        self._children_yang_names.add("leap-seconds")

        self.local_clock = Ptp.LocalClock()
        self.local_clock.parent = self
        self._children_name_map["local_clock"] = "local-clock"
        self._children_yang_names.add("local-clock")

        self.nodes = Ptp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.platform = Ptp.Platform()
        self.platform.parent = self
        self._children_name_map["platform"] = "platform"
        self._children_yang_names.add("platform")
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp"


    class AdvertisedClock(Entity):
        """
        Advertised clock operational data
        
        .. attribute:: clock_properties
        
        	Advertised Clock
        	**type**\:   :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties>`
        
        .. attribute:: domain
        
        	The PTP domain of that the advertised clock is in
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: received_time_source
        
        	The time source received from the parent clock
        	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
        
        .. attribute:: received_timescale
        
        	The timescale received from the parent clock
        	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
        
        .. attribute:: time_source_configured
        
        	Whether the advertised time source is configured
        	**type**\:  bool
        
        .. attribute:: timescale_configured
        
        	Whether the advertised timescale is configured
        	**type**\:  bool
        
        

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

            self.received_time_source = YLeaf(YType.enumeration, "received-time-source")

            self.received_timescale = YLeaf(YType.enumeration, "received-timescale")

            self.time_source_configured = YLeaf(YType.boolean, "time-source-configured")

            self.timescale_configured = YLeaf(YType.boolean, "timescale-configured")

            self.clock_properties = Ptp.AdvertisedClock.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._children_yang_names.add("clock-properties")
            self._segment_path = lambda: "advertised-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.AdvertisedClock, ['domain', 'received_time_source', 'received_timescale', 'time_source_configured', 'timescale_configured'], name, value)


        class ClockProperties(Entity):
            """
            Advertised Clock
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\:  bool
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:   :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\:  bool
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:   :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:   :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.Sender>`
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\:  bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:   :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.AdvertisedClock.ClockProperties.UtcOffset>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.AdvertisedClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "advertised-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"receiver" : ("receiver", Ptp.AdvertisedClock.ClockProperties.Receiver), "sender" : ("sender", Ptp.AdvertisedClock.ClockProperties.Sender), "utc-offset" : ("utc_offset", Ptp.AdvertisedClock.ClockProperties.UtcOffset)}
                self._child_list_classes = {}

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.class_ = YLeaf(YType.uint8, "class")

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.receiver = Ptp.AdvertisedClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.AdvertisedClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")

                self.utc_offset = Ptp.AdvertisedClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/advertised-clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.AdvertisedClock.ClockProperties, ['accuracy', 'class_', 'clock_id', 'configured_clock_class', 'configured_priority', 'frequency_traceable', 'leap_seconds', 'local', 'offset_log_variance', 'priority1', 'priority2', 'steps_removed', 'time_source', 'time_traceable', 'timescale'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\:  bool
                
                

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


    class Dataset(Entity):
        """
        Global PTP datasets
        
        .. attribute:: current_ds
        
        	currentDS information as described in IEEE 1588\-2008
        	**type**\:   :py:class:`CurrentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.CurrentDs>`
        
        .. attribute:: default_ds
        
        	defaultDS information as described in IEEE 1588\-2008
        	**type**\:   :py:class:`DefaultDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.DefaultDs>`
        
        .. attribute:: parent_ds
        
        	parentDS information as described in IEEE 1588\-2008
        	**type**\:   :py:class:`ParentDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.ParentDs>`
        
        .. attribute:: port_dses
        
        	Table for portDS information
        	**type**\:   :py:class:`PortDses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses>`
        
        .. attribute:: time_properties_ds
        
        	timePropertiesDS information as described in IEEE 1588\-2008
        	**type**\:   :py:class:`TimePropertiesDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.TimePropertiesDs>`
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Dataset, self).__init__()

            self.yang_name = "dataset"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"current-ds" : ("current_ds", Ptp.Dataset.CurrentDs), "default-ds" : ("default_ds", Ptp.Dataset.DefaultDs), "parent-ds" : ("parent_ds", Ptp.Dataset.ParentDs), "port-dses" : ("port_dses", Ptp.Dataset.PortDses), "time-properties-ds" : ("time_properties_ds", Ptp.Dataset.TimePropertiesDs)}
            self._child_list_classes = {}

            self.current_ds = Ptp.Dataset.CurrentDs()
            self.current_ds.parent = self
            self._children_name_map["current_ds"] = "current-ds"
            self._children_yang_names.add("current-ds")

            self.default_ds = Ptp.Dataset.DefaultDs()
            self.default_ds.parent = self
            self._children_name_map["default_ds"] = "default-ds"
            self._children_yang_names.add("default-ds")

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


        class CurrentDs(Entity):
            """
            currentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: mean_path_delay
            
            	The mean path delay bewteen the foreign\-master and the local\-clock
            	**type**\:  int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: offset_from_master
            
            	The UTC offset of the local\-clock from the GM
            	**type**\:  int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: steps_removed
            
            	How many steps removed this clock is from the GM
            	**type**\:  int
            
            	**range:** 0..65535
            
            

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

                self.mean_path_delay = YLeaf(YType.int64, "mean-path-delay")

                self.offset_from_master = YLeaf(YType.int64, "offset-from-master")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")
                self._segment_path = lambda: "current-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.CurrentDs, ['mean_path_delay', 'offset_from_master', 'steps_removed'], name, value)


        class DefaultDs(Entity):
            """
            defaultDS information as described in IEEE
            1588\-2008
            
            .. attribute:: clock_accuracy
            
            	The accuracy of the local\-clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_class
            
            	The clock class of the local\-clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_id
            
            	The local\-clock ID
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: domain_number
            
            	The domain of the local\-clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: local_priority
            
            	Local priority of the local clock
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_ports
            
            	The number of active PTP ports on this clock
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: oslv
            
            	The offset scaled log variance of the local\-clock
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority1
            
            	The priority1 of the local\-clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	The priority2 of the local\-clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: signal_fail
            
            	Signal fail status of the local clock
            	**type**\:  bool
            
            .. attribute:: slave_only
            
            	Whether the local\-clock is globally configured as slave\-only
            	**type**\:  bool
            
            .. attribute:: two_step_flag
            
            	Is the twoStepFlag set for this clock
            	**type**\:  bool
            
            

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

                self.clock_accuracy = YLeaf(YType.uint8, "clock-accuracy")

                self.clock_class = YLeaf(YType.uint8, "clock-class")

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.domain_number = YLeaf(YType.uint8, "domain-number")

                self.local_priority = YLeaf(YType.uint32, "local-priority")

                self.number_ports = YLeaf(YType.uint32, "number-ports")

                self.oslv = YLeaf(YType.uint16, "oslv")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                self.slave_only = YLeaf(YType.boolean, "slave-only")

                self.two_step_flag = YLeaf(YType.boolean, "two-step-flag")
                self._segment_path = lambda: "default-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.DefaultDs, ['clock_accuracy', 'clock_class', 'clock_id', 'domain_number', 'local_priority', 'number_ports', 'oslv', 'priority1', 'priority2', 'signal_fail', 'slave_only', 'two_step_flag'], name, value)


        class ParentDs(Entity):
            """
            parentDS information as described in IEEE
            1588\-2008
            
            .. attribute:: gm_clock_accuracy
            
            	The clock accuracy of the GM
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: gm_clock_class
            
            	The clock class of the GM
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: gm_clock_id
            
            	The Clock ID of the GM
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: gm_priority1
            
            	The priority1 of the GM
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: gm_priority2
            
            	The priority2 of the GM
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: gmoslv
            
            	The offset scaled log variance of the GM
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: observed_parent_clock_phase_change_rate
            
            	The observed rate of change of phase of the parent clock
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: observed_parent_oslv
            
            	The observed parent offset scaled log variance
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: parent_clock_id
            
            	The Clock ID of the parent clock
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: parent_port_number
            
            	The port number on which the parent clock is received
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: parent_stats
            
            	Whether the parentStats is valid
            	**type**\:  bool
            
            

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

                self.gm_clock_accuracy = YLeaf(YType.uint8, "gm-clock-accuracy")

                self.gm_clock_class = YLeaf(YType.uint8, "gm-clock-class")

                self.gm_clock_id = YLeaf(YType.uint64, "gm-clock-id")

                self.gm_priority1 = YLeaf(YType.uint8, "gm-priority1")

                self.gm_priority2 = YLeaf(YType.uint8, "gm-priority2")

                self.gmoslv = YLeaf(YType.uint16, "gmoslv")

                self.observed_parent_clock_phase_change_rate = YLeaf(YType.uint32, "observed-parent-clock-phase-change-rate")

                self.observed_parent_oslv = YLeaf(YType.uint16, "observed-parent-oslv")

                self.parent_clock_id = YLeaf(YType.uint64, "parent-clock-id")

                self.parent_port_number = YLeaf(YType.uint16, "parent-port-number")

                self.parent_stats = YLeaf(YType.boolean, "parent-stats")
                self._segment_path = lambda: "parent-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.ParentDs, ['gm_clock_accuracy', 'gm_clock_class', 'gm_clock_id', 'gm_priority1', 'gm_priority2', 'gmoslv', 'observed_parent_clock_phase_change_rate', 'observed_parent_oslv', 'parent_clock_id', 'parent_port_number', 'parent_stats'], name, value)


        class PortDses(Entity):
            """
            Table for portDS information
            
            .. attribute:: port_ds
            
            	PortDS information
            	**type**\: list of    :py:class:`PortDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Dataset.PortDses.PortDs>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: annoucne_receipt_timeout
                
                	The announce timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: clock_id
                
                	The ID of the local\-clock
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: delay_mechanism
                
                	The delay mechanism being used on this port
                	**type**\:   :py:class:`PtpBagDelayMechanism <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagDelayMechanism>`
                
                .. attribute:: local_priority
                
                	Local priority of the local clock
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: log_announce_interval
                
                	The log (base 2) of the announce interval
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: log_min_delay_req_interval
                
                	The log (base 2) of the minimum delay\-request interval
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: log_min_p_delay_req_interval
                
                	The log (base 2) of the minimum peer\-delay\-request interval
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: log_sync_interval
                
                	The log (base 2) of the sync interval
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: master_only
                
                	Is the port master\-only?
                	**type**\:  bool
                
                .. attribute:: peer_mean_path_delay
                
                	The mean path delay between peers
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: port_number
                
                	The port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: port_state
                
                	The port state
                	**type**\:   :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                
                .. attribute:: signal_fail
                
                	Signal fail status of the port
                	**type**\:  bool
                
                .. attribute:: version_number
                
                	The version of IEEE 1588 being run
                	**type**\:  int
                
                	**range:** 0..255
                
                

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

                    self.annoucne_receipt_timeout = YLeaf(YType.uint32, "annoucne-receipt-timeout")

                    self.clock_id = YLeaf(YType.uint64, "clock-id")

                    self.delay_mechanism = YLeaf(YType.enumeration, "delay-mechanism")

                    self.local_priority = YLeaf(YType.uint32, "local-priority")

                    self.log_announce_interval = YLeaf(YType.int16, "log-announce-interval")

                    self.log_min_delay_req_interval = YLeaf(YType.int16, "log-min-delay-req-interval")

                    self.log_min_p_delay_req_interval = YLeaf(YType.int16, "log-min-p-delay-req-interval")

                    self.log_sync_interval = YLeaf(YType.int16, "log-sync-interval")

                    self.master_only = YLeaf(YType.boolean, "master-only")

                    self.peer_mean_path_delay = YLeaf(YType.int64, "peer-mean-path-delay")

                    self.port_number = YLeaf(YType.uint16, "port-number")

                    self.port_state = YLeaf(YType.enumeration, "port-state")

                    self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                    self.version_number = YLeaf(YType.uint8, "version-number")
                    self._segment_path = lambda: "port-ds" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/port-dses/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Dataset.PortDses.PortDs, ['interface_name', 'annoucne_receipt_timeout', 'clock_id', 'delay_mechanism', 'local_priority', 'log_announce_interval', 'log_min_delay_req_interval', 'log_min_p_delay_req_interval', 'log_sync_interval', 'master_only', 'peer_mean_path_delay', 'port_number', 'port_state', 'signal_fail', 'version_number'], name, value)


        class TimePropertiesDs(Entity):
            """
            timePropertiesDS information as described in
            IEEE 1588\-2008
            
            .. attribute:: current_utc_offset
            
            	The current UTC offset
            	**type**\:  int
            
            	**range:** \-32768..32767
            
            .. attribute:: current_utc_offset_valid
            
            	Whether the current UTC offset is valid
            	**type**\:  bool
            
            .. attribute:: frequency_traceable
            
            	Whther the frequency source is traceable
            	**type**\:  bool
            
            .. attribute:: leap59
            
            	Whether the last minute of the day has 59 seconds
            	**type**\:  bool
            
            .. attribute:: leap61
            
            	Whether the last minute of the day has 61 seconds
            	**type**\:  bool
            
            .. attribute:: ptp_timescale
            
            	Whether the timescale being used is the PTP timescale
            	**type**\:  bool
            
            .. attribute:: time_source
            
            	The physical time\-source of the GM clock
            	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: time_traceable
            
            	Whether the time\-of\-day source is traceable
            	**type**\:  bool
            
            

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

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.leap59 = YLeaf(YType.boolean, "leap59")

                self.leap61 = YLeaf(YType.boolean, "leap61")

                self.ptp_timescale = YLeaf(YType.boolean, "ptp-timescale")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")
                self._segment_path = lambda: "time-properties-ds"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/dataset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Dataset.TimePropertiesDs, ['current_utc_offset', 'current_utc_offset_valid', 'frequency_traceable', 'leap59', 'leap61', 'ptp_timescale', 'time_source', 'time_traceable'], name, value)


    class GlobalConfigurationError(Entity):
        """
        Global configuration error operational data
        
        .. attribute:: clock_profile
        
        	The clock profile
        	**type**\:   :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
        
        .. attribute:: clock_profile_set
        
        	Is the clock profile set
        	**type**\:  bool
        
        .. attribute:: configuration_errors
        
        	Configuration Errors
        	**type**\:   :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.GlobalConfigurationError.ConfigurationErrors>`
        
        .. attribute:: domain_number
        
        	The PTP domain
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: priority2
        
        	The configured priority2 value
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: telecom_clock_type
        
        	Configured telecom clock type
        	**type**\:   :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
        
        

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

            self.domain_number = YLeaf(YType.uint8, "domain-number")

            self.priority2 = YLeaf(YType.uint8, "priority2")

            self.telecom_clock_type = YLeaf(YType.enumeration, "telecom-clock-type")

            self.configuration_errors = Ptp.GlobalConfigurationError.ConfigurationErrors()
            self.configuration_errors.parent = self
            self._children_name_map["configuration_errors"] = "configuration-errors"
            self._children_yang_names.add("configuration-errors")
            self._segment_path = lambda: "global-configuration-error"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.GlobalConfigurationError, ['clock_profile', 'clock_profile_set', 'domain_number', 'priority2', 'telecom_clock_type'], name, value)


        class ConfigurationErrors(Entity):
            """
            Configuration Errors
            
            .. attribute:: domain
            
            	Domain not compatible with configured profile
            	**type**\:  bool
            
            .. attribute:: profile_priority1_config
            
            	Priority1 configuration is not compatible with configured profile
            	**type**\:  bool
            
            .. attribute:: profile_priority2_value
            
            	Priority2 value is not compatible with configured profile
            	**type**\:  bool
            
            

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
        
        .. attribute:: address
        
        	The grandmaster's address information
        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address>`
        
        .. attribute:: clock_properties
        
        	Grandmaster clock
        	**type**\:   :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties>`
        
        .. attribute:: domain
        
        	The PTP domain that the grandmaster is in
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: known_for_time
        
        	How long the clock has been grandmaster for, in seconds
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: used_for_frequency
        
        	Whether the grandmaster is setting frequency on the system
        	**type**\:  bool
        
        .. attribute:: used_for_time
        
        	Whether the grandmaster is setting time\-of\-day on the system
        	**type**\:  bool
        
        

        """

        _prefix = 'ptp-oper'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Grandmaster, self).__init__()

            self.yang_name = "grandmaster"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"address" : ("address", Ptp.Grandmaster.Address), "clock-properties" : ("clock_properties", Ptp.Grandmaster.ClockProperties)}
            self._child_list_classes = {}

            self.domain = YLeaf(YType.uint8, "domain")

            self.known_for_time = YLeaf(YType.uint32, "known-for-time")

            self.used_for_frequency = YLeaf(YType.boolean, "used-for-frequency")

            self.used_for_time = YLeaf(YType.boolean, "used-for-time")

            self.address = Ptp.Grandmaster.Address()
            self.address.parent = self
            self._children_name_map["address"] = "address"
            self._children_yang_names.add("address")

            self.clock_properties = Ptp.Grandmaster.ClockProperties()
            self.clock_properties.parent = self
            self._children_name_map["clock_properties"] = "clock-properties"
            self._children_yang_names.add("clock-properties")
            self._segment_path = lambda: "grandmaster"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Grandmaster, ['domain', 'known_for_time', 'used_for_frequency', 'used_for_time'], name, value)


        class Address(Entity):
            """
            The grandmaster's address information
            
            .. attribute:: address_unknown
            
            	Unknown address type
            	**type**\:  bool
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            .. attribute:: ipv4_address
            
            	IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address
            
            	IPv6 address
            	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.Ipv6Address>`
            
            .. attribute:: mac_address
            
            	Ethernet MAC address
            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.Address.MacAddress>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Grandmaster.Address, self).__init__()

                self.yang_name = "address"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.Grandmaster.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.Grandmaster.Address.MacAddress)}
                self._child_list_classes = {}

                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                self.ipv6_address = Ptp.Grandmaster.Address.Ipv6Address()
                self.ipv6_address.parent = self
                self._children_name_map["ipv6_address"] = "ipv6-address"
                self._children_yang_names.add("ipv6-address")

                self.mac_address = Ptp.Grandmaster.Address.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"
                self._children_yang_names.add("mac-address")
                self._segment_path = lambda: "address"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


            class Ipv6Address(Entity):
                """
                IPv6 address
                
                .. attribute:: ipv6_address
                
                	IPv6 Address
                	**type**\:  str
                
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


            class MacAddress(Entity):
                """
                Ethernet MAC address
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\:  str
                
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


        class ClockProperties(Entity):
            """
            Grandmaster clock
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\:  bool
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:   :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\:  bool
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:   :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:   :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.Sender>`
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\:  bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:   :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Grandmaster.ClockProperties.UtcOffset>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Grandmaster.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "grandmaster"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"receiver" : ("receiver", Ptp.Grandmaster.ClockProperties.Receiver), "sender" : ("sender", Ptp.Grandmaster.ClockProperties.Sender), "utc-offset" : ("utc_offset", Ptp.Grandmaster.ClockProperties.UtcOffset)}
                self._child_list_classes = {}

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.class_ = YLeaf(YType.uint8, "class")

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.receiver = Ptp.Grandmaster.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.Grandmaster.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")

                self.utc_offset = Ptp.Grandmaster.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/grandmaster/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Grandmaster.ClockProperties, ['accuracy', 'class_', 'clock_id', 'configured_clock_class', 'configured_priority', 'frequency_traceable', 'leap_seconds', 'local', 'offset_log_variance', 'priority1', 'priority2', 'steps_removed', 'time_source', 'time_traceable', 'timescale'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\:  bool
                
                

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


    class InterfaceConfigurationErrors(Entity):
        """
        Table for interface configuration error
        operational data
        
        .. attribute:: interface_configuration_error
        
        	Interface configuration error operational data
        	**type**\: list of    :py:class:`InterfaceConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: clock_profile
            
            	The clock profile
            	**type**\:   :py:class:`PtpBagProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagProfile>`
            
            .. attribute:: configuration_errors
            
            	Configuration Errors
            	**type**\:   :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors>`
            
            .. attribute:: configuration_profile_name
            
            	Configuration profile name, if a profile is selected
            	**type**\:  str
            
            .. attribute:: restrict_port_state
            
            	Restriction on the port state
            	**type**\:   :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            .. attribute:: telecom_clock_type
            
            	The telecom clock type
            	**type**\:   :py:class:`PtpBagTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagTelecomClock>`
            
            

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

                self.clock_profile = YLeaf(YType.enumeration, "clock-profile")

                self.configuration_profile_name = YLeaf(YType.str, "configuration-profile-name")

                self.restrict_port_state = YLeaf(YType.enumeration, "restrict-port-state")

                self.telecom_clock_type = YLeaf(YType.enumeration, "telecom-clock-type")

                self.configuration_errors = Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors()
                self.configuration_errors.parent = self
                self._children_name_map["configuration_errors"] = "configuration-errors"
                self._children_yang_names.add("configuration-errors")
                self._segment_path = lambda: "interface-configuration-error" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interface-configuration-errors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError, ['interface_name', 'clock_profile', 'configuration_profile_name', 'restrict_port_state', 'telecom_clock_type'], name, value)


            class ConfigurationErrors(Entity):
                """
                Configuration Errors
                
                .. attribute:: ethernet_transport
                
                	Ethernet transport configured but not supported
                	**type**\:  bool
                
                .. attribute:: global_ptp
                
                	PTP enabled on interface but not globally
                	**type**\:  bool
                
                .. attribute:: invalid_grant_reduction
                
                	Reducing invalid unicast grants is not compatible with configured profile
                	**type**\:  bool
                
                .. attribute:: ipv6
                
                	IPv6 transport configured but not supported
                	**type**\:  bool
                
                .. attribute:: local_priority
                
                	Local priority configuration is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: multicast
                
                	Multicast configured but not supported
                	**type**\:  bool
                
                .. attribute:: one_step
                
                	One step clock operation configured but not supported
                	**type**\:  bool
                
                .. attribute:: profile_announce_interval
                
                	Announce interval is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_delay_req_interval
                
                	Delay request interval is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_delay_resp_timeout
                
                	Delay response timeout configuration is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_ethernet
                
                	Ethernet transport is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_ipv4
                
                	IPv6 transport is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_ipv6
                
                	IPv6 transport is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_master_mixed
                
                	Mixed\-mode multicast master is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_master_multicast
                
                	Multicast master is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_master_unicast
                
                	Unicast master is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_mixed
                
                	Mixed\-mode multicast is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_multicast
                
                	Multicast is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_not_global
                
                	Profile is referenced but not globally configured
                	**type**\:  bool
                
                .. attribute:: profile_port_state
                
                	Port state restriction is not compatible with telecom clock type
                	**type**\:  bool
                
                .. attribute:: profile_sync_interval
                
                	Sync interval is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_sync_timeout
                
                	Sync timeout configuration is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: profile_unicast
                
                	Unicast is not compatible with profile
                	**type**\:  bool
                
                .. attribute:: slave
                
                	Slave\-operation configured but not supported
                	**type**\:  bool
                
                .. attribute:: target_address_ipv4
                
                	Ethernet multicast target\-address is configured, but transport is IPv4
                	**type**\:  bool
                
                .. attribute:: target_address_ipv6
                
                	Ethernet multicast target\-address is configured, but transport is IPv6
                	**type**\:  bool
                
                

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

                    self.ethernet_transport = YLeaf(YType.boolean, "ethernet-transport")

                    self.global_ptp = YLeaf(YType.boolean, "global-ptp")

                    self.invalid_grant_reduction = YLeaf(YType.boolean, "invalid-grant-reduction")

                    self.ipv6 = YLeaf(YType.boolean, "ipv6")

                    self.local_priority = YLeaf(YType.boolean, "local-priority")

                    self.multicast = YLeaf(YType.boolean, "multicast")

                    self.one_step = YLeaf(YType.boolean, "one-step")

                    self.profile_announce_interval = YLeaf(YType.boolean, "profile-announce-interval")

                    self.profile_delay_req_interval = YLeaf(YType.boolean, "profile-delay-req-interval")

                    self.profile_delay_resp_timeout = YLeaf(YType.boolean, "profile-delay-resp-timeout")

                    self.profile_ethernet = YLeaf(YType.boolean, "profile-ethernet")

                    self.profile_ipv4 = YLeaf(YType.boolean, "profile-ipv4")

                    self.profile_ipv6 = YLeaf(YType.boolean, "profile-ipv6")

                    self.profile_master_mixed = YLeaf(YType.boolean, "profile-master-mixed")

                    self.profile_master_multicast = YLeaf(YType.boolean, "profile-master-multicast")

                    self.profile_master_unicast = YLeaf(YType.boolean, "profile-master-unicast")

                    self.profile_mixed = YLeaf(YType.boolean, "profile-mixed")

                    self.profile_multicast = YLeaf(YType.boolean, "profile-multicast")

                    self.profile_not_global = YLeaf(YType.boolean, "profile-not-global")

                    self.profile_port_state = YLeaf(YType.boolean, "profile-port-state")

                    self.profile_sync_interval = YLeaf(YType.boolean, "profile-sync-interval")

                    self.profile_sync_timeout = YLeaf(YType.boolean, "profile-sync-timeout")

                    self.profile_unicast = YLeaf(YType.boolean, "profile-unicast")

                    self.slave = YLeaf(YType.boolean, "slave")

                    self.target_address_ipv4 = YLeaf(YType.boolean, "target-address-ipv4")

                    self.target_address_ipv6 = YLeaf(YType.boolean, "target-address-ipv6")
                    self._segment_path = lambda: "configuration-errors"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceConfigurationErrors.InterfaceConfigurationError.ConfigurationErrors, ['ethernet_transport', 'global_ptp', 'invalid_grant_reduction', 'ipv6', 'local_priority', 'multicast', 'one_step', 'profile_announce_interval', 'profile_delay_req_interval', 'profile_delay_resp_timeout', 'profile_ethernet', 'profile_ipv4', 'profile_ipv6', 'profile_master_mixed', 'profile_master_multicast', 'profile_master_unicast', 'profile_mixed', 'profile_multicast', 'profile_not_global', 'profile_port_state', 'profile_sync_interval', 'profile_sync_timeout', 'profile_unicast', 'slave', 'target_address_ipv4', 'target_address_ipv6'], name, value)


    class InterfaceForeignMasters(Entity):
        """
        Table for interface foreign master clock
        operational data
        
        .. attribute:: interface_foreign_master
        
        	Interface foreign master clock operational data
        	**type**\: list of    :py:class:`InterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: foreign_clock
            
            	Foreign clocks received on this interface
            	**type**\: list of    :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock>`
            
            .. attribute:: port_number
            
            	Port number
            	**type**\:  int
            
            	**range:** 0..65535
            
            

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
                
                .. attribute:: address
                
                	The address of the clock
                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address>`
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:   :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                
                .. attribute:: communication_model
                
                	The communication model configured on this clock
                	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                .. attribute:: configured_clock_class
                
                	Clock class configured for the clock, if any
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: configured_priority
                
                	Priority configured for the clock, if any
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: delay_asymmetry
                
                	Delay asymmetry configured for the clock, if any
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:   :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                
                .. attribute:: foreign_clock
                
                	Foreign clock information
                	**type**\:   :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock>`
                
                .. attribute:: foreign_domain
                
                	The PTP domain that the foreign clock is in
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: is_grandmaster
                
                	This clock is the currently selected grand master clock
                	**type**\:  bool
                
                .. attribute:: is_known
                
                	This clock is known by this router
                	**type**\:  bool
                
                .. attribute:: is_qualified
                
                	The clock is qualified for best master clock selection
                	**type**\:  bool
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\:  bool
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\:  bool
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:   :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant>`
                
                .. attribute:: time_known_for
                
                	How long the clock has been known by this router for, in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, self).__init__()

                    self.yang_name = "foreign-clock"
                    self.yang_parent_name = "interface-foreign-master"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"address" : ("address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address), "announce-grant" : ("announce_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant), "delay-response-grant" : ("delay_response_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant), "foreign-clock" : ("foreign_clock", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock), "sync-grant" : ("sync_grant", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant)}
                    self._child_list_classes = {}

                    self.communication_model = YLeaf(YType.enumeration, "communication-model")

                    self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.delay_asymmetry = YLeaf(YType.int32, "delay-asymmetry")

                    self.foreign_domain = YLeaf(YType.uint8, "foreign-domain")

                    self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                    self.is_known = YLeaf(YType.boolean, "is-known")

                    self.is_qualified = YLeaf(YType.boolean, "is-qualified")

                    self.ptsf_loss_announce = YLeaf(YType.boolean, "ptsf-loss-announce")

                    self.ptsf_loss_sync = YLeaf(YType.boolean, "ptsf-loss-sync")

                    self.time_known_for = YLeaf(YType.uint32, "time-known-for")

                    self.address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")

                    self.announce_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"
                    self._children_yang_names.add("announce-grant")

                    self.delay_response_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._children_yang_names.add("delay-response-grant")

                    self.foreign_clock = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock()
                    self.foreign_clock.parent = self
                    self._children_name_map["foreign_clock"] = "foreign-clock"
                    self._children_yang_names.add("foreign-clock")

                    self.sync_grant = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"
                    self._children_yang_names.add("sync-grant")
                    self._segment_path = lambda: "foreign-clock"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock, ['communication_model', 'configured_clock_class', 'configured_priority', 'delay_asymmetry', 'foreign_domain', 'is_grandmaster', 'is_known', 'is_qualified', 'ptsf_loss_announce', 'ptsf_loss_sync', 'time_known_for'], name, value)


                class Address(Entity):
                    """
                    The address of the clock
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\:  bool
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress)}
                        self._child_list_classes = {}

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")

                        self.mac_address = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
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


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
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


                class AnnounceGrant(Entity):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "announce-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.AnnounceGrant, ['grant_duration', 'log_grant_interval'], name, value)


                class DelayResponseGrant(Entity):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "delay-response-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['grant_duration', 'log_grant_interval'], name, value)


                class ForeignClock(Entity):
                    """
                    Foreign clock information
                    
                    .. attribute:: accuracy
                    
                    	Accuracy
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: class_
                    
                    	Class
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: configured_clock_class
                    
                    	The configured clock class
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: configured_priority
                    
                    	The configured priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: frequency_traceable
                    
                    	The clock is frequency traceable
                    	**type**\:  bool
                    
                    .. attribute:: leap_seconds
                    
                    	Leap Seconds
                    	**type**\:   :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                    
                    	**units**\: second
                    
                    .. attribute:: local
                    
                    	The clock is the local clock
                    	**type**\:  bool
                    
                    .. attribute:: offset_log_variance
                    
                    	Offset log variance
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: priority1
                    
                    	Priority 1
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority2
                    
                    	Priority 2
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: receiver
                    
                    	Receiver
                    	**type**\:   :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver>`
                    
                    .. attribute:: sender
                    
                    	Sender
                    	**type**\:   :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender>`
                    
                    .. attribute:: steps_removed
                    
                    	Steps removed
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: time_source
                    
                    	Time source
                    	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                    
                    .. attribute:: time_traceable
                    
                    	The clock is time traceable
                    	**type**\:  bool
                    
                    .. attribute:: timescale
                    
                    	Timescale
                    	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                    
                    .. attribute:: utc_offset
                    
                    	UTC offset
                    	**type**\:   :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock, self).__init__()

                        self.yang_name = "foreign-clock"
                        self.yang_parent_name = "foreign-clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"receiver" : ("receiver", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver), "sender" : ("sender", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender), "utc-offset" : ("utc_offset", Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset)}
                        self._child_list_classes = {}

                        self.accuracy = YLeaf(YType.uint8, "accuracy")

                        self.class_ = YLeaf(YType.uint8, "class")

                        self.clock_id = YLeaf(YType.uint64, "clock-id")

                        self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                        self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                        self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                        self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                        self.local = YLeaf(YType.boolean, "local")

                        self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                        self.priority1 = YLeaf(YType.uint8, "priority1")

                        self.priority2 = YLeaf(YType.uint8, "priority2")

                        self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                        self.time_source = YLeaf(YType.enumeration, "time-source")

                        self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                        self.timescale = YLeaf(YType.enumeration, "timescale")

                        self.receiver = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Receiver()
                        self.receiver.parent = self
                        self._children_name_map["receiver"] = "receiver"
                        self._children_yang_names.add("receiver")

                        self.sender = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.Sender()
                        self.sender.parent = self
                        self._children_name_map["sender"] = "sender"
                        self._children_yang_names.add("sender")

                        self.utc_offset = Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset()
                        self.utc_offset.parent = self
                        self._children_name_map["utc_offset"] = "utc-offset"
                        self._children_yang_names.add("utc-offset")
                        self._segment_path = lambda: "foreign-clock"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.ForeignClock, ['accuracy', 'class_', 'clock_id', 'configured_clock_class', 'configured_priority', 'frequency_traceable', 'leap_seconds', 'local', 'offset_log_variance', 'priority1', 'priority2', 'steps_removed', 'time_source', 'time_traceable', 'timescale'], name, value)


                    class Receiver(Entity):
                        """
                        Receiver
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\:  int
                        
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
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: port_number
                        
                        	Port number
                        	**type**\:  int
                        
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


                    class UtcOffset(Entity):
                        """
                        UTC offset
                        
                        .. attribute:: current_offset
                        
                        	Current offset
                        	**type**\:  int
                        
                        	**range:** \-32768..32767
                        
                        .. attribute:: offset_valid
                        
                        	The current offset is valid
                        	**type**\:  bool
                        
                        

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


                class SyncGrant(Entity):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "sync-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceForeignMasters.InterfaceForeignMaster.ForeignClock.SyncGrant, ['grant_duration', 'log_grant_interval'], name, value)


    class InterfacePacketCounters(Entity):
        """
        Table for interface packet counter operational
        data
        
        .. attribute:: interface_packet_counter
        
        	Interface packet counter operational data
        	**type**\: list of    :py:class:`InterfacePacketCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: counters
            
            	Packet counters
            	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters>`
            
            .. attribute:: peer_counter
            
            	Packet counters for each peer on this interface
            	**type**\: list of    :py:class:`PeerCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter>`
            
            

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
                
                .. attribute:: announce_dropped
                
                	Number of announce packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: announce_received
                
                	Number of announce packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: announce_sent
                
                	Number of announce packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_dropped
                
                	Number of delay\-request packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_received
                
                	Number of delay\-request packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_request_sent
                
                	Number of delay\-request packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_dropped
                
                	Number of delay\-response packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_received
                
                	Number of delay\-response packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: delay_response_sent
                
                	Number of delay\-response packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_dropped
                
                	Number of follow\-up packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_received
                
                	Number of follow\-up packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: follow_up_sent
                
                	Number of follow\-up packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_dropped
                
                	Number of management messages dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_received
                
                	Number of management messages received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: management_sent
                
                	Number of management messages sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_dropped
                
                	Number of other packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_received
                
                	Number of other packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: other_packets_sent
                
                	Number of other packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_dropped
                
                	Number of peer\-delay\-request packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_received
                
                	Number of peer\-delay\-request packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_request_sent
                
                	Number of peer\-delay\-request packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_dropped
                
                	Number of peer\-delay\-response packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_dropped
                
                	Number of peer\-delay\-response follow\-up packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_received
                
                	Number of peer\-delay\-response follow\-up packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_follow_up_sent
                
                	Number of peer\-delay\-response follow\-up packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_received
                
                	Number of peer\-delay\-response packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_delay_response_sent
                
                	Number of peer\-delay\-response packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_dropped
                
                	Number of signaling packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_received
                
                	Number of signaling packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: signaling_sent
                
                	Number of signaling packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_dropped
                
                	Number of sync packetsdropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_received
                
                	Number of sync packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sync_sent
                
                	Number of sync packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_dropped
                
                	Total number of packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_received
                
                	Total number of packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_packets_sent
                
                	Total number of packets sent
                	**type**\:  int
                
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

                    self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                    self.announce_received = YLeaf(YType.uint32, "announce-received")

                    self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                    self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                    self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                    self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                    self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                    self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                    self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                    self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                    self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                    self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                    self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                    self.management_received = YLeaf(YType.uint32, "management-received")

                    self.management_sent = YLeaf(YType.uint32, "management-sent")

                    self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                    self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                    self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                    self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                    self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                    self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                    self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                    self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                    self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                    self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                    self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                    self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                    self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                    self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                    self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                    self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                    self.sync_received = YLeaf(YType.uint32, "sync-received")

                    self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                    self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")

                    self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                    self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")
                    self._segment_path = lambda: "counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.Counters, ['announce_dropped', 'announce_received', 'announce_sent', 'delay_request_dropped', 'delay_request_received', 'delay_request_sent', 'delay_response_dropped', 'delay_response_received', 'delay_response_sent', 'follow_up_dropped', 'follow_up_received', 'follow_up_sent', 'management_dropped', 'management_received', 'management_sent', 'other_packets_dropped', 'other_packets_received', 'other_packets_sent', 'peer_delay_request_dropped', 'peer_delay_request_received', 'peer_delay_request_sent', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_dropped', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_sent', 'peer_delay_response_received', 'peer_delay_response_sent', 'signaling_dropped', 'signaling_received', 'signaling_sent', 'sync_dropped', 'sync_received', 'sync_sent', 'total_packets_dropped', 'total_packets_received', 'total_packets_sent'], name, value)


            class PeerCounter(Entity):
                """
                Packet counters for each peer on this interface
                
                .. attribute:: address
                
                	Peer address
                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address>`
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters>`
                
                

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
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\:  bool
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address>`
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peer-counter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress)}
                        self._child_list_classes = {}

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")

                        self.mac_address = Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
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


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
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


                class Counters(Entity):
                    """
                    Packet counters
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\:  int
                    
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

                        self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                        self.announce_received = YLeaf(YType.uint32, "announce-received")

                        self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                        self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                        self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                        self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                        self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                        self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                        self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                        self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                        self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                        self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                        self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                        self.management_received = YLeaf(YType.uint32, "management-received")

                        self.management_sent = YLeaf(YType.uint32, "management-sent")

                        self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                        self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                        self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                        self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                        self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                        self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                        self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                        self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                        self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                        self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                        self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                        self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                        self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                        self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                        self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                        self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                        self.sync_received = YLeaf(YType.uint32, "sync-received")

                        self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                        self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")

                        self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                        self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfacePacketCounters.InterfacePacketCounter.PeerCounter.Counters, ['announce_dropped', 'announce_received', 'announce_sent', 'delay_request_dropped', 'delay_request_received', 'delay_request_sent', 'delay_response_dropped', 'delay_response_received', 'delay_response_sent', 'follow_up_dropped', 'follow_up_received', 'follow_up_sent', 'management_dropped', 'management_received', 'management_sent', 'other_packets_dropped', 'other_packets_received', 'other_packets_sent', 'peer_delay_request_dropped', 'peer_delay_request_received', 'peer_delay_request_sent', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_dropped', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_sent', 'peer_delay_response_received', 'peer_delay_response_sent', 'signaling_dropped', 'signaling_received', 'signaling_sent', 'sync_dropped', 'sync_received', 'sync_sent', 'total_packets_dropped', 'total_packets_received', 'total_packets_sent'], name, value)


    class InterfaceUnicastPeers(Entity):
        """
        Table for interface unicast peers operational
        data
        
        .. attribute:: interface_unicast_peer
        
        	Interface unicast peers operational data
        	**type**\: list of    :py:class:`InterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: name
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: peers
            
            	Unicast Peers
            	**type**\: list of    :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers>`
            
            .. attribute:: port_number
            
            	Port number
            	**type**\:  int
            
            	**range:** 0..65535
            
            

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
                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address>`
                
                .. attribute:: announce_grant
                
                	Unicast grant information for announce messages
                	**type**\:   :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant>`
                
                .. attribute:: delay_response_grant
                
                	Unicast grant information for delay\-response messages
                	**type**\:   :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant>`
                
                .. attribute:: sync_grant
                
                	Unicast grant information for sync messages
                	**type**\:   :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant>`
                
                

                """

                _prefix = 'ptp-oper'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "interface-unicast-peer"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"address" : ("address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address), "announce-grant" : ("announce_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant), "delay-response-grant" : ("delay_response_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant), "sync-grant" : ("sync_grant", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant)}
                    self._child_list_classes = {}

                    self.address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")

                    self.announce_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant()
                    self.announce_grant.parent = self
                    self._children_name_map["announce_grant"] = "announce-grant"
                    self._children_yang_names.add("announce-grant")

                    self.delay_response_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant()
                    self.delay_response_grant.parent = self
                    self._children_name_map["delay_response_grant"] = "delay-response-grant"
                    self._children_yang_names.add("delay-response-grant")

                    self.sync_grant = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant()
                    self.sync_grant.parent = self
                    self._children_name_map["sync_grant"] = "sync-grant"
                    self._children_yang_names.add("sync-grant")
                    self._segment_path = lambda: "peers"


                class Address(Entity):
                    """
                    The address of the unicast peer
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\:  bool
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress)}
                        self._child_list_classes = {}

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")

                        self.mac_address = Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
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


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
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


                class AnnounceGrant(Entity):
                    """
                    Unicast grant information for announce messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "announce-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.AnnounceGrant, ['grant_duration', 'log_grant_interval'], name, value)


                class DelayResponseGrant(Entity):
                    """
                    Unicast grant information for delay\-response
                    messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "delay-response-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.DelayResponseGrant, ['grant_duration', 'log_grant_interval'], name, value)


                class SyncGrant(Entity):
                    """
                    Unicast grant information for sync messages
                    
                    .. attribute:: grant_duration
                    
                    	Duraction of the grant
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: log_grant_interval
                    
                    	Log of the interval which has been granted
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    

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

                        self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                        self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                        self._segment_path = lambda: "sync-grant"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.InterfaceUnicastPeers.InterfaceUnicastPeer.Peers.SyncGrant, ['grant_duration', 'log_grant_interval'], name, value)


    class Interfaces(Entity):
        """
        Table for interface operational data
        
        .. attribute:: interface
        
        	Interface operational data
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: announce_timeout
            
            	Announce timeout
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: communication_model
            
            	Communication model configured on the interface
            	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
            
            .. attribute:: configured_port_state
            
            	The configured port state
            	**type**\:   :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
            
            .. attribute:: encapsulation
            
            	Encapsulation
            	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
            
            .. attribute:: event_cos
            
            	The class of service used on the interface for event messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: event_dscp
            
            	The DSCP class used on the interface for event messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: general_cos
            
            	The class of service used on the interface for general messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: general_dscp
            
            	The DSCP class used on the interface for general messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv4_address
            
            	IPv4 address, if IPv4 encapsulation is being used
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address
            
            	Ipv6 address, if IPv6 encapsulation is being used
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: line_state
            
            	Line state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_priority
            
            	Local priority, for the G.8275.1 PTP profile
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: log_announce_interval
            
            	Log of the interface's announce interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: log_min_delay_request_interval
            
            	Log of the interface's Minimum delay\-request interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: log_sync_interval
            
            	Log of the interface's sync interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mac_address
            
            	MAC address, if Ethernet encapsulation is being used
            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MacAddress>`
            
            .. attribute:: master_table
            
            	The interface's master table
            	**type**\: list of    :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable>`
            
            .. attribute:: max_sync_rate
            
            	The maximum rate of sync packets on the interface
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: port_number
            
            	Port number
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: port_state
            
            	Port state
            	**type**\:   :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
            
            .. attribute:: signal_fail
            
            	Signal fail status of the interface
            	**type**\:  bool
            
            .. attribute:: supports_ethernet
            
            	The interface supports ethernet transport
            	**type**\:  bool
            
            .. attribute:: supports_ipv6
            
            	The interface supports IPv6 transport
            	**type**\:  bool
            
            .. attribute:: supports_multicast
            
            	The interface supports multicast
            	**type**\:  bool
            
            .. attribute:: supports_one_step
            
            	The interface supports one\-step operation
            	**type**\:  bool
            
            .. attribute:: supports_slave
            
            	The interface supports operation in slave mode
            	**type**\:  bool
            
            .. attribute:: supports_source_ip
            
            	The interface supports source ip configuration
            	**type**\:  bool
            
            .. attribute:: supports_two_step
            
            	The interface supports two\-step operation
            	**type**\:  bool
            
            .. attribute:: two_step
            
            	Two step delay\-request mechanism is being used
            	**type**\:  bool
            
            .. attribute:: unicast_peers
            
            	The number of unicast peers known by the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

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

                self.announce_timeout = YLeaf(YType.uint32, "announce-timeout")

                self.communication_model = YLeaf(YType.enumeration, "communication-model")

                self.configured_port_state = YLeaf(YType.enumeration, "configured-port-state")

                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                self.event_cos = YLeaf(YType.uint32, "event-cos")

                self.event_dscp = YLeaf(YType.uint32, "event-dscp")

                self.general_cos = YLeaf(YType.uint32, "general-cos")

                self.general_dscp = YLeaf(YType.uint32, "general-dscp")

                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                self.line_state = YLeaf(YType.uint32, "line-state")

                self.local_priority = YLeaf(YType.uint8, "local-priority")

                self.log_announce_interval = YLeaf(YType.int32, "log-announce-interval")

                self.log_min_delay_request_interval = YLeaf(YType.int32, "log-min-delay-request-interval")

                self.log_sync_interval = YLeaf(YType.int32, "log-sync-interval")

                self.max_sync_rate = YLeaf(YType.uint8, "max-sync-rate")

                self.port_number = YLeaf(YType.uint16, "port-number")

                self.port_state = YLeaf(YType.enumeration, "port-state")

                self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                self.supports_ethernet = YLeaf(YType.boolean, "supports-ethernet")

                self.supports_ipv6 = YLeaf(YType.boolean, "supports-ipv6")

                self.supports_multicast = YLeaf(YType.boolean, "supports-multicast")

                self.supports_one_step = YLeaf(YType.boolean, "supports-one-step")

                self.supports_slave = YLeaf(YType.boolean, "supports-slave")

                self.supports_source_ip = YLeaf(YType.boolean, "supports-source-ip")

                self.supports_two_step = YLeaf(YType.boolean, "supports-two-step")

                self.two_step = YLeaf(YType.boolean, "two-step")

                self.unicast_peers = YLeaf(YType.uint32, "unicast-peers")

                self.mac_address = Ptp.Interfaces.Interface.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"
                self._children_yang_names.add("mac-address")

                self.master_table = YList(self)
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Interfaces.Interface, ['interface_name', 'announce_timeout', 'communication_model', 'configured_port_state', 'encapsulation', 'event_cos', 'event_dscp', 'general_cos', 'general_dscp', 'ipv4_address', 'ipv6_address', 'line_state', 'local_priority', 'log_announce_interval', 'log_min_delay_request_interval', 'log_sync_interval', 'max_sync_rate', 'port_number', 'port_state', 'signal_fail', 'supports_ethernet', 'supports_ipv6', 'supports_multicast', 'supports_one_step', 'supports_slave', 'supports_source_ip', 'supports_two_step', 'two_step', 'unicast_peers'], name, value)


            class MacAddress(Entity):
                """
                MAC address, if Ethernet encapsulation is being
                used
                
                .. attribute:: macaddr
                
                	macaddr
                	**type**\:  str
                
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
                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address>`
                
                .. attribute:: communication_model
                
                	The configured communication model of the master clock
                	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                
                .. attribute:: is_grandmaster
                
                	Whether this is the grandmaster
                	**type**\:  bool
                
                .. attribute:: is_nonnegotiated
                
                	Whether this master uses non\-negotiated unicast
                	**type**\:  bool
                
                .. attribute:: known
                
                	Whether the interface is receiving messages from this master
                	**type**\:  bool
                
                .. attribute:: priority
                
                	The priority of the master clock, if it is set
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: ptsf_loss_announce
                
                	Announced messages are not being received from the master
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: ptsf_loss_sync
                
                	Sync messages are not being received from the master
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: qualified
                
                	The master is qualified for best master clock selection
                	**type**\:  bool
                
                

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

                    self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                    self.is_nonnegotiated = YLeaf(YType.boolean, "is-nonnegotiated")

                    self.known = YLeaf(YType.boolean, "known")

                    self.priority = YLeaf(YType.uint8, "priority")

                    self.ptsf_loss_announce = YLeaf(YType.uint8, "ptsf-loss-announce")

                    self.ptsf_loss_sync = YLeaf(YType.uint8, "ptsf-loss-sync")

                    self.qualified = YLeaf(YType.boolean, "qualified")

                    self.address = Ptp.Interfaces.Interface.MasterTable.Address()
                    self.address.parent = self
                    self._children_name_map["address"] = "address"
                    self._children_yang_names.add("address")
                    self._segment_path = lambda: "master-table"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Interfaces.Interface.MasterTable, ['communication_model', 'is_grandmaster', 'is_nonnegotiated', 'known', 'priority', 'ptsf_loss_announce', 'ptsf_loss_sync', 'qualified'], name, value)


                class Address(Entity):
                    """
                    The address of the master clock
                    
                    .. attribute:: address_unknown
                    
                    	Unknown address type
                    	**type**\:  bool
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address>`
                    
                    .. attribute:: mac_address
                    
                    	Ethernet MAC address
                    	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Interfaces.Interface.MasterTable.Address.MacAddress>`
                    
                    

                    """

                    _prefix = 'ptp-oper'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Interfaces.Interface.MasterTable.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "master-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.Interfaces.Interface.MasterTable.Address.MacAddress)}
                        self._child_list_classes = {}

                        self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = Ptp.Interfaces.Interface.MasterTable.Address.Ipv6Address()
                        self.ipv6_address.parent = self
                        self._children_name_map["ipv6_address"] = "ipv6-address"
                        self._children_yang_names.add("ipv6-address")

                        self.mac_address = Ptp.Interfaces.Interface.MasterTable.Address.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")
                        self._segment_path = lambda: "address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Interfaces.Interface.MasterTable.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                    class Ipv6Address(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
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


                    class MacAddress(Entity):
                        """
                        Ethernet MAC address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
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


    class LeapSeconds(Entity):
        """
        Upcoming leap\-seconds information
        
        .. attribute:: current_offset
        
        	The current UTC offset, in seconds
        	**type**\:  int
        
        	**range:** \-32768..32767
        
        	**units**\: second
        
        .. attribute:: leap_second
        
        	The list of upcoming leap second updates
        	**type**\: list of    :py:class:`LeapSecond <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LeapSeconds.LeapSecond>`
        
        .. attribute:: offset_valid
        
        	Is the current UTC offset known to be valid?
        	**type**\:  bool
        
        .. attribute:: polling_frequency
        
        	Source file polling frequency, in days
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: day
        
        .. attribute:: source_expiry_date
        
        	Source file expiry timestamp, in seconds since UNIX epoch
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: source_file
        
        	The URL of the file containing upcoming leap seconds
        	**type**\:  str
        
        	**units**\: second
        
        

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

            self.polling_frequency = YLeaf(YType.uint32, "polling-frequency")

            self.source_expiry_date = YLeaf(YType.uint32, "source-expiry-date")

            self.source_file = YLeaf(YType.str, "source-file")

            self.leap_second = YList(self)
            self._segment_path = lambda: "leap-seconds"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.LeapSeconds, ['current_offset', 'offset_valid', 'polling_frequency', 'source_expiry_date', 'source_file'], name, value)


        class LeapSecond(Entity):
            """
            The list of upcoming leap second updates
            
            .. attribute:: offset
            
            	The UTC offset (TAI \- UTC), in seconds
            	**type**\:  int
            
            	**range:** \-32768..32767
            
            	**units**\: second
            
            .. attribute:: offset_applied
            
            	Indicates whether the offset has been applied
            	**type**\:  bool
            
            .. attribute:: offset_start_date
            
            	The UNIX timestamp at which the offset becomes valid
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

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

                self.offset_applied = YLeaf(YType.boolean, "offset-applied")

                self.offset_start_date = YLeaf(YType.uint64, "offset-start-date")
                self._segment_path = lambda: "leap-second"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/leap-seconds/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LeapSeconds.LeapSecond, ['offset', 'offset_applied', 'offset_start_date'], name, value)


    class LocalClock(Entity):
        """
        Local clock operational data
        
        .. attribute:: clock_properties
        
        	Local clock
        	**type**\:   :py:class:`ClockProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties>`
        
        .. attribute:: domain
        
        	The PTP domain of the local clock
        	**type**\:  int
        
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
            
            .. attribute:: accuracy
            
            	Accuracy
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: class_
            
            	Class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_id
            
            	Clock ID
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: configured_clock_class
            
            	The configured clock class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: configured_priority
            
            	The configured priority
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frequency_traceable
            
            	The clock is frequency traceable
            	**type**\:  bool
            
            .. attribute:: leap_seconds
            
            	Leap Seconds
            	**type**\:   :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
            
            	**units**\: second
            
            .. attribute:: local
            
            	The clock is the local clock
            	**type**\:  bool
            
            .. attribute:: offset_log_variance
            
            	Offset log variance
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority1
            
            	Priority 1
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: priority2
            
            	Priority 2
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: receiver
            
            	Receiver
            	**type**\:   :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Receiver>`
            
            .. attribute:: sender
            
            	Sender
            	**type**\:   :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.Sender>`
            
            .. attribute:: steps_removed
            
            	Steps removed
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: time_source
            
            	Time source
            	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
            
            .. attribute:: time_traceable
            
            	The clock is time traceable
            	**type**\:  bool
            
            .. attribute:: timescale
            
            	Timescale
            	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
            
            .. attribute:: utc_offset
            
            	UTC offset
            	**type**\:   :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.LocalClock.ClockProperties.UtcOffset>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.LocalClock.ClockProperties, self).__init__()

                self.yang_name = "clock-properties"
                self.yang_parent_name = "local-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"receiver" : ("receiver", Ptp.LocalClock.ClockProperties.Receiver), "sender" : ("sender", Ptp.LocalClock.ClockProperties.Sender), "utc-offset" : ("utc_offset", Ptp.LocalClock.ClockProperties.UtcOffset)}
                self._child_list_classes = {}

                self.accuracy = YLeaf(YType.uint8, "accuracy")

                self.class_ = YLeaf(YType.uint8, "class")

                self.clock_id = YLeaf(YType.uint64, "clock-id")

                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                self.local = YLeaf(YType.boolean, "local")

                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                self.priority1 = YLeaf(YType.uint8, "priority1")

                self.priority2 = YLeaf(YType.uint8, "priority2")

                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                self.time_source = YLeaf(YType.enumeration, "time-source")

                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                self.timescale = YLeaf(YType.enumeration, "timescale")

                self.receiver = Ptp.LocalClock.ClockProperties.Receiver()
                self.receiver.parent = self
                self._children_name_map["receiver"] = "receiver"
                self._children_yang_names.add("receiver")

                self.sender = Ptp.LocalClock.ClockProperties.Sender()
                self.sender.parent = self
                self._children_name_map["sender"] = "sender"
                self._children_yang_names.add("sender")

                self.utc_offset = Ptp.LocalClock.ClockProperties.UtcOffset()
                self.utc_offset.parent = self
                self._children_name_map["utc_offset"] = "utc-offset"
                self._children_yang_names.add("utc-offset")
                self._segment_path = lambda: "clock-properties"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/local-clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.LocalClock.ClockProperties, ['accuracy', 'class_', 'clock_id', 'configured_clock_class', 'configured_priority', 'frequency_traceable', 'leap_seconds', 'local', 'offset_log_variance', 'priority1', 'priority2', 'steps_removed', 'time_source', 'time_traceable', 'timescale'], name, value)


            class Receiver(Entity):
                """
                Receiver
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_number
                
                	Port number
                	**type**\:  int
                
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


            class UtcOffset(Entity):
                """
                UTC offset
                
                .. attribute:: current_offset
                
                	Current offset
                	**type**\:  int
                
                	**range:** \-32768..32767
                
                .. attribute:: offset_valid
                
                	The current offset is valid
                	**type**\:  bool
                
                

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


    class Nodes(Entity):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific operational data for a given node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node>`
        
        

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
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: node_interface_foreign_masters
            
            	Table for node foreign master clock operational data
            	**type**\:   :py:class:`NodeInterfaceForeignMasters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters>`
            
            .. attribute:: node_interface_unicast_peers
            
            	Table for node unicast peers operational data
            	**type**\:   :py:class:`NodeInterfaceUnicastPeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers>`
            
            .. attribute:: node_interfaces
            
            	Table for node interface operational data
            	**type**\:   :py:class:`NodeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces>`
            
            .. attribute:: packet_counters
            
            	Node packet counter operational data
            	**type**\:   :py:class:`PacketCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters>`
            
            .. attribute:: summary
            
            	Node summary operational data
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'ptp-oper'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-interface-foreign-masters" : ("node_interface_foreign_masters", Ptp.Nodes.Node.NodeInterfaceForeignMasters), "node-interface-unicast-peers" : ("node_interface_unicast_peers", Ptp.Nodes.Node.NodeInterfaceUnicastPeers), "node-interfaces" : ("node_interfaces", Ptp.Nodes.Node.NodeInterfaces), "packet-counters" : ("packet_counters", Ptp.Nodes.Node.PacketCounters), "summary" : ("summary", Ptp.Nodes.Node.Summary)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.node_interface_foreign_masters = Ptp.Nodes.Node.NodeInterfaceForeignMasters()
                self.node_interface_foreign_masters.parent = self
                self._children_name_map["node_interface_foreign_masters"] = "node-interface-foreign-masters"
                self._children_yang_names.add("node-interface-foreign-masters")

                self.node_interface_unicast_peers = Ptp.Nodes.Node.NodeInterfaceUnicastPeers()
                self.node_interface_unicast_peers.parent = self
                self._children_name_map["node_interface_unicast_peers"] = "node-interface-unicast-peers"
                self._children_yang_names.add("node-interface-unicast-peers")

                self.node_interfaces = Ptp.Nodes.Node.NodeInterfaces()
                self.node_interfaces.parent = self
                self._children_name_map["node_interfaces"] = "node-interfaces"
                self._children_yang_names.add("node-interfaces")

                self.packet_counters = Ptp.Nodes.Node.PacketCounters()
                self.packet_counters.parent = self
                self._children_name_map["packet_counters"] = "packet-counters"
                self._children_yang_names.add("packet-counters")

                self.summary = Ptp.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
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
                	**type**\: list of    :py:class:`NodeInterfaceForeignMaster <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster>`
                
                

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
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: foreign_clock
                    
                    	Foreign clocks received on this interface
                    	**type**\: list of    :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock>`
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

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
                        
                        .. attribute:: address
                        
                        	The address of the clock
                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address>`
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:   :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant>`
                        
                        .. attribute:: communication_model
                        
                        	The communication model configured on this clock
                        	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        .. attribute:: configured_clock_class
                        
                        	Clock class configured for the clock, if any
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: configured_priority
                        
                        	Priority configured for the clock, if any
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: delay_asymmetry
                        
                        	Delay asymmetry configured for the clock, if any
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:   :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant>`
                        
                        .. attribute:: foreign_clock
                        
                        	Foreign clock information
                        	**type**\:   :py:class:`ForeignClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock>`
                        
                        .. attribute:: foreign_domain
                        
                        	The PTP domain that the foreign clock is in
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_grandmaster
                        
                        	This clock is the currently selected grand master clock
                        	**type**\:  bool
                        
                        .. attribute:: is_known
                        
                        	This clock is known by this router
                        	**type**\:  bool
                        
                        .. attribute:: is_qualified
                        
                        	The clock is qualified for best master clock selection
                        	**type**\:  bool
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\:  bool
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\:  bool
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:   :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant>`
                        
                        .. attribute:: time_known_for
                        
                        	How long the clock has been known by this router for, in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, self).__init__()

                            self.yang_name = "foreign-clock"
                            self.yang_parent_name = "node-interface-foreign-master"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address" : ("address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address), "announce-grant" : ("announce_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant), "delay-response-grant" : ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant), "foreign-clock" : ("foreign_clock", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock), "sync-grant" : ("sync_grant", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant)}
                            self._child_list_classes = {}

                            self.communication_model = YLeaf(YType.enumeration, "communication-model")

                            self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                            self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                            self.delay_asymmetry = YLeaf(YType.int32, "delay-asymmetry")

                            self.foreign_domain = YLeaf(YType.uint8, "foreign-domain")

                            self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                            self.is_known = YLeaf(YType.boolean, "is-known")

                            self.is_qualified = YLeaf(YType.boolean, "is-qualified")

                            self.ptsf_loss_announce = YLeaf(YType.boolean, "ptsf-loss-announce")

                            self.ptsf_loss_sync = YLeaf(YType.boolean, "ptsf-loss-sync")

                            self.time_known_for = YLeaf(YType.uint32, "time-known-for")

                            self.address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"
                            self._children_yang_names.add("announce-grant")

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._children_yang_names.add("delay-response-grant")

                            self.foreign_clock = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock()
                            self.foreign_clock.parent = self
                            self._children_name_map["foreign_clock"] = "foreign-clock"
                            self._children_yang_names.add("foreign-clock")

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"
                            self._children_yang_names.add("sync-grant")
                            self._segment_path = lambda: "foreign-clock"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock, ['communication_model', 'configured_clock_class', 'configured_priority', 'delay_asymmetry', 'foreign_domain', 'is_grandmaster', 'is_known', 'is_qualified', 'ptsf_loss_announce', 'ptsf_loss_sync', 'time_known_for'], name, value)


                        class Address(Entity):
                            """
                            The address of the clock
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\:  bool
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address>`
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress>`
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress)}
                                self._child_list_classes = {}

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\:  str
                                
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


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\:  str
                                
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


                        class AnnounceGrant(Entity):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "announce-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.AnnounceGrant, ['grant_duration', 'log_grant_interval'], name, value)


                        class DelayResponseGrant(Entity):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "delay-response-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.DelayResponseGrant, ['grant_duration', 'log_grant_interval'], name, value)


                        class ForeignClock(Entity):
                            """
                            Foreign clock information
                            
                            .. attribute:: accuracy
                            
                            	Accuracy
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: class_
                            
                            	Class
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: configured_clock_class
                            
                            	The configured clock class
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: configured_priority
                            
                            	The configured priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: frequency_traceable
                            
                            	The clock is frequency traceable
                            	**type**\:  bool
                            
                            .. attribute:: leap_seconds
                            
                            	Leap Seconds
                            	**type**\:   :py:class:`PtpBagClockLeapSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockLeapSeconds>`
                            
                            	**units**\: second
                            
                            .. attribute:: local
                            
                            	The clock is the local clock
                            	**type**\:  bool
                            
                            .. attribute:: offset_log_variance
                            
                            	Offset log variance
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority1
                            
                            	Priority 1
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: priority2
                            
                            	Priority 2
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: receiver
                            
                            	Receiver
                            	**type**\:   :py:class:`Receiver <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver>`
                            
                            .. attribute:: sender
                            
                            	Sender
                            	**type**\:   :py:class:`Sender <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender>`
                            
                            .. attribute:: steps_removed
                            
                            	Steps removed
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: time_source
                            
                            	Time source
                            	**type**\:   :py:class:`PtpBagClockTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimeSource>`
                            
                            .. attribute:: time_traceable
                            
                            	The clock is time traceable
                            	**type**\:  bool
                            
                            .. attribute:: timescale
                            
                            	Timescale
                            	**type**\:   :py:class:`PtpBagClockTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagClockTimescale>`
                            
                            .. attribute:: utc_offset
                            
                            	UTC offset
                            	**type**\:   :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset>`
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock, self).__init__()

                                self.yang_name = "foreign-clock"
                                self.yang_parent_name = "foreign-clock"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"receiver" : ("receiver", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver), "sender" : ("sender", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender), "utc-offset" : ("utc_offset", Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset)}
                                self._child_list_classes = {}

                                self.accuracy = YLeaf(YType.uint8, "accuracy")

                                self.class_ = YLeaf(YType.uint8, "class")

                                self.clock_id = YLeaf(YType.uint64, "clock-id")

                                self.configured_clock_class = YLeaf(YType.uint8, "configured-clock-class")

                                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                                self.frequency_traceable = YLeaf(YType.boolean, "frequency-traceable")

                                self.leap_seconds = YLeaf(YType.enumeration, "leap-seconds")

                                self.local = YLeaf(YType.boolean, "local")

                                self.offset_log_variance = YLeaf(YType.uint16, "offset-log-variance")

                                self.priority1 = YLeaf(YType.uint8, "priority1")

                                self.priority2 = YLeaf(YType.uint8, "priority2")

                                self.steps_removed = YLeaf(YType.uint16, "steps-removed")

                                self.time_source = YLeaf(YType.enumeration, "time-source")

                                self.time_traceable = YLeaf(YType.boolean, "time-traceable")

                                self.timescale = YLeaf(YType.enumeration, "timescale")

                                self.receiver = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Receiver()
                                self.receiver.parent = self
                                self._children_name_map["receiver"] = "receiver"
                                self._children_yang_names.add("receiver")

                                self.sender = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.Sender()
                                self.sender.parent = self
                                self._children_name_map["sender"] = "sender"
                                self._children_yang_names.add("sender")

                                self.utc_offset = Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock.UtcOffset()
                                self.utc_offset.parent = self
                                self._children_name_map["utc_offset"] = "utc-offset"
                                self._children_yang_names.add("utc-offset")
                                self._segment_path = lambda: "foreign-clock"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.ForeignClock, ['accuracy', 'class_', 'clock_id', 'configured_clock_class', 'configured_priority', 'frequency_traceable', 'leap_seconds', 'local', 'offset_log_variance', 'priority1', 'priority2', 'steps_removed', 'time_source', 'time_traceable', 'timescale'], name, value)


                            class Receiver(Entity):
                                """
                                Receiver
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\:  int
                                
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
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: port_number
                                
                                	Port number
                                	**type**\:  int
                                
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


                            class UtcOffset(Entity):
                                """
                                UTC offset
                                
                                .. attribute:: current_offset
                                
                                	Current offset
                                	**type**\:  int
                                
                                	**range:** \-32768..32767
                                
                                .. attribute:: offset_valid
                                
                                	The current offset is valid
                                	**type**\:  bool
                                
                                

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


                        class SyncGrant(Entity):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "sync-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceForeignMasters.NodeInterfaceForeignMaster.ForeignClock.SyncGrant, ['grant_duration', 'log_grant_interval'], name, value)


            class NodeInterfaceUnicastPeers(Entity):
                """
                Table for node unicast peers operational data
                
                .. attribute:: node_interface_unicast_peer
                
                	Node interface unicast peers operational data
                	**type**\: list of    :py:class:`NodeInterfaceUnicastPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer>`
                
                

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
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: peers
                    
                    	Unicast Peers
                    	**type**\: list of    :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers>`
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

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
                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address>`
                        
                        .. attribute:: announce_grant
                        
                        	Unicast grant information for announce messages
                        	**type**\:   :py:class:`AnnounceGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant>`
                        
                        .. attribute:: delay_response_grant
                        
                        	Unicast grant information for delay\-response messages
                        	**type**\:   :py:class:`DelayResponseGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant>`
                        
                        .. attribute:: sync_grant
                        
                        	Unicast grant information for sync messages
                        	**type**\:   :py:class:`SyncGrant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant>`
                        
                        

                        """

                        _prefix = 'ptp-oper'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers, self).__init__()

                            self.yang_name = "peers"
                            self.yang_parent_name = "node-interface-unicast-peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address" : ("address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address), "announce-grant" : ("announce_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant), "delay-response-grant" : ("delay_response_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant), "sync-grant" : ("sync_grant", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant)}
                            self._child_list_classes = {}

                            self.address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")

                            self.announce_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant()
                            self.announce_grant.parent = self
                            self._children_name_map["announce_grant"] = "announce-grant"
                            self._children_yang_names.add("announce-grant")

                            self.delay_response_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant()
                            self.delay_response_grant.parent = self
                            self._children_name_map["delay_response_grant"] = "delay-response-grant"
                            self._children_yang_names.add("delay-response-grant")

                            self.sync_grant = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant()
                            self.sync_grant.parent = self
                            self._children_name_map["sync_grant"] = "sync-grant"
                            self._children_yang_names.add("sync-grant")
                            self._segment_path = lambda: "peers"


                        class Address(Entity):
                            """
                            The address of the unicast peer
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\:  bool
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address>`
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress>`
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "peers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress)}
                                self._child_list_classes = {}

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\:  str
                                
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


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\:  str
                                
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


                        class AnnounceGrant(Entity):
                            """
                            Unicast grant information for announce messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "announce-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.AnnounceGrant, ['grant_duration', 'log_grant_interval'], name, value)


                        class DelayResponseGrant(Entity):
                            """
                            Unicast grant information for delay\-response
                            messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "delay-response-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.DelayResponseGrant, ['grant_duration', 'log_grant_interval'], name, value)


                        class SyncGrant(Entity):
                            """
                            Unicast grant information for sync messages
                            
                            .. attribute:: grant_duration
                            
                            	Duraction of the grant
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: log_grant_interval
                            
                            	Log of the interval which has been granted
                            	**type**\:  int
                            
                            	**range:** \-128..127
                            
                            

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

                                self.grant_duration = YLeaf(YType.uint32, "grant-duration")

                                self.log_grant_interval = YLeaf(YType.int8, "log-grant-interval")
                                self._segment_path = lambda: "sync-grant"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaceUnicastPeers.NodeInterfaceUnicastPeer.Peers.SyncGrant, ['grant_duration', 'log_grant_interval'], name, value)


            class NodeInterfaces(Entity):
                """
                Table for node interface operational data
                
                .. attribute:: node_interface
                
                	Node interface operational data
                	**type**\: list of    :py:class:`NodeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface>`
                
                

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
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: announce_timeout
                    
                    	Announce timeout
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: communication_model
                    
                    	Communication model configured on the interface
                    	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                    
                    .. attribute:: configured_port_state
                    
                    	The configured port state
                    	**type**\:   :py:class:`PtpBagRestrictPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagRestrictPortState>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation
                    	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                    
                    .. attribute:: event_cos
                    
                    	The class of service used on the interface for event messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_dscp
                    
                    	The DSCP class used on the interface for event messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: general_cos
                    
                    	The class of service used on the interface for general messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: general_dscp
                    
                    	The DSCP class used on the interface for general messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address, if IPv4 encapsulation is being used
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	Ipv6 address, if IPv6 encapsulation is being used
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: line_state
                    
                    	Line state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_priority
                    
                    	Local priority, for the G.8275.1 PTP profile
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: log_announce_interval
                    
                    	Log of the interface's announce interval
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: log_min_delay_request_interval
                    
                    	Log of the interface's Minimum delay\-request interval
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: log_sync_interval
                    
                    	Log of the interface's sync interval
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: mac_address
                    
                    	MAC address, if Ethernet encapsulation is being used
                    	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress>`
                    
                    .. attribute:: master_table
                    
                    	The interface's master table
                    	**type**\: list of    :py:class:`MasterTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable>`
                    
                    .. attribute:: max_sync_rate
                    
                    	The maximum rate of sync packets on the interface
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: port_number
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_state
                    
                    	Port state
                    	**type**\:   :py:class:`PtpBagPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagPortState>`
                    
                    .. attribute:: signal_fail
                    
                    	Signal fail status of the interface
                    	**type**\:  bool
                    
                    .. attribute:: supports_ethernet
                    
                    	The interface supports ethernet transport
                    	**type**\:  bool
                    
                    .. attribute:: supports_ipv6
                    
                    	The interface supports IPv6 transport
                    	**type**\:  bool
                    
                    .. attribute:: supports_multicast
                    
                    	The interface supports multicast
                    	**type**\:  bool
                    
                    .. attribute:: supports_one_step
                    
                    	The interface supports one\-step operation
                    	**type**\:  bool
                    
                    .. attribute:: supports_slave
                    
                    	The interface supports operation in slave mode
                    	**type**\:  bool
                    
                    .. attribute:: supports_source_ip
                    
                    	The interface supports source ip configuration
                    	**type**\:  bool
                    
                    .. attribute:: supports_two_step
                    
                    	The interface supports two\-step operation
                    	**type**\:  bool
                    
                    .. attribute:: two_step
                    
                    	Two step delay\-request mechanism is being used
                    	**type**\:  bool
                    
                    .. attribute:: unicast_peers
                    
                    	The number of unicast peers known by the interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

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

                        self.announce_timeout = YLeaf(YType.uint32, "announce-timeout")

                        self.communication_model = YLeaf(YType.enumeration, "communication-model")

                        self.configured_port_state = YLeaf(YType.enumeration, "configured-port-state")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.event_cos = YLeaf(YType.uint32, "event-cos")

                        self.event_dscp = YLeaf(YType.uint32, "event-dscp")

                        self.general_cos = YLeaf(YType.uint32, "general-cos")

                        self.general_dscp = YLeaf(YType.uint32, "general-dscp")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.line_state = YLeaf(YType.uint32, "line-state")

                        self.local_priority = YLeaf(YType.uint8, "local-priority")

                        self.log_announce_interval = YLeaf(YType.int32, "log-announce-interval")

                        self.log_min_delay_request_interval = YLeaf(YType.int32, "log-min-delay-request-interval")

                        self.log_sync_interval = YLeaf(YType.int32, "log-sync-interval")

                        self.max_sync_rate = YLeaf(YType.uint8, "max-sync-rate")

                        self.port_number = YLeaf(YType.uint16, "port-number")

                        self.port_state = YLeaf(YType.enumeration, "port-state")

                        self.signal_fail = YLeaf(YType.boolean, "signal-fail")

                        self.supports_ethernet = YLeaf(YType.boolean, "supports-ethernet")

                        self.supports_ipv6 = YLeaf(YType.boolean, "supports-ipv6")

                        self.supports_multicast = YLeaf(YType.boolean, "supports-multicast")

                        self.supports_one_step = YLeaf(YType.boolean, "supports-one-step")

                        self.supports_slave = YLeaf(YType.boolean, "supports-slave")

                        self.supports_source_ip = YLeaf(YType.boolean, "supports-source-ip")

                        self.supports_two_step = YLeaf(YType.boolean, "supports-two-step")

                        self.two_step = YLeaf(YType.boolean, "two-step")

                        self.unicast_peers = YLeaf(YType.uint32, "unicast-peers")

                        self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MacAddress()
                        self.mac_address.parent = self
                        self._children_name_map["mac_address"] = "mac-address"
                        self._children_yang_names.add("mac-address")

                        self.master_table = YList(self)
                        self._segment_path = lambda: "node-interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface, ['interface_name', 'announce_timeout', 'communication_model', 'configured_port_state', 'encapsulation', 'event_cos', 'event_dscp', 'general_cos', 'general_dscp', 'ipv4_address', 'ipv6_address', 'line_state', 'local_priority', 'log_announce_interval', 'log_min_delay_request_interval', 'log_sync_interval', 'max_sync_rate', 'port_number', 'port_state', 'signal_fail', 'supports_ethernet', 'supports_ipv6', 'supports_multicast', 'supports_one_step', 'supports_slave', 'supports_source_ip', 'supports_two_step', 'two_step', 'unicast_peers'], name, value)


                    class MacAddress(Entity):
                        """
                        MAC address, if Ethernet encapsulation is being
                        used
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
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
                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address>`
                        
                        .. attribute:: communication_model
                        
                        	The configured communication model of the master clock
                        	**type**\:   :py:class:`PtpBagCommunicationModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagCommunicationModel>`
                        
                        .. attribute:: is_grandmaster
                        
                        	Whether this is the grandmaster
                        	**type**\:  bool
                        
                        .. attribute:: is_nonnegotiated
                        
                        	Whether this master uses non\-negotiated unicast
                        	**type**\:  bool
                        
                        .. attribute:: known
                        
                        	Whether the interface is receiving messages from this master
                        	**type**\:  bool
                        
                        .. attribute:: priority
                        
                        	The priority of the master clock, if it is set
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ptsf_loss_announce
                        
                        	Announced messages are not being received from the master
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ptsf_loss_sync
                        
                        	Sync messages are not being received from the master
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: qualified
                        
                        	The master is qualified for best master clock selection
                        	**type**\:  bool
                        
                        

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

                            self.is_grandmaster = YLeaf(YType.boolean, "is-grandmaster")

                            self.is_nonnegotiated = YLeaf(YType.boolean, "is-nonnegotiated")

                            self.known = YLeaf(YType.boolean, "known")

                            self.priority = YLeaf(YType.uint8, "priority")

                            self.ptsf_loss_announce = YLeaf(YType.uint8, "ptsf-loss-announce")

                            self.ptsf_loss_sync = YLeaf(YType.uint8, "ptsf-loss-sync")

                            self.qualified = YLeaf(YType.boolean, "qualified")

                            self.address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._children_yang_names.add("address")
                            self._segment_path = lambda: "master-table"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable, ['communication_model', 'is_grandmaster', 'is_nonnegotiated', 'known', 'priority', 'ptsf_loss_announce', 'ptsf_loss_sync', 'qualified'], name, value)


                        class Address(Entity):
                            """
                            The address of the master clock
                            
                            .. attribute:: address_unknown
                            
                            	Unknown address type
                            	**type**\:  bool
                            
                            .. attribute:: encapsulation
                            
                            	Encapsulation
                            	**type**\:   :py:class:`PtpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.PtpBagEncap>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address>`
                            
                            .. attribute:: mac_address
                            
                            	Ethernet MAC address
                            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress>`
                            
                            

                            """

                            _prefix = 'ptp-oper'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "master-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipv6-address" : ("ipv6_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address), "mac-address" : ("mac_address", Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress)}
                                self._child_list_classes = {}

                                self.address_unknown = YLeaf(YType.boolean, "address-unknown")

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.Ipv6Address()
                                self.ipv6_address.parent = self
                                self._children_name_map["ipv6_address"] = "ipv6-address"
                                self._children_yang_names.add("ipv6-address")

                                self.mac_address = Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address.MacAddress()
                                self.mac_address.parent = self
                                self._children_name_map["mac_address"] = "mac-address"
                                self._children_yang_names.add("mac-address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Nodes.Node.NodeInterfaces.NodeInterface.MasterTable.Address, ['address_unknown', 'encapsulation', 'ipv4_address'], name, value)


                            class Ipv6Address(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 Address
                                	**type**\:  str
                                
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


                            class MacAddress(Entity):
                                """
                                Ethernet MAC address
                                
                                .. attribute:: macaddr
                                
                                	macaddr
                                	**type**\:  str
                                
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


            class PacketCounters(Entity):
                """
                Node packet counter operational data
                
                .. attribute:: counters
                
                	Packet counters
                	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.Counters>`
                
                .. attribute:: drop_reasons
                
                	Drop reasons
                	**type**\:   :py:class:`DropReasons <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Nodes.Node.PacketCounters.DropReasons>`
                
                

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
                    
                    .. attribute:: announce_dropped
                    
                    	Number of announce packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_received
                    
                    	Number of announce packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: announce_sent
                    
                    	Number of announce packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_dropped
                    
                    	Number of delay\-request packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_received
                    
                    	Number of delay\-request packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_request_sent
                    
                    	Number of delay\-request packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_dropped
                    
                    	Number of delay\-response packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_received
                    
                    	Number of delay\-response packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_response_sent
                    
                    	Number of delay\-response packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_dropped
                    
                    	Number of follow\-up packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_received
                    
                    	Number of follow\-up packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: follow_up_sent
                    
                    	Number of follow\-up packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_dropped
                    
                    	Number of management messages dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_received
                    
                    	Number of management messages received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: management_sent
                    
                    	Number of management messages sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_dropped
                    
                    	Number of other packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_received
                    
                    	Number of other packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: other_packets_sent
                    
                    	Number of other packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_dropped
                    
                    	Number of peer\-delay\-request packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_received
                    
                    	Number of peer\-delay\-request packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_request_sent
                    
                    	Number of peer\-delay\-request packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_dropped
                    
                    	Number of peer\-delay\-response packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_dropped
                    
                    	Number of peer\-delay\-response follow\-up packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_received
                    
                    	Number of peer\-delay\-response follow\-up packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_follow_up_sent
                    
                    	Number of peer\-delay\-response follow\-up packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_received
                    
                    	Number of peer\-delay\-response packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_delay_response_sent
                    
                    	Number of peer\-delay\-response packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_dropped
                    
                    	Number of signaling packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_received
                    
                    	Number of signaling packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: signaling_sent
                    
                    	Number of signaling packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_dropped
                    
                    	Number of sync packetsdropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_received
                    
                    	Number of sync packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_sent
                    
                    	Number of sync packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_dropped
                    
                    	Total number of packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_received
                    
                    	Total number of packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_sent
                    
                    	Total number of packets sent
                    	**type**\:  int
                    
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

                        self.announce_dropped = YLeaf(YType.uint32, "announce-dropped")

                        self.announce_received = YLeaf(YType.uint32, "announce-received")

                        self.announce_sent = YLeaf(YType.uint32, "announce-sent")

                        self.delay_request_dropped = YLeaf(YType.uint32, "delay-request-dropped")

                        self.delay_request_received = YLeaf(YType.uint32, "delay-request-received")

                        self.delay_request_sent = YLeaf(YType.uint32, "delay-request-sent")

                        self.delay_response_dropped = YLeaf(YType.uint32, "delay-response-dropped")

                        self.delay_response_received = YLeaf(YType.uint32, "delay-response-received")

                        self.delay_response_sent = YLeaf(YType.uint32, "delay-response-sent")

                        self.follow_up_dropped = YLeaf(YType.uint32, "follow-up-dropped")

                        self.follow_up_received = YLeaf(YType.uint32, "follow-up-received")

                        self.follow_up_sent = YLeaf(YType.uint32, "follow-up-sent")

                        self.management_dropped = YLeaf(YType.uint32, "management-dropped")

                        self.management_received = YLeaf(YType.uint32, "management-received")

                        self.management_sent = YLeaf(YType.uint32, "management-sent")

                        self.other_packets_dropped = YLeaf(YType.uint32, "other-packets-dropped")

                        self.other_packets_received = YLeaf(YType.uint32, "other-packets-received")

                        self.other_packets_sent = YLeaf(YType.uint32, "other-packets-sent")

                        self.peer_delay_request_dropped = YLeaf(YType.uint32, "peer-delay-request-dropped")

                        self.peer_delay_request_received = YLeaf(YType.uint32, "peer-delay-request-received")

                        self.peer_delay_request_sent = YLeaf(YType.uint32, "peer-delay-request-sent")

                        self.peer_delay_response_dropped = YLeaf(YType.uint32, "peer-delay-response-dropped")

                        self.peer_delay_response_follow_up_dropped = YLeaf(YType.uint32, "peer-delay-response-follow-up-dropped")

                        self.peer_delay_response_follow_up_received = YLeaf(YType.uint32, "peer-delay-response-follow-up-received")

                        self.peer_delay_response_follow_up_sent = YLeaf(YType.uint32, "peer-delay-response-follow-up-sent")

                        self.peer_delay_response_received = YLeaf(YType.uint32, "peer-delay-response-received")

                        self.peer_delay_response_sent = YLeaf(YType.uint32, "peer-delay-response-sent")

                        self.signaling_dropped = YLeaf(YType.uint32, "signaling-dropped")

                        self.signaling_received = YLeaf(YType.uint32, "signaling-received")

                        self.signaling_sent = YLeaf(YType.uint32, "signaling-sent")

                        self.sync_dropped = YLeaf(YType.uint32, "sync-dropped")

                        self.sync_received = YLeaf(YType.uint32, "sync-received")

                        self.sync_sent = YLeaf(YType.uint32, "sync-sent")

                        self.total_packets_dropped = YLeaf(YType.uint32, "total-packets-dropped")

                        self.total_packets_received = YLeaf(YType.uint32, "total-packets-received")

                        self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.Counters, ['announce_dropped', 'announce_received', 'announce_sent', 'delay_request_dropped', 'delay_request_received', 'delay_request_sent', 'delay_response_dropped', 'delay_response_received', 'delay_response_sent', 'follow_up_dropped', 'follow_up_received', 'follow_up_sent', 'management_dropped', 'management_received', 'management_sent', 'other_packets_dropped', 'other_packets_received', 'other_packets_sent', 'peer_delay_request_dropped', 'peer_delay_request_received', 'peer_delay_request_sent', 'peer_delay_response_dropped', 'peer_delay_response_follow_up_dropped', 'peer_delay_response_follow_up_received', 'peer_delay_response_follow_up_sent', 'peer_delay_response_received', 'peer_delay_response_sent', 'signaling_dropped', 'signaling_received', 'signaling_sent', 'sync_dropped', 'sync_received', 'sync_sent', 'total_packets_dropped', 'total_packets_received', 'total_packets_sent'], name, value)


                class DropReasons(Entity):
                    """
                    Drop reasons
                    
                    .. attribute:: g8275_1_incompatible
                    
                    	Packet not compatible with G.8275.1 profile
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g8275_2_incompatible
                    
                    	Packet not compatible with G.8275.2 profile
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_packet
                    
                    	Invalid packet or packet metadata
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_tl_vs
                    
                    	Invalid TLVs received in packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_higher_port
                    
                    	Local packet received, higher port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_lower_port
                    
                    	Local packet received, lower port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: looped_same_port
                    
                    	Local packet received, same port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_clock_class
                    
                    	Clock class below minimum
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_offload_session
                    
                    	No offload session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_timestamp
                    
                    	No timestamp received with packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_for_us
                    
                    	Packet not for us
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_granted
                    
                    	Packet from peer not granted unicast
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_listening
                    
                    	Not listening for packets on this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_master
                    
                    	Packet only handled in Master state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_ready
                    
                    	Not ready for packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_slave
                    
                    	Packet only handled in Slave state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_supported
                    
                    	PTP packet type not supported
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: too_short
                    
                    	Packet too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: too_slow
                    
                    	Packet received too late
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_master
                    
                    	Packet from unknown master
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_domain
                    
                    	Wrong domain number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_master
                    
                    	Packet from incorrect master
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wrong_sequence_id
                    
                    	Unexpected sequence ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: zero_timestamp
                    
                    	Zero timestamp received with packet
                    	**type**\:  int
                    
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

                        self.g8275_1_incompatible = YLeaf(YType.uint32, "g8275-1-incompatible")

                        self.g8275_2_incompatible = YLeaf(YType.uint32, "g8275-2-incompatible")

                        self.invalid_packet = YLeaf(YType.uint32, "invalid-packet")

                        self.invalid_tl_vs = YLeaf(YType.uint32, "invalid-tl-vs")

                        self.looped_higher_port = YLeaf(YType.uint32, "looped-higher-port")

                        self.looped_lower_port = YLeaf(YType.uint32, "looped-lower-port")

                        self.looped_same_port = YLeaf(YType.uint32, "looped-same-port")

                        self.min_clock_class = YLeaf(YType.uint32, "min-clock-class")

                        self.no_offload_session = YLeaf(YType.uint32, "no-offload-session")

                        self.no_timestamp = YLeaf(YType.uint32, "no-timestamp")

                        self.not_for_us = YLeaf(YType.uint32, "not-for-us")

                        self.not_granted = YLeaf(YType.uint32, "not-granted")

                        self.not_listening = YLeaf(YType.uint32, "not-listening")

                        self.not_master = YLeaf(YType.uint32, "not-master")

                        self.not_ready = YLeaf(YType.uint32, "not-ready")

                        self.not_slave = YLeaf(YType.uint32, "not-slave")

                        self.not_supported = YLeaf(YType.uint32, "not-supported")

                        self.too_short = YLeaf(YType.uint32, "too-short")

                        self.too_slow = YLeaf(YType.uint32, "too-slow")

                        self.unknown_master = YLeaf(YType.uint32, "unknown-master")

                        self.wrong_domain = YLeaf(YType.uint32, "wrong-domain")

                        self.wrong_master = YLeaf(YType.uint32, "wrong-master")

                        self.wrong_sequence_id = YLeaf(YType.uint32, "wrong-sequence-id")

                        self.zero_timestamp = YLeaf(YType.uint32, "zero-timestamp")
                        self._segment_path = lambda: "drop-reasons"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Nodes.Node.PacketCounters.DropReasons, ['g8275_1_incompatible', 'g8275_2_incompatible', 'invalid_packet', 'invalid_tl_vs', 'looped_higher_port', 'looped_lower_port', 'looped_same_port', 'min_clock_class', 'no_offload_session', 'no_timestamp', 'not_for_us', 'not_granted', 'not_listening', 'not_master', 'not_ready', 'not_slave', 'not_supported', 'too_short', 'too_slow', 'unknown_master', 'wrong_domain', 'wrong_master', 'wrong_sequence_id', 'zero_timestamp'], name, value)


            class Summary(Entity):
                """
                Node summary operational data
                
                .. attribute:: port_state_faulty_count
                
                	Number of interfaces in 'Faulty' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_init_count
                
                	Number of interfaces in 'Init' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_listening_count
                
                	Number of interfaces in 'Listening' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_master_count
                
                	Number of interfaces in 'Master' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_passive_count
                
                	Number of interfaces in 'Passive' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_pre_master_count
                
                	Number of interfaces in 'Pre\-Master' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_slave_count
                
                	Number of interfaces in 'Slave' port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_state_uncalibrated_count
                
                	Number of interfaces in 'Uncalibrated port state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_interfaces
                
                	Total number of interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_interfaces_valid_port_num
                
                	Total number of interfaces with a valid port number
                	**type**\:  int
                
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

                    self.port_state_faulty_count = YLeaf(YType.uint32, "port-state-faulty-count")

                    self.port_state_init_count = YLeaf(YType.uint32, "port-state-init-count")

                    self.port_state_listening_count = YLeaf(YType.uint32, "port-state-listening-count")

                    self.port_state_master_count = YLeaf(YType.uint32, "port-state-master-count")

                    self.port_state_passive_count = YLeaf(YType.uint32, "port-state-passive-count")

                    self.port_state_pre_master_count = YLeaf(YType.uint32, "port-state-pre-master-count")

                    self.port_state_slave_count = YLeaf(YType.uint32, "port-state-slave-count")

                    self.port_state_uncalibrated_count = YLeaf(YType.uint32, "port-state-uncalibrated-count")

                    self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                    self.total_interfaces_valid_port_num = YLeaf(YType.uint32, "total-interfaces-valid-port-num")
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Nodes.Node.Summary, ['port_state_faulty_count', 'port_state_init_count', 'port_state_listening_count', 'port_state_master_count', 'port_state_passive_count', 'port_state_pre_master_count', 'port_state_slave_count', 'port_state_uncalibrated_count', 'total_interfaces', 'total_interfaces_valid_port_num'], name, value)


    class Platform(Entity):
        """
        PTP platform specific data
        
        .. attribute:: servo
        
        	PTP servo related parameters
        	**type**\:   :py:class:`Servo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo>`
        
        

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
            
            .. attribute:: device_status
            
            	status of device
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: flagof_last_set_time
            
            	last input flag of setTime
            	**type**\:  bool
            
            .. attribute:: last_adjust_freq
            
            	last input of adjustFreq
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: last_received_t1
            
            	last T1 timestamp received
            	**type**\:   :py:class:`LastReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT1>`
            
            .. attribute:: last_received_t2
            
            	last T2 timestamp received
            	**type**\:   :py:class:`LastReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT2>`
            
            .. attribute:: last_received_t3
            
            	last T3 timestamp received
            	**type**\:   :py:class:`LastReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT3>`
            
            .. attribute:: last_received_t4
            
            	last T4 timestamp received
            	**type**\:   :py:class:`LastReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastReceivedT4>`
            
            .. attribute:: last_set_time
            
            	last input of setTime
            	**type**\:   :py:class:`LastSetTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.LastSetTime>`
            
            .. attribute:: last_step_time
            
            	last input of stepTime
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lock_status
            
            	lock status of device
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: log_level
            
            	log level of apr
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mean_path_delay
            
            	Mean Path Delay
            	**type**\:  int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: num_adjust_freq
            
            	number of adjustFreq() been called
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_adjust_freq_time
            
            	number of adjustFreqTime() been called
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_delay_timestamp
            
            	number of delay timestamp received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_discard_delay_timestamp
            
            	number of delay timestamp discarded
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_discard_sync_timestamp
            
            	number of sync timestamp discarded
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_set_time
            
            	number of setTime() been called
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_step_time
            
            	number of stepTime() been called
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_sync_timestamp
            
            	number of sync timestamp received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: offset_from_master
            
            	Time Offset From Master
            	**type**\:  int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: phase_accuracy_last
            
            	 last phase alignment accuracy
            	**type**\:  int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: pre_received_t1
            
            	pre T1 timestamp received
            	**type**\:   :py:class:`PreReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT1>`
            
            .. attribute:: pre_received_t2
            
            	pre T2 timestamp received
            	**type**\:   :py:class:`PreReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT2>`
            
            .. attribute:: pre_received_t3
            
            	pre T3 timestamp received
            	**type**\:   :py:class:`PreReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT3>`
            
            .. attribute:: pre_received_t4
            
            	pre T4 timestamp received
            	**type**\:   :py:class:`PreReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_oper.Ptp.Platform.Servo.PreReceivedT4>`
            
            .. attribute:: running
            
            	running status of apr
            	**type**\:  bool
            
            

            """

            _prefix = 'ptp-pd-oper'
            _revision = '2016-06-08'

            def __init__(self):
                super(Ptp.Platform.Servo, self).__init__()

                self.yang_name = "servo"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"last-received-t1" : ("last_received_t1", Ptp.Platform.Servo.LastReceivedT1), "last-received-t2" : ("last_received_t2", Ptp.Platform.Servo.LastReceivedT2), "last-received-t3" : ("last_received_t3", Ptp.Platform.Servo.LastReceivedT3), "last-received-t4" : ("last_received_t4", Ptp.Platform.Servo.LastReceivedT4), "last-set-time" : ("last_set_time", Ptp.Platform.Servo.LastSetTime), "pre-received-t1" : ("pre_received_t1", Ptp.Platform.Servo.PreReceivedT1), "pre-received-t2" : ("pre_received_t2", Ptp.Platform.Servo.PreReceivedT2), "pre-received-t3" : ("pre_received_t3", Ptp.Platform.Servo.PreReceivedT3), "pre-received-t4" : ("pre_received_t4", Ptp.Platform.Servo.PreReceivedT4)}
                self._child_list_classes = {}

                self.device_status = YLeaf(YType.str, "device-status")

                self.flagof_last_set_time = YLeaf(YType.boolean, "flagof-last-set-time")

                self.last_adjust_freq = YLeaf(YType.int32, "last-adjust-freq")

                self.last_step_time = YLeaf(YType.int32, "last-step-time")

                self.lock_status = YLeaf(YType.uint16, "lock-status")

                self.log_level = YLeaf(YType.uint16, "log-level")

                self.mean_path_delay = YLeaf(YType.int64, "mean-path-delay")

                self.num_adjust_freq = YLeaf(YType.uint32, "num-adjust-freq")

                self.num_adjust_freq_time = YLeaf(YType.uint32, "num-adjust-freq-time")

                self.num_delay_timestamp = YLeaf(YType.uint32, "num-delay-timestamp")

                self.num_discard_delay_timestamp = YLeaf(YType.uint32, "num-discard-delay-timestamp")

                self.num_discard_sync_timestamp = YLeaf(YType.uint32, "num-discard-sync-timestamp")

                self.num_set_time = YLeaf(YType.uint32, "num-set-time")

                self.num_step_time = YLeaf(YType.uint32, "num-step-time")

                self.num_sync_timestamp = YLeaf(YType.uint32, "num-sync-timestamp")

                self.offset_from_master = YLeaf(YType.int64, "offset-from-master")

                self.phase_accuracy_last = YLeaf(YType.int64, "phase-accuracy-last")

                self.running = YLeaf(YType.boolean, "running")

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

                self.last_set_time = Ptp.Platform.Servo.LastSetTime()
                self.last_set_time.parent = self
                self._children_name_map["last_set_time"] = "last-set-time"
                self._children_yang_names.add("last-set-time")

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
                self._perform_setattr(Ptp.Platform.Servo, ['device_status', 'flagof_last_set_time', 'last_adjust_freq', 'last_step_time', 'lock_status', 'log_level', 'mean_path_delay', 'num_adjust_freq', 'num_adjust_freq_time', 'num_delay_timestamp', 'num_discard_delay_timestamp', 'num_discard_sync_timestamp', 'num_set_time', 'num_step_time', 'num_sync_timestamp', 'offset_from_master', 'phase_accuracy_last', 'running'], name, value)


            class LastReceivedT1(Entity):
                """
                last T1 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "last-received-t1"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT1, ['nano_second', 'second'], name, value)


            class LastReceivedT2(Entity):
                """
                last T2 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "last-received-t2"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT2, ['nano_second', 'second'], name, value)


            class LastReceivedT3(Entity):
                """
                last T3 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "last-received-t3"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT3, ['nano_second', 'second'], name, value)


            class LastReceivedT4(Entity):
                """
                last T4 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "last-received-t4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastReceivedT4, ['nano_second', 'second'], name, value)


            class LastSetTime(Entity):
                """
                last input of setTime
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "last-set-time"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.LastSetTime, ['nano_second', 'second'], name, value)


            class PreReceivedT1(Entity):
                """
                pre T1 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "pre-received-t1"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT1, ['nano_second', 'second'], name, value)


            class PreReceivedT2(Entity):
                """
                pre T2 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "pre-received-t2"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT2, ['nano_second', 'second'], name, value)


            class PreReceivedT3(Entity):
                """
                pre T3 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "pre-received-t3"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT3, ['nano_second', 'second'], name, value)


            class PreReceivedT4(Entity):
                """
                pre T4 timestamp received
                
                .. attribute:: nano_second
                
                	value of nano second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: second
                
                	value of second
                	**type**\:  int
                
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

                    self.nano_second = YLeaf(YType.uint32, "nano-second")

                    self.second = YLeaf(YType.uint32, "second")
                    self._segment_path = lambda: "pre-received-t4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-oper:ptp/Cisco-IOS-XR-ptp-pd-oper:platform/servo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Platform.Servo.PreReceivedT4, ['nano_second', 'second'], name, value)

    def clone_ptr(self):
        self._top_entity = Ptp()
        return self._top_entity

