""" CISCO_SONET_MIB 

The MIB module to describe SONET/SDH interfaces
objects. This is an extension to the standard SONET 
MIB(RFC 2558).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CsApsLineFailureCode(Enum):
    """
    CsApsLineFailureCode (Enum Class)

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

    csApsChannelMismatch = Enum.YLeaf(1, "csApsChannelMismatch")

    csApsProtectionByteFail = Enum.YLeaf(2, "csApsProtectionByteFail")

    csApsFEProtectionFailure = Enum.YLeaf(3, "csApsFEProtectionFailure")

    csApsModeMismatch = Enum.YLeaf(4, "csApsModeMismatch")


class CsApsLineSwitchReason(Enum):
    """
    CsApsLineSwitchReason (Enum Class)

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

    csApsOther = Enum.YLeaf(1, "csApsOther")

    csApsRevertive = Enum.YLeaf(2, "csApsRevertive")

    csApsManual = Enum.YLeaf(3, "csApsManual")

    csApsSignalDefectLow = Enum.YLeaf(4, "csApsSignalDefectLow")

    csApsSignalDefectHigh = Enum.YLeaf(5, "csApsSignalDefectHigh")

    csApsSignalFailureLow = Enum.YLeaf(6, "csApsSignalFailureLow")

    csApsSignalFailureHigh = Enum.YLeaf(7, "csApsSignalFailureHigh")

    csApsForceSwitch = Enum.YLeaf(8, "csApsForceSwitch")

    csApsLockOut = Enum.YLeaf(9, "csApsLockOut")

    csApsNoSwitch = Enum.YLeaf(10, "csApsNoSwitch")



class CISCOSONETMIB(Entity):
    """
    
    
    .. attribute:: csapsconfig
    
    	
    	**type**\:  :py:class:`Csapsconfig <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfig>`
    
    .. attribute:: csnotifications
    
    	
    	**type**\:  :py:class:`Csnotifications <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csnotifications>`
    
    .. attribute:: csconfigtable
    
    	The SONET/SDH configuration table. This table has objects  for configuring sonet lines
    	**type**\:  :py:class:`Csconfigtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable>`
    
    .. attribute:: csapsconfigtable
    
    	This table contains objects to configure APS  (Automatic Protection Switching) feature in a SONET  Line. APS is the ability to configure a pair of SONET  lines for redundancy so that the hardware will  automatically switch the active line from working line to the protection line or vice versa, within 60ms,  when the active line fails
    	**type**\:  :py:class:`Csapsconfigtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable>`
    
    .. attribute:: csstotaltable
    
    	The SONET/SDH Section Total table. It contains the  cumulative sum of the various statistics for the 24 hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\:  :py:class:`Csstotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstotaltable>`
    
    .. attribute:: csstracetable
    
    	The SONET/SDH Section Trace table. This table contains  objects for tracing the sonet section
    	**type**\:  :py:class:`Csstracetable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstracetable>`
    
    .. attribute:: csltotaltable
    
    	The SONET/SDH Line Total table. It contains the  cumulative sum of the various statistics for the 24  hour period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the line is enabled
    	**type**\:  :py:class:`Csltotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csltotaltable>`
    
    .. attribute:: cslfarendtotaltable
    
    	The SONET/SDH Far End Line Total table. It contains the  cumulative sum of the various statistics for the 24 hour  period preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the  number of 15 minute intervals that have elapsed since the  line is enabled
    	**type**\:  :py:class:`Cslfarendtotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Cslfarendtotaltable>`
    
    .. attribute:: csptotaltable
    
    	The SONET/SDH Path Total table. It contains the cumulative  sum of the various statistics for the 24 hour period  preceding the current interval.The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is  enabled
    	**type**\:  :py:class:`Csptotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csptotaltable>`
    
    .. attribute:: cspfarendtotaltable
    
    	The SONET/SDH Far End Path Total table. Far End is the  remote end of the line. The table contains the cumulative sum of the various statistics for the 24 hour period  preceding the current interval. The object  'sonetMediumValidIntervals' from RFC2558 contains the number of 15 minute intervals that have elapsed since the line is enabled. 
    	**type**\:  :py:class:`Cspfarendtotaltable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Cspfarendtotaltable>`
    
    .. attribute:: csptracetable
    
    	The SONET/SDH Path Trace table. This table contains objects  for tracing the sonet path
    	**type**\:  :py:class:`Csptracetable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csptracetable>`
    
    .. attribute:: csstatstable
    
    	The SONET/SDH Section statistics table. This table  maintains the number of times the line encountered Loss of Signal(LOS), Loss of frame(LOF), Alarm Indication  signals(AISs), Remote failure indications(RFIs)
    	**type**\:  :py:class:`Csstatstable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstatstable>`
    
    .. attribute:: csau4tug3configtable
    
    	This table contains objects to configure the VC( Virtual Container) related properties of a TUG\-3 within a AU\-4  paths.  This table allows creation of following multiplexing structure\: STM\-1/AU\-4/TUG\-3/TU\-3/DS3 STM\-1/AU\-4/TUG\-3/TU\-3/E3 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-11/DS1 STM\-1/AU\-4/TUG\-3/TUG\-2/TU\-12/E1  Three entries are created in this table for a given AU\-4  path when cspSonetPathPayload object is set to one of the  following\:     vt15vc11(4),     vt2vc12(5),     ds3(3),     e3(8),     vtStructured(9)
    	**type**\:  :py:class:`Csau4Tug3Configtable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csau4Tug3Configtable>`
    
    

    """

    _prefix = 'CISCO-SONET-MIB'
    _revision = '2003-03-07'

    def __init__(self):
        super(CISCOSONETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SONET-MIB"
        self.yang_parent_name = "CISCO-SONET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("csApsConfig", ("csapsconfig", CISCOSONETMIB.Csapsconfig)), ("csNotifications", ("csnotifications", CISCOSONETMIB.Csnotifications)), ("csConfigTable", ("csconfigtable", CISCOSONETMIB.Csconfigtable)), ("csApsConfigTable", ("csapsconfigtable", CISCOSONETMIB.Csapsconfigtable)), ("cssTotalTable", ("csstotaltable", CISCOSONETMIB.Csstotaltable)), ("cssTraceTable", ("csstracetable", CISCOSONETMIB.Csstracetable)), ("cslTotalTable", ("csltotaltable", CISCOSONETMIB.Csltotaltable)), ("cslFarEndTotalTable", ("cslfarendtotaltable", CISCOSONETMIB.Cslfarendtotaltable)), ("cspTotalTable", ("csptotaltable", CISCOSONETMIB.Csptotaltable)), ("cspFarEndTotalTable", ("cspfarendtotaltable", CISCOSONETMIB.Cspfarendtotaltable)), ("cspTraceTable", ("csptracetable", CISCOSONETMIB.Csptracetable)), ("csStatsTable", ("csstatstable", CISCOSONETMIB.Csstatstable)), ("csAu4Tug3ConfigTable", ("csau4tug3configtable", CISCOSONETMIB.Csau4Tug3Configtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.csapsconfig = CISCOSONETMIB.Csapsconfig()
        self.csapsconfig.parent = self
        self._children_name_map["csapsconfig"] = "csApsConfig"
        self._children_yang_names.add("csApsConfig")

        self.csnotifications = CISCOSONETMIB.Csnotifications()
        self.csnotifications.parent = self
        self._children_name_map["csnotifications"] = "csNotifications"
        self._children_yang_names.add("csNotifications")

        self.csconfigtable = CISCOSONETMIB.Csconfigtable()
        self.csconfigtable.parent = self
        self._children_name_map["csconfigtable"] = "csConfigTable"
        self._children_yang_names.add("csConfigTable")

        self.csapsconfigtable = CISCOSONETMIB.Csapsconfigtable()
        self.csapsconfigtable.parent = self
        self._children_name_map["csapsconfigtable"] = "csApsConfigTable"
        self._children_yang_names.add("csApsConfigTable")

        self.csstotaltable = CISCOSONETMIB.Csstotaltable()
        self.csstotaltable.parent = self
        self._children_name_map["csstotaltable"] = "cssTotalTable"
        self._children_yang_names.add("cssTotalTable")

        self.csstracetable = CISCOSONETMIB.Csstracetable()
        self.csstracetable.parent = self
        self._children_name_map["csstracetable"] = "cssTraceTable"
        self._children_yang_names.add("cssTraceTable")

        self.csltotaltable = CISCOSONETMIB.Csltotaltable()
        self.csltotaltable.parent = self
        self._children_name_map["csltotaltable"] = "cslTotalTable"
        self._children_yang_names.add("cslTotalTable")

        self.cslfarendtotaltable = CISCOSONETMIB.Cslfarendtotaltable()
        self.cslfarendtotaltable.parent = self
        self._children_name_map["cslfarendtotaltable"] = "cslFarEndTotalTable"
        self._children_yang_names.add("cslFarEndTotalTable")

        self.csptotaltable = CISCOSONETMIB.Csptotaltable()
        self.csptotaltable.parent = self
        self._children_name_map["csptotaltable"] = "cspTotalTable"
        self._children_yang_names.add("cspTotalTable")

        self.cspfarendtotaltable = CISCOSONETMIB.Cspfarendtotaltable()
        self.cspfarendtotaltable.parent = self
        self._children_name_map["cspfarendtotaltable"] = "cspFarEndTotalTable"
        self._children_yang_names.add("cspFarEndTotalTable")

        self.csptracetable = CISCOSONETMIB.Csptracetable()
        self.csptracetable.parent = self
        self._children_name_map["csptracetable"] = "cspTraceTable"
        self._children_yang_names.add("cspTraceTable")

        self.csstatstable = CISCOSONETMIB.Csstatstable()
        self.csstatstable.parent = self
        self._children_name_map["csstatstable"] = "csStatsTable"
        self._children_yang_names.add("csStatsTable")

        self.csau4tug3configtable = CISCOSONETMIB.Csau4Tug3Configtable()
        self.csau4tug3configtable.parent = self
        self._children_name_map["csau4tug3configtable"] = "csAu4Tug3ConfigTable"
        self._children_yang_names.add("csAu4Tug3ConfigTable")
        self._segment_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB"


    class Csapsconfig(Entity):
        """
        
        
        .. attribute:: csapslinefailurecode
        
        	The object indicates the APS line failure code. This is the failure encountered by the APS line. Refer to CsApsLineFailureCode TC for failure code definitions. The object is used for notifications
        	**type**\:  :py:class:`CsApsLineFailureCode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsApsLineFailureCode>`
        
        .. attribute:: csapslineswitchreason
        
        	This object indicates the APS line switch reason. When the working line on one end fails, its other end is told to do an APS switch.  Refer to CsApsLineSwitchReason TC for more information. The object is used for notifications
        	**type**\:  :py:class:`CsApsLineSwitchReason <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsApsLineSwitchReason>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csapsconfig, self).__init__()

            self.yang_name = "csApsConfig"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csapslinefailurecode', YLeaf(YType.enumeration, 'csApsLineFailureCode')),
                ('csapslineswitchreason', YLeaf(YType.enumeration, 'csApsLineSwitchReason')),
            ])
            self.csapslinefailurecode = None
            self.csapslineswitchreason = None
            self._segment_path = lambda: "csApsConfig"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csapsconfig, ['csapslinefailurecode', 'csapslineswitchreason'], name, value)


    class Csnotifications(Entity):
        """
        
        
        .. attribute:: csnotificationsenabled
        
        	This object controls if the generation of  ciscoSonetSectionStatusChange, ciscoSonetLineStatusChange,  ciscoSonetPathStatusChange and ciscoSonetVTStatusChange notifications is enabled. If the value of this object is 'true(1)', then all notifications in this MIB are enabled; otherwise they are disabled
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csnotifications, self).__init__()

            self.yang_name = "csNotifications"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csnotificationsenabled', YLeaf(YType.boolean, 'csNotificationsEnabled')),
            ])
            self.csnotificationsenabled = None
            self._segment_path = lambda: "csNotifications"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csnotifications, ['csnotificationsenabled'], name, value)


    class Csconfigtable(Entity):
        """
        The SONET/SDH configuration table. This table has objects 
        for configuring sonet lines.
        
        .. attribute:: csconfigentry
        
        	An entry in the table. There is an entry for each SONET line  in the table. Entries are automatically created for an  ifType value of sonet(39). 'ifAdminStatus' from the ifTable  must be used to enable or disable a line. A line is in  disabled(down) state unless provisioned 'up' using  'ifAdminStatus'
        	**type**\: list of  		 :py:class:`Csconfigentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csconfigtable, self).__init__()

            self.yang_name = "csConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csConfigEntry", ("csconfigentry", CISCOSONETMIB.Csconfigtable.Csconfigentry))])
            self._leafs = OrderedDict()

            self.csconfigentry = YList(self)
            self._segment_path = lambda: "csConfigTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csconfigtable, [], name, value)


        class Csconfigentry(Entity):
            """
            An entry in the table. There is an entry for each SONET line 
            in the table. Entries are automatically created for an 
            ifType value of sonet(39). 'ifAdminStatus' from the ifTable 
            must be used to enable or disable a line. A line is in 
            disabled(down) state unless provisioned 'up' using 
            'ifAdminStatus'.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csconfigloopbacktype
            
            	This object specifies the desired loopback mode configuration of the SONET line. The possible values of this objects are follows\:  noLoopback \:           Not in the loopback state.   lineLocal \:          The signal transmitted from this interface         is connected to the associated incoming         receiver. This ensures that the SONET frame         transmitted from the interface is received back         at the interface. lineRemote \:         The signal received at the interface is looped         back out to the associated transmitter.         This ensures that the remote equipment that         originated the signal receives it back. The          signal may undergo degradation as a result of         the characteristics of the transmission          medium
            	**type**\:  :py:class:`Csconfigloopbacktype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigloopbacktype>`
            
            .. attribute:: csconfigxmtclocksource
            
            	Specifies the source of the transmit clock.  loopTiming\: indicates that the recovered receive              clock is used as the transmit clock.  localTiming\: indicates that a local clock source is              used or that an external clock is               attached to the box containing the               interface. 
            	**type**\:  :py:class:`Csconfigxmtclocksource <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigxmtclocksource>`
            
            .. attribute:: csconfigframescramble
            
            	This object is used to disable or enable the Scrambling option in SONET line
            	**type**\:  :py:class:`Csconfigframescramble <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigframescramble>`
            
            .. attribute:: csconfigtype
            
            	This object represents the configured line type. Sts is SONET format. Stm is SDH format.      sonetSts3c   \: OC3 concatenated     sonetStm1    \: European standard OC3     sonetSts12c  \: OC12 concatenated     sonetStm4    \: European standard OC12     sonetSts48c  \: OC48 concatenated     sonetStm16   \: European standard OC48      sonetSts192c \: OC\-192 concatenated     sonetStm64   \: European standard OC\-192     sonetSts3    \: OC3 (unconcatenated)     
            	**type**\:  :py:class:`Csconfigtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigtype>`
            
            .. attribute:: csconfigrdivtype
            
            	This object specifies the type of RDI\-V (Remote Defect Indication \- Virtual Tributary/Container) sent by this  Network Element (NE) to the remote Network Element.        onebit     \: use 1 bit RDI\-V       threebit   \: use 3 bit enhanced RDI\-V.  Default is onebit
            	**type**\:  :py:class:`Csconfigrdivtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigrdivtype>`
            
            .. attribute:: csconfigrdiptype
            
            	This object represents the type of RDI\-P (Remote Defect Indication \- Path) sent by this Network Element (NE) to remote Network Element.        onebit     \: use 1 bit RDI\-P       threebit   \: use 3 bit enhanced RDI\-P.  Default is onebit
            	**type**\:  :py:class:`Csconfigrdiptype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Csconfigrdiptype>`
            
            .. attribute:: cstributarytype
            
            	Type of the tributary carried within the SONET/SDH signal.  vt15vc11    \: carries T1 signal vt2vc12     \: carries E1 signal
            	**type**\:  :py:class:`Cstributarytype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Cstributarytype>`
            
            .. attribute:: cstributarymappingtype
            
            	This object represents the VT/VC mapping type.  asynchronous\:    In this mode, the channel structure of                   DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside the                  VT/VC can be found and extracted from the                  frame.  Default is asynchronous(1)
            	**type**\:  :py:class:`Cstributarymappingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Cstributarymappingtype>`
            
            .. attribute:: cstributaryframingtype
            
            	This object represents the framing type to be assigned to the virtual tributaries in byte sync mapping mode.        notApplicable  \:  If VT mapping is not byteSynchronous(2).       dsx1ESF        \:  Extended Superframe Format       dsx1D4         \:  Superframe Format  Default is dsx1ESF(3) if csTributaryMappingType is  byteSynchronous(2). For asynchronous(1) mapping, the default is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:  :py:class:`Cstributaryframingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Cstributaryframingtype>`
            
            .. attribute:: cssignallingtransportmode
            
            	This object represents the mode used to transport DS0  signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling is  transferred to the VT header. In clearMode(3), only the  framing bit is transferred to the VT header.       Default is signallingTransferMode(2) if csTributaryMappingType  is byteSynchronous. For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:  :py:class:`Cssignallingtransportmode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Cssignallingtransportmode>`
            
            .. attribute:: cstributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.    au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.    au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  Default is au3Grouping(2) for SDH and notApplicable(1) for SONET
            	**type**\:  :py:class:`Cstributarygroupingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csconfigtable.Csconfigentry.Cstributarygroupingtype>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csconfigtable.Csconfigentry, self).__init__()

                self.yang_name = "csConfigEntry"
                self.yang_parent_name = "csConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csconfigloopbacktype', YLeaf(YType.enumeration, 'csConfigLoopbackType')),
                    ('csconfigxmtclocksource', YLeaf(YType.enumeration, 'csConfigXmtClockSource')),
                    ('csconfigframescramble', YLeaf(YType.enumeration, 'csConfigFrameScramble')),
                    ('csconfigtype', YLeaf(YType.enumeration, 'csConfigType')),
                    ('csconfigrdivtype', YLeaf(YType.enumeration, 'csConfigRDIVType')),
                    ('csconfigrdiptype', YLeaf(YType.enumeration, 'csConfigRDIPType')),
                    ('cstributarytype', YLeaf(YType.enumeration, 'csTributaryType')),
                    ('cstributarymappingtype', YLeaf(YType.enumeration, 'csTributaryMappingType')),
                    ('cstributaryframingtype', YLeaf(YType.enumeration, 'csTributaryFramingType')),
                    ('cssignallingtransportmode', YLeaf(YType.enumeration, 'csSignallingTransportMode')),
                    ('cstributarygroupingtype', YLeaf(YType.enumeration, 'csTributaryGroupingType')),
                ])
                self.ifindex = None
                self.csconfigloopbacktype = None
                self.csconfigxmtclocksource = None
                self.csconfigframescramble = None
                self.csconfigtype = None
                self.csconfigrdivtype = None
                self.csconfigrdiptype = None
                self.cstributarytype = None
                self.cstributarymappingtype = None
                self.cstributaryframingtype = None
                self.cssignallingtransportmode = None
                self.cstributarygroupingtype = None
                self._segment_path = lambda: "csConfigEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/csConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csconfigtable.Csconfigentry, ['ifindex', 'csconfigloopbacktype', 'csconfigxmtclocksource', 'csconfigframescramble', 'csconfigtype', 'csconfigrdivtype', 'csconfigrdiptype', 'cstributarytype', 'cstributarymappingtype', 'cstributaryframingtype', 'cssignallingtransportmode', 'cstributarygroupingtype'], name, value)

            class Csconfigframescramble(Enum):
                """
                Csconfigframescramble (Enum Class)

                This object is used to disable or enable the Scrambling

                option in SONET line.

                .. data:: disabled = 1

                .. data:: enabled = 2

                """

                disabled = Enum.YLeaf(1, "disabled")

                enabled = Enum.YLeaf(2, "enabled")


            class Csconfigloopbacktype(Enum):
                """
                Csconfigloopbacktype (Enum Class)

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

                noLoopback = Enum.YLeaf(1, "noLoopback")

                lineLocal = Enum.YLeaf(2, "lineLocal")

                lineRemote = Enum.YLeaf(3, "lineRemote")


            class Csconfigrdiptype(Enum):
                """
                Csconfigrdiptype (Enum Class)

                This object represents the type of RDI\-P (Remote Defect

                Indication \- Path) sent by this Network Element (NE)

                to remote Network Element.

                      onebit     \: use 1 bit RDI\-P

                      threebit   \: use 3 bit enhanced RDI\-P.

                Default is onebit.

                .. data:: onebit = 1

                .. data:: threebit = 3

                """

                onebit = Enum.YLeaf(1, "onebit")

                threebit = Enum.YLeaf(3, "threebit")


            class Csconfigrdivtype(Enum):
                """
                Csconfigrdivtype (Enum Class)

                This object specifies the type of RDI\-V (Remote Defect

                Indication \- Virtual Tributary/Container) sent by this 

                Network Element (NE) to the remote Network Element.

                      onebit     \: use 1 bit RDI\-V

                      threebit   \: use 3 bit enhanced RDI\-V.

                Default is onebit.

                .. data:: onebit = 1

                .. data:: threebit = 3

                """

                onebit = Enum.YLeaf(1, "onebit")

                threebit = Enum.YLeaf(3, "threebit")


            class Csconfigtype(Enum):
                """
                Csconfigtype (Enum Class)

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

                sonetSts3c = Enum.YLeaf(1, "sonetSts3c")

                sonetStm1 = Enum.YLeaf(2, "sonetStm1")

                sonetSts12c = Enum.YLeaf(3, "sonetSts12c")

                sonetStm4 = Enum.YLeaf(4, "sonetStm4")

                sonetSts48c = Enum.YLeaf(5, "sonetSts48c")

                sonetStm16 = Enum.YLeaf(6, "sonetStm16")

                sonetSts192c = Enum.YLeaf(7, "sonetSts192c")

                sonetStm64 = Enum.YLeaf(8, "sonetStm64")

                sonetSts3 = Enum.YLeaf(9, "sonetSts3")


            class Csconfigxmtclocksource(Enum):
                """
                Csconfigxmtclocksource (Enum Class)

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

                loopTiming = Enum.YLeaf(1, "loopTiming")

                localTiming = Enum.YLeaf(2, "localTiming")


            class Cssignallingtransportmode(Enum):
                """
                Cssignallingtransportmode (Enum Class)

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

                notApplicable = Enum.YLeaf(1, "notApplicable")

                signallingTransferMode = Enum.YLeaf(2, "signallingTransferMode")

                clearMode = Enum.YLeaf(3, "clearMode")


            class Cstributaryframingtype(Enum):
                """
                Cstributaryframingtype (Enum Class)

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

                notApplicable = Enum.YLeaf(1, "notApplicable")

                dsx1D4 = Enum.YLeaf(2, "dsx1D4")

                dsx1ESF = Enum.YLeaf(3, "dsx1ESF")


            class Cstributarygroupingtype(Enum):
                """
                Cstributarygroupingtype (Enum Class)

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

                notApplicable = Enum.YLeaf(1, "notApplicable")

                au3Grouping = Enum.YLeaf(2, "au3Grouping")

                au4Grouping = Enum.YLeaf(3, "au4Grouping")


            class Cstributarymappingtype(Enum):
                """
                Cstributarymappingtype (Enum Class)

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

                asynchronous = Enum.YLeaf(1, "asynchronous")

                byteSynchronous = Enum.YLeaf(2, "byteSynchronous")


            class Cstributarytype(Enum):
                """
                Cstributarytype (Enum Class)

                Type of the tributary carried within the SONET/SDH signal.

                vt15vc11    \: carries T1 signal

                vt2vc12     \: carries E1 signal

                .. data:: vt15vc11 = 1

                .. data:: vt2vc12 = 2

                """

                vt15vc11 = Enum.YLeaf(1, "vt15vc11")

                vt2vc12 = Enum.YLeaf(2, "vt2vc12")



    class Csapsconfigtable(Entity):
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
        	**type**\: list of  		 :py:class:`Csapsconfigentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csapsconfigtable, self).__init__()

            self.yang_name = "csApsConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csApsConfigEntry", ("csapsconfigentry", CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry))])
            self._leafs = OrderedDict()

            self.csapsconfigentry = YList(self)
            self._segment_path = lambda: "csApsConfigTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csapsconfigtable, [], name, value)


        class Csapsconfigentry(Entity):
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
            
            .. attribute:: csapsworkingindex  (key)
            
            	When a pair of APS lines is configured, one line has to be the working line, which is the primary line, and the other has to be the protection line, which is the backup line. This object refers to the working line in the APS pair. For G.783 AnnexB, this index refers to Working Section 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsprotectionindex
            
            	The protection line indicates that it will become the active line when an APS switch occurs (APS switch could occur because of a failure on the working line). For G.783 AnnexB, This index refers to Working Section 2
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsenable
            
            	This object is used to enable or disable the APS feature on the working/protection line pairs. When enabled, the hardware will automatically switch the active line  from the working line to the protection line within 60ms, or vice versa
            	**type**\:  :py:class:`Csapsenable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsenable>`
            
            .. attribute:: csapsarchmode
            
            	This object is used to configure APS architecture mode on the working/protection line pairs.   All of the following are supported on single slot.  oneToOne(2) is not  supported across 2 slots,i.e. the   working and protection slot numbers must be the same in   oneToOne(2).   onePlusOne \: This can be supported on the same card  and across 2 cards.  This mode means that the transmit and receive signals  go only over the active line(which could be working or   protection line). (straight cable implied)   oneToOne \: This is supported only on the same card  This mode means that the transmit and receive signals  go over the working and protection lines.  (straight cable implied)   anexBOnePlusOne \: This can be supported on the same card  and across 2 cards.  This mode is like the onePlusOne mode, except that the  'csApsDirection' can only be bi\-directional.  (straight cable implied)   ycableOnePlusOneNok1k2\: With Y\-cable ignore K1K2 bytes.  This mode is the Y\-cable redundancy mode.   straightOnePlusOneNok1k2 \: With straight cable, ignore                              K1K2 bytes. This mode is like                             onePlusOne, but with K1, K2                              bytes ignored
            	**type**\:  :py:class:`Csapsarchmode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsarchmode>`
            
            .. attribute:: csapsactiveline
            
            	This object indicates which line is currently active.  It could be the working line(Section 1 for Annex B), the protection line(Section 2 for Annex B) or none if neither working nor protection line is active.  This object reflects the status of receive direction
            	**type**\:  :py:class:`Csapsactiveline <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsactiveline>`
            
            .. attribute:: csapssigfaultber
            
            	This object contains the Bit Error Rate threshold for Signal Fault detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to the \-n, where n is between 3 and 5
            	**type**\: int
            
            	**range:** 3..5
            
            .. attribute:: csapssigdegradeber
            
            	This object contains the Bit Error Rate threshold for Signal Degrade detection on the working line. Once this threshold is exceeded, an APS switch will occur. This value is 10 to \-n where n is between 5 and 9
            	**type**\: int
            
            	**range:** 5..9
            
            .. attribute:: csapswaittorestore
            
            	This object contains interval in minutes to wait  before attempting to switch back to working line.  Not applicable if the line is configured in  non\-revertive mode, i.e. protection line will  continue to be active, even if failures on the  working line are cleared. The framer clears the  signal\-fault and signal\-degrade when APS switch  occurs. Please refer to 'csApsRevertive' for  description of non\-revertive
            	**type**\: int
            
            	**range:** 1..12
            
            	**units**\: minutes
            
            .. attribute:: csapsdirection
            
            	This object is used to configure the switching  direction which this APS line supports.   Unidirectional \: APS switch only in one direction. Bidirectional  \: APS switch in both ends of the line
            	**type**\:  :py:class:`Csapsdirection <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsdirection>`
            
            .. attribute:: csapsrevertive
            
            	This object is used to configure the APS revertive or nonrevertive option.   revertive \:    Will switch the working line back to active state after   the Wait\-To\-restore interval has expired and the    working line Signal\-Fault/Signal\-Degrade has been    cleared. Please refer to 'csApsWaitToRestore' for    description of Wait\-To\-Restore interval. nonrevertive \:    The  protection line continues to be the active line,   The active line does not switch to the working line
            	**type**\:  :py:class:`Csapsrevertive <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsrevertive>`
            
            .. attribute:: csapsdirectionoperational
            
            	This object shows the actual APS direction that is  implemented on the Near End terminal. APS direction  configured through csApsDirection is negotiated with the Far End and APS direction setting acceptable to  both ends is operational at the Near End
            	**type**\:  :py:class:`Csapsdirectionoperational <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsdirectionoperational>`
            
            .. attribute:: csapsarchmodeoperational
            
            	This object shows the actual APS architecture mode that is implemented on the Near End terminal. APS architecture mode configured through csApsArchMode object is  negotiated with the Far End through APS channel.  Architecture mode acceptable to both the Near End and  the Far End terminals is then operational at the Near  End. This value can be different than the APS  Architecture mode configured
            	**type**\:  :py:class:`Csapsarchmodeoperational <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsarchmodeoperational>`
            
            .. attribute:: csapschannelprotocol
            
            	This object allows to configure APS channel protocol to  be implemented at Near End terminal.  K1 and K2 overhead bytes in a SONET signal are used as an APS channel. This channel is used to carry APS protocol.  Possible values\: bellcore(1) \: Implements APS channel protocol as defined               in bellcore document GR\-253\-CORE. itu(2) \: Implements APS channel protocol as defined in           ITU document G.783
            	**type**\:  :py:class:`Csapschannelprotocol <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapschannelprotocol>`
            
            .. attribute:: csapsfailurestatus
            
            	This object indicates APS line failure status
            	**type**\:  :py:class:`CsApsLineFailureStatus <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsApsLineFailureStatus>`
            
            .. attribute:: csapsswitchreason
            
            	This object indicates APS line switch reason
            	**type**\:  :py:class:`CsApsLineSwitchReason <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CsApsLineSwitchReason>`
            
            .. attribute:: csapsprimarysection
            
            	This object indicates which working section is the APS primary section. In G.783 AnnexB, the K1/K2 Bytes are received on the secondary Section. All the Switch Requests are for a switch from the primary section to the secondary section. The object csApsActiveline will indicate which section is currently carrying the traffic.  Once the switch request clears normally, traffic is maintained on the section to which it was switched by making that section the primary section.   Possible values\:  workingSection1(1)\: Working Section 1 is Primary Section workingSection2(2)\: Working Section 2 is Primary Section none(3)           \: none
            	**type**\:  :py:class:`Csapsprimarysection <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry.Csapsprimarysection>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry, self).__init__()

                self.yang_name = "csApsConfigEntry"
                self.yang_parent_name = "csApsConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csapsworkingindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csapsworkingindex', YLeaf(YType.int32, 'csApsWorkingIndex')),
                    ('csapsprotectionindex', YLeaf(YType.int32, 'csApsProtectionIndex')),
                    ('csapsenable', YLeaf(YType.enumeration, 'csApsEnable')),
                    ('csapsarchmode', YLeaf(YType.enumeration, 'csApsArchMode')),
                    ('csapsactiveline', YLeaf(YType.enumeration, 'csApsActiveLine')),
                    ('csapssigfaultber', YLeaf(YType.uint32, 'csApsSigFaultBER')),
                    ('csapssigdegradeber', YLeaf(YType.uint32, 'csApsSigDegradeBER')),
                    ('csapswaittorestore', YLeaf(YType.uint32, 'csApsWaitToRestore')),
                    ('csapsdirection', YLeaf(YType.enumeration, 'csApsDirection')),
                    ('csapsrevertive', YLeaf(YType.enumeration, 'csApsRevertive')),
                    ('csapsdirectionoperational', YLeaf(YType.enumeration, 'csApsDirectionOperational')),
                    ('csapsarchmodeoperational', YLeaf(YType.enumeration, 'csApsArchModeOperational')),
                    ('csapschannelprotocol', YLeaf(YType.enumeration, 'csApsChannelProtocol')),
                    ('csapsfailurestatus', YLeaf(YType.bits, 'csApsFailureStatus')),
                    ('csapsswitchreason', YLeaf(YType.enumeration, 'csApsSwitchReason')),
                    ('csapsprimarysection', YLeaf(YType.enumeration, 'csApsPrimarySection')),
                ])
                self.csapsworkingindex = None
                self.csapsprotectionindex = None
                self.csapsenable = None
                self.csapsarchmode = None
                self.csapsactiveline = None
                self.csapssigfaultber = None
                self.csapssigdegradeber = None
                self.csapswaittorestore = None
                self.csapsdirection = None
                self.csapsrevertive = None
                self.csapsdirectionoperational = None
                self.csapsarchmodeoperational = None
                self.csapschannelprotocol = None
                self.csapsfailurestatus = Bits()
                self.csapsswitchreason = None
                self.csapsprimarysection = None
                self._segment_path = lambda: "csApsConfigEntry" + "[csApsWorkingIndex='" + str(self.csapsworkingindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/csApsConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csapsconfigtable.Csapsconfigentry, ['csapsworkingindex', 'csapsprotectionindex', 'csapsenable', 'csapsarchmode', 'csapsactiveline', 'csapssigfaultber', 'csapssigdegradeber', 'csapswaittorestore', 'csapsdirection', 'csapsrevertive', 'csapsdirectionoperational', 'csapsarchmodeoperational', 'csapschannelprotocol', 'csapsfailurestatus', 'csapsswitchreason', 'csapsprimarysection'], name, value)

            class Csapsactiveline(Enum):
                """
                Csapsactiveline (Enum Class)

                This object indicates which line is currently active. 

                It could be the working line(Section 1 for Annex B),

                the protection line(Section 2 for Annex B) or none

                if neither working nor protection line is active. 

                This object reflects the status of receive direction.

                .. data:: csApsWorkingLine = 1

                .. data:: csApsProtectionLine = 2

                .. data:: csApsNone = 3

                """

                csApsWorkingLine = Enum.YLeaf(1, "csApsWorkingLine")

                csApsProtectionLine = Enum.YLeaf(2, "csApsProtectionLine")

                csApsNone = Enum.YLeaf(3, "csApsNone")


            class Csapsarchmode(Enum):
                """
                Csapsarchmode (Enum Class)

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

                onePlusOne = Enum.YLeaf(1, "onePlusOne")

                oneToOne = Enum.YLeaf(2, "oneToOne")

                anexBOnePlusOne = Enum.YLeaf(3, "anexBOnePlusOne")

                ycableOnePlusOneNok1k2 = Enum.YLeaf(4, "ycableOnePlusOneNok1k2")

                straightOnePlusOneNok1k2 = Enum.YLeaf(5, "straightOnePlusOneNok1k2")


            class Csapsarchmodeoperational(Enum):
                """
                Csapsarchmodeoperational (Enum Class)

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

                onePlusOne = Enum.YLeaf(1, "onePlusOne")

                oneToOne = Enum.YLeaf(2, "oneToOne")

                anexBOnePlusOne = Enum.YLeaf(3, "anexBOnePlusOne")

                ycableOnePlusOneNok1k2 = Enum.YLeaf(4, "ycableOnePlusOneNok1k2")

                straightOnePlusOneNok1k2 = Enum.YLeaf(5, "straightOnePlusOneNok1k2")


            class Csapschannelprotocol(Enum):
                """
                Csapschannelprotocol (Enum Class)

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

                bellcore = Enum.YLeaf(1, "bellcore")

                itu = Enum.YLeaf(2, "itu")


            class Csapsdirection(Enum):
                """
                Csapsdirection (Enum Class)

                This object is used to configure the switching 

                direction which this APS line supports. 

                Unidirectional \: APS switch only in one direction.

                Bidirectional  \: APS switch in both ends of the line.

                .. data:: uniDirectional = 1

                .. data:: biDirectional = 2

                """

                uniDirectional = Enum.YLeaf(1, "uniDirectional")

                biDirectional = Enum.YLeaf(2, "biDirectional")


            class Csapsdirectionoperational(Enum):
                """
                Csapsdirectionoperational (Enum Class)

                This object shows the actual APS direction that is 

                implemented on the Near End terminal. APS direction 

                configured through csApsDirection is negotiated with

                the Far End and APS direction setting acceptable to 

                both ends is operational at the Near End.

                .. data:: uniDirectional = 1

                .. data:: biDirectional = 2

                """

                uniDirectional = Enum.YLeaf(1, "uniDirectional")

                biDirectional = Enum.YLeaf(2, "biDirectional")


            class Csapsenable(Enum):
                """
                Csapsenable (Enum Class)

                This object is used to enable or disable the APS feature

                on the working/protection line pairs. When enabled,

                the hardware will automatically switch the active line 

                from the working line to the protection line within 60ms,

                or vice versa.

                .. data:: csApsDisabled = 1

                .. data:: csApsEnabled = 2

                """

                csApsDisabled = Enum.YLeaf(1, "csApsDisabled")

                csApsEnabled = Enum.YLeaf(2, "csApsEnabled")


            class Csapsprimarysection(Enum):
                """
                Csapsprimarysection (Enum Class)

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

                workingSection1 = Enum.YLeaf(1, "workingSection1")

                workingSection2 = Enum.YLeaf(2, "workingSection2")

                none = Enum.YLeaf(3, "none")


            class Csapsrevertive(Enum):
                """
                Csapsrevertive (Enum Class)

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

                nonrevertive = Enum.YLeaf(1, "nonrevertive")

                revertive = Enum.YLeaf(2, "revertive")



    class Csstotaltable(Entity):
        """
        The SONET/SDH Section Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the
        number of 15 minute intervals that have elapsed since
        the line is enabled. 
        
        .. attribute:: csstotalentry
        
        	An entry in the SONET/SDH Section Total table. Entries are created automatically for sonet lines
        	**type**\: list of  		 :py:class:`Csstotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstotaltable.Csstotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csstotaltable, self).__init__()

            self.yang_name = "cssTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cssTotalEntry", ("csstotalentry", CISCOSONETMIB.Csstotaltable.Csstotalentry))])
            self._leafs = OrderedDict()

            self.csstotalentry = YList(self)
            self._segment_path = lambda: "cssTotalTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csstotaltable, [], name, value)


        class Csstotalentry(Entity):
            """
            An entry in the SONET/SDH Section Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csstotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csstotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: csstotalsefss
            
            	The number of Severely Errored Framing Seconds  encountered by a SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored framing seconds
            
            .. attribute:: csstotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Section in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csstotaltable.Csstotalentry, self).__init__()

                self.yang_name = "cssTotalEntry"
                self.yang_parent_name = "cssTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csstotaless', YLeaf(YType.uint32, 'cssTotalESs')),
                    ('csstotalsess', YLeaf(YType.uint32, 'cssTotalSESs')),
                    ('csstotalsefss', YLeaf(YType.uint32, 'cssTotalSEFSs')),
                    ('csstotalcvs', YLeaf(YType.uint32, 'cssTotalCVs')),
                ])
                self.ifindex = None
                self.csstotaless = None
                self.csstotalsess = None
                self.csstotalsefss = None
                self.csstotalcvs = None
                self._segment_path = lambda: "cssTotalEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cssTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csstotaltable.Csstotalentry, ['ifindex', 'csstotaless', 'csstotalsess', 'csstotalsefss', 'csstotalcvs'], name, value)


    class Csstracetable(Entity):
        """
        The SONET/SDH Section Trace table. This table contains 
        objects for tracing the sonet section.
        
        .. attribute:: csstraceentry
        
        	An entry in the trace table. Entries exist for active sonet lines. The objects in this table are used to verify  continued connection between the two ends of the line
        	**type**\: list of  		 :py:class:`Csstraceentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstracetable.Csstraceentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csstracetable, self).__init__()

            self.yang_name = "cssTraceTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cssTraceEntry", ("csstraceentry", CISCOSONETMIB.Csstracetable.Csstraceentry))])
            self._leafs = OrderedDict()

            self.csstraceentry = YList(self)
            self._segment_path = lambda: "cssTraceTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csstracetable, [], name, value)


        class Csstraceentry(Entity):
            """
            An entry in the trace table. Entries exist for active sonet
            lines. The objects in this table are used to verify 
            continued connection between the two ends of the line.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csstracetotransmit
            
            	Sonet Section Trace To Transmit. This is string that is transmitted to perform Sonet section trace  diagnostics. The trace string is  repetitively  transmited so that a trace receiving terminal can  verify its continued connection to the intended  transmitter. The default value is a zero\-length string. Unless this object is set to a non\-zero length string,  tracing will not be performed
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csstracetoexpect
            
            	Sonet Section Trace To Expect. The receiving terminal  verifies if the incoming string matches this string.  The value of 'cssTraceFailure' indicates whether a  trace mismatch occurred. The default value is a  zero\-length string
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csstracefailure
            
            	The value of this object is set to 'true' when Sonet  Section received trace does not match the  'cssTraceToExpect'
            	**type**\: bool
            
            .. attribute:: csstracereceived
            
            	This object is used to view the Sonet Section Trace that  is received by the receiving terminal
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csstracetable.Csstraceentry, self).__init__()

                self.yang_name = "cssTraceEntry"
                self.yang_parent_name = "cssTraceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csstracetotransmit', YLeaf(YType.str, 'cssTraceToTransmit')),
                    ('csstracetoexpect', YLeaf(YType.str, 'cssTraceToExpect')),
                    ('csstracefailure', YLeaf(YType.boolean, 'cssTraceFailure')),
                    ('csstracereceived', YLeaf(YType.str, 'cssTraceReceived')),
                ])
                self.ifindex = None
                self.csstracetotransmit = None
                self.csstracetoexpect = None
                self.csstracefailure = None
                self.csstracereceived = None
                self._segment_path = lambda: "cssTraceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cssTraceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csstracetable.Csstraceentry, ['ifindex', 'csstracetotransmit', 'csstracetoexpect', 'csstracefailure', 'csstracereceived'], name, value)


    class Csltotaltable(Entity):
        """
        The SONET/SDH Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 
        hour period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since
        the line is enabled.
        
        .. attribute:: csltotalentry
        
        	An entry in the SONET/SDH Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of  		 :py:class:`Csltotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csltotaltable.Csltotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csltotaltable, self).__init__()

            self.yang_name = "cslTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cslTotalEntry", ("csltotalentry", CISCOSONETMIB.Csltotaltable.Csltotalentry))])
            self._leafs = OrderedDict()

            self.csltotalentry = YList(self)
            self._segment_path = lambda: "cslTotalTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csltotaltable, [], name, value)


        class Csltotalentry(Entity):
            """
            An entry in the SONET/SDH Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csltotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csltotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: csltotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: csltotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csltotaltable.Csltotalentry, self).__init__()

                self.yang_name = "cslTotalEntry"
                self.yang_parent_name = "cslTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csltotaless', YLeaf(YType.uint32, 'cslTotalESs')),
                    ('csltotalsess', YLeaf(YType.uint32, 'cslTotalSESs')),
                    ('csltotalcvs', YLeaf(YType.uint32, 'cslTotalCVs')),
                    ('csltotaluass', YLeaf(YType.uint32, 'cslTotalUASs')),
                ])
                self.ifindex = None
                self.csltotaless = None
                self.csltotalsess = None
                self.csltotalcvs = None
                self.csltotaluass = None
                self._segment_path = lambda: "cslTotalEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cslTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csltotaltable.Csltotalentry, ['ifindex', 'csltotaless', 'csltotalsess', 'csltotalcvs', 'csltotaluass'], name, value)


    class Cslfarendtotaltable(Entity):
        """
        The SONET/SDH Far End Line Total table. It contains the 
        cumulative sum of the various statistics for the 24 hour 
        period preceding the current interval. The object 
        'sonetMediumValidIntervals' from RFC2558 contains the 
        number of 15 minute intervals that have elapsed since the 
        line is enabled.
        
        .. attribute:: cslfarendtotalentry
        
        	An entry in the SONET/SDH Far End Line Total table. Entries are created automatically for sonet lines
        	**type**\: list of  		 :py:class:`Cslfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Cslfarendtotaltable.Cslfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Cslfarendtotaltable, self).__init__()

            self.yang_name = "cslFarEndTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cslFarEndTotalEntry", ("cslfarendtotalentry", CISCOSONETMIB.Cslfarendtotaltable.Cslfarendtotalentry))])
            self._leafs = OrderedDict()

            self.cslfarendtotalentry = YList(self)
            self._segment_path = lambda: "cslFarEndTotalTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Cslfarendtotaltable, [], name, value)


        class Cslfarendtotalentry(Entity):
            """
            An entry in the SONET/SDH Far End Line Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cslfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: cslfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: cslfarendtotalcvs
            
            	The number of Coding Violations encountered by a SONET/SDH  Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: cslfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Far End Line in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Cslfarendtotaltable.Cslfarendtotalentry, self).__init__()

                self.yang_name = "cslFarEndTotalEntry"
                self.yang_parent_name = "cslFarEndTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cslfarendtotaless', YLeaf(YType.uint32, 'cslFarEndTotalESs')),
                    ('cslfarendtotalsess', YLeaf(YType.uint32, 'cslFarEndTotalSESs')),
                    ('cslfarendtotalcvs', YLeaf(YType.uint32, 'cslFarEndTotalCVs')),
                    ('cslfarendtotaluass', YLeaf(YType.uint32, 'cslFarEndTotalUASs')),
                ])
                self.ifindex = None
                self.cslfarendtotaless = None
                self.cslfarendtotalsess = None
                self.cslfarendtotalcvs = None
                self.cslfarendtotaluass = None
                self._segment_path = lambda: "cslFarEndTotalEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cslFarEndTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Cslfarendtotaltable.Cslfarendtotalentry, ['ifindex', 'cslfarendtotaless', 'cslfarendtotalsess', 'cslfarendtotalcvs', 'cslfarendtotaluass'], name, value)


    class Csptotaltable(Entity):
        """
        The SONET/SDH Path Total table. It contains the cumulative 
        sum of the various statistics for the 24 hour period 
        preceding the current interval.The object 
        'sonetMediumValidIntervals' from RFC2558 contains the number
        of 15 minute intervals that have elapsed since the line is 
        enabled.
        
        .. attribute:: csptotalentry
        
        	An entry in the SONET/SDH Path Total table. Entries are created automatically for sonet lines
        	**type**\: list of  		 :py:class:`Csptotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csptotaltable.Csptotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csptotaltable, self).__init__()

            self.yang_name = "cspTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cspTotalEntry", ("csptotalentry", CISCOSONETMIB.Csptotaltable.Csptotalentry))])
            self._leafs = OrderedDict()

            self.csptotalentry = YList(self)
            self._segment_path = lambda: "cspTotalTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csptotaltable, [], name, value)


        class Csptotalentry(Entity):
            """
            An entry in the SONET/SDH Path Total table. Entries
            are created automatically for sonet lines.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csptotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: csptotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: csptotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: csptotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH Path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csptotaltable.Csptotalentry, self).__init__()

                self.yang_name = "cspTotalEntry"
                self.yang_parent_name = "cspTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csptotaless', YLeaf(YType.uint32, 'cspTotalESs')),
                    ('csptotalsess', YLeaf(YType.uint32, 'cspTotalSESs')),
                    ('csptotalcvs', YLeaf(YType.uint32, 'cspTotalCVs')),
                    ('csptotaluass', YLeaf(YType.uint32, 'cspTotalUASs')),
                ])
                self.ifindex = None
                self.csptotaless = None
                self.csptotalsess = None
                self.csptotalcvs = None
                self.csptotaluass = None
                self._segment_path = lambda: "cspTotalEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cspTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csptotaltable.Csptotalentry, ['ifindex', 'csptotaless', 'csptotalsess', 'csptotalcvs', 'csptotaluass'], name, value)


    class Cspfarendtotaltable(Entity):
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
        	**type**\: list of  		 :py:class:`Cspfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Cspfarendtotaltable.Cspfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Cspfarendtotaltable, self).__init__()

            self.yang_name = "cspFarEndTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cspFarEndTotalEntry", ("cspfarendtotalentry", CISCOSONETMIB.Cspfarendtotaltable.Cspfarendtotalentry))])
            self._leafs = OrderedDict()

            self.cspfarendtotalentry = YList(self)
            self._segment_path = lambda: "cspFarEndTotalTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Cspfarendtotaltable, [], name, value)


        class Cspfarendtotalentry(Entity):
            """
            An entry in the SONET/SDH Far End Path Total table. 
            Entries are created automatically for sonet lines.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cspfarendtotaless
            
            	The number of Errored Seconds encountered by a SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: errored seconds
            
            .. attribute:: cspfarendtotalsess
            
            	The number of Severely Errored Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: severely errored seconds
            
            .. attribute:: cspfarendtotalcvs
            
            	The number of Coding Violations encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: coding violations
            
            .. attribute:: cspfarendtotaluass
            
            	The number of Unavailable Seconds encountered by a  SONET/SDH far end path in the last 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: unavailable seconds
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Cspfarendtotaltable.Cspfarendtotalentry, self).__init__()

                self.yang_name = "cspFarEndTotalEntry"
                self.yang_parent_name = "cspFarEndTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cspfarendtotaless', YLeaf(YType.uint32, 'cspFarEndTotalESs')),
                    ('cspfarendtotalsess', YLeaf(YType.uint32, 'cspFarEndTotalSESs')),
                    ('cspfarendtotalcvs', YLeaf(YType.uint32, 'cspFarEndTotalCVs')),
                    ('cspfarendtotaluass', YLeaf(YType.uint32, 'cspFarEndTotalUASs')),
                ])
                self.ifindex = None
                self.cspfarendtotaless = None
                self.cspfarendtotalsess = None
                self.cspfarendtotalcvs = None
                self.cspfarendtotaluass = None
                self._segment_path = lambda: "cspFarEndTotalEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cspFarEndTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Cspfarendtotaltable.Cspfarendtotalentry, ['ifindex', 'cspfarendtotaless', 'cspfarendtotalsess', 'cspfarendtotalcvs', 'cspfarendtotaluass'], name, value)


    class Csptracetable(Entity):
        """
        The SONET/SDH Path Trace table. This table contains objects 
        for tracing the sonet path.
        
        .. attribute:: csptraceentry
        
        	An entry in the SONET/SDH Path Trace table. The entries  exist for active sonet lines. The objects in this table are  used to verify continued connection between the two ends of the line
        	**type**\: list of  		 :py:class:`Csptraceentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csptracetable.Csptraceentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csptracetable, self).__init__()

            self.yang_name = "cspTraceTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cspTraceEntry", ("csptraceentry", CISCOSONETMIB.Csptracetable.Csptraceentry))])
            self._leafs = OrderedDict()

            self.csptraceentry = YList(self)
            self._segment_path = lambda: "cspTraceTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csptracetable, [], name, value)


        class Csptraceentry(Entity):
            """
            An entry in the SONET/SDH Path Trace table. The entries 
            exist for active sonet lines. The objects in this table are 
            used to verify continued connection between the two ends of
            the line.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csptracetotransmit
            
            	Sonet Path Trace To Transmit. The trace string is  repetitively transmited so that a trace receiving terminal  can verify its continued receiving terminal can verify its  continued connection to the intended transmitter. The  default value is a zero\-length string. Unless this object  is set to a non\-zero length string, tracing will not be  performed
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csptracetoexpect
            
            	Sonet Path Trace To Expect.  The receiving terminal verifies if the incoming string matches this string. The value of  'cspTraceFailure' indicates whether a trace mismatch  occured. The default value is a zero\-length string
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            .. attribute:: csptracefailure
            
            	The value of this object is set to 'true' when Sonet Path  received trace does not match the 'cspTraceToExpect'
            	**type**\: bool
            
            .. attribute:: csptracereceived
            
            	This object is used to view the Sonet Path Trace that is received by the receiving terminal
            	**type**\: str
            
            	**length:** 0 \| 16 \| 64
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csptracetable.Csptraceentry, self).__init__()

                self.yang_name = "cspTraceEntry"
                self.yang_parent_name = "cspTraceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csptracetotransmit', YLeaf(YType.str, 'cspTraceToTransmit')),
                    ('csptracetoexpect', YLeaf(YType.str, 'cspTraceToExpect')),
                    ('csptracefailure', YLeaf(YType.boolean, 'cspTraceFailure')),
                    ('csptracereceived', YLeaf(YType.str, 'cspTraceReceived')),
                ])
                self.ifindex = None
                self.csptracetotransmit = None
                self.csptracetoexpect = None
                self.csptracefailure = None
                self.csptracereceived = None
                self._segment_path = lambda: "cspTraceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/cspTraceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csptracetable.Csptraceentry, ['ifindex', 'csptracetotransmit', 'csptracetoexpect', 'csptracefailure', 'csptracereceived'], name, value)


    class Csstatstable(Entity):
        """
        The SONET/SDH Section statistics table. This table 
        maintains the number of times the line encountered Loss of
        Signal(LOS), Loss of frame(LOF), Alarm Indication 
        signals(AISs), Remote failure indications(RFIs).
        
        .. attribute:: csstatsentry
        
        	An entry in the SONET/SDH statistics table. These are  realtime statistics for the Sonet section, line and path layers. The statistics are gathered for each sonet line.  An entry is created automatically and is indexed by  ifIndex
        	**type**\: list of  		 :py:class:`Csstatsentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csstatstable.Csstatsentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csstatstable, self).__init__()

            self.yang_name = "csStatsTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csStatsEntry", ("csstatsentry", CISCOSONETMIB.Csstatstable.Csstatsentry))])
            self._leafs = OrderedDict()

            self.csstatsentry = YList(self)
            self._segment_path = lambda: "csStatsTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csstatstable, [], name, value)


        class Csstatsentry(Entity):
            """
            An entry in the SONET/SDH statistics table. These are 
            realtime statistics for the Sonet section, line and path
            layers. The statistics are gathered for each sonet line. 
            An entry is created automatically and is indexed by 
            ifIndex.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cssloss
            
            	The number of Loss of signals(LOS) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: loss of signals
            
            .. attribute:: csslofs
            
            	The number of Loss of Frames (LOF) encountered by a  SONET/SDH Section. A high value for this object may  indicate a problem with the Sonet Section layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: loss of frames
            
            .. attribute:: cslaiss
            
            	The number of alarm indication signals(AIS)  encountered by  a SONET/SDH Line. A high value for this object may indicate a problem with the Sonet Line layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: alarm indication signals
            
            .. attribute:: cslrfis
            
            	The number of remote failure indications (RFI) encountered  by a SONET/SDH Line. A high value for this object may  indicate a problem with the Sonet Line layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: remote failure indications
            
            .. attribute:: cspaiss
            
            	The  number of alarm indication signals (AIS) encountered by a SONET/SDH Path. A high value for this object may  indicate a problem with the Sonet Path layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: alarm indication signals
            
            .. attribute:: csprfis
            
            	The number of  remote failure indications (RFI)  encountered by a SONET/SDH Path. A high value for this  object may indicate a problem with the Sonet Path layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: remote failure indications
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csstatstable.Csstatsentry, self).__init__()

                self.yang_name = "csStatsEntry"
                self.yang_parent_name = "csStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cssloss', YLeaf(YType.uint32, 'cssLOSs')),
                    ('csslofs', YLeaf(YType.uint32, 'cssLOFs')),
                    ('cslaiss', YLeaf(YType.uint32, 'cslAISs')),
                    ('cslrfis', YLeaf(YType.uint32, 'cslRFIs')),
                    ('cspaiss', YLeaf(YType.uint32, 'cspAISs')),
                    ('csprfis', YLeaf(YType.uint32, 'cspRFIs')),
                ])
                self.ifindex = None
                self.cssloss = None
                self.csslofs = None
                self.cslaiss = None
                self.cslrfis = None
                self.cspaiss = None
                self.csprfis = None
                self._segment_path = lambda: "csStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/csStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csstatstable.Csstatsentry, ['ifindex', 'cssloss', 'csslofs', 'cslaiss', 'cslrfis', 'cspaiss', 'csprfis'], name, value)


    class Csau4Tug3Configtable(Entity):
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
        	**type**\: list of  		 :py:class:`Csau4Tug3Configentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csau4Tug3Configtable.Csau4Tug3Configentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CISCOSONETMIB.Csau4Tug3Configtable, self).__init__()

            self.yang_name = "csAu4Tug3ConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csAu4Tug3ConfigEntry", ("csau4tug3configentry", CISCOSONETMIB.Csau4Tug3Configtable.Csau4Tug3Configentry))])
            self._leafs = OrderedDict()

            self.csau4tug3configentry = YList(self)
            self._segment_path = lambda: "csAu4Tug3ConfigTable"
            self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSONETMIB.Csau4Tug3Configtable, [], name, value)


        class Csau4Tug3Configentry(Entity):
            """
            There is an entry in this table for each TUG\-3 within a 
            AU\-4 SDH path that supports SDH virtual container VC\-4.
            The ifIndex value represents an entry in ifTable with
            ifType = sonetPath(50).The ifTable entry applicable for
            this entry belongs to AU\-4 path.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: csau4tug3  (key)
            
            	This object represents the TUG\-3 number
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: csau4tug3payload
            
            	This object is used for configuring the payload for the tributary group.  The possible values are \:  vc11   \: When set to 'vc11' following things are done\:        \- 28 entries created in ifTable for TU\-11 with           ifType = sonetVT(51)        \- 28 entries created in ifTable for DS1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11  vc12   \: When set to 'vc12' following things are done\:        \- 21 entries created in ifTable for TU\-12 with           ifType = sonetVT(51)        \- 21 entries created in ifTable for E1 with           ifType = ds1(18)           STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12  tu3ds3 \: When set to 'tu3ds3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for DS3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  tu3e3  \: When set to 'tu3e3' following things are done\:        \- 1 entry created in ifTable for TU\-3 with           ifType = sonetVT(51)        \- 1 entry created in ifTable for E3 with           ifType = ds3(30)           STM1<\-AU\-4<\-TUG\-3<\-TU\-3<\-VC3  The value 'other' can not be set
            	**type**\:  :py:class:`Csau4Tug3Payload <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CISCOSONETMIB.Csau4Tug3Configtable.Csau4Tug3Configentry.Csau4Tug3Payload>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CISCOSONETMIB.Csau4Tug3Configtable.Csau4Tug3Configentry, self).__init__()

                self.yang_name = "csAu4Tug3ConfigEntry"
                self.yang_parent_name = "csAu4Tug3ConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','csau4tug3']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('csau4tug3', YLeaf(YType.int32, 'csAu4Tug3')),
                    ('csau4tug3payload', YLeaf(YType.enumeration, 'csAu4Tug3Payload')),
                ])
                self.ifindex = None
                self.csau4tug3 = None
                self.csau4tug3payload = None
                self._segment_path = lambda: "csAu4Tug3ConfigEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[csAu4Tug3='" + str(self.csau4tug3) + "']"
                self._absolute_path = lambda: "CISCO-SONET-MIB:CISCO-SONET-MIB/csAu4Tug3ConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSONETMIB.Csau4Tug3Configtable.Csau4Tug3Configentry, ['ifindex', 'csau4tug3', 'csau4tug3payload'], name, value)

            class Csau4Tug3Payload(Enum):
                """
                Csau4Tug3Payload (Enum Class)

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

                other = Enum.YLeaf(1, "other")

                vc11 = Enum.YLeaf(2, "vc11")

                vc12 = Enum.YLeaf(3, "vc12")

                tu3ds3 = Enum.YLeaf(4, "tu3ds3")

                tu3e3 = Enum.YLeaf(5, "tu3e3")


    def clone_ptr(self):
        self._top_entity = CISCOSONETMIB()
        return self._top_entity

