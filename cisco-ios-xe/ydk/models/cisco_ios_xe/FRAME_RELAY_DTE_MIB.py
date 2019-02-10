""" FRAME_RELAY_DTE_MIB 

The MIB module to describe the use of a Frame Relay
interface by a DTE.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class FRAMERELAYDTEMIB(Entity):
    """
    
    
    .. attribute:: framerelaytrapcontrol
    
    	
    	**type**\:  :py:class:`FrameRelayTrapControl <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrameRelayTrapControl>`
    
    	**config**\: False
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:  :py:class:`FrDlcmiTable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable>`
    
    	**config**\: False
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connections (DLC) or virtual circuits
    	**type**\:  :py:class:`FrCircuitTable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable>`
    
    	**config**\: False
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface.  Discontinuities in the counters contained in this table are the same as apply to the ifEntry associated with the Interface
    	**type**\:  :py:class:`FrErrTable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'FRAME-RELAY-DTE-MIB'
    _revision = '1997-05-01'

    def __init__(self):
        super(FRAMERELAYDTEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "FRAME-RELAY-DTE-MIB"
        self.yang_parent_name = "FRAME-RELAY-DTE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("frameRelayTrapControl", ("framerelaytrapcontrol", FRAMERELAYDTEMIB.FrameRelayTrapControl)), ("frDlcmiTable", ("frdlcmitable", FRAMERELAYDTEMIB.FrDlcmiTable)), ("frCircuitTable", ("frcircuittable", FRAMERELAYDTEMIB.FrCircuitTable)), ("frErrTable", ("frerrtable", FRAMERELAYDTEMIB.FrErrTable))])
        self._leafs = OrderedDict()

        self.framerelaytrapcontrol = FRAMERELAYDTEMIB.FrameRelayTrapControl()
        self.framerelaytrapcontrol.parent = self
        self._children_name_map["framerelaytrapcontrol"] = "frameRelayTrapControl"

        self.frdlcmitable = FRAMERELAYDTEMIB.FrDlcmiTable()
        self.frdlcmitable.parent = self
        self._children_name_map["frdlcmitable"] = "frDlcmiTable"

        self.frcircuittable = FRAMERELAYDTEMIB.FrCircuitTable()
        self.frcircuittable.parent = self
        self._children_name_map["frcircuittable"] = "frCircuitTable"

        self.frerrtable = FRAMERELAYDTEMIB.FrErrTable()
        self.frerrtable.parent = self
        self._children_name_map["frerrtable"] = "frErrTable"
        self._segment_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FRAMERELAYDTEMIB, [], name, value)


    class FrameRelayTrapControl(Entity):
        """
        
        
        .. attribute:: frtrapstate
        
        	This variable indicates whether the system produces the frDLCIStatusChange trap
        	**type**\:  :py:class:`FrTrapState <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrameRelayTrapControl.FrTrapState>`
        
        	**config**\: False
        
        .. attribute:: frtrapmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between trap emissions.  If events occur more rapidly, the impementation may simply fail to trap, or may queue traps until an appropriate time
        	**type**\: int
        
        	**range:** 0..3600000
        
        	**config**\: False
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FRAMERELAYDTEMIB.FrameRelayTrapControl, self).__init__()

            self.yang_name = "frameRelayTrapControl"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('frtrapstate', (YLeaf(YType.enumeration, 'frTrapState'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrameRelayTrapControl.FrTrapState')])),
                ('frtrapmaxrate', (YLeaf(YType.int32, 'frTrapMaxRate'), ['int'])),
            ])
            self.frtrapstate = None
            self.frtrapmaxrate = None
            self._segment_path = lambda: "frameRelayTrapControl"
            self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FRAMERELAYDTEMIB.FrameRelayTrapControl, ['frtrapstate', 'frtrapmaxrate'], name, value)

        class FrTrapState(Enum):
            """
            FrTrapState (Enum Class)

            This variable indicates whether the system produces

            the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")




    class FrDlcmiTable(Entity):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Connection Management Interface
        	**type**\: list of  		 :py:class:`FrDlcmiEntry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FRAMERELAYDTEMIB.FrDlcmiTable, self).__init__()

            self.yang_name = "frDlcmiTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("frDlcmiEntry", ("frdlcmientry", FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry))])
            self._leafs = OrderedDict()

            self.frdlcmientry = YList(self)
            self._segment_path = lambda: "frDlcmiTable"
            self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FRAMERELAYDTEMIB.FrDlcmiTable, [], name, value)


        class FrDlcmiEntry(Entity):
            """
            The Parameters for a particular Data Link Connection
            Management Interface.
            
            .. attribute:: frdlcmiifindex  (key)
            
            	The ifIndex value of the corresponding ifEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data Link Connection Management scheme is active (and by implication, what DLCI it uses) on the Frame Relay interface
            	**type**\:  :py:class:`FrDlcmiState <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState>`
            
            	**config**\: False
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address format is in use on the Frame Relay interface
            	**type**\:  :py:class:`FrDlcmiAddress <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress>`
            
            	**config**\: False
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states the address length in octets.  In the case of Q922 format, the length indicates the entire length of the address including the control portion
            	**type**\:  :py:class:`FrDlcmiAddressLen <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen>`
            
            	**config**\: False
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between successive status enquiry messages
            	**type**\: int
            
            	**range:** 5..30
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals that pass before issuance of a full status enquiry message
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: frdlcmierrorthreshold
            
            	This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down
            	**type**\: int
            
            	**range:** 1..10
            
            	**config**\: False
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down
            	**type**\: int
            
            	**range:** 1..10
            
            	**config**\: False
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for this interface.  Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or higher than the agent's maximal capability is configured, the agent should respond badValue
            	**type**\: int
            
            	**range:** 0..8388607
            
            	**config**\: False
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay interface is using a multicast service
            	**type**\:  :py:class:`FrDlcmiMulticast <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast>`
            
            	**config**\: False
            
            .. attribute:: frdlcmistatus
            
            	This indicates the status of the Frame Relay interface as determined by the performance of the dlcmi.  If no dlcmi is running, the Frame Relay interface will stay in the running state indefinitely
            	**type**\:  :py:class:`FrDlcmiStatus <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiStatus>`
            
            	**config**\: False
            
            .. attribute:: frdlcmirowstatus
            
            	SNMP Version 2 Row Status Variable.  Writable objects in the table may be written in any RowStatus state
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry, self).__init__()

                self.yang_name = "frDlcmiEntry"
                self.yang_parent_name = "frDlcmiTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frdlcmiifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frdlcmiifindex', (YLeaf(YType.int32, 'frDlcmiIfIndex'), ['int'])),
                    ('frdlcmistate', (YLeaf(YType.enumeration, 'frDlcmiState'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrDlcmiTable.FrDlcmiEntry.FrDlcmiState')])),
                    ('frdlcmiaddress', (YLeaf(YType.enumeration, 'frDlcmiAddress'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress')])),
                    ('frdlcmiaddresslen', (YLeaf(YType.enumeration, 'frDlcmiAddressLen'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen')])),
                    ('frdlcmipollinginterval', (YLeaf(YType.int32, 'frDlcmiPollingInterval'), ['int'])),
                    ('frdlcmifullenquiryinterval', (YLeaf(YType.int32, 'frDlcmiFullEnquiryInterval'), ['int'])),
                    ('frdlcmierrorthreshold', (YLeaf(YType.int32, 'frDlcmiErrorThreshold'), ['int'])),
                    ('frdlcmimonitoredevents', (YLeaf(YType.int32, 'frDlcmiMonitoredEvents'), ['int'])),
                    ('frdlcmimaxsupportedvcs', (YLeaf(YType.int32, 'frDlcmiMaxSupportedVCs'), ['int'])),
                    ('frdlcmimulticast', (YLeaf(YType.enumeration, 'frDlcmiMulticast'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast')])),
                    ('frdlcmistatus', (YLeaf(YType.enumeration, 'frDlcmiStatus'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrDlcmiTable.FrDlcmiEntry.FrDlcmiStatus')])),
                    ('frdlcmirowstatus', (YLeaf(YType.enumeration, 'frDlcmiRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.frdlcmiifindex = None
                self.frdlcmistate = None
                self.frdlcmiaddress = None
                self.frdlcmiaddresslen = None
                self.frdlcmipollinginterval = None
                self.frdlcmifullenquiryinterval = None
                self.frdlcmierrorthreshold = None
                self.frdlcmimonitoredevents = None
                self.frdlcmimaxsupportedvcs = None
                self.frdlcmimulticast = None
                self.frdlcmistatus = None
                self.frdlcmirowstatus = None
                self._segment_path = lambda: "frDlcmiEntry" + "[frDlcmiIfIndex='" + str(self.frdlcmiifindex) + "']"
                self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frDlcmiTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry, ['frdlcmiifindex', 'frdlcmistate', 'frdlcmiaddress', 'frdlcmiaddresslen', 'frdlcmipollinginterval', 'frdlcmifullenquiryinterval', 'frdlcmierrorthreshold', 'frdlcmimonitoredevents', 'frdlcmimaxsupportedvcs', 'frdlcmimulticast', 'frdlcmistatus', 'frdlcmirowstatus'], name, value)

            class FrDlcmiAddress(Enum):
                """
                FrDlcmiAddress (Enum Class)

                This variable states which address format is in use on

                the Frame Relay interface.

                .. data:: q921 = 1

                .. data:: q922March90 = 2

                .. data:: q922November90 = 3

                .. data:: q922 = 4

                """

                q921 = Enum.YLeaf(1, "q921")

                q922March90 = Enum.YLeaf(2, "q922March90")

                q922November90 = Enum.YLeaf(3, "q922November90")

                q922 = Enum.YLeaf(4, "q922")


            class FrDlcmiAddressLen(Enum):
                """
                FrDlcmiAddressLen (Enum Class)

                This variable states the address length in octets.  In

                the case of Q922 format, the length indicates the

                entire length of the address including the control

                portion.

                .. data:: twoOctets = 2

                .. data:: threeOctets = 3

                .. data:: fourOctets = 4

                """

                twoOctets = Enum.YLeaf(2, "twoOctets")

                threeOctets = Enum.YLeaf(3, "threeOctets")

                fourOctets = Enum.YLeaf(4, "fourOctets")


            class FrDlcmiMulticast(Enum):
                """
                FrDlcmiMulticast (Enum Class)

                This indicates whether the Frame Relay interface is

                using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = Enum.YLeaf(1, "nonBroadcast")

                broadcast = Enum.YLeaf(2, "broadcast")


            class FrDlcmiState(Enum):
                """
                FrDlcmiState (Enum Class)

                This variable states which Data Link Connection

                Management scheme is active (and by implication, what

                DLCI it uses) on the Frame Relay interface.

                .. data:: noLmiConfigured = 1

                .. data:: lmiRev1 = 2

                .. data:: ansiT1617D = 3

                .. data:: ansiT1617B = 4

                .. data:: itut933A = 5

                .. data:: ansiT1617D1994 = 6

                """

                noLmiConfigured = Enum.YLeaf(1, "noLmiConfigured")

                lmiRev1 = Enum.YLeaf(2, "lmiRev1")

                ansiT1617D = Enum.YLeaf(3, "ansiT1617D")

                ansiT1617B = Enum.YLeaf(4, "ansiT1617B")

                itut933A = Enum.YLeaf(5, "itut933A")

                ansiT1617D1994 = Enum.YLeaf(6, "ansiT1617D1994")


            class FrDlcmiStatus(Enum):
                """
                FrDlcmiStatus (Enum Class)

                This indicates the status of the Frame Relay interface

                as determined by the performance of the dlcmi.  If no

                dlcmi is running, the Frame Relay interface will stay

                in the running state indefinitely.

                .. data:: running = 1

                .. data:: fault = 2

                .. data:: initializing = 3

                """

                running = Enum.YLeaf(1, "running")

                fault = Enum.YLeaf(2, "fault")

                initializing = Enum.YLeaf(3, "initializing")





    class FrCircuitTable(Entity):
        """
        A table containing information about specific Data
        Link Connections (DLC) or virtual circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single Data Link Connection.  Discontinuities in the counters contained in this table are indicated by the value in frCircuitCreationTime
        	**type**\: list of  		 :py:class:`FrCircuitEntry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FRAMERELAYDTEMIB.FrCircuitTable, self).__init__()

            self.yang_name = "frCircuitTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("frCircuitEntry", ("frcircuitentry", FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry))])
            self._leafs = OrderedDict()

            self.frcircuitentry = YList(self)
            self._segment_path = lambda: "frCircuitTable"
            self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FRAMERELAYDTEMIB.FrCircuitTable, [], name, value)


        class FrCircuitEntry(Entity):
            """
            The information regarding a single Data Link
            Connection.  Discontinuities in the counters contained
            in this table are indicated by the value in
            frCircuitCreationTime.
            
            .. attribute:: frcircuitifindex  (key)
            
            	The ifIndex Value of the ifEntry this virtual circuit is layered onto
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: frcircuitdlci  (key)
            
            	The Data Link Connection Identifier for this virtual circuit
            	**type**\: int
            
            	**range:** 0..8388607
            
            	**config**\: False
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual circuit is operational.  In the absence of a Data Link Connection Management Interface, virtual circuit entries (rows) may be created by setting virtual circuit state to 'active', or deleted by changing Circuit state to 'invalid'.  Whether or not the row actually disappears is left to the implementation, so this object may actually read as 'invalid' for some arbitrary length of time.  It is also legal to set the state of a virtual circuit to 'inactive' to temporarily disable a given circuit.  The use of 'invalid' is deprecated in this SNMP Version 2 MIB, in favor of frCircuitRowStatus
            	**type**\:  :py:class:`FrCircuitState <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitState>`
            
            	**config**\: False
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network indicating forward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the FECN flag, or when a switch in the network enqueues the frame to a trunk whose transmission queue is congested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network indicating backward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the BECN flag, or when a switch in the network receives the frame from a trunk whose transmission queue is congested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent from this virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent from this virtual circuit since it was created.  Octets counted are the full frame relay header and the payload, but do not include the flag characters or CRC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received over this virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received over this virtual circuit since it was created.  Octets counted include the full frame relay header, but do not include the flag characters or the CRC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the virtual circuit was created, whether by the Data Link Connection Management Interface or by a SetRequest
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there was a change in the virtual circuit state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount of data, in bits, that the network agrees to transfer under normal conditions, during the measurement interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount of uncommitted data bits that the network will attempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Relay Information Field' bits transferred per second across a user network interface in one direction, measured over the measurement interval.  If the configured committed burst rate and throughput are both non\-zero, the measurement interval, T, is     T=frCircuitCommittedBurst/frCircuitThroughput.  If the configured committed burst rate and throughput are both zero, the measurement interval, T, is            T=frCircuitExcessBurst/ifSpeed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: frcircuitmulticast
            
            	This indicates whether this VC is used as a unicast VC (i.e. not multicast) or the type of multicast service subscribed to
            	**type**\:  :py:class:`FrCircuitMulticast <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitMulticast>`
            
            	**config**\: False
            
            .. attribute:: frcircuittype
            
            	Indication of whether the VC was manually created (static), or dynamically created (dynamic) via the data link control management interface
            	**type**\:  :py:class:`FrCircuitType <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitType>`
            
            	**config**\: False
            
            .. attribute:: frcircuitdiscards
            
            	The number of inbound frames dropped because of format errors, or because the VC is inactive
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitreceiveddes
            
            	Number of frames received from the network indicating that they were eligible for discard since the virtual circuit was created.  This occurs when the remote DTE sets the DE flag, or when in remote DTE's switch detects that the frame was received as Excess Burst data
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitsentdes
            
            	Number of frames sent to the network indicating that they were eligible for discard since the virtual circuit was created.   This occurs when the local DTE sets the DE flag, indicating that during Network congestion situations those frames should be discarded in preference of other frames sent without the DE bit set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frcircuitlogicalifindex
            
            	Normally the same value as frDlcmiIfIndex, but different when an implementation associates a virtual ifEntry with a DLC or set of DLCs in order to associate higher layer objects such as the ipAddrEntry with a subset of the virtual circuits on a Frame Relay interface. The type of such ifEntries is defined by the higher layer object; for example, if PPP/Frame Relay is implemented, the ifType of this ifEntry would be PPP. If it is not so defined, as would be the case with an ipAddrEntry, it should be of type Other
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: frcircuitrowstatus
            
            	This object is used to create a new row or modify or destroy an existing row in the manner described in the definition of the RowStatus textual convention. Writable objects in the table may be written in any RowStatus state
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry, self).__init__()

                self.yang_name = "frCircuitEntry"
                self.yang_parent_name = "frCircuitTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frcircuitifindex','frcircuitdlci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frcircuitifindex', (YLeaf(YType.int32, 'frCircuitIfIndex'), ['int'])),
                    ('frcircuitdlci', (YLeaf(YType.int32, 'frCircuitDlci'), ['int'])),
                    ('frcircuitstate', (YLeaf(YType.enumeration, 'frCircuitState'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrCircuitTable.FrCircuitEntry.FrCircuitState')])),
                    ('frcircuitreceivedfecns', (YLeaf(YType.uint32, 'frCircuitReceivedFECNs'), ['int'])),
                    ('frcircuitreceivedbecns', (YLeaf(YType.uint32, 'frCircuitReceivedBECNs'), ['int'])),
                    ('frcircuitsentframes', (YLeaf(YType.uint32, 'frCircuitSentFrames'), ['int'])),
                    ('frcircuitsentoctets', (YLeaf(YType.uint32, 'frCircuitSentOctets'), ['int'])),
                    ('frcircuitreceivedframes', (YLeaf(YType.uint32, 'frCircuitReceivedFrames'), ['int'])),
                    ('frcircuitreceivedoctets', (YLeaf(YType.uint32, 'frCircuitReceivedOctets'), ['int'])),
                    ('frcircuitcreationtime', (YLeaf(YType.uint32, 'frCircuitCreationTime'), ['int'])),
                    ('frcircuitlasttimechange', (YLeaf(YType.uint32, 'frCircuitLastTimeChange'), ['int'])),
                    ('frcircuitcommittedburst', (YLeaf(YType.int32, 'frCircuitCommittedBurst'), ['int'])),
                    ('frcircuitexcessburst', (YLeaf(YType.int32, 'frCircuitExcessBurst'), ['int'])),
                    ('frcircuitthroughput', (YLeaf(YType.int32, 'frCircuitThroughput'), ['int'])),
                    ('frcircuitmulticast', (YLeaf(YType.enumeration, 'frCircuitMulticast'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrCircuitTable.FrCircuitEntry.FrCircuitMulticast')])),
                    ('frcircuittype', (YLeaf(YType.enumeration, 'frCircuitType'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrCircuitTable.FrCircuitEntry.FrCircuitType')])),
                    ('frcircuitdiscards', (YLeaf(YType.uint32, 'frCircuitDiscards'), ['int'])),
                    ('frcircuitreceiveddes', (YLeaf(YType.uint32, 'frCircuitReceivedDEs'), ['int'])),
                    ('frcircuitsentdes', (YLeaf(YType.uint32, 'frCircuitSentDEs'), ['int'])),
                    ('frcircuitlogicalifindex', (YLeaf(YType.int32, 'frCircuitLogicalIfIndex'), ['int'])),
                    ('frcircuitrowstatus', (YLeaf(YType.enumeration, 'frCircuitRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.frcircuitifindex = None
                self.frcircuitdlci = None
                self.frcircuitstate = None
                self.frcircuitreceivedfecns = None
                self.frcircuitreceivedbecns = None
                self.frcircuitsentframes = None
                self.frcircuitsentoctets = None
                self.frcircuitreceivedframes = None
                self.frcircuitreceivedoctets = None
                self.frcircuitcreationtime = None
                self.frcircuitlasttimechange = None
                self.frcircuitcommittedburst = None
                self.frcircuitexcessburst = None
                self.frcircuitthroughput = None
                self.frcircuitmulticast = None
                self.frcircuittype = None
                self.frcircuitdiscards = None
                self.frcircuitreceiveddes = None
                self.frcircuitsentdes = None
                self.frcircuitlogicalifindex = None
                self.frcircuitrowstatus = None
                self._segment_path = lambda: "frCircuitEntry" + "[frCircuitIfIndex='" + str(self.frcircuitifindex) + "']" + "[frCircuitDlci='" + str(self.frcircuitdlci) + "']"
                self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frCircuitTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry, ['frcircuitifindex', 'frcircuitdlci', 'frcircuitstate', 'frcircuitreceivedfecns', 'frcircuitreceivedbecns', 'frcircuitsentframes', 'frcircuitsentoctets', 'frcircuitreceivedframes', 'frcircuitreceivedoctets', 'frcircuitcreationtime', 'frcircuitlasttimechange', 'frcircuitcommittedburst', 'frcircuitexcessburst', 'frcircuitthroughput', 'frcircuitmulticast', 'frcircuittype', 'frcircuitdiscards', 'frcircuitreceiveddes', 'frcircuitsentdes', 'frcircuitlogicalifindex', 'frcircuitrowstatus'], name, value)

            class FrCircuitMulticast(Enum):
                """
                FrCircuitMulticast (Enum Class)

                This indicates whether this VC is used as a unicast VC

                (i.e. not multicast) or the type of multicast service

                subscribed to

                .. data:: unicast = 1

                .. data:: oneWay = 2

                .. data:: twoWay = 3

                .. data:: nWay = 4

                """

                unicast = Enum.YLeaf(1, "unicast")

                oneWay = Enum.YLeaf(2, "oneWay")

                twoWay = Enum.YLeaf(3, "twoWay")

                nWay = Enum.YLeaf(4, "nWay")


            class FrCircuitState(Enum):
                """
                FrCircuitState (Enum Class)

                Indicates whether the particular virtual circuit is

                operational.  In the absence of a Data Link Connection

                Management Interface, virtual circuit entries (rows)

                may be created by setting virtual circuit state to

                'active', or deleted by changing Circuit state to

                'invalid'.

                Whether or not the row actually disappears is left to

                the implementation, so this object may actually read as

                'invalid' for some arbitrary length of time.  It is

                also legal to set the state of a virtual circuit to

                'inactive' to temporarily disable a given circuit.

                The use of 'invalid' is deprecated in this SNMP Version

                2 MIB, in favor of frCircuitRowStatus.

                .. data:: invalid = 1

                .. data:: active = 2

                .. data:: inactive = 3

                """

                invalid = Enum.YLeaf(1, "invalid")

                active = Enum.YLeaf(2, "active")

                inactive = Enum.YLeaf(3, "inactive")


            class FrCircuitType(Enum):
                """
                FrCircuitType (Enum Class)

                Indication of whether the VC was manually created

                (static), or dynamically created (dynamic) via the data

                link control management interface.

                .. data:: static = 1

                .. data:: dynamic = 2

                """

                static = Enum.YLeaf(1, "static")

                dynamic = Enum.YLeaf(2, "dynamic")





    class FrErrTable(Entity):
        """
        A table containing information about Errors on the
        Frame Relay interface.  Discontinuities in the counters
        contained in this table are the same as apply to the
        ifEntry associated with the Interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of  		 :py:class:`FrErrEntry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable.FrErrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FRAMERELAYDTEMIB.FrErrTable, self).__init__()

            self.yang_name = "frErrTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("frErrEntry", ("frerrentry", FRAMERELAYDTEMIB.FrErrTable.FrErrEntry))])
            self._leafs = OrderedDict()

            self.frerrentry = YList(self)
            self._segment_path = lambda: "frErrTable"
            self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FRAMERELAYDTEMIB.FrErrTable, [], name, value)


        class FrErrEntry(Entity):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  (key)
            
            	The ifIndex Value of the corresponding ifEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface\:  receiveShort\: frame was not long enough to allow         demultiplexing \- the address field was incomplete,         or for virtual circuits using Multiprotocol over         Frame Relay, the protocol identifier was missing         or incomplete.  receiveLong\: frame exceeded maximum length configured for this              interface.  illegalAddress\: address field did not match configured format.  unknownAddress\: frame received on a virtual circuit which was not                 active or administratively disabled.  dlcmiProtoErr\: unspecified error occurred when attempting to                interpret link maintenance frame.  dlcmiUnknownIE\: link maintenance frame contained an Information                 Element type which is not valid for the                 configured link maintenance protocol.  dlcmiSequenceErr\: link maintenance frame contained a sequence                   number other than the expected value.  dlcmiUnknownRpt\: link maintenance frame contained a Report Type                  Information Element whose value was not valid                  for the configured link maintenance protocol.  noErrorSinceReset\: no errors have been detected since the last                    cold start or warm start
            	**type**\:  :py:class:`FrErrType <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable.FrErrEntry.FrErrType>`
            
            	**config**\: False
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the error packet as possible.  As a minimum, it must contain the Q.922 Address or as much as was delivered.  It is desirable to include all header and demultiplexing information
            	**type**\: str
            
            	**length:** 1..1600
            
            	**config**\: False
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frerrfaults
            
            	The number of times the interface has gone down since it was initialized
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: frerrfaulttime
            
            	The value of sysUpTime at the time when the interface was taken down due to excessive errors.  Excessive errors is defined as the time when a DLCMI exceeds the frDlcmiErrorThreshold number of errors within frDlcmiMonitoredEvents. See FrDlcmiEntry for further details
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FRAMERELAYDTEMIB.FrErrTable.FrErrEntry, self).__init__()

                self.yang_name = "frErrEntry"
                self.yang_parent_name = "frErrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frerrifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frerrifindex', (YLeaf(YType.int32, 'frErrIfIndex'), ['int'])),
                    ('frerrtype', (YLeaf(YType.enumeration, 'frErrType'), [('ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FRAMERELAYDTEMIB', 'FrErrTable.FrErrEntry.FrErrType')])),
                    ('frerrdata', (YLeaf(YType.str, 'frErrData'), ['str'])),
                    ('frerrtime', (YLeaf(YType.uint32, 'frErrTime'), ['int'])),
                    ('frerrfaults', (YLeaf(YType.uint32, 'frErrFaults'), ['int'])),
                    ('frerrfaulttime', (YLeaf(YType.uint32, 'frErrFaultTime'), ['int'])),
                ])
                self.frerrifindex = None
                self.frerrtype = None
                self.frerrdata = None
                self.frerrtime = None
                self.frerrfaults = None
                self.frerrfaulttime = None
                self._segment_path = lambda: "frErrEntry" + "[frErrIfIndex='" + str(self.frerrifindex) + "']"
                self._absolute_path = lambda: "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frErrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FRAMERELAYDTEMIB.FrErrTable.FrErrEntry, ['frerrifindex', 'frerrtype', 'frerrdata', 'frerrtime', 'frerrfaults', 'frerrfaulttime'], name, value)

            class FrErrType(Enum):
                """
                FrErrType (Enum Class)

                The type of error that was last seen  on  this interface\:

                receiveShort\: frame was not long enough to allow

                        demultiplexing \- the address field was incomplete,

                        or for virtual circuits using Multiprotocol over

                        Frame Relay, the protocol identifier was missing

                        or incomplete.

                receiveLong\: frame exceeded maximum length configured for this

                             interface.

                illegalAddress\: address field did not match configured format.

                unknownAddress\: frame received on a virtual circuit which was not

                                active or administratively disabled.

                dlcmiProtoErr\: unspecified error occurred when attempting to

                               interpret link maintenance frame.

                dlcmiUnknownIE\: link maintenance frame contained an Information

                                Element type which is not valid for the

                                configured link maintenance protocol.

                dlcmiSequenceErr\: link maintenance frame contained a sequence

                                  number other than the expected value.

                dlcmiUnknownRpt\: link maintenance frame contained a Report Type

                                 Information Element whose value was not valid

                                 for the configured link maintenance protocol.

                noErrorSinceReset\: no errors have been detected since the last

                                   cold start or warm start.

                .. data:: unknownError = 1

                .. data:: receiveShort = 2

                .. data:: receiveLong = 3

                .. data:: illegalAddress = 4

                .. data:: unknownAddress = 5

                .. data:: dlcmiProtoErr = 6

                .. data:: dlcmiUnknownIE = 7

                .. data:: dlcmiSequenceErr = 8

                .. data:: dlcmiUnknownRpt = 9

                .. data:: noErrorSinceReset = 10

                """

                unknownError = Enum.YLeaf(1, "unknownError")

                receiveShort = Enum.YLeaf(2, "receiveShort")

                receiveLong = Enum.YLeaf(3, "receiveLong")

                illegalAddress = Enum.YLeaf(4, "illegalAddress")

                unknownAddress = Enum.YLeaf(5, "unknownAddress")

                dlcmiProtoErr = Enum.YLeaf(6, "dlcmiProtoErr")

                dlcmiUnknownIE = Enum.YLeaf(7, "dlcmiUnknownIE")

                dlcmiSequenceErr = Enum.YLeaf(8, "dlcmiSequenceErr")

                dlcmiUnknownRpt = Enum.YLeaf(9, "dlcmiUnknownRpt")

                noErrorSinceReset = Enum.YLeaf(10, "noErrorSinceReset")




    def clone_ptr(self):
        self._top_entity = FRAMERELAYDTEMIB()
        return self._top_entity



