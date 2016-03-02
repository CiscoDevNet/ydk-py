""" FRAME_RELAY_DTE_MIB 

The MIB module to describe the use of a Frame Relay
interface by a DTE.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class FRAMERELAYDTEMIB(object):
    """
    
    
    .. attribute:: framerelaytrapcontrol
    
    	
    	**type**\: :py:class:`FrameRelayTrapControl <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrameRelayTrapControl>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connections (DLC) or virtual circuits
    	**type**\: :py:class:`FrCircuitTable <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\: :py:class:`FrDlcmiTable <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface.  Discontinuities in the counters contained in this table are the same as apply to the ifEntry associated with the Interface
    	**type**\: :py:class:`FrErrTable <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable>`
    
    

    """

    _prefix = 'frame-relay'
    _revision = '1997-05-01'

    def __init__(self):
        self.framerelaytrapcontrol = FRAMERELAYDTEMIB.FrameRelayTrapControl()
        self.framerelaytrapcontrol.parent = self
        self.frcircuittable = FRAMERELAYDTEMIB.FrCircuitTable()
        self.frcircuittable.parent = self
        self.frdlcmitable = FRAMERELAYDTEMIB.FrDlcmiTable()
        self.frdlcmitable.parent = self
        self.frerrtable = FRAMERELAYDTEMIB.FrErrTable()
        self.frerrtable.parent = self


    class FrCircuitTable(object):
        """
        A table containing information about specific Data
        Link Connections (DLC) or virtual circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single Data Link Connection.  Discontinuities in the counters contained in this table are indicated by the value in frCircuitCreationTime
        	**type**\: list of :py:class:`FrCircuitEntry <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry>`
        
        

        """

        _prefix = 'frame-relay'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frcircuitentry = YList()
            self.frcircuitentry.parent = self
            self.frcircuitentry.name = 'frcircuitentry'


        class FrCircuitEntry(object):
            """
            The information regarding a single Data Link
            Connection.  Discontinuities in the counters contained
            in this table are indicated by the value in
            frCircuitCreationTime.
            
            .. attribute:: frcircuitdlci
            
            	The Data Link Connection Identifier for this virtual circuit
            	**type**\: int
            
            	**range:** 0..8388607
            
            .. attribute:: frcircuitifindex
            
            	The ifIndex Value of the ifEntry this virtual circuit is layered onto
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount of data, in bits, that the network agrees to transfer under normal conditions, during the measurement interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the virtual circuit was created, whether by the Data Link Connection Management Interface or by a SetRequest
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitdiscards
            
            	The number of inbound frames dropped because of format errors, or because the VC is inactive
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount of uncommitted data bits that the network will attempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there was a change in the virtual circuit state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitlogicalifindex
            
            	Normally the same value as frDlcmiIfIndex, but different when an implementation associates a virtual ifEntry with a DLC or set of DLCs in order to associate higher layer objects such as the ipAddrEntry with a subset of the virtual circuits on a Frame Relay interface. The type of such ifEntries is defined by the higher layer object; for example, if PPP/Frame Relay is implemented, the ifType of this ifEntry would be PPP. If it is not so defined, as would be the case with an ipAddrEntry, it should be of type Other
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitmulticast
            
            	This indicates whether this VC is used as a unicast VC (i.e. not multicast) or the type of multicast service subscribed to
            	**type**\: :py:class:`FrCircuitMulticast_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitMulticast_Enum>`
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network indicating backward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the BECN flag, or when a switch in the network receives the frame from a trunk whose transmission queue is congested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceiveddes
            
            	Number of frames received from the network indicating that they were eligible for discard since the virtual circuit was created.  This occurs when the remote DTE sets the DE flag, or when in remote DTE's switch detects that the frame was received as Excess Burst data
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network indicating forward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the FECN flag, or when a switch in the network enqueues the frame to a trunk whose transmission queue is congested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received over this virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received over this virtual circuit since it was created.  Octets counted include the full frame relay header, but do not include the flag characters or the CRC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitrowstatus
            
            	This object is used to create a new row or modify or destroy an existing row in the manner described in the definition of the RowStatus textual convention. Writable objects in the table may be written in any RowStatus state
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: frcircuitsentdes
            
            	Number of frames sent to the network indicating that they were eligible for discard since the virtual circuit was created.   This occurs when the local DTE sets the DE flag, indicating that during Network congestion situations those frames should be discarded in preference of other frames sent without the DE bit set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent from this virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent from this virtual circuit since it was created.  Octets counted are the full frame relay header and the payload, but do not include the flag characters or CRC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual circuit is operational.  In the absence of a Data Link Connection Management Interface, virtual circuit entries (rows) may be created by setting virtual circuit state to 'active', or deleted by changing Circuit state to 'invalid'.  Whether or not the row actually disappears is left to the implementation, so this object may actually read as 'invalid' for some arbitrary length of time.  It is also legal to set the state of a virtual circuit to 'inactive' to temporarily disable a given circuit.  The use of 'invalid' is deprecated in this SNMP Version 2 MIB, in favor of frCircuitRowStatus
            	**type**\: :py:class:`FrCircuitState_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Relay Information Field' bits transferred per second across a user network interface in one direction, measured over the measurement interval.  If the configured committed burst rate and throughput are both non\-zero, the measurement interval, T, is     T=frCircuitCommittedBurst/frCircuitThroughput.  If the configured committed burst rate and throughput are both zero, the measurement interval, T, is            T=frCircuitExcessBurst/ifSpeed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuittype
            
            	Indication of whether the VC was manually created (static), or dynamically created (dynamic) via the data link control management interface
            	**type**\: :py:class:`FrCircuitType_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitType_Enum>`
            
            

            """

            _prefix = 'frame-relay'
            _revision = '1997-05-01'

            def __init__(self):
                self.parent = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.frcircuitcommittedburst = None
                self.frcircuitcreationtime = None
                self.frcircuitdiscards = None
                self.frcircuitexcessburst = None
                self.frcircuitlasttimechange = None
                self.frcircuitlogicalifindex = None
                self.frcircuitmulticast = None
                self.frcircuitreceivedbecns = None
                self.frcircuitreceiveddes = None
                self.frcircuitreceivedfecns = None
                self.frcircuitreceivedframes = None
                self.frcircuitreceivedoctets = None
                self.frcircuitrowstatus = None
                self.frcircuitsentdes = None
                self.frcircuitsentframes = None
                self.frcircuitsentoctets = None
                self.frcircuitstate = None
                self.frcircuitthroughput = None
                self.frcircuittype = None

            class FrCircuitMulticast_Enum(Enum):
                """
                FrCircuitMulticast_Enum

                This indicates whether this VC is used as a unicast VC
                (i.e. not multicast) or the type of multicast service
                subscribed to

                """

                UNICAST = 1

                ONEWAY = 2

                TWOWAY = 3

                NWAY = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitMulticast_Enum']


            class FrCircuitState_Enum(Enum):
                """
                FrCircuitState_Enum

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

                """

                INVALID = 1

                ACTIVE = 2

                INACTIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum']


            class FrCircuitType_Enum(Enum):
                """
                FrCircuitType_Enum

                Indication of whether the VC was manually created
                (static), or dynamically created (dynamic) via the data
                link control management interface.

                """

                STATIC = 1

                DYNAMIC = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry.FrCircuitType_Enum']


            @property
            def _common_path(self):
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frCircuitTable/FRAME-RELAY-DTE-MIB:frCircuitEntry[FRAME-RELAY-DTE-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][FRAME-RELAY-DTE-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.frcircuitcommittedburst is not None:
                    return True

                if self.frcircuitcreationtime is not None:
                    return True

                if self.frcircuitdiscards is not None:
                    return True

                if self.frcircuitexcessburst is not None:
                    return True

                if self.frcircuitlasttimechange is not None:
                    return True

                if self.frcircuitlogicalifindex is not None:
                    return True

                if self.frcircuitmulticast is not None:
                    return True

                if self.frcircuitreceivedbecns is not None:
                    return True

                if self.frcircuitreceiveddes is not None:
                    return True

                if self.frcircuitreceivedfecns is not None:
                    return True

                if self.frcircuitreceivedframes is not None:
                    return True

                if self.frcircuitreceivedoctets is not None:
                    return True

                if self.frcircuitrowstatus is not None:
                    return True

                if self.frcircuitsentdes is not None:
                    return True

                if self.frcircuitsentframes is not None:
                    return True

                if self.frcircuitsentoctets is not None:
                    return True

                if self.frcircuitstate is not None:
                    return True

                if self.frcircuitthroughput is not None:
                    return True

                if self.frcircuittype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FRAMERELAYDTEMIB.FrCircuitTable.FrCircuitEntry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frCircuitTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frcircuitentry is not None:
                for child_ref in self.frcircuitentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FRAMERELAYDTEMIB.FrCircuitTable']['meta_info']


    class FrDlcmiTable(object):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Connection Management Interface
        	**type**\: list of :py:class:`FrDlcmiEntry <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry>`
        
        

        """

        _prefix = 'frame-relay'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frdlcmientry = YList()
            self.frdlcmientry.parent = self
            self.frdlcmientry.name = 'frdlcmientry'


        class FrDlcmiEntry(object):
            """
            The Parameters for a particular Data Link Connection
            Management Interface.
            
            .. attribute:: frdlcmiifindex
            
            	The ifIndex value of the corresponding ifEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address format is in use on the Frame Relay interface
            	**type**\: :py:class:`FrDlcmiAddress_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states the address length in octets.  In the case of Q922 format, the length indicates the entire length of the address including the control portion
            	**type**\: :py:class:`FrDlcmiAddressLen_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals that pass before issuance of a full status enquiry message
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for this interface.  Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or higher than the agent's maximal capability is configured, the agent should respond badValue
            	**type**\: int
            
            	**range:** 0..8388607
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay interface is using a multicast service
            	**type**\: :py:class:`FrDlcmiMulticast_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between successive status enquiry messages
            	**type**\: int
            
            	**range:** 5..30
            
            .. attribute:: frdlcmirowstatus
            
            	SNMP Version 2 Row Status Variable.  Writable objects in the table may be written in any RowStatus state
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data Link Connection Management scheme is active (and by implication, what DLCI it uses) on the Frame Relay interface
            	**type**\: :py:class:`FrDlcmiState_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum>`
            
            .. attribute:: frdlcmistatus
            
            	This indicates the status of the Frame Relay interface as determined by the performance of the dlcmi.  If no dlcmi is running, the Frame Relay interface will stay in the running state indefinitely
            	**type**\: :py:class:`FrDlcmiStatus_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiStatus_Enum>`
            
            

            """

            _prefix = 'frame-relay'
            _revision = '1997-05-01'

            def __init__(self):
                self.parent = None
                self.frdlcmiifindex = None
                self.frdlcmiaddress = None
                self.frdlcmiaddresslen = None
                self.frdlcmierrorthreshold = None
                self.frdlcmifullenquiryinterval = None
                self.frdlcmimaxsupportedvcs = None
                self.frdlcmimonitoredevents = None
                self.frdlcmimulticast = None
                self.frdlcmipollinginterval = None
                self.frdlcmirowstatus = None
                self.frdlcmistate = None
                self.frdlcmistatus = None

            class FrDlcmiAddressLen_Enum(Enum):
                """
                FrDlcmiAddressLen_Enum

                This variable states the address length in octets.  In
                the case of Q922 format, the length indicates the
                entire length of the address including the control
                portion.

                """

                TWOOCTETS = 2

                THREEOCTETS = 3

                FOUROCTETS = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum']


            class FrDlcmiAddress_Enum(Enum):
                """
                FrDlcmiAddress_Enum

                This variable states which address format is in use on
                the Frame Relay interface.

                """

                Q921 = 1

                Q922MARCH90 = 2

                Q922NOVEMBER90 = 3

                Q922 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum']


            class FrDlcmiMulticast_Enum(Enum):
                """
                FrDlcmiMulticast_Enum

                This indicates whether the Frame Relay interface is
                using a multicast service.

                """

                NONBROADCAST = 1

                BROADCAST = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum']


            class FrDlcmiState_Enum(Enum):
                """
                FrDlcmiState_Enum

                This variable states which Data Link Connection
                Management scheme is active (and by implication, what
                DLCI it uses) on the Frame Relay interface.

                """

                NOLMICONFIGURED = 1

                LMIREV1 = 2

                ANSIT1617D = 3

                ANSIT1617B = 4

                ITUT933A = 5

                ANSIT1617D1994 = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum']


            class FrDlcmiStatus_Enum(Enum):
                """
                FrDlcmiStatus_Enum

                This indicates the status of the Frame Relay interface
                as determined by the performance of the dlcmi.  If no
                dlcmi is running, the Frame Relay interface will stay
                in the running state indefinitely.

                """

                RUNNING = 1

                FAULT = 2

                INITIALIZING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiStatus_Enum']


            @property
            def _common_path(self):
                if self.frdlcmiifindex is None:
                    raise YPYDataValidationError('Key property frdlcmiifindex is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frDlcmiTable/FRAME-RELAY-DTE-MIB:frDlcmiEntry[FRAME-RELAY-DTE-MIB:frDlcmiIfIndex = ' + str(self.frdlcmiifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frdlcmiifindex is not None:
                    return True

                if self.frdlcmiaddress is not None:
                    return True

                if self.frdlcmiaddresslen is not None:
                    return True

                if self.frdlcmierrorthreshold is not None:
                    return True

                if self.frdlcmifullenquiryinterval is not None:
                    return True

                if self.frdlcmimaxsupportedvcs is not None:
                    return True

                if self.frdlcmimonitoredevents is not None:
                    return True

                if self.frdlcmimulticast is not None:
                    return True

                if self.frdlcmipollinginterval is not None:
                    return True

                if self.frdlcmirowstatus is not None:
                    return True

                if self.frdlcmistate is not None:
                    return True

                if self.frdlcmistatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable.FrDlcmiEntry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frDlcmiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frdlcmientry is not None:
                for child_ref in self.frdlcmientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FRAMERELAYDTEMIB.FrDlcmiTable']['meta_info']


    class FrErrTable(object):
        """
        A table containing information about Errors on the
        Frame Relay interface.  Discontinuities in the counters
        contained in this table are the same as apply to the
        ifEntry associated with the Interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of :py:class:`FrErrEntry <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable.FrErrEntry>`
        
        

        """

        _prefix = 'frame-relay'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frerrentry = YList()
            self.frerrentry.parent = self
            self.frerrentry.name = 'frerrentry'


        class FrErrEntry(object):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex
            
            	The ifIndex Value of the corresponding ifEntry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the error packet as possible.  As a minimum, it must contain the Q.922 Address or as much as was delivered.  It is desirable to include all header and demultiplexing information
            	**type**\: str
            
            	**range:** 1..1600
            
            .. attribute:: frerrfaults
            
            	The number of times the interface has gone down since it was initialized
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrfaulttime
            
            	The value of sysUpTime at the time when the interface was taken down due to excessive errors.  Excessive errors is defined as the time when a DLCMI exceeds the frDlcmiErrorThreshold number of errors within frDlcmiMonitoredEvents. See FrDlcmiEntry for further details
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface\:  receiveShort\: frame was not long enough to allow         demultiplexing \- the address field was incomplete,         or for virtual circuits using Multiprotocol over         Frame Relay, the protocol identifier was missing         or incomplete.  receiveLong\: frame exceeded maximum length configured for this              interface.  illegalAddress\: address field did not match configured format.  unknownAddress\: frame received on a virtual circuit which was not                 active or administratively disabled.  dlcmiProtoErr\: unspecified error occurred when attempting to                interpret link maintenance frame.  dlcmiUnknownIE\: link maintenance frame contained an Information                 Element type which is not valid for the                 configured link maintenance protocol.  dlcmiSequenceErr\: link maintenance frame contained a sequence                   number other than the expected value.  dlcmiUnknownRpt\: link maintenance frame contained a Report Type                  Information Element whose value was not valid                  for the configured link maintenance protocol.  noErrorSinceReset\: no errors have been detected since the last                    cold start or warm start
            	**type**\: :py:class:`FrErrType_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrErrTable.FrErrEntry.FrErrType_Enum>`
            
            

            """

            _prefix = 'frame-relay'
            _revision = '1997-05-01'

            def __init__(self):
                self.parent = None
                self.frerrifindex = None
                self.frerrdata = None
                self.frerrfaults = None
                self.frerrfaulttime = None
                self.frerrtime = None
                self.frerrtype = None

            class FrErrType_Enum(Enum):
                """
                FrErrType_Enum

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

                """

                UNKNOWNERROR = 1

                RECEIVESHORT = 2

                RECEIVELONG = 3

                ILLEGALADDRESS = 4

                UNKNOWNADDRESS = 5

                DLCMIPROTOERR = 6

                DLCMIUNKNOWNIE = 7

                DLCMISEQUENCEERR = 8

                DLCMIUNKNOWNRPT = 9

                NOERRORSINCERESET = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FRAMERELAYDTEMIB.FrErrTable.FrErrEntry.FrErrType_Enum']


            @property
            def _common_path(self):
                if self.frerrifindex is None:
                    raise YPYDataValidationError('Key property frerrifindex is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frErrTable/FRAME-RELAY-DTE-MIB:frErrEntry[FRAME-RELAY-DTE-MIB:frErrIfIndex = ' + str(self.frerrifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frerrifindex is not None:
                    return True

                if self.frerrdata is not None:
                    return True

                if self.frerrfaults is not None:
                    return True

                if self.frerrfaulttime is not None:
                    return True

                if self.frerrtime is not None:
                    return True

                if self.frerrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FRAMERELAYDTEMIB.FrErrTable.FrErrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frErrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frerrentry is not None:
                for child_ref in self.frerrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FRAMERELAYDTEMIB.FrErrTable']['meta_info']


    class FrameRelayTrapControl(object):
        """
        
        
        .. attribute:: frtrapmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between trap emissions.  If events occur more rapidly, the impementation may simply fail to trap, or may queue traps until an appropriate time
        	**type**\: int
        
        	**range:** 0..3600000
        
        .. attribute:: frtrapstate
        
        	This variable indicates whether the system produces the frDLCIStatusChange trap
        	**type**\: :py:class:`FrTrapState_Enum <ydk.models.frame.FRAME_RELAY_DTE_MIB.FRAMERELAYDTEMIB.FrameRelayTrapControl.FrTrapState_Enum>`
        
        

        """

        _prefix = 'frame-relay'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frtrapmaxrate = None
            self.frtrapstate = None

        class FrTrapState_Enum(Enum):
            """
            FrTrapState_Enum

            This variable indicates whether the system produces
            the frDLCIStatusChange trap.

            """

            ENABLED = 1

            DISABLED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FRAMERELAYDTEMIB.FrameRelayTrapControl.FrTrapState_Enum']


        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frameRelayTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frtrapmaxrate is not None:
                return True

            if self.frtrapstate is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FRAMERELAYDTEMIB.FrameRelayTrapControl']['meta_info']

    @property
    def _common_path(self):

        return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.framerelaytrapcontrol is not None and self.framerelaytrapcontrol._has_data():
            return True

        if self.framerelaytrapcontrol is not None and self.framerelaytrapcontrol.is_presence():
            return True

        if self.frcircuittable is not None and self.frcircuittable._has_data():
            return True

        if self.frcircuittable is not None and self.frcircuittable.is_presence():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable._has_data():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable.is_presence():
            return True

        if self.frerrtable is not None and self.frerrtable._has_data():
            return True

        if self.frerrtable is not None and self.frerrtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.frame._meta import _FRAME_RELAY_DTE_MIB as meta
        return meta._meta_table['FRAMERELAYDTEMIB']['meta_info']


