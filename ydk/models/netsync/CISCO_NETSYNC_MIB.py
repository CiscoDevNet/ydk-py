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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CiscoNetsyncClockMode_Enum(Enum):
    """
    CiscoNetsyncClockMode_Enum

    Clock operating mode\:
    
    netsyncClockModeUnknown  \- system is unable to 
                               determine the operating mode.
    netsyncClockModeFreerun  \- free\-running mode.
    netsyncClockModeHoldover \- holdover mode.
    netsyncClockModeLocked   \- a valid clock source is locked.

    """

    NETSYNCCLOCKMODEUNKNOWN = 1

    NETSYNCCLOCKMODEFREERUN = 2

    NETSYNCCLOCKMODEHOLDOVER = 3

    NETSYNCCLOCKMODELOCKED = 4


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncClockMode_Enum']


class CiscoNetsyncEECOption_Enum(Enum):
    """
    CiscoNetsyncEECOption_Enum

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

    """

    NETSYNCEECOPTIONUNKNOWN = 1

    NETSYNCEECOPTION1 = 2

    NETSYNCEECOPTION2 = 3

    NETSYNCEECOPTIONINVALID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncEECOption_Enum']


class CiscoNetsyncESMCCap_Enum(Enum):
    """
    CiscoNetsyncESMCCap_Enum

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

    """

    NETSYNCESMCCAPNONE = 1

    NETSYNCESMCCAPTXRX = 2

    NETSYNCESMCCAPTX = 3

    NETSYNCESMCCAPRX = 4

    NETSYNCESMCCAPINVALID = 5


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncESMCCap_Enum']


class CiscoNetsyncIfType_Enum(Enum):
    """
    CiscoNetsyncIfType_Enum

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

    """

    NETSYNCIFTYPEUNKNOWN = 1

    NETSYNCIFTYPEINTERNAL = 2

    NETSYNCIFTYPEETHERNET = 3

    NETSYNCIFTYPESONET = 4

    NETSYNCIFTYPETOP = 5

    NETSYNCIFTYPEEXT = 6

    NETSYNCIFTYPECONTROLLER = 7

    NETSYNCIFTYPEGPS = 8

    NETSYNCIFTYPEATM = 9


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncIfType_Enum']


class CiscoNetsyncNetworkOption_Enum(Enum):
    """
    CiscoNetsyncNetworkOption_Enum

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

    """

    NETSYNCNETWORKOPTIONUNKNOWN = 1

    NETSYNCNETWORKOPTION1 = 2

    NETSYNCNETWORKOPTION2GEN1 = 3

    NETSYNCNETWORKOPTION2GEN2 = 4

    NETSYNCNETWORKOPTION3 = 5

    NETSYNCNETWORKOPTIONINVALID = 6


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncNetworkOption_Enum']


class CiscoNetsyncQLMode_Enum(Enum):
    """
    CiscoNetsyncQLMode_Enum

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

    """

    NETSYNCQLMODEUNKNOWN = 1

    NETSYNCQLMODEQLDISABLED = 2

    NETSYNCQLMODEQLENABLED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncQLMode_Enum']


class CiscoNetsyncQualityLevel_Enum(Enum):
    """
    CiscoNetsyncQualityLevel_Enum

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

    """

    NETSYNCQUALITYLEVELNULL = 1

    NETSYNCQUALITYLEVELDNU = 2

    NETSYNCQUALITYLEVELDUS = 3

    NETSYNCQUALITYLEVELFAILED = 4

    NETSYNCQUALITYLEVELINV0 = 5

    NETSYNCQUALITYLEVELINV1 = 6

    NETSYNCQUALITYLEVELINV2 = 7

    NETSYNCQUALITYLEVELINV3 = 8

    NETSYNCQUALITYLEVELINV4 = 9

    NETSYNCQUALITYLEVELINV5 = 10

    NETSYNCQUALITYLEVELINV6 = 11

    NETSYNCQUALITYLEVELINV7 = 12

    NETSYNCQUALITYLEVELINV8 = 13

    NETSYNCQUALITYLEVELINV9 = 14

    NETSYNCQUALITYLEVELINV10 = 15

    NETSYNCQUALITYLEVELINV11 = 16

    NETSYNCQUALITYLEVELINV12 = 17

    NETSYNCQUALITYLEVELINV13 = 18

    NETSYNCQUALITYLEVELINV14 = 19

    NETSYNCQUALITYLEVELINV15 = 20

    NETSYNCQUALITYLEVELNSUPP = 21

    NETSYNCQUALITYLEVELPRC = 22

    NETSYNCQUALITYLEVELPROV = 23

    NETSYNCQUALITYLEVELPRS = 24

    NETSYNCQUALITYLEVELSEC = 25

    NETSYNCQUALITYLEVELSMC = 26

    NETSYNCQUALITYLEVELSSUA = 27

    NETSYNCQUALITYLEVELSSUB = 28

    NETSYNCQUALITYLEVELST2 = 29

    NETSYNCQUALITYLEVELST3 = 30

    NETSYNCQUALITYLEVELST3E = 31

    NETSYNCQUALITYLEVELST4 = 32

    NETSYNCQUALITYLEVELSTU = 33

    NETSYNCQUALITYLEVELTNC = 34

    NETSYNCQUALITYLEVELUNC = 35

    NETSYNCQUALITYLEVELUNK = 36


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncQualityLevel_Enum']


