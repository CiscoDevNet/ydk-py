""" CISCO_SONET_MIB 

The MIB module to describe SONET/SDH interfaces
objects. This is an extension to the standard SONET 
MIB(RFC 2558).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CsApsLineFailureCode_Enum(Enum):
    """
    CsApsLineFailureCode_Enum

    The Sonet APS line failure code \- this is the failure
    encountered by the APS line.
    
        csApsChannelMismatch\:     Transmitted K1 byte and
                                  received K2 byte do not match.
        csApsProtectionByteFail\:  It could mean either K1 byte
                                  with invalid type of switch
                                  request bits was received, or,
                                  priority of received K1 byte
                                  is lower than the transmitted
                                  K1 byte.
        csApsFEProtectionFailure\: Remote end error detected.
        csApsModeMismatch\:        APS architecture mode mismatch.

    """

    CSAPSCHANNELMISMATCH = 1

    CSAPSPROTECTIONBYTEFAIL = 2

    CSAPSFEPROTECTIONFAILURE = 3

    CSAPSMODEMISMATCH = 4


    @staticmethod
    def _meta_info():
        from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CsApsLineFailureCode_Enum']


class CsApsLineSwitchReason_Enum(Enum):
    """
    CsApsLineSwitchReason_Enum

    The reason why APS switch happened. When the working
    line on one end fails, its other end is told to do
    an APS switch. The following options in the increasing
    order of priority indicate what type of switch request
    it is.
    
      csApsRevertive \: Switch back to working line after the
        Wait\-to\-Restore interval is over, and failures are
        cleared. It is the lowest priority.
      csApsManual \: Manual switch causes APS switch unless a
        request of equal or higher priority is in effect.
      csApsSignalDefectLow \: Switch happened because threshold
        for 'csApsSigFaultBER' was exceeded.
      csApsSignalDefectHigh \: Same as above, but higher priority.
      csApsSignalFailureLow \: Switch happened because threshold
        for 'csApsSigDegradeBER' was exceeded.
      csApsSignalFailureHigh \: Same as above, but higher
        priority.
      csApsForceSwitch \: Forced switch forces hardware to switch
        the active line even if the other line (could be
        working line or protection line) is in alarm.
      csApsLockOut \: This is the highest priority switch. This
        will override all other requests.
      csApsNoSwitch \: This is a state when no switch happens.

    """

    CSAPSOTHER = 1

    CSAPSREVERTIVE = 2

    CSAPSMANUAL = 3

    CSAPSSIGNALDEFECTLOW = 4

    CSAPSSIGNALDEFECTHIGH = 5

    CSAPSSIGNALFAILURELOW = 6

    CSAPSSIGNALFAILUREHIGH = 7

    CSAPSFORCESWITCH = 8

    CSAPSLOCKOUT = 9

    CSAPSNOSWITCH = 10


    @staticmethod
    def _meta_info():
        from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CsApsLineSwitchReason_Enum']


class CsApsLineFailureStatus_Bits(FixedBitsDict):
    """
    CsApsLineFailureStatus_Bits

    The indication of the APS line failure status with a bit
    map representing multiple failures. 
    
       noApsLineFailure bit indicates current failure status.
         This bit should be set ONLY if no other bit is set.
    
       csApsChannelMismatchBit is set when the APS line is in
         csApsChannelMismatch.
    
       csApsProtectionByteFailBit is set when the APS line is
         in csApsProtectionByteFail failure code.
    
       csApsFEProtectionFailureBit is set when the APS line is
         in csApsFEProtectionFailure.
    
       csApsModeMismatchBit is set when the APS line is in 
         csApsModeMismatch.
    Keys are:- csApsProtectionByteFailBit , noApsLineFailure , csApsModeMismatchBit , csApsChannelMismatchBit , csApsFEProtectionFailureBit

    """

    def __init__(self):
        self._dictionary = { 
            'csApsProtectionByteFailBit':False,
            'noApsLineFailure':False,
            'csApsModeMismatchBit':False,
            'csApsChannelMismatchBit':False,
            'csApsFEProtectionFailureBit':False,
        }
        self._pos_map = { 
            'csApsProtectionByteFailBit':2,
            'noApsLineFailure':0,
            'csApsModeMismatchBit':4,
            'csApsChannelMismatchBit':1,
            'csApsFEProtectionFailureBit':3,
        }


class CISCOSONETMIB(object):
    """
    
    
    .. attribute:: csapsconfig
    
    	
    	**type**\: :py:class:`CsApsConfig <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfig>`
    
    .. attribute:: csapsconfigtable
    
    	This table contains objects to configure APS  (Automatic Protection Switching) feature in a SONET  Line. APS is the ability to configure a pair of SONET  lines for redundancy so that the hardware will  automatically switch the active line from working line to the protection line or vice versa, within 60ms,  when the active line fails
    	**type**\: :py:class:`CsApsConfigTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable>`
    
    .. attribute:: csau4tug3configtable
    
    	This table contains objects to configure the VC( Virtual Container) related properties of a TUG\-3 within a AU\-4  paths.  This table allows creation of following multiplexing structure\: STM\-1/AU\-4/TUG\-3/TU\-3/DS3 STM\-1/AU\-4/TUG\-3/TU\-3/E3 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-11/DS1 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-12/E1  Three entries are created in this table for a given AU\-4  path when cspSonetPathPayload object is set to one of the  following\:     vt15vc11(4),     vt2vc12(5),     ds3(3),     e3(8),     vtStructured(9)
    	**type**\: :py:class:`CsAu4Tug3ConfigTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsAu4Tug3ConfigTable>`
    
    .. attribute:: csconfigtable
    
    	The SONET/SDH configuration table. This table has objects  for configuring sonet lines
    	**type**\: :py:class:`CsConfigTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable>`
    
    .. attribute:: cslfarendtotaltable
    
    	The SONET/SDH Far End Line Total table. It contains the  cumulative sum of the various statistics for the 24 hour  period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the  line is enabled
    	**type**\: :py:class:`CslFarEndTotalTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CslFarEndTotalTable>`
    
    .. attribute:: csltotaltable
    
    	The SONET/SDH Line Total table. It contains the  cumulative sum of the various statistics for the 24  hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the line is enabled
    	**type**\: :py:class:`CslTotalTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CslTotalTable>`
    
    .. attribute:: csnotifications
    
    	
    	**type**\: :py:class:`CsNotifications <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsNotifications>`
    
    .. attribute:: cspfarendtotaltable
    
    	The SONET/SDH Far End Path Total table. Far End is the  remote end of the line. The table contains the cumulative sum of the various statistics for the 24 hour period  preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\: :py:class:`CspFarEndTotalTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspFarEndTotalTable>`
    
    .. attribute:: csptotaltable
    
    	The SONET/SDH Path Total table. It contains the cumulative  sum of the various statistics for the 24 hour period  preceding the current interval.The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is  enabled
    	**type**\: :py:class:`CspTotalTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspTotalTable>`
    
    .. attribute:: csptracetable
    
    	The SONET/SDH Path Trace table. This table contains objects  for tracing the sonet path
    	**type**\: :py:class:`CspTraceTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspTraceTable>`
    
    .. attribute:: csstatstable
    
    	The SONET/SDH Section statistics table. This table  maintains the number of times the line encountered Loss of Signal(LOS), Loss of frame(LOF), Alarm Indication  signals(AISs), Remote failure indications(RFIs)
    	**type**\: :py:class:`CsStatsTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsStatsTable>`
    
    .. attribute:: csstotaltable
    
    	The SONET/SDH Section Total table. It contains the  cumulative sum of the various statistics for the 24 hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\: :py:class:`CssTotalTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CssTotalTable>`
    
    .. attribute:: csstracetable
    
    	The SONET/SDH Section Trace table. This table contains  objects for tracing the sonet section
    	**type**\: :py:class:`CssTraceTable <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CssTraceTable>`
    
    

    """

    _prefix = 'cisco-sonet'
    _revision = '2003-03-07'

    def __init__(self):
        self.csapsconfig = CISCOSONETMIB.CsApsConfig()
        self.csapsconfig.parent = self
        self.csapsconfigtable = CISCOSONETMIB.CsApsConfigTable()
        self.csapsconfigtable.parent = self
        self.csau4tug3configtable = CISCOSONETMIB.CsAu4Tug3ConfigTable()
        self.csau4tug3configtable.parent = self
        self.csconfigtable = CISCOSONETMIB.CsConfigTable()
        self.csconfigtable.parent = self
        self.cslfarendtotaltable = CISCOSONETMIB.CslFarEndTotalTable()
        self.cslfarendtotaltable.parent = self
        self.csltotaltable = CISCOSONETMIB.CslTotalTable()
        self.csltotaltable.parent = self
        self.csnotifications = CISCOSONETMIB.CsNotifications()
        self.csnotifications.parent = self
        self.cspfarendtotaltable = CISCOSONETMIB.CspFarEndTotalTable()
        self.cspfarendtotaltable.parent = self
        self.csptotaltable = CISCOSONETMIB.CspTotalTable()
        self.csptotaltable.parent = self
        self.csptracetable = CISCOSONETMIB.CspTraceTable()
        self.csptracetable.parent = self
        self.csstatstable = CISCOSONETMIB.CsStatsTable()
        self.csstatstable.parent = self
        self.csstotaltable = CISCOSONETMIB.CssTotalTable()
        self.csstotaltable.parent = self
        self.csstracetable = CISCOSONETMIB.CssTraceTable()
        self.csstracetable.parent = self


    class CsApsConfig(object):
        """
        
        
        .. attribute:: csapslinefailurecode
        
        	The object indicates the APS line failure code. This is the failure encountered by the APS line. Refer to CsApsLineFailureCode TC for failure code definitions. The object is used for notifications
        	**type**\: :py:class:`CsApsLineFailureCode_Enum <ydk.models.sonet.CISCO_SONET_MIB.CsApsLineFailureCode_Enum>`
        
        .. attribute:: csapslineswitchreason
        
        	This object indicates the APS line switch reason. When the working line on one end fails, its other end is told to do an APS switch.  Refer to CsApsLineSwitchReason TC for more information. The object is used for notifications
        	**type**\: :py:class:`CsApsLineSwitchReason_Enum <ydk.models.sonet.CISCO_SONET_MIB.CsApsLineSwitchReason_Enum>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csapslinefailurecode = None
            self.csapslineswitchreason = None

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csApsConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csapslinefailurecode is not None:
                return True

            if self.csapslineswitchreason is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsApsConfig']['meta_info']


    class CsApsConfigTable(object):
        """
        This table contains objects to configure APS 
        (Automatic Protection Switching) feature in a SONET 
        Line. APS is the ability to configure a pair of SONET 
        lines for redundancy so that the hardware will 
        automatically switch the active line from working line
        to the protection line or vice versa, within 60ms, 
        when the active line fails.
        
        .. attribute:: csapsconfigentry
        
        	An entry is created when an APS pair is configured. To create an entry, the following objects must be  specified\: csApsWorkingIndex, csApsProtectionIndex, csApsEnable,   csApsArchMode. The protection line must not be active, i.e, ifAdminStatus must be 'down',  while configuring  APS. An entry is created by setting the value of  'csApsEnable' to csApsEnabled (2) and deleted by  setting it to csApsDisabled (1). Once a line is  configured as working line or protection line, it  remains in that role until APS is disabled on that  sonet line pair. It remains in the  working/protection  role even after the card is reset
        	**type**\: list of :py:class:`CsApsConfigEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csapsconfigentry = YList()
            self.csapsconfigentry.parent = self
            self.csapsconfigentry.name = 'csapsconfigentry'


        class CsApsConfigEntry(object):
            """
            An entry is created when an APS pair is configured.
            To create an entry, the following objects must be 
            specified\:
            csApsWorkingIndex, csApsProtectionIndex, csApsEnable,  
            csApsArchMode. The protection line must not be active,
            i.e, ifAdminStatus must be 'down',  while configuring 
            APS. An entry is created by setting the value of 
            'csApsEnable' to csApsEnabled (2) and deleted by 
            setting it to csApsDisabled (1). Once a line is 
            configured as working line or protection line, it 
            remains in that role until APS is disabled on that 
            sonet line pair. It remains in the  working/protection 
            role even after the card is reset.
            
            .. attribute:: csapsworkingindex
            
            	When a pair of APS lines is configured, one line has to be the working line, which is the primary line, and the other has to be the protection line, which is the backup line. This object refers to the working line in the APS pair. For G.783 AnnexB, this index refers to Working Section 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsactiveline
            
            	This object indicates which line is currently active.  It could be the working line(Section 1 for Annex B), the protection line(Section 2 for Annex B) or none if neither working nor protection line is active.  This object reflects the status of receive direction
            	**type**\: :py:class:`CsApsActiveLine_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsActiveLine_Enum>`
            
            .. attribute:: csapsarchmode
            
            	This object is used to configure APS architecture mode on the working/protection line pairs.   All of the following are supported on single slot.  oneToOne(2) is not  supported across 2 slots,i.e. the   working and protection slot numbers must be the same in   oneToOne(2).   onePlusOne \: This can be supported on the same card  and across 2 cards.  This mode means that the transmit and receive signals  go only over the active line(which could be working or   protection line). (straight cable implied)   oneToOne \: This is supported only on the same card  This mode means that the transmit and receive signals  go over the working and protection lines.  (straight cable implied)   anexBOnePlusOne \: This can be supported on the same card  and across 2 cards.  This mode is like the onePlusOne mode, except that the  'csApsDirection' can only be bi\-directional.  (straight cable implied)   ycableOnePlusOneNok1k2\: With Y\-cable ignore K1K2 bytes.  This mode is the Y\-cable redundancy mode.   straightOnePlusOneNok1k2 \: With straight cable, ignore                              K1K2 bytes. This mode is like                             onePlusOne, but with K1, K2                              bytes ignored
            	**type**\: :py:class:`CsApsArchMode_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchMode_Enum>`
            
            .. attribute:: csapsarchmodeoperational
            
            	This object shows the actual APS architecture mode that is implemented on the Near End terminal. APS architecture mode configured through csApsArchMode object is  negotiated with the Far End through APS channel.  Architecture mode acceptable to both the Near End and  the Far End terminals is then operational at the Near  End. This value can be different than the APS  Architecture mode configured
            	**type**\: :py:class:`CsApsArchModeOperational_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchModeOperational_Enum>`
            
            .. attribute:: csapschannelprotocol
            
            	This object allows to configure APS channel protocol to  be implemented at Near End terminal.  K1 and K2 overhead bytes in a SONET signal are used as an APS channel. This channel is used to carry APS protocol.  Possible values\: bellcore(1) \: Implements APS channel protocol as defined               in bellcore document GR\-253\-CORE. itu(2) \: Implements APS channel protocol as defined in           ITU document G.783
            	**type**\: :py:class:`CsApsChannelProtocol_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsChannelProtocol_Enum>`
            
            .. attribute:: csapsdirection
            
            	This object is used to configure the switching  direction which this APS line supports.   Unidirectional \: APS switch only in one direction. Bidirectional  \: APS switch in both ends of the line
            	**type**\: :py:class:`CsApsDirection_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirection_Enum>`
            
            .. attribute:: csapsdirectionoperational
            
            	This object shows the actual APS direction that is  implemented on the Near End terminal. APS direction  configured through csApsDirection is negotiated with the Far End and APS direction setting acceptable to  both ends is operational at the Near End
            	**type**\: :py:class:`CsApsDirectionOperational_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirectionOperational_Enum>`
            
            .. attribute:: csapsenable
            
            	This object is used to enable or disable the APS feature on the working/protection line pairs. When enabled, the hardware will automatically switch the active line  from the working line to the protection line within 60ms, or vice versa
            	**type**\: :py:class:`CsApsEnable_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsEnable_Enum>`
            
            .. attribute:: csapsfailurestatus
            
            	This object indicates APS line failure status
            	**type**\: :py:class:`CsApsLineFailureStatus_Bits <ydk.models.sonet.CISCO_SONET_MIB.CsApsLineFailureStatus_Bits>`
            
            .. attribute:: csapsprimarysection
            
            	This object indicates which working section is the APS primary section. In G.783 AnnexB, the K1/K2 Bytes are received on the secondary Section. All the Switch Requests are for a switch from the primary section to the secondary section. The object csApsActiveline will indicate which section is currently carrying the traffic.  Once the switch request clears normally, traffic is maintained on the section to which it was switched by making that section the primary section.   Possible values\:  workingSection1(1)\: Working Section 1 is Primary Section workingSection2(2)\: Working Section 2 is Primary Section none(3)           \: none
            	**type**\: :py:class:`CsApsPrimarySection_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsPrimarySection_Enum>`
            
            .. attribute:: csapsprotectionindex
            
            	The protection line indicates that it will become the active line when an APS switch occurs (APS switch could occur because of a failure on the working line). For G.783 AnnexB, This index refers to Working Section 2
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsrevertive
            
            	This object is used to configure the APS revertive or nonrevertive option.   revertive \:    Will switch the working line back to active state after   the Wait\-To\-restore interval has expired and the    working line Signal\-Fault/Signal\-Degrade has been    cleared. Please refer to 'csApsWaitToRestore' for    description of Wait\-To\-Restore interval. nonrevertive \:    The  protection line continues to be the active line,   The active line does not switch to the working line
            	**type**\: :py:class:`CsApsRevertive_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsRevertive_Enum>`
            
            .. attribute:: csapssigdegradeber
            
            	This object contains the Bit Error Rate threshold for Signal Degrade detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to \-n where n is between 5 and 9
            	**type**\: int
            
            	**range:** 5..9
            
            .. attribute:: csapssigfaultber
            
            	This object contains the Bit Error Rate threshold for Signal Fault detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to the \-n, where n is between 3 and 5
            	**type**\: int
            
            	**range:** 3..5
            
            .. attribute:: csapsswitchreason
            
            	This object indicates APS line switch reason
            	**type**\: :py:class:`CsApsLineSwitchReason_Enum <ydk.models.sonet.CISCO_SONET_MIB.CsApsLineSwitchReason_Enum>`
            
            .. attribute:: csapswaittorestore
            
            	This object contains interval in minutes to wait  before attempting to switch back to working line.  Not applicable if the line is configured in  non\-revertive mode, i.e. protection line will  continue to be active, even if failures on the  working line are cleared. The framer clears the  signal\-fault and signal\-degrade when APS switch  occurs. Please refer to 'csApsRevertive' for  description of non\-revertive
            	**type**\: int
            
            	**range:** 1..12
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.csapsworkingindex = None
                self.csapsactiveline = None
                self.csapsarchmode = None
                self.csapsarchmodeoperational = None
                self.csapschannelprotocol = None
                self.csapsdirection = None
                self.csapsdirectionoperational = None
                self.csapsenable = None
                self.csapsfailurestatus = CsApsLineFailureStatus_Bits()
                self.csapsprimarysection = None
                self.csapsprotectionindex = None
                self.csapsrevertive = None
                self.csapssigdegradeber = None
                self.csapssigfaultber = None
                self.csapsswitchreason = None
                self.csapswaittorestore = None

            class CsApsActiveLine_Enum(Enum):
                """
                CsApsActiveLine_Enum

                This object indicates which line is currently active. 
                It could be the working line(Section 1 for Annex B),
                the protection line(Section 2 for Annex B) or none
                if neither working nor protection line is active. 
                This object reflects the status of receive direction.

                """

                CSAPSWORKINGLINE = 1

                CSAPSPROTECTIONLINE = 2

                CSAPSNONE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsActiveLine_Enum']


            class CsApsArchModeOperational_Enum(Enum):
                """
                CsApsArchModeOperational_Enum

                This object shows the actual APS architecture mode that
                is implemented on the Near End terminal. APS architecture
                mode configured through csApsArchMode object is 
                negotiated with the Far End through APS channel. 
                Architecture mode acceptable to both the Near End and 
                the Far End terminals is then operational at the Near 
                End. This value can be different than the APS 
                Architecture mode configured.

                """

                ONEPLUSONE = 1

                ONETOONE = 2

                ANEXBONEPLUSONE = 3

                YCABLEONEPLUSONENOK1K2 = 4

                STRAIGHTONEPLUSONENOK1K2 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchModeOperational_Enum']


            class CsApsArchMode_Enum(Enum):
                """
                CsApsArchMode_Enum

                This object is used to configure APS architecture mode
                on the working/protection line pairs.
                
                 All of the following are supported on single slot.
                 oneToOne(2) is not  supported across 2 slots,i.e. the 
                 working and protection slot numbers must be the same in 
                 oneToOne(2).
                
                 onePlusOne \: This can be supported on the same card
                 and across 2 cards.
                 This mode means that the transmit and receive signals
                 go only over the active line(which could be working or 
                 protection line). (straight cable implied)
                
                 oneToOne \: This is supported only on the same card
                 This mode means that the transmit and receive signals
                 go over the working and protection lines.
                 (straight cable implied)
                
                 anexBOnePlusOne \: This can be supported on the same card
                 and across 2 cards.
                 This mode is like the onePlusOne mode, except that the
                 'csApsDirection' can only be bi\-directional.
                 (straight cable implied)
                
                 ycableOnePlusOneNok1k2\: With Y\-cable ignore K1K2 bytes.
                 This mode is the Y\-cable redundancy mode.
                
                 straightOnePlusOneNok1k2 \: With straight cable, ignore 
                                            K1K2 bytes. This mode is like
                                            onePlusOne, but with K1, K2 
                                            bytes ignored.

                """

                ONEPLUSONE = 1

                ONETOONE = 2

                ANEXBONEPLUSONE = 3

                YCABLEONEPLUSONENOK1K2 = 4

                STRAIGHTONEPLUSONENOK1K2 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchMode_Enum']


            class CsApsChannelProtocol_Enum(Enum):
                """
                CsApsChannelProtocol_Enum

                This object allows to configure APS channel protocol to 
                be implemented at Near End terminal.
                
                K1 and K2 overhead bytes in a SONET signal are used as
                an APS channel.
                This channel is used to carry APS protocol.
                
                Possible values\:
                bellcore(1) \: Implements APS channel protocol as defined
                              in bellcore document GR\-253\-CORE.
                itu(2) \: Implements APS channel protocol as defined in 
                         ITU document G.783.

                """

                BELLCORE = 1

                ITU = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsChannelProtocol_Enum']


            class CsApsDirectionOperational_Enum(Enum):
                """
                CsApsDirectionOperational_Enum

                This object shows the actual APS direction that is 
                implemented on the Near End terminal. APS direction 
                configured through csApsDirection is negotiated with
                the Far End and APS direction setting acceptable to 
                both ends is operational at the Near End.

                """

                UNIDIRECTIONAL = 1

                BIDIRECTIONAL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirectionOperational_Enum']


            class CsApsDirection_Enum(Enum):
                """
                CsApsDirection_Enum

                This object is used to configure the switching 
                direction which this APS line supports. 
                
                Unidirectional \: APS switch only in one direction.
                Bidirectional  \: APS switch in both ends of the line.

                """

                UNIDIRECTIONAL = 1

                BIDIRECTIONAL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirection_Enum']


            class CsApsEnable_Enum(Enum):
                """
                CsApsEnable_Enum

                This object is used to enable or disable the APS feature
                on the working/protection line pairs. When enabled,
                the hardware will automatically switch the active line 
                from the working line to the protection line within 60ms,
                or vice versa.

                """

                CSAPSDISABLED = 1

                CSAPSENABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsEnable_Enum']


            class CsApsPrimarySection_Enum(Enum):
                """
                CsApsPrimarySection_Enum

                This object indicates which working section is the APS
                primary section. In G.783 AnnexB, the K1/K2 Bytes are
                received on the secondary Section. All the Switch
                Requests are for a switch from the primary section to
                the secondary section. The object csApsActiveline will
                indicate which section is currently carrying the
                traffic.  Once the switch request clears normally,
                traffic is maintained on the section to which it was
                switched by making that section the primary section. 
                
                Possible values\: 
                workingSection1(1)\: Working Section 1 is Primary Section
                workingSection2(2)\: Working Section 2 is Primary Section
                none(3)           \: none.

                """

                WORKINGSECTION1 = 1

                WORKINGSECTION2 = 2

                NONE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsPrimarySection_Enum']


            class CsApsRevertive_Enum(Enum):
                """
                CsApsRevertive_Enum

                This object is used to configure the APS revertive or
                nonrevertive option. 
                
                revertive \: 
                  Will switch the working line back to active state after
                  the Wait\-To\-restore interval has expired and the 
                  working line Signal\-Fault/Signal\-Degrade has been 
                  cleared. Please refer to 'csApsWaitToRestore' for 
                  description of Wait\-To\-Restore interval.
                nonrevertive \: 
                  The  protection line continues to be the active line,
                  The active line does not switch to the working line.

                """

                NONREVERTIVE = 1

                REVERTIVE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsRevertive_Enum']


            @property
            def _common_path(self):
                if self.csapsworkingindex is None:
                    raise YPYDataValidationError('Key property csapsworkingindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csApsConfigTable/CISCO-SONET-MIB:csApsConfigEntry[CISCO-SONET-MIB:csApsWorkingIndex = ' + str(self.csapsworkingindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csapsworkingindex is not None:
                    return True

                if self.csapsactiveline is not None:
                    return True

                if self.csapsarchmode is not None:
                    return True

                if self.csapsarchmodeoperational is not None:
                    return True

                if self.csapschannelprotocol is not None:
                    return True

                if self.csapsdirection is not None:
                    return True

                if self.csapsdirectionoperational is not None:
                    return True

                if self.csapsenable is not None:
                    return True

                if self.csapsfailurestatus is not None:
                    if self.csapsfailurestatus._has_data():
                        return True

                if self.csapsprimarysection is not None:
                    return True

                if self.csapsprotectionindex is not None:
                    return True

                if self.csapsrevertive is not None:
                    return True

                if self.csapssigdegradeber is not None:
                    return True

                if self.csapssigfaultber is not None:
                    return True

                if self.csapsswitchreason is not None:
                    return True

                if self.csapswaittorestore is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csApsConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csapsconfigentry is not None:
                for child_ref in self.csapsconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsApsConfigTable']['meta_info']


    class CsAu4Tug3ConfigTable(object):
        """
        This table contains objects to configure the VC( Virtual
        Container) related properties of a TUG\-3 within a AU\-4 
        paths.
        
        This table allows creation of
        following multiplexing structure\:
        STM\-1/AU\-4/TUG\-3/TU\-3/DS3
        STM\-1/AU\-4/TUG\-3/TU\-3/E3
        STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-11/DS1
        STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-12/E1
        
        Three entries are created in this table for a given AU\-4 
        path when cspSonetPathPayload object is set to one of the 
        following\:
            vt15vc11(4),
            vt2vc12(5),
            ds3(3),
            e3(8),
            vtStructured(9)
        
        .. attribute:: csau4tug3configentry
        
        	There is an entry in this table for each TUG\-3 within a  AU\-4 SDH path that supports SDH virtual container VC\-4. The ifIndex value represents an entry in ifTable with ifType = sonetPath(50).The ifTable entry applicable for this entry belongs to AU\-4 path
        	**type**\: list of :py:class:`CsAu4Tug3ConfigEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csau4tug3configentry = YList()
            self.csau4tug3configentry.parent = self
            self.csau4tug3configentry.name = 'csau4tug3configentry'


        class CsAu4Tug3ConfigEntry(object):
            """
            There is an entry in this table for each TUG\-3 within a 
            AU\-4 SDH path that supports SDH virtual container VC\-4.
            The ifIndex value represents an entry in ifTable with
            ifType = sonetPath(50).The ifTable entry applicable for
            this entry belongs to AU\-4 path.
            
            .. attribute:: csau4tug3
            
            	This object represents the TUG\-3 number
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csau4tug3payload
            
            	This object is used for configuring the payload for the tributary group.  The possible values are \:  vc11   \: When set to 'vc11' following things are done\:        \- 28 entries created in ifTable for TU\-11 with           ifType = sonetVT(51)        \- 28 entries created in ifTable for DS1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11  vc12   \: When set to 'vc12' following things are done\:        \- 21 entries created in ifTable for TU\-12 with           ifType = sonetVT(51)        \- 21 entries created in ifTable for E1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12  tu3ds3 \: When set to 'tu3ds3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for DS3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  tu3e3  \: When set to 'tu3e3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for E3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  The value 'other' can not be set
            	**type**\: :py:class:`CsAu4Tug3Payload_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry.CsAu4Tug3Payload_Enum>`
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.csau4tug3 = None
                self.ifindex = None
                self.csau4tug3payload = None

            class CsAu4Tug3Payload_Enum(Enum):
                """
                CsAu4Tug3Payload_Enum

                This object is used for configuring the payload
                for the tributary group.
                
                The possible values are \:
                
                vc11   \: When set to 'vc11' following things are done\:
                       \- 28 entries created in ifTable for TU\-11 with 
                         ifType = sonetVT(51)
                       \- 28 entries created in ifTable for DS1 with 
                         ifType = ds1(18)
                
                         STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11
                
                vc12   \: When set to 'vc12' following things are done\:
                       \- 21 entries created in ifTable for TU\-12 with 
                         ifType = sonetVT(51)
                       \- 21 entries created in ifTable for E1 with 
                         ifType = ds1(18)
                
                         STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12
                
                tu3ds3 \: When set to 'tu3ds3' following things are done\:
                       \- 1 entry created in ifTable for TU\-3 with 
                         ifType = sonetVT(51)
                       \- 1 entry created in ifTable for DS3 with 
                         ifType = ds3(30)
                
                         STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3
                
                tu3e3  \: When set to 'tu3e3' following things are done\:
                       \- 1 entry created in ifTable for TU\-3 with 
                         ifType = sonetVT(51)
                       \- 1 entry created in ifTable for E3 with 
                         ifType = ds3(30)
                
                         STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3
                
                The value 'other' can not be set.

                """

                OTHER = 1

                VC11 = 2

                VC12 = 3

                TU3DS3 = 4

                TU3E3 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry.CsAu4Tug3Payload_Enum']


            @property
            def _common_path(self):
                if self.csau4tug3 is None:
                    raise YPYDataValidationError('Key property csau4tug3 is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csAu4Tug3ConfigTable/CISCO-SONET-MIB:csAu4Tug3ConfigEntry[CISCO-SONET-MIB:csAu4Tug3 = ' + str(self.csau4tug3) + '][CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csau4tug3 is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.csau4tug3payload is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csAu4Tug3ConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csau4tug3configentry is not None:
                for child_ref in self.csau4tug3configentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable']['meta_info']


    class CsConfigTable(object):
        """
        The SONET/SDH configuration table. This table has objects 
        for configuring sonet lines.
        
        .. attribute:: csconfigentry
        
        	An entry in the table. There is an entry for each SONET line  in the table. Entries are automatically created for an  ifType value of sonet(39). 'ifAdminStatus' from the ifTable  must be used to enable or disable a line. A line is in  disabled(down) state unless provisioned 'up' using  'ifAdminStatus'
        	**type**\: list of :py:class:`CsConfigEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csconfigentry = YList()
            self.csconfigentry.parent = self
            self.csconfigentry.name = 'csconfigentry'


        class CsConfigEntry(object):
            """
            An entry in the table. There is an entry for each SONET line 
            in the table. Entries are automatically created for an 
            ifType value of sonet(39). 'ifAdminStatus' from the ifTable 
            must be used to enable or disable a line. A line is in 
            disabled(down) state unless provisioned 'up' using 
            'ifAdminStatus'.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csconfigframescramble
            
            	This object is used to disable or enable the Scrambling option in SONET line
            	**type**\: :py:class:`CsConfigFrameScramble_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigFrameScramble_Enum>`
            
            .. attribute:: csconfigloopbacktype
            
            	This object specifies the desired loopback mode configuration of the SONET line. The possible values of this objects are follows\:  noLoopback \:           Not in the loopback state.   lineLocal \:          The signal transmitted from this interface         is connected to the associated incoming         receiver. This ensures that the SONET frame         transmitted from the interface is received back         at the interface. lineRemote \:         The signal received at the interface is looped         back out to the associated transmitter.         This ensures that the remote equipment that         originated the signal receives it back. The          signal may undergo degradation as a result of         the characteristics of the transmission          medium
            	**type**\: :py:class:`CsConfigLoopbackType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigLoopbackType_Enum>`
            
            .. attribute:: csconfigrdiptype
            
            	This object represents the type of RDI\-P (Remote Defect Indication \- Path) sent by this Network Element (NE) to remote Network Element.        onebit     \: use 1 bit RDI\-P       threebit   \: use 3 bit enhanced RDI\-P.  Default is onebit
            	**type**\: :py:class:`CsConfigRDIPType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIPType_Enum>`
            
            .. attribute:: csconfigrdivtype
            
            	This object specifies the type of RDI\-V (Remote Defect Indication \- Virtual Tributary/Container) sent by this  Network Element (NE) to the remote Network Element.        onebit     \: use 1 bit RDI\-V       threebit   \: use 3 bit enhanced RDI\-V.  Default is onebit
            	**type**\: :py:class:`CsConfigRDIVType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIVType_Enum>`
            
            .. attribute:: csconfigtype
            
            	This object represents the configured line type. Sts is SONET format. Stm is SDH format.      sonetSts3c   \: OC3 concatenated     sonetStm1    \: European standard OC3     sonetSts12c  \: OC12 concatenated     sonetStm4    \: European standard OC12     sonetSts48c  \: OC48 concatenated     sonetStm16   \: European standard OC48      sonetSts192c \: OC\-192 concatenated     sonetStm64   \: European standard OC\-192     sonetSts3    \: OC3 (unconcatenated)     
            	**type**\: :py:class:`CsConfigType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigType_Enum>`
            
            .. attribute:: csconfigxmtclocksource
            
            	Specifies the source of the transmit clock.  loopTiming\: indicates that the recovered receive              clock is used as the transmit clock.  localTiming\: indicates that a local clock source is              used or that an external clock is               attached to the box containing the               interface. 
            	**type**\: :py:class:`CsConfigXmtClockSource_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigXmtClockSource_Enum>`
            
            .. attribute:: cssignallingtransportmode
            
            	This object represents the mode used to transport DS0  signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling is  transferred to the VT header. In clearMode(3), only the  framing bit is transferred to the VT header.       Default is signallingTransferMode(2) if csTributaryMappingType  is byteSynchronous. For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\: :py:class:`CsSignallingTransportMode_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsSignallingTransportMode_Enum>`
            
            .. attribute:: cstributaryframingtype
            
            	This object represents the framing type to be assigned to the virtual tributaries in byte sync mapping mode.        notApplicable  \:  If VT mapping is not byteSynchronous(2).       dsx1ESF        \:  Extended Superframe Format       dsx1D4         \:  Superframe Format  Default is dsx1ESF(3) if csTributaryMappingType is  byteSynchronous(2). For asynchronous(1) mapping, the default is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\: :py:class:`CsTributaryFramingType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryFramingType_Enum>`
            
            .. attribute:: cstributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.    au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.    au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  Default is au3Grouping(2) for SDH and notApplicable(1) for SONET
            	**type**\: :py:class:`CsTributaryGroupingType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryGroupingType_Enum>`
            
            .. attribute:: cstributarymappingtype
            
            	This object represents the VT/VC mapping type.  asynchronous\:    In this mode, the channel structure of                   DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside the                  VT/VC can be found and extracted from the                  frame.  Default is asynchronous(1)
            	**type**\: :py:class:`CsTributaryMappingType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryMappingType_Enum>`
            
            .. attribute:: cstributarytype
            
            	Type of the tributary carried within the SONET/SDH signal.  vt15vc11    \: carries T1 signal vt2vc12     \: carries E1 signal
            	**type**\: :py:class:`CsTributaryType_Enum <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryType_Enum>`
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csconfigframescramble = None
                self.csconfigloopbacktype = None
                self.csconfigrdiptype = None
                self.csconfigrdivtype = None
                self.csconfigtype = None
                self.csconfigxmtclocksource = None
                self.cssignallingtransportmode = None
                self.cstributaryframingtype = None
                self.cstributarygroupingtype = None
                self.cstributarymappingtype = None
                self.cstributarytype = None

            class CsConfigFrameScramble_Enum(Enum):
                """
                CsConfigFrameScramble_Enum

                This object is used to disable or enable the Scrambling
                option in SONET line.

                """

                DISABLED = 1

                ENABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigFrameScramble_Enum']


            class CsConfigLoopbackType_Enum(Enum):
                """
                CsConfigLoopbackType_Enum

                This object specifies the desired loopback mode
                configuration of the SONET line.
                The possible values of this objects are follows\:
                
                noLoopback \:  
                        Not in the loopback state.  
                lineLocal \: 
                        The signal transmitted from this interface
                        is connected to the associated incoming
                        receiver. This ensures that the SONET frame
                        transmitted from the interface is received back
                        at the interface.
                lineRemote \:
                        The signal received at the interface is looped
                        back out to the associated transmitter.
                        This ensures that the remote equipment that
                        originated the signal receives it back. The 
                        signal may undergo degradation as a result of
                        the characteristics of the transmission 
                        medium.

                """

                NOLOOPBACK = 1

                LINELOCAL = 2

                LINEREMOTE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigLoopbackType_Enum']


            class CsConfigRDIPType_Enum(Enum):
                """
                CsConfigRDIPType_Enum

                This object represents the type of RDI\-P (Remote Defect
                Indication \- Path) sent by this Network Element (NE)
                to remote Network Element.
                
                      onebit     \: use 1 bit RDI\-P
                      threebit   \: use 3 bit enhanced RDI\-P.
                
                Default is onebit.

                """

                ONEBIT = 1

                THREEBIT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIPType_Enum']


            class CsConfigRDIVType_Enum(Enum):
                """
                CsConfigRDIVType_Enum

                This object specifies the type of RDI\-V (Remote Defect
                Indication \- Virtual Tributary/Container) sent by this 
                Network Element (NE) to the remote Network Element.
                
                      onebit     \: use 1 bit RDI\-V
                      threebit   \: use 3 bit enhanced RDI\-V.
                
                Default is onebit.

                """

                ONEBIT = 1

                THREEBIT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIVType_Enum']


            class CsConfigType_Enum(Enum):
                """
                CsConfigType_Enum

                This object represents the configured line type.
                Sts is SONET format. Stm is SDH format. 
                    sonetSts3c   \: OC3 concatenated
                    sonetStm1    \: European standard OC3
                    sonetSts12c  \: OC12 concatenated
                    sonetStm4    \: European standard OC12
                    sonetSts48c  \: OC48 concatenated
                    sonetStm16   \: European standard OC48 
                    sonetSts192c \: OC\-192 concatenated
                    sonetStm64   \: European standard OC\-192
                    sonetSts3    \: OC3 (unconcatenated)
                    

                """

                SONETSTS3C = 1

                SONETSTM1 = 2

                SONETSTS12C = 3

                SONETSTM4 = 4

                SONETSTS48C = 5

                SONETSTM16 = 6

                SONETSTS192C = 7

                SONETSTM64 = 8

                SONETSTS3 = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigType_Enum']


            class CsConfigXmtClockSource_Enum(Enum):
                """
                CsConfigXmtClockSource_Enum

                Specifies the source of the transmit clock.
                
                loopTiming\: indicates that the recovered receive 
                            clock is used as the transmit clock.
                
                localTiming\: indicates that a local clock source is
                             used or that an external clock is 
                             attached to the box containing the 
                             interface. 

                """

                LOOPTIMING = 1

                LOCALTIMING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigXmtClockSource_Enum']


            class CsSignallingTransportMode_Enum(Enum):
                """
                CsSignallingTransportMode_Enum

                This object represents the mode used to transport DS0 
                signalling information for T1 byteSynchronous mapping (GR253).
                In signallingTransferMode(2), the robbed\-bit signalling is 
                transferred to the VT header. In clearMode(3), only the 
                framing bit is transferred to the VT header.
                     
                Default is signallingTransferMode(2) if csTributaryMappingType 
                is byteSynchronous. For asynchronous mapping, it is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.

                """

                NOTAPPLICABLE = 1

                SIGNALLINGTRANSFERMODE = 2

                CLEARMODE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsSignallingTransportMode_Enum']


            class CsTributaryFramingType_Enum(Enum):
                """
                CsTributaryFramingType_Enum

                This object represents the framing type to be assigned to the
                virtual tributaries in byte sync mapping mode.
                
                      notApplicable  \:  If VT mapping is not byteSynchronous(2).
                      dsx1ESF        \:  Extended Superframe Format
                      dsx1D4         \:  Superframe Format
                
                Default is dsx1ESF(3) if csTributaryMappingType is 
                byteSynchronous(2). For asynchronous(1) mapping, the default is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.

                """

                NOTAPPLICABLE = 1

                DSX1D4 = 2

                DSX1ESF = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryFramingType_Enum']


            class CsTributaryGroupingType_Enum(Enum):
                """
                CsTributaryGroupingType_Enum

                This object represents the method used to group VCs into an
                STM\-1 signal. Applicable only to SDH.
                
                  au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or
                               STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.
                
                  au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or
                               STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.
                
                Default is au3Grouping(2) for SDH and notApplicable(1) for SONET.

                """

                NOTAPPLICABLE = 1

                AU3GROUPING = 2

                AU4GROUPING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryGroupingType_Enum']


            class CsTributaryMappingType_Enum(Enum):
                """
                CsTributaryMappingType_Enum

                This object represents the VT/VC mapping type.
                
                asynchronous\:    In this mode, the channel structure of 
                                 DS1/E1 is neither visible nor preserved.
                
                byteSynchronous\: In this mode, the DS0 signals inside the
                                 VT/VC can be found and extracted from the
                                 frame.
                
                Default is asynchronous(1).

                """

                ASYNCHRONOUS = 1

                BYTESYNCHRONOUS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryMappingType_Enum']


            class CsTributaryType_Enum(Enum):
                """
                CsTributaryType_Enum

                Type of the tributary carried within the SONET/SDH signal.
                
                vt15vc11    \: carries T1 signal
                vt2vc12     \: carries E1 signal

                """

                VT15VC11 = 1

                VT2VC12 = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryType_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csConfigTable/CISCO-SONET-MIB:csConfigEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csconfigframescramble is not None:
                    return True

                if self.csconfigloopbacktype is not None:
                    return True

                if self.csconfigrdiptype is not None:
                    return True

                if self.csconfigrdivtype is not None:
                    return True

                if self.csconfigtype is not None:
                    return True

                if self.csconfigxmtclocksource is not None:
                    return True

                if self.cssignallingtransportmode is not None:
                    return True

                if self.cstributaryframingtype is not None:
                    return True

                if self.cstributarygroupingtype is not None:
                    return True

                if self.cstributarymappingtype is not None:
                    return True

                if self.cstributarytype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csconfigentry is not None:
                for child_ref in self.csconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsConfigTable']['meta_info']


    class CsNotifications(object):
        """
        
        
        .. attribute:: csnotificationsenabled
        
        	This object controls if the generation of  ciscoSonetSectionStatusChange, ciscoSonetLineStatusChange,  ciscoSonetPathStatusChange and ciscoSonetVTStatusChange notifications is enabled. If the value of this object is 'true(1)', then all notifications in this MIB are enabled; otherwise they are disabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csnotificationsenabled = None

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csNotifications'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csnotificationsenabled is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsNotifications']['meta_info']


    class CsStatsTable(object):
        """
        The SONET/SDH Section statistics table. This table 
        maintains the number of times the line encountered Loss of
        Signal(LOS), Loss of frame(LOF), Alarm Indication 
        signals(AISs), Remote failure indications(RFIs).
        
        .. attribute:: csstatsentry
        
        	An entry in the SONET/SDH statistics table. These are  realtime statistics for the Sonet section, line and path layers. The statistics are gathered for each sonet line.  An entry is created automatically and is indexed by  ifIndex
        	**type**\: list of :py:class:`CsStatsEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CsStatsTable.CsStatsEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstatsentry = YList()
            self.csstatsentry.parent = self
            self.csstatsentry.name = 'csstatsentry'


        class CsStatsEntry(object):
            """
            An entry in the SONET/SDH statistics table. These are 
            realtime statistics for the Sonet section, line and path
            layers. The statistics are gathered for each sonet line. 
            An entry is created automatically and is indexed by 
            ifIndex.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cslaiss
            
            	The number of alarm indication signals(AIS)  encountered by  a SONET/SDH Line. A high value for this object may indicate a problem with the Sonet Line layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cslrfis
            
            	The number of remote failure indications (RFI) encountered  by a SONET/SDH Line. A high value for this object may  indicate a problem with the Sonet Line layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cspaiss
            
            	The  number of alarm indication signals (AIS) encountered by a SONET/SDH Path. A high value for this object may  indicate a problem with the Sonet Path layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csprfis
            
            	The number of  remote failure indications (RFI)  encountered by a SONET/SDH Path. A high value for this  object may indicate a problem with the Sonet Path layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csslofs
            
            	The number of Loss of Frames (LOF) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cssloss
            
            	The number of Loss of signals(LOS) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cslaiss = None
                self.cslrfis = None
                self.cspaiss = None
                self.csprfis = None
                self.csslofs = None
                self.cssloss = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csStatsTable/CISCO-SONET-MIB:csStatsEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cslaiss is not None:
                    return True

                if self.cslrfis is not None:
                    return True

                if self.cspaiss is not None:
                    return True

                if self.csprfis is not None:
                    return True

                if self.csslofs is not None:
                    return True

                if self.cssloss is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CsStatsTable.CsStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csstatsentry is not None:
                for child_ref in self.csstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CsStatsTable']['meta_info']


    class CslFarEndTotalTable(object):
        """
        The SONET/SDH Far End Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour 
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since the 
        line is enabled.
        
        .. attribute:: cslfarendtotalentry
        
        	An entry in the SONET/SDH Far End Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of :py:class:`CslFarEndTotalEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.cslfarendtotalentry = YList()
            self.cslfarendtotalentry.parent = self
            self.cslfarendtotalentry.name = 'cslfarendtotalentry'


        class CslFarEndTotalEntry(object):
            """
            An entry in the SONET/SDH Far End Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cslfarendtotalcvs
            
            	The number of Coding Violations encountered by a SONET/SDH  Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cslfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cslfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cslfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cslfarendtotalcvs = None
                self.cslfarendtotaless = None
                self.cslfarendtotalsess = None
                self.cslfarendtotaluass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslFarEndTotalTable/CISCO-SONET-MIB:cslFarEndTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cslfarendtotalcvs is not None:
                    return True

                if self.cslfarendtotaless is not None:
                    return True

                if self.cslfarendtotalsess is not None:
                    return True

                if self.cslfarendtotaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslFarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cslfarendtotalentry is not None:
                for child_ref in self.cslfarendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CslFarEndTotalTable']['meta_info']


    class CslTotalTable(object):
        """
        The SONET/SDH Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 
        hour period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since
        the line is enabled.
        
        .. attribute:: csltotalentry
        
        	An entry in the SONET/SDH Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of :py:class:`CslTotalEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CslTotalTable.CslTotalEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csltotalentry = YList()
            self.csltotalentry.parent = self
            self.csltotalentry.name = 'csltotalentry'


        class CslTotalEntry(object):
            """
            An entry in the SONET/SDH Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csltotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csltotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csltotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csltotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csltotalcvs = None
                self.csltotaless = None
                self.csltotalsess = None
                self.csltotaluass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslTotalTable/CISCO-SONET-MIB:cslTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csltotalcvs is not None:
                    return True

                if self.csltotaless is not None:
                    return True

                if self.csltotalsess is not None:
                    return True

                if self.csltotaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CslTotalTable.CslTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csltotalentry is not None:
                for child_ref in self.csltotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CslTotalTable']['meta_info']


    class CspFarEndTotalTable(object):
        """
        The SONET/SDH Far End Path Total table. Far End is the 
        remote end of the line. The table contains the cumulative
        sum of the various statistics for the 24 hour period 
        preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the
        number of 15 minute intervals that have elapsed since
        the line is enabled. 
        
        .. attribute:: cspfarendtotalentry
        
        	An entry in the SONET/SDH Far End Path Total table.  Entries are created automatically for sonet lines
        	**type**\: list of :py:class:`CspFarEndTotalEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.cspfarendtotalentry = YList()
            self.cspfarendtotalentry.parent = self
            self.cspfarendtotalentry.name = 'cspfarendtotalentry'


        class CspFarEndTotalEntry(object):
            """
            An entry in the SONET/SDH Far End Path Total table. 
            Entries are created automatically for sonet lines.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cspfarendtotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cspfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cspfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cspfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cspfarendtotalcvs = None
                self.cspfarendtotaless = None
                self.cspfarendtotalsess = None
                self.cspfarendtotaluass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspFarEndTotalTable/CISCO-SONET-MIB:cspFarEndTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cspfarendtotalcvs is not None:
                    return True

                if self.cspfarendtotaless is not None:
                    return True

                if self.cspfarendtotalsess is not None:
                    return True

                if self.cspfarendtotaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspFarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cspfarendtotalentry is not None:
                for child_ref in self.cspfarendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CspFarEndTotalTable']['meta_info']


    class CspTotalTable(object):
        """
        The SONET/SDH Path Total table. It contains the cumulative 
        sum of the various statistics for the 24 hour period 
        preceding the current interval.The object 
        'sonetMediumValidIntervals' from RFC2558 contains the number
        of 15 minute intervals that have elapsed since the line is 
        enabled.
        
        .. attribute:: csptotalentry
        
        	An entry in the SONET/SDH Path Total table. Entries are created automatically for sonet lines
        	**type**\: list of :py:class:`CspTotalEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspTotalTable.CspTotalEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csptotalentry = YList()
            self.csptotalentry.parent = self
            self.csptotalentry.name = 'csptotalentry'


        class CspTotalEntry(object):
            """
            An entry in the SONET/SDH Path Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csptotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csptotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csptotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csptotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csptotalcvs = None
                self.csptotaless = None
                self.csptotalsess = None
                self.csptotaluass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTotalTable/CISCO-SONET-MIB:cspTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csptotalcvs is not None:
                    return True

                if self.csptotaless is not None:
                    return True

                if self.csptotalsess is not None:
                    return True

                if self.csptotaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CspTotalTable.CspTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csptotalentry is not None:
                for child_ref in self.csptotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CspTotalTable']['meta_info']


    class CspTraceTable(object):
        """
        The SONET/SDH Path Trace table. This table contains objects 
        for tracing the sonet path.
        
        .. attribute:: csptraceentry
        
        	An entry in the SONET/SDH Path Trace table. The entries  exist for active sonet lines. The objects in this table are  used to verify continued connection between the two ends of the line
        	**type**\: list of :py:class:`CspTraceEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CspTraceTable.CspTraceEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csptraceentry = YList()
            self.csptraceentry.parent = self
            self.csptraceentry.name = 'csptraceentry'


        class CspTraceEntry(object):
            """
            An entry in the SONET/SDH Path Trace table. The entries 
            exist for active sonet lines. The objects in this table are 
            used to verify continued connection between the two ends of
            the line.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csptracefailure
            
            	The value of this object is set to 'true' when Sonet Path  received trace does not match the 'cspTraceToExpect'
            	**type**\: bool
            
            .. attribute:: csptracereceived
            
            	This object is used to view the Sonet Path Trace that is received by the receiving terminal
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            .. attribute:: csptracetoexpect
            
            	Sonet Path Trace To Expect.  The receiving terminal verifies if the incoming string matches this string. The value of  'cspTraceFailure' indicates whether a trace mismatch  occured. The default value is a zero\-length string
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            .. attribute:: csptracetotransmit
            
            	Sonet Path Trace To Transmit. The trace string is  repetitively transmited so that a trace receiving terminal  can verify its continued receiving terminal can verify its  continued connection to the intended transmitter. The  default value is a zero\-length string. Unless this object  is set to a non\-zero length string, tracing will not be  performed
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csptracefailure = None
                self.csptracereceived = None
                self.csptracetoexpect = None
                self.csptracetotransmit = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTraceTable/CISCO-SONET-MIB:cspTraceEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csptracefailure is not None:
                    return True

                if self.csptracereceived is not None:
                    return True

                if self.csptracetoexpect is not None:
                    return True

                if self.csptracetotransmit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CspTraceTable.CspTraceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTraceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csptraceentry is not None:
                for child_ref in self.csptraceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CspTraceTable']['meta_info']


    class CssTotalTable(object):
        """
        The SONET/SDH Section Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the
        number of 15 minute intervals that have elapsed since
        the line is enabled. 
        
        .. attribute:: csstotalentry
        
        	An entry in the SONET/SDH Section Total table. Entries are created automatically for sonet lines
        	**type**\: list of :py:class:`CssTotalEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CssTotalTable.CssTotalEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstotalentry = YList()
            self.csstotalentry.parent = self
            self.csstotalentry.name = 'csstotalentry'


        class CssTotalEntry(object):
            """
            An entry in the SONET/SDH Section Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csstotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csstotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csstotalsefss
            
            	The number of Severely Errored Framing Seconds  encountered by a SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csstotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csstotalcvs = None
                self.csstotaless = None
                self.csstotalsefss = None
                self.csstotalsess = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTotalTable/CISCO-SONET-MIB:cssTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csstotalcvs is not None:
                    return True

                if self.csstotaless is not None:
                    return True

                if self.csstotalsefss is not None:
                    return True

                if self.csstotalsess is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CssTotalTable.CssTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csstotalentry is not None:
                for child_ref in self.csstotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CssTotalTable']['meta_info']


    class CssTraceTable(object):
        """
        The SONET/SDH Section Trace table. This table contains 
        objects for tracing the sonet section.
        
        .. attribute:: csstraceentry
        
        	An entry in the trace table. Entries exist for active sonet lines. The objects in this table are used to verify  continued connection between the two ends of the line
        	**type**\: list of :py:class:`CssTraceEntry <ydk.models.sonet.CISCO_SONET_MIB.CISCOSONETMIB.CssTraceTable.CssTraceEntry>`
        
        

        """

        _prefix = 'cisco-sonet'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstraceentry = YList()
            self.csstraceentry.parent = self
            self.csstraceentry.name = 'csstraceentry'


        class CssTraceEntry(object):
            """
            An entry in the trace table. Entries exist for active sonet
            lines. The objects in this table are used to verify 
            continued connection between the two ends of the line.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csstracefailure
            
            	The value of this object is set to 'true' when Sonet  Section received trace does not match the  'cssTraceToExpect'
            	**type**\: bool
            
            .. attribute:: csstracereceived
            
            	This object is used to view the Sonet Section Trace that  is received by the receiving terminal
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            .. attribute:: csstracetoexpect
            
            	Sonet Section Trace To Expect. The receiving terminal  verifies if the incoming string matches this string.  The value of 'cssTraceFailure' indicates whether a  trace mismatch occurred. The default value is a  zero\-length string
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            .. attribute:: csstracetotransmit
            
            	Sonet Section Trace To Transmit. This is string that is transmitted to perform Sonet section trace  diagnostics. The trace string is  repetitively  transmited so that a trace receiving terminal can  verify its continued connection to the intended  transmitter. The default value is a zero\-length string. Unless this object is set to a non\-zero length string,  tracing will not be performed
            	**type**\: str
            
            	**range:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'cisco-sonet'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csstracefailure = None
                self.csstracereceived = None
                self.csstracetoexpect = None
                self.csstracetotransmit = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTraceTable/CISCO-SONET-MIB:cssTraceEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.csstracefailure is not None:
                    return True

                if self.csstracereceived is not None:
                    return True

                if self.csstracetoexpect is not None:
                    return True

                if self.csstracetotransmit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CISCOSONETMIB.CssTraceTable.CssTraceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTraceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csstraceentry is not None:
                for child_ref in self.csstraceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CISCOSONETMIB.CssTraceTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-SONET-MIB:CISCO-SONET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.csapsconfig is not None and self.csapsconfig._has_data():
            return True

        if self.csapsconfig is not None and self.csapsconfig.is_presence():
            return True

        if self.csapsconfigtable is not None and self.csapsconfigtable._has_data():
            return True

        if self.csapsconfigtable is not None and self.csapsconfigtable.is_presence():
            return True

        if self.csau4tug3configtable is not None and self.csau4tug3configtable._has_data():
            return True

        if self.csau4tug3configtable is not None and self.csau4tug3configtable.is_presence():
            return True

        if self.csconfigtable is not None and self.csconfigtable._has_data():
            return True

        if self.csconfigtable is not None and self.csconfigtable.is_presence():
            return True

        if self.cslfarendtotaltable is not None and self.cslfarendtotaltable._has_data():
            return True

        if self.cslfarendtotaltable is not None and self.cslfarendtotaltable.is_presence():
            return True

        if self.csltotaltable is not None and self.csltotaltable._has_data():
            return True

        if self.csltotaltable is not None and self.csltotaltable.is_presence():
            return True

        if self.csnotifications is not None and self.csnotifications._has_data():
            return True

        if self.csnotifications is not None and self.csnotifications.is_presence():
            return True

        if self.cspfarendtotaltable is not None and self.cspfarendtotaltable._has_data():
            return True

        if self.cspfarendtotaltable is not None and self.cspfarendtotaltable.is_presence():
            return True

        if self.csptotaltable is not None and self.csptotaltable._has_data():
            return True

        if self.csptotaltable is not None and self.csptotaltable.is_presence():
            return True

        if self.csptracetable is not None and self.csptracetable._has_data():
            return True

        if self.csptracetable is not None and self.csptracetable.is_presence():
            return True

        if self.csstatstable is not None and self.csstatstable._has_data():
            return True

        if self.csstatstable is not None and self.csstatstable.is_presence():
            return True

        if self.csstotaltable is not None and self.csstotaltable._has_data():
            return True

        if self.csstotaltable is not None and self.csstotaltable.is_presence():
            return True

        if self.csstracetable is not None and self.csstracetable._has_data():
            return True

        if self.csstracetable is not None and self.csstracetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.sonet._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CISCOSONETMIB']['meta_info']


