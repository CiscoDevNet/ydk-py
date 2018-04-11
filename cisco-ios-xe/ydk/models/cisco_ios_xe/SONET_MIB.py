""" SONET_MIB 

The MIB module to describe SONET/SDH interface objects.

Copyright (C) The Internet Society (2003).  This version
of this MIB module is part of RFC 3592;  see the RFC
itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SONETMIB(Entity):
    """
    
    
    .. attribute:: sonetmedium
    
    	
    	**type**\:  :py:class:`Sonetmedium <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmedium>`
    
    .. attribute:: sonetmediumtable
    
    	The SONET/SDH Medium table
    	**type**\:  :py:class:`Sonetmediumtable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable>`
    
    .. attribute:: sonetsectioncurrenttable
    
    	The SONET/SDH Section Current table
    	**type**\:  :py:class:`Sonetsectioncurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetsectioncurrenttable>`
    
    .. attribute:: sonetsectionintervaltable
    
    	The SONET/SDH Section Interval table
    	**type**\:  :py:class:`Sonetsectionintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetsectionintervaltable>`
    
    .. attribute:: sonetlinecurrenttable
    
    	The SONET/SDH Line Current table
    	**type**\:  :py:class:`Sonetlinecurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetlinecurrenttable>`
    
    .. attribute:: sonetlineintervaltable
    
    	The SONET/SDH Line Interval table
    	**type**\:  :py:class:`Sonetlineintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetlineintervaltable>`
    
    .. attribute:: sonetfarendlinecurrenttable
    
    	The SONET/SDH Far End Line Current table
    	**type**\:  :py:class:`Sonetfarendlinecurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendlinecurrenttable>`
    
    .. attribute:: sonetfarendlineintervaltable
    
    	The SONET/SDH Far End Line Interval table
    	**type**\:  :py:class:`Sonetfarendlineintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendlineintervaltable>`
    
    .. attribute:: sonetpathcurrenttable
    
    	The SONET/SDH Path Current table
    	**type**\:  :py:class:`Sonetpathcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable>`
    
    .. attribute:: sonetpathintervaltable
    
    	The SONET/SDH Path Interval table
    	**type**\:  :py:class:`Sonetpathintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathintervaltable>`
    
    .. attribute:: sonetfarendpathcurrenttable
    
    	The SONET/SDH Far End Path Current table
    	**type**\:  :py:class:`Sonetfarendpathcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendpathcurrenttable>`
    
    .. attribute:: sonetfarendpathintervaltable
    
    	The SONET/SDH Far End Path Interval table
    	**type**\:  :py:class:`Sonetfarendpathintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendpathintervaltable>`
    
    .. attribute:: sonetvtcurrenttable
    
    	The SONET/SDH VT Current table
    	**type**\:  :py:class:`Sonetvtcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetvtcurrenttable>`
    
    .. attribute:: sonetvtintervaltable
    
    	The SONET/SDH VT Interval table
    	**type**\:  :py:class:`Sonetvtintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetvtintervaltable>`
    
    .. attribute:: sonetfarendvtcurrenttable
    
    	The SONET/SDH Far End VT Current table
    	**type**\:  :py:class:`Sonetfarendvtcurrenttable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendvtcurrenttable>`
    
    .. attribute:: sonetfarendvtintervaltable
    
    	The SONET/SDH Far End VT Interval table
    	**type**\:  :py:class:`Sonetfarendvtintervaltable <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendvtintervaltable>`
    
    

    """

    _prefix = 'SONET-MIB'
    _revision = '2003-08-11'

    def __init__(self):
        super(SONETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SONET-MIB"
        self.yang_parent_name = "SONET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("sonetMedium", ("sonetmedium", SONETMIB.Sonetmedium)), ("sonetMediumTable", ("sonetmediumtable", SONETMIB.Sonetmediumtable)), ("sonetSectionCurrentTable", ("sonetsectioncurrenttable", SONETMIB.Sonetsectioncurrenttable)), ("sonetSectionIntervalTable", ("sonetsectionintervaltable", SONETMIB.Sonetsectionintervaltable)), ("sonetLineCurrentTable", ("sonetlinecurrenttable", SONETMIB.Sonetlinecurrenttable)), ("sonetLineIntervalTable", ("sonetlineintervaltable", SONETMIB.Sonetlineintervaltable)), ("sonetFarEndLineCurrentTable", ("sonetfarendlinecurrenttable", SONETMIB.Sonetfarendlinecurrenttable)), ("sonetFarEndLineIntervalTable", ("sonetfarendlineintervaltable", SONETMIB.Sonetfarendlineintervaltable)), ("sonetPathCurrentTable", ("sonetpathcurrenttable", SONETMIB.Sonetpathcurrenttable)), ("sonetPathIntervalTable", ("sonetpathintervaltable", SONETMIB.Sonetpathintervaltable)), ("sonetFarEndPathCurrentTable", ("sonetfarendpathcurrenttable", SONETMIB.Sonetfarendpathcurrenttable)), ("sonetFarEndPathIntervalTable", ("sonetfarendpathintervaltable", SONETMIB.Sonetfarendpathintervaltable)), ("sonetVTCurrentTable", ("sonetvtcurrenttable", SONETMIB.Sonetvtcurrenttable)), ("sonetVTIntervalTable", ("sonetvtintervaltable", SONETMIB.Sonetvtintervaltable)), ("sonetFarEndVTCurrentTable", ("sonetfarendvtcurrenttable", SONETMIB.Sonetfarendvtcurrenttable)), ("sonetFarEndVTIntervalTable", ("sonetfarendvtintervaltable", SONETMIB.Sonetfarendvtintervaltable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.sonetmedium = SONETMIB.Sonetmedium()
        self.sonetmedium.parent = self
        self._children_name_map["sonetmedium"] = "sonetMedium"
        self._children_yang_names.add("sonetMedium")

        self.sonetmediumtable = SONETMIB.Sonetmediumtable()
        self.sonetmediumtable.parent = self
        self._children_name_map["sonetmediumtable"] = "sonetMediumTable"
        self._children_yang_names.add("sonetMediumTable")

        self.sonetsectioncurrenttable = SONETMIB.Sonetsectioncurrenttable()
        self.sonetsectioncurrenttable.parent = self
        self._children_name_map["sonetsectioncurrenttable"] = "sonetSectionCurrentTable"
        self._children_yang_names.add("sonetSectionCurrentTable")

        self.sonetsectionintervaltable = SONETMIB.Sonetsectionintervaltable()
        self.sonetsectionintervaltable.parent = self
        self._children_name_map["sonetsectionintervaltable"] = "sonetSectionIntervalTable"
        self._children_yang_names.add("sonetSectionIntervalTable")

        self.sonetlinecurrenttable = SONETMIB.Sonetlinecurrenttable()
        self.sonetlinecurrenttable.parent = self
        self._children_name_map["sonetlinecurrenttable"] = "sonetLineCurrentTable"
        self._children_yang_names.add("sonetLineCurrentTable")

        self.sonetlineintervaltable = SONETMIB.Sonetlineintervaltable()
        self.sonetlineintervaltable.parent = self
        self._children_name_map["sonetlineintervaltable"] = "sonetLineIntervalTable"
        self._children_yang_names.add("sonetLineIntervalTable")

        self.sonetfarendlinecurrenttable = SONETMIB.Sonetfarendlinecurrenttable()
        self.sonetfarendlinecurrenttable.parent = self
        self._children_name_map["sonetfarendlinecurrenttable"] = "sonetFarEndLineCurrentTable"
        self._children_yang_names.add("sonetFarEndLineCurrentTable")

        self.sonetfarendlineintervaltable = SONETMIB.Sonetfarendlineintervaltable()
        self.sonetfarendlineintervaltable.parent = self
        self._children_name_map["sonetfarendlineintervaltable"] = "sonetFarEndLineIntervalTable"
        self._children_yang_names.add("sonetFarEndLineIntervalTable")

        self.sonetpathcurrenttable = SONETMIB.Sonetpathcurrenttable()
        self.sonetpathcurrenttable.parent = self
        self._children_name_map["sonetpathcurrenttable"] = "sonetPathCurrentTable"
        self._children_yang_names.add("sonetPathCurrentTable")

        self.sonetpathintervaltable = SONETMIB.Sonetpathintervaltable()
        self.sonetpathintervaltable.parent = self
        self._children_name_map["sonetpathintervaltable"] = "sonetPathIntervalTable"
        self._children_yang_names.add("sonetPathIntervalTable")

        self.sonetfarendpathcurrenttable = SONETMIB.Sonetfarendpathcurrenttable()
        self.sonetfarendpathcurrenttable.parent = self
        self._children_name_map["sonetfarendpathcurrenttable"] = "sonetFarEndPathCurrentTable"
        self._children_yang_names.add("sonetFarEndPathCurrentTable")

        self.sonetfarendpathintervaltable = SONETMIB.Sonetfarendpathintervaltable()
        self.sonetfarendpathintervaltable.parent = self
        self._children_name_map["sonetfarendpathintervaltable"] = "sonetFarEndPathIntervalTable"
        self._children_yang_names.add("sonetFarEndPathIntervalTable")

        self.sonetvtcurrenttable = SONETMIB.Sonetvtcurrenttable()
        self.sonetvtcurrenttable.parent = self
        self._children_name_map["sonetvtcurrenttable"] = "sonetVTCurrentTable"
        self._children_yang_names.add("sonetVTCurrentTable")

        self.sonetvtintervaltable = SONETMIB.Sonetvtintervaltable()
        self.sonetvtintervaltable.parent = self
        self._children_name_map["sonetvtintervaltable"] = "sonetVTIntervalTable"
        self._children_yang_names.add("sonetVTIntervalTable")

        self.sonetfarendvtcurrenttable = SONETMIB.Sonetfarendvtcurrenttable()
        self.sonetfarendvtcurrenttable.parent = self
        self._children_name_map["sonetfarendvtcurrenttable"] = "sonetFarEndVTCurrentTable"
        self._children_yang_names.add("sonetFarEndVTCurrentTable")

        self.sonetfarendvtintervaltable = SONETMIB.Sonetfarendvtintervaltable()
        self.sonetfarendvtintervaltable.parent = self
        self._children_name_map["sonetfarendvtintervaltable"] = "sonetFarEndVTIntervalTable"
        self._children_yang_names.add("sonetFarEndVTIntervalTable")
        self._segment_path = lambda: "SONET-MIB:SONET-MIB"


    class Sonetmedium(Entity):
        """
        
        
        .. attribute:: sonetsesthresholdset
        
        	An enumerated integer indicating which recognized set of SES thresholds that the agent uses for determining severely errored seconds and unavailable time.  other(1)   None of the following.  bellcore1991(2)   Bellcore TR\-NWT\-000253, 1991 [TR253], or   ANSI T1M1.3/93\-005R2, 1993 [T1M1.3].   See also Appendix B.  ansi1993(3)   ANSI T1.231, 1993 [T1.231a], or   Bellcore GR\-253\-CORE, Issue 2, 1995 [GR253]  itu1995(4)   ITU Recommendation G.826, 1995 [G.826]  ansi1997(5)   ANSI T1.231, 1997 [T1.231b]  If a manager changes the value of this object then the SES statistics collected prior to this change must be invalidated
        	**type**\:  :py:class:`Sonetsesthresholdset <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmedium.Sonetsesthresholdset>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetmedium, self).__init__()

            self.yang_name = "sonetMedium"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sonetsesthresholdset', YLeaf(YType.enumeration, 'sonetSESthresholdSet')),
            ])
            self.sonetsesthresholdset = None
            self._segment_path = lambda: "sonetMedium"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetmedium, ['sonetsesthresholdset'], name, value)

        class Sonetsesthresholdset(Enum):
            """
            Sonetsesthresholdset (Enum Class)

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



    class Sonetmediumtable(Entity):
        """
        The SONET/SDH Medium table.
        
        .. attribute:: sonetmediumentry
        
        	An entry in the SONET/SDH Medium table
        	**type**\: list of  		 :py:class:`Sonetmediumentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable.Sonetmediumentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetmediumtable, self).__init__()

            self.yang_name = "sonetMediumTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetMediumEntry", ("sonetmediumentry", SONETMIB.Sonetmediumtable.Sonetmediumentry))])
            self._leafs = OrderedDict()

            self.sonetmediumentry = YList(self)
            self._segment_path = lambda: "sonetMediumTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetmediumtable, [], name, value)


        class Sonetmediumentry(Entity):
            """
            An entry in the SONET/SDH Medium table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetmediumtype
            
            	This variable identifies whether a SONET or a SDH signal is used across this interface
            	**type**\:  :py:class:`Sonetmediumtype <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable.Sonetmediumentry.Sonetmediumtype>`
            
            .. attribute:: sonetmediumtimeelapsed
            
            	The number of seconds, including partial seconds, that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 1..900
            
            .. attribute:: sonetmediumvalidintervals
            
            	The number of previous 15\-minute intervals for which data was collected. A SONET/SDH interface must be capable of supporting at least n intervals. The minimum value of n is 4. The default of n is 32. The maximum value of n is 96. The value will be <n> unless the measurement was (re\-)started within the last (<n>\*15) minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases (e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available. 
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: sonetmediumlinecoding
            
            	This variable describes the line coding for this interface. The B3ZS and CMI are used for electrical SONET/SDH signals (STS\-1 and STS\-3). The Non\-Return to Zero (NRZ) and the Return to Zero are used for optical SONET/SDH signals
            	**type**\:  :py:class:`Sonetmediumlinecoding <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable.Sonetmediumentry.Sonetmediumlinecoding>`
            
            .. attribute:: sonetmediumlinetype
            
            	This variable describes the line type for this interface. The line types are Short and Long Range Single Mode fiber or Multi\-Mode fiber interfaces, and coax and UTP for electrical interfaces.  The value sonetOther should be used when the Line Type is not one of the listed values
            	**type**\:  :py:class:`Sonetmediumlinetype <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable.Sonetmediumentry.Sonetmediumlinetype>`
            
            .. attribute:: sonetmediumcircuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting. Note that the circuit identifier, if available, is also represented by ifPhysAddress
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: sonetmediuminvalidintervals
            
            	The number of intervals in the range from 0 to sonetMediumValidIntervals for which no data is available. This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: sonetmediumloopbackconfig
            
            	The current loopback state of the SONET/SDH interface.  The values mean\:    sonetNoLoop      Not in the loopback state. A device that is not      capable of performing a loopback on this interface      shall always return this value.    sonetFacilityLoop      The received signal at this interface is looped back      out through the corresponding transmitter in the return      direction.    sonetTerminalLoop      The signal that is about to be transmitted is connected      to the associated incoming receiver.    sonetOtherLoop      Loopbacks that are not defined here
            	**type**\:  :py:class:`Sonetmediumloopbackconfig <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetmediumtable.Sonetmediumentry.Sonetmediumloopbackconfig>`
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetmediumtable.Sonetmediumentry, self).__init__()

                self.yang_name = "sonetMediumEntry"
                self.yang_parent_name = "sonetMediumTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetmediumtype', YLeaf(YType.enumeration, 'sonetMediumType')),
                    ('sonetmediumtimeelapsed', YLeaf(YType.int32, 'sonetMediumTimeElapsed')),
                    ('sonetmediumvalidintervals', YLeaf(YType.int32, 'sonetMediumValidIntervals')),
                    ('sonetmediumlinecoding', YLeaf(YType.enumeration, 'sonetMediumLineCoding')),
                    ('sonetmediumlinetype', YLeaf(YType.enumeration, 'sonetMediumLineType')),
                    ('sonetmediumcircuitidentifier', YLeaf(YType.str, 'sonetMediumCircuitIdentifier')),
                    ('sonetmediuminvalidintervals', YLeaf(YType.int32, 'sonetMediumInvalidIntervals')),
                    ('sonetmediumloopbackconfig', YLeaf(YType.bits, 'sonetMediumLoopbackConfig')),
                ])
                self.ifindex = None
                self.sonetmediumtype = None
                self.sonetmediumtimeelapsed = None
                self.sonetmediumvalidintervals = None
                self.sonetmediumlinecoding = None
                self.sonetmediumlinetype = None
                self.sonetmediumcircuitidentifier = None
                self.sonetmediuminvalidintervals = None
                self.sonetmediumloopbackconfig = Bits()
                self._segment_path = lambda: "sonetMediumEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetMediumTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetmediumtable.Sonetmediumentry, ['ifindex', 'sonetmediumtype', 'sonetmediumtimeelapsed', 'sonetmediumvalidintervals', 'sonetmediumlinecoding', 'sonetmediumlinetype', 'sonetmediumcircuitidentifier', 'sonetmediuminvalidintervals', 'sonetmediumloopbackconfig'], name, value)

            class Sonetmediumlinecoding(Enum):
                """
                Sonetmediumlinecoding (Enum Class)

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
                Sonetmediumlinetype (Enum Class)

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
                Sonetmediumtype (Enum Class)

                This variable identifies whether a SONET

                or a SDH signal is used across this interface.

                .. data:: sonet = 1

                .. data:: sdh = 2

                """

                sonet = Enum.YLeaf(1, "sonet")

                sdh = Enum.YLeaf(2, "sdh")



    class Sonetsectioncurrenttable(Entity):
        """
        The SONET/SDH Section Current table.
        
        .. attribute:: sonetsectioncurrententry
        
        	An entry in the SONET/SDH Section Current table
        	**type**\: list of  		 :py:class:`Sonetsectioncurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetsectioncurrenttable.Sonetsectioncurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetsectioncurrenttable, self).__init__()

            self.yang_name = "sonetSectionCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetSectionCurrentEntry", ("sonetsectioncurrententry", SONETMIB.Sonetsectioncurrenttable.Sonetsectioncurrententry))])
            self._leafs = OrderedDict()

            self.sonetsectioncurrententry = YList(self)
            self._segment_path = lambda: "sonetSectionCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetsectioncurrenttable, [], name, value)


        class Sonetsectioncurrententry(Entity):
            """
            An entry in the SONET/SDH Section Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetsectioncurrentstatus
            
            	This variable indicates the status of the interface. The sonetSectionCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetSectionNoDefect should be set if and only if no other flag is set.  The various bit positions are\:       1   sonetSectionNoDefect       2   sonetSectionLOS       4   sonetSectionLOF
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: sonetsectioncurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetsectioncurrenttable.Sonetsectioncurrententry, self).__init__()

                self.yang_name = "sonetSectionCurrentEntry"
                self.yang_parent_name = "sonetSectionCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetsectioncurrentstatus', YLeaf(YType.int32, 'sonetSectionCurrentStatus')),
                    ('sonetsectioncurrentess', YLeaf(YType.uint32, 'sonetSectionCurrentESs')),
                    ('sonetsectioncurrentsess', YLeaf(YType.uint32, 'sonetSectionCurrentSESs')),
                    ('sonetsectioncurrentsefss', YLeaf(YType.uint32, 'sonetSectionCurrentSEFSs')),
                    ('sonetsectioncurrentcvs', YLeaf(YType.uint32, 'sonetSectionCurrentCVs')),
                ])
                self.ifindex = None
                self.sonetsectioncurrentstatus = None
                self.sonetsectioncurrentess = None
                self.sonetsectioncurrentsess = None
                self.sonetsectioncurrentsefss = None
                self.sonetsectioncurrentcvs = None
                self._segment_path = lambda: "sonetSectionCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetSectionCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetsectioncurrenttable.Sonetsectioncurrententry, ['ifindex', 'sonetsectioncurrentstatus', 'sonetsectioncurrentess', 'sonetsectioncurrentsess', 'sonetsectioncurrentsefss', 'sonetsectioncurrentcvs'], name, value)


    class Sonetsectionintervaltable(Entity):
        """
        The SONET/SDH Section Interval table.
        
        .. attribute:: sonetsectionintervalentry
        
        	An entry in the SONET/SDH Section Interval table
        	**type**\: list of  		 :py:class:`Sonetsectionintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetsectionintervaltable.Sonetsectionintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetsectionintervaltable, self).__init__()

            self.yang_name = "sonetSectionIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetSectionIntervalEntry", ("sonetsectionintervalentry", SONETMIB.Sonetsectionintervaltable.Sonetsectionintervalentry))])
            self._leafs = OrderedDict()

            self.sonetsectionintervalentry = YList(self)
            self._segment_path = lambda: "sonetSectionIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetsectionintervaltable, [], name, value)


        class Sonetsectionintervalentry(Entity):
            """
            An entry in the SONET/SDH Section Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetsectionintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetsectionintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetsectionintervaltable.Sonetsectionintervalentry, self).__init__()

                self.yang_name = "sonetSectionIntervalEntry"
                self.yang_parent_name = "sonetSectionIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetsectionintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetsectionintervalnumber', YLeaf(YType.int32, 'sonetSectionIntervalNumber')),
                    ('sonetsectionintervaless', YLeaf(YType.uint32, 'sonetSectionIntervalESs')),
                    ('sonetsectionintervalsess', YLeaf(YType.uint32, 'sonetSectionIntervalSESs')),
                    ('sonetsectionintervalsefss', YLeaf(YType.uint32, 'sonetSectionIntervalSEFSs')),
                    ('sonetsectionintervalcvs', YLeaf(YType.uint32, 'sonetSectionIntervalCVs')),
                    ('sonetsectionintervalvaliddata', YLeaf(YType.boolean, 'sonetSectionIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetsectionintervalnumber = None
                self.sonetsectionintervaless = None
                self.sonetsectionintervalsess = None
                self.sonetsectionintervalsefss = None
                self.sonetsectionintervalcvs = None
                self.sonetsectionintervalvaliddata = None
                self._segment_path = lambda: "sonetSectionIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetSectionIntervalNumber='" + str(self.sonetsectionintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetSectionIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetsectionintervaltable.Sonetsectionintervalentry, ['ifindex', 'sonetsectionintervalnumber', 'sonetsectionintervaless', 'sonetsectionintervalsess', 'sonetsectionintervalsefss', 'sonetsectionintervalcvs', 'sonetsectionintervalvaliddata'], name, value)


    class Sonetlinecurrenttable(Entity):
        """
        The SONET/SDH Line Current table.
        
        .. attribute:: sonetlinecurrententry
        
        	An entry in the SONET/SDH Line Current table
        	**type**\: list of  		 :py:class:`Sonetlinecurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetlinecurrenttable.Sonetlinecurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetlinecurrenttable, self).__init__()

            self.yang_name = "sonetLineCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetLineCurrentEntry", ("sonetlinecurrententry", SONETMIB.Sonetlinecurrenttable.Sonetlinecurrententry))])
            self._leafs = OrderedDict()

            self.sonetlinecurrententry = YList(self)
            self._segment_path = lambda: "sonetLineCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetlinecurrenttable, [], name, value)


        class Sonetlinecurrententry(Entity):
            """
            An entry in the SONET/SDH Line Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetlinecurrentstatus
            
            	This variable indicates the status of the interface. The sonetLineCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetLineNoDefect should be set if and only if no other flag is set.  The various bit positions are\:  1   sonetLineNoDefect  2   sonetLineAIS  4   sonetLineRDI
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: sonetlinecurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetlinecurrenttable.Sonetlinecurrententry, self).__init__()

                self.yang_name = "sonetLineCurrentEntry"
                self.yang_parent_name = "sonetLineCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetlinecurrentstatus', YLeaf(YType.int32, 'sonetLineCurrentStatus')),
                    ('sonetlinecurrentess', YLeaf(YType.uint32, 'sonetLineCurrentESs')),
                    ('sonetlinecurrentsess', YLeaf(YType.uint32, 'sonetLineCurrentSESs')),
                    ('sonetlinecurrentcvs', YLeaf(YType.uint32, 'sonetLineCurrentCVs')),
                    ('sonetlinecurrentuass', YLeaf(YType.uint32, 'sonetLineCurrentUASs')),
                ])
                self.ifindex = None
                self.sonetlinecurrentstatus = None
                self.sonetlinecurrentess = None
                self.sonetlinecurrentsess = None
                self.sonetlinecurrentcvs = None
                self.sonetlinecurrentuass = None
                self._segment_path = lambda: "sonetLineCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetLineCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetlinecurrenttable.Sonetlinecurrententry, ['ifindex', 'sonetlinecurrentstatus', 'sonetlinecurrentess', 'sonetlinecurrentsess', 'sonetlinecurrentcvs', 'sonetlinecurrentuass'], name, value)


    class Sonetlineintervaltable(Entity):
        """
        The SONET/SDH Line Interval table.
        
        .. attribute:: sonetlineintervalentry
        
        	An entry in the SONET/SDH Line Interval table
        	**type**\: list of  		 :py:class:`Sonetlineintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetlineintervaltable.Sonetlineintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetlineintervaltable, self).__init__()

            self.yang_name = "sonetLineIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetLineIntervalEntry", ("sonetlineintervalentry", SONETMIB.Sonetlineintervaltable.Sonetlineintervalentry))])
            self._leafs = OrderedDict()

            self.sonetlineintervalentry = YList(self)
            self._segment_path = lambda: "sonetLineIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetlineintervaltable, [], name, value)


        class Sonetlineintervalentry(Entity):
            """
            An entry in the SONET/SDH Line Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetlineintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetlineintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetlineintervaltable.Sonetlineintervalentry, self).__init__()

                self.yang_name = "sonetLineIntervalEntry"
                self.yang_parent_name = "sonetLineIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetlineintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetlineintervalnumber', YLeaf(YType.int32, 'sonetLineIntervalNumber')),
                    ('sonetlineintervaless', YLeaf(YType.uint32, 'sonetLineIntervalESs')),
                    ('sonetlineintervalsess', YLeaf(YType.uint32, 'sonetLineIntervalSESs')),
                    ('sonetlineintervalcvs', YLeaf(YType.uint32, 'sonetLineIntervalCVs')),
                    ('sonetlineintervaluass', YLeaf(YType.uint32, 'sonetLineIntervalUASs')),
                    ('sonetlineintervalvaliddata', YLeaf(YType.boolean, 'sonetLineIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetlineintervalnumber = None
                self.sonetlineintervaless = None
                self.sonetlineintervalsess = None
                self.sonetlineintervalcvs = None
                self.sonetlineintervaluass = None
                self.sonetlineintervalvaliddata = None
                self._segment_path = lambda: "sonetLineIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetLineIntervalNumber='" + str(self.sonetlineintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetLineIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetlineintervaltable.Sonetlineintervalentry, ['ifindex', 'sonetlineintervalnumber', 'sonetlineintervaless', 'sonetlineintervalsess', 'sonetlineintervalcvs', 'sonetlineintervaluass', 'sonetlineintervalvaliddata'], name, value)


    class Sonetfarendlinecurrenttable(Entity):
        """
        The SONET/SDH Far End Line Current table.
        
        .. attribute:: sonetfarendlinecurrententry
        
        	An entry in the SONET/SDH Far End Line Current table
        	**type**\: list of  		 :py:class:`Sonetfarendlinecurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendlinecurrenttable, self).__init__()

            self.yang_name = "sonetFarEndLineCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndLineCurrentEntry", ("sonetfarendlinecurrententry", SONETMIB.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry))])
            self._leafs = OrderedDict()

            self.sonetfarendlinecurrententry = YList(self)
            self._segment_path = lambda: "sonetFarEndLineCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendlinecurrenttable, [], name, value)


        class Sonetfarendlinecurrententry(Entity):
            """
            An entry in the SONET/SDH Far End Line Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendlinecurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry, self).__init__()

                self.yang_name = "sonetFarEndLineCurrentEntry"
                self.yang_parent_name = "sonetFarEndLineCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendlinecurrentess', YLeaf(YType.uint32, 'sonetFarEndLineCurrentESs')),
                    ('sonetfarendlinecurrentsess', YLeaf(YType.uint32, 'sonetFarEndLineCurrentSESs')),
                    ('sonetfarendlinecurrentcvs', YLeaf(YType.uint32, 'sonetFarEndLineCurrentCVs')),
                    ('sonetfarendlinecurrentuass', YLeaf(YType.uint32, 'sonetFarEndLineCurrentUASs')),
                ])
                self.ifindex = None
                self.sonetfarendlinecurrentess = None
                self.sonetfarendlinecurrentsess = None
                self.sonetfarendlinecurrentcvs = None
                self.sonetfarendlinecurrentuass = None
                self._segment_path = lambda: "sonetFarEndLineCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndLineCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry, ['ifindex', 'sonetfarendlinecurrentess', 'sonetfarendlinecurrentsess', 'sonetfarendlinecurrentcvs', 'sonetfarendlinecurrentuass'], name, value)


    class Sonetfarendlineintervaltable(Entity):
        """
        The SONET/SDH Far End Line Interval table.
        
        .. attribute:: sonetfarendlineintervalentry
        
        	An entry in the SONET/SDH Far End Line Interval table
        	**type**\: list of  		 :py:class:`Sonetfarendlineintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendlineintervaltable, self).__init__()

            self.yang_name = "sonetFarEndLineIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndLineIntervalEntry", ("sonetfarendlineintervalentry", SONETMIB.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry))])
            self._leafs = OrderedDict()

            self.sonetfarendlineintervalentry = YList(self)
            self._segment_path = lambda: "sonetFarEndLineIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendlineintervaltable, [], name, value)


        class Sonetfarendlineintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End Line Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendlineintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendlineintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry, self).__init__()

                self.yang_name = "sonetFarEndLineIntervalEntry"
                self.yang_parent_name = "sonetFarEndLineIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetfarendlineintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendlineintervalnumber', YLeaf(YType.int32, 'sonetFarEndLineIntervalNumber')),
                    ('sonetfarendlineintervaless', YLeaf(YType.uint32, 'sonetFarEndLineIntervalESs')),
                    ('sonetfarendlineintervalsess', YLeaf(YType.uint32, 'sonetFarEndLineIntervalSESs')),
                    ('sonetfarendlineintervalcvs', YLeaf(YType.uint32, 'sonetFarEndLineIntervalCVs')),
                    ('sonetfarendlineintervaluass', YLeaf(YType.uint32, 'sonetFarEndLineIntervalUASs')),
                    ('sonetfarendlineintervalvaliddata', YLeaf(YType.boolean, 'sonetFarEndLineIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetfarendlineintervalnumber = None
                self.sonetfarendlineintervaless = None
                self.sonetfarendlineintervalsess = None
                self.sonetfarendlineintervalcvs = None
                self.sonetfarendlineintervaluass = None
                self.sonetfarendlineintervalvaliddata = None
                self._segment_path = lambda: "sonetFarEndLineIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetFarEndLineIntervalNumber='" + str(self.sonetfarendlineintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndLineIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry, ['ifindex', 'sonetfarendlineintervalnumber', 'sonetfarendlineintervaless', 'sonetfarendlineintervalsess', 'sonetfarendlineintervalcvs', 'sonetfarendlineintervaluass', 'sonetfarendlineintervalvaliddata'], name, value)


    class Sonetpathcurrenttable(Entity):
        """
        The SONET/SDH Path Current table.
        
        .. attribute:: sonetpathcurrententry
        
        	An entry in the SONET/SDH Path Current table
        	**type**\: list of  		 :py:class:`Sonetpathcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetpathcurrenttable, self).__init__()

            self.yang_name = "sonetPathCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetPathCurrentEntry", ("sonetpathcurrententry", SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry))])
            self._leafs = OrderedDict()

            self.sonetpathcurrententry = YList(self)
            self._segment_path = lambda: "sonetPathCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetpathcurrenttable, [], name, value)


        class Sonetpathcurrententry(Entity):
            """
            An entry in the SONET/SDH Path Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetpathcurrentwidth
            
            	A value that indicates the type of the SONET/SDH Path.  For SONET, the assigned types are the STS\-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768. STS\-1 is equal to 51.84 Mbps.  For SDH, the assigned types are the STM\-Nc VCs, where N = 1, 4, 16, 64 and 256
            	**type**\:  :py:class:`Sonetpathcurrentwidth <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry.Sonetpathcurrentwidth>`
            
            .. attribute:: sonetpathcurrentstatus
            
            	This variable indicates the status of the interface. The sonetPathCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetPathNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetPathNoDefect    2   sonetPathSTSLOP    4   sonetPathSTSAIS    8   sonetPathSTSRDI   16   sonetPathUnequipped   32   sonetPathSignalLabelMismatch
            	**type**\: int
            
            	**range:** 1..62
            
            .. attribute:: sonetpathcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cspsonetpathpayload
            
            	Specifies the payload carried by the SONET/SDH Path. The payload specification corresponds to C2 (Signal Label) overhead byte in SONET/SDH Path Overhead\: unequipped(1)    \: Path is not provisioned to carry any payload. unspecified(2)   \: Path is carrying an unspecifed payload. ds3(3)           \: Path is carrying a DS3 path as payload. vt15vc11(4)      \: Path is carrying SONET\-VT1.5/SDH\-VC11 payload. vt2vc12(5)       \: Path is carrying SONET\-VT2/SDH\-VC12 as payload. atmCell(6)       \: Path is carrying ATM Cells as payload. hdlcFr(7)        \: Path is carrying Frame Relay (HDLC) payload. e3(8)            \: Path is carrying an E3 path as payload. vtStructured(9)  \: Path is carrying VTGs/TUG3s/TUG2s which may                    each carry a different payload.  A write operation on this object will result in update to C2 overhead byte in the Path Overhead
            	**type**\:  :py:class:`Cspsonetpathpayload <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry.Cspsonetpathpayload>`
            
            .. attribute:: csptributarymappingtype
            
            	This object represents the VT/VC mapping type. asynchronous\: In this mode, the channel structure of                DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside                   the VT/VC can be found and extracted                   from the frame. The initial value is asynchronous(1)
            	**type**\:  :py:class:`Csptributarymappingtype <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry.Csptributarymappingtype>`
            
            .. attribute:: cspsignallingtransportmode
            
            	This object represents the mode used to transport DS0  Signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling  is transferred to the VT header. In clearMode(3), only  the framing bit is transferred to the VT header.           The initial value is signallingTransferMode(2)  if csTributaryMappingType is byteSynchronous.  For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\:  :py:class:`Cspsignallingtransportmode <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry.Cspsignallingtransportmode>`
            
            .. attribute:: csptributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.  au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.  au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  The initial value is au3Grouping(2) for SDH and  notApplicable(1) for SONET
            	**type**\:  :py:class:`Csptributarygroupingtype <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry.Csptributarygroupingtype>`
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry, self).__init__()

                self.yang_name = "sonetPathCurrentEntry"
                self.yang_parent_name = "sonetPathCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetpathcurrentwidth', YLeaf(YType.enumeration, 'sonetPathCurrentWidth')),
                    ('sonetpathcurrentstatus', YLeaf(YType.int32, 'sonetPathCurrentStatus')),
                    ('sonetpathcurrentess', YLeaf(YType.uint32, 'sonetPathCurrentESs')),
                    ('sonetpathcurrentsess', YLeaf(YType.uint32, 'sonetPathCurrentSESs')),
                    ('sonetpathcurrentcvs', YLeaf(YType.uint32, 'sonetPathCurrentCVs')),
                    ('sonetpathcurrentuass', YLeaf(YType.uint32, 'sonetPathCurrentUASs')),
                    ('cspsonetpathpayload', YLeaf(YType.enumeration, 'CISCO-SONET-MIB:cspSonetPathPayload')),
                    ('csptributarymappingtype', YLeaf(YType.enumeration, 'CISCO-SONET-MIB:cspTributaryMappingType')),
                    ('cspsignallingtransportmode', YLeaf(YType.enumeration, 'CISCO-SONET-MIB:cspSignallingTransportMode')),
                    ('csptributarygroupingtype', YLeaf(YType.enumeration, 'CISCO-SONET-MIB:cspTributaryGroupingType')),
                ])
                self.ifindex = None
                self.sonetpathcurrentwidth = None
                self.sonetpathcurrentstatus = None
                self.sonetpathcurrentess = None
                self.sonetpathcurrentsess = None
                self.sonetpathcurrentcvs = None
                self.sonetpathcurrentuass = None
                self.cspsonetpathpayload = None
                self.csptributarymappingtype = None
                self.cspsignallingtransportmode = None
                self.csptributarygroupingtype = None
                self._segment_path = lambda: "sonetPathCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetPathCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetpathcurrenttable.Sonetpathcurrententry, ['ifindex', 'sonetpathcurrentwidth', 'sonetpathcurrentstatus', 'sonetpathcurrentess', 'sonetpathcurrentsess', 'sonetpathcurrentcvs', 'sonetpathcurrentuass', 'cspsonetpathpayload', 'csptributarymappingtype', 'cspsignallingtransportmode', 'csptributarygroupingtype'], name, value)

            class Cspsignallingtransportmode(Enum):
                """
                Cspsignallingtransportmode (Enum Class)

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
                Cspsonetpathpayload (Enum Class)

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
                Csptributarygroupingtype (Enum Class)

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
                Csptributarymappingtype (Enum Class)

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
                Sonetpathcurrentwidth (Enum Class)

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



    class Sonetpathintervaltable(Entity):
        """
        The SONET/SDH Path Interval table.
        
        .. attribute:: sonetpathintervalentry
        
        	An entry in the SONET/SDH Path Interval table
        	**type**\: list of  		 :py:class:`Sonetpathintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetpathintervaltable.Sonetpathintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetpathintervaltable, self).__init__()

            self.yang_name = "sonetPathIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetPathIntervalEntry", ("sonetpathintervalentry", SONETMIB.Sonetpathintervaltable.Sonetpathintervalentry))])
            self._leafs = OrderedDict()

            self.sonetpathintervalentry = YList(self)
            self._segment_path = lambda: "sonetPathIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetpathintervaltable, [], name, value)


        class Sonetpathintervalentry(Entity):
            """
            An entry in the SONET/SDH Path Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetpathintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetpathintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetpathintervaltable.Sonetpathintervalentry, self).__init__()

                self.yang_name = "sonetPathIntervalEntry"
                self.yang_parent_name = "sonetPathIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetpathintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetpathintervalnumber', YLeaf(YType.int32, 'sonetPathIntervalNumber')),
                    ('sonetpathintervaless', YLeaf(YType.uint32, 'sonetPathIntervalESs')),
                    ('sonetpathintervalsess', YLeaf(YType.uint32, 'sonetPathIntervalSESs')),
                    ('sonetpathintervalcvs', YLeaf(YType.uint32, 'sonetPathIntervalCVs')),
                    ('sonetpathintervaluass', YLeaf(YType.uint32, 'sonetPathIntervalUASs')),
                    ('sonetpathintervalvaliddata', YLeaf(YType.boolean, 'sonetPathIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetpathintervalnumber = None
                self.sonetpathintervaless = None
                self.sonetpathintervalsess = None
                self.sonetpathintervalcvs = None
                self.sonetpathintervaluass = None
                self.sonetpathintervalvaliddata = None
                self._segment_path = lambda: "sonetPathIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetPathIntervalNumber='" + str(self.sonetpathintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetPathIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetpathintervaltable.Sonetpathintervalentry, ['ifindex', 'sonetpathintervalnumber', 'sonetpathintervaless', 'sonetpathintervalsess', 'sonetpathintervalcvs', 'sonetpathintervaluass', 'sonetpathintervalvaliddata'], name, value)


    class Sonetfarendpathcurrenttable(Entity):
        """
        The SONET/SDH Far End Path Current table.
        
        .. attribute:: sonetfarendpathcurrententry
        
        	An entry in the SONET/SDH Far End Path Current table
        	**type**\: list of  		 :py:class:`Sonetfarendpathcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendpathcurrenttable, self).__init__()

            self.yang_name = "sonetFarEndPathCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndPathCurrentEntry", ("sonetfarendpathcurrententry", SONETMIB.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry))])
            self._leafs = OrderedDict()

            self.sonetfarendpathcurrententry = YList(self)
            self._segment_path = lambda: "sonetFarEndPathCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendpathcurrenttable, [], name, value)


        class Sonetfarendpathcurrententry(Entity):
            """
            An entry in the SONET/SDH Far End Path Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendpathcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry, self).__init__()

                self.yang_name = "sonetFarEndPathCurrentEntry"
                self.yang_parent_name = "sonetFarEndPathCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendpathcurrentess', YLeaf(YType.uint32, 'sonetFarEndPathCurrentESs')),
                    ('sonetfarendpathcurrentsess', YLeaf(YType.uint32, 'sonetFarEndPathCurrentSESs')),
                    ('sonetfarendpathcurrentcvs', YLeaf(YType.uint32, 'sonetFarEndPathCurrentCVs')),
                    ('sonetfarendpathcurrentuass', YLeaf(YType.uint32, 'sonetFarEndPathCurrentUASs')),
                ])
                self.ifindex = None
                self.sonetfarendpathcurrentess = None
                self.sonetfarendpathcurrentsess = None
                self.sonetfarendpathcurrentcvs = None
                self.sonetfarendpathcurrentuass = None
                self._segment_path = lambda: "sonetFarEndPathCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndPathCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry, ['ifindex', 'sonetfarendpathcurrentess', 'sonetfarendpathcurrentsess', 'sonetfarendpathcurrentcvs', 'sonetfarendpathcurrentuass'], name, value)


    class Sonetfarendpathintervaltable(Entity):
        """
        The SONET/SDH Far End Path Interval table.
        
        .. attribute:: sonetfarendpathintervalentry
        
        	An entry in the SONET/SDH Far End Path Interval table
        	**type**\: list of  		 :py:class:`Sonetfarendpathintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendpathintervaltable, self).__init__()

            self.yang_name = "sonetFarEndPathIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndPathIntervalEntry", ("sonetfarendpathintervalentry", SONETMIB.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry))])
            self._leafs = OrderedDict()

            self.sonetfarendpathintervalentry = YList(self)
            self._segment_path = lambda: "sonetFarEndPathIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendpathintervaltable, [], name, value)


        class Sonetfarendpathintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End Path Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendpathintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendpathintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry, self).__init__()

                self.yang_name = "sonetFarEndPathIntervalEntry"
                self.yang_parent_name = "sonetFarEndPathIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetfarendpathintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendpathintervalnumber', YLeaf(YType.int32, 'sonetFarEndPathIntervalNumber')),
                    ('sonetfarendpathintervaless', YLeaf(YType.uint32, 'sonetFarEndPathIntervalESs')),
                    ('sonetfarendpathintervalsess', YLeaf(YType.uint32, 'sonetFarEndPathIntervalSESs')),
                    ('sonetfarendpathintervalcvs', YLeaf(YType.uint32, 'sonetFarEndPathIntervalCVs')),
                    ('sonetfarendpathintervaluass', YLeaf(YType.uint32, 'sonetFarEndPathIntervalUASs')),
                    ('sonetfarendpathintervalvaliddata', YLeaf(YType.boolean, 'sonetFarEndPathIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetfarendpathintervalnumber = None
                self.sonetfarendpathintervaless = None
                self.sonetfarendpathintervalsess = None
                self.sonetfarendpathintervalcvs = None
                self.sonetfarendpathintervaluass = None
                self.sonetfarendpathintervalvaliddata = None
                self._segment_path = lambda: "sonetFarEndPathIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetFarEndPathIntervalNumber='" + str(self.sonetfarendpathintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndPathIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry, ['ifindex', 'sonetfarendpathintervalnumber', 'sonetfarendpathintervaless', 'sonetfarendpathintervalsess', 'sonetfarendpathintervalcvs', 'sonetfarendpathintervaluass', 'sonetfarendpathintervalvaliddata'], name, value)


    class Sonetvtcurrenttable(Entity):
        """
        The SONET/SDH VT Current table.
        
        .. attribute:: sonetvtcurrententry
        
        	An entry in the SONET/SDH VT Current table
        	**type**\: list of  		 :py:class:`Sonetvtcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetvtcurrenttable.Sonetvtcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetvtcurrenttable, self).__init__()

            self.yang_name = "sonetVTCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetVTCurrentEntry", ("sonetvtcurrententry", SONETMIB.Sonetvtcurrenttable.Sonetvtcurrententry))])
            self._leafs = OrderedDict()

            self.sonetvtcurrententry = YList(self)
            self._segment_path = lambda: "sonetVTCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetvtcurrenttable, [], name, value)


        class Sonetvtcurrententry(Entity):
            """
            An entry in the SONET/SDH VT Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetvtcurrentwidth
            
            	A value that indicates the type of the SONET VT and SDH VC.  Assigned widths are VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c
            	**type**\:  :py:class:`Sonetvtcurrentwidth <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetvtcurrenttable.Sonetvtcurrententry.Sonetvtcurrentwidth>`
            
            .. attribute:: sonetvtcurrentstatus
            
            	This variable indicates the status of the interface. The sonetVTCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects and failures simultaneously. The sonetVTNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetVTNoDefect    2   sonetVTLOP    4   sonetVTPathAIS    8   sonetVTPathRDI   16   sonetVTPathRFI   32   sonetVTUnequipped   64   sonetVTSignalLabelMismatch
            	**type**\: int
            
            	**range:** 1..126
            
            .. attribute:: sonetvtcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetvtcurrenttable.Sonetvtcurrententry, self).__init__()

                self.yang_name = "sonetVTCurrentEntry"
                self.yang_parent_name = "sonetVTCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetvtcurrentwidth', YLeaf(YType.enumeration, 'sonetVTCurrentWidth')),
                    ('sonetvtcurrentstatus', YLeaf(YType.int32, 'sonetVTCurrentStatus')),
                    ('sonetvtcurrentess', YLeaf(YType.uint32, 'sonetVTCurrentESs')),
                    ('sonetvtcurrentsess', YLeaf(YType.uint32, 'sonetVTCurrentSESs')),
                    ('sonetvtcurrentcvs', YLeaf(YType.uint32, 'sonetVTCurrentCVs')),
                    ('sonetvtcurrentuass', YLeaf(YType.uint32, 'sonetVTCurrentUASs')),
                ])
                self.ifindex = None
                self.sonetvtcurrentwidth = None
                self.sonetvtcurrentstatus = None
                self.sonetvtcurrentess = None
                self.sonetvtcurrentsess = None
                self.sonetvtcurrentcvs = None
                self.sonetvtcurrentuass = None
                self._segment_path = lambda: "sonetVTCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetVTCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetvtcurrenttable.Sonetvtcurrententry, ['ifindex', 'sonetvtcurrentwidth', 'sonetvtcurrentstatus', 'sonetvtcurrentess', 'sonetvtcurrentsess', 'sonetvtcurrentcvs', 'sonetvtcurrentuass'], name, value)

            class Sonetvtcurrentwidth(Enum):
                """
                Sonetvtcurrentwidth (Enum Class)

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



    class Sonetvtintervaltable(Entity):
        """
        The SONET/SDH VT Interval table.
        
        .. attribute:: sonetvtintervalentry
        
        	An entry in the SONET/SDH VT Interval table
        	**type**\: list of  		 :py:class:`Sonetvtintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetvtintervaltable.Sonetvtintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetvtintervaltable, self).__init__()

            self.yang_name = "sonetVTIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetVTIntervalEntry", ("sonetvtintervalentry", SONETMIB.Sonetvtintervaltable.Sonetvtintervalentry))])
            self._leafs = OrderedDict()

            self.sonetvtintervalentry = YList(self)
            self._segment_path = lambda: "sonetVTIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetvtintervaltable, [], name, value)


        class Sonetvtintervalentry(Entity):
            """
            An entry in the SONET/SDH VT Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetvtintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetvtintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetvtintervaltable.Sonetvtintervalentry, self).__init__()

                self.yang_name = "sonetVTIntervalEntry"
                self.yang_parent_name = "sonetVTIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetvtintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetvtintervalnumber', YLeaf(YType.int32, 'sonetVTIntervalNumber')),
                    ('sonetvtintervaless', YLeaf(YType.uint32, 'sonetVTIntervalESs')),
                    ('sonetvtintervalsess', YLeaf(YType.uint32, 'sonetVTIntervalSESs')),
                    ('sonetvtintervalcvs', YLeaf(YType.uint32, 'sonetVTIntervalCVs')),
                    ('sonetvtintervaluass', YLeaf(YType.uint32, 'sonetVTIntervalUASs')),
                    ('sonetvtintervalvaliddata', YLeaf(YType.boolean, 'sonetVTIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetvtintervalnumber = None
                self.sonetvtintervaless = None
                self.sonetvtintervalsess = None
                self.sonetvtintervalcvs = None
                self.sonetvtintervaluass = None
                self.sonetvtintervalvaliddata = None
                self._segment_path = lambda: "sonetVTIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetVTIntervalNumber='" + str(self.sonetvtintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetVTIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetvtintervaltable.Sonetvtintervalentry, ['ifindex', 'sonetvtintervalnumber', 'sonetvtintervaless', 'sonetvtintervalsess', 'sonetvtintervalcvs', 'sonetvtintervaluass', 'sonetvtintervalvaliddata'], name, value)


    class Sonetfarendvtcurrenttable(Entity):
        """
        The SONET/SDH Far End VT Current table.
        
        .. attribute:: sonetfarendvtcurrententry
        
        	An entry in the SONET/SDH Far End VT Current table
        	**type**\: list of  		 :py:class:`Sonetfarendvtcurrententry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendvtcurrenttable, self).__init__()

            self.yang_name = "sonetFarEndVTCurrentTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndVTCurrentEntry", ("sonetfarendvtcurrententry", SONETMIB.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry))])
            self._leafs = OrderedDict()

            self.sonetfarendvtcurrententry = YList(self)
            self._segment_path = lambda: "sonetFarEndVTCurrentTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendvtcurrenttable, [], name, value)


        class Sonetfarendvtcurrententry(Entity):
            """
            An entry in the SONET/SDH Far End VT Current table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendvtcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry, self).__init__()

                self.yang_name = "sonetFarEndVTCurrentEntry"
                self.yang_parent_name = "sonetFarEndVTCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendvtcurrentess', YLeaf(YType.uint32, 'sonetFarEndVTCurrentESs')),
                    ('sonetfarendvtcurrentsess', YLeaf(YType.uint32, 'sonetFarEndVTCurrentSESs')),
                    ('sonetfarendvtcurrentcvs', YLeaf(YType.uint32, 'sonetFarEndVTCurrentCVs')),
                    ('sonetfarendvtcurrentuass', YLeaf(YType.uint32, 'sonetFarEndVTCurrentUASs')),
                ])
                self.ifindex = None
                self.sonetfarendvtcurrentess = None
                self.sonetfarendvtcurrentsess = None
                self.sonetfarendvtcurrentcvs = None
                self.sonetfarendvtcurrentuass = None
                self._segment_path = lambda: "sonetFarEndVTCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndVTCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry, ['ifindex', 'sonetfarendvtcurrentess', 'sonetfarendvtcurrentsess', 'sonetfarendvtcurrentcvs', 'sonetfarendvtcurrentuass'], name, value)


    class Sonetfarendvtintervaltable(Entity):
        """
        The SONET/SDH Far End VT Interval table.
        
        .. attribute:: sonetfarendvtintervalentry
        
        	An entry in the SONET/SDH Far End VT Interval table
        	**type**\: list of  		 :py:class:`Sonetfarendvtintervalentry <ydk.models.cisco_ios_xe.SONET_MIB.SONETMIB.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry>`
        
        

        """

        _prefix = 'SONET-MIB'
        _revision = '2003-08-11'

        def __init__(self):
            super(SONETMIB.Sonetfarendvtintervaltable, self).__init__()

            self.yang_name = "sonetFarEndVTIntervalTable"
            self.yang_parent_name = "SONET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sonetFarEndVTIntervalEntry", ("sonetfarendvtintervalentry", SONETMIB.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry))])
            self._leafs = OrderedDict()

            self.sonetfarendvtintervalentry = YList(self)
            self._segment_path = lambda: "sonetFarEndVTIntervalTable"
            self._absolute_path = lambda: "SONET-MIB:SONET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SONETMIB.Sonetfarendvtintervaltable, [], name, value)


        class Sonetfarendvtintervalentry(Entity):
            """
            An entry in the SONET/SDH Far
            End VT Interval table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: sonetfarendvtintervalnumber  (key)
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendvtintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'SONET-MIB'
            _revision = '2003-08-11'

            def __init__(self):
                super(SONETMIB.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry, self).__init__()

                self.yang_name = "sonetFarEndVTIntervalEntry"
                self.yang_parent_name = "sonetFarEndVTIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','sonetfarendvtintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('sonetfarendvtintervalnumber', YLeaf(YType.int32, 'sonetFarEndVTIntervalNumber')),
                    ('sonetfarendvtintervaless', YLeaf(YType.uint32, 'sonetFarEndVTIntervalESs')),
                    ('sonetfarendvtintervalsess', YLeaf(YType.uint32, 'sonetFarEndVTIntervalSESs')),
                    ('sonetfarendvtintervalcvs', YLeaf(YType.uint32, 'sonetFarEndVTIntervalCVs')),
                    ('sonetfarendvtintervaluass', YLeaf(YType.uint32, 'sonetFarEndVTIntervalUASs')),
                    ('sonetfarendvtintervalvaliddata', YLeaf(YType.boolean, 'sonetFarEndVTIntervalValidData')),
                ])
                self.ifindex = None
                self.sonetfarendvtintervalnumber = None
                self.sonetfarendvtintervaless = None
                self.sonetfarendvtintervalsess = None
                self.sonetfarendvtintervalcvs = None
                self.sonetfarendvtintervaluass = None
                self.sonetfarendvtintervalvaliddata = None
                self._segment_path = lambda: "sonetFarEndVTIntervalEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[sonetFarEndVTIntervalNumber='" + str(self.sonetfarendvtintervalnumber) + "']"
                self._absolute_path = lambda: "SONET-MIB:SONET-MIB/sonetFarEndVTIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SONETMIB.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry, ['ifindex', 'sonetfarendvtintervalnumber', 'sonetfarendvtintervaless', 'sonetfarendvtintervalsess', 'sonetfarendvtintervalcvs', 'sonetfarendvtintervaluass', 'sonetfarendvtintervalvaliddata'], name, value)

    def clone_ptr(self):
        self._top_entity = SONETMIB()
        return self._top_entity

