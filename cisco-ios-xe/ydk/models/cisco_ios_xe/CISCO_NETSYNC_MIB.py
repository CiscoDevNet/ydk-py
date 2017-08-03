""" CISCO_NETSYNC_MIB 

The Synchronous Ethernet (SyncE) MIB is defined
for monitoring network synchronization based on
ITU\-T G.781 clock selection.

Synchronous Ethernet (SyncE) is a standard defined
for delivering timing to the remote NEs through a 
Packet Network.   SyncE is well defined by ITU\-T
which included G.8261, G.8262, G.8264 and G.781.
It leverages the PHY layer of Ethernet to transmit
frequency to the remote sites.  Its functionality
and accuracy mimics that of the SONET/SDH network
because of its physical layer characteristic.
In order to allow best clock source traceabiliy,
correctly define the timing source and helps
preventing timing loop, Synchronization Status
Message is required for SyncE.  This is similar
to SONET/SDH.  However, since SONET/SDH use 4 bits
from the two S bytes in the SONET/SDH overhead
frame for such message, Ethernet relies on a
different channel called ESMC (Ethernet
Synchronization Messaging Channel) which is based
on IEEE 802.3 Organization Specific Slow Protocol.

Glossary\:
AIS\: Alarm Indication Signal
ATM\: Asynchronous Transfer Mode
EEC\: Ethernet Equipment Clock
ESMC\: Ethernet Synchronization Messaging Channel
QL\: Quality Level
SASE\: Stand Alone Synchronization Equipment
SSM\: Synchronization Status Messaging

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cisconetsyncclockmode(Enum):
    """
    Cisconetsyncclockmode

    Clock operating mode\:

    netsyncClockModeUnknown  \- system is unable to 

                               determine the operating mode.

    netsyncClockModeFreerun  \- free\-running mode.

    netsyncClockModeHoldover \- holdover mode.

    netsyncClockModeLocked   \- a valid clock source is locked.

    .. data:: netsyncClockModeUnknown = 1

    .. data:: netsyncClockModeFreerun = 2

    .. data:: netsyncClockModeHoldover = 3

    .. data:: netsyncClockModeLocked = 4

    """

    netsyncClockModeUnknown = Enum.YLeaf(1, "netsyncClockModeUnknown")

    netsyncClockModeFreerun = Enum.YLeaf(2, "netsyncClockModeFreerun")

    netsyncClockModeHoldover = Enum.YLeaf(3, "netsyncClockModeHoldover")

    netsyncClockModeLocked = Enum.YLeaf(4, "netsyncClockModeLocked")


class Cisconetsynceecoption(Enum):
    """
    Cisconetsynceecoption

    Network synchronization EEC (Ethernet Equipment Clock)

    options.

    The EEC options are for Synchronous Ethernet devices and define

    the requirements for clocks, e.g. bandwidth, frequency accuracy,

    holdover and noise generation.

    Two options are defined\:

    EEC\-Option 1\: Designed to interwork with network optimized for

    the 2048 kbit/s hierarchy.

    EEC\-Option 2\: Designed to interwork with network optimized for

    the 1544 kbit/s hierarchy.

    netsyncEECOptionUnknown   Unknown

    netsyncEECOption1         EEC option 1

    netsyncEECOption2         EEC option 2

    netsyncEECOptionInvalid   Invalid EEC option

    .. data:: netsyncEECOptionUnknown = 1

    .. data:: netsyncEECOption1 = 2

    .. data:: netsyncEECOption2 = 3

    .. data:: netsyncEECOptionInvalid = 4

    """

    netsyncEECOptionUnknown = Enum.YLeaf(1, "netsyncEECOptionUnknown")

    netsyncEECOption1 = Enum.YLeaf(2, "netsyncEECOption1")

    netsyncEECOption2 = Enum.YLeaf(3, "netsyncEECOption2")

    netsyncEECOptionInvalid = Enum.YLeaf(4, "netsyncEECOptionInvalid")


class Cisconetsyncesmccap(Enum):
    """
    Cisconetsyncesmccap

    Network synchronization clock source interface ESMC

    (Ethernet Synchronization Messaging Channel)

    capability.

    ESMC Capability         Capability information

    ======================  ======================

    netsyncESMCCapNone      No ESMC capability

    netsyncESMCCapTxRx      To transmit and receive ESMC

    netsyncESMCCapTx        To transmit SSM only

    netsyncESMCCapRx        To receive SSM only

    netsyncESMCCapInvalid   Capability invalid or unsupported

    .. data:: netsyncESMCCapNone = 1

    .. data:: netsyncESMCCapTxRx = 2

    .. data:: netsyncESMCCapTx = 3

    .. data:: netsyncESMCCapRx = 4

    .. data:: netsyncESMCCapInvalid = 5

    """

    netsyncESMCCapNone = Enum.YLeaf(1, "netsyncESMCCapNone")

    netsyncESMCCapTxRx = Enum.YLeaf(2, "netsyncESMCCapTxRx")

    netsyncESMCCapTx = Enum.YLeaf(3, "netsyncESMCCapTx")

    netsyncESMCCapRx = Enum.YLeaf(4, "netsyncESMCCapRx")

    netsyncESMCCapInvalid = Enum.YLeaf(5, "netsyncESMCCapInvalid")


class Cisconetsynciftype(Enum):
    """
    Cisconetsynciftype

    Network synchronization clock source Interface type.

    Netsync interface         Interface type

    ========================  ==============

    netsyncIfTypeUnknown      Unknown

    netsyncIfTypeInternal     Internal

    netsyncIfTypeEthernet     Ethernet

    netsyncIfTypeSonet        SONET

    netsyncIfTypeTop          Timing Over Packet

    netsyncIfTypeExt          External interface

    netsyncIfTypeController   T1/E1 Controller

    netsyncIfTypeGps          GPS

    netsyncIfTypeAtm          ATM

    For external and GPS interface types, the following

    syntax is used for specifying an interface\:

        <slot>/<card>/<port> <signal type> where

    slot \: slot number of the device where card is present.

    card \: bay number in which card is inserted.

    port \: port number on the card.

    signal type\: hardware signal of the specified

                 <slot>/<card>/<port>. Examples of signal

                 type are T1 SF and T1 ESF.

    .. data:: netsyncIfTypeUnknown = 1

    .. data:: netsyncIfTypeInternal = 2

    .. data:: netsyncIfTypeEthernet = 3

    .. data:: netsyncIfTypeSonet = 4

    .. data:: netsyncIfTypeTop = 5

    .. data:: netsyncIfTypeExt = 6

    .. data:: netsyncIfTypeController = 7

    .. data:: netsyncIfTypeGps = 8

    .. data:: netsyncIfTypeAtm = 9

    """

    netsyncIfTypeUnknown = Enum.YLeaf(1, "netsyncIfTypeUnknown")

    netsyncIfTypeInternal = Enum.YLeaf(2, "netsyncIfTypeInternal")

    netsyncIfTypeEthernet = Enum.YLeaf(3, "netsyncIfTypeEthernet")

    netsyncIfTypeSonet = Enum.YLeaf(4, "netsyncIfTypeSonet")

    netsyncIfTypeTop = Enum.YLeaf(5, "netsyncIfTypeTop")

    netsyncIfTypeExt = Enum.YLeaf(6, "netsyncIfTypeExt")

    netsyncIfTypeController = Enum.YLeaf(7, "netsyncIfTypeController")

    netsyncIfTypeGps = Enum.YLeaf(8, "netsyncIfTypeGps")

    netsyncIfTypeAtm = Enum.YLeaf(9, "netsyncIfTypeAtm")


class Cisconetsyncnetworkoption(Enum):
    """
    Cisconetsyncnetworkoption

    Network synchronization networking options.

    Network option                Network option type

    ===========================   ===================

    netsyncNetworkOptionUnknown   Unknown network option

    netsyncNetworkOption1         Option I

    netsyncNetworkOption2Gen1     Option II Generation 1

    netsyncNetworkOption2Gen2     Option II Generation 2

    netsyncNetworkOption3         Option III

    netsyncNetworkOptionInvalid   Invalid network option

    Option I refers to ITU\-T Option I synchronization networks.

    Option II refers to ITU\-T Option II synchronization networks

    designed for North America.

    Option III refers to ITU\-T Option III synchronization networks

    designed for Japan.

    .. data:: netsyncNetworkOptionUnknown = 1

    .. data:: netsyncNetworkOption1 = 2

    .. data:: netsyncNetworkOption2Gen1 = 3

    .. data:: netsyncNetworkOption2Gen2 = 4

    .. data:: netsyncNetworkOption3 = 5

    .. data:: netsyncNetworkOptionInvalid = 6

    """

    netsyncNetworkOptionUnknown = Enum.YLeaf(1, "netsyncNetworkOptionUnknown")

    netsyncNetworkOption1 = Enum.YLeaf(2, "netsyncNetworkOption1")

    netsyncNetworkOption2Gen1 = Enum.YLeaf(3, "netsyncNetworkOption2Gen1")

    netsyncNetworkOption2Gen2 = Enum.YLeaf(4, "netsyncNetworkOption2Gen2")

    netsyncNetworkOption3 = Enum.YLeaf(5, "netsyncNetworkOption3")

    netsyncNetworkOptionInvalid = Enum.YLeaf(6, "netsyncNetworkOptionInvalid")


class Cisconetsyncqlmode(Enum):
    """
    Cisconetsyncqlmode

    The clock mode of the network synchronization clock selection

    process as described in ITU\-T standard G.781 section 5.12.

    G.781 clock selection runs in one of two clock modes\:

    QL (Quality Level) enabled mode and QL disabled mode.  

    netsyncQLModeUnknown    \- QL mode unknown

    netsyncQLModeQlDisabled \- QL\-disabled mode;

                              clock selection is running 

                              in QL disabled mode,

                              which primarily considers

                              the source's priority as the

                              clock selection criteria.

    netsyncQLModeQlEnabled  \- QL\-enabled mode

                              clock selection is running

                              in QL enabled mode,

                              which primarily considers

                              the source's clock quality

                              level and priority as the

                              clock selection criteria.

    .. data:: netsyncQLModeUnknown = 1

    .. data:: netsyncQLModeQlDisabled = 2

    .. data:: netsyncQLModeQlEnabled = 3

    """

    netsyncQLModeUnknown = Enum.YLeaf(1, "netsyncQLModeUnknown")

    netsyncQLModeQlDisabled = Enum.YLeaf(2, "netsyncQLModeQlDisabled")

    netsyncQLModeQlEnabled = Enum.YLeaf(3, "netsyncQLModeQlEnabled")


class Cisconetsyncqualitylevel(Enum):
    """
    Cisconetsyncqualitylevel

    Clock source QL (quality level) is defined in ITU\-T G.781

    section 5.4 to reflect the synchronization quality within a

    network Option, i.e. I, II, and III.

    The following clock source quality levels are defined for the

    synchronization process of Option I\: 

    QL\-PRC     Primary reference clock 

    QL\-SSU\-A   Type I or V slave clock defined in ITU\-T G.811

    QL\-SSU\-B   Type VI slave clock defined in ITU\-T G.812

    QL\-SEC     Synchronous equipment clock

    QL\-DNU     Do not use for synchronization

    QL\-INVx    Unallocated SSM value,

               where x represent the value of SSM received

    QL\-FAILED  Signal failure state

    QL\-UNC     Unconnected to an input

    QL\-NSUPP   Not supporting the SSM processing

    The following clock source quality levels are defined for the

    synchronization process of Option II\: 

    QL\-PRS     PRS traceable

    QL\-STU     Synchronized; traceability unknown

    QL\-ST2     Stratum 2

    QL\-TNC     Transit node clock

    QL\-ST3E    Stratum 3E

    QL\-ST3     Stratum 3

    QL\-SMC     SONET clock self timed

    QL\-ST4     Stratum 4 freerun

    QL\-PROV    Provisionable by the network operator

    QL\-DUS     Do not use for synchronization

    QL\-INVx    Unallocated SSM value,

               where x represent the value of SSM received

    QL\-FAILED  Signal failure state

    QL\-UNC     Unconnected to an input

    QL\-NSUPP   Not supporting the SSM processing

    The following clock source quality levels are defined for the

    synchronization process of Option III\:

    QL\-UNK     Unknown clock source

    QL\-SEC     Synchronous equipment clock

    QL\-INVx    Unallocated SSM value,

               where x represent the value of SSM received

    QL\-FAILED  Signal failure state

    QL\-UNC     Unconnected to an input

    QL\-NSUPP   Not supporting the SSM processing        

    .. data:: netsyncQualityLevelNULL = 1

    .. data:: netsyncQualityLevelDNU = 2

    .. data:: netsyncQualityLevelDUS = 3

    .. data:: netsyncQualityLevelFAILED = 4

    .. data:: netsyncQualityLevelINV0 = 5

    .. data:: netsyncQualityLevelINV1 = 6

    .. data:: netsyncQualityLevelINV2 = 7

    .. data:: netsyncQualityLevelINV3 = 8

    .. data:: netsyncQualityLevelINV4 = 9

    .. data:: netsyncQualityLevelINV5 = 10

    .. data:: netsyncQualityLevelINV6 = 11

    .. data:: netsyncQualityLevelINV7 = 12

    .. data:: netsyncQualityLevelINV8 = 13

    .. data:: netsyncQualityLevelINV9 = 14

    .. data:: netsyncQualityLevelINV10 = 15

    .. data:: netsyncQualityLevelINV11 = 16

    .. data:: netsyncQualityLevelINV12 = 17

    .. data:: netsyncQualityLevelINV13 = 18

    .. data:: netsyncQualityLevelINV14 = 19

    .. data:: netsyncQualityLevelINV15 = 20

    .. data:: netsyncQualityLevelNSUPP = 21

    .. data:: netsyncQualityLevelPRC = 22

    .. data:: netsyncQualityLevelPROV = 23

    .. data:: netsyncQualityLevelPRS = 24

    .. data:: netsyncQualityLevelSEC = 25

    .. data:: netsyncQualityLevelSMC = 26

    .. data:: netsyncQualityLevelSSUA = 27

    .. data:: netsyncQualityLevelSSUB = 28

    .. data:: netsyncQualityLevelST2 = 29

    .. data:: netsyncQualityLevelST3 = 30

    .. data:: netsyncQualityLevelST3E = 31

    .. data:: netsyncQualityLevelST4 = 32

    .. data:: netsyncQualityLevelSTU = 33

    .. data:: netsyncQualityLevelTNC = 34

    .. data:: netsyncQualityLevelUNC = 35

    .. data:: netsyncQualityLevelUNK = 36

    """

    netsyncQualityLevelNULL = Enum.YLeaf(1, "netsyncQualityLevelNULL")

    netsyncQualityLevelDNU = Enum.YLeaf(2, "netsyncQualityLevelDNU")

    netsyncQualityLevelDUS = Enum.YLeaf(3, "netsyncQualityLevelDUS")

    netsyncQualityLevelFAILED = Enum.YLeaf(4, "netsyncQualityLevelFAILED")

    netsyncQualityLevelINV0 = Enum.YLeaf(5, "netsyncQualityLevelINV0")

    netsyncQualityLevelINV1 = Enum.YLeaf(6, "netsyncQualityLevelINV1")

    netsyncQualityLevelINV2 = Enum.YLeaf(7, "netsyncQualityLevelINV2")

    netsyncQualityLevelINV3 = Enum.YLeaf(8, "netsyncQualityLevelINV3")

    netsyncQualityLevelINV4 = Enum.YLeaf(9, "netsyncQualityLevelINV4")

    netsyncQualityLevelINV5 = Enum.YLeaf(10, "netsyncQualityLevelINV5")

    netsyncQualityLevelINV6 = Enum.YLeaf(11, "netsyncQualityLevelINV6")

    netsyncQualityLevelINV7 = Enum.YLeaf(12, "netsyncQualityLevelINV7")

    netsyncQualityLevelINV8 = Enum.YLeaf(13, "netsyncQualityLevelINV8")

    netsyncQualityLevelINV9 = Enum.YLeaf(14, "netsyncQualityLevelINV9")

    netsyncQualityLevelINV10 = Enum.YLeaf(15, "netsyncQualityLevelINV10")

    netsyncQualityLevelINV11 = Enum.YLeaf(16, "netsyncQualityLevelINV11")

    netsyncQualityLevelINV12 = Enum.YLeaf(17, "netsyncQualityLevelINV12")

    netsyncQualityLevelINV13 = Enum.YLeaf(18, "netsyncQualityLevelINV13")

    netsyncQualityLevelINV14 = Enum.YLeaf(19, "netsyncQualityLevelINV14")

    netsyncQualityLevelINV15 = Enum.YLeaf(20, "netsyncQualityLevelINV15")

    netsyncQualityLevelNSUPP = Enum.YLeaf(21, "netsyncQualityLevelNSUPP")

    netsyncQualityLevelPRC = Enum.YLeaf(22, "netsyncQualityLevelPRC")

    netsyncQualityLevelPROV = Enum.YLeaf(23, "netsyncQualityLevelPROV")

    netsyncQualityLevelPRS = Enum.YLeaf(24, "netsyncQualityLevelPRS")

    netsyncQualityLevelSEC = Enum.YLeaf(25, "netsyncQualityLevelSEC")

    netsyncQualityLevelSMC = Enum.YLeaf(26, "netsyncQualityLevelSMC")

    netsyncQualityLevelSSUA = Enum.YLeaf(27, "netsyncQualityLevelSSUA")

    netsyncQualityLevelSSUB = Enum.YLeaf(28, "netsyncQualityLevelSSUB")

    netsyncQualityLevelST2 = Enum.YLeaf(29, "netsyncQualityLevelST2")

    netsyncQualityLevelST3 = Enum.YLeaf(30, "netsyncQualityLevelST3")

    netsyncQualityLevelST3E = Enum.YLeaf(31, "netsyncQualityLevelST3E")

    netsyncQualityLevelST4 = Enum.YLeaf(32, "netsyncQualityLevelST4")

    netsyncQualityLevelSTU = Enum.YLeaf(33, "netsyncQualityLevelSTU")

    netsyncQualityLevelTNC = Enum.YLeaf(34, "netsyncQualityLevelTNC")

    netsyncQualityLevelUNC = Enum.YLeaf(35, "netsyncQualityLevelUNC")

    netsyncQualityLevelUNK = Enum.YLeaf(36, "netsyncQualityLevelUNK")


class Cisconetsyncssmcap(Enum):
    """
    Cisconetsyncssmcap

    Network synchronization clock source interface SSM

    (Synchronization Status Message) capability.

    SSM Capability         Capability information

    =====================  ======================

    netsyncSSMCapNone      No SSM capability

    netsyncSSMCapTxRx      To transmit and receive SSM

    netsyncSSMCapTx        To transmit SSM only

    netsyncSSMCapRx        To receive SSM only

    netsyncSSMCapInvalid   Capability invalid or unsupported

    .. data:: netsyncSSMCapNone = 1

    .. data:: netsyncSSMCapTxRx = 2

    .. data:: netsyncSSMCapTx = 3

    .. data:: netsyncSSMCapRx = 4

    .. data:: netsyncSSMCapInvalid = 5

    """

    netsyncSSMCapNone = Enum.YLeaf(1, "netsyncSSMCapNone")

    netsyncSSMCapTxRx = Enum.YLeaf(2, "netsyncSSMCapTxRx")

    netsyncSSMCapTx = Enum.YLeaf(3, "netsyncSSMCapTx")

    netsyncSSMCapRx = Enum.YLeaf(4, "netsyncSSMCapRx")

    netsyncSSMCapInvalid = Enum.YLeaf(5, "netsyncSSMCapInvalid")


class Cisconetsyncalarminfo(Bits):
    """
    Cisconetsyncalarminfo

    Input clock source's alarm reasons\:
    
    netsyncSrcAlarmReasonAIS      \- Alarm Indication Signal
    netsyncSrcAlarmReasonOOR      \- Out of range
    netsyncSrcAlarmReasonOIR      \- Online Insertion Removal
    netsyncSrcAlarmReasonInternal \- Internal
    Keys are:- netsyncSrcAlarmReasonInternal , netsyncSrcAlarmReasonOIR , netsyncSrcAlarmReasonAIS , netsyncSrcAlarmReasonOOR

    """

    def __init__(self):
        super(Cisconetsyncalarminfo, self).__init__()


class CiscoNetsyncMib(Entity):
    """
    
    
    .. attribute:: cisconetsyncmibnotifcontrol
    
    	
    	**type**\:   :py:class:`Cisconetsyncmibnotifcontrol <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cisconetsyncmibnotifcontrol>`
    
    .. attribute:: cnsclkselglobaltable
    
    	G.781 clock selection process table. This table contains the global parameters for the G.781 clock selection process
    	**type**\:   :py:class:`Cnsclkselglobaltable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsclkselglobaltable>`
    
    .. attribute:: cnsextoutputtable
    
    	T4 external output table. This table contains a list of T4 external outputs.  Each T4 external output is associated with clock source(s) to be found in cnsT4ClockSourceTable. The clock selection process considers all the available clock sources and select the T4 clock source based on the G.781 clock selection algorithm
    	**type**\:   :py:class:`Cnsextoutputtable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsextoutputtable>`
    
    .. attribute:: cnsinputsourcetable
    
    	T0 clock source table. This table contains a list of input sources for input T0 clock selection
    	**type**\:   :py:class:`Cnsinputsourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsinputsourcetable>`
    
    .. attribute:: cnsselectedinputsourcetable
    
    	T0 selected clock source table. This table contains the selected clock source for the input T0 clock
    	**type**\:   :py:class:`Cnsselectedinputsourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsselectedinputsourcetable>`
    
    .. attribute:: cnst4clocksourcetable
    
    	T4 clock source table. This table contains a list of input sources for a specific T4 external output. An entry shall be added to cnsExtOutputTable first. Then clock sources shall be added in this table for the selection process to select the appropriate T4 clock source
    	**type**\:   :py:class:`Cnst4Clocksourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnst4Clocksourcetable>`
    
    

    """

    _prefix = 'CISCO-NETSYNC-MIB'
    _revision = '2010-10-15'

    def __init__(self):
        super(CiscoNetsyncMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-NETSYNC-MIB"
        self.yang_parent_name = "CISCO-NETSYNC-MIB"

        self.cisconetsyncmibnotifcontrol = CiscoNetsyncMib.Cisconetsyncmibnotifcontrol()
        self.cisconetsyncmibnotifcontrol.parent = self
        self._children_name_map["cisconetsyncmibnotifcontrol"] = "ciscoNetsyncMIBNotifControl"
        self._children_yang_names.add("ciscoNetsyncMIBNotifControl")

        self.cnsclkselglobaltable = CiscoNetsyncMib.Cnsclkselglobaltable()
        self.cnsclkselglobaltable.parent = self
        self._children_name_map["cnsclkselglobaltable"] = "cnsClkSelGlobalTable"
        self._children_yang_names.add("cnsClkSelGlobalTable")

        self.cnsextoutputtable = CiscoNetsyncMib.Cnsextoutputtable()
        self.cnsextoutputtable.parent = self
        self._children_name_map["cnsextoutputtable"] = "cnsExtOutputTable"
        self._children_yang_names.add("cnsExtOutputTable")

        self.cnsinputsourcetable = CiscoNetsyncMib.Cnsinputsourcetable()
        self.cnsinputsourcetable.parent = self
        self._children_name_map["cnsinputsourcetable"] = "cnsInputSourceTable"
        self._children_yang_names.add("cnsInputSourceTable")

        self.cnsselectedinputsourcetable = CiscoNetsyncMib.Cnsselectedinputsourcetable()
        self.cnsselectedinputsourcetable.parent = self
        self._children_name_map["cnsselectedinputsourcetable"] = "cnsSelectedInputSourceTable"
        self._children_yang_names.add("cnsSelectedInputSourceTable")

        self.cnst4clocksourcetable = CiscoNetsyncMib.Cnst4Clocksourcetable()
        self.cnst4clocksourcetable.parent = self
        self._children_name_map["cnst4clocksourcetable"] = "cnsT4ClockSourceTable"
        self._children_yang_names.add("cnsT4ClockSourceTable")


    class Cisconetsyncmibnotifcontrol(Entity):
        """
        
        
        .. attribute:: cnsmibenablestatusnotification
        
        	A control object to enable/disable ciscoNetsyncSelectedT0Clock, ciscoNetsyncSelectedT4Clock, ciscoNetsyncInputSignalFailureStatus, ciscoNetsyncInputAlarmStatus notifications at the system level. This object should hold any of the below values.     true \- The notif is enabled globally for the system     false\- The notif is disabled globally for the system
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cisconetsyncmibnotifcontrol, self).__init__()

            self.yang_name = "ciscoNetsyncMIBNotifControl"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnsmibenablestatusnotification = YLeaf(YType.boolean, "cnsMIBEnableStatusNotification")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cnsmibenablestatusnotification") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cisconetsyncmibnotifcontrol, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cisconetsyncmibnotifcontrol, self).__setattr__(name, value)

        def has_data(self):
            return self.cnsmibenablestatusnotification.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cnsmibenablestatusnotification.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoNetsyncMIBNotifControl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cnsmibenablestatusnotification.is_set or self.cnsmibenablestatusnotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cnsmibenablestatusnotification.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsMIBEnableStatusNotification"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cnsMIBEnableStatusNotification"):
                self.cnsmibenablestatusnotification = value
                self.cnsmibenablestatusnotification.value_namespace = name_space
                self.cnsmibenablestatusnotification.value_namespace_prefix = name_space_prefix


    class Cnsclkselglobaltable(Entity):
        """
        G.781 clock selection process table.
        This table contains the global parameters for the G.781 clock
        selection process.
        
        .. attribute:: cnsclkselglobalentry
        
        	An entry is added to cnsClkSelGlobalTable when G.781 clock selection is enabled in the device configuration.  The entry is removed when G.781 clock selection is removed from the configuration
        	**type**\: list of    :py:class:`Cnsclkselglobalentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsclkselglobaltable.Cnsclkselglobalentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cnsclkselglobaltable, self).__init__()

            self.yang_name = "cnsClkSelGlobalTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnsclkselglobalentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cnsclkselglobaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cnsclkselglobaltable, self).__setattr__(name, value)


        class Cnsclkselglobalentry(Entity):
            """
            An entry is added to cnsClkSelGlobalTable when G.781 clock
            selection is enabled in the device configuration.  The entry
            is removed when G.781 clock selection is removed from the
            configuration.
            
            .. attribute:: cnsclkselgloprocindex  <key>
            
            	An index that uniquely represents a clock selection process.  This index is assigned arbitrarily by the system and may not be persistent across reboots
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselglobclockmode
            
            	This object indicates the operating mode of the system clock
            	**type**\:   :py:class:`Cisconetsyncclockmode <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncclockmode>`
            
            .. attribute:: cnsclkselglobcurrholdoverseconds
            
            	This object indicates the duration of the current holdover period. If a system clock is in holdover mode, the object carries the current holdover duration in seconds. If the system clock is not in holdover, the object carries the value 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cnsclkselglobeecoption
            
            	This object indicates the network synchronization EEC (Ethernet Equipment Clock) option
            	**type**\:   :py:class:`Cisconetsynceecoption <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsynceecoption>`
            
            .. attribute:: cnsclkselglobesmcmode
            
            	This object indicates if global ESMC is enabled. With ESMC enabled globally, the system is capable of handling ESMC messages
            	**type**\:  bool
            
            .. attribute:: cnsclkselglobholdofftime
            
            	This object indicates the global holdoff time in the G.781 clock selection process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnsclkselgloblastholdoverseconds
            
            	This object indicates the duration of the last holdover period in seconds. If the holdover duration is less than a second, the object will carry the value zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cnsclkselglobnetsyncenable
            
            	This object indicates whether the G.781 clock selection is enabled or not.  'true'  \- G.781 clock selection is enabled 'false' \- G.781 clock selection is disabled
            	**type**\:  bool
            
            .. attribute:: cnsclkselglobnetworkoption
            
            	This object indicates the synchronization network option
            	**type**\:   :py:class:`Cisconetsyncnetworkoption <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncnetworkoption>`
            
            .. attribute:: cnsclkselglobnofsources
            
            	This object indicates the number of synchronization sources currently configured for the G.781 clock selection process
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: clock sources
            
            .. attribute:: cnsclkselglobprocessmode
            
            	This object indicates the QL mode of the network synchronization clock selection process as described in ITU\-T standard G.781 section 5.12
            	**type**\:   :py:class:`Cisconetsyncqlmode <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqlmode>`
            
            .. attribute:: cnsclkselglobrevertivemode
            
            	This object indicates the revertive mode setting in the G.781 clock selection process.  The switching of clock sources can be made revertive or non\-revertive. In non\-revertive mode, an alternate clock source is maintained even after the original clock source has recovered from the failure that caused the switch. In revertive mode, the clock selection process switches back to the original clock source after recovering from the failure
            	**type**\:  bool
            
            .. attribute:: cnsclkselglobwtrtime
            
            	This object indicates the global wait\-to\-restore time in the G.781 clock selection process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CiscoNetsyncMib.Cnsclkselglobaltable.Cnsclkselglobalentry, self).__init__()

                self.yang_name = "cnsClkSelGlobalEntry"
                self.yang_parent_name = "cnsClkSelGlobalTable"

                self.cnsclkselgloprocindex = YLeaf(YType.uint32, "cnsClkSelGloProcIndex")

                self.cnsclkselglobclockmode = YLeaf(YType.enumeration, "cnsClkSelGlobClockMode")

                self.cnsclkselglobcurrholdoverseconds = YLeaf(YType.uint32, "cnsClkSelGlobCurrHoldoverSeconds")

                self.cnsclkselglobeecoption = YLeaf(YType.enumeration, "cnsClkSelGlobEECOption")

                self.cnsclkselglobesmcmode = YLeaf(YType.boolean, "cnsClkSelGlobESMCMode")

                self.cnsclkselglobholdofftime = YLeaf(YType.uint32, "cnsClkSelGlobHoldoffTime")

                self.cnsclkselgloblastholdoverseconds = YLeaf(YType.uint32, "cnsClkSelGlobLastHoldoverSeconds")

                self.cnsclkselglobnetsyncenable = YLeaf(YType.boolean, "cnsClkSelGlobNetsyncEnable")

                self.cnsclkselglobnetworkoption = YLeaf(YType.enumeration, "cnsClkSelGlobNetworkOption")

                self.cnsclkselglobnofsources = YLeaf(YType.uint32, "cnsClkSelGlobNofSources")

                self.cnsclkselglobprocessmode = YLeaf(YType.enumeration, "cnsClkSelGlobProcessMode")

                self.cnsclkselglobrevertivemode = YLeaf(YType.boolean, "cnsClkSelGlobRevertiveMode")

                self.cnsclkselglobwtrtime = YLeaf(YType.uint32, "cnsClkSelGlobWtrTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnsclkselgloprocindex",
                                "cnsclkselglobclockmode",
                                "cnsclkselglobcurrholdoverseconds",
                                "cnsclkselglobeecoption",
                                "cnsclkselglobesmcmode",
                                "cnsclkselglobholdofftime",
                                "cnsclkselgloblastholdoverseconds",
                                "cnsclkselglobnetsyncenable",
                                "cnsclkselglobnetworkoption",
                                "cnsclkselglobnofsources",
                                "cnsclkselglobprocessmode",
                                "cnsclkselglobrevertivemode",
                                "cnsclkselglobwtrtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNetsyncMib.Cnsclkselglobaltable.Cnsclkselglobalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNetsyncMib.Cnsclkselglobaltable.Cnsclkselglobalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnsclkselgloprocindex.is_set or
                    self.cnsclkselglobclockmode.is_set or
                    self.cnsclkselglobcurrholdoverseconds.is_set or
                    self.cnsclkselglobeecoption.is_set or
                    self.cnsclkselglobesmcmode.is_set or
                    self.cnsclkselglobholdofftime.is_set or
                    self.cnsclkselgloblastholdoverseconds.is_set or
                    self.cnsclkselglobnetsyncenable.is_set or
                    self.cnsclkselglobnetworkoption.is_set or
                    self.cnsclkselglobnofsources.is_set or
                    self.cnsclkselglobprocessmode.is_set or
                    self.cnsclkselglobrevertivemode.is_set or
                    self.cnsclkselglobwtrtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnsclkselgloprocindex.yfilter != YFilter.not_set or
                    self.cnsclkselglobclockmode.yfilter != YFilter.not_set or
                    self.cnsclkselglobcurrholdoverseconds.yfilter != YFilter.not_set or
                    self.cnsclkselglobeecoption.yfilter != YFilter.not_set or
                    self.cnsclkselglobesmcmode.yfilter != YFilter.not_set or
                    self.cnsclkselglobholdofftime.yfilter != YFilter.not_set or
                    self.cnsclkselgloblastholdoverseconds.yfilter != YFilter.not_set or
                    self.cnsclkselglobnetsyncenable.yfilter != YFilter.not_set or
                    self.cnsclkselglobnetworkoption.yfilter != YFilter.not_set or
                    self.cnsclkselglobnofsources.yfilter != YFilter.not_set or
                    self.cnsclkselglobprocessmode.yfilter != YFilter.not_set or
                    self.cnsclkselglobrevertivemode.yfilter != YFilter.not_set or
                    self.cnsclkselglobwtrtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnsClkSelGlobalEntry" + "[cnsClkSelGloProcIndex='" + self.cnsclkselgloprocindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsClkSelGlobalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnsclkselgloprocindex.is_set or self.cnsclkselgloprocindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselgloprocindex.get_name_leafdata())
                if (self.cnsclkselglobclockmode.is_set or self.cnsclkselglobclockmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobclockmode.get_name_leafdata())
                if (self.cnsclkselglobcurrholdoverseconds.is_set or self.cnsclkselglobcurrholdoverseconds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobcurrholdoverseconds.get_name_leafdata())
                if (self.cnsclkselglobeecoption.is_set or self.cnsclkselglobeecoption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobeecoption.get_name_leafdata())
                if (self.cnsclkselglobesmcmode.is_set or self.cnsclkselglobesmcmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobesmcmode.get_name_leafdata())
                if (self.cnsclkselglobholdofftime.is_set or self.cnsclkselglobholdofftime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobholdofftime.get_name_leafdata())
                if (self.cnsclkselgloblastholdoverseconds.is_set or self.cnsclkselgloblastholdoverseconds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselgloblastholdoverseconds.get_name_leafdata())
                if (self.cnsclkselglobnetsyncenable.is_set or self.cnsclkselglobnetsyncenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobnetsyncenable.get_name_leafdata())
                if (self.cnsclkselglobnetworkoption.is_set or self.cnsclkselglobnetworkoption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobnetworkoption.get_name_leafdata())
                if (self.cnsclkselglobnofsources.is_set or self.cnsclkselglobnofsources.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobnofsources.get_name_leafdata())
                if (self.cnsclkselglobprocessmode.is_set or self.cnsclkselglobprocessmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobprocessmode.get_name_leafdata())
                if (self.cnsclkselglobrevertivemode.is_set or self.cnsclkselglobrevertivemode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobrevertivemode.get_name_leafdata())
                if (self.cnsclkselglobwtrtime.is_set or self.cnsclkselglobwtrtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsclkselglobwtrtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnsClkSelGloProcIndex" or name == "cnsClkSelGlobClockMode" or name == "cnsClkSelGlobCurrHoldoverSeconds" or name == "cnsClkSelGlobEECOption" or name == "cnsClkSelGlobESMCMode" or name == "cnsClkSelGlobHoldoffTime" or name == "cnsClkSelGlobLastHoldoverSeconds" or name == "cnsClkSelGlobNetsyncEnable" or name == "cnsClkSelGlobNetworkOption" or name == "cnsClkSelGlobNofSources" or name == "cnsClkSelGlobProcessMode" or name == "cnsClkSelGlobRevertiveMode" or name == "cnsClkSelGlobWtrTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnsClkSelGloProcIndex"):
                    self.cnsclkselgloprocindex = value
                    self.cnsclkselgloprocindex.value_namespace = name_space
                    self.cnsclkselgloprocindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobClockMode"):
                    self.cnsclkselglobclockmode = value
                    self.cnsclkselglobclockmode.value_namespace = name_space
                    self.cnsclkselglobclockmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobCurrHoldoverSeconds"):
                    self.cnsclkselglobcurrholdoverseconds = value
                    self.cnsclkselglobcurrholdoverseconds.value_namespace = name_space
                    self.cnsclkselglobcurrholdoverseconds.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobEECOption"):
                    self.cnsclkselglobeecoption = value
                    self.cnsclkselglobeecoption.value_namespace = name_space
                    self.cnsclkselglobeecoption.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobESMCMode"):
                    self.cnsclkselglobesmcmode = value
                    self.cnsclkselglobesmcmode.value_namespace = name_space
                    self.cnsclkselglobesmcmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobHoldoffTime"):
                    self.cnsclkselglobholdofftime = value
                    self.cnsclkselglobholdofftime.value_namespace = name_space
                    self.cnsclkselglobholdofftime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobLastHoldoverSeconds"):
                    self.cnsclkselgloblastholdoverseconds = value
                    self.cnsclkselgloblastholdoverseconds.value_namespace = name_space
                    self.cnsclkselgloblastholdoverseconds.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobNetsyncEnable"):
                    self.cnsclkselglobnetsyncenable = value
                    self.cnsclkselglobnetsyncenable.value_namespace = name_space
                    self.cnsclkselglobnetsyncenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobNetworkOption"):
                    self.cnsclkselglobnetworkoption = value
                    self.cnsclkselglobnetworkoption.value_namespace = name_space
                    self.cnsclkselglobnetworkoption.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobNofSources"):
                    self.cnsclkselglobnofsources = value
                    self.cnsclkselglobnofsources.value_namespace = name_space
                    self.cnsclkselglobnofsources.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobProcessMode"):
                    self.cnsclkselglobprocessmode = value
                    self.cnsclkselglobprocessmode.value_namespace = name_space
                    self.cnsclkselglobprocessmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobRevertiveMode"):
                    self.cnsclkselglobrevertivemode = value
                    self.cnsclkselglobrevertivemode.value_namespace = name_space
                    self.cnsclkselglobrevertivemode.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsClkSelGlobWtrTime"):
                    self.cnsclkselglobwtrtime = value
                    self.cnsclkselglobwtrtime.value_namespace = name_space
                    self.cnsclkselglobwtrtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnsclkselglobalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnsclkselglobalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnsClkSelGlobalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnsClkSelGlobalEntry"):
                for c in self.cnsclkselglobalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNetsyncMib.Cnsclkselglobaltable.Cnsclkselglobalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnsclkselglobalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsClkSelGlobalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnsselectedinputsourcetable(Entity):
        """
        T0 selected clock source table.
        This table contains the selected clock source for the input T0
        clock.
        
        .. attribute:: cnsselectedinputsourceentry
        
        	An entry is created in the table when the G.781 clock selection process has successfully selected a T0 clock source.  The entry shall remain during the time the G.781 clock selection process remains enabled
        	**type**\: list of    :py:class:`Cnsselectedinputsourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cnsselectedinputsourcetable, self).__init__()

            self.yang_name = "cnsSelectedInputSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnsselectedinputsourceentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cnsselectedinputsourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cnsselectedinputsourcetable, self).__setattr__(name, value)


        class Cnsselectedinputsourceentry(Entity):
            """
            An entry is created in the table when the G.781 clock
            selection process has successfully selected a T0 clock
            source.  The entry shall remain during the time
            the G.781 clock selection process remains enabled.
            
            .. attribute:: cnsselinpsrcnetsyncindex  <key>
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsselinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\:  bool
            
            .. attribute:: cnsselinpsrcintftype
            
            	This object indicates the type of the selected T0 clock
            	**type**\:   :py:class:`Cisconetsynciftype <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsynciftype>`
            
            .. attribute:: cnsselinpsrcmsw
            
            	This object indicates the manual switching flag. The 'true' value indicates the currently selected clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode. Furthermore, in QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\:  bool
            
            .. attribute:: cnsselinpsrcname
            
            	This object indicates the name of the selected T0 clock
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cnsselinpsrcpriority
            
            	This object indicates the configured priority of the selected T0 clock. A smaller value represents a higher priority
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnsselinpsrcqualitylevel
            
            	This object indicates the selected T0 clock source's effective quality level, which is the derived clock quality based on the three factors\:  (a) Received quality level.  (b) Configured Rx quality level.  This factor supersedes (a).  (c) System overridden quality level as a result of exceptional events such as signal failure or ESMC failure.  This factor supersedes (a) and (b)
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsselinpsrctimestamp
            
            	This object indicates the timestamp of the T0 clock source being selected by the G.781 clock selection process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CiscoNetsyncMib.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry, self).__init__()

                self.yang_name = "cnsSelectedInputSourceEntry"
                self.yang_parent_name = "cnsSelectedInputSourceTable"

                self.cnsselinpsrcnetsyncindex = YLeaf(YType.uint32, "cnsSelInpSrcNetsyncIndex")

                self.cnsselinpsrcfsw = YLeaf(YType.boolean, "cnsSelInpSrcFSW")

                self.cnsselinpsrcintftype = YLeaf(YType.enumeration, "cnsSelInpSrcIntfType")

                self.cnsselinpsrcmsw = YLeaf(YType.boolean, "cnsSelInpSrcMSW")

                self.cnsselinpsrcname = YLeaf(YType.str, "cnsSelInpSrcName")

                self.cnsselinpsrcpriority = YLeaf(YType.uint32, "cnsSelInpSrcPriority")

                self.cnsselinpsrcqualitylevel = YLeaf(YType.enumeration, "cnsSelInpSrcQualityLevel")

                self.cnsselinpsrctimestamp = YLeaf(YType.uint32, "cnsSelInpSrcTimestamp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnsselinpsrcnetsyncindex",
                                "cnsselinpsrcfsw",
                                "cnsselinpsrcintftype",
                                "cnsselinpsrcmsw",
                                "cnsselinpsrcname",
                                "cnsselinpsrcpriority",
                                "cnsselinpsrcqualitylevel",
                                "cnsselinpsrctimestamp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNetsyncMib.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNetsyncMib.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnsselinpsrcnetsyncindex.is_set or
                    self.cnsselinpsrcfsw.is_set or
                    self.cnsselinpsrcintftype.is_set or
                    self.cnsselinpsrcmsw.is_set or
                    self.cnsselinpsrcname.is_set or
                    self.cnsselinpsrcpriority.is_set or
                    self.cnsselinpsrcqualitylevel.is_set or
                    self.cnsselinpsrctimestamp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnsselinpsrcnetsyncindex.yfilter != YFilter.not_set or
                    self.cnsselinpsrcfsw.yfilter != YFilter.not_set or
                    self.cnsselinpsrcintftype.yfilter != YFilter.not_set or
                    self.cnsselinpsrcmsw.yfilter != YFilter.not_set or
                    self.cnsselinpsrcname.yfilter != YFilter.not_set or
                    self.cnsselinpsrcpriority.yfilter != YFilter.not_set or
                    self.cnsselinpsrcqualitylevel.yfilter != YFilter.not_set or
                    self.cnsselinpsrctimestamp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnsSelectedInputSourceEntry" + "[cnsSelInpSrcNetsyncIndex='" + self.cnsselinpsrcnetsyncindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsSelectedInputSourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnsselinpsrcnetsyncindex.is_set or self.cnsselinpsrcnetsyncindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcnetsyncindex.get_name_leafdata())
                if (self.cnsselinpsrcfsw.is_set or self.cnsselinpsrcfsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcfsw.get_name_leafdata())
                if (self.cnsselinpsrcintftype.is_set or self.cnsselinpsrcintftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcintftype.get_name_leafdata())
                if (self.cnsselinpsrcmsw.is_set or self.cnsselinpsrcmsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcmsw.get_name_leafdata())
                if (self.cnsselinpsrcname.is_set or self.cnsselinpsrcname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcname.get_name_leafdata())
                if (self.cnsselinpsrcpriority.is_set or self.cnsselinpsrcpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcpriority.get_name_leafdata())
                if (self.cnsselinpsrcqualitylevel.is_set or self.cnsselinpsrcqualitylevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrcqualitylevel.get_name_leafdata())
                if (self.cnsselinpsrctimestamp.is_set or self.cnsselinpsrctimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsselinpsrctimestamp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnsSelInpSrcNetsyncIndex" or name == "cnsSelInpSrcFSW" or name == "cnsSelInpSrcIntfType" or name == "cnsSelInpSrcMSW" or name == "cnsSelInpSrcName" or name == "cnsSelInpSrcPriority" or name == "cnsSelInpSrcQualityLevel" or name == "cnsSelInpSrcTimestamp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnsSelInpSrcNetsyncIndex"):
                    self.cnsselinpsrcnetsyncindex = value
                    self.cnsselinpsrcnetsyncindex.value_namespace = name_space
                    self.cnsselinpsrcnetsyncindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcFSW"):
                    self.cnsselinpsrcfsw = value
                    self.cnsselinpsrcfsw.value_namespace = name_space
                    self.cnsselinpsrcfsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcIntfType"):
                    self.cnsselinpsrcintftype = value
                    self.cnsselinpsrcintftype.value_namespace = name_space
                    self.cnsselinpsrcintftype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcMSW"):
                    self.cnsselinpsrcmsw = value
                    self.cnsselinpsrcmsw.value_namespace = name_space
                    self.cnsselinpsrcmsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcName"):
                    self.cnsselinpsrcname = value
                    self.cnsselinpsrcname.value_namespace = name_space
                    self.cnsselinpsrcname.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcPriority"):
                    self.cnsselinpsrcpriority = value
                    self.cnsselinpsrcpriority.value_namespace = name_space
                    self.cnsselinpsrcpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcQualityLevel"):
                    self.cnsselinpsrcqualitylevel = value
                    self.cnsselinpsrcqualitylevel.value_namespace = name_space
                    self.cnsselinpsrcqualitylevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsSelInpSrcTimestamp"):
                    self.cnsselinpsrctimestamp = value
                    self.cnsselinpsrctimestamp.value_namespace = name_space
                    self.cnsselinpsrctimestamp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnsselectedinputsourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnsselectedinputsourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnsSelectedInputSourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnsSelectedInputSourceEntry"):
                for c in self.cnsselectedinputsourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNetsyncMib.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnsselectedinputsourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsSelectedInputSourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnsinputsourcetable(Entity):
        """
        T0 clock source table.
        This table contains a list of input sources for input T0 clock
        selection.
        
        .. attribute:: cnsinputsourceentry
        
        	An entry is created in the table when a user adds a T0 clock source in the configuration. An entry is removed  in the table when a user removes a T0 clock source from the configuration
        	**type**\: list of    :py:class:`Cnsinputsourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsinputsourcetable.Cnsinputsourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cnsinputsourcetable, self).__init__()

            self.yang_name = "cnsInputSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnsinputsourceentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cnsinputsourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cnsinputsourcetable, self).__setattr__(name, value)


        class Cnsinputsourceentry(Entity):
            """
            An entry is created in the table when a user adds a T0
            clock source in the configuration. An entry is removed 
            in the table when a user removes a T0 clock source from
            the configuration.
            
            .. attribute:: cnsinpsrcnetsyncindex  <key>
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsinpsrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the input clock source
            	**type**\:  bool
            
            .. attribute:: cnsinpsrcalarminfo
            
            	This object indicates the alarm reasons of an input clock source if an alarm event is being reported on it
            	**type**\:   :py:class:`Cisconetsyncalarminfo <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncalarminfo>`
            
            .. attribute:: cnsinpsrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T0 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:   :py:class:`Cisconetsyncesmccap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncesmccap>`
            
            .. attribute:: cnsinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\:  bool
            
            .. attribute:: cnsinpsrcholdofftime
            
            	This object indicates the hold\-off time value of an input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnsinpsrcintftype
            
            	This object indicates the type of an input clock source configured for the T0 clock selection
            	**type**\:   :py:class:`Cisconetsynciftype <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsynciftype>`
            
            .. attribute:: cnsinpsrclockout
            
            	This object indicates whether or not the lockout command has been applied to a clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\:  bool
            
            .. attribute:: cnsinpsrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected clock source is a result of the manual switching. The switch allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in cnsInputSourceTable.  A clock source is not locked out when cnsInpSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsInpSrcSignalFailure contains the value 'false'.  The QL is identified in cnsInpSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\:  bool
            
            .. attribute:: cnsinpsrcname
            
            	This object indicates the name of an input clock source configured for the T0 clock selection
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cnsinpsrcpriority
            
            	This object indicates the priority of an input clock source configured for the T0 clock selection.  A smaller value represents a higher priority
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnsinpsrcqualitylevel
            
            	This object indicates the current clock quality level of the input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsinpsrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsinpsrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of an input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsinpsrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsinpsrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of an input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsinpsrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the input clock source
            	**type**\:  bool
            
            .. attribute:: cnsinpsrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T0 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:   :py:class:`Cisconetsyncssmcap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncssmcap>`
            
            .. attribute:: cnsinpsrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of an input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Seconds
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CiscoNetsyncMib.Cnsinputsourcetable.Cnsinputsourceentry, self).__init__()

                self.yang_name = "cnsInputSourceEntry"
                self.yang_parent_name = "cnsInputSourceTable"

                self.cnsinpsrcnetsyncindex = YLeaf(YType.uint32, "cnsInpSrcNetsyncIndex")

                self.cnsinpsrcalarm = YLeaf(YType.boolean, "cnsInpSrcAlarm")

                self.cnsinpsrcalarminfo = YLeaf(YType.bits, "cnsInpSrcAlarmInfo")

                self.cnsinpsrcesmccap = YLeaf(YType.enumeration, "cnsInpSrcESMCCap")

                self.cnsinpsrcfsw = YLeaf(YType.boolean, "cnsInpSrcFSW")

                self.cnsinpsrcholdofftime = YLeaf(YType.uint32, "cnsInpSrcHoldoffTime")

                self.cnsinpsrcintftype = YLeaf(YType.enumeration, "cnsInpSrcIntfType")

                self.cnsinpsrclockout = YLeaf(YType.boolean, "cnsInpSrcLockout")

                self.cnsinpsrcmsw = YLeaf(YType.boolean, "cnsInpSrcMSW")

                self.cnsinpsrcname = YLeaf(YType.str, "cnsInpSrcName")

                self.cnsinpsrcpriority = YLeaf(YType.uint32, "cnsInpSrcPriority")

                self.cnsinpsrcqualitylevel = YLeaf(YType.enumeration, "cnsInpSrcQualityLevel")

                self.cnsinpsrcqualitylevelrx = YLeaf(YType.enumeration, "cnsInpSrcQualityLevelRx")

                self.cnsinpsrcqualitylevelrxcfg = YLeaf(YType.enumeration, "cnsInpSrcQualityLevelRxCfg")

                self.cnsinpsrcqualityleveltx = YLeaf(YType.enumeration, "cnsInpSrcQualityLevelTx")

                self.cnsinpsrcqualityleveltxcfg = YLeaf(YType.enumeration, "cnsInpSrcQualityLevelTxCfg")

                self.cnsinpsrcsignalfailure = YLeaf(YType.boolean, "cnsInpSrcSignalFailure")

                self.cnsinpsrcssmcap = YLeaf(YType.enumeration, "cnsInpSrcSSMCap")

                self.cnsinpsrcwtrtime = YLeaf(YType.uint32, "cnsInpSrcWtrTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnsinpsrcnetsyncindex",
                                "cnsinpsrcalarm",
                                "cnsinpsrcalarminfo",
                                "cnsinpsrcesmccap",
                                "cnsinpsrcfsw",
                                "cnsinpsrcholdofftime",
                                "cnsinpsrcintftype",
                                "cnsinpsrclockout",
                                "cnsinpsrcmsw",
                                "cnsinpsrcname",
                                "cnsinpsrcpriority",
                                "cnsinpsrcqualitylevel",
                                "cnsinpsrcqualitylevelrx",
                                "cnsinpsrcqualitylevelrxcfg",
                                "cnsinpsrcqualityleveltx",
                                "cnsinpsrcqualityleveltxcfg",
                                "cnsinpsrcsignalfailure",
                                "cnsinpsrcssmcap",
                                "cnsinpsrcwtrtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNetsyncMib.Cnsinputsourcetable.Cnsinputsourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNetsyncMib.Cnsinputsourcetable.Cnsinputsourceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnsinpsrcnetsyncindex.is_set or
                    self.cnsinpsrcalarm.is_set or
                    self.cnsinpsrcalarminfo.is_set or
                    self.cnsinpsrcesmccap.is_set or
                    self.cnsinpsrcfsw.is_set or
                    self.cnsinpsrcholdofftime.is_set or
                    self.cnsinpsrcintftype.is_set or
                    self.cnsinpsrclockout.is_set or
                    self.cnsinpsrcmsw.is_set or
                    self.cnsinpsrcname.is_set or
                    self.cnsinpsrcpriority.is_set or
                    self.cnsinpsrcqualitylevel.is_set or
                    self.cnsinpsrcqualitylevelrx.is_set or
                    self.cnsinpsrcqualitylevelrxcfg.is_set or
                    self.cnsinpsrcqualityleveltx.is_set or
                    self.cnsinpsrcqualityleveltxcfg.is_set or
                    self.cnsinpsrcsignalfailure.is_set or
                    self.cnsinpsrcssmcap.is_set or
                    self.cnsinpsrcwtrtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnsinpsrcnetsyncindex.yfilter != YFilter.not_set or
                    self.cnsinpsrcalarm.yfilter != YFilter.not_set or
                    self.cnsinpsrcalarminfo.yfilter != YFilter.not_set or
                    self.cnsinpsrcesmccap.yfilter != YFilter.not_set or
                    self.cnsinpsrcfsw.yfilter != YFilter.not_set or
                    self.cnsinpsrcholdofftime.yfilter != YFilter.not_set or
                    self.cnsinpsrcintftype.yfilter != YFilter.not_set or
                    self.cnsinpsrclockout.yfilter != YFilter.not_set or
                    self.cnsinpsrcmsw.yfilter != YFilter.not_set or
                    self.cnsinpsrcname.yfilter != YFilter.not_set or
                    self.cnsinpsrcpriority.yfilter != YFilter.not_set or
                    self.cnsinpsrcqualitylevel.yfilter != YFilter.not_set or
                    self.cnsinpsrcqualitylevelrx.yfilter != YFilter.not_set or
                    self.cnsinpsrcqualitylevelrxcfg.yfilter != YFilter.not_set or
                    self.cnsinpsrcqualityleveltx.yfilter != YFilter.not_set or
                    self.cnsinpsrcqualityleveltxcfg.yfilter != YFilter.not_set or
                    self.cnsinpsrcsignalfailure.yfilter != YFilter.not_set or
                    self.cnsinpsrcssmcap.yfilter != YFilter.not_set or
                    self.cnsinpsrcwtrtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnsInputSourceEntry" + "[cnsInpSrcNetsyncIndex='" + self.cnsinpsrcnetsyncindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsInputSourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnsinpsrcnetsyncindex.is_set or self.cnsinpsrcnetsyncindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcnetsyncindex.get_name_leafdata())
                if (self.cnsinpsrcalarm.is_set or self.cnsinpsrcalarm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcalarm.get_name_leafdata())
                if (self.cnsinpsrcalarminfo.is_set or self.cnsinpsrcalarminfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcalarminfo.get_name_leafdata())
                if (self.cnsinpsrcesmccap.is_set or self.cnsinpsrcesmccap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcesmccap.get_name_leafdata())
                if (self.cnsinpsrcfsw.is_set or self.cnsinpsrcfsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcfsw.get_name_leafdata())
                if (self.cnsinpsrcholdofftime.is_set or self.cnsinpsrcholdofftime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcholdofftime.get_name_leafdata())
                if (self.cnsinpsrcintftype.is_set or self.cnsinpsrcintftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcintftype.get_name_leafdata())
                if (self.cnsinpsrclockout.is_set or self.cnsinpsrclockout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrclockout.get_name_leafdata())
                if (self.cnsinpsrcmsw.is_set or self.cnsinpsrcmsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcmsw.get_name_leafdata())
                if (self.cnsinpsrcname.is_set or self.cnsinpsrcname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcname.get_name_leafdata())
                if (self.cnsinpsrcpriority.is_set or self.cnsinpsrcpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcpriority.get_name_leafdata())
                if (self.cnsinpsrcqualitylevel.is_set or self.cnsinpsrcqualitylevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcqualitylevel.get_name_leafdata())
                if (self.cnsinpsrcqualitylevelrx.is_set or self.cnsinpsrcqualitylevelrx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcqualitylevelrx.get_name_leafdata())
                if (self.cnsinpsrcqualitylevelrxcfg.is_set or self.cnsinpsrcqualitylevelrxcfg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcqualitylevelrxcfg.get_name_leafdata())
                if (self.cnsinpsrcqualityleveltx.is_set or self.cnsinpsrcqualityleveltx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcqualityleveltx.get_name_leafdata())
                if (self.cnsinpsrcqualityleveltxcfg.is_set or self.cnsinpsrcqualityleveltxcfg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcqualityleveltxcfg.get_name_leafdata())
                if (self.cnsinpsrcsignalfailure.is_set or self.cnsinpsrcsignalfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcsignalfailure.get_name_leafdata())
                if (self.cnsinpsrcssmcap.is_set or self.cnsinpsrcssmcap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcssmcap.get_name_leafdata())
                if (self.cnsinpsrcwtrtime.is_set or self.cnsinpsrcwtrtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsinpsrcwtrtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnsInpSrcNetsyncIndex" or name == "cnsInpSrcAlarm" or name == "cnsInpSrcAlarmInfo" or name == "cnsInpSrcESMCCap" or name == "cnsInpSrcFSW" or name == "cnsInpSrcHoldoffTime" or name == "cnsInpSrcIntfType" or name == "cnsInpSrcLockout" or name == "cnsInpSrcMSW" or name == "cnsInpSrcName" or name == "cnsInpSrcPriority" or name == "cnsInpSrcQualityLevel" or name == "cnsInpSrcQualityLevelRx" or name == "cnsInpSrcQualityLevelRxCfg" or name == "cnsInpSrcQualityLevelTx" or name == "cnsInpSrcQualityLevelTxCfg" or name == "cnsInpSrcSignalFailure" or name == "cnsInpSrcSSMCap" or name == "cnsInpSrcWtrTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnsInpSrcNetsyncIndex"):
                    self.cnsinpsrcnetsyncindex = value
                    self.cnsinpsrcnetsyncindex.value_namespace = name_space
                    self.cnsinpsrcnetsyncindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcAlarm"):
                    self.cnsinpsrcalarm = value
                    self.cnsinpsrcalarm.value_namespace = name_space
                    self.cnsinpsrcalarm.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcAlarmInfo"):
                    self.cnsinpsrcalarminfo[value] = True
                if(value_path == "cnsInpSrcESMCCap"):
                    self.cnsinpsrcesmccap = value
                    self.cnsinpsrcesmccap.value_namespace = name_space
                    self.cnsinpsrcesmccap.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcFSW"):
                    self.cnsinpsrcfsw = value
                    self.cnsinpsrcfsw.value_namespace = name_space
                    self.cnsinpsrcfsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcHoldoffTime"):
                    self.cnsinpsrcholdofftime = value
                    self.cnsinpsrcholdofftime.value_namespace = name_space
                    self.cnsinpsrcholdofftime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcIntfType"):
                    self.cnsinpsrcintftype = value
                    self.cnsinpsrcintftype.value_namespace = name_space
                    self.cnsinpsrcintftype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcLockout"):
                    self.cnsinpsrclockout = value
                    self.cnsinpsrclockout.value_namespace = name_space
                    self.cnsinpsrclockout.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcMSW"):
                    self.cnsinpsrcmsw = value
                    self.cnsinpsrcmsw.value_namespace = name_space
                    self.cnsinpsrcmsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcName"):
                    self.cnsinpsrcname = value
                    self.cnsinpsrcname.value_namespace = name_space
                    self.cnsinpsrcname.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcPriority"):
                    self.cnsinpsrcpriority = value
                    self.cnsinpsrcpriority.value_namespace = name_space
                    self.cnsinpsrcpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcQualityLevel"):
                    self.cnsinpsrcqualitylevel = value
                    self.cnsinpsrcqualitylevel.value_namespace = name_space
                    self.cnsinpsrcqualitylevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcQualityLevelRx"):
                    self.cnsinpsrcqualitylevelrx = value
                    self.cnsinpsrcqualitylevelrx.value_namespace = name_space
                    self.cnsinpsrcqualitylevelrx.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcQualityLevelRxCfg"):
                    self.cnsinpsrcqualitylevelrxcfg = value
                    self.cnsinpsrcqualitylevelrxcfg.value_namespace = name_space
                    self.cnsinpsrcqualitylevelrxcfg.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcQualityLevelTx"):
                    self.cnsinpsrcqualityleveltx = value
                    self.cnsinpsrcqualityleveltx.value_namespace = name_space
                    self.cnsinpsrcqualityleveltx.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcQualityLevelTxCfg"):
                    self.cnsinpsrcqualityleveltxcfg = value
                    self.cnsinpsrcqualityleveltxcfg.value_namespace = name_space
                    self.cnsinpsrcqualityleveltxcfg.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcSignalFailure"):
                    self.cnsinpsrcsignalfailure = value
                    self.cnsinpsrcsignalfailure.value_namespace = name_space
                    self.cnsinpsrcsignalfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcSSMCap"):
                    self.cnsinpsrcssmcap = value
                    self.cnsinpsrcssmcap.value_namespace = name_space
                    self.cnsinpsrcssmcap.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsInpSrcWtrTime"):
                    self.cnsinpsrcwtrtime = value
                    self.cnsinpsrcwtrtime.value_namespace = name_space
                    self.cnsinpsrcwtrtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnsinputsourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnsinputsourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnsInputSourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnsInputSourceEntry"):
                for c in self.cnsinputsourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNetsyncMib.Cnsinputsourcetable.Cnsinputsourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnsinputsourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsInputSourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnsextoutputtable(Entity):
        """
        T4 external output table.
        This table contains a list of T4 external outputs.
        
        Each T4 external output is associated with clock
        source(s) to be found in cnsT4ClockSourceTable.
        The clock selection process considers all the
        available clock sources and select the T4 clock
        source based on the G.781 clock selection algorithm.
        
        .. attribute:: cnsextoutputentry
        
        	An entry is created in the table when a user adds a T4 external output in the configuration.  A T4 external output configured input clock sources are defined in cnsT4ClockSourceTable.  An entry is removed from the table when a user removes a T4 external output from the configuration
        	**type**\: list of    :py:class:`Cnsextoutputentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cnsextoutputtable, self).__init__()

            self.yang_name = "cnsExtOutputTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnsextoutputentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cnsextoutputtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cnsextoutputtable, self).__setattr__(name, value)


        class Cnsextoutputentry(Entity):
            """
            An entry is created in the table when a user adds
            a T4 external output in the configuration.  A T4 external
            output configured input clock sources are defined in
            cnsT4ClockSourceTable.
            
            An entry is removed from the table when a user removes
            a T4 external output from the configuration.
            
            .. attribute:: cnsextoutlistindex  <key>
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source, The T4 selected synchronization source is identified by cnsExtOutSelNetsyncIndex, which contains the index to the clock source in cnsT4ClockSourceTable.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\:  bool
            
            .. attribute:: cnsextoutintftype
            
            	This object indicates the interface type of the T4 external output
            	**type**\:   :py:class:`Cisconetsynciftype <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsynciftype>`
            
            .. attribute:: cnsextoutmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies in row in cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'.  The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be  performed only to a source which has the highest available QL
            	**type**\:  bool
            
            .. attribute:: cnsextoutname
            
            	This object indicates the name of a T4 external output
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cnsextoutpriority
            
            	This object indicates the priority of the selected clock source for a T4 external output.  A smaller value represents a higher priority
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnsextoutqualitylevel
            
            	This object indicates the clock quality of the T4 external output
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnsextoutselnetsyncindex
            
            	An index that uniquely represents the selected input clock source whose information is reported by a row in cnsT4ClockSourceTable. The index lists the value of cnsT4ClkSrcNetsyncIndex, which is the input clock source of the T4 external output selected by the G.781 clock selection process
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutsquelch
            
            	This object indicates whether or not a T4 external output is squelched.  Squelching is a sychronization function defined to prevent transmission of a timing signal with a quality that is lower than the quality of the clock in the receiving networks element or SASE. It is also used for the prevention of timing loops
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry, self).__init__()

                self.yang_name = "cnsExtOutputEntry"
                self.yang_parent_name = "cnsExtOutputTable"

                self.cnsextoutlistindex = YLeaf(YType.uint32, "cnsExtOutListIndex")

                self.cnsextoutfsw = YLeaf(YType.boolean, "cnsExtOutFSW")

                self.cnsextoutintftype = YLeaf(YType.enumeration, "cnsExtOutIntfType")

                self.cnsextoutmsw = YLeaf(YType.boolean, "cnsExtOutMSW")

                self.cnsextoutname = YLeaf(YType.str, "cnsExtOutName")

                self.cnsextoutpriority = YLeaf(YType.uint32, "cnsExtOutPriority")

                self.cnsextoutqualitylevel = YLeaf(YType.enumeration, "cnsExtOutQualityLevel")

                self.cnsextoutselnetsyncindex = YLeaf(YType.uint32, "cnsExtOutSelNetsyncIndex")

                self.cnsextoutsquelch = YLeaf(YType.boolean, "cnsExtOutSquelch")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnsextoutlistindex",
                                "cnsextoutfsw",
                                "cnsextoutintftype",
                                "cnsextoutmsw",
                                "cnsextoutname",
                                "cnsextoutpriority",
                                "cnsextoutqualitylevel",
                                "cnsextoutselnetsyncindex",
                                "cnsextoutsquelch") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnsextoutlistindex.is_set or
                    self.cnsextoutfsw.is_set or
                    self.cnsextoutintftype.is_set or
                    self.cnsextoutmsw.is_set or
                    self.cnsextoutname.is_set or
                    self.cnsextoutpriority.is_set or
                    self.cnsextoutqualitylevel.is_set or
                    self.cnsextoutselnetsyncindex.is_set or
                    self.cnsextoutsquelch.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnsextoutlistindex.yfilter != YFilter.not_set or
                    self.cnsextoutfsw.yfilter != YFilter.not_set or
                    self.cnsextoutintftype.yfilter != YFilter.not_set or
                    self.cnsextoutmsw.yfilter != YFilter.not_set or
                    self.cnsextoutname.yfilter != YFilter.not_set or
                    self.cnsextoutpriority.yfilter != YFilter.not_set or
                    self.cnsextoutqualitylevel.yfilter != YFilter.not_set or
                    self.cnsextoutselnetsyncindex.yfilter != YFilter.not_set or
                    self.cnsextoutsquelch.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnsExtOutputEntry" + "[cnsExtOutListIndex='" + self.cnsextoutlistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsExtOutputTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnsextoutlistindex.is_set or self.cnsextoutlistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutlistindex.get_name_leafdata())
                if (self.cnsextoutfsw.is_set or self.cnsextoutfsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutfsw.get_name_leafdata())
                if (self.cnsextoutintftype.is_set or self.cnsextoutintftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutintftype.get_name_leafdata())
                if (self.cnsextoutmsw.is_set or self.cnsextoutmsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutmsw.get_name_leafdata())
                if (self.cnsextoutname.is_set or self.cnsextoutname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutname.get_name_leafdata())
                if (self.cnsextoutpriority.is_set or self.cnsextoutpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutpriority.get_name_leafdata())
                if (self.cnsextoutqualitylevel.is_set or self.cnsextoutqualitylevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutqualitylevel.get_name_leafdata())
                if (self.cnsextoutselnetsyncindex.is_set or self.cnsextoutselnetsyncindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutselnetsyncindex.get_name_leafdata())
                if (self.cnsextoutsquelch.is_set or self.cnsextoutsquelch.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutsquelch.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnsExtOutListIndex" or name == "cnsExtOutFSW" or name == "cnsExtOutIntfType" or name == "cnsExtOutMSW" or name == "cnsExtOutName" or name == "cnsExtOutPriority" or name == "cnsExtOutQualityLevel" or name == "cnsExtOutSelNetsyncIndex" or name == "cnsExtOutSquelch"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnsExtOutListIndex"):
                    self.cnsextoutlistindex = value
                    self.cnsextoutlistindex.value_namespace = name_space
                    self.cnsextoutlistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutFSW"):
                    self.cnsextoutfsw = value
                    self.cnsextoutfsw.value_namespace = name_space
                    self.cnsextoutfsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutIntfType"):
                    self.cnsextoutintftype = value
                    self.cnsextoutintftype.value_namespace = name_space
                    self.cnsextoutintftype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutMSW"):
                    self.cnsextoutmsw = value
                    self.cnsextoutmsw.value_namespace = name_space
                    self.cnsextoutmsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutName"):
                    self.cnsextoutname = value
                    self.cnsextoutname.value_namespace = name_space
                    self.cnsextoutname.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutPriority"):
                    self.cnsextoutpriority = value
                    self.cnsextoutpriority.value_namespace = name_space
                    self.cnsextoutpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutQualityLevel"):
                    self.cnsextoutqualitylevel = value
                    self.cnsextoutqualitylevel.value_namespace = name_space
                    self.cnsextoutqualitylevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutSelNetsyncIndex"):
                    self.cnsextoutselnetsyncindex = value
                    self.cnsextoutselnetsyncindex.value_namespace = name_space
                    self.cnsextoutselnetsyncindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsExtOutSquelch"):
                    self.cnsextoutsquelch = value
                    self.cnsextoutsquelch.value_namespace = name_space
                    self.cnsextoutsquelch.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnsextoutputentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnsextoutputentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnsExtOutputTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnsExtOutputEntry"):
                for c in self.cnsextoutputentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnsextoutputentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsExtOutputEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cnst4Clocksourcetable(Entity):
        """
        T4 clock source table.
        This table contains a list of input sources for a specific
        T4 external output. An entry shall be added to
        cnsExtOutputTable first. Then clock sources shall be
        added in this table for the selection process to select
        the appropriate T4 clock source.
        
        .. attribute:: cnst4clocksourceentry
        
        	An entry is created in the table when a user adds a clock source to a T4 external output in the configuration. The T4 external output is defined in the T4 external output table. An entry is removed in the table when a user removes a T4 clock source from the configuration
        	**type**\: list of    :py:class:`Cnst4Clocksourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnst4Clocksourcetable.Cnst4Clocksourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CiscoNetsyncMib.Cnst4Clocksourcetable, self).__init__()

            self.yang_name = "cnsT4ClockSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"

            self.cnst4clocksourceentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNetsyncMib.Cnst4Clocksourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNetsyncMib.Cnst4Clocksourcetable, self).__setattr__(name, value)


        class Cnst4Clocksourceentry(Entity):
            """
            An entry is created in the table when a user adds a
            clock source to a T4 external output in the configuration.
            The T4 external output is defined in the T4 external
            output table. An entry is removed in the table when a user
            removes a T4 clock source from the configuration.
            
            .. attribute:: cnsextoutlistindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cnsextoutlistindex <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncMib.Cnsextoutputtable.Cnsextoutputentry>`
            
            .. attribute:: cnst4clksrcnetsyncindex  <key>
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnst4clksrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the T4 input clock source
            	**type**\:  bool
            
            .. attribute:: cnst4clksrcalarminfo
            
            	This object indicates the alarm reasons of a T4 input clock source if an alarm event is being reported on the clock source
            	**type**\:   :py:class:`Cisconetsyncalarminfo <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncalarminfo>`
            
            .. attribute:: cnst4clksrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T4 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:   :py:class:`Cisconetsyncesmccap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncesmccap>`
            
            .. attribute:: cnst4clksrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\:  bool
            
            .. attribute:: cnst4clksrcholdofftime
            
            	This object indicates the hold\-off time value of a T4 input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnst4clksrcintftype
            
            	This object indicates the type of an input clock source configured for the T4 clock selection
            	**type**\:   :py:class:`Cisconetsynciftype <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsynciftype>`
            
            .. attribute:: cnst4clksrclockout
            
            	This object indicates whether or not the lockout command has been applied on a T4 clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\:  bool
            
            .. attribute:: cnst4clksrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switching. The switch allows a user to select a  synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in  cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'. The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\:  bool
            
            .. attribute:: cnst4clksrcname
            
            	This object indicates the name of a input clock source configured for the T4 clock selection
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cnst4clksrcpriority
            
            	This object indicates the priority of an input clock source configured for the T4 clock selection.  A smaller value represents a higher priority
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: cnst4clksrcqualitylevel
            
            	This object indicates the current clock quality level of the T4 input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnst4clksrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the T4 input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnst4clksrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of a T4 input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnst4clksrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the T4 input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnst4clksrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of a T4 input clock source
            	**type**\:   :py:class:`Cisconetsyncqualitylevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncqualitylevel>`
            
            .. attribute:: cnst4clksrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the T4 input clock source
            	**type**\:  bool
            
            .. attribute:: cnst4clksrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T4 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:   :py:class:`Cisconetsyncssmcap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.Cisconetsyncssmcap>`
            
            .. attribute:: cnst4clksrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of a T4 input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CiscoNetsyncMib.Cnst4Clocksourcetable.Cnst4Clocksourceentry, self).__init__()

                self.yang_name = "cnsT4ClockSourceEntry"
                self.yang_parent_name = "cnsT4ClockSourceTable"

                self.cnsextoutlistindex = YLeaf(YType.str, "cnsExtOutListIndex")

                self.cnst4clksrcnetsyncindex = YLeaf(YType.uint32, "cnsT4ClkSrcNetsyncIndex")

                self.cnst4clksrcalarm = YLeaf(YType.boolean, "cnsT4ClkSrcAlarm")

                self.cnst4clksrcalarminfo = YLeaf(YType.bits, "cnsT4ClkSrcAlarmInfo")

                self.cnst4clksrcesmccap = YLeaf(YType.enumeration, "cnsT4ClkSrcESMCCap")

                self.cnst4clksrcfsw = YLeaf(YType.boolean, "cnsT4ClkSrcFSW")

                self.cnst4clksrcholdofftime = YLeaf(YType.uint32, "cnsT4ClkSrcHoldoffTime")

                self.cnst4clksrcintftype = YLeaf(YType.enumeration, "cnsT4ClkSrcIntfType")

                self.cnst4clksrclockout = YLeaf(YType.boolean, "cnsT4ClkSrcLockout")

                self.cnst4clksrcmsw = YLeaf(YType.boolean, "cnsT4ClkSrcMSW")

                self.cnst4clksrcname = YLeaf(YType.str, "cnsT4ClkSrcName")

                self.cnst4clksrcpriority = YLeaf(YType.uint32, "cnsT4ClkSrcPriority")

                self.cnst4clksrcqualitylevel = YLeaf(YType.enumeration, "cnsT4ClkSrcQualityLevel")

                self.cnst4clksrcqualitylevelrx = YLeaf(YType.enumeration, "cnsT4ClkSrcQualityLevelRx")

                self.cnst4clksrcqualitylevelrxcfg = YLeaf(YType.enumeration, "cnsT4ClkSrcQualityLevelRxCfg")

                self.cnst4clksrcqualityleveltx = YLeaf(YType.enumeration, "cnsT4ClkSrcQualityLevelTx")

                self.cnst4clksrcqualityleveltxcfg = YLeaf(YType.enumeration, "cnsT4ClkSrcQualityLevelTxCfg")

                self.cnst4clksrcsignalfailure = YLeaf(YType.boolean, "cnsT4ClkSrcSignalFailure")

                self.cnst4clksrcssmcap = YLeaf(YType.enumeration, "cnsT4ClkSrcSSMCap")

                self.cnst4clksrcwtrtime = YLeaf(YType.uint32, "cnsT4ClkSrcWtrTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cnsextoutlistindex",
                                "cnst4clksrcnetsyncindex",
                                "cnst4clksrcalarm",
                                "cnst4clksrcalarminfo",
                                "cnst4clksrcesmccap",
                                "cnst4clksrcfsw",
                                "cnst4clksrcholdofftime",
                                "cnst4clksrcintftype",
                                "cnst4clksrclockout",
                                "cnst4clksrcmsw",
                                "cnst4clksrcname",
                                "cnst4clksrcpriority",
                                "cnst4clksrcqualitylevel",
                                "cnst4clksrcqualitylevelrx",
                                "cnst4clksrcqualitylevelrxcfg",
                                "cnst4clksrcqualityleveltx",
                                "cnst4clksrcqualityleveltxcfg",
                                "cnst4clksrcsignalfailure",
                                "cnst4clksrcssmcap",
                                "cnst4clksrcwtrtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNetsyncMib.Cnst4Clocksourcetable.Cnst4Clocksourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNetsyncMib.Cnst4Clocksourcetable.Cnst4Clocksourceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cnsextoutlistindex.is_set or
                    self.cnst4clksrcnetsyncindex.is_set or
                    self.cnst4clksrcalarm.is_set or
                    self.cnst4clksrcalarminfo.is_set or
                    self.cnst4clksrcesmccap.is_set or
                    self.cnst4clksrcfsw.is_set or
                    self.cnst4clksrcholdofftime.is_set or
                    self.cnst4clksrcintftype.is_set or
                    self.cnst4clksrclockout.is_set or
                    self.cnst4clksrcmsw.is_set or
                    self.cnst4clksrcname.is_set or
                    self.cnst4clksrcpriority.is_set or
                    self.cnst4clksrcqualitylevel.is_set or
                    self.cnst4clksrcqualitylevelrx.is_set or
                    self.cnst4clksrcqualitylevelrxcfg.is_set or
                    self.cnst4clksrcqualityleveltx.is_set or
                    self.cnst4clksrcqualityleveltxcfg.is_set or
                    self.cnst4clksrcsignalfailure.is_set or
                    self.cnst4clksrcssmcap.is_set or
                    self.cnst4clksrcwtrtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cnsextoutlistindex.yfilter != YFilter.not_set or
                    self.cnst4clksrcnetsyncindex.yfilter != YFilter.not_set or
                    self.cnst4clksrcalarm.yfilter != YFilter.not_set or
                    self.cnst4clksrcalarminfo.yfilter != YFilter.not_set or
                    self.cnst4clksrcesmccap.yfilter != YFilter.not_set or
                    self.cnst4clksrcfsw.yfilter != YFilter.not_set or
                    self.cnst4clksrcholdofftime.yfilter != YFilter.not_set or
                    self.cnst4clksrcintftype.yfilter != YFilter.not_set or
                    self.cnst4clksrclockout.yfilter != YFilter.not_set or
                    self.cnst4clksrcmsw.yfilter != YFilter.not_set or
                    self.cnst4clksrcname.yfilter != YFilter.not_set or
                    self.cnst4clksrcpriority.yfilter != YFilter.not_set or
                    self.cnst4clksrcqualitylevel.yfilter != YFilter.not_set or
                    self.cnst4clksrcqualitylevelrx.yfilter != YFilter.not_set or
                    self.cnst4clksrcqualitylevelrxcfg.yfilter != YFilter.not_set or
                    self.cnst4clksrcqualityleveltx.yfilter != YFilter.not_set or
                    self.cnst4clksrcqualityleveltxcfg.yfilter != YFilter.not_set or
                    self.cnst4clksrcsignalfailure.yfilter != YFilter.not_set or
                    self.cnst4clksrcssmcap.yfilter != YFilter.not_set or
                    self.cnst4clksrcwtrtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cnsT4ClockSourceEntry" + "[cnsExtOutListIndex='" + self.cnsextoutlistindex.get() + "']" + "[cnsT4ClkSrcNetsyncIndex='" + self.cnst4clksrcnetsyncindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsT4ClockSourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cnsextoutlistindex.is_set or self.cnsextoutlistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnsextoutlistindex.get_name_leafdata())
                if (self.cnst4clksrcnetsyncindex.is_set or self.cnst4clksrcnetsyncindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcnetsyncindex.get_name_leafdata())
                if (self.cnst4clksrcalarm.is_set or self.cnst4clksrcalarm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcalarm.get_name_leafdata())
                if (self.cnst4clksrcalarminfo.is_set or self.cnst4clksrcalarminfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcalarminfo.get_name_leafdata())
                if (self.cnst4clksrcesmccap.is_set or self.cnst4clksrcesmccap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcesmccap.get_name_leafdata())
                if (self.cnst4clksrcfsw.is_set or self.cnst4clksrcfsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcfsw.get_name_leafdata())
                if (self.cnst4clksrcholdofftime.is_set or self.cnst4clksrcholdofftime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcholdofftime.get_name_leafdata())
                if (self.cnst4clksrcintftype.is_set or self.cnst4clksrcintftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcintftype.get_name_leafdata())
                if (self.cnst4clksrclockout.is_set or self.cnst4clksrclockout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrclockout.get_name_leafdata())
                if (self.cnst4clksrcmsw.is_set or self.cnst4clksrcmsw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcmsw.get_name_leafdata())
                if (self.cnst4clksrcname.is_set or self.cnst4clksrcname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcname.get_name_leafdata())
                if (self.cnst4clksrcpriority.is_set or self.cnst4clksrcpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcpriority.get_name_leafdata())
                if (self.cnst4clksrcqualitylevel.is_set or self.cnst4clksrcqualitylevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcqualitylevel.get_name_leafdata())
                if (self.cnst4clksrcqualitylevelrx.is_set or self.cnst4clksrcqualitylevelrx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcqualitylevelrx.get_name_leafdata())
                if (self.cnst4clksrcqualitylevelrxcfg.is_set or self.cnst4clksrcqualitylevelrxcfg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcqualitylevelrxcfg.get_name_leafdata())
                if (self.cnst4clksrcqualityleveltx.is_set or self.cnst4clksrcqualityleveltx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcqualityleveltx.get_name_leafdata())
                if (self.cnst4clksrcqualityleveltxcfg.is_set or self.cnst4clksrcqualityleveltxcfg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcqualityleveltxcfg.get_name_leafdata())
                if (self.cnst4clksrcsignalfailure.is_set or self.cnst4clksrcsignalfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcsignalfailure.get_name_leafdata())
                if (self.cnst4clksrcssmcap.is_set or self.cnst4clksrcssmcap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcssmcap.get_name_leafdata())
                if (self.cnst4clksrcwtrtime.is_set or self.cnst4clksrcwtrtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cnst4clksrcwtrtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cnsExtOutListIndex" or name == "cnsT4ClkSrcNetsyncIndex" or name == "cnsT4ClkSrcAlarm" or name == "cnsT4ClkSrcAlarmInfo" or name == "cnsT4ClkSrcESMCCap" or name == "cnsT4ClkSrcFSW" or name == "cnsT4ClkSrcHoldoffTime" or name == "cnsT4ClkSrcIntfType" or name == "cnsT4ClkSrcLockout" or name == "cnsT4ClkSrcMSW" or name == "cnsT4ClkSrcName" or name == "cnsT4ClkSrcPriority" or name == "cnsT4ClkSrcQualityLevel" or name == "cnsT4ClkSrcQualityLevelRx" or name == "cnsT4ClkSrcQualityLevelRxCfg" or name == "cnsT4ClkSrcQualityLevelTx" or name == "cnsT4ClkSrcQualityLevelTxCfg" or name == "cnsT4ClkSrcSignalFailure" or name == "cnsT4ClkSrcSSMCap" or name == "cnsT4ClkSrcWtrTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cnsExtOutListIndex"):
                    self.cnsextoutlistindex = value
                    self.cnsextoutlistindex.value_namespace = name_space
                    self.cnsextoutlistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcNetsyncIndex"):
                    self.cnst4clksrcnetsyncindex = value
                    self.cnst4clksrcnetsyncindex.value_namespace = name_space
                    self.cnst4clksrcnetsyncindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcAlarm"):
                    self.cnst4clksrcalarm = value
                    self.cnst4clksrcalarm.value_namespace = name_space
                    self.cnst4clksrcalarm.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcAlarmInfo"):
                    self.cnst4clksrcalarminfo[value] = True
                if(value_path == "cnsT4ClkSrcESMCCap"):
                    self.cnst4clksrcesmccap = value
                    self.cnst4clksrcesmccap.value_namespace = name_space
                    self.cnst4clksrcesmccap.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcFSW"):
                    self.cnst4clksrcfsw = value
                    self.cnst4clksrcfsw.value_namespace = name_space
                    self.cnst4clksrcfsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcHoldoffTime"):
                    self.cnst4clksrcholdofftime = value
                    self.cnst4clksrcholdofftime.value_namespace = name_space
                    self.cnst4clksrcholdofftime.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcIntfType"):
                    self.cnst4clksrcintftype = value
                    self.cnst4clksrcintftype.value_namespace = name_space
                    self.cnst4clksrcintftype.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcLockout"):
                    self.cnst4clksrclockout = value
                    self.cnst4clksrclockout.value_namespace = name_space
                    self.cnst4clksrclockout.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcMSW"):
                    self.cnst4clksrcmsw = value
                    self.cnst4clksrcmsw.value_namespace = name_space
                    self.cnst4clksrcmsw.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcName"):
                    self.cnst4clksrcname = value
                    self.cnst4clksrcname.value_namespace = name_space
                    self.cnst4clksrcname.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcPriority"):
                    self.cnst4clksrcpriority = value
                    self.cnst4clksrcpriority.value_namespace = name_space
                    self.cnst4clksrcpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcQualityLevel"):
                    self.cnst4clksrcqualitylevel = value
                    self.cnst4clksrcqualitylevel.value_namespace = name_space
                    self.cnst4clksrcqualitylevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcQualityLevelRx"):
                    self.cnst4clksrcqualitylevelrx = value
                    self.cnst4clksrcqualitylevelrx.value_namespace = name_space
                    self.cnst4clksrcqualitylevelrx.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcQualityLevelRxCfg"):
                    self.cnst4clksrcqualitylevelrxcfg = value
                    self.cnst4clksrcqualitylevelrxcfg.value_namespace = name_space
                    self.cnst4clksrcqualitylevelrxcfg.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcQualityLevelTx"):
                    self.cnst4clksrcqualityleveltx = value
                    self.cnst4clksrcqualityleveltx.value_namespace = name_space
                    self.cnst4clksrcqualityleveltx.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcQualityLevelTxCfg"):
                    self.cnst4clksrcqualityleveltxcfg = value
                    self.cnst4clksrcqualityleveltxcfg.value_namespace = name_space
                    self.cnst4clksrcqualityleveltxcfg.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcSignalFailure"):
                    self.cnst4clksrcsignalfailure = value
                    self.cnst4clksrcsignalfailure.value_namespace = name_space
                    self.cnst4clksrcsignalfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcSSMCap"):
                    self.cnst4clksrcssmcap = value
                    self.cnst4clksrcssmcap.value_namespace = name_space
                    self.cnst4clksrcssmcap.value_namespace_prefix = name_space_prefix
                if(value_path == "cnsT4ClkSrcWtrTime"):
                    self.cnst4clksrcwtrtime = value
                    self.cnst4clksrcwtrtime.value_namespace = name_space
                    self.cnst4clksrcwtrtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cnst4clocksourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cnst4clocksourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cnsT4ClockSourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cnsT4ClockSourceEntry"):
                for c in self.cnst4clocksourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNetsyncMib.Cnst4Clocksourcetable.Cnst4Clocksourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cnst4clocksourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cnsT4ClockSourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cisconetsyncmibnotifcontrol is not None and self.cisconetsyncmibnotifcontrol.has_data()) or
            (self.cnsclkselglobaltable is not None and self.cnsclkselglobaltable.has_data()) or
            (self.cnsextoutputtable is not None and self.cnsextoutputtable.has_data()) or
            (self.cnsinputsourcetable is not None and self.cnsinputsourcetable.has_data()) or
            (self.cnsselectedinputsourcetable is not None and self.cnsselectedinputsourcetable.has_data()) or
            (self.cnst4clocksourcetable is not None and self.cnst4clocksourcetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cisconetsyncmibnotifcontrol is not None and self.cisconetsyncmibnotifcontrol.has_operation()) or
            (self.cnsclkselglobaltable is not None and self.cnsclkselglobaltable.has_operation()) or
            (self.cnsextoutputtable is not None and self.cnsextoutputtable.has_operation()) or
            (self.cnsinputsourcetable is not None and self.cnsinputsourcetable.has_operation()) or
            (self.cnsselectedinputsourcetable is not None and self.cnsselectedinputsourcetable.has_operation()) or
            (self.cnst4clocksourcetable is not None and self.cnst4clocksourcetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ciscoNetsyncMIBNotifControl"):
            if (self.cisconetsyncmibnotifcontrol is None):
                self.cisconetsyncmibnotifcontrol = CiscoNetsyncMib.Cisconetsyncmibnotifcontrol()
                self.cisconetsyncmibnotifcontrol.parent = self
                self._children_name_map["cisconetsyncmibnotifcontrol"] = "ciscoNetsyncMIBNotifControl"
            return self.cisconetsyncmibnotifcontrol

        if (child_yang_name == "cnsClkSelGlobalTable"):
            if (self.cnsclkselglobaltable is None):
                self.cnsclkselglobaltable = CiscoNetsyncMib.Cnsclkselglobaltable()
                self.cnsclkselglobaltable.parent = self
                self._children_name_map["cnsclkselglobaltable"] = "cnsClkSelGlobalTable"
            return self.cnsclkselglobaltable

        if (child_yang_name == "cnsExtOutputTable"):
            if (self.cnsextoutputtable is None):
                self.cnsextoutputtable = CiscoNetsyncMib.Cnsextoutputtable()
                self.cnsextoutputtable.parent = self
                self._children_name_map["cnsextoutputtable"] = "cnsExtOutputTable"
            return self.cnsextoutputtable

        if (child_yang_name == "cnsInputSourceTable"):
            if (self.cnsinputsourcetable is None):
                self.cnsinputsourcetable = CiscoNetsyncMib.Cnsinputsourcetable()
                self.cnsinputsourcetable.parent = self
                self._children_name_map["cnsinputsourcetable"] = "cnsInputSourceTable"
            return self.cnsinputsourcetable

        if (child_yang_name == "cnsSelectedInputSourceTable"):
            if (self.cnsselectedinputsourcetable is None):
                self.cnsselectedinputsourcetable = CiscoNetsyncMib.Cnsselectedinputsourcetable()
                self.cnsselectedinputsourcetable.parent = self
                self._children_name_map["cnsselectedinputsourcetable"] = "cnsSelectedInputSourceTable"
            return self.cnsselectedinputsourcetable

        if (child_yang_name == "cnsT4ClockSourceTable"):
            if (self.cnst4clocksourcetable is None):
                self.cnst4clocksourcetable = CiscoNetsyncMib.Cnst4Clocksourcetable()
                self.cnst4clocksourcetable.parent = self
                self._children_name_map["cnst4clocksourcetable"] = "cnsT4ClockSourceTable"
            return self.cnst4clocksourcetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoNetsyncMIBNotifControl" or name == "cnsClkSelGlobalTable" or name == "cnsExtOutputTable" or name == "cnsInputSourceTable" or name == "cnsSelectedInputSourceTable" or name == "cnsT4ClockSourceTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoNetsyncMib()
        return self._top_entity

