""" CISCO_DOT3_OAM_MIB 

The MIB module for managing the new Ethernet OAM features
introduced by the Ethernet in the First Mile task force (IEEE
802.3ah).  The functionality presented here is based on IEEE
802.3ah [802.3ah], released in October, 2004.  [802.3ah] was
prepared as an addendum to the standing version of IEEE 802.3
[802.3\-2002] at the time.  Since then, [802.3ah] has been
merged into the base IEEE 802.3 specification in [802.3\-2005].

In particular, this MIB focuses on the new OAM functions
introduced in Clause 57 of [802.3ah].  The OAM functionality
of Clause 57 is controlled by new management attributes
introduced in Clause 30 of [802.3ah].  The OAM functions are
not specific to any particular Ethernet physical layer, and
can be generically applied to any Ethernet interface of
[802.3\-2002].  

An Ethernet OAM protocol data unit is a valid Ethernet frame
with a destination MAC address equal to the reserved MAC
address for Slow Protocols (See 43B of [802.3ah]), a
lengthOrType field equal to the reserved type for Slow
Protocols, and a Slow Protocols subtype equal to that of the
subtype reserved for Ethernet OAM.  OAMPDU is used throughout
this document as an abbreviation for Ethernet OAM protocol
data unit.  

The following reference is used throughout this MIB module\:  

  [802.3ah] refers to\:
    IEEE Std 802.3ah\-2004\: 'Draft amendment to \-
    Information technology \- Telecommunications and
    information exchange between systems \- Local and
    metropolitan are networks \- Specific requirements \- Part
    3\: Carrier sense multiple access with collision detection
    (CSMA/CD) access method and physical layer specifications
    \- Media Access Control Parameters, Physical Layers and
    Management Parameters for subscriber access networks',
    October 2004.

  [802.3\-2002] refers to\:
    IEEE Std 802.3\-2002\: 
    'Information technology \- Telecommunications and
    information exchange between systems \- Local and
    metropolitan are networks \- Specific requirements \- Part
    3\: Carrier sense multiple access with collision detection
    (CSMA/CD) access method and physical layer specifications
    \- Media Access Control Parameters, Physical Layers and
    Management Parameters for subscriber access networks',
    March 2002.

  [802.3\-2005] refers to\:
    IEEE Std 802.3\-2002\: 
    'Information technology \- Telecommunications and
    information exchange between systems \- Local and
    metropolitan are networks \- Specific requirements \- Part
    3\: Carrier sense multiple access with collision detection
    (CSMA/CD) access method and physical layer specifications
    \- Media Access Control Parameters, Physical Layers and
    Management Parameters for subscriber access networks',
    December 2005.

  [802\-2001] refers to\:
    'IEEE Standard for LAN/MAN (Local Area
    Network/Metropolitan Area Network)\: Overview and
    Architecture', IEEE 802, June 2001.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoDot3OamMib(object):
    """
    
    
    .. attribute:: cdot3oameventconfigtable
    
    	Ethernet OAM includes the ability to generate and receive Event Notification OAMPDUs to indicate various link problems. This table contains the mechanisms to enable Event Notifications and configure the thresholds to generate the standard Ethernet OAM events.  There is one entry in the table for every entry in cdot3OamTable that supports OAM events (where cdot3OamFunctionsSupported includes the eventSupport bit set). The values in the table are maintained across changes to cdot3OamOperStatus.    The standard threshold crossing events are\:   \- Errored Symbol Period Event.  Generated when the number of     symbol errors exceeds a threshold within a given window      defined by a number of symbols (for example, 1,000 symbols     out of 1,000,000 had errors).     \- Errored Frame Period Event.  Generated when the number of      frame errors exceeds a threshold within a given window      defined by a number of frames (for example, 10 frames out     of 1000 had errors).     \- Errored Frame Event.  Generated when the number of frame      errors exceeds a threshold within a given window defined      by a period of time (for example, 10 frames in 1 second      had errors).   \- Errored Frame Seconds Summary Event.  Generated when the      number of errored frame seconds exceeds a threshold within     a given time period (for example, 10 errored frame seconds     within the last 100 seconds).  An errored frame second is      defined as a 1 second interval which had >0 frame errors.   There are other events (dying gasp, critical events) that are not threshold crossing events but which can be enabled/disabled via this table.  
    	**type**\:   :py:class:`Cdot3Oameventconfigtable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oameventconfigtable>`
    
    .. attribute:: cdot3oameventlogtable
    
    	This table records a history of the events that have occurred at the Ethernet OAM level.  These events can include locally detected events, which may result in locally generated OAMPDUs, and remotely detected events, which are detected by the OAM peer entity and signaled to the local entity via Ethernet OAM.  Ethernet OAM events can be signaled by Event Notification OAMPDUs or by the flags field in any OAMPDU.    This table contains both threshold crossing events and non\-threshold crossing events.  The parameters for the threshold window, threshold value, and actual value (cdot3OamEventLogWindowXX, cdot3OamEventLogThresholdXX, cdot3OamEventLogValue) are only applicable to threshold crossing events, and are returned as all F's (2^32 \- 1) for non\-threshold crossing events.   Entries in the table are automatically created when such events are detected.  The size of the table is implementation dependent.  When the table reaches its maximum size, older entries are automatically deleted to make room for newer entries. 
    	**type**\:   :py:class:`Cdot3Oameventlogtable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oameventlogtable>`
    
    .. attribute:: cdot3oamloopbacktable
    
    	This table contains controls for the loopback state of the local link as well as indicating the status of the loopback function.  There is one entry in this table for each entry in cdot3OamTable that supports loopback functionality (where cdot3OamFunctionsSupported includes the loopbackSupport bit set).  Loopback can be used to place the remote OAM entity in a state where every received frame (except OAMPDUs) is echoed back over the same interface on which they were received.   In this state, at the remote entity, 'normal' traffic is disabled as only the looped back frames are transmitted on the interface. Loopback is thus an intrusive operation that prohibits normal data flow and should be used accordingly.  
    	**type**\:   :py:class:`Cdot3Oamloopbacktable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamloopbacktable>`
    
    .. attribute:: cdot3oampeertable
    
    	This table contains information about the OAM peer for a particular Ethernet like interface. OAM entities communicate with a single OAM peer entity on Ethernet links on which OAM is enabled and operating properly.  There is one entry in this table for each entry in the cdot3OamTable for which information on the peer OAM entity is available.  
    	**type**\:   :py:class:`Cdot3Oampeertable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oampeertable>`
    
    .. attribute:: cdot3oamstatstable
    
    	This table contains statistics for the OAM function on a particular Ethernet like interface. There is an entry in the table for every entry in the cdot3OamTable.   The counters in this table are defined as 32\-bit entries to match the counter size as defined in [802.3ah].  Given the OAM protocol is a slow protocol, the counters increment at a slow rate. 
    	**type**\:   :py:class:`Cdot3Oamstatstable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamstatstable>`
    
    .. attribute:: cdot3oamtable
    
    	This table contains the primary controls and status for the OAM capabilities of an Ethernet like interface.  There will be one row in this table for each Ethernet like interface in the system that supports the OAM functions defined in [802.3ah]
    	**type**\:   :py:class:`Cdot3Oamtable <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable>`
    
    

    """

    _prefix = 'CISCO-DOT3-OAM-MIB'
    _revision = '2006-05-31'

    def __init__(self):
        self.cdot3oameventconfigtable = CiscoDot3OamMib.Cdot3Oameventconfigtable()
        self.cdot3oameventconfigtable.parent = self
        self.cdot3oameventlogtable = CiscoDot3OamMib.Cdot3Oameventlogtable()
        self.cdot3oameventlogtable.parent = self
        self.cdot3oamloopbacktable = CiscoDot3OamMib.Cdot3Oamloopbacktable()
        self.cdot3oamloopbacktable.parent = self
        self.cdot3oampeertable = CiscoDot3OamMib.Cdot3Oampeertable()
        self.cdot3oampeertable.parent = self
        self.cdot3oamstatstable = CiscoDot3OamMib.Cdot3Oamstatstable()
        self.cdot3oamstatstable.parent = self
        self.cdot3oamtable = CiscoDot3OamMib.Cdot3Oamtable()
        self.cdot3oamtable.parent = self


    class Cdot3Oamtable(object):
        """
        This table contains the primary controls and status for the
        OAM capabilities of an Ethernet like interface.  There will be
        one row in this table for each Ethernet like interface in the
        system that supports the OAM functions defined in [802.3ah].
        
        .. attribute:: cdot3oamentry
        
        	An entry in the table, containing information on the Ethernet OAM function for a single Ethernet like interface. Entries in the table are created automatically for each interface supporting Ethernet OAM. The status of the row entry can be determined from cdot3OamOperStatus.    A cdot3OamEntry is indexed in the cdot3OamTable by the ifIndex object of the Interfaces MIB.  
        	**type**\: list of    :py:class:`Cdot3Oamentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oamentry = YList()
            self.cdot3oamentry.parent = self
            self.cdot3oamentry.name = 'cdot3oamentry'


        class Cdot3Oamentry(object):
            """
            An entry in the table, containing information on the Ethernet
            OAM function for a single Ethernet like interface. Entries in
            the table are created automatically for each interface
            supporting Ethernet OAM. The status of the row entry can be
            determined from cdot3OamOperStatus.  
            
            A cdot3OamEntry is indexed in the cdot3OamTable by the ifIndex
            object of the Interfaces MIB.  
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oamadminstate
            
            	This object is used to provision the default administrative OAM mode for this interface.  This object represents the desired state of OAM for this interface.    The cdot3OamAdminState always starts in the disabled(1) state until an explicit management action or configuration information retained by the system causes a transition to the enabled(2) state.   When enabled(2), Ethernet OAM will attempt to operate over this interface.  
            	**type**\:   :py:class:`Cdot3OamadminstateEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamadminstateEnum>`
            
            .. attribute:: cdot3oamconfigrevision
            
            	The configuration revision of the OAM entity as reflected in the latest OAMPDU sent by the OAM entity.  The config revision is used by OAM entities to indicate configuration changes have occurred which might require the peer OAM entity to re\-evaluate whether OAM peering is allowed. 
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cdot3oamfunctionssupported
            
            	The OAM functions supported on this Ethernet like interface. OAM consists of separate functional sets beyond the basic discovery process which is always required.  These functional groups can be supported independently by any implementation. These values are communicated to the peer via the local configuration field of Information OAMPDUs.    Setting 'unidirectionalSupport(0)' indicates that the OAM entity supports the transmission of OAMPDUs on links that are operating in unidirectional mode (traffic flowing in one direction only).  Setting 'loopbackSupport(1)' indicates the OAM entity can initiate and respond to loopback commands. Setting 'eventSupport(2)' indicates the OAM entity can send and receive Event Notification OAMPDUs. Setting 'variableSupport(3)' indicates the OAM entity can send and receive Variable Request and Response OAMPDUs.  
            	**type**\:   :py:class:`Cdot3Oamfunctionssupported <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3Oamfunctionssupported>`
            
            .. attribute:: cdot3oammaxoampdusize
            
            	The largest OAMPDU that the OAM entity supports.  OAM entities exchange maximum OAMPDU sizes and negotiate to use the smaller of the two maximum OAMPDU sizes between the peers. This value is determined by the local implementation.  
            	**type**\:  int
            
            	**range:** 64..1518
            
            	**units**\: octets
            
            .. attribute:: cdot3oammode
            
            	This object configures the mode of OAM operation for this Ethernet like interface.  OAM on Ethernet interfaces may be in 'active' mode or 'passive' mode.  These two modes differ in that active mode provides additional capabilities to initiate monitoring activities with the remote OAM peer entity, while passive mode generally waits for the peer to initiate OAM actions with it.  As an example, an active OAM entity can put the remote OAM entity in a loopback state, where a passive OAM entity cannot.    The default value of cdot3OamMode is dependent on the type of system on which this Ethernet like interface resides.  The default value should be 'active(1)' unless it is known that this system should take on a subservient role to the other device connected over this interface.    Changing this value results in incrementing the configuration revision field of locally generated OAMPDUs (30.3.6.1.12) and potentially re\-doing the OAM discovery process if the cdot3OamOperStatus was already operational(9).  
            	**type**\:   :py:class:`Cdot3OammodeEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OammodeEnum>`
            
            .. attribute:: cdot3oamoperstatus
            
            	At initialization and failure conditions, two OAM entities on the same full\-duplex Ethernet link begin a discovery phase to determine what OAM capabilities may be used on that link.  The progress of this initialization is controlled by the OAM sublayer.               This value is always disabled(1) if OAM is disabled on this interface via the cdot3OamAdminState.    If the link has detected a fault and is transmitting OAMPDUs with a link fault indication, the value is linkFault(2). Also, if the interface is not operational (ifOperStatus is not  up(1)), linkFault(2) is returned.  Note that the object  ifOperStatus may not be up(1) as a result of link failure or administrative action (ifAdminState being down(2) or testing(3)).                     The passiveWait(3) state is returned only by OAM entities in passive mode (cdot3OamMode) and reflects the state in which the OAM entity is waiting to see if the peer device is OAM capable.  The activeSendLocal(4) value is used by active mode devices (cdot3OamMode) and reflects the OAM entity actively trying to discover whether the peer has OAM capability but has not yet made that determination.                     The state sendLocalAndRemote(5) reflects that the local OAM entity has discovered the peer but has not yet accepted or rejected the configuration of the peer.  The local device can, for whatever reason, decide that the peer device is unacceptable and decline OAM peering.  If the local OAM entity rejects the peer OAM entity, the state becomes oamPeeringLocallyRejected(7).  If the OAM peering is allowed by the local device, the state moves to sendLocalAndRemoteOk(6).  Note that both the sendLocalAndRemote(5) and oamPeeringLocallyRejected(7) states fall within the state SEND\_LOCAL\_REMOTE of the Discovery state diagram [802.3ah, Figure 57\-5], with the difference being whether the local OAM client has actively rejected the peering or has just not indicated any decision yet.  Whether a peering decision has been made is indicated via the local flags field in the OAMPDU (reflected in the aOAMLocalFlagsField of 30.3.6.1.10).    If the remote OAM entity rejects the peering, the state becomes oamPeeringRemotelyRejected(8).  Note that both the sendLocalAndRemoteOk(6) and oamPeeringRemotelyRejected(8) states fall within the state SEND\_LOCAL\_REMOTE\_OK of the Discovery state diagram [802.3ah, Figure 57\-5], with the difference being whether the remote OAM client has rejected the peering or has just not yet decided.  This is indicated via the remote flags field in the OAM PDU (reflected in the aOAMRemoteFlagsField of 30.3.6.1.11).                     When the local OAM entity learns that both it and the remote OAM entity have accepted the peering, the state moves to operational(9) corresponding to the SEND\_ANY state of the Discovery state diagram [802.3ah, Figure 57\-5].    Since Ethernet OAM functions are not designed to work completely over half\-duplex interfaces, the value nonOperHalfDuplex(10) is returned whenever Ethernet OAM is enabled (cdot3OamAdminState is enabled(1)) but the interface is in half\-duplex operation.  
            	**type**\:   :py:class:`Cdot3OamoperstatusEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamoperstatusEnum>`
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oamadminstate = None
                self.cdot3oamconfigrevision = None
                self.cdot3oamfunctionssupported = CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3Oamfunctionssupported()
                self.cdot3oammaxoampdusize = None
                self.cdot3oammode = None
                self.cdot3oamoperstatus = None

            class Cdot3OamadminstateEnum(Enum):
                """
                Cdot3OamadminstateEnum

                This object is used to provision the default administrative

                OAM mode for this interface.  This object represents the

                desired state of OAM for this interface.  

                The cdot3OamAdminState always starts in the disabled(1) state

                until an explicit management action or configuration

                information retained by the system causes a transition to the

                enabled(2) state.   When enabled(2), Ethernet OAM will attempt

                to operate over this interface.  

                .. data:: disabled = 1

                .. data:: enabled = 2

                """

                disabled = 1

                enabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamadminstateEnum']


            class Cdot3OammodeEnum(Enum):
                """
                Cdot3OammodeEnum

                This object configures the mode of OAM operation for this

                Ethernet like interface.  OAM on Ethernet interfaces may be in

                'active' mode or 'passive' mode.  These two modes differ in

                that active mode provides additional capabilities to initiate

                monitoring activities with the remote OAM peer entity, while

                passive mode generally waits for the peer to initiate OAM

                actions with it.  As an example, an active OAM entity can put

                the remote OAM entity in a loopback state, where a passive OAM

                entity cannot.  

                The default value of cdot3OamMode is dependent on the type of

                system on which this Ethernet like interface resides.  The

                default value should be 'active(1)' unless it is known that

                this system should take on a subservient role to the other

                device connected over this interface.  

                Changing this value results in incrementing the configuration

                revision field of locally generated OAMPDUs (30.3.6.1.12) and

                potentially re\-doing the OAM discovery process if the

                cdot3OamOperStatus was already operational(9).  

                .. data:: active = 1

                .. data:: passive = 2

                """

                active = 1

                passive = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OammodeEnum']


            class Cdot3OamoperstatusEnum(Enum):
                """
                Cdot3OamoperstatusEnum

                At initialization and failure conditions, two OAM entities on

                the same full\-duplex Ethernet link begin a discovery phase to

                determine what OAM capabilities may be used on that link.  The

                progress of this initialization is controlled by the OAM

                sublayer.  

                This value is always disabled(1) if OAM is disabled on this

                interface via the cdot3OamAdminState.  

                If the link has detected a fault and is transmitting OAMPDUs

                with a link fault indication, the value is linkFault(2). Also,

                if the interface is not operational (ifOperStatus is not 

                up(1)), linkFault(2) is returned.  Note that the object 

                ifOperStatus may not be up(1) as a result of link failure or

                administrative action (ifAdminState being down(2) or

                testing(3)).  

                The passiveWait(3) state is returned only by OAM entities in

                passive mode (cdot3OamMode) and reflects the state in which the

                OAM entity is waiting to see if the peer device is OAM

                capable.  The activeSendLocal(4) value is used by active mode

                devices (cdot3OamMode) and reflects the OAM entity actively

                trying to discover whether the peer has OAM capability but has

                not yet made that determination.  

                The state sendLocalAndRemote(5) reflects that the local OAM

                entity has discovered the peer but has not yet accepted or

                rejected the configuration of the peer.  The local device can,

                for whatever reason, decide that the peer device is

                unacceptable and decline OAM peering.  If the local OAM entity

                rejects the peer OAM entity, the state becomes

                oamPeeringLocallyRejected(7).  If the OAM peering is allowed

                by the local device, the state moves to

                sendLocalAndRemoteOk(6).  Note that both the

                sendLocalAndRemote(5) and oamPeeringLocallyRejected(7) states

                fall within the state SEND\_LOCAL\_REMOTE of the Discovery state

                diagram [802.3ah, Figure 57\-5], with the difference being

                whether the local OAM client has actively rejected the peering

                or has just not indicated any decision yet.  Whether a peering

                decision has been made is indicated via the local flags field

                in the OAMPDU (reflected in the aOAMLocalFlagsField of

                30.3.6.1.10).  

                If the remote OAM entity rejects the peering, the state

                becomes oamPeeringRemotelyRejected(8).  Note that both the

                sendLocalAndRemoteOk(6) and oamPeeringRemotelyRejected(8)

                states fall within the state SEND\_LOCAL\_REMOTE\_OK of the

                Discovery state diagram [802.3ah, Figure 57\-5], with the

                difference being whether the remote OAM client has rejected

                the peering or has just not yet decided.  This is indicated

                via the remote flags field in the OAM PDU (reflected in the

                aOAMRemoteFlagsField of 30.3.6.1.11).  

                When the local OAM entity learns that both it and the remote

                OAM entity have accepted the peering, the state moves to

                operational(9) corresponding to the SEND\_ANY state of the

                Discovery state diagram [802.3ah, Figure 57\-5].  

                Since Ethernet OAM functions are not designed to work

                completely over half\-duplex interfaces, the value

                nonOperHalfDuplex(10) is returned whenever Ethernet OAM is

                enabled (cdot3OamAdminState is enabled(1)) but the interface is

                in half\-duplex operation.  

                .. data:: disabled = 1

                .. data:: linkFault = 2

                .. data:: passiveWait = 3

                .. data:: activeSendLocal = 4

                .. data:: sendLocalAndRemote = 5

                .. data:: sendLocalAndRemoteOk = 6

                .. data:: oamPeeringLocallyRejected = 7

                .. data:: oamPeeringRemotelyRejected = 8

                .. data:: operational = 9

                .. data:: nonOperHalfDuplex = 10

                """

                disabled = 1

                linkFault = 2

                passiveWait = 3

                activeSendLocal = 4

                sendLocalAndRemote = 5

                sendLocalAndRemoteOk = 6

                oamPeeringLocallyRejected = 7

                oamPeeringRemotelyRejected = 8

                operational = 9

                nonOperHalfDuplex = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamoperstatusEnum']


            class Cdot3Oamfunctionssupported(FixedBitsDict):
                """
                Cdot3Oamfunctionssupported

                The OAM functions supported on this Ethernet like interface.
                OAM consists of separate functional sets beyond the basic
                discovery process which is always required.  These functional
                groups can be supported independently by any implementation.
                These values are communicated to the peer via the local
                configuration field of Information OAMPDUs.  
                
                Setting 'unidirectionalSupport(0)' indicates that the OAM
                entity supports the transmission of OAMPDUs on links that are
                operating in unidirectional mode (traffic flowing in one
                direction only).  Setting 'loopbackSupport(1)' indicates the
                OAM entity can initiate and respond to loopback commands.
                Setting 'eventSupport(2)' indicates the OAM entity can send
                and receive Event Notification OAMPDUs. Setting
                'variableSupport(3)' indicates the OAM entity can send and
                receive Variable Request and Response OAMPDUs.  
                Keys are:- loopbackSupport , eventSupport , variableSupport , unidirectionalSupport

                """

                def __init__(self):
                    self._dictionary = { 
                        'loopbackSupport':False,
                        'eventSupport':False,
                        'variableSupport':False,
                        'unidirectionalSupport':False,
                    }
                    self._pos_map = { 
                        'loopbackSupport':1,
                        'eventSupport':2,
                        'variableSupport':3,
                        'unidirectionalSupport':0,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamTable/CISCO-DOT3-OAM-MIB:cdot3OamEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oamadminstate is not None:
                    return True

                if self.cdot3oamconfigrevision is not None:
                    return True

                if self.cdot3oamfunctionssupported is not None:
                    if self.cdot3oamfunctionssupported._has_data():
                        return True

                if self.cdot3oammaxoampdusize is not None:
                    return True

                if self.cdot3oammode is not None:
                    return True

                if self.cdot3oamoperstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oamentry is not None:
                for child_ref in self.cdot3oamentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oamtable']['meta_info']


    class Cdot3Oampeertable(object):
        """
        This table contains information about the OAM peer for a
        particular Ethernet like interface. OAM entities communicate
        with a single OAM peer entity on Ethernet links on which OAM
        is enabled and operating properly.  There is one entry in this
        table for each entry in the cdot3OamTable for which information
        on the peer OAM entity is available.  
        
        .. attribute:: cdot3oampeerentry
        
        	An entry in the table, containing information on the peer OAM entity for a single Ethernet like interface.    Note that there is at most one OAM peer for each Ethernet like interface.  Entries are automatically created when information about the OAM peer entity becomes available, and automatically deleted when the OAM peer entity is no longer in communication.  Peer information is not available when cdot3OamOperStatus is disabled(1), linkFault(2), passiveWait(3), activeSendLocal(4). or nonOperHalfDuplex(10)). 
        	**type**\: list of    :py:class:`Cdot3Oampeerentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oampeerentry = YList()
            self.cdot3oampeerentry.parent = self
            self.cdot3oampeerentry.name = 'cdot3oampeerentry'


        class Cdot3Oampeerentry(object):
            """
            An entry in the table, containing information on the peer OAM
            entity for a single Ethernet like interface.  
            
            Note that there is at most one OAM peer for each Ethernet like
            interface.  Entries are automatically created when information
            about the OAM peer entity becomes available, and automatically
            deleted when the OAM peer entity is no longer in
            communication.  Peer information is not available when
            cdot3OamOperStatus is disabled(1), linkFault(2),
            passiveWait(3), activeSendLocal(4). or nonOperHalfDuplex(10)). 
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oampeerconfigrevision
            
            	The configuration revision of the OAM peer as reflected in the latest OAMPDU.  This attribute is changed by the peer whenever it has a local configuration change for Ethernet OAM this interface.  The configuration revision can be determined from the Revision field of the Local Information TLV of the most recently received Information OAMPDU with a Local Information TLV. A value of zero is returned if no Local Information TLV has been received.  
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cdot3oampeerfunctionssupported
            
            	The OAM functions supported on this Ethernet like interface. OAM consists of separate functionality sets above the basic discovery process.  This value indicates the capabilities of the peer OAM entity with respect to these functions.  This value is initialized so all bits are clear.   If unidirectionalSupport(0) is set, then the peer OAM entity supports sending OAM frames on Ethernet interfaces when the receive path is known to be inoperable.   If loopbackSupport(1) is set, then the peer OAM entity can send and receive OAM loopback commands.  If eventSupport(2) is set, then the peer OAM entity can send and receive event OAMPDUs to signal various error conditions. If variableSupport(3) is set, then the peer OAM entity can send and receive variable requests to monitor attribute value as described in Clause 57 of [802.3ah].     The capabilities of the OAM peer can be determined from the configuration field of the Local Information TLV of the most recently received Information OAMPDU with a Local Information TLV.  All zeros are returned if no Local Information TLV has yet been received. 
            	**type**\:   :py:class:`Cdot3Oampeerfunctionssupported <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3Oampeerfunctionssupported>`
            
            .. attribute:: cdot3oampeermacaddress
            
            	The MAC address of the peer OAM entity.  The MAC address is derived from the most recently received OAMPDU
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: cdot3oampeermaxoampdusize
            
            	The maximum size of OAMPDU supported by the peer as reflected in the latest Information OAMPDU received with a Local Information TLV.   Ethernet OAM on this interface must not use OAMPDUs that exceed this size.  The maximum OAMPDU size can be determined from the PDU Configuration field of the Local Information TLV of the last Information OAMPDU received from the peer.  A value of zero is returned if no Local Information TLV has been received.  Otherwise, the value of the OAM peer's maximum OAMPDU size is returned in this value.   Note that the values 1..63 are invalid sizes for Ethernet frames and should never appear. 
            	**type**\:  int
            
            	**range:** 0..1518
            
            	**units**\: octets
            
            .. attribute:: cdot3oampeermode
            
            	The mode of the OAM peer as reflected in the latest Information OAMPDU received with a Local Information TLV.  The mode of the peer can be determined from the Configuration field in the Local Information TLV of the last Information OAMPDU received from the peer.  The value is unknown(3) whenever no Local Information TLV has been received.  The values of active(1) and passive(2) are returned when a Local Information TLV has been received indicating the peer is in active or passive mode, respectively. 
            	**type**\:   :py:class:`Cdot3OampeermodeEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3OampeermodeEnum>`
            
            .. attribute:: cdot3oampeervendorinfo
            
            	The Vendor Info of the OAM peer as reflected in the latest Information OAMPDU received with a Local Information TLV.  The vendor information field is within the Local Information TLV, and can be used to determine additional information about the peer entity.  The format of the vendor information is unspecified within the 32\-bit field.  This value is initialized to zero before any Local Information TLV is received.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oampeervendoroui
            
            	The OUI of the OAM peer as reflected in the latest Information OAMPDU received with a Local Information TLV.  The OUI can be used to identify the vendor of the remote OAM entity.  This value is initialized to zero before any Local Information TLV is received.  
            	**type**\:  str
            
            	**length:** 3
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oampeerconfigrevision = None
                self.cdot3oampeerfunctionssupported = CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3Oampeerfunctionssupported()
                self.cdot3oampeermacaddress = None
                self.cdot3oampeermaxoampdusize = None
                self.cdot3oampeermode = None
                self.cdot3oampeervendorinfo = None
                self.cdot3oampeervendoroui = None

            class Cdot3OampeermodeEnum(Enum):
                """
                Cdot3OampeermodeEnum

                The mode of the OAM peer as reflected in the latest

                Information OAMPDU received with a Local Information TLV.  The

                mode of the peer can be determined from the Configuration

                field in the Local Information TLV of the last Information

                OAMPDU received from the peer.  The value is unknown(3)

                whenever no Local Information TLV has been received.  The

                values of active(1) and passive(2) are returned when a Local

                Information TLV has been received indicating the peer is in

                active or passive mode, respectively. 

                .. data:: active = 1

                .. data:: passive = 2

                .. data:: unknown = 3

                """

                active = 1

                passive = 2

                unknown = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3OampeermodeEnum']


            class Cdot3Oampeerfunctionssupported(FixedBitsDict):
                """
                Cdot3Oampeerfunctionssupported

                The OAM functions supported on this Ethernet like interface.
                OAM consists of separate functionality sets above the basic
                discovery process.  This value indicates the capabilities of
                the peer OAM entity with respect to these functions.  This
                value is initialized so all bits are clear. 
                
                If unidirectionalSupport(0) is set, then the peer OAM entity
                supports sending OAM frames on Ethernet interfaces when the
                receive path is known to be inoperable.   If
                loopbackSupport(1) is set, then the peer OAM entity can send
                and receive OAM loopback commands.  If eventSupport(2) is set,
                then the peer OAM entity can send and receive event OAMPDUs to
                signal various error conditions. If variableSupport(3) is set,
                then the peer OAM entity can send and receive variable
                requests to monitor attribute value as described in Clause 57
                of [802.3ah].   
                
                The capabilities of the OAM peer can be determined from the
                configuration field of the Local Information TLV of the most
                recently received Information OAMPDU with a Local Information
                TLV.  All zeros are returned if no Local Information TLV has
                yet been received. 
                Keys are:- loopbackSupport , eventSupport , variableSupport , unidirectionalSupport

                """

                def __init__(self):
                    self._dictionary = { 
                        'loopbackSupport':False,
                        'eventSupport':False,
                        'variableSupport':False,
                        'unidirectionalSupport':False,
                    }
                    self._pos_map = { 
                        'loopbackSupport':1,
                        'eventSupport':2,
                        'variableSupport':3,
                        'unidirectionalSupport':0,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamPeerTable/CISCO-DOT3-OAM-MIB:cdot3OamPeerEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oampeerconfigrevision is not None:
                    return True

                if self.cdot3oampeerfunctionssupported is not None:
                    if self.cdot3oampeerfunctionssupported._has_data():
                        return True

                if self.cdot3oampeermacaddress is not None:
                    return True

                if self.cdot3oampeermaxoampdusize is not None:
                    return True

                if self.cdot3oampeermode is not None:
                    return True

                if self.cdot3oampeervendorinfo is not None:
                    return True

                if self.cdot3oampeervendoroui is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oampeerentry is not None:
                for child_ref in self.cdot3oampeerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oampeertable']['meta_info']


    class Cdot3Oamloopbacktable(object):
        """
        This table contains controls for the loopback state of the
        local link as well as indicating the status of the loopback
        function.  There is one entry in this table for each entry in
        cdot3OamTable that supports loopback functionality (where
        cdot3OamFunctionsSupported includes the loopbackSupport bit
        set).
        
        Loopback can be used to place the remote OAM entity in a state
        where every received frame (except OAMPDUs) is echoed back
        over the same interface on which they were received.   In this
        state, at the remote entity, 'normal' traffic is disabled as
        only the looped back frames are transmitted on the interface.
        Loopback is thus an intrusive operation that prohibits normal
        data flow and should be used accordingly.  
        
        .. attribute:: cdot3oamloopbackentry
        
        	An entry in the table, containing information on the loopback status for a single Ethernet like interface.  Entries in the table are automatically created whenever the local OAM entity supports loopback capabilities.  The loopback status on the interface can be determined from the cdot3OamLoopbackStatus object.  
        	**type**\: list of    :py:class:`Cdot3Oamloopbackentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oamloopbackentry = YList()
            self.cdot3oamloopbackentry.parent = self
            self.cdot3oamloopbackentry.name = 'cdot3oamloopbackentry'


        class Cdot3Oamloopbackentry(object):
            """
            An entry in the table, containing information on the loopback
            status for a single Ethernet like interface.  Entries in the
            table are automatically created whenever the local OAM entity
            supports loopback capabilities.  The loopback status on the
            interface can be determined from the cdot3OamLoopbackStatus
            object.  
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oamloopbackignorerx
            
            	Since OAM loopback is a disruptive operation (user traffic does not pass), this attribute provides a mechanism to provide controls over whether received OAM loopback commands are processed or ignored.  When the value is ignore(1), received loopback commands are ignored.  When the value is process(2), OAM loopback commands are processed.  The default value is to ignore loopback commands (ignore(1)).  
            	**type**\:   :py:class:`Cdot3OamloopbackignorerxEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackignorerxEnum>`
            
            .. attribute:: cdot3oamloopbackstatus
            
            	The loopback status of the OAM entity.  This status is determined by a combination of the local parser and multiplexer states, the remote parser and multiplexer states, as well as by the actions of the local OAM client.  When operating in normal mode with no loopback in progress, the status reads noLoopback(1).    The values initiatingLooopback(2) and terminatingLoopback(4) can be read or written.  The other values can only be read \- they can never be written.  Writing initiatingLoopback causes the local OAM entity to start the loopback process with its peer.  This value can only be written when the status is noLoopback(1).  Writing the value initiatingLoopback(2) in any other state has no effect.  When in remoteLoopback(3), writing terminatingLoopback(4) causes the local OAM entity to initiate the termination of the loopback state.  Writing terminatingLoopack(4) in any other state has no effect.                     If the OAM client initiates a looopback and has sent an Loopback OAMPDU and is waiting for a response, where the local parser and multiplexer states are DISCARD (see [802.3ah, 57.2.11.1]), the status is 'initiatingLoopback'.  In this case, the local OAM entity has yet to receive any acknowledgement that the remote OAM entity has received its loopback command request.                    If the local OAM client knows that the remote OAM entity is in loopback mode (via the remote state information as described in [802.3ah, 57.2.11.1, 30.3.6.1.15]), the status is remoteLoopback(3).  If the local OAM client is in the process of terminating the remote loopback [802.3ah, 57.2.11.3, 30.3.6.1.14], with its local multiplexer and parser states in DISCARD, the status is terminatingLoopback(4).  If the remote OAM client has put the local OAM entity in loopback mode as indicated by its local parser state, the status is localLoopback(5).    The unknown(6) status indicates the parser and multiplexer combination is unexpected.  This status may be returned if the OAM loopback is in a transition state but should not persist.   The values of this attribute correspond to the following values of the local and remote parser and multiplexer states.     value            LclPrsr   LclMux    RmtPrsr   RmtMux   noLoopback         FWD       FWD       FWD       FWD     initLoopback     DISCARD   DISCARD     FWD       FWD    rmtLoopback      DISCARD     FWD      LPBK    DISCARD   tmtngLoopback    DISCARD   DISCARD    LPBK    DISCARD   lclLoopback        LPBK    DISCARD   DISCARD     FWD   unknown            \*\*\*   any other combination   \*\*\*
            	**type**\:   :py:class:`Cdot3OamloopbackstatusEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackstatusEnum>`
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oamloopbackignorerx = None
                self.cdot3oamloopbackstatus = None

            class Cdot3OamloopbackignorerxEnum(Enum):
                """
                Cdot3OamloopbackignorerxEnum

                Since OAM loopback is a disruptive operation (user traffic

                does not pass), this attribute provides a mechanism to provide

                controls over whether received OAM loopback commands are

                processed or ignored.  When the value is ignore(1), received

                loopback commands are ignored.  When the value is process(2),

                OAM loopback commands are processed.  The default value is to

                ignore loopback commands (ignore(1)).  

                .. data:: ignore = 1

                .. data:: process = 2

                """

                ignore = 1

                process = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackignorerxEnum']


            class Cdot3OamloopbackstatusEnum(Enum):
                """
                Cdot3OamloopbackstatusEnum

                The loopback status of the OAM entity.  This status is

                determined by a combination of the local parser and

                multiplexer states, the remote parser and multiplexer states,

                as well as by the actions of the local OAM client.  When

                operating in normal mode with no loopback in progress, the

                status reads noLoopback(1).  

                The values initiatingLooopback(2) and terminatingLoopback(4)

                can be read or written.  The other values can only be read \-

                they can never be written.  Writing initiatingLoopback causes

                the local OAM entity to start the loopback process with its

                peer.  This value can only be written when the status is

                noLoopback(1).  Writing the value initiatingLoopback(2) in any

                other state has no effect.  When in remoteLoopback(3), writing

                terminatingLoopback(4) causes the local OAM entity to initiate

                the termination of the loopback state.  Writing

                terminatingLoopack(4) in any other state has no effect.                    

                If the OAM client initiates a looopback and has sent an

                Loopback OAMPDU and is waiting for a response, where the local

                parser and multiplexer states are DISCARD (see [802.3ah,

                57.2.11.1]), the status is 'initiatingLoopback'.  In this

                case, the local OAM entity has yet to receive any

                acknowledgement that the remote OAM entity has received its

                loopback command request.  

                If the local OAM client knows that the remote OAM entity is in

                loopback mode (via the remote state information as described

                in [802.3ah, 57.2.11.1, 30.3.6.1.15]), the status is

                remoteLoopback(3).  If the local OAM client is in the process

                of terminating the remote loopback [802.3ah, 57.2.11.3,

                30.3.6.1.14], with its local multiplexer and parser states in

                DISCARD, the status is terminatingLoopback(4).  If the remote

                OAM client has put the local OAM entity in loopback mode as

                indicated by its local parser state, the status is

                localLoopback(5).  

                The unknown(6) status indicates the parser and multiplexer

                combination is unexpected.  This status may be returned if the

                OAM loopback is in a transition state but should not persist. 

                The values of this attribute correspond to the following

                values of the local and remote parser and multiplexer states. 

                  value            LclPrsr   LclMux    RmtPrsr   RmtMux

                  noLoopback         FWD       FWD       FWD       FWD  

                  initLoopback     DISCARD   DISCARD     FWD       FWD 

                  rmtLoopback      DISCARD     FWD      LPBK    DISCARD

                  tmtngLoopback    DISCARD   DISCARD    LPBK    DISCARD

                  lclLoopback        LPBK    DISCARD   DISCARD     FWD

                  unknown            \*\*\*   any other combination   \*\*\*

                .. data:: noLoopback = 1

                .. data:: initiatingLoopback = 2

                .. data:: remoteLoopback = 3

                .. data:: terminatingLoopback = 4

                .. data:: localLoopback = 5

                .. data:: unknown = 6

                """

                noLoopback = 1

                initiatingLoopback = 2

                remoteLoopback = 3

                terminatingLoopback = 4

                localLoopback = 5

                unknown = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackstatusEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamLoopbackTable/CISCO-DOT3-OAM-MIB:cdot3OamLoopbackEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oamloopbackignorerx is not None:
                    return True

                if self.cdot3oamloopbackstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamLoopbackTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oamloopbackentry is not None:
                for child_ref in self.cdot3oamloopbackentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable']['meta_info']


    class Cdot3Oamstatstable(object):
        """
        This table contains statistics for the OAM function on a
        particular Ethernet like interface. There is an entry in the
        table for every entry in the cdot3OamTable. 
        
        The counters in this table are defined as 32\-bit entries to
        match the counter size as defined in [802.3ah].  Given the OAM
        protocol is a slow protocol, the counters increment at a slow
        rate. 
        
        .. attribute:: cdot3oamstatsentry
        
        	An entry in the table, containing statistics information on the Ethernet OAM function for a single Ethernet like interface.  Entries are automatically created for every entry in the cdot3OamTable.  Counters are maintained across transitions in cdot3OamOperStatus.  
        	**type**\: list of    :py:class:`Cdot3Oamstatsentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oamstatsentry = YList()
            self.cdot3oamstatsentry.parent = self
            self.cdot3oamstatsentry.name = 'cdot3oamstatsentry'


        class Cdot3Oamstatsentry(object):
            """
            An entry in the table, containing statistics information on
            the Ethernet OAM function for a single Ethernet like
            interface.  Entries are automatically created for every entry
            in the cdot3OamTable.  Counters are maintained across
            transitions in cdot3OamOperStatus.  
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oamduplicateeventnotificationrx
            
            	A count of the number of duplicate Event OAMPDUs received on this interface.  Event notification OAMPDUs may be sent in duplicate to increase the probability of successfully being received, given the possibility that a frame may be lost in transit.    A duplicate Event Notification OAMPDU is indicated as an Event Notification OAMPDU with a Sequence Number field that is identical to the previously received Event Notification OAMPDU Sequence Number.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamduplicateeventnotificationtx
            
            	A count of the number of duplicate Event OAMPDUs transmitted on this interface.  Event notification OAMPDUs may be sent in duplicate to increase the probability of successfully being received, given the possibility that a frame may be lost in transit.    A duplicate Event Notification OAMPDU is indicated as an Event Notification OAMPDU with a Sequence Number field that is identical to the previously transmitted Event Notification OAMPDU Sequence Number.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamframeslostduetooam
            
            	A count of the number of frames that were dropped by the OAM multiplexer.  Since the OAM multiplexer has multiple inputs and a single output, there may be cases where frames are dropped due to transmit resource contention.  This counter is incremented whenever a frame is dropped by the OAM layer. Note that any Ethernet frame, not just OAMPDUs, may be dropped by the OAM layer.  This can occur when an OAMPDU takes precedence over a 'normal' frame resulting in the 'normal' frame being dropped.    When this counter is incremented, no other counters in this MIB are incremented.                  Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oaminformationrx
            
            	A count of the number of Information OAMPDUs received on this interface.  Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oaminformationtx
            
            	A count of the number of Information OAMPDUs transmitted on this interface.  Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamloopbackcontrolrx
            
            	A count of the number of Loopback Control OAMPDUs received on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamloopbackcontroltx
            
            	A count of the number of Loopback Control OAMPDUs transmitted on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamorgspecificrx
            
            	A count of the number of Organization Specific OAMPDUs received on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamorgspecifictx
            
            	A count of the number of Organization Specific OAMPDUs transmitted on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamuniqueeventnotificationrx
            
            	A count of the number of unique Event OAMPDUs received on this interface.  Event notification OAMPDUs may be sent in duplicate to increase the probability of successfully being received, given the possibility that a frame may be lost in transit.  Duplicate Event Notification receptions are counted by cdot3OamDuplicateEventNotificationRx.    A unique Event Notification OAMPDU is indicated as an Event Notification OAMPDU with a Sequence Number field that is distinct from the previously received Event Notification OAMPDU Sequence Number.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamuniqueeventnotificationtx
            
            	A count of the number of unique Event OAMPDUs transmitted on this interface.  Event notifications may be sent in duplicate to increase the probability of successfully being received, given the possibility that a frame may be lost in transit. Duplicate Event Notification transmissions are counted by cdot3OamDuplicateEventNotificationTx.    A unique Event Notification OAMPDU is indicated as an Event Notification OAMPDU with a Sequence Number field that is distinct from the previously transmitted Event Notification OAMPDU Sequence Number.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamunsupportedcodesrx
            
            	A count of the number of OAMPDUs received on this interface with an unsupported op\-code.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamunsupportedcodestx
            
            	A count of the number of OAMPDUs transmitted on this interface with an unsupported op\-code.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamvariablerequestrx
            
            	A count of the number of Variable Request OAMPDUs received on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamvariablerequesttx
            
            	A count of the number of Variable Request OAMPDUs transmitted on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamvariableresponserx
            
            	A count of the number of Variable Response OAMPDUs received on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamvariableresponsetx
            
            	A count of the number of Variable Response OAMPDUs transmitted on this interface.    Discontinuities of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oamduplicateeventnotificationrx = None
                self.cdot3oamduplicateeventnotificationtx = None
                self.cdot3oamframeslostduetooam = None
                self.cdot3oaminformationrx = None
                self.cdot3oaminformationtx = None
                self.cdot3oamloopbackcontrolrx = None
                self.cdot3oamloopbackcontroltx = None
                self.cdot3oamorgspecificrx = None
                self.cdot3oamorgspecifictx = None
                self.cdot3oamuniqueeventnotificationrx = None
                self.cdot3oamuniqueeventnotificationtx = None
                self.cdot3oamunsupportedcodesrx = None
                self.cdot3oamunsupportedcodestx = None
                self.cdot3oamvariablerequestrx = None
                self.cdot3oamvariablerequesttx = None
                self.cdot3oamvariableresponserx = None
                self.cdot3oamvariableresponsetx = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamStatsTable/CISCO-DOT3-OAM-MIB:cdot3OamStatsEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oamduplicateeventnotificationrx is not None:
                    return True

                if self.cdot3oamduplicateeventnotificationtx is not None:
                    return True

                if self.cdot3oamframeslostduetooam is not None:
                    return True

                if self.cdot3oaminformationrx is not None:
                    return True

                if self.cdot3oaminformationtx is not None:
                    return True

                if self.cdot3oamloopbackcontrolrx is not None:
                    return True

                if self.cdot3oamloopbackcontroltx is not None:
                    return True

                if self.cdot3oamorgspecificrx is not None:
                    return True

                if self.cdot3oamorgspecifictx is not None:
                    return True

                if self.cdot3oamuniqueeventnotificationrx is not None:
                    return True

                if self.cdot3oamuniqueeventnotificationtx is not None:
                    return True

                if self.cdot3oamunsupportedcodesrx is not None:
                    return True

                if self.cdot3oamunsupportedcodestx is not None:
                    return True

                if self.cdot3oamvariablerequestrx is not None:
                    return True

                if self.cdot3oamvariablerequesttx is not None:
                    return True

                if self.cdot3oamvariableresponserx is not None:
                    return True

                if self.cdot3oamvariableresponsetx is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oamstatsentry is not None:
                for child_ref in self.cdot3oamstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oamstatstable']['meta_info']


    class Cdot3Oameventconfigtable(object):
        """
        Ethernet OAM includes the ability to generate and receive
        Event Notification OAMPDUs to indicate various link problems.
        This table contains the mechanisms to enable Event
        Notifications and configure the thresholds to generate the
        standard Ethernet OAM events.  There is one entry in the table
        for every entry in cdot3OamTable that supports OAM events
        (where cdot3OamFunctionsSupported includes the eventSupport
        bit set). The values in the table are maintained across
        changes to cdot3OamOperStatus.  
        
        The standard threshold crossing events are\:
          \- Errored Symbol Period Event.  Generated when the number of
            symbol errors exceeds a threshold within a given window 
            defined by a number of symbols (for example, 1,000 symbols
            out of 1,000,000 had errors).  
          \- Errored Frame Period Event.  Generated when the number of 
            frame errors exceeds a threshold within a given window 
            defined by a number of frames (for example, 10 frames out
            of 1000 had errors).  
          \- Errored Frame Event.  Generated when the number of frame 
            errors exceeds a threshold within a given window defined 
            by a period of time (for example, 10 frames in 1 second 
            had errors).
          \- Errored Frame Seconds Summary Event.  Generated when the 
            number of errored frame seconds exceeds a threshold within
            a given time period (for example, 10 errored frame seconds
            within the last 100 seconds).  An errored frame second is 
            defined as a 1 second interval which had >0 frame errors.  
        There are other events (dying gasp, critical events) that are
        not threshold crossing events but which can be
        enabled/disabled via this table.  
        
        .. attribute:: cdot3oameventconfigentry
        
        	Entries are automatically created and deleted from this table, and exist whenever the OAM entity supports Ethernet OAM events (as indicated by the eventSupport bit in cdot3OamFunctionsSuppported).  Values in the table are maintained across changes to the value of cdot3OamOperStatus.  Event configuration controls when the local management entity sends Event Notification OAMPDUs to its OAM peer, and when certain event flags are set or cleared in OAMPDUs. 
        	**type**\: list of    :py:class:`Cdot3Oameventconfigentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oameventconfigentry = YList()
            self.cdot3oameventconfigentry.parent = self
            self.cdot3oameventconfigentry.name = 'cdot3oameventconfigentry'


        class Cdot3Oameventconfigentry(object):
            """
            Entries are automatically created and deleted from this
            table, and exist whenever the OAM entity supports Ethernet OAM
            events (as indicated by the eventSupport bit in
            cdot3OamFunctionsSuppported).  Values in the table are
            maintained across changes to the value of cdot3OamOperStatus.
            
            Event configuration controls when the local management entity
            sends Event Notification OAMPDUs to its OAM peer, and when
            certain event flags are set or cleared in OAMPDUs. 
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oamcriticaleventenable
            
            	If true, the local OAM entity should attempt to indicate a critical event via the OAMPDU flags to its peer OAM entity when a critical event occurs.   The exact definition of a critical event is implementation dependent.  If the system does not support critical event capability, setting this object has no effect, and reading the object should always result in 'false'.                    By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored
            	**type**\:  bool
            
            .. attribute:: cdot3oamdyinggaspenable
            
            	If true, the local OAM entity should attempt to indicate a dying gasp via the OAMPDU flags field to its peer OAM entity when a dying gasp event occurs.  The exact definition of a dying gasp event is implementation dependent.  If the system does not support dying gasp capability, setting this object has no effect, and reading the object should always result in 'false'.                    By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored
            	**type**\:  bool
            
            .. attribute:: cdot3oamerrframeevnotifenable
            
            	If true, the OAM entity should send an Event Notification OAMPDU when an Errored Frame Event occurs.                   By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored. 
            	**type**\:  bool
            
            .. attribute:: cdot3oamerrframeperiodevnotifenable
            
            	If true, the OAM entity should send an Event Notification OAMPDU when an Errored Frame Period Event occurs.   By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored. 
            	**type**\:  bool
            
            .. attribute:: cdot3oamerrframeperiodthreshold
            
            	The number of frame errors that must occur for this event to be triggered.  The default value is one frame error.  If the threshold value is zero, then an Event Notification OAMPDU is sent periodically (at the end of every window).  This can be used as an asynchronous notification to the peer OAM entity of the statistics related to this threshold crossing alarm.                  If cdot3OamErrFramePeriodThreshold frame errors occur within a window of cdot3OamErrFramePeriodWindow frames, an Event Notification OAMPDU should be generated with an Errored Frame Period Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamerrframeperiodwindow
            
            	The number of frames over which the threshold is defined. The default value of the window is the number of minimum size Ethernet frames that can be received over the physical layer in one second.                    If cdot3OamErrFramePeriodThreshold frame errors occur within a window of cdot3OamErrFramePeriodWindow frames, an Event Notification OAMPDU should be generated with an Errored Frame Period Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamerrframesecsevnotifenable
            
            	If true, the local OAM entity should send an Event Notification OAMPDU when an Errored Frame Seconds Event occurs.                   By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored
            	**type**\:  bool
            
            .. attribute:: cdot3oamerrframesecssummarythreshold
            
            	The number of errored frame seconds that must occur for this event to be triggered.  The default value is one errored frame second. If the threshold value is zero, then an Event Notification OAMPDU is sent periodically (at the end of every window).  This can be used as an asynchronous notification to the peer OAM entity of the statistics related to this threshold crossing alarm.                   If cdot3OamErrFrameSecsSummaryThreshold frame errors occur within a window of cdot3OamErrFrameSecsSummaryWindow (in tenths of seconds), an Event Notification OAMPDU should be generated with an Errored Frame Seconds Summary Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 1..900
            
            	**units**\: errored frame seconds
            
            .. attribute:: cdot3oamerrframesecssummarywindow
            
            	The amount of time (in 100ms intervals) over which the threshold is defined.  The default value is 100 (10 seconds).                    If cdot3OamErrFrameSecsSummaryThreshold frame errors occur within a window of cdot3OamErrFrameSecsSummaryWindow (in tenths of seconds), an Event Notification OAMPDU should be generated with an Errored Frame Seconds Summary Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 100..9000
            
            	**units**\: tenths of a second
            
            .. attribute:: cdot3oamerrframethreshold
            
            	The number of frame errors that must occur for this event to be triggered.  The default value is one frame error. If the threshold value is zero, then an Event Notification OAMPDU is sent periodically (at the end of every window).  This can be used as an asynchronous notification to the peer OAM entity of the statistics related to this threshold crossing alarm.                   If cdot3OamErrFrameThreshold frame errors occur within a window of cdot3OamErrFrameWindow (in tenths of seconds), an Event Notification OAMPDU should be generated with an Errored Frame Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: cdot3oamerrframewindow
            
            	The amount of time (in 100ms increments) over which the threshold is defined.  The default value is 10 (1 second).                    If cdot3OamErrFrameThreshold frame errors occur within a window of cdot3OamErrFrameWindow seconds (measured in tenths of seconds), an Event Notification OAMPDU should be generated with an Errored Frame Event TLV indicating the threshold has been crossed in this window.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: tenths of a second
            
            .. attribute:: cdot3oamerrsymperiodevnotifenable
            
            	If true, the OAM entity should send an Event Notification OAMPDU when an Errored Symbol Period Event occurs.  By default, this object should have the value true for Ethernet like interfaces that support OAM.  If the OAM layer does not support event notifications (as indicated via the cdot3OamFunctionsSupported attribute), this value is ignored
            	**type**\:  bool
            
            .. attribute:: cdot3oamerrsymperiodthresholdhi
            
            	The two objects cdot3OamErrSymPeriodThresholdHi and cdot3OamErrSymPeriodThresholdLo together form an unsigned 64\-bit integer representing the number of symbol errors that must occur within a given window to cause this event.    This is defined as    cdot3OamErrSymPeriodThreshold =                     ((2^32) \* cdot3OamErrSymPeriodThresholdHi)                             + cdot3OamErrSymPeriodThresholdLo                     If cdot3OamErrSymPeriodThreshold symbol errors occur within a window of cdot3OamErrSymPeriodWindow symbols, an Event Notification OAMPDU should be generated with an Errored Symbol Period Event TLV indicating the threshold has been crossed in this window.    The default value for cdot3OamErrSymPeriodThreshold is one symbol errors.  If the threshold value is zero, then an Event Notification OAMPDU is sent periodically (at the end of every window).  This can be used as an asynchronous notification to the peer OAM entity of the statistics related to this threshold crossing alarm.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: 2^32 symbols
            
            .. attribute:: cdot3oamerrsymperiodthresholdlo
            
            	The two objects cdot3OamErrSymPeriodThresholdHi and cdot3OamErrSymPeriodThresholdLo together form an unsigned 64\-bit integer representing the number of symbol errors that must occur within a given window to cause this event.    This is defined as    cdot3OamErrSymPeriodThreshold =                     ((2^32) \* cdot3OamErrSymPeriodThresholdHi)                             + cdot3OamErrSymPeriodThresholdLo                     If cdot3OamErrSymPeriodThreshold symbol errors occur within a window of cdot3OamErrSymPeriodWindow symbols, an Event Notification OAMPDU should be generated with an Errored Symbol Period Event TLV indicating the threshold has been crossed in this window.    The default value for cdot3OamErrSymPeriodThreshold is one symbol error. If the threshold value is zero, then an Event Notification OAMPDU is sent periodically (at the end of every window).  This can be used as an asynchronous notification to the peer OAM entity of the statistics related to this threshold crossing alarm. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: symbols
            
            .. attribute:: cdot3oamerrsymperiodwindowhi
            
            	The two objects cdot3OamErrSymPeriodWindowHi and cdot3OamErrSymPeriodLo together form an unsigned 64\-bit integer representing the number of symbols over which this threshold event is defined.  This is defined as  cdot3OamErrSymPeriodWindow = ((2^32)\*cdot3OamErrSymPeriodWindowHi)                                 + cdot3OamErrSymPeriodWindowLo  If cdot3OamErrSymPeriodThreshold symbol errors occur within a window of cdot3OamErrSymPeriodWindow symbols, an Event Notification OAMPDU should be generated with an Errored Symbol Period Event TLV indicating the threshold has been crossed in this window.    The default value for cdot3OamErrSymPeriodWindow is the number of symbols in one second for the underlying physical layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: 2^32 symbols
            
            .. attribute:: cdot3oamerrsymperiodwindowlo
            
            	The two objects cdot3OamErrSymPeriodWindowHi and cdot3OamErrSymPeriodWindowLo together form an unsigned 64\-bit integer representing the number of symbols over which this threshold event is defined.  This is defined as  cdot3OamErrSymPeriodWindow = ((2^32)\*cdot3OamErrSymPeriodWindowHi)                                 + cdot3OamErrSymPeriodWindowLo  If cdot3OamErrSymPeriodThreshold symbol errors occur within a window of cdot3OamErrSymPeriodWindow symbols, an Event Notification OAMPDU should be generated with an Errored Symbol Period Event TLV indicating the threshold has been crossed in this window.    The default value for cdot3OamErrSymPeriodWindow is the number of symbols in one second for the underlying physical layer. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: symbols
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oamcriticaleventenable = None
                self.cdot3oamdyinggaspenable = None
                self.cdot3oamerrframeevnotifenable = None
                self.cdot3oamerrframeperiodevnotifenable = None
                self.cdot3oamerrframeperiodthreshold = None
                self.cdot3oamerrframeperiodwindow = None
                self.cdot3oamerrframesecsevnotifenable = None
                self.cdot3oamerrframesecssummarythreshold = None
                self.cdot3oamerrframesecssummarywindow = None
                self.cdot3oamerrframethreshold = None
                self.cdot3oamerrframewindow = None
                self.cdot3oamerrsymperiodevnotifenable = None
                self.cdot3oamerrsymperiodthresholdhi = None
                self.cdot3oamerrsymperiodthresholdlo = None
                self.cdot3oamerrsymperiodwindowhi = None
                self.cdot3oamerrsymperiodwindowlo = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamEventConfigTable/CISCO-DOT3-OAM-MIB:cdot3OamEventConfigEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oamcriticaleventenable is not None:
                    return True

                if self.cdot3oamdyinggaspenable is not None:
                    return True

                if self.cdot3oamerrframeevnotifenable is not None:
                    return True

                if self.cdot3oamerrframeperiodevnotifenable is not None:
                    return True

                if self.cdot3oamerrframeperiodthreshold is not None:
                    return True

                if self.cdot3oamerrframeperiodwindow is not None:
                    return True

                if self.cdot3oamerrframesecsevnotifenable is not None:
                    return True

                if self.cdot3oamerrframesecssummarythreshold is not None:
                    return True

                if self.cdot3oamerrframesecssummarywindow is not None:
                    return True

                if self.cdot3oamerrframethreshold is not None:
                    return True

                if self.cdot3oamerrframewindow is not None:
                    return True

                if self.cdot3oamerrsymperiodevnotifenable is not None:
                    return True

                if self.cdot3oamerrsymperiodthresholdhi is not None:
                    return True

                if self.cdot3oamerrsymperiodthresholdlo is not None:
                    return True

                if self.cdot3oamerrsymperiodwindowhi is not None:
                    return True

                if self.cdot3oamerrsymperiodwindowlo is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamEventConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oameventconfigentry is not None:
                for child_ref in self.cdot3oameventconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oameventconfigtable']['meta_info']


    class Cdot3Oameventlogtable(object):
        """
        This table records a history of the events that have occurred
        at the Ethernet OAM level.  These events can include locally
        detected events, which may result in locally generated
        OAMPDUs, and remotely detected events, which are detected by
        the OAM peer entity and signaled to the local entity via
        Ethernet OAM.  Ethernet OAM events can be signaled by Event
        Notification OAMPDUs or by the flags field in any OAMPDU.  
        
        This table contains both threshold crossing events and
        non\-threshold crossing events.  The parameters for the
        threshold window, threshold value, and actual value
        (cdot3OamEventLogWindowXX, cdot3OamEventLogThresholdXX,
        cdot3OamEventLogValue) are only applicable to threshold
        crossing events, and are returned as all F's (2^32 \- 1) for
        non\-threshold crossing events.  
        Entries in the table are automatically created when such
        events are detected.  The size of the table is implementation
        dependent.  When the table reaches its maximum size, older
        entries are automatically deleted to make room for newer
        entries. 
        
        .. attribute:: cdot3oameventlogentry
        
        	An entry in the cdot3OamEventLogTable.  Entries are automatically created whenever Ethernet OAM events occur at the local OAM entity, and when Event Notification OAMPDUs are received at the local OAM entity (indicating events have occurred at the peer OAM entity).  The size of the table is implementation dependent, but when the table becomes full, older events are automatically deleted to make room for newer events.  The table index cdot3OamEventLogIndex increments for each new entry, and when the maximum value is reached the value restarts at zero.  
        	**type**\: list of    :py:class:`Cdot3Oameventlogentry <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry>`
        
        

        """

        _prefix = 'CISCO-DOT3-OAM-MIB'
        _revision = '2006-05-31'

        def __init__(self):
            self.parent = None
            self.cdot3oameventlogentry = YList()
            self.cdot3oameventlogentry.parent = self
            self.cdot3oameventlogentry.name = 'cdot3oameventlogentry'


        class Cdot3Oameventlogentry(object):
            """
            An entry in the cdot3OamEventLogTable.  Entries are
            automatically created whenever Ethernet OAM events occur at
            the local OAM entity, and when Event Notification OAMPDUs are
            received at the local OAM entity (indicating events have
            occurred at the peer OAM entity).  The size of the table is
            implementation dependent, but when the table becomes full,
            older events are automatically deleted to make room for newer
            events.  The table index cdot3OamEventLogIndex increments for
            each new entry, and when the maximum value is reached the
            value restarts at zero.  
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdot3oameventlogindex  <key>
            
            	An arbitrary integer for identifying individual events within the event log.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogeventtotal
            
            	Each Event Notification TLV contains a running total of the number of times an event has occurred, as well as the number of times an Event Notification for the event has been transmitted.  For non\-threshold crossing events, the number of events (cdot3OamLogRunningTotal) and the number of resultant Event Notifications (cdot3OamLogEventTotal) should be identical.   For threshold crossing events, since multiple occurrences may be required to cross the threshold, these values are likely different.  This value represents the total number of times one or more of these occurrences have resulted in an Event Notification (for example, 51 when 3253 symbol errors have occurred since the last reset, which has resulted in 51 symbol error threshold crossing events since the last reset).  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventloglocation
            
            	Whether this event occurred locally (local(1)), or was  received from the OAM peer via Ethernet OAM (remote(2))
            	**type**\:   :py:class:`Cdot3OameventloglocationEnum <ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB.CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry.Cdot3OameventloglocationEnum>`
            
            .. attribute:: cdot3oameventlogoui
            
            	The OUI of the entity defining the object type.  All IEEE 802.3 defined events (as appearing in [802.3ah] except for the Organizationally Unique Event TLVs) use the IEEE 802.3 OUI of 0x0180C2.  Organizations defining their own Event Notification TLVs include their OUI in the Event Notification TLV which gets reflected here.  
            	**type**\:  str
            
            	**length:** 3
            
            .. attribute:: cdot3oameventlogrunningtotal
            
            	Each Event Notification TLV contains a running total of the number of times an event has occurred, as well as the number of times an Event Notification for the event has been transmitted.  For non\-threshold crossing events, the number of events (cdot3OamLogRunningTotal) and the number of resultant Event Notifications (cdot3OamLogEventTotal) should be identical.   For threshold crossing events, since multiple occurrences may be required to cross the threshold, these values are likely different.  This value represents the total number of times this event has happened since the last reset (for example, 3253, when 3253 symbol errors have occurred since the last reset, which has resulted in 51 symbol error threshold crossing events since the last reset).  
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cdot3oameventlogthresholdhi
            
            	If the event represents a threshold crossing event, the two objects cdot3OamEventThresholdHi and cdot3OamEventThresholdLo form an unsigned 64\-bit integer yielding the value that was crossed for the threshold crossing event (for example, 10, when 11 occurrences happened in 5 seconds while the threshold was 10).  The two objects are combined as\:  cdot3OamEventLogThreshold = ((2^32) \* cdot3OamEventLogThresholdHi)                                  + cdot3OamEventLogThresholdLo  Otherwise, this value is returned as all F's (2^32 \-1) and  adds no useful information.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogthresholdlo
            
            	If the event represents a threshold crossing event, the two objects cdot3OamEventThresholdHi and cdot3OamEventThresholdLo form an unsigned 64\-bit integer yielding the value that was crossed for the threshold crossing event (for example, 10, when 11 occurrences happened in 5 seconds while the threshold was 10).  The two objects are combined as\:  cdot3OamEventLogThreshold = ((2^32) \* cdot3OamEventLogThresholdHi)                                  + cdot3OamEventLogThresholdLo  Otherwise, this value is returned as all F's (2^32 \- 1) and adds no useful information.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogtimestamp
            
            	The value of sysUpTime at the time of the logged event.  For locally generated events, the time of the event can be accurately retrieved from sysUpTime.  For remotely generated events, the time of the event is indicated by the reception of the Event Notification OAMPDU indicating the event occurred on the peer.  A system may attempt to adjust the timestamp value to more accurately reflect the time of the event at the peer OAM entity by using other information, such as that found in the timestamp found of the Event Notification TLVs, which provides an indication of the relative time between events at the peer entity.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogtype
            
            	The type of event that generated this entry in the event log.  When the OUI is the IEEE 802.3 OUI of 0x0180C2, the following event types are defined\:     erroredSymbolEvent(1),      erroredFramePeriodEvent (2),      erroredFrameEvent(3),     erroredFrameSecondsEvent(4),      linkFault(256),      dyingGaspEvent(257),     criticalLinkEvent(258) The first four are considered threshold crossing events as they are generated when a metric exceeds a given value within a specified window.  The other three are not threshold crossing events.    When the OUI is not 71874 (0x0180C2 in hex), then some other organization has defined the event space.  If event subtyping is known to the implementation, it may be reflected here. Otherwise, this value should return all Fs (2^32 \- 1).  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogvalue
            
            	If the event represents a threshold crossing event, this value indicates the value of the parameter within the given window that generated this event (for example, 11, when 11 occurrences happened in 5 seconds while the threshold was 10).    Otherwise, this value is returned as all F's  (2^64 \- 1) and adds no useful information.  
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cdot3oameventlogwindowhi
            
            	If the event represents a threshold crossing event, the two objects cdot3OamEventWindowHi and cdot3OamEventWindowLo form an unsigned 64\-bit integer yielding the window over which the value was measured for the threshold crossing event (for example, 5, when 11 occurrences happened in 5 seconds while the threshold was 10).   The two objects are combined as\:  cdot3OamEventLogWindow = ((2^32) \* cdot3OamEventLogWindowHi)                                 + cdot3OamEventLogWindowLo   Otherwise, this value is returned as all F's (2^32 \- 1) and  adds no useful information.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdot3oameventlogwindowlo
            
            	If the event represents a threshold crossing event, the two objects cdot3OamEventWindowHi and cdot3OamEventWindowLo form an unsigned 64\-bit integer yielding the window over which the value was measured for the threshold crossing event (for example, 5, when 11 occurrences happened in 5 seconds while the threshold was 10).   The two objects are combined as\:  cdot3OamEventLogWindow = ((2^32) \* cdot3OamEventLogWindowHi)                                 + cdot3OamEventLogWindowLo  Otherwise, this value is returned as all F's (2^32 \- 1) and  adds no useful information.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-DOT3-OAM-MIB'
            _revision = '2006-05-31'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdot3oameventlogindex = None
                self.cdot3oameventlogeventtotal = None
                self.cdot3oameventloglocation = None
                self.cdot3oameventlogoui = None
                self.cdot3oameventlogrunningtotal = None
                self.cdot3oameventlogthresholdhi = None
                self.cdot3oameventlogthresholdlo = None
                self.cdot3oameventlogtimestamp = None
                self.cdot3oameventlogtype = None
                self.cdot3oameventlogvalue = None
                self.cdot3oameventlogwindowhi = None
                self.cdot3oameventlogwindowlo = None

            class Cdot3OameventloglocationEnum(Enum):
                """
                Cdot3OameventloglocationEnum

                Whether this event occurred locally (local(1)), or was 

                received from the OAM peer via Ethernet OAM (remote(2)).

                .. data:: local = 1

                .. data:: remote = 2

                """

                local = 1

                remote = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                    return meta._meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry.Cdot3OameventloglocationEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.cdot3oameventlogindex is None:
                    raise YPYModelError('Key property cdot3oameventlogindex is None')

                return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamEventLogTable/CISCO-DOT3-OAM-MIB:cdot3OamEventLogEntry[CISCO-DOT3-OAM-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-DOT3-OAM-MIB:cdot3OamEventLogIndex = ' + str(self.cdot3oameventlogindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdot3oameventlogindex is not None:
                    return True

                if self.cdot3oameventlogeventtotal is not None:
                    return True

                if self.cdot3oameventloglocation is not None:
                    return True

                if self.cdot3oameventlogoui is not None:
                    return True

                if self.cdot3oameventlogrunningtotal is not None:
                    return True

                if self.cdot3oameventlogthresholdhi is not None:
                    return True

                if self.cdot3oameventlogthresholdlo is not None:
                    return True

                if self.cdot3oameventlogtimestamp is not None:
                    return True

                if self.cdot3oameventlogtype is not None:
                    return True

                if self.cdot3oameventlogvalue is not None:
                    return True

                if self.cdot3oameventlogwindowhi is not None:
                    return True

                if self.cdot3oameventlogwindowlo is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
                return meta._meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB/CISCO-DOT3-OAM-MIB:cdot3OamEventLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdot3oameventlogentry is not None:
                for child_ref in self.cdot3oameventlogentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
            return meta._meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-DOT3-OAM-MIB:CISCO-DOT3-OAM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cdot3oameventconfigtable is not None and self.cdot3oameventconfigtable._has_data():
            return True

        if self.cdot3oameventlogtable is not None and self.cdot3oameventlogtable._has_data():
            return True

        if self.cdot3oamloopbacktable is not None and self.cdot3oamloopbacktable._has_data():
            return True

        if self.cdot3oampeertable is not None and self.cdot3oampeertable._has_data():
            return True

        if self.cdot3oamstatstable is not None and self.cdot3oamstatstable._has_data():
            return True

        if self.cdot3oamtable is not None and self.cdot3oamtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_DOT3_OAM_MIB as meta
        return meta._meta_table['CiscoDot3OamMib']['meta_info']


