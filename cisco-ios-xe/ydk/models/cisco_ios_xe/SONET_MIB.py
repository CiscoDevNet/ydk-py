""" SONET_MIB 

The MIB module to describe SONET/SDH interface objects.

Copyright (C) The Internet Society (2003).  This version
of this MIB module is part of RFC 3592;  see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SonetMib(Entity):
    """
    
    
    .. attribute:: sonetfarendlinecurrenttable
    
    	The SONET/SDH Far End Line Current table
    	**type**\:   :py:class:`Sonetfarendlinecurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendlinecurrenttable>`
    
    .. attribute:: sonetfarendlineintervaltable
    
    	The SONET/SDH Far End Line Interval table
    	**type**\:   :py:class:`Sonetfarendlineintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendlineintervaltable>`
    
    .. attribute:: sonetfarendpathcurrenttable
    
    	The SONET/SDH Far End Path Current table
    	**type**\:   :py:class:`Sonetfarendpathcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendpathcurrenttable>`
    
    .. attribute:: sonetfarendpathintervaltable
    
    	The SONET/SDH Far End Path Interval table
    	**type**\:   :py:class:`Sonetfarendpathintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendpathintervaltable>`
    
    .. attribute:: sonetfarendvtcurrenttable
    
    	The SONET/SDH Far End VT Current table
    	**type**\:   :py:class:`Sonetfarendvtcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendvtcurrenttable>`
    
    .. attribute:: sonetfarendvtintervaltable
    
    	The SONET/SDH Far End VT Interval table
    	**type**\:   :py:class:`Sonetfarendvtintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendvtintervaltable>`
    
    .. attribute:: sonetlinecurrenttable
    
    	The SONET/SDH Line Current table
    	**type**\:   :py:class:`Sonetlinecurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetlinecurrenttable>`
    
    .. attribute:: sonetlineintervaltable
    
    	The SONET/SDH Line Interval table
    	**type**\:   :py:class:`Sonetlineintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetlineintervaltable>`
    
    .. attribute:: sonetmedium
    
    	
    	**type**\:   :py:class:`Sonetmedium <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmedium>`
    
    .. attribute:: sonetmediumtable
    
    	The SONET/SDH Medium table
    	**type**\:   :py:class:`Sonetmediumtable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable>`
    
    .. attribute:: sonetpathcurrenttable
    
    	The SONET/SDH Path Current table
    	**type**\:   :py:class:`Sonetpathcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable>`
    
    .. attribute:: sonetpathintervaltable
    
    	The SONET/SDH Path Interval table
    	**type**\:   :py:class:`Sonetpathintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathintervaltable>`
    
    .. attribute:: sonetsectioncurrenttable
    
    	The SONET/SDH Section Current table
    	**type**\:   :py:class:`Sonetsectioncurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetsectioncurrenttable>`
    
    .. attribute:: sonetsectionintervaltable
    
    	The SONET/SDH Section Interval table
    	**type**\:   :py:class:`Sonetsectionintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetsectionintervaltable>`
    
    .. attribute:: sonetvtcurrenttable
    
    	The SONET/SDH VT Current table
    	**type**\:   :py:class:`Sonetvtcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetvtcurrenttable>`
    
    .. attribute:: sonetvtintervaltable
    
    	The SONET/SDH VT Interval table
    	**type**\:   :py:class:`Sonetvtintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetvtintervaltable>`
    
    

    """

    _prefix = 'SONET-MIB'
    _revision = '2003-08-11'

    def __init__(self):
        super(SonetMib, self).__init__()
        self._top_entity = None

        self.yang_name = "SONET-MIB"
        self.yang_parent_name = "SONET-MIB"

        self.sonetfarendlinecurrenttable = SonetMib.Sonetfarendlinecurrenttable()
        self.sonetfarendlinecurrenttable.parent = self
        self._children_name_map["sonetfarendlinecurrenttable"] = "sonetFarEndLineCurrentTable"
        self._children_yang_names.add("sonetFarEndLineCurrentTable")

        self.sonetfarendlineintervaltable = SonetMib.Sonetfarendlineintervaltable()
        self.sonetfarendlineintervaltable.parent = self
        self._children_name_map["sonetfarendlineintervaltable"] = "sonetFarEndLineIntervalTable"
        self._children_yang_names.add("sonetFarEndLineIntervalTable")

        self.sonetfarendpathcurrenttable = SonetMib.Sonetfarendpathcurrenttable()
        self.sonetfarendpathcurrenttable.parent = self
        self._children_name_map["sonetfarendpathcurrenttable"] = "sonetFarEndPathCurrentTable"
        self._children_yang_names.add("sonetFarEndPathCurrentTable")

        self.sonetfarendpathintervaltable = SonetMib.Sonetfarendpathintervaltable()
        self.sonetfarendpathintervaltable.parent = self
        self._children_name_map["sonetfarendpathintervaltable"] = "sonetFarEndPathIntervalTable"
        self._children_yang_names.add("sonetFarEndPathIntervalTable")

        self.sonetfarendvtcurrenttable = SonetMib.Sonetfarendvtcurrenttable()
        self.sonetfarendvtcurrenttable.parent = self
        self._children_name_map["sonetfarendvtcurrenttable"] = "sonetFarEndVTCurrentTable"
        self._children_yang_names.add("sonetFarEndVTCurrentTable")

        self.sonetfarendvtintervaltable = SonetMib.Sonetfarendvtintervaltable()
        self.sonetfarendvtintervaltable.parent = self
        self._children_name_map["sonetfarendvtintervaltable"] = "sonetFarEndVTIntervalTable"
        self._children_yang_names.add("sonetFarEndVTIntervalTable")

        self.sonetlinecurrenttable = SonetMib.Sonetlinecurrenttable()
        self.sonetlinecurrenttable.parent = self
        self._children_name_map["sonetlinecurrenttable"] = "sonetLineCurrentTable"
        self._children_yang_names.add("sonetLineCurrentTable")

        self.sonetlineintervaltable = SonetMib.Sonetlineintervaltable()
        self.sonetlineintervaltable.parent = self
        self._children_name_map["sonetlineintervaltable"] = "sonetLineIntervalTable"
        self._children_yang_names.add("sonetLineIntervalTable")

        self.sonetmedium = SonetMib.Sonetmedium()
        self.sonetmedium.parent = self
        self._children_name_map["sonetmedium"] = "sonetMedium"
        self._children_yang_names.add("sonetMedium")

        self.sonetmediumtable = SonetMib.Sonetmediumtable()
        self.sonetmediumtable.parent = self
        self._children_name_map["sonetmediumtable"] = "sonetMediumTable"
        self._children_yang_names.add("sonetMediumTable")

        self.sonetpathcurrenttable = SonetMib.Sonetpathcurrenttable()
        self.sonetpathcurrenttable.parent = self
        self._children_name_map["sonetpathcurrenttable"] = "sonetPathCurrentTable"
        self._children_yang_names.add("sonetPathCurrentTable")

        self.sonetpathintervaltable = SonetMib.Sonetpathintervaltable()
        self.sonetpathintervaltable.parent = self
        self._children_name_map["sonetpathintervaltable"] = "sonetPathIntervalTable"
        self._children_yang_names.add("sonetPathIntervalTable")

        self.sonetsectioncurrenttable = SonetMib.Sonetsectioncurrenttable()
        self.sonetsectioncurrenttable.parent = self
        self._children_name_map["sonetsectioncurrenttable"] = "sonetSectionCurrentTable"
        self._children_yang_names.add("sonetSectionCurrentTable")

        self.sonetsectionintervaltable = SonetMib.Sonetsectionintervaltable()
        self.sonetsectionintervaltable.parent = self
        self._children_name_map["sonetsectionintervaltable"] = "sonetSectionIntervalTable"
        self._children_yang_names.add("sonetSectionIntervalTable")

        self.sonetvtcurrenttable = SonetMib.Sonetvtcurrenttable()
        self.sonetvtcurrenttable.parent = self
        self._children_name_map["sonetvtcurrenttable"] = "sonetVTCurrentTable"
        self._children_yang_names.add("sonetVTCurrentTable")

        self.sonetvtintervaltable = SonetMib.Sonetvtintervaltable()
        self.sonetvtintervaltable.parent = self
        self._children_name_map["sonetvtintervaltable"] = "sonetVTIntervalTable"
        self._children_yang_names.add("sonetVTIntervalTable")


    class Sonetmedium(Entity):
        """
        
        
        .. attribute:: sonetsesthresholdset
        
        	An enumerated integer indicating which recognized set of SES thresholds that the agent uses for determining severely errored seconds and unavailable time.  other(1)   None of the following.  bellcore1991(2)   Bellcore TR\-NWT\-000253, 1991 [TR253], or   ANSI T1M1.3/93\-005R2, 1993 [T1M1.3].   See also Appendix B.  ansi1993(3)   ANSI T1.231, 1993 [T1.231a], or   Bellcore GR\-253\-CORE, Issue 2, 1995 [GR253]  itu1995(4)   ITU Recommendation G.826, 1995 [G.826]  ansi1997(5)   ANSI T1.231, 1997 [T1.231b]  If a manager changes the value of this object then the SES statistics collected prior to this change must be invalidated
        	**type**\:   :py:class:`Sonetsesthresholdset <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmedium.Sonetsesthresholdset>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetmedium, self).__init__()

            self.yang_name = "sonetMedium"
            self.yang_parent_name = "SONET-MIB"

            self.sonetsesthresholdset = YLeaf(YType.enumeration, "sonetSESthresholdSet")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("sonetsesthresholdset") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SonetMib.Sonetmedium, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetmedium, self).__setattr__(name, value)

        class Sonetsesthresholdset(Enum):
            """
            Sonetsesthresholdset

            An enumerated integer indicating which

            recognized set of SES thresholds that

            the agent uses for determining severely

            errored seconds and unavailable time.

            other(1)

              None of the following.

            bellcore1991(2)

              Bellcore TR\-NWT\-000253, 1991 [TR253], or

              ANSI T1M1.3/93\-005R2, 1993 [T1M1.3].

              See also Appendix B.

            ansi1993(3)

              ANSI T1.231, 1993 [T1.231a], or

              Bellcore GR\-253\-CORE, Issue 2, 1995 [GR253]

            itu1995(4)

              ITU Recommendation G.826, 1995 [G.826]

            ansi1997(5)

              ANSI T1.231, 1997 [T1.231b]

            If a manager changes the value of this

            object then the SES statistics collected

            prior to this change must be invalidated.

            .. data:: other = 1

            .. data:: bellcore1991 = 2

            .. data:: ansi1993 = 3

            .. data:: itu1995 = 4

            .. data:: ansi1997 = 5

            """

            other = Enum.YLeaf(1, "other")

            bellcore1991 = Enum.YLeaf(2, "bellcore1991")

            ansi1993 = Enum.YLeaf(3, "ansi1993")

            itu1995 = Enum.YLeaf(4, "itu1995")

            ansi1997 = Enum.YLeaf(5, "ansi1997")


        def has_data(self):
            return self.sonetsesthresholdset.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.sonetsesthresholdset.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetMedium" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.sonetsesthresholdset.is_set or self.sonetsesthresholdset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sonetsesthresholdset.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetSESthresholdSet"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "sonetSESthresholdSet"):
                self.sonetsesthresholdset = value
                self.sonetsesthresholdset.value_namespace = name_space
                self.sonetsesthresholdset.value_namespace_prefix = name_space_prefix


    class Sonetmediumtable(Entity):
        """
        The SONET/SDH Medium table.
        
        .. attribute:: sonetmediumentry
        
        	An entry in the SONET/SDH Medium table
        	**type**\: list of    :py:class:`Sonetmediumentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable.Sonetmediumentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetmediumtable, self).__init__()

            self.yang_name = "sonetMediumTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetmediumentry = YList(self)

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
                        super(SonetMib.Sonetmediumtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetmediumtable, self).__setattr__(name, value)


        class Sonetmediumentry(Entity):
            """
            An entry in the SONET/SDH Medium table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetmediumcircuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting. Note that the circuit identifier, if available, is also represented by ifPhysAddress
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: sonetmediuminvalidintervals
            
            	The number of intervals in the range from 0 to sonetMediumValidIntervals for which no data is available. This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\:  int
            
            	**range:** 0..96
            
            .. attribute:: sonetmediumlinecoding
            
            	This variable describes the line coding for this interface. The B3ZS and CMI are used for electrical SONET/SDH signals (STS\-1 and STS\-3). The Non\-Return to Zero (NRZ) and the Return to Zero are used for optical SONET/SDH signals
            	**type**\:   :py:class:`Sonetmediumlinecoding <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable.Sonetmediumentry.Sonetmediumlinecoding>`
            
            .. attribute:: sonetmediumlinetype
            
            	This variable describes the line type for this interface. The line types are Short and Long Range Single Mode fiber or Multi\-Mode fiber interfaces, and coax and UTP for electrical interfaces.  The value sonetOther should be used when the Line Type is not one of the listed values
            	**type**\:   :py:class:`Sonetmediumlinetype <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable.Sonetmediumentry.Sonetmediumlinetype>`
            
            .. attribute:: sonetmediumloopbackconfig
            
            	The current loopback state of the SONET/SDH interface.  The values mean\:    sonetNoLoop      Not in the loopback state. A device that is not      capable of performing a loopback on this interface      shall always return this value.    sonetFacilityLoop      The received signal at this interface is looped back      out through the corresponding transmitter in the return      direction.    sonetTerminalLoop      The signal that is about to be transmitted is connected      to the associated incoming receiver.    sonetOtherLoop      Loopbacks that are not defined here
            	**type**\:   :py:class:`Sonetmediumloopbackconfig <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable.Sonetmediumentry.Sonetmediumloopbackconfig>`
            
            .. attribute:: sonetmediumtimeelapsed
            
            	The number of seconds, including partial seconds, that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 1..900
            
            .. attribute:: sonetmediumtype
            
            	This variable identifies whether a SONET or a SDH signal is used across this interface
            	**type**\:   :py:class:`Sonetmediumtype <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetmediumtable.Sonetmediumentry.Sonetmediumtype>`
            
            .. attribute:: sonetmediumvalidintervals
            
            	The number of previous 15\-minute intervals for which data was collected. A SONET/SDH interface must be capable of supporting at least n intervals. The minimum value of n is 4. The default of n is 32. The maximum value of n is 96. The value will be <n> unless the measurement was (re\-)started within the last (<n>\*15) minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases (e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available. 
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetmediumtable.Sonetmediumentry, self).__init__()

                self.yang_name = "sonetMediumEntry"
                self.yang_parent_name = "sonetMediumTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetmediumcircuitidentifier = YLeaf(YType.str, "sonetMediumCircuitIdentifier")

                self.sonetmediuminvalidintervals = YLeaf(YType.int32, "sonetMediumInvalidIntervals")

                self.sonetmediumlinecoding = YLeaf(YType.enumeration, "sonetMediumLineCoding")

                self.sonetmediumlinetype = YLeaf(YType.enumeration, "sonetMediumLineType")

                self.sonetmediumloopbackconfig = YLeaf(YType.bits, "sonetMediumLoopbackConfig")

                self.sonetmediumtimeelapsed = YLeaf(YType.int32, "sonetMediumTimeElapsed")

                self.sonetmediumtype = YLeaf(YType.enumeration, "sonetMediumType")

                self.sonetmediumvalidintervals = YLeaf(YType.int32, "sonetMediumValidIntervals")

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
                                "sonetmediumcircuitidentifier",
                                "sonetmediuminvalidintervals",
                                "sonetmediumlinecoding",
                                "sonetmediumlinetype",
                                "sonetmediumloopbackconfig",
                                "sonetmediumtimeelapsed",
                                "sonetmediumtype",
                                "sonetmediumvalidintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetmediumtable.Sonetmediumentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetmediumtable.Sonetmediumentry, self).__setattr__(name, value)

            class Sonetmediumlinecoding(Enum):
                """
                Sonetmediumlinecoding

                This variable describes the line coding for

                this interface. The B3ZS and CMI are used for

                electrical SONET/SDH signals (STS\-1 and STS\-3).

                The Non\-Return to Zero (NRZ) and the Return

                to Zero are used for optical SONET/SDH signals.

                .. data:: sonetMediumOther = 1

                .. data:: sonetMediumB3ZS = 2

                .. data:: sonetMediumCMI = 3

                .. data:: sonetMediumNRZ = 4

                .. data:: sonetMediumRZ = 5

                """

                sonetMediumOther = Enum.YLeaf(1, "sonetMediumOther")

                sonetMediumB3ZS = Enum.YLeaf(2, "sonetMediumB3ZS")

                sonetMediumCMI = Enum.YLeaf(3, "sonetMediumCMI")

                sonetMediumNRZ = Enum.YLeaf(4, "sonetMediumNRZ")

                sonetMediumRZ = Enum.YLeaf(5, "sonetMediumRZ")


            class Sonetmediumlinetype(Enum):
                """
                Sonetmediumlinetype

                This variable describes the line type for

                this interface. The line types are

                Short and Long Range

                Single Mode fiber or Multi\-Mode fiber interfaces,

                and coax and UTP for electrical interfaces.  The

                value sonetOther should be used when the Line Type is

                not one of the listed values.

                .. data:: sonetOther = 1

                .. data:: sonetShortSingleMode = 2

                .. data:: sonetLongSingleMode = 3

                .. data:: sonetMultiMode = 4

                .. data:: sonetCoax = 5

                .. data:: sonetUTP = 6

                """

                sonetOther = Enum.YLeaf(1, "sonetOther")

                sonetShortSingleMode = Enum.YLeaf(2, "sonetShortSingleMode")

                sonetLongSingleMode = Enum.YLeaf(3, "sonetLongSingleMode")

                sonetMultiMode = Enum.YLeaf(4, "sonetMultiMode")

                sonetCoax = Enum.YLeaf(5, "sonetCoax")

                sonetUTP = Enum.YLeaf(6, "sonetUTP")


            class Sonetmediumtype(Enum):
                """
                Sonetmediumtype

                This variable identifies whether a SONET

                or a SDH signal is used across this interface.

                .. data:: sonet = 1

                .. data:: sdh = 2

                """

                sonet = Enum.YLeaf(1, "sonet")

                sdh = Enum.YLeaf(2, "sdh")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetmediumcircuitidentifier.is_set or
                    self.sonetmediuminvalidintervals.is_set or
                    self.sonetmediumlinecoding.is_set or
                    self.sonetmediumlinetype.is_set or
                    self.sonetmediumloopbackconfig.is_set or
                    self.sonetmediumtimeelapsed.is_set or
                    self.sonetmediumtype.is_set or
                    self.sonetmediumvalidintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetmediumcircuitidentifier.yfilter != YFilter.not_set or
                    self.sonetmediuminvalidintervals.yfilter != YFilter.not_set or
                    self.sonetmediumlinecoding.yfilter != YFilter.not_set or
                    self.sonetmediumlinetype.yfilter != YFilter.not_set or
                    self.sonetmediumloopbackconfig.yfilter != YFilter.not_set or
                    self.sonetmediumtimeelapsed.yfilter != YFilter.not_set or
                    self.sonetmediumtype.yfilter != YFilter.not_set or
                    self.sonetmediumvalidintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetMediumEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetMediumTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetmediumcircuitidentifier.is_set or self.sonetmediumcircuitidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumcircuitidentifier.get_name_leafdata())
                if (self.sonetmediuminvalidintervals.is_set or self.sonetmediuminvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediuminvalidintervals.get_name_leafdata())
                if (self.sonetmediumlinecoding.is_set or self.sonetmediumlinecoding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumlinecoding.get_name_leafdata())
                if (self.sonetmediumlinetype.is_set or self.sonetmediumlinetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumlinetype.get_name_leafdata())
                if (self.sonetmediumloopbackconfig.is_set or self.sonetmediumloopbackconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumloopbackconfig.get_name_leafdata())
                if (self.sonetmediumtimeelapsed.is_set or self.sonetmediumtimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumtimeelapsed.get_name_leafdata())
                if (self.sonetmediumtype.is_set or self.sonetmediumtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumtype.get_name_leafdata())
                if (self.sonetmediumvalidintervals.is_set or self.sonetmediumvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetmediumvalidintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetMediumCircuitIdentifier" or name == "sonetMediumInvalidIntervals" or name == "sonetMediumLineCoding" or name == "sonetMediumLineType" or name == "sonetMediumLoopbackConfig" or name == "sonetMediumTimeElapsed" or name == "sonetMediumType" or name == "sonetMediumValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumCircuitIdentifier"):
                    self.sonetmediumcircuitidentifier = value
                    self.sonetmediumcircuitidentifier.value_namespace = name_space
                    self.sonetmediumcircuitidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumInvalidIntervals"):
                    self.sonetmediuminvalidintervals = value
                    self.sonetmediuminvalidintervals.value_namespace = name_space
                    self.sonetmediuminvalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumLineCoding"):
                    self.sonetmediumlinecoding = value
                    self.sonetmediumlinecoding.value_namespace = name_space
                    self.sonetmediumlinecoding.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumLineType"):
                    self.sonetmediumlinetype = value
                    self.sonetmediumlinetype.value_namespace = name_space
                    self.sonetmediumlinetype.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumLoopbackConfig"):
                    self.sonetmediumloopbackconfig[value] = True
                if(value_path == "sonetMediumTimeElapsed"):
                    self.sonetmediumtimeelapsed = value
                    self.sonetmediumtimeelapsed.value_namespace = name_space
                    self.sonetmediumtimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumType"):
                    self.sonetmediumtype = value
                    self.sonetmediumtype.value_namespace = name_space
                    self.sonetmediumtype.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetMediumValidIntervals"):
                    self.sonetmediumvalidintervals = value
                    self.sonetmediumvalidintervals.value_namespace = name_space
                    self.sonetmediumvalidintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetmediumentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetmediumentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetMediumTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetMediumEntry"):
                for c in self.sonetmediumentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetmediumtable.Sonetmediumentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetmediumentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetMediumEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetsectioncurrenttable(Entity):
        """
        The SONET/SDH Section Current table.
        
        .. attribute:: sonetsectioncurrententry
        
        	An entry in the SONET/SDH Section Current table
        	**type**\: list of    :py:class:`Sonetsectioncurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetsectioncurrenttable, self).__init__()

            self.yang_name = "sonetSectionCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetsectioncurrententry = YList(self)

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
                        super(SonetMib.Sonetsectioncurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetsectioncurrenttable, self).__setattr__(name, value)


        class Sonetsectioncurrententry(Entity):
            """
            An entry in the SONET/SDH Section Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetsectioncurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentstatus
            
            	This variable indicates the status of the interface. The sonetSectionCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetSectionNoDefect should be set if and only if no other flag is set.  The various bit positions are\:       1   sonetSectionNoDefect       2   sonetSectionLOS       4   sonetSectionLOF
            	**type**\:  int
            
            	**range:** 1..6
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry, self).__init__()

                self.yang_name = "sonetSectionCurrentEntry"
                self.yang_parent_name = "sonetSectionCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetsectioncurrentcvs = YLeaf(YType.uint32, "sonetSectionCurrentCVs")

                self.sonetsectioncurrentess = YLeaf(YType.uint32, "sonetSectionCurrentESs")

                self.sonetsectioncurrentsefss = YLeaf(YType.uint32, "sonetSectionCurrentSEFSs")

                self.sonetsectioncurrentsess = YLeaf(YType.uint32, "sonetSectionCurrentSESs")

                self.sonetsectioncurrentstatus = YLeaf(YType.int32, "sonetSectionCurrentStatus")

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
                                "sonetsectioncurrentcvs",
                                "sonetsectioncurrentess",
                                "sonetsectioncurrentsefss",
                                "sonetsectioncurrentsess",
                                "sonetsectioncurrentstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetsectioncurrentcvs.is_set or
                    self.sonetsectioncurrentess.is_set or
                    self.sonetsectioncurrentsefss.is_set or
                    self.sonetsectioncurrentsess.is_set or
                    self.sonetsectioncurrentstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetsectioncurrentcvs.yfilter != YFilter.not_set or
                    self.sonetsectioncurrentess.yfilter != YFilter.not_set or
                    self.sonetsectioncurrentsefss.yfilter != YFilter.not_set or
                    self.sonetsectioncurrentsess.yfilter != YFilter.not_set or
                    self.sonetsectioncurrentstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetSectionCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetSectionCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetsectioncurrentcvs.is_set or self.sonetsectioncurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectioncurrentcvs.get_name_leafdata())
                if (self.sonetsectioncurrentess.is_set or self.sonetsectioncurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectioncurrentess.get_name_leafdata())
                if (self.sonetsectioncurrentsefss.is_set or self.sonetsectioncurrentsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectioncurrentsefss.get_name_leafdata())
                if (self.sonetsectioncurrentsess.is_set or self.sonetsectioncurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectioncurrentsess.get_name_leafdata())
                if (self.sonetsectioncurrentstatus.is_set or self.sonetsectioncurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectioncurrentstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetSectionCurrentCVs" or name == "sonetSectionCurrentESs" or name == "sonetSectionCurrentSEFSs" or name == "sonetSectionCurrentSESs" or name == "sonetSectionCurrentStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionCurrentCVs"):
                    self.sonetsectioncurrentcvs = value
                    self.sonetsectioncurrentcvs.value_namespace = name_space
                    self.sonetsectioncurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionCurrentESs"):
                    self.sonetsectioncurrentess = value
                    self.sonetsectioncurrentess.value_namespace = name_space
                    self.sonetsectioncurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionCurrentSEFSs"):
                    self.sonetsectioncurrentsefss = value
                    self.sonetsectioncurrentsefss.value_namespace = name_space
                    self.sonetsectioncurrentsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionCurrentSESs"):
                    self.sonetsectioncurrentsess = value
                    self.sonetsectioncurrentsess.value_namespace = name_space
                    self.sonetsectioncurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionCurrentStatus"):
                    self.sonetsectioncurrentstatus = value
                    self.sonetsectioncurrentstatus.value_namespace = name_space
                    self.sonetsectioncurrentstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetsectioncurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetsectioncurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetSectionCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetSectionCurrentEntry"):
                for c in self.sonetsectioncurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetsectioncurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetSectionCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetsectionintervaltable(Entity):
        """
        The SONET/SDH Section Interval table.
        
        .. attribute:: sonetsectionintervalentry
        
        	An entry in the SONET/SDH Section Interval table
        	**type**\: list of    :py:class:`Sonetsectionintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetsectionintervaltable, self).__init__()

            self.yang_name = "sonetSectionIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetsectionintervalentry = YList(self)

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
                        super(SonetMib.Sonetsectionintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetsectionintervaltable, self).__setattr__(name, value)


        class Sonetsectionintervalentry(Entity):
            """
            An entry in the SONET/SDH Section Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetsectionintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetsectionintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry, self).__init__()

                self.yang_name = "sonetSectionIntervalEntry"
                self.yang_parent_name = "sonetSectionIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetsectionintervalnumber = YLeaf(YType.int32, "sonetSectionIntervalNumber")

                self.sonetsectionintervalcvs = YLeaf(YType.uint32, "sonetSectionIntervalCVs")

                self.sonetsectionintervaless = YLeaf(YType.uint32, "sonetSectionIntervalESs")

                self.sonetsectionintervalsefss = YLeaf(YType.uint32, "sonetSectionIntervalSEFSs")

                self.sonetsectionintervalsess = YLeaf(YType.uint32, "sonetSectionIntervalSESs")

                self.sonetsectionintervalvaliddata = YLeaf(YType.boolean, "sonetSectionIntervalValidData")

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
                                "sonetsectionintervalnumber",
                                "sonetsectionintervalcvs",
                                "sonetsectionintervaless",
                                "sonetsectionintervalsefss",
                                "sonetsectionintervalsess",
                                "sonetsectionintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetsectionintervalnumber.is_set or
                    self.sonetsectionintervalcvs.is_set or
                    self.sonetsectionintervaless.is_set or
                    self.sonetsectionintervalsefss.is_set or
                    self.sonetsectionintervalsess.is_set or
                    self.sonetsectionintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetsectionintervalnumber.yfilter != YFilter.not_set or
                    self.sonetsectionintervalcvs.yfilter != YFilter.not_set or
                    self.sonetsectionintervaless.yfilter != YFilter.not_set or
                    self.sonetsectionintervalsefss.yfilter != YFilter.not_set or
                    self.sonetsectionintervalsess.yfilter != YFilter.not_set or
                    self.sonetsectionintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetSectionIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetSectionIntervalNumber='" + self.sonetsectionintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetSectionIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetsectionintervalnumber.is_set or self.sonetsectionintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervalnumber.get_name_leafdata())
                if (self.sonetsectionintervalcvs.is_set or self.sonetsectionintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervalcvs.get_name_leafdata())
                if (self.sonetsectionintervaless.is_set or self.sonetsectionintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervaless.get_name_leafdata())
                if (self.sonetsectionintervalsefss.is_set or self.sonetsectionintervalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervalsefss.get_name_leafdata())
                if (self.sonetsectionintervalsess.is_set or self.sonetsectionintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervalsess.get_name_leafdata())
                if (self.sonetsectionintervalvaliddata.is_set or self.sonetsectionintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetsectionintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetSectionIntervalNumber" or name == "sonetSectionIntervalCVs" or name == "sonetSectionIntervalESs" or name == "sonetSectionIntervalSEFSs" or name == "sonetSectionIntervalSESs" or name == "sonetSectionIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalNumber"):
                    self.sonetsectionintervalnumber = value
                    self.sonetsectionintervalnumber.value_namespace = name_space
                    self.sonetsectionintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalCVs"):
                    self.sonetsectionintervalcvs = value
                    self.sonetsectionintervalcvs.value_namespace = name_space
                    self.sonetsectionintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalESs"):
                    self.sonetsectionintervaless = value
                    self.sonetsectionintervaless.value_namespace = name_space
                    self.sonetsectionintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalSEFSs"):
                    self.sonetsectionintervalsefss = value
                    self.sonetsectionintervalsefss.value_namespace = name_space
                    self.sonetsectionintervalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalSESs"):
                    self.sonetsectionintervalsess = value
                    self.sonetsectionintervalsess.value_namespace = name_space
                    self.sonetsectionintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetSectionIntervalValidData"):
                    self.sonetsectionintervalvaliddata = value
                    self.sonetsectionintervalvaliddata.value_namespace = name_space
                    self.sonetsectionintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetsectionintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetsectionintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetSectionIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetSectionIntervalEntry"):
                for c in self.sonetsectionintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetsectionintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetSectionIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetlinecurrenttable(Entity):
        """
        The SONET/SDH Line Current table.
        
        .. attribute:: sonetlinecurrententry
        
        	An entry in the SONET/SDH Line Current table
        	**type**\: list of    :py:class:`Sonetlinecurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetlinecurrenttable, self).__init__()

            self.yang_name = "sonetLineCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetlinecurrententry = YList(self)

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
                        super(SonetMib.Sonetlinecurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetlinecurrenttable, self).__setattr__(name, value)


        class Sonetlinecurrententry(Entity):
            """
            An entry in the SONET/SDH Line Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetlinecurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentstatus
            
            	This variable indicates the status of the interface. The sonetLineCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetLineNoDefect should be set if and only if no other flag is set.  The various bit positions are\:  1   sonetLineNoDefect  2   sonetLineAIS  4   sonetLineRDI
            	**type**\:  int
            
            	**range:** 1..6
            
            .. attribute:: sonetlinecurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry, self).__init__()

                self.yang_name = "sonetLineCurrentEntry"
                self.yang_parent_name = "sonetLineCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetlinecurrentcvs = YLeaf(YType.uint32, "sonetLineCurrentCVs")

                self.sonetlinecurrentess = YLeaf(YType.uint32, "sonetLineCurrentESs")

                self.sonetlinecurrentsess = YLeaf(YType.uint32, "sonetLineCurrentSESs")

                self.sonetlinecurrentstatus = YLeaf(YType.int32, "sonetLineCurrentStatus")

                self.sonetlinecurrentuass = YLeaf(YType.uint32, "sonetLineCurrentUASs")

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
                                "sonetlinecurrentcvs",
                                "sonetlinecurrentess",
                                "sonetlinecurrentsess",
                                "sonetlinecurrentstatus",
                                "sonetlinecurrentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetlinecurrentcvs.is_set or
                    self.sonetlinecurrentess.is_set or
                    self.sonetlinecurrentsess.is_set or
                    self.sonetlinecurrentstatus.is_set or
                    self.sonetlinecurrentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetlinecurrentcvs.yfilter != YFilter.not_set or
                    self.sonetlinecurrentess.yfilter != YFilter.not_set or
                    self.sonetlinecurrentsess.yfilter != YFilter.not_set or
                    self.sonetlinecurrentstatus.yfilter != YFilter.not_set or
                    self.sonetlinecurrentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetLineCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetLineCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetlinecurrentcvs.is_set or self.sonetlinecurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlinecurrentcvs.get_name_leafdata())
                if (self.sonetlinecurrentess.is_set or self.sonetlinecurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlinecurrentess.get_name_leafdata())
                if (self.sonetlinecurrentsess.is_set or self.sonetlinecurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlinecurrentsess.get_name_leafdata())
                if (self.sonetlinecurrentstatus.is_set or self.sonetlinecurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlinecurrentstatus.get_name_leafdata())
                if (self.sonetlinecurrentuass.is_set or self.sonetlinecurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlinecurrentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetLineCurrentCVs" or name == "sonetLineCurrentESs" or name == "sonetLineCurrentSESs" or name == "sonetLineCurrentStatus" or name == "sonetLineCurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineCurrentCVs"):
                    self.sonetlinecurrentcvs = value
                    self.sonetlinecurrentcvs.value_namespace = name_space
                    self.sonetlinecurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineCurrentESs"):
                    self.sonetlinecurrentess = value
                    self.sonetlinecurrentess.value_namespace = name_space
                    self.sonetlinecurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineCurrentSESs"):
                    self.sonetlinecurrentsess = value
                    self.sonetlinecurrentsess.value_namespace = name_space
                    self.sonetlinecurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineCurrentStatus"):
                    self.sonetlinecurrentstatus = value
                    self.sonetlinecurrentstatus.value_namespace = name_space
                    self.sonetlinecurrentstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineCurrentUASs"):
                    self.sonetlinecurrentuass = value
                    self.sonetlinecurrentuass.value_namespace = name_space
                    self.sonetlinecurrentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetlinecurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetlinecurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetLineCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetLineCurrentEntry"):
                for c in self.sonetlinecurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetlinecurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetLineCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetlineintervaltable(Entity):
        """
        The SONET/SDH Line Interval table.
        
        .. attribute:: sonetlineintervalentry
        
        	An entry in the SONET/SDH Line Interval table
        	**type**\: list of    :py:class:`Sonetlineintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetlineintervaltable.Sonetlineintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetlineintervaltable, self).__init__()

            self.yang_name = "sonetLineIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetlineintervalentry = YList(self)

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
                        super(SonetMib.Sonetlineintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetlineintervaltable, self).__setattr__(name, value)


        class Sonetlineintervalentry(Entity):
            """
            An entry in the SONET/SDH Line Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetlineintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetlineintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetlineintervaltable.Sonetlineintervalentry, self).__init__()

                self.yang_name = "sonetLineIntervalEntry"
                self.yang_parent_name = "sonetLineIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetlineintervalnumber = YLeaf(YType.int32, "sonetLineIntervalNumber")

                self.sonetlineintervalcvs = YLeaf(YType.uint32, "sonetLineIntervalCVs")

                self.sonetlineintervaless = YLeaf(YType.uint32, "sonetLineIntervalESs")

                self.sonetlineintervalsess = YLeaf(YType.uint32, "sonetLineIntervalSESs")

                self.sonetlineintervaluass = YLeaf(YType.uint32, "sonetLineIntervalUASs")

                self.sonetlineintervalvaliddata = YLeaf(YType.boolean, "sonetLineIntervalValidData")

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
                                "sonetlineintervalnumber",
                                "sonetlineintervalcvs",
                                "sonetlineintervaless",
                                "sonetlineintervalsess",
                                "sonetlineintervaluass",
                                "sonetlineintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetlineintervaltable.Sonetlineintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetlineintervaltable.Sonetlineintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetlineintervalnumber.is_set or
                    self.sonetlineintervalcvs.is_set or
                    self.sonetlineintervaless.is_set or
                    self.sonetlineintervalsess.is_set or
                    self.sonetlineintervaluass.is_set or
                    self.sonetlineintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetlineintervalnumber.yfilter != YFilter.not_set or
                    self.sonetlineintervalcvs.yfilter != YFilter.not_set or
                    self.sonetlineintervaless.yfilter != YFilter.not_set or
                    self.sonetlineintervalsess.yfilter != YFilter.not_set or
                    self.sonetlineintervaluass.yfilter != YFilter.not_set or
                    self.sonetlineintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetLineIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetLineIntervalNumber='" + self.sonetlineintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetLineIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetlineintervalnumber.is_set or self.sonetlineintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervalnumber.get_name_leafdata())
                if (self.sonetlineintervalcvs.is_set or self.sonetlineintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervalcvs.get_name_leafdata())
                if (self.sonetlineintervaless.is_set or self.sonetlineintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervaless.get_name_leafdata())
                if (self.sonetlineintervalsess.is_set or self.sonetlineintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervalsess.get_name_leafdata())
                if (self.sonetlineintervaluass.is_set or self.sonetlineintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervaluass.get_name_leafdata())
                if (self.sonetlineintervalvaliddata.is_set or self.sonetlineintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetlineintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetLineIntervalNumber" or name == "sonetLineIntervalCVs" or name == "sonetLineIntervalESs" or name == "sonetLineIntervalSESs" or name == "sonetLineIntervalUASs" or name == "sonetLineIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalNumber"):
                    self.sonetlineintervalnumber = value
                    self.sonetlineintervalnumber.value_namespace = name_space
                    self.sonetlineintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalCVs"):
                    self.sonetlineintervalcvs = value
                    self.sonetlineintervalcvs.value_namespace = name_space
                    self.sonetlineintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalESs"):
                    self.sonetlineintervaless = value
                    self.sonetlineintervaless.value_namespace = name_space
                    self.sonetlineintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalSESs"):
                    self.sonetlineintervalsess = value
                    self.sonetlineintervalsess.value_namespace = name_space
                    self.sonetlineintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalUASs"):
                    self.sonetlineintervaluass = value
                    self.sonetlineintervaluass.value_namespace = name_space
                    self.sonetlineintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetLineIntervalValidData"):
                    self.sonetlineintervalvaliddata = value
                    self.sonetlineintervalvaliddata.value_namespace = name_space
                    self.sonetlineintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetlineintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetlineintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetLineIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetLineIntervalEntry"):
                for c in self.sonetlineintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetlineintervaltable.Sonetlineintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetlineintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetLineIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendlinecurrenttable(Entity):
        """
        The SONET/SDH Far End Line Current table.
        
        .. attribute:: sonetfarendlinecurrententry
        
        	An entry in the SONET/SDH Far End Line Current table
        	**type**\: list of    :py:class:`Sonetfarendlinecurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendlinecurrenttable, self).__init__()

            self.yang_name = "sonetFarEndLineCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendlinecurrententry = YList(self)

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
                        super(SonetMib.Sonetfarendlinecurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendlinecurrenttable, self).__setattr__(name, value)


        class Sonetfarendlinecurrententry(Entity):
            """
            An entry in the SONET/SDH Far End Line Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendlinecurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry, self).__init__()

                self.yang_name = "sonetFarEndLineCurrentEntry"
                self.yang_parent_name = "sonetFarEndLineCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendlinecurrentcvs = YLeaf(YType.uint32, "sonetFarEndLineCurrentCVs")

                self.sonetfarendlinecurrentess = YLeaf(YType.uint32, "sonetFarEndLineCurrentESs")

                self.sonetfarendlinecurrentsess = YLeaf(YType.uint32, "sonetFarEndLineCurrentSESs")

                self.sonetfarendlinecurrentuass = YLeaf(YType.uint32, "sonetFarEndLineCurrentUASs")

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
                                "sonetfarendlinecurrentcvs",
                                "sonetfarendlinecurrentess",
                                "sonetfarendlinecurrentsess",
                                "sonetfarendlinecurrentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendlinecurrentcvs.is_set or
                    self.sonetfarendlinecurrentess.is_set or
                    self.sonetfarendlinecurrentsess.is_set or
                    self.sonetfarendlinecurrentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendlinecurrentcvs.yfilter != YFilter.not_set or
                    self.sonetfarendlinecurrentess.yfilter != YFilter.not_set or
                    self.sonetfarendlinecurrentsess.yfilter != YFilter.not_set or
                    self.sonetfarendlinecurrentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndLineCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndLineCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendlinecurrentcvs.is_set or self.sonetfarendlinecurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlinecurrentcvs.get_name_leafdata())
                if (self.sonetfarendlinecurrentess.is_set or self.sonetfarendlinecurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlinecurrentess.get_name_leafdata())
                if (self.sonetfarendlinecurrentsess.is_set or self.sonetfarendlinecurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlinecurrentsess.get_name_leafdata())
                if (self.sonetfarendlinecurrentuass.is_set or self.sonetfarendlinecurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlinecurrentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndLineCurrentCVs" or name == "sonetFarEndLineCurrentESs" or name == "sonetFarEndLineCurrentSESs" or name == "sonetFarEndLineCurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineCurrentCVs"):
                    self.sonetfarendlinecurrentcvs = value
                    self.sonetfarendlinecurrentcvs.value_namespace = name_space
                    self.sonetfarendlinecurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineCurrentESs"):
                    self.sonetfarendlinecurrentess = value
                    self.sonetfarendlinecurrentess.value_namespace = name_space
                    self.sonetfarendlinecurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineCurrentSESs"):
                    self.sonetfarendlinecurrentsess = value
                    self.sonetfarendlinecurrentsess.value_namespace = name_space
                    self.sonetfarendlinecurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineCurrentUASs"):
                    self.sonetfarendlinecurrentuass = value
                    self.sonetfarendlinecurrentuass.value_namespace = name_space
                    self.sonetfarendlinecurrentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendlinecurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendlinecurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndLineCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndLineCurrentEntry"):
                for c in self.sonetfarendlinecurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendlinecurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndLineCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendlineintervaltable(Entity):
        """
        The SONET/SDH Far End Line Interval table.
        
        .. attribute:: sonetfarendlineintervalentry
        
        	An entry in the SONET/SDH Far End Line Interval table
        	**type**\: list of    :py:class:`Sonetfarendlineintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendlineintervaltable, self).__init__()

            self.yang_name = "sonetFarEndLineIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendlineintervalentry = YList(self)

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
                        super(SonetMib.Sonetfarendlineintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendlineintervaltable, self).__setattr__(name, value)


        class Sonetfarendlineintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End Line Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendlineintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendlineintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry, self).__init__()

                self.yang_name = "sonetFarEndLineIntervalEntry"
                self.yang_parent_name = "sonetFarEndLineIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendlineintervalnumber = YLeaf(YType.int32, "sonetFarEndLineIntervalNumber")

                self.sonetfarendlineintervalcvs = YLeaf(YType.uint32, "sonetFarEndLineIntervalCVs")

                self.sonetfarendlineintervaless = YLeaf(YType.uint32, "sonetFarEndLineIntervalESs")

                self.sonetfarendlineintervalsess = YLeaf(YType.uint32, "sonetFarEndLineIntervalSESs")

                self.sonetfarendlineintervaluass = YLeaf(YType.uint32, "sonetFarEndLineIntervalUASs")

                self.sonetfarendlineintervalvaliddata = YLeaf(YType.boolean, "sonetFarEndLineIntervalValidData")

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
                                "sonetfarendlineintervalnumber",
                                "sonetfarendlineintervalcvs",
                                "sonetfarendlineintervaless",
                                "sonetfarendlineintervalsess",
                                "sonetfarendlineintervaluass",
                                "sonetfarendlineintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendlineintervalnumber.is_set or
                    self.sonetfarendlineintervalcvs.is_set or
                    self.sonetfarendlineintervaless.is_set or
                    self.sonetfarendlineintervalsess.is_set or
                    self.sonetfarendlineintervaluass.is_set or
                    self.sonetfarendlineintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervalnumber.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervalcvs.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervaless.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervalsess.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervaluass.yfilter != YFilter.not_set or
                    self.sonetfarendlineintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndLineIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetFarEndLineIntervalNumber='" + self.sonetfarendlineintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndLineIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendlineintervalnumber.is_set or self.sonetfarendlineintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervalnumber.get_name_leafdata())
                if (self.sonetfarendlineintervalcvs.is_set or self.sonetfarendlineintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervalcvs.get_name_leafdata())
                if (self.sonetfarendlineintervaless.is_set or self.sonetfarendlineintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervaless.get_name_leafdata())
                if (self.sonetfarendlineintervalsess.is_set or self.sonetfarendlineintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervalsess.get_name_leafdata())
                if (self.sonetfarendlineintervaluass.is_set or self.sonetfarendlineintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervaluass.get_name_leafdata())
                if (self.sonetfarendlineintervalvaliddata.is_set or self.sonetfarendlineintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendlineintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndLineIntervalNumber" or name == "sonetFarEndLineIntervalCVs" or name == "sonetFarEndLineIntervalESs" or name == "sonetFarEndLineIntervalSESs" or name == "sonetFarEndLineIntervalUASs" or name == "sonetFarEndLineIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalNumber"):
                    self.sonetfarendlineintervalnumber = value
                    self.sonetfarendlineintervalnumber.value_namespace = name_space
                    self.sonetfarendlineintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalCVs"):
                    self.sonetfarendlineintervalcvs = value
                    self.sonetfarendlineintervalcvs.value_namespace = name_space
                    self.sonetfarendlineintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalESs"):
                    self.sonetfarendlineintervaless = value
                    self.sonetfarendlineintervaless.value_namespace = name_space
                    self.sonetfarendlineintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalSESs"):
                    self.sonetfarendlineintervalsess = value
                    self.sonetfarendlineintervalsess.value_namespace = name_space
                    self.sonetfarendlineintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalUASs"):
                    self.sonetfarendlineintervaluass = value
                    self.sonetfarendlineintervaluass.value_namespace = name_space
                    self.sonetfarendlineintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndLineIntervalValidData"):
                    self.sonetfarendlineintervalvaliddata = value
                    self.sonetfarendlineintervalvaliddata.value_namespace = name_space
                    self.sonetfarendlineintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendlineintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendlineintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndLineIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndLineIntervalEntry"):
                for c in self.sonetfarendlineintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendlineintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndLineIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetpathcurrenttable(Entity):
        """
        The SONET/SDH Path Current table.
        
        .. attribute:: sonetpathcurrententry
        
        	An entry in the SONET/SDH Path Current table
        	**type**\: list of    :py:class:`Sonetpathcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetpathcurrenttable, self).__init__()

            self.yang_name = "sonetPathCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetpathcurrententry = YList(self)

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
                        super(SonetMib.Sonetpathcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetpathcurrenttable, self).__setattr__(name, value)


        class Sonetpathcurrententry(Entity):
            """
            An entry in the SONET/SDH Path Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cspsignallingtransportmode
            
            	This object represents the mode used to transport DS0  Signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling  is transferred to the VT header. In clearMode(3), only  the framing bit is transferred to the VT header.           The initial value is signallingTransferMode(2)  if csTributaryMappingType is byteSynchronous.  For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:   :py:class:`Cspsignallingtransportmode <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.Cspsignallingtransportmode>`
            
            .. attribute:: cspsonetpathpayload
            
            	Specifies the payload carried by the SONET/SDH Path. The payload specification corresponds to C2 (Signal Label) overhead byte in SONET/SDH Path Overhead\: unequipped(1)    \: Path is not provisioned to carry any payload. unspecified(2)   \: Path is carrying an unspecifed payload. ds3(3)           \: Path is carrying a DS3 path as payload. vt15vc11(4)      \: Path is carrying SONET\-VT1.5/SDH\-VC11 payload. vt2vc12(5)       \: Path is carrying SONET\-VT2/SDH\-VC12 as payload. atmCell(6)       \: Path is carrying ATM Cells as payload. hdlcFr(7)        \: Path is carrying Frame Relay (HDLC) payload. e3(8)            \: Path is carrying an E3 path as payload. vtStructured(9)  \: Path is carrying VTGs/TUG3s/TUG2s which may                    each carry a different payload.  A write operation on this object will result in update to C2 overhead byte in the Path Overhead
            	**type**\:   :py:class:`Cspsonetpathpayload <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.Cspsonetpathpayload>`
            
            .. attribute:: csptributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.  au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.  au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  The initial value is au3Grouping(2) for SDH and  notApplicable(1) for SONET
            	**type**\:   :py:class:`Csptributarygroupingtype <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.Csptributarygroupingtype>`
            
            .. attribute:: csptributarymappingtype
            
            	This object represents the VT/VC mapping type. asynchronous\: In this mode, the channel structure of                DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside                   the VT/VC can be found and extracted                   from the frame. The initial value is asynchronous(1)
            	**type**\:   :py:class:`Csptributarymappingtype <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.Csptributarymappingtype>`
            
            .. attribute:: sonetpathcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentstatus
            
            	This variable indicates the status of the interface. The sonetPathCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetPathNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetPathNoDefect    2   sonetPathSTSLOP    4   sonetPathSTSAIS    8   sonetPathSTSRDI   16   sonetPathUnequipped   32   sonetPathSignalLabelMismatch
            	**type**\:  int
            
            	**range:** 1..62
            
            .. attribute:: sonetpathcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentwidth
            
            	A value that indicates the type of the SONET/SDH Path.  For SONET, the assigned types are the STS\-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768. STS\-1 is equal to 51.84 Mbps.  For SDH, the assigned types are the STM\-Nc VCs, where N = 1, 4, 16, 64 and 256
            	**type**\:   :py:class:`Sonetpathcurrentwidth <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.Sonetpathcurrentwidth>`
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry, self).__init__()

                self.yang_name = "sonetPathCurrentEntry"
                self.yang_parent_name = "sonetPathCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cspsignallingtransportmode = YLeaf(YType.enumeration, "CISCO-SONET-MIB:cspSignallingTransportMode")

                self.cspsonetpathpayload = YLeaf(YType.enumeration, "CISCO-SONET-MIB:cspSonetPathPayload")

                self.csptributarygroupingtype = YLeaf(YType.enumeration, "CISCO-SONET-MIB:cspTributaryGroupingType")

                self.csptributarymappingtype = YLeaf(YType.enumeration, "CISCO-SONET-MIB:cspTributaryMappingType")

                self.sonetpathcurrentcvs = YLeaf(YType.uint32, "sonetPathCurrentCVs")

                self.sonetpathcurrentess = YLeaf(YType.uint32, "sonetPathCurrentESs")

                self.sonetpathcurrentsess = YLeaf(YType.uint32, "sonetPathCurrentSESs")

                self.sonetpathcurrentstatus = YLeaf(YType.int32, "sonetPathCurrentStatus")

                self.sonetpathcurrentuass = YLeaf(YType.uint32, "sonetPathCurrentUASs")

                self.sonetpathcurrentwidth = YLeaf(YType.enumeration, "sonetPathCurrentWidth")

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
                                "cspsignallingtransportmode",
                                "cspsonetpathpayload",
                                "csptributarygroupingtype",
                                "csptributarymappingtype",
                                "sonetpathcurrentcvs",
                                "sonetpathcurrentess",
                                "sonetpathcurrentsess",
                                "sonetpathcurrentstatus",
                                "sonetpathcurrentuass",
                                "sonetpathcurrentwidth") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry, self).__setattr__(name, value)

            class Cspsignallingtransportmode(Enum):
                """
                Cspsignallingtransportmode

                This object represents the mode used to transport DS0 

                Signalling information for T1 byteSynchronous mapping

                (GR253).

                In signallingTransferMode(2), the robbed\-bit signalling 

                is transferred to the VT header. In clearMode(3), only 

                the framing bit is transferred to the VT header.

                The initial value is signallingTransferMode(2) 

                if csTributaryMappingType is byteSynchronous. 

                For asynchronous mapping, it is 

                notApplicable(1).

                The value notApplicable(1) can not be set.

                .. data:: notApplicable = 1

                .. data:: signallingTransferMode = 2

                .. data:: clearMode = 3

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                signallingTransferMode = Enum.YLeaf(2, "signallingTransferMode")

                clearMode = Enum.YLeaf(3, "clearMode")


            class Cspsonetpathpayload(Enum):
                """
                Cspsonetpathpayload

                Specifies the payload carried by the SONET/SDH Path.

                The payload specification corresponds to C2 (Signal Label)

                overhead byte in SONET/SDH Path Overhead\:

                unequipped(1)    \: Path is not provisioned to carry any payload.

                unspecified(2)   \: Path is carrying an unspecifed payload.

                ds3(3)           \: Path is carrying a DS3 path as payload.

                vt15vc11(4)      \: Path is carrying SONET\-VT1.5/SDH\-VC11 payload.

                vt2vc12(5)       \: Path is carrying SONET\-VT2/SDH\-VC12 as payload.

                atmCell(6)       \: Path is carrying ATM Cells as payload.

                hdlcFr(7)        \: Path is carrying Frame Relay (HDLC) payload.

                e3(8)            \: Path is carrying an E3 path as payload.

                vtStructured(9)  \: Path is carrying VTGs/TUG3s/TUG2s which may

                                   each carry a different payload. 

                A write operation on this object will result in update to

                C2 overhead byte in the Path Overhead.

                .. data:: unequipped = 1

                .. data:: unspecified = 2

                .. data:: ds3 = 3

                .. data:: vt15vc11 = 4

                .. data:: vt2vc12 = 5

                .. data:: atmCell = 6

                .. data:: hdlcFr = 7

                .. data:: e3 = 8

                .. data:: vtStructured = 9

                """

                unequipped = Enum.YLeaf(1, "unequipped")

                unspecified = Enum.YLeaf(2, "unspecified")

                ds3 = Enum.YLeaf(3, "ds3")

                vt15vc11 = Enum.YLeaf(4, "vt15vc11")

                vt2vc12 = Enum.YLeaf(5, "vt2vc12")

                atmCell = Enum.YLeaf(6, "atmCell")

                hdlcFr = Enum.YLeaf(7, "hdlcFr")

                e3 = Enum.YLeaf(8, "e3")

                vtStructured = Enum.YLeaf(9, "vtStructured")


            class Csptributarygroupingtype(Enum):
                """
                Csptributarygroupingtype

                This object represents the method used to group VCs into

                an STM\-1 signal. Applicable only to SDH.

                au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or

                             STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.

                au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or

                             STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.

                The initial value is au3Grouping(2) for SDH and 

                notApplicable(1) for SONET.

                .. data:: notApplicable = 1

                .. data:: au3Grouping = 2

                .. data:: au4Grouping = 3

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                au3Grouping = Enum.YLeaf(2, "au3Grouping")

                au4Grouping = Enum.YLeaf(3, "au4Grouping")


            class Csptributarymappingtype(Enum):
                """
                Csptributarymappingtype

                This object represents the VT/VC mapping type.

                asynchronous\: In this mode, the channel structure of 

                              DS1/E1 is neither visible nor preserved.

                byteSynchronous\: In this mode, the DS0 signals inside 

                                 the VT/VC can be found and extracted 

                                 from the frame.

                The initial value is asynchronous(1).

                .. data:: asynchronous = 1

                .. data:: byteSynchronous = 2

                """

                asynchronous = Enum.YLeaf(1, "asynchronous")

                byteSynchronous = Enum.YLeaf(2, "byteSynchronous")


            class Sonetpathcurrentwidth(Enum):
                """
                Sonetpathcurrentwidth

                A value that indicates the type of the SONET/SDH

                Path.  For SONET, the assigned types are

                the STS\-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768.

                STS\-1 is equal to 51.84 Mbps.  For SDH, the assigned

                types are the STM\-Nc VCs, where N = 1, 4, 16, 64 and 256.

                .. data:: sts1 = 1

                .. data:: sts3cSTM1 = 2

                .. data:: sts12cSTM4 = 3

                .. data:: sts24c = 4

                .. data:: sts48cSTM16 = 5

                .. data:: sts192cSTM64 = 6

                .. data:: sts768cSTM256 = 7

                """

                sts1 = Enum.YLeaf(1, "sts1")

                sts3cSTM1 = Enum.YLeaf(2, "sts3cSTM1")

                sts12cSTM4 = Enum.YLeaf(3, "sts12cSTM4")

                sts24c = Enum.YLeaf(4, "sts24c")

                sts48cSTM16 = Enum.YLeaf(5, "sts48cSTM16")

                sts192cSTM64 = Enum.YLeaf(6, "sts192cSTM64")

                sts768cSTM256 = Enum.YLeaf(7, "sts768cSTM256")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cspsignallingtransportmode.is_set or
                    self.cspsonetpathpayload.is_set or
                    self.csptributarygroupingtype.is_set or
                    self.csptributarymappingtype.is_set or
                    self.sonetpathcurrentcvs.is_set or
                    self.sonetpathcurrentess.is_set or
                    self.sonetpathcurrentsess.is_set or
                    self.sonetpathcurrentstatus.is_set or
                    self.sonetpathcurrentuass.is_set or
                    self.sonetpathcurrentwidth.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cspsignallingtransportmode.yfilter != YFilter.not_set or
                    self.cspsonetpathpayload.yfilter != YFilter.not_set or
                    self.csptributarygroupingtype.yfilter != YFilter.not_set or
                    self.csptributarymappingtype.yfilter != YFilter.not_set or
                    self.sonetpathcurrentcvs.yfilter != YFilter.not_set or
                    self.sonetpathcurrentess.yfilter != YFilter.not_set or
                    self.sonetpathcurrentsess.yfilter != YFilter.not_set or
                    self.sonetpathcurrentstatus.yfilter != YFilter.not_set or
                    self.sonetpathcurrentuass.yfilter != YFilter.not_set or
                    self.sonetpathcurrentwidth.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetPathCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetPathCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cspsignallingtransportmode.is_set or self.cspsignallingtransportmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspsignallingtransportmode.get_name_leafdata())
                if (self.cspsonetpathpayload.is_set or self.cspsonetpathpayload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cspsonetpathpayload.get_name_leafdata())
                if (self.csptributarygroupingtype.is_set or self.csptributarygroupingtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptributarygroupingtype.get_name_leafdata())
                if (self.csptributarymappingtype.is_set or self.csptributarymappingtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csptributarymappingtype.get_name_leafdata())
                if (self.sonetpathcurrentcvs.is_set or self.sonetpathcurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentcvs.get_name_leafdata())
                if (self.sonetpathcurrentess.is_set or self.sonetpathcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentess.get_name_leafdata())
                if (self.sonetpathcurrentsess.is_set or self.sonetpathcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentsess.get_name_leafdata())
                if (self.sonetpathcurrentstatus.is_set or self.sonetpathcurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentstatus.get_name_leafdata())
                if (self.sonetpathcurrentuass.is_set or self.sonetpathcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentuass.get_name_leafdata())
                if (self.sonetpathcurrentwidth.is_set or self.sonetpathcurrentwidth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathcurrentwidth.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cspSignallingTransportMode" or name == "cspSonetPathPayload" or name == "cspTributaryGroupingType" or name == "cspTributaryMappingType" or name == "sonetPathCurrentCVs" or name == "sonetPathCurrentESs" or name == "sonetPathCurrentSESs" or name == "sonetPathCurrentStatus" or name == "sonetPathCurrentUASs" or name == "sonetPathCurrentWidth"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cspSignallingTransportMode"):
                    self.cspsignallingtransportmode = value
                    self.cspsignallingtransportmode.value_namespace = name_space
                    self.cspsignallingtransportmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cspSonetPathPayload"):
                    self.cspsonetpathpayload = value
                    self.cspsonetpathpayload.value_namespace = name_space
                    self.cspsonetpathpayload.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTributaryGroupingType"):
                    self.csptributarygroupingtype = value
                    self.csptributarygroupingtype.value_namespace = name_space
                    self.csptributarygroupingtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cspTributaryMappingType"):
                    self.csptributarymappingtype = value
                    self.csptributarymappingtype.value_namespace = name_space
                    self.csptributarymappingtype.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentCVs"):
                    self.sonetpathcurrentcvs = value
                    self.sonetpathcurrentcvs.value_namespace = name_space
                    self.sonetpathcurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentESs"):
                    self.sonetpathcurrentess = value
                    self.sonetpathcurrentess.value_namespace = name_space
                    self.sonetpathcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentSESs"):
                    self.sonetpathcurrentsess = value
                    self.sonetpathcurrentsess.value_namespace = name_space
                    self.sonetpathcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentStatus"):
                    self.sonetpathcurrentstatus = value
                    self.sonetpathcurrentstatus.value_namespace = name_space
                    self.sonetpathcurrentstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentUASs"):
                    self.sonetpathcurrentuass = value
                    self.sonetpathcurrentuass.value_namespace = name_space
                    self.sonetpathcurrentuass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathCurrentWidth"):
                    self.sonetpathcurrentwidth = value
                    self.sonetpathcurrentwidth.value_namespace = name_space
                    self.sonetpathcurrentwidth.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetpathcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetpathcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetPathCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetPathCurrentEntry"):
                for c in self.sonetpathcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetpathcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetPathCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetpathintervaltable(Entity):
        """
        The SONET/SDH Path Interval table.
        
        .. attribute:: sonetpathintervalentry
        
        	An entry in the SONET/SDH Path Interval table
        	**type**\: list of    :py:class:`Sonetpathintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetpathintervaltable.Sonetpathintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetpathintervaltable, self).__init__()

            self.yang_name = "sonetPathIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetpathintervalentry = YList(self)

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
                        super(SonetMib.Sonetpathintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetpathintervaltable, self).__setattr__(name, value)


        class Sonetpathintervalentry(Entity):
            """
            An entry in the SONET/SDH Path Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetpathintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetpathintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetpathintervaltable.Sonetpathintervalentry, self).__init__()

                self.yang_name = "sonetPathIntervalEntry"
                self.yang_parent_name = "sonetPathIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetpathintervalnumber = YLeaf(YType.int32, "sonetPathIntervalNumber")

                self.sonetpathintervalcvs = YLeaf(YType.uint32, "sonetPathIntervalCVs")

                self.sonetpathintervaless = YLeaf(YType.uint32, "sonetPathIntervalESs")

                self.sonetpathintervalsess = YLeaf(YType.uint32, "sonetPathIntervalSESs")

                self.sonetpathintervaluass = YLeaf(YType.uint32, "sonetPathIntervalUASs")

                self.sonetpathintervalvaliddata = YLeaf(YType.boolean, "sonetPathIntervalValidData")

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
                                "sonetpathintervalnumber",
                                "sonetpathintervalcvs",
                                "sonetpathintervaless",
                                "sonetpathintervalsess",
                                "sonetpathintervaluass",
                                "sonetpathintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetpathintervaltable.Sonetpathintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetpathintervaltable.Sonetpathintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetpathintervalnumber.is_set or
                    self.sonetpathintervalcvs.is_set or
                    self.sonetpathintervaless.is_set or
                    self.sonetpathintervalsess.is_set or
                    self.sonetpathintervaluass.is_set or
                    self.sonetpathintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetpathintervalnumber.yfilter != YFilter.not_set or
                    self.sonetpathintervalcvs.yfilter != YFilter.not_set or
                    self.sonetpathintervaless.yfilter != YFilter.not_set or
                    self.sonetpathintervalsess.yfilter != YFilter.not_set or
                    self.sonetpathintervaluass.yfilter != YFilter.not_set or
                    self.sonetpathintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetPathIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetPathIntervalNumber='" + self.sonetpathintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetPathIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetpathintervalnumber.is_set or self.sonetpathintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervalnumber.get_name_leafdata())
                if (self.sonetpathintervalcvs.is_set or self.sonetpathintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervalcvs.get_name_leafdata())
                if (self.sonetpathintervaless.is_set or self.sonetpathintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervaless.get_name_leafdata())
                if (self.sonetpathintervalsess.is_set or self.sonetpathintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervalsess.get_name_leafdata())
                if (self.sonetpathintervaluass.is_set or self.sonetpathintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervaluass.get_name_leafdata())
                if (self.sonetpathintervalvaliddata.is_set or self.sonetpathintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetpathintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetPathIntervalNumber" or name == "sonetPathIntervalCVs" or name == "sonetPathIntervalESs" or name == "sonetPathIntervalSESs" or name == "sonetPathIntervalUASs" or name == "sonetPathIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalNumber"):
                    self.sonetpathintervalnumber = value
                    self.sonetpathintervalnumber.value_namespace = name_space
                    self.sonetpathintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalCVs"):
                    self.sonetpathintervalcvs = value
                    self.sonetpathintervalcvs.value_namespace = name_space
                    self.sonetpathintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalESs"):
                    self.sonetpathintervaless = value
                    self.sonetpathintervaless.value_namespace = name_space
                    self.sonetpathintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalSESs"):
                    self.sonetpathintervalsess = value
                    self.sonetpathintervalsess.value_namespace = name_space
                    self.sonetpathintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalUASs"):
                    self.sonetpathintervaluass = value
                    self.sonetpathintervaluass.value_namespace = name_space
                    self.sonetpathintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetPathIntervalValidData"):
                    self.sonetpathintervalvaliddata = value
                    self.sonetpathintervalvaliddata.value_namespace = name_space
                    self.sonetpathintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetpathintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetpathintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetPathIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetPathIntervalEntry"):
                for c in self.sonetpathintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetpathintervaltable.Sonetpathintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetpathintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetPathIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendpathcurrenttable(Entity):
        """
        The SONET/SDH Far End Path Current table.
        
        .. attribute:: sonetfarendpathcurrententry
        
        	An entry in the SONET/SDH Far End Path Current table
        	**type**\: list of    :py:class:`Sonetfarendpathcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendpathcurrenttable, self).__init__()

            self.yang_name = "sonetFarEndPathCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendpathcurrententry = YList(self)

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
                        super(SonetMib.Sonetfarendpathcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendpathcurrenttable, self).__setattr__(name, value)


        class Sonetfarendpathcurrententry(Entity):
            """
            An entry in the SONET/SDH Far End Path Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendpathcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry, self).__init__()

                self.yang_name = "sonetFarEndPathCurrentEntry"
                self.yang_parent_name = "sonetFarEndPathCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendpathcurrentcvs = YLeaf(YType.uint32, "sonetFarEndPathCurrentCVs")

                self.sonetfarendpathcurrentess = YLeaf(YType.uint32, "sonetFarEndPathCurrentESs")

                self.sonetfarendpathcurrentsess = YLeaf(YType.uint32, "sonetFarEndPathCurrentSESs")

                self.sonetfarendpathcurrentuass = YLeaf(YType.uint32, "sonetFarEndPathCurrentUASs")

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
                                "sonetfarendpathcurrentcvs",
                                "sonetfarendpathcurrentess",
                                "sonetfarendpathcurrentsess",
                                "sonetfarendpathcurrentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendpathcurrentcvs.is_set or
                    self.sonetfarendpathcurrentess.is_set or
                    self.sonetfarendpathcurrentsess.is_set or
                    self.sonetfarendpathcurrentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendpathcurrentcvs.yfilter != YFilter.not_set or
                    self.sonetfarendpathcurrentess.yfilter != YFilter.not_set or
                    self.sonetfarendpathcurrentsess.yfilter != YFilter.not_set or
                    self.sonetfarendpathcurrentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndPathCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndPathCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendpathcurrentcvs.is_set or self.sonetfarendpathcurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathcurrentcvs.get_name_leafdata())
                if (self.sonetfarendpathcurrentess.is_set or self.sonetfarendpathcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathcurrentess.get_name_leafdata())
                if (self.sonetfarendpathcurrentsess.is_set or self.sonetfarendpathcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathcurrentsess.get_name_leafdata())
                if (self.sonetfarendpathcurrentuass.is_set or self.sonetfarendpathcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathcurrentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndPathCurrentCVs" or name == "sonetFarEndPathCurrentESs" or name == "sonetFarEndPathCurrentSESs" or name == "sonetFarEndPathCurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathCurrentCVs"):
                    self.sonetfarendpathcurrentcvs = value
                    self.sonetfarendpathcurrentcvs.value_namespace = name_space
                    self.sonetfarendpathcurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathCurrentESs"):
                    self.sonetfarendpathcurrentess = value
                    self.sonetfarendpathcurrentess.value_namespace = name_space
                    self.sonetfarendpathcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathCurrentSESs"):
                    self.sonetfarendpathcurrentsess = value
                    self.sonetfarendpathcurrentsess.value_namespace = name_space
                    self.sonetfarendpathcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathCurrentUASs"):
                    self.sonetfarendpathcurrentuass = value
                    self.sonetfarendpathcurrentuass.value_namespace = name_space
                    self.sonetfarendpathcurrentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendpathcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendpathcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndPathCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndPathCurrentEntry"):
                for c in self.sonetfarendpathcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendpathcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndPathCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendpathintervaltable(Entity):
        """
        The SONET/SDH Far End Path Interval table.
        
        .. attribute:: sonetfarendpathintervalentry
        
        	An entry in the SONET/SDH Far End Path Interval table
        	**type**\: list of    :py:class:`Sonetfarendpathintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendpathintervaltable, self).__init__()

            self.yang_name = "sonetFarEndPathIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendpathintervalentry = YList(self)

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
                        super(SonetMib.Sonetfarendpathintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendpathintervaltable, self).__setattr__(name, value)


        class Sonetfarendpathintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End Path Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendpathintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendpathintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry, self).__init__()

                self.yang_name = "sonetFarEndPathIntervalEntry"
                self.yang_parent_name = "sonetFarEndPathIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendpathintervalnumber = YLeaf(YType.int32, "sonetFarEndPathIntervalNumber")

                self.sonetfarendpathintervalcvs = YLeaf(YType.uint32, "sonetFarEndPathIntervalCVs")

                self.sonetfarendpathintervaless = YLeaf(YType.uint32, "sonetFarEndPathIntervalESs")

                self.sonetfarendpathintervalsess = YLeaf(YType.uint32, "sonetFarEndPathIntervalSESs")

                self.sonetfarendpathintervaluass = YLeaf(YType.uint32, "sonetFarEndPathIntervalUASs")

                self.sonetfarendpathintervalvaliddata = YLeaf(YType.boolean, "sonetFarEndPathIntervalValidData")

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
                                "sonetfarendpathintervalnumber",
                                "sonetfarendpathintervalcvs",
                                "sonetfarendpathintervaless",
                                "sonetfarendpathintervalsess",
                                "sonetfarendpathintervaluass",
                                "sonetfarendpathintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendpathintervalnumber.is_set or
                    self.sonetfarendpathintervalcvs.is_set or
                    self.sonetfarendpathintervaless.is_set or
                    self.sonetfarendpathintervalsess.is_set or
                    self.sonetfarendpathintervaluass.is_set or
                    self.sonetfarendpathintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervalnumber.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervalcvs.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervaless.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervalsess.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervaluass.yfilter != YFilter.not_set or
                    self.sonetfarendpathintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndPathIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetFarEndPathIntervalNumber='" + self.sonetfarendpathintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndPathIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendpathintervalnumber.is_set or self.sonetfarendpathintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervalnumber.get_name_leafdata())
                if (self.sonetfarendpathintervalcvs.is_set or self.sonetfarendpathintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervalcvs.get_name_leafdata())
                if (self.sonetfarendpathintervaless.is_set or self.sonetfarendpathintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervaless.get_name_leafdata())
                if (self.sonetfarendpathintervalsess.is_set or self.sonetfarendpathintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervalsess.get_name_leafdata())
                if (self.sonetfarendpathintervaluass.is_set or self.sonetfarendpathintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervaluass.get_name_leafdata())
                if (self.sonetfarendpathintervalvaliddata.is_set or self.sonetfarendpathintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendpathintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndPathIntervalNumber" or name == "sonetFarEndPathIntervalCVs" or name == "sonetFarEndPathIntervalESs" or name == "sonetFarEndPathIntervalSESs" or name == "sonetFarEndPathIntervalUASs" or name == "sonetFarEndPathIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalNumber"):
                    self.sonetfarendpathintervalnumber = value
                    self.sonetfarendpathintervalnumber.value_namespace = name_space
                    self.sonetfarendpathintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalCVs"):
                    self.sonetfarendpathintervalcvs = value
                    self.sonetfarendpathintervalcvs.value_namespace = name_space
                    self.sonetfarendpathintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalESs"):
                    self.sonetfarendpathintervaless = value
                    self.sonetfarendpathintervaless.value_namespace = name_space
                    self.sonetfarendpathintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalSESs"):
                    self.sonetfarendpathintervalsess = value
                    self.sonetfarendpathintervalsess.value_namespace = name_space
                    self.sonetfarendpathintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalUASs"):
                    self.sonetfarendpathintervaluass = value
                    self.sonetfarendpathintervaluass.value_namespace = name_space
                    self.sonetfarendpathintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndPathIntervalValidData"):
                    self.sonetfarendpathintervalvaliddata = value
                    self.sonetfarendpathintervalvaliddata.value_namespace = name_space
                    self.sonetfarendpathintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendpathintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendpathintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndPathIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndPathIntervalEntry"):
                for c in self.sonetfarendpathintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendpathintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndPathIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetvtcurrenttable(Entity):
        """
        The SONET/SDH VT Current table.
        
        .. attribute:: sonetvtcurrententry
        
        	An entry in the SONET/SDH VT Current table
        	**type**\: list of    :py:class:`Sonetvtcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetvtcurrenttable, self).__init__()

            self.yang_name = "sonetVTCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetvtcurrententry = YList(self)

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
                        super(SonetMib.Sonetvtcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetvtcurrenttable, self).__setattr__(name, value)


        class Sonetvtcurrententry(Entity):
            """
            An entry in the SONET/SDH VT Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetvtcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentstatus
            
            	This variable indicates the status of the interface. The sonetVTCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects and failures simultaneously. The sonetVTNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetVTNoDefect    2   sonetVTLOP    4   sonetVTPathAIS    8   sonetVTPathRDI   16   sonetVTPathRFI   32   sonetVTUnequipped   64   sonetVTSignalLabelMismatch
            	**type**\:  int
            
            	**range:** 1..126
            
            .. attribute:: sonetvtcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentwidth
            
            	A value that indicates the type of the SONET VT and SDH VC.  Assigned widths are VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c
            	**type**\:   :py:class:`Sonetvtcurrentwidth <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry.Sonetvtcurrentwidth>`
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry, self).__init__()

                self.yang_name = "sonetVTCurrentEntry"
                self.yang_parent_name = "sonetVTCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetvtcurrentcvs = YLeaf(YType.uint32, "sonetVTCurrentCVs")

                self.sonetvtcurrentess = YLeaf(YType.uint32, "sonetVTCurrentESs")

                self.sonetvtcurrentsess = YLeaf(YType.uint32, "sonetVTCurrentSESs")

                self.sonetvtcurrentstatus = YLeaf(YType.int32, "sonetVTCurrentStatus")

                self.sonetvtcurrentuass = YLeaf(YType.uint32, "sonetVTCurrentUASs")

                self.sonetvtcurrentwidth = YLeaf(YType.enumeration, "sonetVTCurrentWidth")

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
                                "sonetvtcurrentcvs",
                                "sonetvtcurrentess",
                                "sonetvtcurrentsess",
                                "sonetvtcurrentstatus",
                                "sonetvtcurrentuass",
                                "sonetvtcurrentwidth") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry, self).__setattr__(name, value)

            class Sonetvtcurrentwidth(Enum):
                """
                Sonetvtcurrentwidth

                A value that indicates the type of the SONET

                VT and SDH VC.  Assigned widths are

                VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c.

                .. data:: vtWidth15VC11 = 1

                .. data:: vtWidth2VC12 = 2

                .. data:: vtWidth3 = 3

                .. data:: vtWidth6VC2 = 4

                .. data:: vtWidth6c = 5

                """

                vtWidth15VC11 = Enum.YLeaf(1, "vtWidth15VC11")

                vtWidth2VC12 = Enum.YLeaf(2, "vtWidth2VC12")

                vtWidth3 = Enum.YLeaf(3, "vtWidth3")

                vtWidth6VC2 = Enum.YLeaf(4, "vtWidth6VC2")

                vtWidth6c = Enum.YLeaf(5, "vtWidth6c")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetvtcurrentcvs.is_set or
                    self.sonetvtcurrentess.is_set or
                    self.sonetvtcurrentsess.is_set or
                    self.sonetvtcurrentstatus.is_set or
                    self.sonetvtcurrentuass.is_set or
                    self.sonetvtcurrentwidth.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetvtcurrentcvs.yfilter != YFilter.not_set or
                    self.sonetvtcurrentess.yfilter != YFilter.not_set or
                    self.sonetvtcurrentsess.yfilter != YFilter.not_set or
                    self.sonetvtcurrentstatus.yfilter != YFilter.not_set or
                    self.sonetvtcurrentuass.yfilter != YFilter.not_set or
                    self.sonetvtcurrentwidth.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetVTCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetVTCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetvtcurrentcvs.is_set or self.sonetvtcurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentcvs.get_name_leafdata())
                if (self.sonetvtcurrentess.is_set or self.sonetvtcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentess.get_name_leafdata())
                if (self.sonetvtcurrentsess.is_set or self.sonetvtcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentsess.get_name_leafdata())
                if (self.sonetvtcurrentstatus.is_set or self.sonetvtcurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentstatus.get_name_leafdata())
                if (self.sonetvtcurrentuass.is_set or self.sonetvtcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentuass.get_name_leafdata())
                if (self.sonetvtcurrentwidth.is_set or self.sonetvtcurrentwidth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtcurrentwidth.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetVTCurrentCVs" or name == "sonetVTCurrentESs" or name == "sonetVTCurrentSESs" or name == "sonetVTCurrentStatus" or name == "sonetVTCurrentUASs" or name == "sonetVTCurrentWidth"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentCVs"):
                    self.sonetvtcurrentcvs = value
                    self.sonetvtcurrentcvs.value_namespace = name_space
                    self.sonetvtcurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentESs"):
                    self.sonetvtcurrentess = value
                    self.sonetvtcurrentess.value_namespace = name_space
                    self.sonetvtcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentSESs"):
                    self.sonetvtcurrentsess = value
                    self.sonetvtcurrentsess.value_namespace = name_space
                    self.sonetvtcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentStatus"):
                    self.sonetvtcurrentstatus = value
                    self.sonetvtcurrentstatus.value_namespace = name_space
                    self.sonetvtcurrentstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentUASs"):
                    self.sonetvtcurrentuass = value
                    self.sonetvtcurrentuass.value_namespace = name_space
                    self.sonetvtcurrentuass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTCurrentWidth"):
                    self.sonetvtcurrentwidth = value
                    self.sonetvtcurrentwidth.value_namespace = name_space
                    self.sonetvtcurrentwidth.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetvtcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetvtcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetVTCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetVTCurrentEntry"):
                for c in self.sonetvtcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetvtcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetVTCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetvtintervaltable(Entity):
        """
        The SONET/SDH VT Interval table.
        
        .. attribute:: sonetvtintervalentry
        
        	An entry in the SONET/SDH VT Interval table
        	**type**\: list of    :py:class:`Sonetvtintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetvtintervaltable.Sonetvtintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetvtintervaltable, self).__init__()

            self.yang_name = "sonetVTIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetvtintervalentry = YList(self)

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
                        super(SonetMib.Sonetvtintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetvtintervaltable, self).__setattr__(name, value)


        class Sonetvtintervalentry(Entity):
            """
            An entry in the SONET/SDH VT Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetvtintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetvtintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetvtintervaltable.Sonetvtintervalentry, self).__init__()

                self.yang_name = "sonetVTIntervalEntry"
                self.yang_parent_name = "sonetVTIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetvtintervalnumber = YLeaf(YType.int32, "sonetVTIntervalNumber")

                self.sonetvtintervalcvs = YLeaf(YType.uint32, "sonetVTIntervalCVs")

                self.sonetvtintervaless = YLeaf(YType.uint32, "sonetVTIntervalESs")

                self.sonetvtintervalsess = YLeaf(YType.uint32, "sonetVTIntervalSESs")

                self.sonetvtintervaluass = YLeaf(YType.uint32, "sonetVTIntervalUASs")

                self.sonetvtintervalvaliddata = YLeaf(YType.boolean, "sonetVTIntervalValidData")

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
                                "sonetvtintervalnumber",
                                "sonetvtintervalcvs",
                                "sonetvtintervaless",
                                "sonetvtintervalsess",
                                "sonetvtintervaluass",
                                "sonetvtintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetvtintervaltable.Sonetvtintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetvtintervaltable.Sonetvtintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetvtintervalnumber.is_set or
                    self.sonetvtintervalcvs.is_set or
                    self.sonetvtintervaless.is_set or
                    self.sonetvtintervalsess.is_set or
                    self.sonetvtintervaluass.is_set or
                    self.sonetvtintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetvtintervalnumber.yfilter != YFilter.not_set or
                    self.sonetvtintervalcvs.yfilter != YFilter.not_set or
                    self.sonetvtintervaless.yfilter != YFilter.not_set or
                    self.sonetvtintervalsess.yfilter != YFilter.not_set or
                    self.sonetvtintervaluass.yfilter != YFilter.not_set or
                    self.sonetvtintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetVTIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetVTIntervalNumber='" + self.sonetvtintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetVTIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetvtintervalnumber.is_set or self.sonetvtintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervalnumber.get_name_leafdata())
                if (self.sonetvtintervalcvs.is_set or self.sonetvtintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervalcvs.get_name_leafdata())
                if (self.sonetvtintervaless.is_set or self.sonetvtintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervaless.get_name_leafdata())
                if (self.sonetvtintervalsess.is_set or self.sonetvtintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervalsess.get_name_leafdata())
                if (self.sonetvtintervaluass.is_set or self.sonetvtintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervaluass.get_name_leafdata())
                if (self.sonetvtintervalvaliddata.is_set or self.sonetvtintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetvtintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetVTIntervalNumber" or name == "sonetVTIntervalCVs" or name == "sonetVTIntervalESs" or name == "sonetVTIntervalSESs" or name == "sonetVTIntervalUASs" or name == "sonetVTIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalNumber"):
                    self.sonetvtintervalnumber = value
                    self.sonetvtintervalnumber.value_namespace = name_space
                    self.sonetvtintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalCVs"):
                    self.sonetvtintervalcvs = value
                    self.sonetvtintervalcvs.value_namespace = name_space
                    self.sonetvtintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalESs"):
                    self.sonetvtintervaless = value
                    self.sonetvtintervaless.value_namespace = name_space
                    self.sonetvtintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalSESs"):
                    self.sonetvtintervalsess = value
                    self.sonetvtintervalsess.value_namespace = name_space
                    self.sonetvtintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalUASs"):
                    self.sonetvtintervaluass = value
                    self.sonetvtintervaluass.value_namespace = name_space
                    self.sonetvtintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetVTIntervalValidData"):
                    self.sonetvtintervalvaliddata = value
                    self.sonetvtintervalvaliddata.value_namespace = name_space
                    self.sonetvtintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetvtintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetvtintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetVTIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetVTIntervalEntry"):
                for c in self.sonetvtintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetvtintervaltable.Sonetvtintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetvtintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetVTIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendvtcurrenttable(Entity):
        """
        The SONET/SDH Far End VT Current table.
        
        .. attribute:: sonetfarendvtcurrententry
        
        	An entry in the SONET/SDH Far End VT Current table
        	**type**\: list of    :py:class:`Sonetfarendvtcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendvtcurrenttable, self).__init__()

            self.yang_name = "sonetFarEndVTCurrentTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendvtcurrententry = YList(self)

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
                        super(SonetMib.Sonetfarendvtcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendvtcurrenttable, self).__setattr__(name, value)


        class Sonetfarendvtcurrententry(Entity):
            """
            An entry in the SONET/SDH Far End VT Current table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendvtcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry, self).__init__()

                self.yang_name = "sonetFarEndVTCurrentEntry"
                self.yang_parent_name = "sonetFarEndVTCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendvtcurrentcvs = YLeaf(YType.uint32, "sonetFarEndVTCurrentCVs")

                self.sonetfarendvtcurrentess = YLeaf(YType.uint32, "sonetFarEndVTCurrentESs")

                self.sonetfarendvtcurrentsess = YLeaf(YType.uint32, "sonetFarEndVTCurrentSESs")

                self.sonetfarendvtcurrentuass = YLeaf(YType.uint32, "sonetFarEndVTCurrentUASs")

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
                                "sonetfarendvtcurrentcvs",
                                "sonetfarendvtcurrentess",
                                "sonetfarendvtcurrentsess",
                                "sonetfarendvtcurrentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendvtcurrentcvs.is_set or
                    self.sonetfarendvtcurrentess.is_set or
                    self.sonetfarendvtcurrentsess.is_set or
                    self.sonetfarendvtcurrentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendvtcurrentcvs.yfilter != YFilter.not_set or
                    self.sonetfarendvtcurrentess.yfilter != YFilter.not_set or
                    self.sonetfarendvtcurrentsess.yfilter != YFilter.not_set or
                    self.sonetfarendvtcurrentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndVTCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndVTCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendvtcurrentcvs.is_set or self.sonetfarendvtcurrentcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtcurrentcvs.get_name_leafdata())
                if (self.sonetfarendvtcurrentess.is_set or self.sonetfarendvtcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtcurrentess.get_name_leafdata())
                if (self.sonetfarendvtcurrentsess.is_set or self.sonetfarendvtcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtcurrentsess.get_name_leafdata())
                if (self.sonetfarendvtcurrentuass.is_set or self.sonetfarendvtcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtcurrentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndVTCurrentCVs" or name == "sonetFarEndVTCurrentESs" or name == "sonetFarEndVTCurrentSESs" or name == "sonetFarEndVTCurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTCurrentCVs"):
                    self.sonetfarendvtcurrentcvs = value
                    self.sonetfarendvtcurrentcvs.value_namespace = name_space
                    self.sonetfarendvtcurrentcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTCurrentESs"):
                    self.sonetfarendvtcurrentess = value
                    self.sonetfarendvtcurrentess.value_namespace = name_space
                    self.sonetfarendvtcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTCurrentSESs"):
                    self.sonetfarendvtcurrentsess = value
                    self.sonetfarendvtcurrentsess.value_namespace = name_space
                    self.sonetfarendvtcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTCurrentUASs"):
                    self.sonetfarendvtcurrentuass = value
                    self.sonetfarendvtcurrentuass.value_namespace = name_space
                    self.sonetfarendvtcurrentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendvtcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendvtcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndVTCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndVTCurrentEntry"):
                for c in self.sonetfarendvtcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendvtcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndVTCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sonetfarendvtintervaltable(Entity):
        """
        The SONET/SDH Far End VT Interval table.
        
        .. attribute:: sonetfarendvtintervalentry
        
        	An entry in the SONET/SDH Far End VT Interval table
        	**type**\: list of    :py:class:`Sonetfarendvtintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SonetMib.Sonetfarendvtintervaltable, self).__init__()

            self.yang_name = "sonetFarEndVTIntervalTable"
            self.yang_parent_name = "SONET-MIB"

            self.sonetfarendvtintervalentry = YList(self)

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
                        super(SonetMib.Sonetfarendvtintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetMib.Sonetfarendvtintervaltable, self).__setattr__(name, value)


        class Sonetfarendvtintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End VT Interval table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendvtintervalnumber  <key>
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendvtintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry, self).__init__()

                self.yang_name = "sonetFarEndVTIntervalEntry"
                self.yang_parent_name = "sonetFarEndVTIntervalTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.sonetfarendvtintervalnumber = YLeaf(YType.int32, "sonetFarEndVTIntervalNumber")

                self.sonetfarendvtintervalcvs = YLeaf(YType.uint32, "sonetFarEndVTIntervalCVs")

                self.sonetfarendvtintervaless = YLeaf(YType.uint32, "sonetFarEndVTIntervalESs")

                self.sonetfarendvtintervalsess = YLeaf(YType.uint32, "sonetFarEndVTIntervalSESs")

                self.sonetfarendvtintervaluass = YLeaf(YType.uint32, "sonetFarEndVTIntervalUASs")

                self.sonetfarendvtintervalvaliddata = YLeaf(YType.boolean, "sonetFarEndVTIntervalValidData")

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
                                "sonetfarendvtintervalnumber",
                                "sonetfarendvtintervalcvs",
                                "sonetfarendvtintervaless",
                                "sonetfarendvtintervalsess",
                                "sonetfarendvtintervaluass",
                                "sonetfarendvtintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.sonetfarendvtintervalnumber.is_set or
                    self.sonetfarendvtintervalcvs.is_set or
                    self.sonetfarendvtintervaless.is_set or
                    self.sonetfarendvtintervalsess.is_set or
                    self.sonetfarendvtintervaluass.is_set or
                    self.sonetfarendvtintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervalnumber.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervalcvs.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervaless.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervalsess.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervaluass.yfilter != YFilter.not_set or
                    self.sonetfarendvtintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sonetFarEndVTIntervalEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[sonetFarEndVTIntervalNumber='" + self.sonetfarendvtintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SONET-MIB:SONET-MIB/sonetFarEndVTIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.sonetfarendvtintervalnumber.is_set or self.sonetfarendvtintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervalnumber.get_name_leafdata())
                if (self.sonetfarendvtintervalcvs.is_set or self.sonetfarendvtintervalcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervalcvs.get_name_leafdata())
                if (self.sonetfarendvtintervaless.is_set or self.sonetfarendvtintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervaless.get_name_leafdata())
                if (self.sonetfarendvtintervalsess.is_set or self.sonetfarendvtintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervalsess.get_name_leafdata())
                if (self.sonetfarendvtintervaluass.is_set or self.sonetfarendvtintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervaluass.get_name_leafdata())
                if (self.sonetfarendvtintervalvaliddata.is_set or self.sonetfarendvtintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sonetfarendvtintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "sonetFarEndVTIntervalNumber" or name == "sonetFarEndVTIntervalCVs" or name == "sonetFarEndVTIntervalESs" or name == "sonetFarEndVTIntervalSESs" or name == "sonetFarEndVTIntervalUASs" or name == "sonetFarEndVTIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalNumber"):
                    self.sonetfarendvtintervalnumber = value
                    self.sonetfarendvtintervalnumber.value_namespace = name_space
                    self.sonetfarendvtintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalCVs"):
                    self.sonetfarendvtintervalcvs = value
                    self.sonetfarendvtintervalcvs.value_namespace = name_space
                    self.sonetfarendvtintervalcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalESs"):
                    self.sonetfarendvtintervaless = value
                    self.sonetfarendvtintervaless.value_namespace = name_space
                    self.sonetfarendvtintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalSESs"):
                    self.sonetfarendvtintervalsess = value
                    self.sonetfarendvtintervalsess.value_namespace = name_space
                    self.sonetfarendvtintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalUASs"):
                    self.sonetfarendvtintervaluass = value
                    self.sonetfarendvtintervaluass.value_namespace = name_space
                    self.sonetfarendvtintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "sonetFarEndVTIntervalValidData"):
                    self.sonetfarendvtintervalvaliddata = value
                    self.sonetfarendvtintervalvaliddata.value_namespace = name_space
                    self.sonetfarendvtintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sonetfarendvtintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sonetfarendvtintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sonetFarEndVTIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SONET-MIB:SONET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sonetFarEndVTIntervalEntry"):
                for c in self.sonetfarendvtintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sonetfarendvtintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sonetFarEndVTIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.sonetfarendlinecurrenttable is not None and self.sonetfarendlinecurrenttable.has_data()) or
            (self.sonetfarendlineintervaltable is not None and self.sonetfarendlineintervaltable.has_data()) or
            (self.sonetfarendpathcurrenttable is not None and self.sonetfarendpathcurrenttable.has_data()) or
            (self.sonetfarendpathintervaltable is not None and self.sonetfarendpathintervaltable.has_data()) or
            (self.sonetfarendvtcurrenttable is not None and self.sonetfarendvtcurrenttable.has_data()) or
            (self.sonetfarendvtintervaltable is not None and self.sonetfarendvtintervaltable.has_data()) or
            (self.sonetlinecurrenttable is not None and self.sonetlinecurrenttable.has_data()) or
            (self.sonetlineintervaltable is not None and self.sonetlineintervaltable.has_data()) or
            (self.sonetmedium is not None and self.sonetmedium.has_data()) or
            (self.sonetmediumtable is not None and self.sonetmediumtable.has_data()) or
            (self.sonetpathcurrenttable is not None and self.sonetpathcurrenttable.has_data()) or
            (self.sonetpathintervaltable is not None and self.sonetpathintervaltable.has_data()) or
            (self.sonetsectioncurrenttable is not None and self.sonetsectioncurrenttable.has_data()) or
            (self.sonetsectionintervaltable is not None and self.sonetsectionintervaltable.has_data()) or
            (self.sonetvtcurrenttable is not None and self.sonetvtcurrenttable.has_data()) or
            (self.sonetvtintervaltable is not None and self.sonetvtintervaltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.sonetfarendlinecurrenttable is not None and self.sonetfarendlinecurrenttable.has_operation()) or
            (self.sonetfarendlineintervaltable is not None and self.sonetfarendlineintervaltable.has_operation()) or
            (self.sonetfarendpathcurrenttable is not None and self.sonetfarendpathcurrenttable.has_operation()) or
            (self.sonetfarendpathintervaltable is not None and self.sonetfarendpathintervaltable.has_operation()) or
            (self.sonetfarendvtcurrenttable is not None and self.sonetfarendvtcurrenttable.has_operation()) or
            (self.sonetfarendvtintervaltable is not None and self.sonetfarendvtintervaltable.has_operation()) or
            (self.sonetlinecurrenttable is not None and self.sonetlinecurrenttable.has_operation()) or
            (self.sonetlineintervaltable is not None and self.sonetlineintervaltable.has_operation()) or
            (self.sonetmedium is not None and self.sonetmedium.has_operation()) or
            (self.sonetmediumtable is not None and self.sonetmediumtable.has_operation()) or
            (self.sonetpathcurrenttable is not None and self.sonetpathcurrenttable.has_operation()) or
            (self.sonetpathintervaltable is not None and self.sonetpathintervaltable.has_operation()) or
            (self.sonetsectioncurrenttable is not None and self.sonetsectioncurrenttable.has_operation()) or
            (self.sonetsectionintervaltable is not None and self.sonetsectionintervaltable.has_operation()) or
            (self.sonetvtcurrenttable is not None and self.sonetvtcurrenttable.has_operation()) or
            (self.sonetvtintervaltable is not None and self.sonetvtintervaltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "SONET-MIB:SONET-MIB" + path_buffer

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

        if (child_yang_name == "sonetFarEndLineCurrentTable"):
            if (self.sonetfarendlinecurrenttable is None):
                self.sonetfarendlinecurrenttable = SonetMib.Sonetfarendlinecurrenttable()
                self.sonetfarendlinecurrenttable.parent = self
                self._children_name_map["sonetfarendlinecurrenttable"] = "sonetFarEndLineCurrentTable"
            return self.sonetfarendlinecurrenttable

        if (child_yang_name == "sonetFarEndLineIntervalTable"):
            if (self.sonetfarendlineintervaltable is None):
                self.sonetfarendlineintervaltable = SonetMib.Sonetfarendlineintervaltable()
                self.sonetfarendlineintervaltable.parent = self
                self._children_name_map["sonetfarendlineintervaltable"] = "sonetFarEndLineIntervalTable"
            return self.sonetfarendlineintervaltable

        if (child_yang_name == "sonetFarEndPathCurrentTable"):
            if (self.sonetfarendpathcurrenttable is None):
                self.sonetfarendpathcurrenttable = SonetMib.Sonetfarendpathcurrenttable()
                self.sonetfarendpathcurrenttable.parent = self
                self._children_name_map["sonetfarendpathcurrenttable"] = "sonetFarEndPathCurrentTable"
            return self.sonetfarendpathcurrenttable

        if (child_yang_name == "sonetFarEndPathIntervalTable"):
            if (self.sonetfarendpathintervaltable is None):
                self.sonetfarendpathintervaltable = SonetMib.Sonetfarendpathintervaltable()
                self.sonetfarendpathintervaltable.parent = self
                self._children_name_map["sonetfarendpathintervaltable"] = "sonetFarEndPathIntervalTable"
            return self.sonetfarendpathintervaltable

        if (child_yang_name == "sonetFarEndVTCurrentTable"):
            if (self.sonetfarendvtcurrenttable is None):
                self.sonetfarendvtcurrenttable = SonetMib.Sonetfarendvtcurrenttable()
                self.sonetfarendvtcurrenttable.parent = self
                self._children_name_map["sonetfarendvtcurrenttable"] = "sonetFarEndVTCurrentTable"
            return self.sonetfarendvtcurrenttable

        if (child_yang_name == "sonetFarEndVTIntervalTable"):
            if (self.sonetfarendvtintervaltable is None):
                self.sonetfarendvtintervaltable = SonetMib.Sonetfarendvtintervaltable()
                self.sonetfarendvtintervaltable.parent = self
                self._children_name_map["sonetfarendvtintervaltable"] = "sonetFarEndVTIntervalTable"
            return self.sonetfarendvtintervaltable

        if (child_yang_name == "sonetLineCurrentTable"):
            if (self.sonetlinecurrenttable is None):
                self.sonetlinecurrenttable = SonetMib.Sonetlinecurrenttable()
                self.sonetlinecurrenttable.parent = self
                self._children_name_map["sonetlinecurrenttable"] = "sonetLineCurrentTable"
            return self.sonetlinecurrenttable

        if (child_yang_name == "sonetLineIntervalTable"):
            if (self.sonetlineintervaltable is None):
                self.sonetlineintervaltable = SonetMib.Sonetlineintervaltable()
                self.sonetlineintervaltable.parent = self
                self._children_name_map["sonetlineintervaltable"] = "sonetLineIntervalTable"
            return self.sonetlineintervaltable

        if (child_yang_name == "sonetMedium"):
            if (self.sonetmedium is None):
                self.sonetmedium = SonetMib.Sonetmedium()
                self.sonetmedium.parent = self
                self._children_name_map["sonetmedium"] = "sonetMedium"
            return self.sonetmedium

        if (child_yang_name == "sonetMediumTable"):
            if (self.sonetmediumtable is None):
                self.sonetmediumtable = SonetMib.Sonetmediumtable()
                self.sonetmediumtable.parent = self
                self._children_name_map["sonetmediumtable"] = "sonetMediumTable"
            return self.sonetmediumtable

        if (child_yang_name == "sonetPathCurrentTable"):
            if (self.sonetpathcurrenttable is None):
                self.sonetpathcurrenttable = SonetMib.Sonetpathcurrenttable()
                self.sonetpathcurrenttable.parent = self
                self._children_name_map["sonetpathcurrenttable"] = "sonetPathCurrentTable"
            return self.sonetpathcurrenttable

        if (child_yang_name == "sonetPathIntervalTable"):
            if (self.sonetpathintervaltable is None):
                self.sonetpathintervaltable = SonetMib.Sonetpathintervaltable()
                self.sonetpathintervaltable.parent = self
                self._children_name_map["sonetpathintervaltable"] = "sonetPathIntervalTable"
            return self.sonetpathintervaltable

        if (child_yang_name == "sonetSectionCurrentTable"):
            if (self.sonetsectioncurrenttable is None):
                self.sonetsectioncurrenttable = SonetMib.Sonetsectioncurrenttable()
                self.sonetsectioncurrenttable.parent = self
                self._children_name_map["sonetsectioncurrenttable"] = "sonetSectionCurrentTable"
            return self.sonetsectioncurrenttable

        if (child_yang_name == "sonetSectionIntervalTable"):
            if (self.sonetsectionintervaltable is None):
                self.sonetsectionintervaltable = SonetMib.Sonetsectionintervaltable()
                self.sonetsectionintervaltable.parent = self
                self._children_name_map["sonetsectionintervaltable"] = "sonetSectionIntervalTable"
            return self.sonetsectionintervaltable

        if (child_yang_name == "sonetVTCurrentTable"):
            if (self.sonetvtcurrenttable is None):
                self.sonetvtcurrenttable = SonetMib.Sonetvtcurrenttable()
                self.sonetvtcurrenttable.parent = self
                self._children_name_map["sonetvtcurrenttable"] = "sonetVTCurrentTable"
            return self.sonetvtcurrenttable

        if (child_yang_name == "sonetVTIntervalTable"):
            if (self.sonetvtintervaltable is None):
                self.sonetvtintervaltable = SonetMib.Sonetvtintervaltable()
                self.sonetvtintervaltable.parent = self
                self._children_name_map["sonetvtintervaltable"] = "sonetVTIntervalTable"
            return self.sonetvtintervaltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "sonetFarEndLineCurrentTable" or name == "sonetFarEndLineIntervalTable" or name == "sonetFarEndPathCurrentTable" or name == "sonetFarEndPathIntervalTable" or name == "sonetFarEndVTCurrentTable" or name == "sonetFarEndVTIntervalTable" or name == "sonetLineCurrentTable" or name == "sonetLineIntervalTable" or name == "sonetMedium" or name == "sonetMediumTable" or name == "sonetPathCurrentTable" or name == "sonetPathIntervalTable" or name == "sonetSectionCurrentTable" or name == "sonetSectionIntervalTable" or name == "sonetVTCurrentTable" or name == "sonetVTIntervalTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SonetMib()
        return self._top_entity

