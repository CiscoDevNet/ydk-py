""" CISCO_SONET_MIB 

The MIB module to describe SONET/SDH interfaces
objects. This is an extension to the standard SONET 
MIB(RFC 2558).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CsapslinefailurecodeEnum(Enum):
    """
    CsapslinefailurecodeEnum

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

    .. data:: csApsChannelMismatch = 1

    .. data:: csApsProtectionByteFail = 2

    .. data:: csApsFEProtectionFailure = 3

    .. data:: csApsModeMismatch = 4

    """

    csApsChannelMismatch = 1

    csApsProtectionByteFail = 2

    csApsFEProtectionFailure = 3

    csApsModeMismatch = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CsapslinefailurecodeEnum']


class CsapslineswitchreasonEnum(Enum):
    """
    CsapslineswitchreasonEnum

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

    .. data:: csApsOther = 1

    .. data:: csApsRevertive = 2

    .. data:: csApsManual = 3

    .. data:: csApsSignalDefectLow = 4

    .. data:: csApsSignalDefectHigh = 5

    .. data:: csApsSignalFailureLow = 6

    .. data:: csApsSignalFailureHigh = 7

    .. data:: csApsForceSwitch = 8

    .. data:: csApsLockOut = 9

    .. data:: csApsNoSwitch = 10

    """

    csApsOther = 1

    csApsRevertive = 2

    csApsManual = 3

    csApsSignalDefectLow = 4

    csApsSignalDefectHigh = 5

    csApsSignalFailureLow = 6

    csApsSignalFailureHigh = 7

    csApsForceSwitch = 8

    csApsLockOut = 9

    csApsNoSwitch = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CsapslineswitchreasonEnum']


class Csapslinefailurestatus(FixedBitsDict):
    """
    Csapslinefailurestatus

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
    Keys are:- noApsLineFailure , csApsChannelMismatchBit , csApsFEProtectionFailureBit , csApsProtectionByteFailBit , csApsModeMismatchBit

    """

    def __init__(self):
        self._dictionary = { 
            'noApsLineFailure':False,
            'csApsChannelMismatchBit':False,
            'csApsFEProtectionFailureBit':False,
            'csApsProtectionByteFailBit':False,
            'csApsModeMismatchBit':False,
        }
        self._pos_map = { 
            'noApsLineFailure':0,
            'csApsChannelMismatchBit':1,
            'csApsFEProtectionFailureBit':3,
            'csApsProtectionByteFailBit':2,
            'csApsModeMismatchBit':4,
        }


class CiscoSonetMib(object):
    """
    
    
    .. attribute:: csapsconfig
    
    	
    	**type**\:   :py:class:`Csapsconfig <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfig>`
    
    .. attribute:: csapsconfigtable
    
    	This table contains objects to configure APS  (Automatic Protection Switching) feature in a SONET  Line. APS is the ability to configure a pair of SONET  lines for redundancy so that the hardware will  automatically switch the active line from working line to the protection line or vice versa, within 60ms,  when the active line fails
    	**type**\:   :py:class:`Csapsconfigtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable>`
    
    .. attribute:: csau4tug3configtable
    
    	This table contains objects to configure the VC( Virtual Container) related properties of a TUG\-3 within a AU\-4  paths.  This table allows creation of following multiplexing structure\: STM\-1/AU\-4/TUG\-3/TU\-3/DS3 STM\-1/AU\-4/TUG\-3/TU\-3/E3 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-11/DS1 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-12/E1  Three entries are created in this table for a given AU\-4  path when cspSonetPathPayload object is set to one of the  following\:     vt15vc11(4),     vt2vc12(5),     ds3(3),     e3(8),     vtStructured(9)
    	**type**\:   :py:class:`Csau4Tug3Configtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csau4Tug3Configtable>`
    
    .. attribute:: csconfigtable
    
    	The SONET/SDH configuration table. This table has objects  for configuring sonet lines
    	**type**\:   :py:class:`Csconfigtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable>`
    
    .. attribute:: cslfarendtotaltable
    
    	The SONET/SDH Far End Line Total table. It contains the  cumulative sum of the various statistics for the 24 hour  period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the  line is enabled
    	**type**\:   :py:class:`Cslfarendtotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cslfarendtotaltable>`
    
    .. attribute:: csltotaltable
    
    	The SONET/SDH Line Total table. It contains the  cumulative sum of the various statistics for the 24  hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the line is enabled
    	**type**\:   :py:class:`Csltotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csltotaltable>`
    
    .. attribute:: csnotifications
    
    	
    	**type**\:   :py:class:`Csnotifications <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csnotifications>`
    
    .. attribute:: cspfarendtotaltable
    
    	The SONET/SDH Far End Path Total table. Far End is the  remote end of the line. The table contains the cumulative sum of the various statistics for the 24 hour period  preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\:   :py:class:`Cspfarendtotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cspfarendtotaltable>`
    
    .. attribute:: csptotaltable
    
    	The SONET/SDH Path Total table. It contains the cumulative  sum of the various statistics for the 24 hour period  preceding the current interval.The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is  enabled
    	**type**\:   :py:class:`Csptotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csptotaltable>`
    
    .. attribute:: csptracetable
    
    	The SONET/SDH Path Trace table. This table contains objects  for tracing the sonet path
    	**type**\:   :py:class:`Csptracetable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csptracetable>`
    
    .. attribute:: csstatstable
    
    	The SONET/SDH Section statistics table. This table  maintains the number of times the line encountered Loss of Signal(LOS), Loss of frame(LOF), Alarm Indication  signals(AISs), Remote failure indications(RFIs)
    	**type**\:   :py:class:`Csstatstable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstatstable>`
    
    .. attribute:: csstotaltable
    
    	The SONET/SDH Section Total table. It contains the  cumulative sum of the various statistics for the 24 hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\:   :py:class:`Csstotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstotaltable>`
    
    .. attribute:: csstracetable
    
    	The SONET/SDH Section Trace table. This table contains  objects for tracing the sonet section
    	**type**\:   :py:class:`Csstracetable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstracetable>`
    
    

    """

    _prefix = 'CISCO-SONET-MIB'
    _revision = '2003-03-07'

    def __init__(self):
        self.csapsconfig = CiscoSonetMib.Csapsconfig()
        self.csapsconfig.parent = self
        self.csapsconfigtable = CiscoSonetMib.Csapsconfigtable()
        self.csapsconfigtable.parent = self
        self.csau4tug3configtable = CiscoSonetMib.Csau4Tug3Configtable()
        self.csau4tug3configtable.parent = self
        self.csconfigtable = CiscoSonetMib.Csconfigtable()
        self.csconfigtable.parent = self
        self.cslfarendtotaltable = CiscoSonetMib.Cslfarendtotaltable()
        self.cslfarendtotaltable.parent = self
        self.csltotaltable = CiscoSonetMib.Csltotaltable()
        self.csltotaltable.parent = self
        self.csnotifications = CiscoSonetMib.Csnotifications()
        self.csnotifications.parent = self
        self.cspfarendtotaltable = CiscoSonetMib.Cspfarendtotaltable()
        self.cspfarendtotaltable.parent = self
        self.csptotaltable = CiscoSonetMib.Csptotaltable()
        self.csptotaltable.parent = self
        self.csptracetable = CiscoSonetMib.Csptracetable()
        self.csptracetable.parent = self
        self.csstatstable = CiscoSonetMib.Csstatstable()
        self.csstatstable.parent = self
        self.csstotaltable = CiscoSonetMib.Csstotaltable()
        self.csstotaltable.parent = self
        self.csstracetable = CiscoSonetMib.Csstracetable()
        self.csstracetable.parent = self


    class Csapsconfig(object):
        """
        
        
        .. attribute:: csapslinefailurecode
        
        	The object indicates the APS line failure code. This is the failure encountered by the APS line. Refer to CsApsLineFailureCode TC for failure code definitions. The object is used for notifications
        	**type**\:   :py:class:`CsapslinefailurecodeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsapslinefailurecodeEnum>`
        
        .. attribute:: csapslineswitchreason
        
        	This object indicates the APS line switch reason. When the working line on one end fails, its other end is told to do an APS switch.  Refer to CsApsLineSwitchReason TC for more information. The object is used for notifications
        	**type**\:   :py:class:`CsapslineswitchreasonEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsapslineswitchreasonEnum>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
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
            if self.csapslinefailurecode is not None:
                return True

            if self.csapslineswitchreason is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csapsconfig']['meta_info']


    class Csnotifications(object):
        """
        
        
        .. attribute:: csnotificationsenabled
        
        	This object controls if the generation of  ciscoSonetSectionStatusChange, ciscoSonetLineStatusChange,  ciscoSonetPathStatusChange and ciscoSonetVTStatusChange notifications is enabled. If the value of this object is 'true(1)', then all notifications in this MIB are enabled; otherwise they are disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
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
            if self.csnotificationsenabled is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csnotifications']['meta_info']


    class Csconfigtable(object):
        """
        The SONET/SDH configuration table. This table has objects 
        for configuring sonet lines.
        
        .. attribute:: csconfigentry
        
        	An entry in the table. There is an entry for each SONET line  in the table. Entries are automatically created for an  ifType value of sonet(39). 'ifAdminStatus' from the ifTable  must be used to enable or disable a line. A line is in  disabled(down) state unless provisioned 'up' using  'ifAdminStatus'
        	**type**\: list of    :py:class:`Csconfigentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csconfigentry = YList()
            self.csconfigentry.parent = self
            self.csconfigentry.name = 'csconfigentry'


        class Csconfigentry(object):
            """
            An entry in the table. There is an entry for each SONET line 
            in the table. Entries are automatically created for an 
            ifType value of sonet(39). 'ifAdminStatus' from the ifTable 
            must be used to enable or disable a line. A line is in 
            disabled(down) state unless provisioned 'up' using 
            'ifAdminStatus'.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csconfigframescramble
            
            	This object is used to disable or enable the Scrambling option in SONET line
            	**type**\:   :py:class:`CsconfigframescrambleEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigframescrambleEnum>`
            
            .. attribute:: csconfigloopbacktype
            
            	This object specifies the desired loopback mode configuration of the SONET line. The possible values of this objects are follows\:  noLoopback \:           Not in the loopback state.   lineLocal \:          The signal transmitted from this interface         is connected to the associated incoming         receiver. This ensures that the SONET frame         transmitted from the interface is received back         at the interface. lineRemote \:         The signal received at the interface is looped         back out to the associated transmitter.         This ensures that the remote equipment that         originated the signal receives it back. The          signal may undergo degradation as a result of         the characteristics of the transmission          medium
            	**type**\:   :py:class:`CsconfigloopbacktypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigloopbacktypeEnum>`
            
            .. attribute:: csconfigrdiptype
            
            	This object represents the type of RDI\-P (Remote Defect Indication \- Path) sent by this Network Element (NE) to remote Network Element.        onebit     \: use 1 bit RDI\-P       threebit   \: use 3 bit enhanced RDI\-P.  Default is onebit
            	**type**\:   :py:class:`CsconfigrdiptypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigrdiptypeEnum>`
            
            .. attribute:: csconfigrdivtype
            
            	This object specifies the type of RDI\-V (Remote Defect Indication \- Virtual Tributary/Container) sent by this  Network Element (NE) to the remote Network Element.        onebit     \: use 1 bit RDI\-V       threebit   \: use 3 bit enhanced RDI\-V.  Default is onebit
            	**type**\:   :py:class:`CsconfigrdivtypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigrdivtypeEnum>`
            
            .. attribute:: csconfigtype
            
            	This object represents the configured line type. Sts is SONET format. Stm is SDH format.      sonetSts3c   \: OC3 concatenated     sonetStm1    \: European standard OC3     sonetSts12c  \: OC12 concatenated     sonetStm4    \: European standard OC12     sonetSts48c  \: OC48 concatenated     sonetStm16   \: European standard OC48      sonetSts192c \: OC\-192 concatenated     sonetStm64   \: European standard OC\-192     sonetSts3    \: OC3 (unconcatenated)     
            	**type**\:   :py:class:`CsconfigtypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigtypeEnum>`
            
            .. attribute:: csconfigxmtclocksource
            
            	Specifies the source of the transmit clock.  loopTiming\: indicates that the recovered receive              clock is used as the transmit clock.  localTiming\: indicates that a local clock source is              used or that an external clock is               attached to the box containing the               interface. 
            	**type**\:   :py:class:`CsconfigxmtclocksourceEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigxmtclocksourceEnum>`
            
            .. attribute:: cssignallingtransportmode
            
            	This object represents the mode used to transport DS0  signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling is  transferred to the VT header. In clearMode(3), only the  framing bit is transferred to the VT header.       Default is signallingTransferMode(2) if csTributaryMappingType  is byteSynchronous. For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:   :py:class:`CssignallingtransportmodeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CssignallingtransportmodeEnum>`
            
            .. attribute:: cstributaryframingtype
            
            	This object represents the framing type to be assigned to the virtual tributaries in byte sync mapping mode.        notApplicable  \:  If VT mapping is not byteSynchronous(2).       dsx1ESF        \:  Extended Superframe Format       dsx1D4         \:  Superframe Format  Default is dsx1ESF(3) if csTributaryMappingType is  byteSynchronous(2). For asynchronous(1) mapping, the default is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:   :py:class:`CstributaryframingtypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CstributaryframingtypeEnum>`
            
            .. attribute:: cstributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.    au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.    au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  Default is au3Grouping(2) for SDH and notApplicable(1) for SONET
            	**type**\:   :py:class:`CstributarygroupingtypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarygroupingtypeEnum>`
            
            .. attribute:: cstributarymappingtype
            
            	This object represents the VT/VC mapping type.  asynchronous\:    In this mode, the channel structure of                   DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside the                  VT/VC can be found and extracted from the                  frame.  Default is asynchronous(1)
            	**type**\:   :py:class:`CstributarymappingtypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarymappingtypeEnum>`
            
            .. attribute:: cstributarytype
            
            	Type of the tributary carried within the SONET/SDH signal.  vt15vc11    \: carries T1 signal vt2vc12     \: carries E1 signal
            	**type**\:   :py:class:`CstributarytypeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarytypeEnum>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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

            class CsconfigframescrambleEnum(Enum):
                """
                CsconfigframescrambleEnum

                This object is used to disable or enable the Scrambling

                option in SONET line.

                .. data:: disabled = 1

                .. data:: enabled = 2

                """

                disabled = 1

                enabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigframescrambleEnum']


            class CsconfigloopbacktypeEnum(Enum):
                """
                CsconfigloopbacktypeEnum

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

                .. data:: noLoopback = 1

                .. data:: lineLocal = 2

                .. data:: lineRemote = 3

                """

                noLoopback = 1

                lineLocal = 2

                lineRemote = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigloopbacktypeEnum']


            class CsconfigrdiptypeEnum(Enum):
                """
                CsconfigrdiptypeEnum

                This object represents the type of RDI\-P (Remote Defect

                Indication \- Path) sent by this Network Element (NE)

                to remote Network Element.

                      onebit     \: use 1 bit RDI\-P

                      threebit   \: use 3 bit enhanced RDI\-P.

                Default is onebit.

                .. data:: onebit = 1

                .. data:: threebit = 3

                """

                onebit = 1

                threebit = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigrdiptypeEnum']


            class CsconfigrdivtypeEnum(Enum):
                """
                CsconfigrdivtypeEnum

                This object specifies the type of RDI\-V (Remote Defect

                Indication \- Virtual Tributary/Container) sent by this 

                Network Element (NE) to the remote Network Element.

                      onebit     \: use 1 bit RDI\-V

                      threebit   \: use 3 bit enhanced RDI\-V.

                Default is onebit.

                .. data:: onebit = 1

                .. data:: threebit = 3

                """

                onebit = 1

                threebit = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigrdivtypeEnum']


            class CsconfigtypeEnum(Enum):
                """
                CsconfigtypeEnum

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

                .. data:: sonetSts3c = 1

                .. data:: sonetStm1 = 2

                .. data:: sonetSts12c = 3

                .. data:: sonetStm4 = 4

                .. data:: sonetSts48c = 5

                .. data:: sonetStm16 = 6

                .. data:: sonetSts192c = 7

                .. data:: sonetStm64 = 8

                .. data:: sonetSts3 = 9

                """

                sonetSts3c = 1

                sonetStm1 = 2

                sonetSts12c = 3

                sonetStm4 = 4

                sonetSts48c = 5

                sonetStm16 = 6

                sonetSts192c = 7

                sonetStm64 = 8

                sonetSts3 = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigtypeEnum']


            class CsconfigxmtclocksourceEnum(Enum):
                """
                CsconfigxmtclocksourceEnum

                Specifies the source of the transmit clock.

                loopTiming\: indicates that the recovered receive 

                            clock is used as the transmit clock.

                localTiming\: indicates that a local clock source is

                             used or that an external clock is 

                             attached to the box containing the 

                             interface. 

                .. data:: loopTiming = 1

                .. data:: localTiming = 2

                """

                loopTiming = 1

                localTiming = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CsconfigxmtclocksourceEnum']


            class CssignallingtransportmodeEnum(Enum):
                """
                CssignallingtransportmodeEnum

                This object represents the mode used to transport DS0 

                signalling information for T1 byteSynchronous mapping (GR253).

                In signallingTransferMode(2), the robbed\-bit signalling is 

                transferred to the VT header. In clearMode(3), only the 

                framing bit is transferred to the VT header.

                Default is signallingTransferMode(2) if csTributaryMappingType 

                is byteSynchronous. For asynchronous mapping, it is 

                notApplicable(1).

                The value notApplicable(1) can not be set.

                .. data:: notApplicable = 1

                .. data:: signallingTransferMode = 2

                .. data:: clearMode = 3

                """

                notApplicable = 1

                signallingTransferMode = 2

                clearMode = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CssignallingtransportmodeEnum']


            class CstributaryframingtypeEnum(Enum):
                """
                CstributaryframingtypeEnum

                This object represents the framing type to be assigned to the

                virtual tributaries in byte sync mapping mode.

                      notApplicable  \:  If VT mapping is not byteSynchronous(2).

                      dsx1ESF        \:  Extended Superframe Format

                      dsx1D4         \:  Superframe Format

                Default is dsx1ESF(3) if csTributaryMappingType is 

                byteSynchronous(2). For asynchronous(1) mapping, the default is 

                notApplicable(1).

                The value notApplicable(1) can not be set.

                .. data:: notApplicable = 1

                .. data:: dsx1D4 = 2

                .. data:: dsx1ESF = 3

                """

                notApplicable = 1

                dsx1D4 = 2

                dsx1ESF = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CstributaryframingtypeEnum']


            class CstributarygroupingtypeEnum(Enum):
                """
                CstributarygroupingtypeEnum

                This object represents the method used to group VCs into an

                STM\-1 signal. Applicable only to SDH.

                  au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or

                               STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.

                  au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or

                               STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.

                Default is au3Grouping(2) for SDH and notApplicable(1) for SONET.

                .. data:: notApplicable = 1

                .. data:: au3Grouping = 2

                .. data:: au4Grouping = 3

                """

                notApplicable = 1

                au3Grouping = 2

                au4Grouping = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarygroupingtypeEnum']


            class CstributarymappingtypeEnum(Enum):
                """
                CstributarymappingtypeEnum

                This object represents the VT/VC mapping type.

                asynchronous\:    In this mode, the channel structure of 

                                 DS1/E1 is neither visible nor preserved.

                byteSynchronous\: In this mode, the DS0 signals inside the

                                 VT/VC can be found and extracted from the

                                 frame.

                Default is asynchronous(1).

                .. data:: asynchronous = 1

                .. data:: byteSynchronous = 2

                """

                asynchronous = 1

                byteSynchronous = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarymappingtypeEnum']


            class CstributarytypeEnum(Enum):
                """
                CstributarytypeEnum

                Type of the tributary carried within the SONET/SDH signal.

                vt15vc11    \: carries T1 signal

                vt2vc12     \: carries E1 signal

                .. data:: vt15vc11 = 1

                .. data:: vt2vc12 = 2

                """

                vt15vc11 = 1

                vt2vc12 = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry.CstributarytypeEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csConfigTable/CISCO-SONET-MIB:csConfigEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csconfigtable.Csconfigentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csconfigentry is not None:
                for child_ref in self.csconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csconfigtable']['meta_info']


    class Csapsconfigtable(object):
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
        	**type**\: list of    :py:class:`Csapsconfigentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csapsconfigentry = YList()
            self.csapsconfigentry.parent = self
            self.csapsconfigentry.name = 'csapsconfigentry'


        class Csapsconfigentry(object):
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
            
            .. attribute:: csapsworkingindex  <key>
            
            	When a pair of APS lines is configured, one line has to be the working line, which is the primary line, and the other has to be the protection line, which is the backup line. This object refers to the working line in the APS pair. For G.783 AnnexB, this index refers to Working Section 1
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsactiveline
            
            	This object indicates which line is currently active.  It could be the working line(Section 1 for Annex B), the protection line(Section 2 for Annex B) or none if neither working nor protection line is active.  This object reflects the status of receive direction
            	**type**\:   :py:class:`CsapsactivelineEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsactivelineEnum>`
            
            .. attribute:: csapsarchmode
            
            	This object is used to configure APS architecture mode on the working/protection line pairs.   All of the following are supported on single slot.  oneToOne(2) is not  supported across 2 slots,i.e. the   working and protection slot numbers must be the same in   oneToOne(2).   onePlusOne \: This can be supported on the same card  and across 2 cards.  This mode means that the transmit and receive signals  go only over the active line(which could be working or   protection line). (straight cable implied)   oneToOne \: This is supported only on the same card  This mode means that the transmit and receive signals  go over the working and protection lines.  (straight cable implied)   anexBOnePlusOne \: This can be supported on the same card  and across 2 cards.  This mode is like the onePlusOne mode, except that the  'csApsDirection' can only be bi\-directional.  (straight cable implied)   ycableOnePlusOneNok1k2\: With Y\-cable ignore K1K2 bytes.  This mode is the Y\-cable redundancy mode.   straightOnePlusOneNok1k2 \: With straight cable, ignore                              K1K2 bytes. This mode is like                             onePlusOne, but with K1, K2                              bytes ignored
            	**type**\:   :py:class:`CsapsarchmodeEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsarchmodeEnum>`
            
            .. attribute:: csapsarchmodeoperational
            
            	This object shows the actual APS architecture mode that is implemented on the Near End terminal. APS architecture mode configured through csApsArchMode object is  negotiated with the Far End through APS channel.  Architecture mode acceptable to both the Near End and  the Far End terminals is then operational at the Near  End. This value can be different than the APS  Architecture mode configured
            	**type**\:   :py:class:`CsapsarchmodeoperationalEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsarchmodeoperationalEnum>`
            
            .. attribute:: csapschannelprotocol
            
            	This object allows to configure APS channel protocol to  be implemented at Near End terminal.  K1 and K2 overhead bytes in a SONET signal are used as an APS channel. This channel is used to carry APS protocol.  Possible values\: bellcore(1) \: Implements APS channel protocol as defined               in bellcore document GR\-253\-CORE. itu(2) \: Implements APS channel protocol as defined in           ITU document G.783
            	**type**\:   :py:class:`CsapschannelprotocolEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapschannelprotocolEnum>`
            
            .. attribute:: csapsdirection
            
            	This object is used to configure the switching  direction which this APS line supports.   Unidirectional \: APS switch only in one direction. Bidirectional  \: APS switch in both ends of the line
            	**type**\:   :py:class:`CsapsdirectionEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsdirectionEnum>`
            
            .. attribute:: csapsdirectionoperational
            
            	This object shows the actual APS direction that is  implemented on the Near End terminal. APS direction  configured through csApsDirection is negotiated with the Far End and APS direction setting acceptable to  both ends is operational at the Near End
            	**type**\:   :py:class:`CsapsdirectionoperationalEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsdirectionoperationalEnum>`
            
            .. attribute:: csapsenable
            
            	This object is used to enable or disable the APS feature on the working/protection line pairs. When enabled, the hardware will automatically switch the active line  from the working line to the protection line within 60ms, or vice versa
            	**type**\:   :py:class:`CsapsenableEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsenableEnum>`
            
            .. attribute:: csapsfailurestatus
            
            	This object indicates APS line failure status
            	**type**\:   :py:class:`Csapslinefailurestatus <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.Csapslinefailurestatus>`
            
            .. attribute:: csapsprimarysection
            
            	This object indicates which working section is the APS primary section. In G.783 AnnexB, the K1/K2 Bytes are received on the secondary Section. All the Switch Requests are for a switch from the primary section to the secondary section. The object csApsActiveline will indicate which section is currently carrying the traffic.  Once the switch request clears normally, traffic is maintained on the section to which it was switched by making that section the primary section.   Possible values\:  workingSection1(1)\: Working Section 1 is Primary Section workingSection2(2)\: Working Section 2 is Primary Section none(3)           \: none
            	**type**\:   :py:class:`CsapsprimarysectionEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsprimarysectionEnum>`
            
            .. attribute:: csapsprotectionindex
            
            	The protection line indicates that it will become the active line when an APS switch occurs (APS switch could occur because of a failure on the working line). For G.783 AnnexB, This index refers to Working Section 2
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsrevertive
            
            	This object is used to configure the APS revertive or nonrevertive option.   revertive \:    Will switch the working line back to active state after   the Wait\-To\-restore interval has expired and the    working line Signal\-Fault/Signal\-Degrade has been    cleared. Please refer to 'csApsWaitToRestore' for    description of Wait\-To\-Restore interval. nonrevertive \:    The  protection line continues to be the active line,   The active line does not switch to the working line
            	**type**\:   :py:class:`CsapsrevertiveEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsrevertiveEnum>`
            
            .. attribute:: csapssigdegradeber
            
            	This object contains the Bit Error Rate threshold for Signal Degrade detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to \-n where n is between 5 and 9
            	**type**\:  int
            
            	**range:** 5..9
            
            .. attribute:: csapssigfaultber
            
            	This object contains the Bit Error Rate threshold for Signal Fault detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to the \-n, where n is between 3 and 5
            	**type**\:  int
            
            	**range:** 3..5
            
            .. attribute:: csapsswitchreason
            
            	This object indicates APS line switch reason
            	**type**\:   :py:class:`CsapslineswitchreasonEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsapslineswitchreasonEnum>`
            
            .. attribute:: csapswaittorestore
            
            	This object contains interval in minutes to wait  before attempting to switch back to working line.  Not applicable if the line is configured in  non\-revertive mode, i.e. protection line will  continue to be active, even if failures on the  working line are cleared. The framer clears the  signal\-fault and signal\-degrade when APS switch  occurs. Please refer to 'csApsRevertive' for  description of non\-revertive
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: minutes
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                self.csapsfailurestatus = Csapslinefailurestatus()
                self.csapsprimarysection = None
                self.csapsprotectionindex = None
                self.csapsrevertive = None
                self.csapssigdegradeber = None
                self.csapssigfaultber = None
                self.csapsswitchreason = None
                self.csapswaittorestore = None

            class CsapsactivelineEnum(Enum):
                """
                CsapsactivelineEnum

                This object indicates which line is currently active. 

                It could be the working line(Section 1 for Annex B),

                the protection line(Section 2 for Annex B) or none

                if neither working nor protection line is active. 

                This object reflects the status of receive direction.

                .. data:: csApsWorkingLine = 1

                .. data:: csApsProtectionLine = 2

                .. data:: csApsNone = 3

                """

                csApsWorkingLine = 1

                csApsProtectionLine = 2

                csApsNone = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsactivelineEnum']


            class CsapsarchmodeEnum(Enum):
                """
                CsapsarchmodeEnum

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

                .. data:: onePlusOne = 1

                .. data:: oneToOne = 2

                .. data:: anexBOnePlusOne = 3

                .. data:: ycableOnePlusOneNok1k2 = 4

                .. data:: straightOnePlusOneNok1k2 = 5

                """

                onePlusOne = 1

                oneToOne = 2

                anexBOnePlusOne = 3

                ycableOnePlusOneNok1k2 = 4

                straightOnePlusOneNok1k2 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsarchmodeEnum']


            class CsapsarchmodeoperationalEnum(Enum):
                """
                CsapsarchmodeoperationalEnum

                This object shows the actual APS architecture mode that

                is implemented on the Near End terminal. APS architecture

                mode configured through csApsArchMode object is 

                negotiated with the Far End through APS channel. 

                Architecture mode acceptable to both the Near End and 

                the Far End terminals is then operational at the Near 

                End. This value can be different than the APS 

                Architecture mode configured.

                .. data:: onePlusOne = 1

                .. data:: oneToOne = 2

                .. data:: anexBOnePlusOne = 3

                .. data:: ycableOnePlusOneNok1k2 = 4

                .. data:: straightOnePlusOneNok1k2 = 5

                """

                onePlusOne = 1

                oneToOne = 2

                anexBOnePlusOne = 3

                ycableOnePlusOneNok1k2 = 4

                straightOnePlusOneNok1k2 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsarchmodeoperationalEnum']


            class CsapschannelprotocolEnum(Enum):
                """
                CsapschannelprotocolEnum

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

                .. data:: bellcore = 1

                .. data:: itu = 2

                """

                bellcore = 1

                itu = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapschannelprotocolEnum']


            class CsapsdirectionEnum(Enum):
                """
                CsapsdirectionEnum

                This object is used to configure the switching 

                direction which this APS line supports. 

                Unidirectional \: APS switch only in one direction.

                Bidirectional  \: APS switch in both ends of the line.

                .. data:: uniDirectional = 1

                .. data:: biDirectional = 2

                """

                uniDirectional = 1

                biDirectional = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsdirectionEnum']


            class CsapsdirectionoperationalEnum(Enum):
                """
                CsapsdirectionoperationalEnum

                This object shows the actual APS direction that is 

                implemented on the Near End terminal. APS direction 

                configured through csApsDirection is negotiated with

                the Far End and APS direction setting acceptable to 

                both ends is operational at the Near End.

                .. data:: uniDirectional = 1

                .. data:: biDirectional = 2

                """

                uniDirectional = 1

                biDirectional = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsdirectionoperationalEnum']


            class CsapsenableEnum(Enum):
                """
                CsapsenableEnum

                This object is used to enable or disable the APS feature

                on the working/protection line pairs. When enabled,

                the hardware will automatically switch the active line 

                from the working line to the protection line within 60ms,

                or vice versa.

                .. data:: csApsDisabled = 1

                .. data:: csApsEnabled = 2

                """

                csApsDisabled = 1

                csApsEnabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsenableEnum']


            class CsapsprimarysectionEnum(Enum):
                """
                CsapsprimarysectionEnum

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

                .. data:: workingSection1 = 1

                .. data:: workingSection2 = 2

                .. data:: none = 3

                """

                workingSection1 = 1

                workingSection2 = 2

                none = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsprimarysectionEnum']


            class CsapsrevertiveEnum(Enum):
                """
                CsapsrevertiveEnum

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

                .. data:: nonrevertive = 1

                .. data:: revertive = 2

                """

                nonrevertive = 1

                revertive = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.CsapsrevertiveEnum']


            @property
            def _common_path(self):
                if self.csapsworkingindex is None:
                    raise YPYModelError('Key property csapsworkingindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csApsConfigTable/CISCO-SONET-MIB:csApsConfigEntry[CISCO-SONET-MIB:csApsWorkingIndex = ' + str(self.csapsworkingindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csapsconfigtable.Csapsconfigentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csApsConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csapsconfigentry is not None:
                for child_ref in self.csapsconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csapsconfigtable']['meta_info']


    class Csstotaltable(object):
        """
        The SONET/SDH Section Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the
        number of 15 minute intervals that have elapsed since
        the line is enabled. 
        
        .. attribute:: csstotalentry
        
        	An entry in the SONET/SDH Section Total table. Entries are created automatically for sonet lines
        	**type**\: list of    :py:class:`Csstotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstotaltable.Csstotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstotalentry = YList()
            self.csstotalentry.parent = self
            self.csstotalentry.name = 'csstotalentry'


        class Csstotalentry(object):
            """
            An entry in the SONET/SDH Section Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csstotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: csstotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Section in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csstotalsefss
            
            	The number of Severely Errored Framing Seconds  encountered by a SONET/SDH Section in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored framing seconds
            
            .. attribute:: csstotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTotalTable/CISCO-SONET-MIB:cssTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csstotaltable.Csstotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csstotalentry is not None:
                for child_ref in self.csstotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csstotaltable']['meta_info']


    class Csstracetable(object):
        """
        The SONET/SDH Section Trace table. This table contains 
        objects for tracing the sonet section.
        
        .. attribute:: csstraceentry
        
        	An entry in the trace table. Entries exist for active sonet lines. The objects in this table are used to verify  continued connection between the two ends of the line
        	**type**\: list of    :py:class:`Csstraceentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstracetable.Csstraceentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstraceentry = YList()
            self.csstraceentry.parent = self
            self.csstraceentry.name = 'csstraceentry'


        class Csstraceentry(object):
            """
            An entry in the trace table. Entries exist for active sonet
            lines. The objects in this table are used to verify 
            continued connection between the two ends of the line.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csstracefailure
            
            	The value of this object is set to 'true' when Sonet  Section received trace does not match the  'cssTraceToExpect'
            	**type**\:  bool
            
            .. attribute:: csstracereceived
            
            	This object is used to view the Sonet Section Trace that  is received by the receiving terminal
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csstracetoexpect
            
            	Sonet Section Trace To Expect. The receiving terminal  verifies if the incoming string matches this string.  The value of 'cssTraceFailure' indicates whether a  trace mismatch occurred. The default value is a  zero\-length string
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csstracetotransmit
            
            	Sonet Section Trace To Transmit. This is string that is transmitted to perform Sonet section trace  diagnostics. The trace string is  repetitively  transmited so that a trace receiving terminal can  verify its continued connection to the intended  transmitter. The default value is a zero\-length string. Unless this object is set to a non\-zero length string,  tracing will not be performed
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTraceTable/CISCO-SONET-MIB:cssTraceEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csstracetable.Csstraceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cssTraceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csstraceentry is not None:
                for child_ref in self.csstraceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csstracetable']['meta_info']


    class Csltotaltable(object):
        """
        The SONET/SDH Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 
        hour period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since
        the line is enabled.
        
        .. attribute:: csltotalentry
        
        	An entry in the SONET/SDH Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of    :py:class:`Csltotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csltotaltable.Csltotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csltotalentry = YList()
            self.csltotalentry.parent = self
            self.csltotalentry.name = 'csltotalentry'


        class Csltotalentry(object):
            """
            An entry in the SONET/SDH Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csltotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: csltotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csltotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: csltotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslTotalTable/CISCO-SONET-MIB:cslTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csltotaltable.Csltotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csltotalentry is not None:
                for child_ref in self.csltotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csltotaltable']['meta_info']


    class Cslfarendtotaltable(object):
        """
        The SONET/SDH Far End Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour 
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since the 
        line is enabled.
        
        .. attribute:: cslfarendtotalentry
        
        	An entry in the SONET/SDH Far End Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of    :py:class:`Cslfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.cslfarendtotalentry = YList()
            self.cslfarendtotalentry.parent = self
            self.cslfarendtotalentry.name = 'cslfarendtotalentry'


        class Cslfarendtotalentry(object):
            """
            An entry in the SONET/SDH Far End Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cslfarendtotalcvs
            
            	The number of Coding Violations encountered by a SONET/SDH  Far End Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: cslfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Far End Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: cslfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: cslfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslFarEndTotalTable/CISCO-SONET-MIB:cslFarEndTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cslFarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cslfarendtotalentry is not None:
                for child_ref in self.cslfarendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Cslfarendtotaltable']['meta_info']


    class Csptotaltable(object):
        """
        The SONET/SDH Path Total table. It contains the cumulative 
        sum of the various statistics for the 24 hour period 
        preceding the current interval.The object 
        'sonetMediumValidIntervals' from RFC2558 contains the number
        of 15 minute intervals that have elapsed since the line is 
        enabled.
        
        .. attribute:: csptotalentry
        
        	An entry in the SONET/SDH Path Total table. Entries are created automatically for sonet lines
        	**type**\: list of    :py:class:`Csptotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csptotaltable.Csptotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csptotalentry = YList()
            self.csptotalentry.parent = self
            self.csptotalentry.name = 'csptotalentry'


        class Csptotalentry(object):
            """
            An entry in the SONET/SDH Path Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csptotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: csptotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csptotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: csptotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTotalTable/CISCO-SONET-MIB:cspTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csptotaltable.Csptotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csptotalentry is not None:
                for child_ref in self.csptotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csptotaltable']['meta_info']


    class Cspfarendtotaltable(object):
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
        	**type**\: list of    :py:class:`Cspfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.cspfarendtotalentry = YList()
            self.cspfarendtotalentry.parent = self
            self.cspfarendtotalentry.name = 'cspfarendtotalentry'


        class Cspfarendtotalentry(object):
            """
            An entry in the SONET/SDH Far End Path Total table. 
            Entries are created automatically for sonet lines.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cspfarendtotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: cspfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH far end path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: cspfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: cspfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspFarEndTotalTable/CISCO-SONET-MIB:cspFarEndTotalEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspFarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cspfarendtotalentry is not None:
                for child_ref in self.cspfarendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Cspfarendtotaltable']['meta_info']


    class Csptracetable(object):
        """
        The SONET/SDH Path Trace table. This table contains objects 
        for tracing the sonet path.
        
        .. attribute:: csptraceentry
        
        	An entry in the SONET/SDH Path Trace table. The entries  exist for active sonet lines. The objects in this table are  used to verify continued connection between the two ends of the line
        	**type**\: list of    :py:class:`Csptraceentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csptracetable.Csptraceentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csptraceentry = YList()
            self.csptraceentry.parent = self
            self.csptraceentry.name = 'csptraceentry'


        class Csptraceentry(object):
            """
            An entry in the SONET/SDH Path Trace table. The entries 
            exist for active sonet lines. The objects in this table are 
            used to verify continued connection between the two ends of
            the line.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csptracefailure
            
            	The value of this object is set to 'true' when Sonet Path  received trace does not match the 'cspTraceToExpect'
            	**type**\:  bool
            
            .. attribute:: csptracereceived
            
            	This object is used to view the Sonet Path Trace that is received by the receiving terminal
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csptracetoexpect
            
            	Sonet Path Trace To Expect.  The receiving terminal verifies if the incoming string matches this string. The value of  'cspTraceFailure' indicates whether a trace mismatch  occured. The default value is a zero\-length string
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csptracetotransmit
            
            	Sonet Path Trace To Transmit. The trace string is  repetitively transmited so that a trace receiving terminal  can verify its continued receiving terminal can verify its  continued connection to the intended transmitter. The  default value is a zero\-length string. Unless this object  is set to a non\-zero length string, tracing will not be  performed
            	**type**\:  str
            
            	**length:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTraceTable/CISCO-SONET-MIB:cspTraceEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csptracetable.Csptraceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:cspTraceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csptraceentry is not None:
                for child_ref in self.csptraceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csptracetable']['meta_info']


    class Csstatstable(object):
        """
        The SONET/SDH Section statistics table. This table 
        maintains the number of times the line encountered Loss of
        Signal(LOS), Loss of frame(LOF), Alarm Indication 
        signals(AISs), Remote failure indications(RFIs).
        
        .. attribute:: csstatsentry
        
        	An entry in the SONET/SDH statistics table. These are  realtime statistics for the Sonet section, line and path layers. The statistics are gathered for each sonet line.  An entry is created automatically and is indexed by  ifIndex
        	**type**\: list of    :py:class:`Csstatsentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstatstable.Csstatsentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csstatsentry = YList()
            self.csstatsentry.parent = self
            self.csstatsentry.name = 'csstatsentry'


        class Csstatsentry(object):
            """
            An entry in the SONET/SDH statistics table. These are 
            realtime statistics for the Sonet section, line and path
            layers. The statistics are gathered for each sonet line. 
            An entry is created automatically and is indexed by 
            ifIndex.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cslaiss
            
            	The number of alarm indication signals(AIS)  encountered by  a SONET/SDH Line. A high value for this object may indicate a problem with the Sonet Line layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: alarm indication signals
            
            .. attribute:: cslrfis
            
            	The number of remote failure indications (RFI) encountered  by a SONET/SDH Line. A high value for this object may  indicate a problem with the Sonet Line layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: remote failure indications
            
            .. attribute:: cspaiss
            
            	The  number of alarm indication signals (AIS) encountered by a SONET/SDH Path. A high value for this object may  indicate a problem with the Sonet Path layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: alarm indication signals
            
            .. attribute:: csprfis
            
            	The number of  remote failure indications (RFI)  encountered by a SONET/SDH Path. A high value for this  object may indicate a problem with the Sonet Path layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: remote failure indications
            
            .. attribute:: csslofs
            
            	The number of Loss of Frames (LOF) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: loss of frames
            
            .. attribute:: cssloss
            
            	The number of Loss of signals(LOS) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: loss of signals
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
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
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csStatsTable/CISCO-SONET-MIB:csStatsEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csstatstable.Csstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csstatsentry is not None:
                for child_ref in self.csstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csstatstable']['meta_info']


    class Csau4Tug3Configtable(object):
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
        	**type**\: list of    :py:class:`Csau4Tug3Configentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            self.parent = None
            self.csau4tug3configentry = YList()
            self.csau4tug3configentry.parent = self
            self.csau4tug3configentry.name = 'csau4tug3configentry'


        class Csau4Tug3Configentry(object):
            """
            There is an entry in this table for each TUG\-3 within a 
            AU\-4 SDH path that supports SDH virtual container VC\-4.
            The ifIndex value represents an entry in ifTable with
            ifType = sonetPath(50).The ifTable entry applicable for
            this entry belongs to AU\-4 path.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csau4tug3  <key>
            
            	This object represents the TUG\-3 number
            	**type**\:  int
            
            	**range:** 1..3
            
            .. attribute:: csau4tug3payload
            
            	This object is used for configuring the payload for the tributary group.  The possible values are \:  vc11   \: When set to 'vc11' following things are done\:        \- 28 entries created in ifTable for TU\-11 with           ifType = sonetVT(51)        \- 28 entries created in ifTable for DS1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11  vc12   \: When set to 'vc12' following things are done\:        \- 21 entries created in ifTable for TU\-12 with           ifType = sonetVT(51)        \- 21 entries created in ifTable for E1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12  tu3ds3 \: When set to 'tu3ds3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for DS3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  tu3e3  \: When set to 'tu3e3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for E3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  The value 'other' can not be set
            	**type**\:   :py:class:`Csau4Tug3PayloadEnum <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry.Csau4Tug3PayloadEnum>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.csau4tug3 = None
                self.csau4tug3payload = None

            class Csau4Tug3PayloadEnum(Enum):
                """
                Csau4Tug3PayloadEnum

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

                .. data:: other = 1

                .. data:: vc11 = 2

                .. data:: vc12 = 3

                .. data:: tu3ds3 = 4

                .. data:: tu3e3 = 5

                """

                other = 1

                vc11 = 2

                vc12 = 3

                tu3ds3 = 4

                tu3e3 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                    return meta._meta_table['CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry.Csau4Tug3PayloadEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.csau4tug3 is None:
                    raise YPYModelError('Key property csau4tug3 is None')

                return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csAu4Tug3ConfigTable/CISCO-SONET-MIB:csAu4Tug3ConfigEntry[CISCO-SONET-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-SONET-MIB:csAu4Tug3 = ' + str(self.csau4tug3) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.csau4tug3 is not None:
                    return True

                if self.csau4tug3payload is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
                return meta._meta_table['CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SONET-MIB:CISCO-SONET-MIB/CISCO-SONET-MIB:csAu4Tug3ConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csau4tug3configentry is not None:
                for child_ref in self.csau4tug3configentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
            return meta._meta_table['CiscoSonetMib.Csau4Tug3Configtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-SONET-MIB:CISCO-SONET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.csapsconfig is not None and self.csapsconfig._has_data():
            return True

        if self.csapsconfigtable is not None and self.csapsconfigtable._has_data():
            return True

        if self.csau4tug3configtable is not None and self.csau4tug3configtable._has_data():
            return True

        if self.csconfigtable is not None and self.csconfigtable._has_data():
            return True

        if self.cslfarendtotaltable is not None and self.cslfarendtotaltable._has_data():
            return True

        if self.csltotaltable is not None and self.csltotaltable._has_data():
            return True

        if self.csnotifications is not None and self.csnotifications._has_data():
            return True

        if self.cspfarendtotaltable is not None and self.cspfarendtotaltable._has_data():
            return True

        if self.csptotaltable is not None and self.csptotaltable._has_data():
            return True

        if self.csptracetable is not None and self.csptracetable._has_data():
            return True

        if self.csstatstable is not None and self.csstatstable._has_data():
            return True

        if self.csstotaltable is not None and self.csstotaltable._has_data():
            return True

        if self.csstracetable is not None and self.csstracetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SONET_MIB as meta
        return meta._meta_table['CiscoSonetMib']['meta_info']