class CiscoNetsyncSSMCap_Enum(Enum):
    """
    CiscoNetsyncSSMCap_Enum

    Network synchronization clock source interface SSM
    (Synchronization Status Message) capability.
    
    SSM Capability         Capability information
    =====================  ======================
    netsyncSSMCapNone      No SSM capability
    netsyncSSMCapTxRx      To transmit and receive SSM
    netsyncSSMCapTx        To transmit SSM only
    netsyncSSMCapRx        To receive SSM only
    netsyncSSMCapInvalid   Capability invalid or unsupported

    """

    NETSYNCSSMCAPNONE = 1

    NETSYNCSSMCAPTXRX = 2

    NETSYNCSSMCAPTX = 3

    NETSYNCSSMCAPRX = 4

    NETSYNCSSMCAPINVALID = 5


    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CiscoNetsyncSSMCap_Enum']


class CiscoNetsyncAlarmInfo_Bits(FixedBitsDict):
    """
    CiscoNetsyncAlarmInfo_Bits

    Input clock source's alarm reasons\:
    
    netsyncSrcAlarmReasonAIS      \- Alarm Indication Signal
    netsyncSrcAlarmReasonOOR      \- Out of range
    netsyncSrcAlarmReasonOIR      \- Online Insertion Removal
    netsyncSrcAlarmReasonInternal \- Internal
    Keys are:- netsyncSrcAlarmReasonInternal , netsyncSrcAlarmReasonOOR , netsyncSrcAlarmReasonOIR , netsyncSrcAlarmReasonAIS

    """

    def __init__(self):
        self._dictionary = { 
            'netsyncSrcAlarmReasonInternal':False,
            'netsyncSrcAlarmReasonOOR':False,
            'netsyncSrcAlarmReasonOIR':False,
            'netsyncSrcAlarmReasonAIS':False,
        }
        self._pos_map = { 
            'netsyncSrcAlarmReasonInternal':3,
            'netsyncSrcAlarmReasonOOR':1,
            'netsyncSrcAlarmReasonOIR':2,
            'netsyncSrcAlarmReasonAIS':0,
        }


