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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoNetsyncClockMode(Enum):
    """
    CiscoNetsyncClockMode (Enum Class)

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


class CiscoNetsyncEECOption(Enum):
    """
    CiscoNetsyncEECOption (Enum Class)

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


class CiscoNetsyncESMCCap(Enum):
    """
    CiscoNetsyncESMCCap (Enum Class)

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


class CiscoNetsyncIfType(Enum):
    """
    CiscoNetsyncIfType (Enum Class)

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


class CiscoNetsyncNetworkOption(Enum):
    """
    CiscoNetsyncNetworkOption (Enum Class)

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


class CiscoNetsyncQLMode(Enum):
    """
    CiscoNetsyncQLMode (Enum Class)

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


class CiscoNetsyncQualityLevel(Enum):
    """
    CiscoNetsyncQualityLevel (Enum Class)

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


class CiscoNetsyncSSMCap(Enum):
    """
    CiscoNetsyncSSMCap (Enum Class)

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



class CISCONETSYNCMIB(Entity):
    """
    
    
    .. attribute:: cisconetsyncmibnotifcontrol
    
    	
    	**type**\:  :py:class:`Cisconetsyncmibnotifcontrol <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cisconetsyncmibnotifcontrol>`
    
    .. attribute:: cnsclkselglobaltable
    
    	G.781 clock selection process table. This table contains the global parameters for the G.781 clock selection process
    	**type**\:  :py:class:`Cnsclkselglobaltable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsclkselglobaltable>`
    
    .. attribute:: cnsselectedinputsourcetable
    
    	T0 selected clock source table. This table contains the selected clock source for the input T0 clock
    	**type**\:  :py:class:`Cnsselectedinputsourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsselectedinputsourcetable>`
    
    .. attribute:: cnsinputsourcetable
    
    	T0 clock source table. This table contains a list of input sources for input T0 clock selection
    	**type**\:  :py:class:`Cnsinputsourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsinputsourcetable>`
    
    .. attribute:: cnsextoutputtable
    
    	T4 external output table. This table contains a list of T4 external outputs.  Each T4 external output is associated with clock source(s) to be found in cnsT4ClockSourceTable. The clock selection process considers all the available clock sources and select the T4 clock source based on the G.781 clock selection algorithm
    	**type**\:  :py:class:`Cnsextoutputtable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsextoutputtable>`
    
    .. attribute:: cnst4clocksourcetable
    
    	T4 clock source table. This table contains a list of input sources for a specific T4 external output. An entry shall be added to cnsExtOutputTable first. Then clock sources shall be added in this table for the selection process to select the appropriate T4 clock source
    	**type**\:  :py:class:`Cnst4Clocksourcetable <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnst4Clocksourcetable>`
    
    

    """

    _prefix = 'CISCO-NETSYNC-MIB'
    _revision = '2010-10-15'

    def __init__(self):
        super(CISCONETSYNCMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-NETSYNC-MIB"
        self.yang_parent_name = "CISCO-NETSYNC-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoNetsyncMIBNotifControl", ("cisconetsyncmibnotifcontrol", CISCONETSYNCMIB.Cisconetsyncmibnotifcontrol)), ("cnsClkSelGlobalTable", ("cnsclkselglobaltable", CISCONETSYNCMIB.Cnsclkselglobaltable)), ("cnsSelectedInputSourceTable", ("cnsselectedinputsourcetable", CISCONETSYNCMIB.Cnsselectedinputsourcetable)), ("cnsInputSourceTable", ("cnsinputsourcetable", CISCONETSYNCMIB.Cnsinputsourcetable)), ("cnsExtOutputTable", ("cnsextoutputtable", CISCONETSYNCMIB.Cnsextoutputtable)), ("cnsT4ClockSourceTable", ("cnst4clocksourcetable", CISCONETSYNCMIB.Cnst4Clocksourcetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cisconetsyncmibnotifcontrol = CISCONETSYNCMIB.Cisconetsyncmibnotifcontrol()
        self.cisconetsyncmibnotifcontrol.parent = self
        self._children_name_map["cisconetsyncmibnotifcontrol"] = "ciscoNetsyncMIBNotifControl"
        self._children_yang_names.add("ciscoNetsyncMIBNotifControl")

        self.cnsclkselglobaltable = CISCONETSYNCMIB.Cnsclkselglobaltable()
        self.cnsclkselglobaltable.parent = self
        self._children_name_map["cnsclkselglobaltable"] = "cnsClkSelGlobalTable"
        self._children_yang_names.add("cnsClkSelGlobalTable")

        self.cnsselectedinputsourcetable = CISCONETSYNCMIB.Cnsselectedinputsourcetable()
        self.cnsselectedinputsourcetable.parent = self
        self._children_name_map["cnsselectedinputsourcetable"] = "cnsSelectedInputSourceTable"
        self._children_yang_names.add("cnsSelectedInputSourceTable")

        self.cnsinputsourcetable = CISCONETSYNCMIB.Cnsinputsourcetable()
        self.cnsinputsourcetable.parent = self
        self._children_name_map["cnsinputsourcetable"] = "cnsInputSourceTable"
        self._children_yang_names.add("cnsInputSourceTable")

        self.cnsextoutputtable = CISCONETSYNCMIB.Cnsextoutputtable()
        self.cnsextoutputtable.parent = self
        self._children_name_map["cnsextoutputtable"] = "cnsExtOutputTable"
        self._children_yang_names.add("cnsExtOutputTable")

        self.cnst4clocksourcetable = CISCONETSYNCMIB.Cnst4Clocksourcetable()
        self.cnst4clocksourcetable.parent = self
        self._children_name_map["cnst4clocksourcetable"] = "cnsT4ClockSourceTable"
        self._children_yang_names.add("cnsT4ClockSourceTable")
        self._segment_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB"


    class Cisconetsyncmibnotifcontrol(Entity):
        """
        
        
        .. attribute:: cnsmibenablestatusnotification
        
        	A control object to enable/disable ciscoNetsyncSelectedT0Clock, ciscoNetsyncSelectedT4Clock, ciscoNetsyncInputSignalFailureStatus, ciscoNetsyncInputAlarmStatus notifications at the system level. This object should hold any of the below values.     true \- The notif is enabled globally for the system     false\- The notif is disabled globally for the system
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cisconetsyncmibnotifcontrol, self).__init__()

            self.yang_name = "ciscoNetsyncMIBNotifControl"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cnsmibenablestatusnotification', YLeaf(YType.boolean, 'cnsMIBEnableStatusNotification')),
            ])
            self.cnsmibenablestatusnotification = None
            self._segment_path = lambda: "ciscoNetsyncMIBNotifControl"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cisconetsyncmibnotifcontrol, ['cnsmibenablestatusnotification'], name, value)


    class Cnsclkselglobaltable(Entity):
        """
        G.781 clock selection process table.
        This table contains the global parameters for the G.781 clock
        selection process.
        
        .. attribute:: cnsclkselglobalentry
        
        	An entry is added to cnsClkSelGlobalTable when G.781 clock selection is enabled in the device configuration.  The entry is removed when G.781 clock selection is removed from the configuration
        	**type**\: list of  		 :py:class:`Cnsclkselglobalentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsclkselglobaltable.Cnsclkselglobalentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cnsclkselglobaltable, self).__init__()

            self.yang_name = "cnsClkSelGlobalTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cnsClkSelGlobalEntry", ("cnsclkselglobalentry", CISCONETSYNCMIB.Cnsclkselglobaltable.Cnsclkselglobalentry))])
            self._leafs = OrderedDict()

            self.cnsclkselglobalentry = YList(self)
            self._segment_path = lambda: "cnsClkSelGlobalTable"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cnsclkselglobaltable, [], name, value)


        class Cnsclkselglobalentry(Entity):
            """
            An entry is added to cnsClkSelGlobalTable when G.781 clock
            selection is enabled in the device configuration.  The entry
            is removed when G.781 clock selection is removed from the
            configuration.
            
            .. attribute:: cnsclkselgloprocindex  (key)
            
            	An index that uniquely represents a clock selection process.  This index is assigned arbitrarily by the system and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselglobprocessmode
            
            	This object indicates the QL mode of the network synchronization clock selection process as described in ITU\-T standard G.781 section 5.12
            	**type**\:  :py:class:`CiscoNetsyncQLMode <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQLMode>`
            
            .. attribute:: cnsclkselglobclockmode
            
            	This object indicates the operating mode of the system clock
            	**type**\:  :py:class:`CiscoNetsyncClockMode <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncClockMode>`
            
            .. attribute:: cnsclkselglobnetsyncenable
            
            	This object indicates whether the G.781 clock selection is enabled or not.  'true'  \- G.781 clock selection is enabled 'false' \- G.781 clock selection is disabled
            	**type**\: bool
            
            .. attribute:: cnsclkselglobrevertivemode
            
            	This object indicates the revertive mode setting in the G.781 clock selection process.  The switching of clock sources can be made revertive or non\-revertive. In non\-revertive mode, an alternate clock source is maintained even after the original clock source has recovered from the failure that caused the switch. In revertive mode, the clock selection process switches back to the original clock source after recovering from the failure
            	**type**\: bool
            
            .. attribute:: cnsclkselglobesmcmode
            
            	This object indicates if global ESMC is enabled. With ESMC enabled globally, the system is capable of handling ESMC messages
            	**type**\: bool
            
            .. attribute:: cnsclkselglobeecoption
            
            	This object indicates the network synchronization EEC (Ethernet Equipment Clock) option
            	**type**\:  :py:class:`CiscoNetsyncEECOption <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncEECOption>`
            
            .. attribute:: cnsclkselglobnetworkoption
            
            	This object indicates the synchronization network option
            	**type**\:  :py:class:`CiscoNetsyncNetworkOption <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncNetworkOption>`
            
            .. attribute:: cnsclkselglobholdofftime
            
            	This object indicates the global holdoff time in the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnsclkselglobwtrtime
            
            	This object indicates the global wait\-to\-restore time in the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cnsclkselglobnofsources
            
            	This object indicates the number of synchronization sources currently configured for the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: clock sources
            
            .. attribute:: cnsclkselgloblastholdoverseconds
            
            	This object indicates the duration of the last holdover period in seconds. If the holdover duration is less than a second, the object will carry the value zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cnsclkselglobcurrholdoverseconds
            
            	This object indicates the duration of the current holdover period. If a system clock is in holdover mode, the object carries the current holdover duration in seconds. If the system clock is not in holdover, the object carries the value 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CISCONETSYNCMIB.Cnsclkselglobaltable.Cnsclkselglobalentry, self).__init__()

                self.yang_name = "cnsClkSelGlobalEntry"
                self.yang_parent_name = "cnsClkSelGlobalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnsclkselgloprocindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnsclkselgloprocindex', YLeaf(YType.uint32, 'cnsClkSelGloProcIndex')),
                    ('cnsclkselglobprocessmode', YLeaf(YType.enumeration, 'cnsClkSelGlobProcessMode')),
                    ('cnsclkselglobclockmode', YLeaf(YType.enumeration, 'cnsClkSelGlobClockMode')),
                    ('cnsclkselglobnetsyncenable', YLeaf(YType.boolean, 'cnsClkSelGlobNetsyncEnable')),
                    ('cnsclkselglobrevertivemode', YLeaf(YType.boolean, 'cnsClkSelGlobRevertiveMode')),
                    ('cnsclkselglobesmcmode', YLeaf(YType.boolean, 'cnsClkSelGlobESMCMode')),
                    ('cnsclkselglobeecoption', YLeaf(YType.enumeration, 'cnsClkSelGlobEECOption')),
                    ('cnsclkselglobnetworkoption', YLeaf(YType.enumeration, 'cnsClkSelGlobNetworkOption')),
                    ('cnsclkselglobholdofftime', YLeaf(YType.uint32, 'cnsClkSelGlobHoldoffTime')),
                    ('cnsclkselglobwtrtime', YLeaf(YType.uint32, 'cnsClkSelGlobWtrTime')),
                    ('cnsclkselglobnofsources', YLeaf(YType.uint32, 'cnsClkSelGlobNofSources')),
                    ('cnsclkselgloblastholdoverseconds', YLeaf(YType.uint32, 'cnsClkSelGlobLastHoldoverSeconds')),
                    ('cnsclkselglobcurrholdoverseconds', YLeaf(YType.uint32, 'cnsClkSelGlobCurrHoldoverSeconds')),
                ])
                self.cnsclkselgloprocindex = None
                self.cnsclkselglobprocessmode = None
                self.cnsclkselglobclockmode = None
                self.cnsclkselglobnetsyncenable = None
                self.cnsclkselglobrevertivemode = None
                self.cnsclkselglobesmcmode = None
                self.cnsclkselglobeecoption = None
                self.cnsclkselglobnetworkoption = None
                self.cnsclkselglobholdofftime = None
                self.cnsclkselglobwtrtime = None
                self.cnsclkselglobnofsources = None
                self.cnsclkselgloblastholdoverseconds = None
                self.cnsclkselglobcurrholdoverseconds = None
                self._segment_path = lambda: "cnsClkSelGlobalEntry" + "[cnsClkSelGloProcIndex='" + str(self.cnsclkselgloprocindex) + "']"
                self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsClkSelGlobalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONETSYNCMIB.Cnsclkselglobaltable.Cnsclkselglobalentry, ['cnsclkselgloprocindex', 'cnsclkselglobprocessmode', 'cnsclkselglobclockmode', 'cnsclkselglobnetsyncenable', 'cnsclkselglobrevertivemode', 'cnsclkselglobesmcmode', 'cnsclkselglobeecoption', 'cnsclkselglobnetworkoption', 'cnsclkselglobholdofftime', 'cnsclkselglobwtrtime', 'cnsclkselglobnofsources', 'cnsclkselgloblastholdoverseconds', 'cnsclkselglobcurrholdoverseconds'], name, value)


    class Cnsselectedinputsourcetable(Entity):
        """
        T0 selected clock source table.
        This table contains the selected clock source for the input T0
        clock.
        
        .. attribute:: cnsselectedinputsourceentry
        
        	An entry is created in the table when the G.781 clock selection process has successfully selected a T0 clock source.  The entry shall remain during the time the G.781 clock selection process remains enabled
        	**type**\: list of  		 :py:class:`Cnsselectedinputsourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cnsselectedinputsourcetable, self).__init__()

            self.yang_name = "cnsSelectedInputSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cnsSelectedInputSourceEntry", ("cnsselectedinputsourceentry", CISCONETSYNCMIB.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry))])
            self._leafs = OrderedDict()

            self.cnsselectedinputsourceentry = YList(self)
            self._segment_path = lambda: "cnsSelectedInputSourceTable"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cnsselectedinputsourcetable, [], name, value)


        class Cnsselectedinputsourceentry(Entity):
            """
            An entry is created in the table when the G.781 clock
            selection process has successfully selected a T0 clock
            source.  The entry shall remain during the time
            the G.781 clock selection process remains enabled.
            
            .. attribute:: cnsselinpsrcnetsyncindex  (key)
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsselinpsrcname
            
            	This object indicates the name of the selected T0 clock
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cnsselinpsrcintftype
            
            	This object indicates the type of the selected T0 clock
            	**type**\:  :py:class:`CiscoNetsyncIfType <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncIfType>`
            
            .. attribute:: cnsselinpsrcqualitylevel
            
            	This object indicates the selected T0 clock source's effective quality level, which is the derived clock quality based on the three factors\:  (a) Received quality level.  (b) Configured Rx quality level.  This factor supersedes (a).  (c) System overridden quality level as a result of exceptional events such as signal failure or ESMC failure.  This factor supersedes (a) and (b)
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsselinpsrcpriority
            
            	This object indicates the configured priority of the selected T0 clock. A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsselinpsrctimestamp
            
            	This object indicates the timestamp of the T0 clock source being selected by the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsselinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsselinpsrcmsw
            
            	This object indicates the manual switching flag. The 'true' value indicates the currently selected clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode. Furthermore, in QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CISCONETSYNCMIB.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry, self).__init__()

                self.yang_name = "cnsSelectedInputSourceEntry"
                self.yang_parent_name = "cnsSelectedInputSourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnsselinpsrcnetsyncindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnsselinpsrcnetsyncindex', YLeaf(YType.uint32, 'cnsSelInpSrcNetsyncIndex')),
                    ('cnsselinpsrcname', YLeaf(YType.str, 'cnsSelInpSrcName')),
                    ('cnsselinpsrcintftype', YLeaf(YType.enumeration, 'cnsSelInpSrcIntfType')),
                    ('cnsselinpsrcqualitylevel', YLeaf(YType.enumeration, 'cnsSelInpSrcQualityLevel')),
                    ('cnsselinpsrcpriority', YLeaf(YType.uint32, 'cnsSelInpSrcPriority')),
                    ('cnsselinpsrctimestamp', YLeaf(YType.uint32, 'cnsSelInpSrcTimestamp')),
                    ('cnsselinpsrcfsw', YLeaf(YType.boolean, 'cnsSelInpSrcFSW')),
                    ('cnsselinpsrcmsw', YLeaf(YType.boolean, 'cnsSelInpSrcMSW')),
                ])
                self.cnsselinpsrcnetsyncindex = None
                self.cnsselinpsrcname = None
                self.cnsselinpsrcintftype = None
                self.cnsselinpsrcqualitylevel = None
                self.cnsselinpsrcpriority = None
                self.cnsselinpsrctimestamp = None
                self.cnsselinpsrcfsw = None
                self.cnsselinpsrcmsw = None
                self._segment_path = lambda: "cnsSelectedInputSourceEntry" + "[cnsSelInpSrcNetsyncIndex='" + str(self.cnsselinpsrcnetsyncindex) + "']"
                self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsSelectedInputSourceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONETSYNCMIB.Cnsselectedinputsourcetable.Cnsselectedinputsourceentry, ['cnsselinpsrcnetsyncindex', 'cnsselinpsrcname', 'cnsselinpsrcintftype', 'cnsselinpsrcqualitylevel', 'cnsselinpsrcpriority', 'cnsselinpsrctimestamp', 'cnsselinpsrcfsw', 'cnsselinpsrcmsw'], name, value)


    class Cnsinputsourcetable(Entity):
        """
        T0 clock source table.
        This table contains a list of input sources for input T0 clock
        selection.
        
        .. attribute:: cnsinputsourceentry
        
        	An entry is created in the table when a user adds a T0 clock source in the configuration. An entry is removed  in the table when a user removes a T0 clock source from the configuration
        	**type**\: list of  		 :py:class:`Cnsinputsourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsinputsourcetable.Cnsinputsourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cnsinputsourcetable, self).__init__()

            self.yang_name = "cnsInputSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cnsInputSourceEntry", ("cnsinputsourceentry", CISCONETSYNCMIB.Cnsinputsourcetable.Cnsinputsourceentry))])
            self._leafs = OrderedDict()

            self.cnsinputsourceentry = YList(self)
            self._segment_path = lambda: "cnsInputSourceTable"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cnsinputsourcetable, [], name, value)


        class Cnsinputsourceentry(Entity):
            """
            An entry is created in the table when a user adds a T0
            clock source in the configuration. An entry is removed 
            in the table when a user removes a T0 clock source from
            the configuration.
            
            .. attribute:: cnsinpsrcnetsyncindex  (key)
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsinpsrcname
            
            	This object indicates the name of an input clock source configured for the T0 clock selection
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cnsinpsrcintftype
            
            	This object indicates the type of an input clock source configured for the T0 clock selection
            	**type**\:  :py:class:`CiscoNetsyncIfType <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncIfType>`
            
            .. attribute:: cnsinpsrcpriority
            
            	This object indicates the priority of an input clock source configured for the T0 clock selection.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsinpsrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T0 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:  :py:class:`CiscoNetsyncESMCCap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncESMCCap>`
            
            .. attribute:: cnsinpsrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T0 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:  :py:class:`CiscoNetsyncSSMCap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncSSMCap>`
            
            .. attribute:: cnsinpsrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of an input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsinpsrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of an input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsinpsrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsinpsrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsinpsrcqualitylevel
            
            	This object indicates the current clock quality level of the input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsinpsrcholdofftime
            
            	This object indicates the hold\-off time value of an input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnsinpsrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of an input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Seconds
            
            .. attribute:: cnsinpsrclockout
            
            	This object indicates whether or not the lockout command has been applied to a clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\: bool
            
            .. attribute:: cnsinpsrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the input clock source
            	**type**\: bool
            
            .. attribute:: cnsinpsrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the input clock source
            	**type**\: bool
            
            .. attribute:: cnsinpsrcalarminfo
            
            	This object indicates the alarm reasons of an input clock source if an alarm event is being reported on it
            	**type**\:  :py:class:`CiscoNetsyncAlarmInfo <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncAlarmInfo>`
            
            .. attribute:: cnsinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsinpsrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected clock source is a result of the manual switching. The switch allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in cnsInputSourceTable.  A clock source is not locked out when cnsInpSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsInpSrcSignalFailure contains the value 'false'.  The QL is identified in cnsInpSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CISCONETSYNCMIB.Cnsinputsourcetable.Cnsinputsourceentry, self).__init__()

                self.yang_name = "cnsInputSourceEntry"
                self.yang_parent_name = "cnsInputSourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnsinpsrcnetsyncindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnsinpsrcnetsyncindex', YLeaf(YType.uint32, 'cnsInpSrcNetsyncIndex')),
                    ('cnsinpsrcname', YLeaf(YType.str, 'cnsInpSrcName')),
                    ('cnsinpsrcintftype', YLeaf(YType.enumeration, 'cnsInpSrcIntfType')),
                    ('cnsinpsrcpriority', YLeaf(YType.uint32, 'cnsInpSrcPriority')),
                    ('cnsinpsrcesmccap', YLeaf(YType.enumeration, 'cnsInpSrcESMCCap')),
                    ('cnsinpsrcssmcap', YLeaf(YType.enumeration, 'cnsInpSrcSSMCap')),
                    ('cnsinpsrcqualityleveltxcfg', YLeaf(YType.enumeration, 'cnsInpSrcQualityLevelTxCfg')),
                    ('cnsinpsrcqualitylevelrxcfg', YLeaf(YType.enumeration, 'cnsInpSrcQualityLevelRxCfg')),
                    ('cnsinpsrcqualityleveltx', YLeaf(YType.enumeration, 'cnsInpSrcQualityLevelTx')),
                    ('cnsinpsrcqualitylevelrx', YLeaf(YType.enumeration, 'cnsInpSrcQualityLevelRx')),
                    ('cnsinpsrcqualitylevel', YLeaf(YType.enumeration, 'cnsInpSrcQualityLevel')),
                    ('cnsinpsrcholdofftime', YLeaf(YType.uint32, 'cnsInpSrcHoldoffTime')),
                    ('cnsinpsrcwtrtime', YLeaf(YType.uint32, 'cnsInpSrcWtrTime')),
                    ('cnsinpsrclockout', YLeaf(YType.boolean, 'cnsInpSrcLockout')),
                    ('cnsinpsrcsignalfailure', YLeaf(YType.boolean, 'cnsInpSrcSignalFailure')),
                    ('cnsinpsrcalarm', YLeaf(YType.boolean, 'cnsInpSrcAlarm')),
                    ('cnsinpsrcalarminfo', YLeaf(YType.bits, 'cnsInpSrcAlarmInfo')),
                    ('cnsinpsrcfsw', YLeaf(YType.boolean, 'cnsInpSrcFSW')),
                    ('cnsinpsrcmsw', YLeaf(YType.boolean, 'cnsInpSrcMSW')),
                ])
                self.cnsinpsrcnetsyncindex = None
                self.cnsinpsrcname = None
                self.cnsinpsrcintftype = None
                self.cnsinpsrcpriority = None
                self.cnsinpsrcesmccap = None
                self.cnsinpsrcssmcap = None
                self.cnsinpsrcqualityleveltxcfg = None
                self.cnsinpsrcqualitylevelrxcfg = None
                self.cnsinpsrcqualityleveltx = None
                self.cnsinpsrcqualitylevelrx = None
                self.cnsinpsrcqualitylevel = None
                self.cnsinpsrcholdofftime = None
                self.cnsinpsrcwtrtime = None
                self.cnsinpsrclockout = None
                self.cnsinpsrcsignalfailure = None
                self.cnsinpsrcalarm = None
                self.cnsinpsrcalarminfo = Bits()
                self.cnsinpsrcfsw = None
                self.cnsinpsrcmsw = None
                self._segment_path = lambda: "cnsInputSourceEntry" + "[cnsInpSrcNetsyncIndex='" + str(self.cnsinpsrcnetsyncindex) + "']"
                self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsInputSourceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONETSYNCMIB.Cnsinputsourcetable.Cnsinputsourceentry, ['cnsinpsrcnetsyncindex', 'cnsinpsrcname', 'cnsinpsrcintftype', 'cnsinpsrcpriority', 'cnsinpsrcesmccap', 'cnsinpsrcssmcap', 'cnsinpsrcqualityleveltxcfg', 'cnsinpsrcqualitylevelrxcfg', 'cnsinpsrcqualityleveltx', 'cnsinpsrcqualitylevelrx', 'cnsinpsrcqualitylevel', 'cnsinpsrcholdofftime', 'cnsinpsrcwtrtime', 'cnsinpsrclockout', 'cnsinpsrcsignalfailure', 'cnsinpsrcalarm', 'cnsinpsrcalarminfo', 'cnsinpsrcfsw', 'cnsinpsrcmsw'], name, value)


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
        	**type**\: list of  		 :py:class:`Cnsextoutputentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsextoutputtable.Cnsextoutputentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cnsextoutputtable, self).__init__()

            self.yang_name = "cnsExtOutputTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cnsExtOutputEntry", ("cnsextoutputentry", CISCONETSYNCMIB.Cnsextoutputtable.Cnsextoutputentry))])
            self._leafs = OrderedDict()

            self.cnsextoutputentry = YList(self)
            self._segment_path = lambda: "cnsExtOutputTable"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cnsextoutputtable, [], name, value)


        class Cnsextoutputentry(Entity):
            """
            An entry is created in the table when a user adds
            a T4 external output in the configuration.  A T4 external
            output configured input clock sources are defined in
            cnsT4ClockSourceTable.
            
            An entry is removed from the table when a user removes
            a T4 external output from the configuration.
            
            .. attribute:: cnsextoutlistindex  (key)
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutselnetsyncindex
            
            	An index that uniquely represents the selected input clock source whose information is reported by a row in cnsT4ClockSourceTable. The index lists the value of cnsT4ClkSrcNetsyncIndex, which is the input clock source of the T4 external output selected by the G.781 clock selection process
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutname
            
            	This object indicates the name of a T4 external output
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cnsextoutintftype
            
            	This object indicates the interface type of the T4 external output
            	**type**\:  :py:class:`CiscoNetsyncIfType <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncIfType>`
            
            .. attribute:: cnsextoutqualitylevel
            
            	This object indicates the clock quality of the T4 external output
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnsextoutpriority
            
            	This object indicates the priority of the selected clock source for a T4 external output.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsextoutfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source, The T4 selected synchronization source is identified by cnsExtOutSelNetsyncIndex, which contains the index to the clock source in cnsT4ClockSourceTable.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsextoutmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies in row in cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'.  The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be  performed only to a source which has the highest available QL
            	**type**\: bool
            
            .. attribute:: cnsextoutsquelch
            
            	This object indicates whether or not a T4 external output is squelched.  Squelching is a sychronization function defined to prevent transmission of a timing signal with a quality that is lower than the quality of the clock in the receiving networks element or SASE. It is also used for the prevention of timing loops
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CISCONETSYNCMIB.Cnsextoutputtable.Cnsextoutputentry, self).__init__()

                self.yang_name = "cnsExtOutputEntry"
                self.yang_parent_name = "cnsExtOutputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnsextoutlistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnsextoutlistindex', YLeaf(YType.uint32, 'cnsExtOutListIndex')),
                    ('cnsextoutselnetsyncindex', YLeaf(YType.uint32, 'cnsExtOutSelNetsyncIndex')),
                    ('cnsextoutname', YLeaf(YType.str, 'cnsExtOutName')),
                    ('cnsextoutintftype', YLeaf(YType.enumeration, 'cnsExtOutIntfType')),
                    ('cnsextoutqualitylevel', YLeaf(YType.enumeration, 'cnsExtOutQualityLevel')),
                    ('cnsextoutpriority', YLeaf(YType.uint32, 'cnsExtOutPriority')),
                    ('cnsextoutfsw', YLeaf(YType.boolean, 'cnsExtOutFSW')),
                    ('cnsextoutmsw', YLeaf(YType.boolean, 'cnsExtOutMSW')),
                    ('cnsextoutsquelch', YLeaf(YType.boolean, 'cnsExtOutSquelch')),
                ])
                self.cnsextoutlistindex = None
                self.cnsextoutselnetsyncindex = None
                self.cnsextoutname = None
                self.cnsextoutintftype = None
                self.cnsextoutqualitylevel = None
                self.cnsextoutpriority = None
                self.cnsextoutfsw = None
                self.cnsextoutmsw = None
                self.cnsextoutsquelch = None
                self._segment_path = lambda: "cnsExtOutputEntry" + "[cnsExtOutListIndex='" + str(self.cnsextoutlistindex) + "']"
                self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsExtOutputTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONETSYNCMIB.Cnsextoutputtable.Cnsextoutputentry, ['cnsextoutlistindex', 'cnsextoutselnetsyncindex', 'cnsextoutname', 'cnsextoutintftype', 'cnsextoutqualitylevel', 'cnsextoutpriority', 'cnsextoutfsw', 'cnsextoutmsw', 'cnsextoutsquelch'], name, value)


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
        	**type**\: list of  		 :py:class:`Cnst4Clocksourceentry <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnst4Clocksourcetable.Cnst4Clocksourceentry>`
        
        

        """

        _prefix = 'CISCO-NETSYNC-MIB'
        _revision = '2010-10-15'

        def __init__(self):
            super(CISCONETSYNCMIB.Cnst4Clocksourcetable, self).__init__()

            self.yang_name = "cnsT4ClockSourceTable"
            self.yang_parent_name = "CISCO-NETSYNC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cnsT4ClockSourceEntry", ("cnst4clocksourceentry", CISCONETSYNCMIB.Cnst4Clocksourcetable.Cnst4Clocksourceentry))])
            self._leafs = OrderedDict()

            self.cnst4clocksourceentry = YList(self)
            self._segment_path = lambda: "cnsT4ClockSourceTable"
            self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCONETSYNCMIB.Cnst4Clocksourcetable, [], name, value)


        class Cnst4Clocksourceentry(Entity):
            """
            An entry is created in the table when a user adds a
            clock source to a T4 external output in the configuration.
            The T4 external output is defined in the T4 external
            output table. An entry is removed in the table when a user
            removes a T4 clock source from the configuration.
            
            .. attribute:: cnsextoutlistindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cnsextoutlistindex <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.Cnsextoutputtable.Cnsextoutputentry>`
            
            .. attribute:: cnst4clksrcnetsyncindex  (key)
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnst4clksrcname
            
            	This object indicates the name of a input clock source configured for the T4 clock selection
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cnst4clksrcintftype
            
            	This object indicates the type of an input clock source configured for the T4 clock selection
            	**type**\:  :py:class:`CiscoNetsyncIfType <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncIfType>`
            
            .. attribute:: cnst4clksrcpriority
            
            	This object indicates the priority of an input clock source configured for the T4 clock selection.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnst4clksrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T4 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:  :py:class:`CiscoNetsyncESMCCap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncESMCCap>`
            
            .. attribute:: cnst4clksrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T4 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\:  :py:class:`CiscoNetsyncSSMCap <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncSSMCap>`
            
            .. attribute:: cnst4clksrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of a T4 input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnst4clksrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of a T4 input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnst4clksrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the T4 input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnst4clksrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the T4 input clock source
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnst4clksrcqualitylevel
            
            	This object indicates the current clock quality level of the T4 input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\:  :py:class:`CiscoNetsyncQualityLevel <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel>`
            
            .. attribute:: cnst4clksrcholdofftime
            
            	This object indicates the hold\-off time value of a T4 input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cnst4clksrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of a T4 input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cnst4clksrclockout
            
            	This object indicates whether or not the lockout command has been applied on a T4 clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\: bool
            
            .. attribute:: cnst4clksrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the T4 input clock source
            	**type**\: bool
            
            .. attribute:: cnst4clksrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the T4 input clock source
            	**type**\: bool
            
            .. attribute:: cnst4clksrcalarminfo
            
            	This object indicates the alarm reasons of a T4 input clock source if an alarm event is being reported on the clock source
            	**type**\:  :py:class:`CiscoNetsyncAlarmInfo <ydk.models.cisco_ios_xe.CISCO_NETSYNC_MIB.CiscoNetsyncAlarmInfo>`
            
            .. attribute:: cnst4clksrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnst4clksrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switching. The switch allows a user to select a  synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in  cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'. The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-NETSYNC-MIB'
            _revision = '2010-10-15'

            def __init__(self):
                super(CISCONETSYNCMIB.Cnst4Clocksourcetable.Cnst4Clocksourceentry, self).__init__()

                self.yang_name = "cnsT4ClockSourceEntry"
                self.yang_parent_name = "cnsT4ClockSourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cnsextoutlistindex','cnst4clksrcnetsyncindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cnsextoutlistindex', YLeaf(YType.str, 'cnsExtOutListIndex')),
                    ('cnst4clksrcnetsyncindex', YLeaf(YType.uint32, 'cnsT4ClkSrcNetsyncIndex')),
                    ('cnst4clksrcname', YLeaf(YType.str, 'cnsT4ClkSrcName')),
                    ('cnst4clksrcintftype', YLeaf(YType.enumeration, 'cnsT4ClkSrcIntfType')),
                    ('cnst4clksrcpriority', YLeaf(YType.uint32, 'cnsT4ClkSrcPriority')),
                    ('cnst4clksrcesmccap', YLeaf(YType.enumeration, 'cnsT4ClkSrcESMCCap')),
                    ('cnst4clksrcssmcap', YLeaf(YType.enumeration, 'cnsT4ClkSrcSSMCap')),
                    ('cnst4clksrcqualityleveltxcfg', YLeaf(YType.enumeration, 'cnsT4ClkSrcQualityLevelTxCfg')),
                    ('cnst4clksrcqualitylevelrxcfg', YLeaf(YType.enumeration, 'cnsT4ClkSrcQualityLevelRxCfg')),
                    ('cnst4clksrcqualityleveltx', YLeaf(YType.enumeration, 'cnsT4ClkSrcQualityLevelTx')),
                    ('cnst4clksrcqualitylevelrx', YLeaf(YType.enumeration, 'cnsT4ClkSrcQualityLevelRx')),
                    ('cnst4clksrcqualitylevel', YLeaf(YType.enumeration, 'cnsT4ClkSrcQualityLevel')),
                    ('cnst4clksrcholdofftime', YLeaf(YType.uint32, 'cnsT4ClkSrcHoldoffTime')),
                    ('cnst4clksrcwtrtime', YLeaf(YType.uint32, 'cnsT4ClkSrcWtrTime')),
                    ('cnst4clksrclockout', YLeaf(YType.boolean, 'cnsT4ClkSrcLockout')),
                    ('cnst4clksrcsignalfailure', YLeaf(YType.boolean, 'cnsT4ClkSrcSignalFailure')),
                    ('cnst4clksrcalarm', YLeaf(YType.boolean, 'cnsT4ClkSrcAlarm')),
                    ('cnst4clksrcalarminfo', YLeaf(YType.bits, 'cnsT4ClkSrcAlarmInfo')),
                    ('cnst4clksrcfsw', YLeaf(YType.boolean, 'cnsT4ClkSrcFSW')),
                    ('cnst4clksrcmsw', YLeaf(YType.boolean, 'cnsT4ClkSrcMSW')),
                ])
                self.cnsextoutlistindex = None
                self.cnst4clksrcnetsyncindex = None
                self.cnst4clksrcname = None
                self.cnst4clksrcintftype = None
                self.cnst4clksrcpriority = None
                self.cnst4clksrcesmccap = None
                self.cnst4clksrcssmcap = None
                self.cnst4clksrcqualityleveltxcfg = None
                self.cnst4clksrcqualitylevelrxcfg = None
                self.cnst4clksrcqualityleveltx = None
                self.cnst4clksrcqualitylevelrx = None
                self.cnst4clksrcqualitylevel = None
                self.cnst4clksrcholdofftime = None
                self.cnst4clksrcwtrtime = None
                self.cnst4clksrclockout = None
                self.cnst4clksrcsignalfailure = None
                self.cnst4clksrcalarm = None
                self.cnst4clksrcalarminfo = Bits()
                self.cnst4clksrcfsw = None
                self.cnst4clksrcmsw = None
                self._segment_path = lambda: "cnsT4ClockSourceEntry" + "[cnsExtOutListIndex='" + str(self.cnsextoutlistindex) + "']" + "[cnsT4ClkSrcNetsyncIndex='" + str(self.cnst4clksrcnetsyncindex) + "']"
                self._absolute_path = lambda: "CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/cnsT4ClockSourceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCONETSYNCMIB.Cnst4Clocksourcetable.Cnst4Clocksourceentry, ['cnsextoutlistindex', 'cnst4clksrcnetsyncindex', 'cnst4clksrcname', 'cnst4clksrcintftype', 'cnst4clksrcpriority', 'cnst4clksrcesmccap', 'cnst4clksrcssmcap', 'cnst4clksrcqualityleveltxcfg', 'cnst4clksrcqualitylevelrxcfg', 'cnst4clksrcqualityleveltx', 'cnst4clksrcqualitylevelrx', 'cnst4clksrcqualitylevel', 'cnst4clksrcholdofftime', 'cnst4clksrcwtrtime', 'cnst4clksrclockout', 'cnst4clksrcsignalfailure', 'cnst4clksrcalarm', 'cnst4clksrcalarminfo', 'cnst4clksrcfsw', 'cnst4clksrcmsw'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCONETSYNCMIB()
        return self._top_entity

