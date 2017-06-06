""" FRAME_RELAY_DTE_MIB 

The MIB module to describe the use of a Frame Relay
interface by a DTE.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class FrameRelayDteMib(object):
    """
    
    
    .. attribute:: framerelaytrapcontrol
    
    	
    	**type**\:   :py:class:`Framerelaytrapcontrol <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Framerelaytrapcontrol>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connections (DLC) or virtual circuits
    	**type**\:   :py:class:`Frcircuittable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:   :py:class:`Frdlcmitable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface.  Discontinuities in the counters contained in this table are the same as apply to the ifEntry associated with the Interface
    	**type**\:   :py:class:`Frerrtable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable>`
    
    

    """

    _prefix = 'FRAME-RELAY-DTE-MIB'
    _revision = '1997-05-01'

    def __init__(self):
        self.framerelaytrapcontrol = FrameRelayDteMib.Framerelaytrapcontrol()
        self.framerelaytrapcontrol.parent = self
        self.frcircuittable = FrameRelayDteMib.Frcircuittable()
        self.frcircuittable.parent = self
        self.frdlcmitable = FrameRelayDteMib.Frdlcmitable()
        self.frdlcmitable.parent = self
        self.frerrtable = FrameRelayDteMib.Frerrtable()
        self.frerrtable.parent = self


    class Framerelaytrapcontrol(object):
        """
        
        
        .. attribute:: frtrapmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between trap emissions.  If events occur more rapidly, the impementation may simply fail to trap, or may queue traps until an appropriate time
        	**type**\:  int
        
        	**range:** 0..3600000
        
        .. attribute:: frtrapstate
        
        	This variable indicates whether the system produces the frDLCIStatusChange trap
        	**type**\:   :py:class:`FrtrapstateEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Framerelaytrapcontrol.FrtrapstateEnum>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frtrapmaxrate = None
            self.frtrapstate = None

        class FrtrapstateEnum(Enum):
            """
            FrtrapstateEnum

            This variable indicates whether the system produces

            the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FrameRelayDteMib.Framerelaytrapcontrol.FrtrapstateEnum']


        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frameRelayTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frtrapmaxrate is not None:
                return True

            if self.frtrapstate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FrameRelayDteMib.Framerelaytrapcontrol']['meta_info']


    class Frdlcmitable(object):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Connection Management Interface
        	**type**\: list of    :py:class:`Frdlcmientry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frdlcmientry = YList()
            self.frdlcmientry.parent = self
            self.frdlcmientry.name = 'frdlcmientry'


        class Frdlcmientry(object):
            """
            The Parameters for a particular Data Link Connection
            Management Interface.
            
            .. attribute:: frdlcmiifindex  <key>
            
            	The ifIndex value of the corresponding ifEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address format is in use on the Frame Relay interface
            	**type**\:   :py:class:`FrdlcmiaddressEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states the address length in octets.  In the case of Q922 format, the length indicates the entire length of the address including the control portion
            	**type**\:   :py:class:`FrdlcmiaddresslenEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals that pass before issuance of a full status enquiry message
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for this interface.  Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or higher than the agent's maximal capability is configured, the agent should respond badValue
            	**type**\:  int
            
            	**range:** 0..8388607
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay interface is using a multicast service
            	**type**\:   :py:class:`FrdlcmimulticastEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between successive status enquiry messages
            	**type**\:  int
            
            	**range:** 5..30
            
            	**units**\: seconds
            
            .. attribute:: frdlcmirowstatus
            
            	SNMP Version 2 Row Status Variable.  Writable objects in the table may be written in any RowStatus state
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data Link Connection Management scheme is active (and by implication, what DLCI it uses) on the Frame Relay interface
            	**type**\:   :py:class:`FrdlcmistateEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum>`
            
            .. attribute:: frdlcmistatus
            
            	This indicates the status of the Frame Relay interface as determined by the performance of the dlcmi.  If no dlcmi is running, the Frame Relay interface will stay in the running state indefinitely
            	**type**\:   :py:class:`FrdlcmistatusEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistatusEnum>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
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

            class FrdlcmiaddressEnum(Enum):
                """
                FrdlcmiaddressEnum

                This variable states which address format is in use on

                the Frame Relay interface.

                .. data:: q921 = 1

                .. data:: q922March90 = 2

                .. data:: q922November90 = 3

                .. data:: q922 = 4

                """

                q921 = 1

                q922March90 = 2

                q922November90 = 3

                q922 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum']


            class FrdlcmiaddresslenEnum(Enum):
                """
                FrdlcmiaddresslenEnum

                This variable states the address length in octets.  In

                the case of Q922 format, the length indicates the

                entire length of the address including the control

                portion.

                .. data:: twoOctets = 2

                .. data:: threeOctets = 3

                .. data:: fourOctets = 4

                """

                twoOctets = 2

                threeOctets = 3

                fourOctets = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum']


            class FrdlcmimulticastEnum(Enum):
                """
                FrdlcmimulticastEnum

                This indicates whether the Frame Relay interface is

                using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = 1

                broadcast = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum']


            class FrdlcmistateEnum(Enum):
                """
                FrdlcmistateEnum

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

                noLmiConfigured = 1

                lmiRev1 = 2

                ansiT1617D = 3

                ansiT1617B = 4

                itut933A = 5

                ansiT1617D1994 = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum']


            class FrdlcmistatusEnum(Enum):
                """
                FrdlcmistatusEnum

                This indicates the status of the Frame Relay interface

                as determined by the performance of the dlcmi.  If no

                dlcmi is running, the Frame Relay interface will stay

                in the running state indefinitely.

                .. data:: running = 1

                .. data:: fault = 2

                .. data:: initializing = 3

                """

                running = 1

                fault = 2

                initializing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistatusEnum']


            @property
            def _common_path(self):
                if self.frdlcmiifindex is None:
                    raise YPYModelError('Key property frdlcmiifindex is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frDlcmiTable/FRAME-RELAY-DTE-MIB:frDlcmiEntry[FRAME-RELAY-DTE-MIB:frDlcmiIfIndex = ' + str(self.frdlcmiifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frDlcmiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frdlcmientry is not None:
                for child_ref in self.frdlcmientry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FrameRelayDteMib.Frdlcmitable']['meta_info']


    class Frcircuittable(object):
        """
        A table containing information about specific Data
        Link Connections (DLC) or virtual circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single Data Link Connection.  Discontinuities in the counters contained in this table are indicated by the value in frCircuitCreationTime
        	**type**\: list of    :py:class:`Frcircuitentry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frcircuitentry = YList()
            self.frcircuitentry.parent = self
            self.frcircuitentry.name = 'frcircuitentry'


        class Frcircuitentry(object):
            """
            The information regarding a single Data Link
            Connection.  Discontinuities in the counters contained
            in this table are indicated by the value in
            frCircuitCreationTime.
            
            .. attribute:: frcircuitifindex  <key>
            
            	The ifIndex Value of the ifEntry this virtual circuit is layered onto
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitdlci  <key>
            
            	The Data Link Connection Identifier for this virtual circuit
            	**type**\:  int
            
            	**range:** 0..8388607
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount of data, in bits, that the network agrees to transfer under normal conditions, during the measurement interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the virtual circuit was created, whether by the Data Link Connection Management Interface or by a SetRequest
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitdiscards
            
            	The number of inbound frames dropped because of format errors, or because the VC is inactive
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount of uncommitted data bits that the network will attempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there was a change in the virtual circuit state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitlogicalifindex
            
            	Normally the same value as frDlcmiIfIndex, but different when an implementation associates a virtual ifEntry with a DLC or set of DLCs in order to associate higher layer objects such as the ipAddrEntry with a subset of the virtual circuits on a Frame Relay interface. The type of such ifEntries is defined by the higher layer object; for example, if PPP/Frame Relay is implemented, the ifType of this ifEntry would be PPP. If it is not so defined, as would be the case with an ipAddrEntry, it should be of type Other
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitmulticast
            
            	This indicates whether this VC is used as a unicast VC (i.e. not multicast) or the type of multicast service subscribed to
            	**type**\:   :py:class:`FrcircuitmulticastEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitmulticastEnum>`
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network indicating backward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the BECN flag, or when a switch in the network receives the frame from a trunk whose transmission queue is congested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceiveddes
            
            	Number of frames received from the network indicating that they were eligible for discard since the virtual circuit was created.  This occurs when the remote DTE sets the DE flag, or when in remote DTE's switch detects that the frame was received as Excess Burst data
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network indicating forward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the FECN flag, or when a switch in the network enqueues the frame to a trunk whose transmission queue is congested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received over this virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received over this virtual circuit since it was created.  Octets counted include the full frame relay header, but do not include the flag characters or the CRC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitrowstatus
            
            	This object is used to create a new row or modify or destroy an existing row in the manner described in the definition of the RowStatus textual convention. Writable objects in the table may be written in any RowStatus state
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: frcircuitsentdes
            
            	Number of frames sent to the network indicating that they were eligible for discard since the virtual circuit was created.   This occurs when the local DTE sets the DE flag, indicating that during Network congestion situations those frames should be discarded in preference of other frames sent without the DE bit set
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent from this virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent from this virtual circuit since it was created.  Octets counted are the full frame relay header and the payload, but do not include the flag characters or CRC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual circuit is operational.  In the absence of a Data Link Connection Management Interface, virtual circuit entries (rows) may be created by setting virtual circuit state to 'active', or deleted by changing Circuit state to 'invalid'.  Whether or not the row actually disappears is left to the implementation, so this object may actually read as 'invalid' for some arbitrary length of time.  It is also legal to set the state of a virtual circuit to 'inactive' to temporarily disable a given circuit.  The use of 'invalid' is deprecated in this SNMP Version 2 MIB, in favor of frCircuitRowStatus
            	**type**\:   :py:class:`FrcircuitstateEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Relay Information Field' bits transferred per second across a user network interface in one direction, measured over the measurement interval.  If the configured committed burst rate and throughput are both non\-zero, the measurement interval, T, is     T=frCircuitCommittedBurst/frCircuitThroughput.  If the configured committed burst rate and throughput are both zero, the measurement interval, T, is            T=frCircuitExcessBurst/ifSpeed
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuittype
            
            	Indication of whether the VC was manually created (static), or dynamically created (dynamic) via the data link control management interface
            	**type**\:   :py:class:`FrcircuittypeEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuittypeEnum>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                self.parent = None
                self.frcircuitifindex = None
                self.frcircuitdlci = None
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

            class FrcircuitmulticastEnum(Enum):
                """
                FrcircuitmulticastEnum

                This indicates whether this VC is used as a unicast VC

                (i.e. not multicast) or the type of multicast service

                subscribed to

                .. data:: unicast = 1

                .. data:: oneWay = 2

                .. data:: twoWay = 3

                .. data:: nWay = 4

                """

                unicast = 1

                oneWay = 2

                twoWay = 3

                nWay = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitmulticastEnum']


            class FrcircuitstateEnum(Enum):
                """
                FrcircuitstateEnum

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

                invalid = 1

                active = 2

                inactive = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum']


            class FrcircuittypeEnum(Enum):
                """
                FrcircuittypeEnum

                Indication of whether the VC was manually created

                (static), or dynamically created (dynamic) via the data

                link control management interface.

                .. data:: static = 1

                .. data:: dynamic = 2

                """

                static = 1

                dynamic = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuittypeEnum']


            @property
            def _common_path(self):
                if self.frcircuitifindex is None:
                    raise YPYModelError('Key property frcircuitifindex is None')
                if self.frcircuitdlci is None:
                    raise YPYModelError('Key property frcircuitdlci is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frCircuitTable/FRAME-RELAY-DTE-MIB:frCircuitEntry[FRAME-RELAY-DTE-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + '][FRAME-RELAY-DTE-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.frcircuitifindex is not None:
                    return True

                if self.frcircuitdlci is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FrameRelayDteMib.Frcircuittable.Frcircuitentry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frCircuitTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frcircuitentry is not None:
                for child_ref in self.frcircuitentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FrameRelayDteMib.Frcircuittable']['meta_info']


    class Frerrtable(object):
        """
        A table containing information about Errors on the
        Frame Relay interface.  Discontinuities in the counters
        contained in this table are the same as apply to the
        ifEntry associated with the Interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of    :py:class:`Frerrentry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable.Frerrentry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            self.parent = None
            self.frerrentry = YList()
            self.frerrentry.parent = self
            self.frerrentry.name = 'frerrentry'


        class Frerrentry(object):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  <key>
            
            	The ifIndex Value of the corresponding ifEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the error packet as possible.  As a minimum, it must contain the Q.922 Address or as much as was delivered.  It is desirable to include all header and demultiplexing information
            	**type**\:  str
            
            	**length:** 1..1600
            
            .. attribute:: frerrfaults
            
            	The number of times the interface has gone down since it was initialized
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrfaulttime
            
            	The value of sysUpTime at the time when the interface was taken down due to excessive errors.  Excessive errors is defined as the time when a DLCMI exceeds the frDlcmiErrorThreshold number of errors within frDlcmiMonitoredEvents. See FrDlcmiEntry for further details
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error was detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface\:  receiveShort\: frame was not long enough to allow         demultiplexing \- the address field was incomplete,         or for virtual circuits using Multiprotocol over         Frame Relay, the protocol identifier was missing         or incomplete.  receiveLong\: frame exceeded maximum length configured for this              interface.  illegalAddress\: address field did not match configured format.  unknownAddress\: frame received on a virtual circuit which was not                 active or administratively disabled.  dlcmiProtoErr\: unspecified error occurred when attempting to                interpret link maintenance frame.  dlcmiUnknownIE\: link maintenance frame contained an Information                 Element type which is not valid for the                 configured link maintenance protocol.  dlcmiSequenceErr\: link maintenance frame contained a sequence                   number other than the expected value.  dlcmiUnknownRpt\: link maintenance frame contained a Report Type                  Information Element whose value was not valid                  for the configured link maintenance protocol.  noErrorSinceReset\: no errors have been detected since the last                    cold start or warm start
            	**type**\:   :py:class:`FrerrtypeEnum <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable.Frerrentry.FrerrtypeEnum>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                self.parent = None
                self.frerrifindex = None
                self.frerrdata = None
                self.frerrfaults = None
                self.frerrfaulttime = None
                self.frerrtime = None
                self.frerrtype = None

            class FrerrtypeEnum(Enum):
                """
                FrerrtypeEnum

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

                unknownError = 1

                receiveShort = 2

                receiveLong = 3

                illegalAddress = 4

                unknownAddress = 5

                dlcmiProtoErr = 6

                dlcmiUnknownIE = 7

                dlcmiSequenceErr = 8

                dlcmiUnknownRpt = 9

                noErrorSinceReset = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                    return meta._meta_table['FrameRelayDteMib.Frerrtable.Frerrentry.FrerrtypeEnum']


            @property
            def _common_path(self):
                if self.frerrifindex is None:
                    raise YPYModelError('Key property frerrifindex is None')

                return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frErrTable/FRAME-RELAY-DTE-MIB:frErrEntry[FRAME-RELAY-DTE-MIB:frErrIfIndex = ' + str(self.frerrifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
                return meta._meta_table['FrameRelayDteMib.Frerrtable.Frerrentry']['meta_info']

        @property
        def _common_path(self):

            return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/FRAME-RELAY-DTE-MIB:frErrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frerrentry is not None:
                for child_ref in self.frerrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
            return meta._meta_table['FrameRelayDteMib.Frerrtable']['meta_info']

    @property
    def _common_path(self):

        return '/FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.framerelaytrapcontrol is not None and self.framerelaytrapcontrol._has_data():
            return True

        if self.frcircuittable is not None and self.frcircuittable._has_data():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable._has_data():
            return True

        if self.frerrtable is not None and self.frerrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _FRAME_RELAY_DTE_MIB as meta
        return meta._meta_table['FrameRelayDteMib']['meta_info']