class CISCONETSYNCMIB(object):
    """
    
    
    .. attribute:: cisconetsyncmibnotifcontrol
    
    	
    	**type**\: :py:class:`CiscoNetsyncMIBNotifControl <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl>`
    
    .. attribute:: cnsclkselglobaltable
    
    	G.781 clock selection process table. This table contains the global parameters for the G.781 clock selection process
    	**type**\: :py:class:`CnsClkSelGlobalTable <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsClkSelGlobalTable>`
    
    .. attribute:: cnsextoutputtable
    
    	T4 external output table. This table contains a list of T4 external outputs.  Each T4 external output is associated with clock source(s) to be found in cnsT4ClockSourceTable. The clock selection process considers all the available clock sources and select the T4 clock source based on the G.781 clock selection algorithm
    	**type**\: :py:class:`CnsExtOutputTable <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsExtOutputTable>`
    
    .. attribute:: cnsinputsourcetable
    
    	T0 clock source table. This table contains a list of input sources for input T0 clock selection
    	**type**\: :py:class:`CnsInputSourceTable <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsInputSourceTable>`
    
    .. attribute:: cnsselectedinputsourcetable
    
    	T0 selected clock source table. This table contains the selected clock source for the input T0 clock
    	**type**\: :py:class:`CnsSelectedInputSourceTable <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsSelectedInputSourceTable>`
    
    .. attribute:: cnst4clocksourcetable
    
    	T4 clock source table. This table contains a list of input sources for a specific T4 external output. An entry shall be added to cnsExtOutputTable first. Then clock sources shall be added in this table for the selection process to select the appropriate T4 clock source
    	**type**\: :py:class:`CnsT4ClockSourceTable <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsT4ClockSourceTable>`
    
    

    """

    _prefix = 'cisco-netsync'
    _revision = '2010-10-15'

    def __init__(self):
        self.cisconetsyncmibnotifcontrol = CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl()
        self.cisconetsyncmibnotifcontrol.parent = self
        self.cnsclkselglobaltable = CISCONETSYNCMIB.CnsClkSelGlobalTable()
        self.cnsclkselglobaltable.parent = self
        self.cnsextoutputtable = CISCONETSYNCMIB.CnsExtOutputTable()
        self.cnsextoutputtable.parent = self
        self.cnsinputsourcetable = CISCONETSYNCMIB.CnsInputSourceTable()
        self.cnsinputsourcetable.parent = self
        self.cnsselectedinputsourcetable = CISCONETSYNCMIB.CnsSelectedInputSourceTable()
        self.cnsselectedinputsourcetable.parent = self
        self.cnst4clocksourcetable = CISCONETSYNCMIB.CnsT4ClockSourceTable()
        self.cnst4clocksourcetable.parent = self


    class CiscoNetsyncMIBNotifControl(object):
        """
        
        
        .. attribute:: cnsmibenablestatusnotification
        
        	A control object to enable/disable ciscoNetsyncSelectedT0Clock, ciscoNetsyncSelectedT4Clock, ciscoNetsyncInputSignalFailureStatus, ciscoNetsyncInputAlarmStatus notifications at the system level. This object should hold any of the below values.     true \- The notif is enabled globally for the system     false\- The notif is disabled globally for the system
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnsmibenablestatusnotification = None

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:ciscoNetsyncMIBNotifControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnsmibenablestatusnotification is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl']['meta_info']


    class CnsClkSelGlobalTable(object):
        """
        G.781 clock selection process table.
        This table contains the global parameters for the G.781 clock
        selection process.
        
        .. attribute:: cnsclkselglobalentry
        
        	An entry is added to cnsClkSelGlobalTable when G.781 clock selection is enabled in the device configuration.  The entry is removed when G.781 clock selection is removed from the configuration
        	**type**\: list of :py:class:`CnsClkSelGlobalEntry <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry>`
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnsclkselglobalentry = YList()
            self.cnsclkselglobalentry.parent = self
            self.cnsclkselglobalentry.name = 'cnsclkselglobalentry'


        class CnsClkSelGlobalEntry(object):
            """
            An entry is added to cnsClkSelGlobalTable when G.781 clock
            selection is enabled in the device configuration.  The entry
            is removed when G.781 clock selection is removed from the
            configuration.
            
            .. attribute:: cnsclkselgloprocindex
            
            	An index that uniquely represents a clock selection process.  This index is assigned arbitrarily by the system and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselglobclockmode
            
            	This object indicates the operating mode of the system clock
            	**type**\: :py:class:`CiscoNetsyncClockMode_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncClockMode_Enum>`
            
            .. attribute:: cnsclkselglobcurrholdoverseconds
            
            	This object indicates the duration of the current holdover period. If a system clock is in holdover mode, the object carries the current holdover duration in seconds. If the system clock is not in holdover, the object carries the value 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselglobeecoption
            
            	This object indicates the network synchronization EEC (Ethernet Equipment Clock) option
            	**type**\: :py:class:`CiscoNetsyncEECOption_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncEECOption_Enum>`
            
            .. attribute:: cnsclkselglobesmcmode
            
            	This object indicates if global ESMC is enabled. With ESMC enabled globally, the system is capable of handling ESMC messages
            	**type**\: bool
            
            .. attribute:: cnsclkselglobholdofftime
            
            	This object indicates the global holdoff time in the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselgloblastholdoverseconds
            
            	This object indicates the duration of the last holdover period in seconds. If the holdover duration is less than a second, the object will carry the value zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsclkselglobnetsyncenable
            
            	This object indicates whether the G.781 clock selection is enabled or not.  'true'  \- G.781 clock selection is enabled 'false' \- G.781 clock selection is disabled
            	**type**\: bool
            
            .. attribute:: cnsclkselglobnetworkoption
            
            	This object indicates the synchronization network option
            	**type**\: :py:class:`CiscoNetsyncNetworkOption_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncNetworkOption_Enum>`
            
            .. attribute:: cnsclkselglobnofsources
            
            	This object indicates the number of synchronization sources currently configured for the G.781 clock selection process
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: cnsclkselglobprocessmode
            
            	This object indicates the QL mode of the network synchronization clock selection process as described in ITU\-T standard G.781 section 5.12
            	**type**\: :py:class:`CiscoNetsyncQLMode_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQLMode_Enum>`
            
            .. attribute:: cnsclkselglobrevertivemode
            
            	This object indicates the revertive mode setting in the G.781 clock selection process.  The switching of clock sources can be made revertive or non\-revertive. In non\-revertive mode, an alternate clock source is maintained even after the original clock source has recovered from the failure that caused the switch. In revertive mode, the clock selection process switches back to the original clock source after recovering from the failure
            	**type**\: bool
            
            .. attribute:: cnsclkselglobwtrtime
            
            	This object indicates the global wait\-to\-restore time in the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netsync'
            _revision = '2010-10-15'

            def __init__(self):
                self.parent = None
                self.cnsclkselgloprocindex = None
                self.cnsclkselglobclockmode = None
                self.cnsclkselglobcurrholdoverseconds = None
                self.cnsclkselglobeecoption = None
                self.cnsclkselglobesmcmode = None
                self.cnsclkselglobholdofftime = None
                self.cnsclkselgloblastholdoverseconds = None
                self.cnsclkselglobnetsyncenable = None
                self.cnsclkselglobnetworkoption = None
                self.cnsclkselglobnofsources = None
                self.cnsclkselglobprocessmode = None
                self.cnsclkselglobrevertivemode = None
                self.cnsclkselglobwtrtime = None

            @property
            def _common_path(self):
                if self.cnsclkselgloprocindex is None:
                    raise YPYDataValidationError('Key property cnsclkselgloprocindex is None')

                return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsClkSelGlobalTable/CISCO-NETSYNC-MIB:cnsClkSelGlobalEntry[CISCO-NETSYNC-MIB:cnsClkSelGloProcIndex = ' + str(self.cnsclkselgloprocindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnsclkselgloprocindex is not None:
                    return True

                if self.cnsclkselglobclockmode is not None:
                    return True

                if self.cnsclkselglobcurrholdoverseconds is not None:
                    return True

                if self.cnsclkselglobeecoption is not None:
                    return True

                if self.cnsclkselglobesmcmode is not None:
                    return True

                if self.cnsclkselglobholdofftime is not None:
                    return True

                if self.cnsclkselgloblastholdoverseconds is not None:
                    return True

                if self.cnsclkselglobnetsyncenable is not None:
                    return True

                if self.cnsclkselglobnetworkoption is not None:
                    return True

                if self.cnsclkselglobnofsources is not None:
                    return True

                if self.cnsclkselglobprocessmode is not None:
                    return True

                if self.cnsclkselglobrevertivemode is not None:
                    return True

                if self.cnsclkselglobwtrtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
                return meta._meta_table['CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsClkSelGlobalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnsclkselglobalentry is not None:
                for child_ref in self.cnsclkselglobalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CnsClkSelGlobalTable']['meta_info']


    class CnsExtOutputTable(object):
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
        	**type**\: list of :py:class:`CnsExtOutputEntry <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry>`
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnsextoutputentry = YList()
            self.cnsextoutputentry.parent = self
            self.cnsextoutputentry.name = 'cnsextoutputentry'


        class CnsExtOutputEntry(object):
            """
            An entry is created in the table when a user adds
            a T4 external output in the configuration.  A T4 external
            output configured input clock sources are defined in
            cnsT4ClockSourceTable.
            
            An entry is removed from the table when a user removes
            a T4 external output from the configuration.
            
            .. attribute:: cnsextoutlistindex
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source, The T4 selected synchronization source is identified by cnsExtOutSelNetsyncIndex, which contains the index to the clock source in cnsT4ClockSourceTable.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsextoutintftype
            
            	This object indicates the interface type of the T4 external output
            	**type**\: :py:class:`CiscoNetsyncIfType_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncIfType_Enum>`
            
            .. attribute:: cnsextoutmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies in row in cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'.  The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be  performed only to a source which has the highest available QL
            	**type**\: bool
            
            .. attribute:: cnsextoutname
            
            	This object indicates the name of a T4 external output
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cnsextoutpriority
            
            	This object indicates the priority of the selected clock source for a T4 external output.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsextoutqualitylevel
            
            	This object indicates the clock quality of the T4 external output
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsextoutselnetsyncindex
            
            	An index that uniquely represents the selected input clock source whose information is reported by a row in cnsT4ClockSourceTable. The index lists the value of cnsT4ClkSrcNetsyncIndex, which is the input clock source of the T4 external output selected by the G.781 clock selection process
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsextoutsquelch
            
            	This object indicates whether or not a T4 external output is squelched.  Squelching is a sychronization function defined to prevent transmission of a timing signal with a quality that is lower than the quality of the clock in the receiving networks element or SASE. It is also used for the prevention of timing loops
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-netsync'
            _revision = '2010-10-15'

            def __init__(self):
                self.parent = None
                self.cnsextoutlistindex = None
                self.cnsextoutfsw = None
                self.cnsextoutintftype = None
                self.cnsextoutmsw = None
                self.cnsextoutname = None
                self.cnsextoutpriority = None
                self.cnsextoutqualitylevel = None
                self.cnsextoutselnetsyncindex = None
                self.cnsextoutsquelch = None

            @property
            def _common_path(self):
                if self.cnsextoutlistindex is None:
                    raise YPYDataValidationError('Key property cnsextoutlistindex is None')

                return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsExtOutputTable/CISCO-NETSYNC-MIB:cnsExtOutputEntry[CISCO-NETSYNC-MIB:cnsExtOutListIndex = ' + str(self.cnsextoutlistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnsextoutlistindex is not None:
                    return True

                if self.cnsextoutfsw is not None:
                    return True

                if self.cnsextoutintftype is not None:
                    return True

                if self.cnsextoutmsw is not None:
                    return True

                if self.cnsextoutname is not None:
                    return True

                if self.cnsextoutpriority is not None:
                    return True

                if self.cnsextoutqualitylevel is not None:
                    return True

                if self.cnsextoutselnetsyncindex is not None:
                    return True

                if self.cnsextoutsquelch is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
                return meta._meta_table['CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsExtOutputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnsextoutputentry is not None:
                for child_ref in self.cnsextoutputentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CnsExtOutputTable']['meta_info']


    class CnsInputSourceTable(object):
        """
        T0 clock source table.
        This table contains a list of input sources for input T0 clock
        selection.
        
        .. attribute:: cnsinputsourceentry
        
        	An entry is created in the table when a user adds a T0 clock source in the configuration. An entry is removed  in the table when a user removes a T0 clock source from the configuration
        	**type**\: list of :py:class:`CnsInputSourceEntry <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry>`
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnsinputsourceentry = YList()
            self.cnsinputsourceentry.parent = self
            self.cnsinputsourceentry.name = 'cnsinputsourceentry'


        class CnsInputSourceEntry(object):
            """
            An entry is created in the table when a user adds a T0
            clock source in the configuration. An entry is removed 
            in the table when a user removes a T0 clock source from
            the configuration.
            
            .. attribute:: cnsinpsrcnetsyncindex
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsinpsrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the input clock source
            	**type**\: bool
            
            .. attribute:: cnsinpsrcalarminfo
            
            	This object indicates the alarm reasons of an input clock source if an alarm event is being reported on it
            	**type**\: :py:class:`CiscoNetsyncAlarmInfo_Bits <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncAlarmInfo_Bits>`
            
            .. attribute:: cnsinpsrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T0 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\: :py:class:`CiscoNetsyncESMCCap_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncESMCCap_Enum>`
            
            .. attribute:: cnsinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsinpsrcholdofftime
            
            	This object indicates the hold\-off time value of an input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnsinpsrcintftype
            
            	This object indicates the type of an input clock source configured for the T0 clock selection
            	**type**\: :py:class:`CiscoNetsyncIfType_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncIfType_Enum>`
            
            .. attribute:: cnsinpsrclockout
            
            	This object indicates whether or not the lockout command has been applied to a clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\: bool
            
            .. attribute:: cnsinpsrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected clock source is a result of the manual switching. The switch allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in cnsInputSourceTable.  A clock source is not locked out when cnsInpSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsInpSrcSignalFailure contains the value 'false'.  The QL is identified in cnsInpSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            .. attribute:: cnsinpsrcname
            
            	This object indicates the name of an input clock source configured for the T0 clock selection
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cnsinpsrcpriority
            
            	This object indicates the priority of an input clock source configured for the T0 clock selection.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsinpsrcqualitylevel
            
            	This object indicates the current clock quality level of the input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsinpsrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsinpsrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of an input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsinpsrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsinpsrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of an input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsinpsrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the input clock source
            	**type**\: bool
            
            .. attribute:: cnsinpsrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T0 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsInpSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\: :py:class:`CiscoNetsyncSSMCap_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncSSMCap_Enum>`
            
            .. attribute:: cnsinpsrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of an input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netsync'
            _revision = '2010-10-15'

            def __init__(self):
                self.parent = None
                self.cnsinpsrcnetsyncindex = None
                self.cnsinpsrcalarm = None
                self.cnsinpsrcalarminfo = CiscoNetsyncAlarmInfo_Bits()
                self.cnsinpsrcesmccap = None
                self.cnsinpsrcfsw = None
                self.cnsinpsrcholdofftime = None
                self.cnsinpsrcintftype = None
                self.cnsinpsrclockout = None
                self.cnsinpsrcmsw = None
                self.cnsinpsrcname = None
                self.cnsinpsrcpriority = None
                self.cnsinpsrcqualitylevel = None
                self.cnsinpsrcqualitylevelrx = None
                self.cnsinpsrcqualitylevelrxcfg = None
                self.cnsinpsrcqualityleveltx = None
                self.cnsinpsrcqualityleveltxcfg = None
                self.cnsinpsrcsignalfailure = None
                self.cnsinpsrcssmcap = None
                self.cnsinpsrcwtrtime = None

            @property
            def _common_path(self):
                if self.cnsinpsrcnetsyncindex is None:
                    raise YPYDataValidationError('Key property cnsinpsrcnetsyncindex is None')

                return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsInputSourceTable/CISCO-NETSYNC-MIB:cnsInputSourceEntry[CISCO-NETSYNC-MIB:cnsInpSrcNetsyncIndex = ' + str(self.cnsinpsrcnetsyncindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnsinpsrcnetsyncindex is not None:
                    return True

                if self.cnsinpsrcalarm is not None:
                    return True

                if self.cnsinpsrcalarminfo is not None:
                    if self.cnsinpsrcalarminfo._has_data():
                        return True

                if self.cnsinpsrcesmccap is not None:
                    return True

                if self.cnsinpsrcfsw is not None:
                    return True

                if self.cnsinpsrcholdofftime is not None:
                    return True

                if self.cnsinpsrcintftype is not None:
                    return True

                if self.cnsinpsrclockout is not None:
                    return True

                if self.cnsinpsrcmsw is not None:
                    return True

                if self.cnsinpsrcname is not None:
                    return True

                if self.cnsinpsrcpriority is not None:
                    return True

                if self.cnsinpsrcqualitylevel is not None:
                    return True

                if self.cnsinpsrcqualitylevelrx is not None:
                    return True

                if self.cnsinpsrcqualitylevelrxcfg is not None:
                    return True

                if self.cnsinpsrcqualityleveltx is not None:
                    return True

                if self.cnsinpsrcqualityleveltxcfg is not None:
                    return True

                if self.cnsinpsrcsignalfailure is not None:
                    return True

                if self.cnsinpsrcssmcap is not None:
                    return True

                if self.cnsinpsrcwtrtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
                return meta._meta_table['CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsInputSourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnsinputsourceentry is not None:
                for child_ref in self.cnsinputsourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CnsInputSourceTable']['meta_info']


    class CnsSelectedInputSourceTable(object):
        """
        T0 selected clock source table.
        This table contains the selected clock source for the input T0
        clock.
        
        .. attribute:: cnsselectedinputsourceentry
        
        	An entry is created in the table when the G.781 clock selection process has successfully selected a T0 clock source.  The entry shall remain during the time the G.781 clock selection process remains enabled
        	**type**\: list of :py:class:`CnsSelectedInputSourceEntry <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry>`
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnsselectedinputsourceentry = YList()
            self.cnsselectedinputsourceentry.parent = self
            self.cnsselectedinputsourceentry.name = 'cnsselectedinputsourceentry'


        class CnsSelectedInputSourceEntry(object):
            """
            An entry is created in the table when the G.781 clock
            selection process has successfully selected a T0 clock
            source.  The entry shall remain during the time
            the G.781 clock selection process remains enabled.
            
            .. attribute:: cnsselinpsrcnetsyncindex
            
            	An index that uniquely represents an entry in this table. This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnsselinpsrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected clock source is a result of the forced switching. The 'false' value indicates the currently selected clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnsselinpsrcintftype
            
            	This object indicates the type of the selected T0 clock
            	**type**\: :py:class:`CiscoNetsyncIfType_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncIfType_Enum>`
            
            .. attribute:: cnsselinpsrcmsw
            
            	This object indicates the manual switching flag. The 'true' value indicates the currently selected clock source is a result of the manual switch command. The command allows a user to select a synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode. Furthermore, in QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            .. attribute:: cnsselinpsrcname
            
            	This object indicates the name of the selected T0 clock
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cnsselinpsrcpriority
            
            	This object indicates the configured priority of the selected T0 clock. A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnsselinpsrcqualitylevel
            
            	This object indicates the selected T0 clock source's effective quality level, which is the derived clock quality based on the three factors\:  (a) Received quality level.  (b) Configured Rx quality level.  This factor supersedes (a).  (c) System overridden quality level as a result of exceptional events such as signal failure or ESMC failure.  This factor supersedes (a) and (b)
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnsselinpsrctimestamp
            
            	This object indicates the timestamp of the T0 clock source being selected by the G.781 clock selection process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netsync'
            _revision = '2010-10-15'

            def __init__(self):
                self.parent = None
                self.cnsselinpsrcnetsyncindex = None
                self.cnsselinpsrcfsw = None
                self.cnsselinpsrcintftype = None
                self.cnsselinpsrcmsw = None
                self.cnsselinpsrcname = None
                self.cnsselinpsrcpriority = None
                self.cnsselinpsrcqualitylevel = None
                self.cnsselinpsrctimestamp = None

            @property
            def _common_path(self):
                if self.cnsselinpsrcnetsyncindex is None:
                    raise YPYDataValidationError('Key property cnsselinpsrcnetsyncindex is None')

                return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsSelectedInputSourceTable/CISCO-NETSYNC-MIB:cnsSelectedInputSourceEntry[CISCO-NETSYNC-MIB:cnsSelInpSrcNetsyncIndex = ' + str(self.cnsselinpsrcnetsyncindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnsselinpsrcnetsyncindex is not None:
                    return True

                if self.cnsselinpsrcfsw is not None:
                    return True

                if self.cnsselinpsrcintftype is not None:
                    return True

                if self.cnsselinpsrcmsw is not None:
                    return True

                if self.cnsselinpsrcname is not None:
                    return True

                if self.cnsselinpsrcpriority is not None:
                    return True

                if self.cnsselinpsrcqualitylevel is not None:
                    return True

                if self.cnsselinpsrctimestamp is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
                return meta._meta_table['CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsSelectedInputSourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnsselectedinputsourceentry is not None:
                for child_ref in self.cnsselectedinputsourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CnsSelectedInputSourceTable']['meta_info']


    class CnsT4ClockSourceTable(object):
        """
        T4 clock source table.
        This table contains a list of input sources for a specific
        T4 external output. An entry shall be added to
        cnsExtOutputTable first. Then clock sources shall be
        added in this table for the selection process to select
        the appropriate T4 clock source.
        
        .. attribute:: cnst4clocksourceentry
        
        	An entry is created in the table when a user adds a clock source to a T4 external output in the configuration. The T4 external output is defined in the T4 external output table. An entry is removed in the table when a user removes a T4 clock source from the configuration
        	**type**\: list of :py:class:`CnsT4ClockSourceEntry <ydk.models.netsync.CISCO_NETSYNC_MIB.CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry>`
        
        

        """

        _prefix = 'cisco-netsync'
        _revision = '2010-10-15'

        def __init__(self):
            self.parent = None
            self.cnst4clocksourceentry = YList()
            self.cnst4clocksourceentry.parent = self
            self.cnst4clocksourceentry.name = 'cnst4clocksourceentry'


        class CnsT4ClockSourceEntry(object):
            """
            An entry is created in the table when a user adds a
            clock source to a T4 external output in the configuration.
            The T4 external output is defined in the T4 external
            output table. An entry is removed in the table when a user
            removes a T4 clock source from the configuration.
            
            .. attribute:: cnsextoutlistindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnst4clksrcnetsyncindex
            
            	An index that uniquely represents an entry in this table.  This index is assigned arbitrarily by the clock selection process and may not be persistent across reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cnst4clksrcalarm
            
            	This object indicates whether or not an alarm event is currently being reported on the T4 input clock source
            	**type**\: bool
            
            .. attribute:: cnst4clksrcalarminfo
            
            	This object indicates the alarm reasons of a T4 input clock source if an alarm event is being reported on the clock source
            	**type**\: :py:class:`CiscoNetsyncAlarmInfo_Bits <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncAlarmInfo_Bits>`
            
            .. attribute:: cnst4clksrcesmccap
            
            	This object indicates the ESMC capability of an input clock source configured for the T4 clock selection.  This is applicable only to Synchronous Ethernet input clock source identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\: :py:class:`CiscoNetsyncESMCCap_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncESMCCap_Enum>`
            
            .. attribute:: cnst4clksrcfsw
            
            	This object indicates the forced switching flag. Forced switching, as described in G.781, is used to override the currently selected synchronization source.  The 'true' value indicates the currently selected T4 clock source is a result of the forced switching. The 'false' value indicates the currently selected T4 clock source is not a result of forced switching
            	**type**\: bool
            
            .. attribute:: cnst4clksrcholdofftime
            
            	This object indicates the hold\-off time value of a T4 input clock source.  The hold\-off time prevents short activation of signal failure is passed to the selection process.  When a signal failure event is reported on a clock source, it waits the duration of the hold\-off time before declaring signal failure on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnst4clksrcintftype
            
            	This object indicates the type of an input clock source configured for the T4 clock selection
            	**type**\: :py:class:`CiscoNetsyncIfType_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncIfType_Enum>`
            
            .. attribute:: cnst4clksrclockout
            
            	This object indicates whether or not the lockout command has been applied on a T4 clock source.  The 'true' value means the clock source is not considered by the selection process
            	**type**\: bool
            
            .. attribute:: cnst4clksrcmsw
            
            	This object indicates the manual switching flag.  The 'true' value indicates the currently selected T4 clock source is a result of the manual switching. The switch allows a user to select a  synchronization source assuming it is enabled, not locked out, not in signal fail condition, and has a QL better than DNU in QL\-enabled mode.  A clock source is enabled when it occupies a row in  cnsT4ClockSourceTable.  A clock source is not locked out when cnsT4ClkSrcLockout contains the value 'false'. A clock source is not in signal failure condition when cnsT4ClkSrcSignalFailure contains the value 'false'. The QL is identified in cnsT4ClkSrcQualityLevel.  In QL\-enabled mode, a manual switch can be performed only to a source which has the highest available QL
            	**type**\: bool
            
            .. attribute:: cnst4clksrcname
            
            	This object indicates the name of a input clock source configured for the T4 clock selection
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cnst4clksrcpriority
            
            	This object indicates the priority of an input clock source configured for the T4 clock selection.  A smaller value represents a higher priority
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: cnst4clksrcqualitylevel
            
            	This object indicates the current clock quality level of the T4 input clock source.  This is the effective quality which is derived from three values\:  1) most recent clock quality level received, 2) forced clock quality level (entered via configuration) 3) overridden clock quality level as a result of line protocol down, signal failure, or alarms
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnst4clksrcqualitylevelrx
            
            	This object indicates the last clock quality level received on the T4 input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnst4clksrcqualitylevelrxcfg
            
            	This object indicates the configured receive clock quality level of a T4 input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnst4clksrcqualityleveltx
            
            	This object indicates the most recent clock quality level transmitted on the T4 input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnst4clksrcqualityleveltxcfg
            
            	This object indicates the configured transmit clock quality level of a T4 input clock source
            	**type**\: :py:class:`CiscoNetsyncQualityLevel_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncQualityLevel_Enum>`
            
            .. attribute:: cnst4clksrcsignalfailure
            
            	This object indicates whether or not a signal failure event is currently being reported on the T4 input clock source
            	**type**\: bool
            
            .. attribute:: cnst4clksrcssmcap
            
            	This object indicates the SSM capability of an input clock source configured for the T4 clock selection. This is applicable only to any synchronous interface clock source except SyncE interface, which is identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'
            	**type**\: :py:class:`CiscoNetsyncSSMCap_Enum <ydk.models.netsync.CISCO_NETSYNC_MIB.CiscoNetsyncSSMCap_Enum>`
            
            .. attribute:: cnst4clksrcwtrtime
            
            	This object indicates the wait\-to\-restore time value of a T4 input clock source.  The wait\-to\-restore time ensures that a previous failed synchronization source is only again considered as available by the selection process if it is fault\-free for a certain time. When a signal failure condition is cleared on a clock source, it waits the duration of the wait\-to\-restore time before clearing the signal failure status on the clock source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netsync'
            _revision = '2010-10-15'

            def __init__(self):
                self.parent = None
                self.cnsextoutlistindex = None
                self.cnst4clksrcnetsyncindex = None
                self.cnst4clksrcalarm = None
                self.cnst4clksrcalarminfo = CiscoNetsyncAlarmInfo_Bits()
                self.cnst4clksrcesmccap = None
                self.cnst4clksrcfsw = None
                self.cnst4clksrcholdofftime = None
                self.cnst4clksrcintftype = None
                self.cnst4clksrclockout = None
                self.cnst4clksrcmsw = None
                self.cnst4clksrcname = None
                self.cnst4clksrcpriority = None
                self.cnst4clksrcqualitylevel = None
                self.cnst4clksrcqualitylevelrx = None
                self.cnst4clksrcqualitylevelrxcfg = None
                self.cnst4clksrcqualityleveltx = None
                self.cnst4clksrcqualityleveltxcfg = None
                self.cnst4clksrcsignalfailure = None
                self.cnst4clksrcssmcap = None
                self.cnst4clksrcwtrtime = None

            @property
            def _common_path(self):
                if self.cnsextoutlistindex is None:
                    raise YPYDataValidationError('Key property cnsextoutlistindex is None')
                if self.cnst4clksrcnetsyncindex is None:
                    raise YPYDataValidationError('Key property cnst4clksrcnetsyncindex is None')

                return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsT4ClockSourceTable/CISCO-NETSYNC-MIB:cnsT4ClockSourceEntry[CISCO-NETSYNC-MIB:cnsExtOutListIndex = ' + str(self.cnsextoutlistindex) + '][CISCO-NETSYNC-MIB:cnsT4ClkSrcNetsyncIndex = ' + str(self.cnst4clksrcnetsyncindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnsextoutlistindex is not None:
                    return True

                if self.cnst4clksrcnetsyncindex is not None:
                    return True

                if self.cnst4clksrcalarm is not None:
                    return True

                if self.cnst4clksrcalarminfo is not None:
                    if self.cnst4clksrcalarminfo._has_data():
                        return True

                if self.cnst4clksrcesmccap is not None:
                    return True

                if self.cnst4clksrcfsw is not None:
                    return True

                if self.cnst4clksrcholdofftime is not None:
                    return True

                if self.cnst4clksrcintftype is not None:
                    return True

                if self.cnst4clksrclockout is not None:
                    return True

                if self.cnst4clksrcmsw is not None:
                    return True

                if self.cnst4clksrcname is not None:
                    return True

                if self.cnst4clksrcpriority is not None:
                    return True

                if self.cnst4clksrcqualitylevel is not None:
                    return True

                if self.cnst4clksrcqualitylevelrx is not None:
                    return True

                if self.cnst4clksrcqualitylevelrxcfg is not None:
                    return True

                if self.cnst4clksrcqualityleveltx is not None:
                    return True

                if self.cnst4clksrcqualityleveltxcfg is not None:
                    return True

                if self.cnst4clksrcsignalfailure is not None:
                    return True

                if self.cnst4clksrcssmcap is not None:
                    return True

                if self.cnst4clksrcwtrtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
                return meta._meta_table['CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB/CISCO-NETSYNC-MIB:cnsT4ClockSourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnst4clocksourceentry is not None:
                for child_ref in self.cnst4clocksourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
            return meta._meta_table['CISCONETSYNCMIB.CnsT4ClockSourceTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-NETSYNC-MIB:CISCO-NETSYNC-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cisconetsyncmibnotifcontrol is not None and self.cisconetsyncmibnotifcontrol._has_data():
            return True

        if self.cisconetsyncmibnotifcontrol is not None and self.cisconetsyncmibnotifcontrol.is_presence():
            return True

        if self.cnsclkselglobaltable is not None and self.cnsclkselglobaltable._has_data():
            return True

        if self.cnsclkselglobaltable is not None and self.cnsclkselglobaltable.is_presence():
            return True

        if self.cnsextoutputtable is not None and self.cnsextoutputtable._has_data():
            return True

        if self.cnsextoutputtable is not None and self.cnsextoutputtable.is_presence():
            return True

        if self.cnsinputsourcetable is not None and self.cnsinputsourcetable._has_data():
            return True

        if self.cnsinputsourcetable is not None and self.cnsinputsourcetable.is_presence():
            return True

        if self.cnsselectedinputsourcetable is not None and self.cnsselectedinputsourcetable._has_data():
            return True

        if self.cnsselectedinputsourcetable is not None and self.cnsselectedinputsourcetable.is_presence():
            return True

        if self.cnst4clocksourcetable is not None and self.cnst4clocksourcetable._has_data():
            return True

        if self.cnst4clocksourcetable is not None and self.cnst4clocksourcetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.netsync._meta import _CISCO_NETSYNC_MIB as meta
        return meta._meta_table['CISCONETSYNCMIB']['meta_info']


