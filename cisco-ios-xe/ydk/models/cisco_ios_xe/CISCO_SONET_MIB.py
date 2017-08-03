""" CISCO_SONET_MIB 

The MIB module to describe SONET/SDH interfaces
objects. This is an extension to the standard SONET 
MIB(RFC 2558).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Csapslinefailurecode(Enum):
    """
    Csapslinefailurecode

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


class Csapslineswitchreason(Enum):
    """
    Csapslineswitchreason

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


class Csapslinefailurestatus(Bits):
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
    Keys are:- noApsLineFailure , csApsChannelMismatchBit , csApsModeMismatchBit , csApsFEProtectionFailureBit , csApsProtectionByteFailBit

    """

    def __init__(self):
        super(Csapslinefailurestatus, self).__init__()


class CiscoSonetMib(Entity):
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
        super(CiscoSonetMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SONET-MIB"
        self.yang_parent_name = "CISCO-SONET-MIB"

        self.csapsconfig = CiscoSonetMib.Csapsconfig()
        self.csapsconfig.parent = self
        self._children_name_map["csapsconfig"] = "csApsConfig"
        self._children_yang_names.add("csApsConfig")

        self.csapsconfigtable = CiscoSonetMib.Csapsconfigtable()
        self.csapsconfigtable.parent = self
        self._children_name_map["csapsconfigtable"] = "csApsConfigTable"
        self._children_yang_names.add("csApsConfigTable")

        self.csau4tug3configtable = CiscoSonetMib.Csau4Tug3Configtable()
        self.csau4tug3configtable.parent = self
        self._children_name_map["csau4tug3configtable"] = "csAu4Tug3ConfigTable"
        self._children_yang_names.add("csAu4Tug3ConfigTable")

        self.csconfigtable = CiscoSonetMib.Csconfigtable()
        self.csconfigtable.parent = self
        self._children_name_map["csconfigtable"] = "csConfigTable"
        self._children_yang_names.add("csConfigTable")

        self.cslfarendtotaltable = CiscoSonetMib.Cslfarendtotaltable()
        self.cslfarendtotaltable.parent = self
        self._children_name_map["cslfarendtotaltable"] = "cslFarEndTotalTable"
        self._children_yang_names.add("cslFarEndTotalTable")

        self.csltotaltable = CiscoSonetMib.Csltotaltable()
        self.csltotaltable.parent = self
        self._children_name_map["csltotaltable"] = "cslTotalTable"
        self._children_yang_names.add("cslTotalTable")

        self.csnotifications = CiscoSonetMib.Csnotifications()
        self.csnotifications.parent = self
        self._children_name_map["csnotifications"] = "csNotifications"
        self._children_yang_names.add("csNotifications")

        self.cspfarendtotaltable = CiscoSonetMib.Cspfarendtotaltable()
        self.cspfarendtotaltable.parent = self
        self._children_name_map["cspfarendtotaltable"] = "cspFarEndTotalTable"
        self._children_yang_names.add("cspFarEndTotalTable")

        self.csptotaltable = CiscoSonetMib.Csptotaltable()
        self.csptotaltable.parent = self
        self._children_name_map["csptotaltable"] = "cspTotalTable"
        self._children_yang_names.add("cspTotalTable")

        self.csptracetable = CiscoSonetMib.Csptracetable()
        self.csptracetable.parent = self
        self._children_name_map["csptracetable"] = "cspTraceTable"
        self._children_yang_names.add("cspTraceTable")

        self.csstatstable = CiscoSonetMib.Csstatstable()
        self.csstatstable.parent = self
        self._children_name_map["csstatstable"] = "csStatsTable"
        self._children_yang_names.add("csStatsTable")

        self.csstotaltable = CiscoSonetMib.Csstotaltable()
        self.csstotaltable.parent = self
        self._children_name_map["csstotaltable"] = "cssTotalTable"
        self._children_yang_names.add("cssTotalTable")

        self.csstracetable = CiscoSonetMib.Csstracetable()
        self.csstracetable.parent = self
        self._children_name_map["csstracetable"] = "cssTraceTable"
        self._children_yang_names.add("cssTraceTable")


    class Csapsconfig(Entity):
        """
        
        
        .. attribute:: csapslinefailurecode
        
        	The object indicates the APS line failure code. This is the failure encountered by the APS line. Refer to CsApsLineFailureCode TC for failure code definitions. The object is used for notifications
        	**type**\:   :py:class:`Csapslinefailurecode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.Csapslinefailurecode>`
        
        .. attribute:: csapslineswitchreason
        
        	This object indicates the APS line switch reason. When the working line on one end fails, its other end is told to do an APS switch.  Refer to CsApsLineSwitchReason TC for more information. The object is used for notifications
        	**type**\:   :py:class:`Csapslineswitchreason <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.Csapslineswitchreason>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csapsconfig, self).__init__()

            self.yang_name = "csApsConfig"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csapslinefailurecode = YLeaf(YType.enumeration, "csApsLineFailureCode")

            self.csapslineswitchreason = YLeaf(YType.enumeration, "csApsLineSwitchReason")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csapslinefailurecode",
                            "csapslineswitchreason") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSonetMib.Csapsconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csapsconfig, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csapslinefailurecode.is_set or
                self.csapslineswitchreason.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csapslinefailurecode.yfilter != YFilter.not_set or
                self.csapslineswitchreason.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csApsConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csapslinefailurecode.is_set or self.csapslinefailurecode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csapslinefailurecode.get_name_leafdata())
            if (self.csapslineswitchreason.is_set or self.csapslineswitchreason.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csapslineswitchreason.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csApsLineFailureCode" or name == "csApsLineSwitchReason"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "csApsLineFailureCode"):
                self.csapslinefailurecode = value
                self.csapslinefailurecode.value_namespace = name_space
                self.csapslinefailurecode.value_namespace_prefix = name_space_prefix
            if(value_path == "csApsLineSwitchReason"):
                self.csapslineswitchreason = value
                self.csapslineswitchreason.value_namespace = name_space
                self.csapslineswitchreason.value_namespace_prefix = name_space_prefix


    class Csnotifications(Entity):
        """
        
        
        .. attribute:: csnotificationsenabled
        
        	This object controls if the generation of  ciscoSonetSectionStatusChange, ciscoSonetLineStatusChange,  ciscoSonetPathStatusChange and ciscoSonetVTStatusChange notifications is enabled. If the value of this object is 'true(1)', then all notifications in this MIB are enabled; otherwise they are disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csnotifications, self).__init__()

            self.yang_name = "csNotifications"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csnotificationsenabled = YLeaf(YType.boolean, "csNotificationsEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csnotificationsenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSonetMib.Csnotifications, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csnotifications, self).__setattr__(name, value)

        def has_data(self):
            return self.csnotificationsenabled.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csnotificationsenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csNotifications" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csnotificationsenabled.is_set or self.csnotificationsenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csnotificationsenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csNotificationsEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "csNotificationsEnabled"):
                self.csnotificationsenabled = value
                self.csnotificationsenabled.value_namespace = name_space
                self.csnotificationsenabled.value_namespace_prefix = name_space_prefix


    class Csconfigtable(Entity):
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
            super(CiscoSonetMib.Csconfigtable, self).__init__()

            self.yang_name = "csConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csconfigentry = YList(self)

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
                        super(CiscoSonetMib.Csconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csconfigtable, self).__setattr__(name, value)


        class Csconfigentry(Entity):
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
            	**type**\:   :py:class:`Csconfigframescramble <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigframescramble>`
            
            .. attribute:: csconfigloopbacktype
            
            	This object specifies the desired loopback mode configuration of the SONET line. The possible values of this objects are follows\:  noLoopback \:           Not in the loopback state.   lineLocal \:          The signal transmitted from this interface         is connected to the associated incoming         receiver. This ensures that the SONET frame         transmitted from the interface is received back         at the interface. lineRemote \:         The signal received at the interface is looped         back out to the associated transmitter.         This ensures that the remote equipment that         originated the signal receives it back. The          signal may undergo degradation as a result of         the characteristics of the transmission          medium
            	**type**\:   :py:class:`Csconfigloopbacktype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigloopbacktype>`
            
            .. attribute:: csconfigrdiptype
            
            	This object represents the type of RDI\-P (Remote Defect Indication \- Path) sent by this Network Element (NE) to remote Network Element.        onebit     \: use 1 bit RDI\-P       threebit   \: use 3 bit enhanced RDI\-P.  Default is onebit
            	**type**\:   :py:class:`Csconfigrdiptype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigrdiptype>`
            
            .. attribute:: csconfigrdivtype
            
            	This object specifies the type of RDI\-V (Remote Defect Indication \- Virtual Tributary/Container) sent by this  Network Element (NE) to the remote Network Element.        onebit     \: use 1 bit RDI\-V       threebit   \: use 3 bit enhanced RDI\-V.  Default is onebit
            	**type**\:   :py:class:`Csconfigrdivtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigrdivtype>`
            
            .. attribute:: csconfigtype
            
            	This object represents the configured line type. Sts is SONET format. Stm is SDH format.      sonetSts3c   \: OC3 concatenated     sonetStm1    \: European standard OC3     sonetSts12c  \: OC12 concatenated     sonetStm4    \: European standard OC12     sonetSts48c  \: OC48 concatenated     sonetStm16   \: European standard OC48      sonetSts192c \: OC\-192 concatenated     sonetStm64   \: European standard OC\-192     sonetSts3    \: OC3 (unconcatenated)     
            	**type**\:   :py:class:`Csconfigtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigtype>`
            
            .. attribute:: csconfigxmtclocksource
            
            	Specifies the source of the transmit clock.  loopTiming\: indicates that the recovered receive              clock is used as the transmit clock.  localTiming\: indicates that a local clock source is              used or that an external clock is               attached to the box containing the               interface. 
            	**type**\:   :py:class:`Csconfigxmtclocksource <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Csconfigxmtclocksource>`
            
            .. attribute:: cssignallingtransportmode
            
            	This object represents the mode used to transport DS0  signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling is  transferred to the VT header. In clearMode(3), only the  framing bit is transferred to the VT header.       Default is signallingTransferMode(2) if csTributaryMappingType  is byteSynchronous. For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:   :py:class:`Cssignallingtransportmode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Cssignallingtransportmode>`
            
            .. attribute:: cstributaryframingtype
            
            	This object represents the framing type to be assigned to the virtual tributaries in byte sync mapping mode.        notApplicable  \:  If VT mapping is not byteSynchronous(2).       dsx1ESF        \:  Extended Superframe Format       dsx1D4         \:  Superframe Format  Default is dsx1ESF(3) if csTributaryMappingType is  byteSynchronous(2). For asynchronous(1) mapping, the default is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:   :py:class:`Cstributaryframingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Cstributaryframingtype>`
            
            .. attribute:: cstributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.    au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.    au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or                STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  Default is au3Grouping(2) for SDH and notApplicable(1) for SONET
            	**type**\:   :py:class:`Cstributarygroupingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Cstributarygroupingtype>`
            
            .. attribute:: cstributarymappingtype
            
            	This object represents the VT/VC mapping type.  asynchronous\:    In this mode, the channel structure of                   DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside the                  VT/VC can be found and extracted from the                  frame.  Default is asynchronous(1)
            	**type**\:   :py:class:`Cstributarymappingtype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Cstributarymappingtype>`
            
            .. attribute:: cstributarytype
            
            	Type of the tributary carried within the SONET/SDH signal.  vt15vc11    \: carries T1 signal vt2vc12     \: carries E1 signal
            	**type**\:   :py:class:`Cstributarytype <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csconfigtable.Csconfigentry.Cstributarytype>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CiscoSonetMib.Csconfigtable.Csconfigentry, self).__init__()

                self.yang_name = "csConfigEntry"
                self.yang_parent_name = "csConfigTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csconfigframescramble = YLeaf(YType.enumeration, "csConfigFrameScramble")

                self.csconfigloopbacktype = YLeaf(YType.enumeration, "csConfigLoopbackType")

                self.csconfigrdiptype = YLeaf(YType.enumeration, "csConfigRDIPType")

                self.csconfigrdivtype = YLeaf(YType.enumeration, "csConfigRDIVType")

                self.csconfigtype = YLeaf(YType.enumeration, "csConfigType")

                self.csconfigxmtclocksource = YLeaf(YType.enumeration, "csConfigXmtClockSource")

                self.cssignallingtransportmode = YLeaf(YType.enumeration, "csSignallingTransportMode")

                self.cstributaryframingtype = YLeaf(YType.enumeration, "csTributaryFramingType")

                self.cstributarygroupingtype = YLeaf(YType.enumeration, "csTributaryGroupingType")

                self.cstributarymappingtype = YLeaf(YType.enumeration, "csTributaryMappingType")

                self.cstributarytype = YLeaf(YType.enumeration, "csTributaryType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csconfigframescramble",
                                "csconfigloopbacktype",
                                "csconfigrdiptype",
                                "csconfigrdivtype",
                                "csconfigtype",
                                "csconfigxmtclocksource",
                                "cssignallingtransportmode",
                                "cstributaryframingtype",
                                "cstributarygroupingtype",
                                "cstributarymappingtype",
                                "cstributarytype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csconfigtable.Csconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csconfigtable.Csconfigentry, self).__setattr__(name, value)

            class Csconfigframescramble(Enum):
                """
                Csconfigframescramble

                This object is used to disable or enable the Scrambling

                option in SONET line.

                .. data:: disabled = 1

                .. data:: enabled = 2

                """

                disabled = Enum.YLeaf(1, "disabled")

                enabled = Enum.YLeaf(2, "enabled")


            class Csconfigloopbacktype(Enum):
                """
                Csconfigloopbacktype

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
                Csconfigrdiptype

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
                Csconfigrdivtype

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
                Csconfigtype

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
                Csconfigxmtclocksource

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
                Cssignallingtransportmode

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
                Cstributaryframingtype

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
                Cstributarygroupingtype

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
                Cstributarymappingtype

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
                Cstributarytype

                Type of the tributary carried within the SONET/SDH signal.

                vt15vc11    \: carries T1 signal

                vt2vc12     \: carries E1 signal

                .. data:: vt15vc11 = 1

                .. data:: vt2vc12 = 2

                """

                vt15vc11 = Enum.YLeaf(1, "vt15vc11")

                vt2vc12 = Enum.YLeaf(2, "vt2vc12")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csconfigframescramble.is_set or
                    self.csconfigloopbacktype.is_set or
                    self.csconfigrdiptype.is_set or
                    self.csconfigrdivtype.is_set or
                    self.csconfigtype.is_set or
                    self.csconfigxmtclocksource.is_set or
                    self.cssignallingtransportmode.is_set or
                    self.cstributaryframingtype.is_set or
                    self.cstributarygroupingtype.is_set or
                    self.cstributarymappingtype.is_set or
                    self.cstributarytype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csconfigframescramble.yfilter != YFilter.not_set or
                    self.csconfigloopbacktype.yfilter != YFilter.not_set or
                    self.csconfigrdiptype.yfilter != YFilter.not_set or
                    self.csconfigrdivtype.yfilter != YFilter.not_set or
                    self.csconfigtype.yfilter != YFilter.not_set or
                    self.csconfigxmtclocksource.yfilter != YFilter.not_set or
                    self.cssignallingtransportmode.yfilter != YFilter.not_set or
                    self.cstributaryframingtype.yfilter != YFilter.not_set or
                    self.cstributarygroupingtype.yfilter != YFilter.not_set or
                    self.cstributarymappingtype.yfilter != YFilter.not_set or
                    self.cstributarytype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csConfigEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/csConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csconfigframescramble.is_set or self.csconfigframescramble.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigframescramble.get_name_leafdata())
                if (self.csconfigloopbacktype.is_set or self.csconfigloopbacktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigloopbacktype.get_name_leafdata())
                if (self.csconfigrdiptype.is_set or self.csconfigrdiptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigrdiptype.get_name_leafdata())
                if (self.csconfigrdivtype.is_set or self.csconfigrdivtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigrdivtype.get_name_leafdata())
                if (self.csconfigtype.is_set or self.csconfigtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigtype.get_name_leafdata())
                if (self.csconfigxmtclocksource.is_set or self.csconfigxmtclocksource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csconfigxmtclocksource.get_name_leafdata())
                if (self.cssignallingtransportmode.is_set or self.cssignallingtransportmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cssignallingtransportmode.get_name_leafdata())
                if (self.cstributaryframingtype.is_set or self.cstributaryframingtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cstributaryframingtype.get_name_leafdata())
                if (self.cstributarygroupingtype.is_set or self.cstributarygroupingtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cstributarygroupingtype.get_name_leafdata())
                if (self.cstributarymappingtype.is_set or self.cstributarymappingtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cstributarymappingtype.get_name_leafdata())
                if (self.cstributarytype.is_set or self.cstributarytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cstributarytype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "csConfigFrameScramble" or name == "csConfigLoopbackType" or name == "csConfigRDIPType" or name == "csConfigRDIVType" or name == "csConfigType" or name == "csConfigXmtClockSource" or name == "csSignallingTransportMode" or name == "csTributaryFramingType" or name == "csTributaryGroupingType" or name == "csTributaryMappingType" or name == "csTributaryType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigFrameScramble"):
                    self.csconfigframescramble = value
                    self.csconfigframescramble.value_namespace = name_space
                    self.csconfigframescramble.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigLoopbackType"):
                    self.csconfigloopbacktype = value
                    self.csconfigloopbacktype.value_namespace = name_space
                    self.csconfigloopbacktype.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigRDIPType"):
                    self.csconfigrdiptype = value
                    self.csconfigrdiptype.value_namespace = name_space
                    self.csconfigrdiptype.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigRDIVType"):
                    self.csconfigrdivtype = value
                    self.csconfigrdivtype.value_namespace = name_space
                    self.csconfigrdivtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigType"):
                    self.csconfigtype = value
                    self.csconfigtype.value_namespace = name_space
                    self.csconfigtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csConfigXmtClockSource"):
                    self.csconfigxmtclocksource = value
                    self.csconfigxmtclocksource.value_namespace = name_space
                    self.csconfigxmtclocksource.value_namespace_prefix = name_space_prefix
                if(value_path == "csSignallingTransportMode"):
                    self.cssignallingtransportmode = value
                    self.cssignallingtransportmode.value_namespace = name_space
                    self.cssignallingtransportmode.value_namespace_prefix = name_space_prefix
                if(value_path == "csTributaryFramingType"):
                    self.cstributaryframingtype = value
                    self.cstributaryframingtype.value_namespace = name_space
                    self.cstributaryframingtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csTributaryGroupingType"):
                    self.cstributarygroupingtype = value
                    self.cstributarygroupingtype.value_namespace = name_space
                    self.cstributarygroupingtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csTributaryMappingType"):
                    self.cstributarymappingtype = value
                    self.cstributarymappingtype.value_namespace = name_space
                    self.cstributarymappingtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csTributaryType"):
                    self.cstributarytype = value
                    self.cstributarytype.value_namespace = name_space
                    self.cstributarytype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csConfigEntry"):
                for c in self.csconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csconfigtable.Csconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csapsconfigentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csapsconfigtable, self).__init__()

            self.yang_name = "csApsConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csapsconfigentry = YList(self)

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
                        super(CiscoSonetMib.Csapsconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csapsconfigtable, self).__setattr__(name, value)


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
            
            .. attribute:: csapsworkingindex  <key>
            
            	When a pair of APS lines is configured, one line has to be the working line, which is the primary line, and the other has to be the protection line, which is the backup line. This object refers to the working line in the APS pair. For G.783 AnnexB, this index refers to Working Section 1
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsactiveline
            
            	This object indicates which line is currently active.  It could be the working line(Section 1 for Annex B), the protection line(Section 2 for Annex B) or none if neither working nor protection line is active.  This object reflects the status of receive direction
            	**type**\:   :py:class:`Csapsactiveline <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsactiveline>`
            
            .. attribute:: csapsarchmode
            
            	This object is used to configure APS architecture mode on the working/protection line pairs.   All of the following are supported on single slot.  oneToOne(2) is not  supported across 2 slots,i.e. the   working and protection slot numbers must be the same in   oneToOne(2).   onePlusOne \: This can be supported on the same card  and across 2 cards.  This mode means that the transmit and receive signals  go only over the active line(which could be working or   protection line). (straight cable implied)   oneToOne \: This is supported only on the same card  This mode means that the transmit and receive signals  go over the working and protection lines.  (straight cable implied)   anexBOnePlusOne \: This can be supported on the same card  and across 2 cards.  This mode is like the onePlusOne mode, except that the  'csApsDirection' can only be bi\-directional.  (straight cable implied)   ycableOnePlusOneNok1k2\: With Y\-cable ignore K1K2 bytes.  This mode is the Y\-cable redundancy mode.   straightOnePlusOneNok1k2 \: With straight cable, ignore                              K1K2 bytes. This mode is like                             onePlusOne, but with K1, K2                              bytes ignored
            	**type**\:   :py:class:`Csapsarchmode <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsarchmode>`
            
            .. attribute:: csapsarchmodeoperational
            
            	This object shows the actual APS architecture mode that is implemented on the Near End terminal. APS architecture mode configured through csApsArchMode object is  negotiated with the Far End through APS channel.  Architecture mode acceptable to both the Near End and  the Far End terminals is then operational at the Near  End. This value can be different than the APS  Architecture mode configured
            	**type**\:   :py:class:`Csapsarchmodeoperational <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsarchmodeoperational>`
            
            .. attribute:: csapschannelprotocol
            
            	This object allows to configure APS channel protocol to  be implemented at Near End terminal.  K1 and K2 overhead bytes in a SONET signal are used as an APS channel. This channel is used to carry APS protocol.  Possible values\: bellcore(1) \: Implements APS channel protocol as defined               in bellcore document GR\-253\-CORE. itu(2) \: Implements APS channel protocol as defined in           ITU document G.783
            	**type**\:   :py:class:`Csapschannelprotocol <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapschannelprotocol>`
            
            .. attribute:: csapsdirection
            
            	This object is used to configure the switching  direction which this APS line supports.   Unidirectional \: APS switch only in one direction. Bidirectional  \: APS switch in both ends of the line
            	**type**\:   :py:class:`Csapsdirection <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsdirection>`
            
            .. attribute:: csapsdirectionoperational
            
            	This object shows the actual APS direction that is  implemented on the Near End terminal. APS direction  configured through csApsDirection is negotiated with the Far End and APS direction setting acceptable to  both ends is operational at the Near End
            	**type**\:   :py:class:`Csapsdirectionoperational <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsdirectionoperational>`
            
            .. attribute:: csapsenable
            
            	This object is used to enable or disable the APS feature on the working/protection line pairs. When enabled, the hardware will automatically switch the active line  from the working line to the protection line within 60ms, or vice versa
            	**type**\:   :py:class:`Csapsenable <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsenable>`
            
            .. attribute:: csapsfailurestatus
            
            	This object indicates APS line failure status
            	**type**\:   :py:class:`Csapslinefailurestatus <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.Csapslinefailurestatus>`
            
            .. attribute:: csapsprimarysection
            
            	This object indicates which working section is the APS primary section. In G.783 AnnexB, the K1/K2 Bytes are received on the secondary Section. All the Switch Requests are for a switch from the primary section to the secondary section. The object csApsActiveline will indicate which section is currently carrying the traffic.  Once the switch request clears normally, traffic is maintained on the section to which it was switched by making that section the primary section.   Possible values\:  workingSection1(1)\: Working Section 1 is Primary Section workingSection2(2)\: Working Section 2 is Primary Section none(3)           \: none
            	**type**\:   :py:class:`Csapsprimarysection <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsprimarysection>`
            
            .. attribute:: csapsprotectionindex
            
            	The protection line indicates that it will become the active line when an APS switch occurs (APS switch could occur because of a failure on the working line). For G.783 AnnexB, This index refers to Working Section 2
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csapsrevertive
            
            	This object is used to configure the APS revertive or nonrevertive option.   revertive \:    Will switch the working line back to active state after   the Wait\-To\-restore interval has expired and the    working line Signal\-Fault/Signal\-Degrade has been    cleared. Please refer to 'csApsWaitToRestore' for    description of Wait\-To\-Restore interval. nonrevertive \:    The  protection line continues to be the active line,   The active line does not switch to the working line
            	**type**\:   :py:class:`Csapsrevertive <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csapsconfigtable.Csapsconfigentry.Csapsrevertive>`
            
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
            	**type**\:   :py:class:`Csapslineswitchreason <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.Csapslineswitchreason>`
            
            .. attribute:: csapswaittorestore
            
            	This object contains interval in minutes to wait  before attempting to switch back to working line.  Not applicable if the line is configured in  non\-revertive mode, i.e. protection line will  continue to be active, even if failures on the  working line are cleared. The framer clears the  signal\-fault and signal\-degrade when APS switch  occurs. Please refer to 'csApsRevertive' for  description of non\-revertive
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: minutes
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CiscoSonetMib.Csapsconfigtable.Csapsconfigentry, self).__init__()

                self.yang_name = "csApsConfigEntry"
                self.yang_parent_name = "csApsConfigTable"

                self.csapsworkingindex = YLeaf(YType.int32, "csApsWorkingIndex")

                self.csapsactiveline = YLeaf(YType.enumeration, "csApsActiveLine")

                self.csapsarchmode = YLeaf(YType.enumeration, "csApsArchMode")

                self.csapsarchmodeoperational = YLeaf(YType.enumeration, "csApsArchModeOperational")

                self.csapschannelprotocol = YLeaf(YType.enumeration, "csApsChannelProtocol")

                self.csapsdirection = YLeaf(YType.enumeration, "csApsDirection")

                self.csapsdirectionoperational = YLeaf(YType.enumeration, "csApsDirectionOperational")

                self.csapsenable = YLeaf(YType.enumeration, "csApsEnable")

                self.csapsfailurestatus = YLeaf(YType.bits, "csApsFailureStatus")

                self.csapsprimarysection = YLeaf(YType.enumeration, "csApsPrimarySection")

                self.csapsprotectionindex = YLeaf(YType.int32, "csApsProtectionIndex")

                self.csapsrevertive = YLeaf(YType.enumeration, "csApsRevertive")

                self.csapssigdegradeber = YLeaf(YType.uint32, "csApsSigDegradeBER")

                self.csapssigfaultber = YLeaf(YType.uint32, "csApsSigFaultBER")

                self.csapsswitchreason = YLeaf(YType.enumeration, "csApsSwitchReason")

                self.csapswaittorestore = YLeaf(YType.uint32, "csApsWaitToRestore")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csapsworkingindex",
                                "csapsactiveline",
                                "csapsarchmode",
                                "csapsarchmodeoperational",
                                "csapschannelprotocol",
                                "csapsdirection",
                                "csapsdirectionoperational",
                                "csapsenable",
                                "csapsfailurestatus",
                                "csapsprimarysection",
                                "csapsprotectionindex",
                                "csapsrevertive",
                                "csapssigdegradeber",
                                "csapssigfaultber",
                                "csapsswitchreason",
                                "csapswaittorestore") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csapsconfigtable.Csapsconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csapsconfigtable.Csapsconfigentry, self).__setattr__(name, value)

            class Csapsactiveline(Enum):
                """
                Csapsactiveline

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
                Csapsarchmode

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
                Csapsarchmodeoperational

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
                Csapschannelprotocol

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
                Csapsdirection

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
                Csapsdirectionoperational

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
                Csapsenable

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
                Csapsprimarysection

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
                Csapsrevertive

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


            def has_data(self):
                return (
                    self.csapsworkingindex.is_set or
                    self.csapsactiveline.is_set or
                    self.csapsarchmode.is_set or
                    self.csapsarchmodeoperational.is_set or
                    self.csapschannelprotocol.is_set or
                    self.csapsdirection.is_set or
                    self.csapsdirectionoperational.is_set or
                    self.csapsenable.is_set or
                    self.csapsfailurestatus.is_set or
                    self.csapsprimarysection.is_set or
                    self.csapsprotectionindex.is_set or
                    self.csapsrevertive.is_set or
                    self.csapssigdegradeber.is_set or
                    self.csapssigfaultber.is_set or
                    self.csapsswitchreason.is_set or
                    self.csapswaittorestore.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csapsworkingindex.yfilter != YFilter.not_set or
                    self.csapsactiveline.yfilter != YFilter.not_set or
                    self.csapsarchmode.yfilter != YFilter.not_set or
                    self.csapsarchmodeoperational.yfilter != YFilter.not_set or
                    self.csapschannelprotocol.yfilter != YFilter.not_set or
                    self.csapsdirection.yfilter != YFilter.not_set or
                    self.csapsdirectionoperational.yfilter != YFilter.not_set or
                    self.csapsenable.yfilter != YFilter.not_set or
                    self.csapsfailurestatus.yfilter != YFilter.not_set or
                    self.csapsprimarysection.yfilter != YFilter.not_set or
                    self.csapsprotectionindex.yfilter != YFilter.not_set or
                    self.csapsrevertive.yfilter != YFilter.not_set or
                    self.csapssigdegradeber.yfilter != YFilter.not_set or
                    self.csapssigfaultber.yfilter != YFilter.not_set or
                    self.csapsswitchreason.yfilter != YFilter.not_set or
                    self.csapswaittorestore.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csApsConfigEntry" + "[csApsWorkingIndex='" + self.csapsworkingindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/csApsConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csapsworkingindex.is_set or self.csapsworkingindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsworkingindex.get_name_leafdata())
                if (self.csapsactiveline.is_set or self.csapsactiveline.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsactiveline.get_name_leafdata())
                if (self.csapsarchmode.is_set or self.csapsarchmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsarchmode.get_name_leafdata())
                if (self.csapsarchmodeoperational.is_set or self.csapsarchmodeoperational.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsarchmodeoperational.get_name_leafdata())
                if (self.csapschannelprotocol.is_set or self.csapschannelprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapschannelprotocol.get_name_leafdata())
                if (self.csapsdirection.is_set or self.csapsdirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsdirection.get_name_leafdata())
                if (self.csapsdirectionoperational.is_set or self.csapsdirectionoperational.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsdirectionoperational.get_name_leafdata())
                if (self.csapsenable.is_set or self.csapsenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsenable.get_name_leafdata())
                if (self.csapsfailurestatus.is_set or self.csapsfailurestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsfailurestatus.get_name_leafdata())
                if (self.csapsprimarysection.is_set or self.csapsprimarysection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsprimarysection.get_name_leafdata())
                if (self.csapsprotectionindex.is_set or self.csapsprotectionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsprotectionindex.get_name_leafdata())
                if (self.csapsrevertive.is_set or self.csapsrevertive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsrevertive.get_name_leafdata())
                if (self.csapssigdegradeber.is_set or self.csapssigdegradeber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapssigdegradeber.get_name_leafdata())
                if (self.csapssigfaultber.is_set or self.csapssigfaultber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapssigfaultber.get_name_leafdata())
                if (self.csapsswitchreason.is_set or self.csapsswitchreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapsswitchreason.get_name_leafdata())
                if (self.csapswaittorestore.is_set or self.csapswaittorestore.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csapswaittorestore.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csApsWorkingIndex" or name == "csApsActiveLine" or name == "csApsArchMode" or name == "csApsArchModeOperational" or name == "csApsChannelProtocol" or name == "csApsDirection" or name == "csApsDirectionOperational" or name == "csApsEnable" or name == "csApsFailureStatus" or name == "csApsPrimarySection" or name == "csApsProtectionIndex" or name == "csApsRevertive" or name == "csApsSigDegradeBER" or name == "csApsSigFaultBER" or name == "csApsSwitchReason" or name == "csApsWaitToRestore"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csApsWorkingIndex"):
                    self.csapsworkingindex = value
                    self.csapsworkingindex.value_namespace = name_space
                    self.csapsworkingindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsActiveLine"):
                    self.csapsactiveline = value
                    self.csapsactiveline.value_namespace = name_space
                    self.csapsactiveline.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsArchMode"):
                    self.csapsarchmode = value
                    self.csapsarchmode.value_namespace = name_space
                    self.csapsarchmode.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsArchModeOperational"):
                    self.csapsarchmodeoperational = value
                    self.csapsarchmodeoperational.value_namespace = name_space
                    self.csapsarchmodeoperational.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsChannelProtocol"):
                    self.csapschannelprotocol = value
                    self.csapschannelprotocol.value_namespace = name_space
                    self.csapschannelprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsDirection"):
                    self.csapsdirection = value
                    self.csapsdirection.value_namespace = name_space
                    self.csapsdirection.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsDirectionOperational"):
                    self.csapsdirectionoperational = value
                    self.csapsdirectionoperational.value_namespace = name_space
                    self.csapsdirectionoperational.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsEnable"):
                    self.csapsenable = value
                    self.csapsenable.value_namespace = name_space
                    self.csapsenable.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsFailureStatus"):
                    self.csapsfailurestatus[value] = True
                if(value_path == "csApsPrimarySection"):
                    self.csapsprimarysection = value
                    self.csapsprimarysection.value_namespace = name_space
                    self.csapsprimarysection.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsProtectionIndex"):
                    self.csapsprotectionindex = value
                    self.csapsprotectionindex.value_namespace = name_space
                    self.csapsprotectionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsRevertive"):
                    self.csapsrevertive = value
                    self.csapsrevertive.value_namespace = name_space
                    self.csapsrevertive.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsSigDegradeBER"):
                    self.csapssigdegradeber = value
                    self.csapssigdegradeber.value_namespace = name_space
                    self.csapssigdegradeber.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsSigFaultBER"):
                    self.csapssigfaultber = value
                    self.csapssigfaultber.value_namespace = name_space
                    self.csapssigfaultber.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsSwitchReason"):
                    self.csapsswitchreason = value
                    self.csapsswitchreason.value_namespace = name_space
                    self.csapsswitchreason.value_namespace_prefix = name_space_prefix
                if(value_path == "csApsWaitToRestore"):
                    self.csapswaittorestore = value
                    self.csapswaittorestore.value_namespace = name_space
                    self.csapswaittorestore.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csapsconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csapsconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csApsConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csApsConfigEntry"):
                for c in self.csapsconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csapsconfigtable.Csapsconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csapsconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csApsConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csstotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csstotaltable.Csstotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csstotaltable, self).__init__()

            self.yang_name = "cssTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csstotalentry = YList(self)

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
                        super(CiscoSonetMib.Csstotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csstotaltable, self).__setattr__(name, value)


        class Csstotalentry(Entity):
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
                super(CiscoSonetMib.Csstotaltable.Csstotalentry, self).__init__()

                self.yang_name = "cssTotalEntry"
                self.yang_parent_name = "cssTotalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csstotalcvs = YLeaf(YType.uint32, "cssTotalCVs")

                self.csstotaless = YLeaf(YType.uint32, "cssTotalESs")

                self.csstotalsefss = YLeaf(YType.uint32, "cssTotalSEFSs")

                self.csstotalsess = YLeaf(YType.uint32, "cssTotalSESs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csstotalcvs",
                                "csstotaless",
                                "csstotalsefss",
                                "csstotalsess") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csstotaltable.Csstotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csstotaltable.Csstotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csstotalcvs.is_set or
                    self.csstotaless.is_set or
                    self.csstotalsefss.is_set or
                    self.csstotalsess.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csstotalcvs.yfilter != YFilter.not_set or
                    self.csstotaless.yfilter != YFilter.not_set or
                    self.csstotalsefss.yfilter != YFilter.not_set or
                    self.csstotalsess.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cssTotalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cssTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csstotalcvs.is_set or self.csstotalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstotalcvs.get_name_leafdata())
                if (self.csstotaless.is_set or self.csstotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstotaless.get_name_leafdata())
                if (self.csstotalsefss.is_set or self.csstotalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstotalsefss.get_name_leafdata())
                if (self.csstotalsess.is_set or self.csstotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstotalsess.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cssTotalCVs" or name == "cssTotalESs" or name == "cssTotalSEFSs" or name == "cssTotalSESs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTotalCVs"):
                    self.csstotalcvs = value
                    self.csstotalcvs.value_namespace = name_space
                    self.csstotalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTotalESs"):
                    self.csstotaless = value
                    self.csstotaless.value_namespace = name_space
                    self.csstotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTotalSEFSs"):
                    self.csstotalsefss = value
                    self.csstotalsefss.value_namespace = name_space
                    self.csstotalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTotalSESs"):
                    self.csstotalsess = value
                    self.csstotalsess.value_namespace = name_space
                    self.csstotalsess.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csstotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csstotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cssTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cssTotalEntry"):
                for c in self.csstotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csstotaltable.Csstotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csstotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cssTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csstracetable(Entity):
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
            super(CiscoSonetMib.Csstracetable, self).__init__()

            self.yang_name = "cssTraceTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csstraceentry = YList(self)

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
                        super(CiscoSonetMib.Csstracetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csstracetable, self).__setattr__(name, value)


        class Csstraceentry(Entity):
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
                super(CiscoSonetMib.Csstracetable.Csstraceentry, self).__init__()

                self.yang_name = "cssTraceEntry"
                self.yang_parent_name = "cssTraceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csstracefailure = YLeaf(YType.boolean, "cssTraceFailure")

                self.csstracereceived = YLeaf(YType.str, "cssTraceReceived")

                self.csstracetoexpect = YLeaf(YType.str, "cssTraceToExpect")

                self.csstracetotransmit = YLeaf(YType.str, "cssTraceToTransmit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csstracefailure",
                                "csstracereceived",
                                "csstracetoexpect",
                                "csstracetotransmit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csstracetable.Csstraceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csstracetable.Csstraceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csstracefailure.is_set or
                    self.csstracereceived.is_set or
                    self.csstracetoexpect.is_set or
                    self.csstracetotransmit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csstracefailure.yfilter != YFilter.not_set or
                    self.csstracereceived.yfilter != YFilter.not_set or
                    self.csstracetoexpect.yfilter != YFilter.not_set or
                    self.csstracetotransmit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cssTraceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cssTraceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csstracefailure.is_set or self.csstracefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstracefailure.get_name_leafdata())
                if (self.csstracereceived.is_set or self.csstracereceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstracereceived.get_name_leafdata())
                if (self.csstracetoexpect.is_set or self.csstracetoexpect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstracetoexpect.get_name_leafdata())
                if (self.csstracetotransmit.is_set or self.csstracetotransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csstracetotransmit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cssTraceFailure" or name == "cssTraceReceived" or name == "cssTraceToExpect" or name == "cssTraceToTransmit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTraceFailure"):
                    self.csstracefailure = value
                    self.csstracefailure.value_namespace = name_space
                    self.csstracefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTraceReceived"):
                    self.csstracereceived = value
                    self.csstracereceived.value_namespace = name_space
                    self.csstracereceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTraceToExpect"):
                    self.csstracetoexpect = value
                    self.csstracetoexpect.value_namespace = name_space
                    self.csstracetoexpect.value_namespace_prefix = name_space_prefix
                if(value_path == "cssTraceToTransmit"):
                    self.csstracetotransmit = value
                    self.csstracetotransmit.value_namespace = name_space
                    self.csstracetotransmit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csstraceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csstraceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cssTraceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cssTraceEntry"):
                for c in self.csstraceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csstracetable.Csstraceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csstraceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cssTraceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csltotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csltotaltable.Csltotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csltotaltable, self).__init__()

            self.yang_name = "cslTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csltotalentry = YList(self)

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
                        super(CiscoSonetMib.Csltotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csltotaltable, self).__setattr__(name, value)


        class Csltotalentry(Entity):
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
                super(CiscoSonetMib.Csltotaltable.Csltotalentry, self).__init__()

                self.yang_name = "cslTotalEntry"
                self.yang_parent_name = "cslTotalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csltotalcvs = YLeaf(YType.uint32, "cslTotalCVs")

                self.csltotaless = YLeaf(YType.uint32, "cslTotalESs")

                self.csltotalsess = YLeaf(YType.uint32, "cslTotalSESs")

                self.csltotaluass = YLeaf(YType.uint32, "cslTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csltotalcvs",
                                "csltotaless",
                                "csltotalsess",
                                "csltotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csltotaltable.Csltotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csltotaltable.Csltotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csltotalcvs.is_set or
                    self.csltotaless.is_set or
                    self.csltotalsess.is_set or
                    self.csltotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csltotalcvs.yfilter != YFilter.not_set or
                    self.csltotaless.yfilter != YFilter.not_set or
                    self.csltotalsess.yfilter != YFilter.not_set or
                    self.csltotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cslTotalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cslTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csltotalcvs.is_set or self.csltotalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csltotalcvs.get_name_leafdata())
                if (self.csltotaless.is_set or self.csltotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csltotaless.get_name_leafdata())
                if (self.csltotalsess.is_set or self.csltotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csltotalsess.get_name_leafdata())
                if (self.csltotaluass.is_set or self.csltotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csltotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cslTotalCVs" or name == "cslTotalESs" or name == "cslTotalSESs" or name == "cslTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cslTotalCVs"):
                    self.csltotalcvs = value
                    self.csltotalcvs.value_namespace = name_space
                    self.csltotalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "cslTotalESs"):
                    self.csltotaless = value
                    self.csltotaless.value_namespace = name_space
                    self.csltotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cslTotalSESs"):
                    self.csltotalsess = value
                    self.csltotalsess.value_namespace = name_space
                    self.csltotalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cslTotalUASs"):
                    self.csltotaluass = value
                    self.csltotaluass.value_namespace = name_space
                    self.csltotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csltotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csltotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cslTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cslTotalEntry"):
                for c in self.csltotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csltotaltable.Csltotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csltotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cslTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cslfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Cslfarendtotaltable, self).__init__()

            self.yang_name = "cslFarEndTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.cslfarendtotalentry = YList(self)

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
                        super(CiscoSonetMib.Cslfarendtotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Cslfarendtotaltable, self).__setattr__(name, value)


        class Cslfarendtotalentry(Entity):
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
                super(CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry, self).__init__()

                self.yang_name = "cslFarEndTotalEntry"
                self.yang_parent_name = "cslFarEndTotalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cslfarendtotalcvs = YLeaf(YType.uint32, "cslFarEndTotalCVs")

                self.cslfarendtotaless = YLeaf(YType.uint32, "cslFarEndTotalESs")

                self.cslfarendtotalsess = YLeaf(YType.uint32, "cslFarEndTotalSESs")

                self.cslfarendtotaluass = YLeaf(YType.uint32, "cslFarEndTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cslfarendtotalcvs",
                                "cslfarendtotaless",
                                "cslfarendtotalsess",
                                "cslfarendtotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cslfarendtotalcvs.is_set or
                    self.cslfarendtotaless.is_set or
                    self.cslfarendtotalsess.is_set or
                    self.cslfarendtotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cslfarendtotalcvs.yfilter != YFilter.not_set or
                    self.cslfarendtotaless.yfilter != YFilter.not_set or
                    self.cslfarendtotalsess.yfilter != YFilter.not_set or
                    self.cslfarendtotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cslFarEndTotalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cslFarEndTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cslfarendtotalcvs.is_set or self.cslfarendtotalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslfarendtotalcvs.get_name_leafdata())
                if (self.cslfarendtotaless.is_set or self.cslfarendtotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslfarendtotaless.get_name_leafdata())
                if (self.cslfarendtotalsess.is_set or self.cslfarendtotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslfarendtotalsess.get_name_leafdata())
                if (self.cslfarendtotaluass.is_set or self.cslfarendtotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslfarendtotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cslFarEndTotalCVs" or name == "cslFarEndTotalESs" or name == "cslFarEndTotalSESs" or name == "cslFarEndTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cslFarEndTotalCVs"):
                    self.cslfarendtotalcvs = value
                    self.cslfarendtotalcvs.value_namespace = name_space
                    self.cslfarendtotalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "cslFarEndTotalESs"):
                    self.cslfarendtotaless = value
                    self.cslfarendtotaless.value_namespace = name_space
                    self.cslfarendtotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cslFarEndTotalSESs"):
                    self.cslfarendtotalsess = value
                    self.cslfarendtotalsess.value_namespace = name_space
                    self.cslfarendtotalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cslFarEndTotalUASs"):
                    self.cslfarendtotaluass = value
                    self.cslfarendtotaluass.value_namespace = name_space
                    self.cslfarendtotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cslfarendtotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cslfarendtotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cslFarEndTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cslFarEndTotalEntry"):
                for c in self.cslfarendtotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Cslfarendtotaltable.Cslfarendtotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cslfarendtotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cslFarEndTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csptotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csptotaltable.Csptotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csptotaltable, self).__init__()

            self.yang_name = "cspTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csptotalentry = YList(self)

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
                        super(CiscoSonetMib.Csptotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csptotaltable, self).__setattr__(name, value)


        class Csptotalentry(Entity):
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
                super(CiscoSonetMib.Csptotaltable.Csptotalentry, self).__init__()

                self.yang_name = "cspTotalEntry"
                self.yang_parent_name = "cspTotalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csptotalcvs = YLeaf(YType.uint32, "cspTotalCVs")

                self.csptotaless = YLeaf(YType.uint32, "cspTotalESs")

                self.csptotalsess = YLeaf(YType.uint32, "cspTotalSESs")

                self.csptotaluass = YLeaf(YType.uint32, "cspTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csptotalcvs",
                                "csptotaless",
                                "csptotalsess",
                                "csptotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csptotaltable.Csptotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csptotaltable.Csptotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csptotalcvs.is_set or
                    self.csptotaless.is_set or
                    self.csptotalsess.is_set or
                    self.csptotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csptotalcvs.yfilter != YFilter.not_set or
                    self.csptotaless.yfilter != YFilter.not_set or
                    self.csptotalsess.yfilter != YFilter.not_set or
                    self.csptotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cspTotalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cspTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csptotalcvs.is_set or self.csptotalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptotalcvs.get_name_leafdata())
                if (self.csptotaless.is_set or self.csptotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptotaless.get_name_leafdata())
                if (self.csptotalsess.is_set or self.csptotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptotalsess.get_name_leafdata())
                if (self.csptotaluass.is_set or self.csptotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cspTotalCVs" or name == "cspTotalESs" or name == "cspTotalSESs" or name == "cspTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTotalCVs"):
                    self.csptotalcvs = value
                    self.csptotalcvs.value_namespace = name_space
                    self.csptotalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTotalESs"):
                    self.csptotaless = value
                    self.csptotaless.value_namespace = name_space
                    self.csptotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTotalSESs"):
                    self.csptotalsess = value
                    self.csptotalsess.value_namespace = name_space
                    self.csptotalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTotalUASs"):
                    self.csptotaluass = value
                    self.csptotaluass.value_namespace = name_space
                    self.csptotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csptotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csptotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cspTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cspTotalEntry"):
                for c in self.csptotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csptotaltable.Csptotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csptotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cspTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cspfarendtotalentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Cspfarendtotaltable, self).__init__()

            self.yang_name = "cspFarEndTotalTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.cspfarendtotalentry = YList(self)

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
                        super(CiscoSonetMib.Cspfarendtotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Cspfarendtotaltable, self).__setattr__(name, value)


        class Cspfarendtotalentry(Entity):
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
                super(CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry, self).__init__()

                self.yang_name = "cspFarEndTotalEntry"
                self.yang_parent_name = "cspFarEndTotalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cspfarendtotalcvs = YLeaf(YType.uint32, "cspFarEndTotalCVs")

                self.cspfarendtotaless = YLeaf(YType.uint32, "cspFarEndTotalESs")

                self.cspfarendtotalsess = YLeaf(YType.uint32, "cspFarEndTotalSESs")

                self.cspfarendtotaluass = YLeaf(YType.uint32, "cspFarEndTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cspfarendtotalcvs",
                                "cspfarendtotaless",
                                "cspfarendtotalsess",
                                "cspfarendtotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cspfarendtotalcvs.is_set or
                    self.cspfarendtotaless.is_set or
                    self.cspfarendtotalsess.is_set or
                    self.cspfarendtotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cspfarendtotalcvs.yfilter != YFilter.not_set or
                    self.cspfarendtotaless.yfilter != YFilter.not_set or
                    self.cspfarendtotalsess.yfilter != YFilter.not_set or
                    self.cspfarendtotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cspFarEndTotalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cspFarEndTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cspfarendtotalcvs.is_set or self.cspfarendtotalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspfarendtotalcvs.get_name_leafdata())
                if (self.cspfarendtotaless.is_set or self.cspfarendtotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspfarendtotaless.get_name_leafdata())
                if (self.cspfarendtotalsess.is_set or self.cspfarendtotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspfarendtotalsess.get_name_leafdata())
                if (self.cspfarendtotaluass.is_set or self.cspfarendtotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspfarendtotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cspFarEndTotalCVs" or name == "cspFarEndTotalESs" or name == "cspFarEndTotalSESs" or name == "cspFarEndTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cspFarEndTotalCVs"):
                    self.cspfarendtotalcvs = value
                    self.cspfarendtotalcvs.value_namespace = name_space
                    self.cspfarendtotalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "cspFarEndTotalESs"):
                    self.cspfarendtotaless = value
                    self.cspfarendtotaless.value_namespace = name_space
                    self.cspfarendtotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cspFarEndTotalSESs"):
                    self.cspfarendtotalsess = value
                    self.cspfarendtotalsess.value_namespace = name_space
                    self.cspfarendtotalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cspFarEndTotalUASs"):
                    self.cspfarendtotaluass = value
                    self.cspfarendtotaluass.value_namespace = name_space
                    self.cspfarendtotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cspfarendtotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cspfarendtotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cspFarEndTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cspFarEndTotalEntry"):
                for c in self.cspfarendtotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Cspfarendtotaltable.Cspfarendtotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cspfarendtotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cspFarEndTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csptracetable(Entity):
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
            super(CiscoSonetMib.Csptracetable, self).__init__()

            self.yang_name = "cspTraceTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csptraceentry = YList(self)

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
                        super(CiscoSonetMib.Csptracetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csptracetable, self).__setattr__(name, value)


        class Csptraceentry(Entity):
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
                super(CiscoSonetMib.Csptracetable.Csptraceentry, self).__init__()

                self.yang_name = "cspTraceEntry"
                self.yang_parent_name = "cspTraceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csptracefailure = YLeaf(YType.boolean, "cspTraceFailure")

                self.csptracereceived = YLeaf(YType.str, "cspTraceReceived")

                self.csptracetoexpect = YLeaf(YType.str, "cspTraceToExpect")

                self.csptracetotransmit = YLeaf(YType.str, "cspTraceToTransmit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csptracefailure",
                                "csptracereceived",
                                "csptracetoexpect",
                                "csptracetotransmit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csptracetable.Csptraceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csptracetable.Csptraceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csptracefailure.is_set or
                    self.csptracereceived.is_set or
                    self.csptracetoexpect.is_set or
                    self.csptracetotransmit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csptracefailure.yfilter != YFilter.not_set or
                    self.csptracereceived.yfilter != YFilter.not_set or
                    self.csptracetoexpect.yfilter != YFilter.not_set or
                    self.csptracetotransmit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cspTraceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/cspTraceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csptracefailure.is_set or self.csptracefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptracefailure.get_name_leafdata())
                if (self.csptracereceived.is_set or self.csptracereceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptracereceived.get_name_leafdata())
                if (self.csptracetoexpect.is_set or self.csptracetoexpect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptracetoexpect.get_name_leafdata())
                if (self.csptracetotransmit.is_set or self.csptracetotransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptracetotransmit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cspTraceFailure" or name == "cspTraceReceived" or name == "cspTraceToExpect" or name == "cspTraceToTransmit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTraceFailure"):
                    self.csptracefailure = value
                    self.csptracefailure.value_namespace = name_space
                    self.csptracefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTraceReceived"):
                    self.csptracereceived = value
                    self.csptracereceived.value_namespace = name_space
                    self.csptracereceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTraceToExpect"):
                    self.csptracetoexpect = value
                    self.csptracetoexpect.value_namespace = name_space
                    self.csptracetoexpect.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTraceToTransmit"):
                    self.csptracetotransmit = value
                    self.csptracetotransmit.value_namespace = name_space
                    self.csptracetotransmit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csptraceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csptraceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cspTraceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cspTraceEntry"):
                for c in self.csptraceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csptracetable.Csptraceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csptraceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cspTraceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csstatstable(Entity):
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
            super(CiscoSonetMib.Csstatstable, self).__init__()

            self.yang_name = "csStatsTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csstatsentry = YList(self)

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
                        super(CiscoSonetMib.Csstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csstatstable, self).__setattr__(name, value)


        class Csstatsentry(Entity):
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
                super(CiscoSonetMib.Csstatstable.Csstatsentry, self).__init__()

                self.yang_name = "csStatsEntry"
                self.yang_parent_name = "csStatsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cslaiss = YLeaf(YType.uint32, "cslAISs")

                self.cslrfis = YLeaf(YType.uint32, "cslRFIs")

                self.cspaiss = YLeaf(YType.uint32, "cspAISs")

                self.csprfis = YLeaf(YType.uint32, "cspRFIs")

                self.csslofs = YLeaf(YType.uint32, "cssLOFs")

                self.cssloss = YLeaf(YType.uint32, "cssLOSs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cslaiss",
                                "cslrfis",
                                "cspaiss",
                                "csprfis",
                                "csslofs",
                                "cssloss") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csstatstable.Csstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csstatstable.Csstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cslaiss.is_set or
                    self.cslrfis.is_set or
                    self.cspaiss.is_set or
                    self.csprfis.is_set or
                    self.csslofs.is_set or
                    self.cssloss.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cslaiss.yfilter != YFilter.not_set or
                    self.cslrfis.yfilter != YFilter.not_set or
                    self.cspaiss.yfilter != YFilter.not_set or
                    self.csprfis.yfilter != YFilter.not_set or
                    self.csslofs.yfilter != YFilter.not_set or
                    self.cssloss.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csStatsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/csStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cslaiss.is_set or self.cslaiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslaiss.get_name_leafdata())
                if (self.cslrfis.is_set or self.cslrfis.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cslrfis.get_name_leafdata())
                if (self.cspaiss.is_set or self.cspaiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspaiss.get_name_leafdata())
                if (self.csprfis.is_set or self.csprfis.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csprfis.get_name_leafdata())
                if (self.csslofs.is_set or self.csslofs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csslofs.get_name_leafdata())
                if (self.cssloss.is_set or self.cssloss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cssloss.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cslAISs" or name == "cslRFIs" or name == "cspAISs" or name == "cspRFIs" or name == "cssLOFs" or name == "cssLOSs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cslAISs"):
                    self.cslaiss = value
                    self.cslaiss.value_namespace = name_space
                    self.cslaiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cslRFIs"):
                    self.cslrfis = value
                    self.cslrfis.value_namespace = name_space
                    self.cslrfis.value_namespace_prefix = name_space_prefix
                if(value_path == "cspAISs"):
                    self.cspaiss = value
                    self.cspaiss.value_namespace = name_space
                    self.cspaiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cspRFIs"):
                    self.csprfis = value
                    self.csprfis.value_namespace = name_space
                    self.csprfis.value_namespace_prefix = name_space_prefix
                if(value_path == "cssLOFs"):
                    self.csslofs = value
                    self.csslofs.value_namespace = name_space
                    self.csslofs.value_namespace_prefix = name_space_prefix
                if(value_path == "cssLOSs"):
                    self.cssloss = value
                    self.cssloss.value_namespace = name_space
                    self.cssloss.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csStatsEntry"):
                for c in self.csstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csstatstable.Csstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csau4Tug3Configentry <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry>`
        
        

        """

        _prefix = 'CISCO-SONET-MIB'
        _revision = '2003-03-07'

        def __init__(self):
            super(CiscoSonetMib.Csau4Tug3Configtable, self).__init__()

            self.yang_name = "csAu4Tug3ConfigTable"
            self.yang_parent_name = "CISCO-SONET-MIB"

            self.csau4tug3configentry = YList(self)

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
                        super(CiscoSonetMib.Csau4Tug3Configtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSonetMib.Csau4Tug3Configtable, self).__setattr__(name, value)


        class Csau4Tug3Configentry(Entity):
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
            	**type**\:   :py:class:`Csau4Tug3Payload <ydk.models.cisco_ios_xe.CISCO_SONET_MIB.CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry.Csau4Tug3Payload>`
            
            

            """

            _prefix = 'CISCO-SONET-MIB'
            _revision = '2003-03-07'

            def __init__(self):
                super(CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry, self).__init__()

                self.yang_name = "csAu4Tug3ConfigEntry"
                self.yang_parent_name = "csAu4Tug3ConfigTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csau4tug3 = YLeaf(YType.int32, "csAu4Tug3")

                self.csau4tug3payload = YLeaf(YType.enumeration, "csAu4Tug3Payload")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csau4tug3",
                                "csau4tug3payload") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry, self).__setattr__(name, value)

            class Csau4Tug3Payload(Enum):
                """
                Csau4Tug3Payload

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


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csau4tug3.is_set or
                    self.csau4tug3payload.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csau4tug3.yfilter != YFilter.not_set or
                    self.csau4tug3payload.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csAu4Tug3ConfigEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[csAu4Tug3='" + self.csau4tug3.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/csAu4Tug3ConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csau4tug3.is_set or self.csau4tug3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csau4tug3.get_name_leafdata())
                if (self.csau4tug3payload.is_set or self.csau4tug3payload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csau4tug3payload.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "csAu4Tug3" or name == "csAu4Tug3Payload"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csAu4Tug3"):
                    self.csau4tug3 = value
                    self.csau4tug3.value_namespace = name_space
                    self.csau4tug3.value_namespace_prefix = name_space_prefix
                if(value_path == "csAu4Tug3Payload"):
                    self.csau4tug3payload = value
                    self.csau4tug3payload.value_namespace = name_space
                    self.csau4tug3payload.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csau4tug3configentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csau4tug3configentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csAu4Tug3ConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csAu4Tug3ConfigEntry"):
                for c in self.csau4tug3configentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSonetMib.Csau4Tug3Configtable.Csau4Tug3Configentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csau4tug3configentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csAu4Tug3ConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.csapsconfig is not None and self.csapsconfig.has_data()) or
            (self.csapsconfigtable is not None and self.csapsconfigtable.has_data()) or
            (self.csau4tug3configtable is not None and self.csau4tug3configtable.has_data()) or
            (self.csconfigtable is not None and self.csconfigtable.has_data()) or
            (self.cslfarendtotaltable is not None and self.cslfarendtotaltable.has_data()) or
            (self.csltotaltable is not None and self.csltotaltable.has_data()) or
            (self.csnotifications is not None and self.csnotifications.has_data()) or
            (self.cspfarendtotaltable is not None and self.cspfarendtotaltable.has_data()) or
            (self.csptotaltable is not None and self.csptotaltable.has_data()) or
            (self.csptracetable is not None and self.csptracetable.has_data()) or
            (self.csstatstable is not None and self.csstatstable.has_data()) or
            (self.csstotaltable is not None and self.csstotaltable.has_data()) or
            (self.csstracetable is not None and self.csstracetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.csapsconfig is not None and self.csapsconfig.has_operation()) or
            (self.csapsconfigtable is not None and self.csapsconfigtable.has_operation()) or
            (self.csau4tug3configtable is not None and self.csau4tug3configtable.has_operation()) or
            (self.csconfigtable is not None and self.csconfigtable.has_operation()) or
            (self.cslfarendtotaltable is not None and self.cslfarendtotaltable.has_operation()) or
            (self.csltotaltable is not None and self.csltotaltable.has_operation()) or
            (self.csnotifications is not None and self.csnotifications.has_operation()) or
            (self.cspfarendtotaltable is not None and self.cspfarendtotaltable.has_operation()) or
            (self.csptotaltable is not None and self.csptotaltable.has_operation()) or
            (self.csptracetable is not None and self.csptracetable.has_operation()) or
            (self.csstatstable is not None and self.csstatstable.has_operation()) or
            (self.csstotaltable is not None and self.csstotaltable.has_operation()) or
            (self.csstracetable is not None and self.csstracetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-SONET-MIB:CISCO-SONET-MIB" + path_buffer

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

        if (child_yang_name == "csApsConfig"):
            if (self.csapsconfig is None):
                self.csapsconfig = CiscoSonetMib.Csapsconfig()
                self.csapsconfig.parent = self
                self._children_name_map["csapsconfig"] = "csApsConfig"
            return self.csapsconfig

        if (child_yang_name == "csApsConfigTable"):
            if (self.csapsconfigtable is None):
                self.csapsconfigtable = CiscoSonetMib.Csapsconfigtable()
                self.csapsconfigtable.parent = self
                self._children_name_map["csapsconfigtable"] = "csApsConfigTable"
            return self.csapsconfigtable

        if (child_yang_name == "csAu4Tug3ConfigTable"):
            if (self.csau4tug3configtable is None):
                self.csau4tug3configtable = CiscoSonetMib.Csau4Tug3Configtable()
                self.csau4tug3configtable.parent = self
                self._children_name_map["csau4tug3configtable"] = "csAu4Tug3ConfigTable"
            return self.csau4tug3configtable

        if (child_yang_name == "csConfigTable"):
            if (self.csconfigtable is None):
                self.csconfigtable = CiscoSonetMib.Csconfigtable()
                self.csconfigtable.parent = self
                self._children_name_map["csconfigtable"] = "csConfigTable"
            return self.csconfigtable

        if (child_yang_name == "cslFarEndTotalTable"):
            if (self.cslfarendtotaltable is None):
                self.cslfarendtotaltable = CiscoSonetMib.Cslfarendtotaltable()
                self.cslfarendtotaltable.parent = self
                self._children_name_map["cslfarendtotaltable"] = "cslFarEndTotalTable"
            return self.cslfarendtotaltable

        if (child_yang_name == "cslTotalTable"):
            if (self.csltotaltable is None):
                self.csltotaltable = CiscoSonetMib.Csltotaltable()
                self.csltotaltable.parent = self
                self._children_name_map["csltotaltable"] = "cslTotalTable"
            return self.csltotaltable

        if (child_yang_name == "csNotifications"):
            if (self.csnotifications is None):
                self.csnotifications = CiscoSonetMib.Csnotifications()
                self.csnotifications.parent = self
                self._children_name_map["csnotifications"] = "csNotifications"
            return self.csnotifications

        if (child_yang_name == "cspFarEndTotalTable"):
            if (self.cspfarendtotaltable is None):
                self.cspfarendtotaltable = CiscoSonetMib.Cspfarendtotaltable()
                self.cspfarendtotaltable.parent = self
                self._children_name_map["cspfarendtotaltable"] = "cspFarEndTotalTable"
            return self.cspfarendtotaltable

        if (child_yang_name == "cspTotalTable"):
            if (self.csptotaltable is None):
                self.csptotaltable = CiscoSonetMib.Csptotaltable()
                self.csptotaltable.parent = self
                self._children_name_map["csptotaltable"] = "cspTotalTable"
            return self.csptotaltable

        if (child_yang_name == "cspTraceTable"):
            if (self.csptracetable is None):
                self.csptracetable = CiscoSonetMib.Csptracetable()
                self.csptracetable.parent = self
                self._children_name_map["csptracetable"] = "cspTraceTable"
            return self.csptracetable

        if (child_yang_name == "csStatsTable"):
            if (self.csstatstable is None):
                self.csstatstable = CiscoSonetMib.Csstatstable()
                self.csstatstable.parent = self
                self._children_name_map["csstatstable"] = "csStatsTable"
            return self.csstatstable

        if (child_yang_name == "cssTotalTable"):
            if (self.csstotaltable is None):
                self.csstotaltable = CiscoSonetMib.Csstotaltable()
                self.csstotaltable.parent = self
                self._children_name_map["csstotaltable"] = "cssTotalTable"
            return self.csstotaltable

        if (child_yang_name == "cssTraceTable"):
            if (self.csstracetable is None):
                self.csstracetable = CiscoSonetMib.Csstracetable()
                self.csstracetable.parent = self
                self._children_name_map["csstracetable"] = "cssTraceTable"
            return self.csstracetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "csApsConfig" or name == "csApsConfigTable" or name == "csAu4Tug3ConfigTable" or name == "csConfigTable" or name == "cslFarEndTotalTable" or name == "cslTotalTable" or name == "csNotifications" or name == "cspFarEndTotalTable" or name == "cspTotalTable" or name == "cspTraceTable" or name == "csStatsTable" or name == "cssTotalTable" or name == "cssTraceTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoSonetMib()
        return self._top_entity

