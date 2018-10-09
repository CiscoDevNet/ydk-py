""" CISCO_POWER_ETHERNET_EXT_MIB 

A MIB module for extending the POWER\-ETHERNET\-MIB
(RFC3621) to add objects which provide additional
management information about Power Sourcing Equipment
(PSE) not available in POWER\-ETHERNET\-MIB.

Glossary

Power Sourcing Equipment (PSE)
    These are devices supplying electrical power to
    other equipment. They are, for example, inline power
    switches, inline power daughterboards and power patch
    panels.

Powered Device (PD)
    These are devices receiving their electrical power
    supply from Power Sourcing Equipment. They are, for
    example, IP telephones and wireless access points
    or bridges.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CpeExtLldpPwrClassOrZero(Enum):
    """
    CpeExtLldpPwrClassOrZero (Enum Class)

    The power class of the PD or PSE port that implements

    the LLDP based Data Link Layer power classification

    'unknown' \- power classification of the powered devices is

                unknown.

    'class0'  \- power classification of the powered devices is

                class 0 in IEEE specifications.

    'class1'  \- power classification of the powered devices is

                class 1 in IEEE specifications.

    'class2'  \- power classification of the powered devices is

                class 2 in IEEE specifications.

    'class3'  \- power classification of the powered devices is

                class 3 in IEEE specifications.

    'class4'  \- power classification of the powered devices is

                class 4 in IEEE specifications.

    .. data:: unknown = 0

    .. data:: class0 = 1

    .. data:: class1 = 2

    .. data:: class2 = 3

    .. data:: class3 = 4

    .. data:: class4 = 5

    """

    unknown = Enum.YLeaf(0, "unknown")

    class0 = Enum.YLeaf(1, "class0")

    class1 = Enum.YLeaf(2, "class1")

    class2 = Enum.YLeaf(3, "class2")

    class3 = Enum.YLeaf(4, "class3")

    class4 = Enum.YLeaf(5, "class4")


class CpeExtLldpPwrSrc(Enum):
    """
    CpeExtLldpPwrSrc (Enum Class)

    The power source of the PD or PSE port which implements the

    LLDP based Data Link Layer power classification.

    'pseAndLocal'   \- A PD powered both locally and by a PSE.

    'local'         \- A PD powered locally only.

    'pse'           \- A PD powered by a PSE only.

    'backupSrc'     \- A PSE powered by a backup power source.

    'primarySrc'    \- A PSE powered by its primary power source.

    'unknown'       \- A PD or PSE where the power source is

                      unknown.

    .. data:: pseAndLocal = 1

    .. data:: local = 2

    .. data:: pse = 3

    .. data:: backupSrc = 4

    .. data:: primarySrc = 5

    .. data:: unknown = 6

    """

    pseAndLocal = Enum.YLeaf(1, "pseAndLocal")

    local = Enum.YLeaf(2, "local")

    pse = Enum.YLeaf(3, "pse")

    backupSrc = Enum.YLeaf(4, "backupSrc")

    primarySrc = Enum.YLeaf(5, "primarySrc")

    unknown = Enum.YLeaf(6, "unknown")


class CpeExtLldpPwrType(Enum):
    """
    CpeExtLldpPwrType (Enum Class)

    The requested Data Terminal Equipment (DTE) Power via

    Media Dependent Interface (MDI) type based on Data Link Layer

    (DLL) power classification.

    In Data Link Layer power classification, the PSE and PD perform 

    power negotiation using the Link Layer Discovery Protocol (LLDP)

    as soon as the data link is established. It has finer power

    resolution than the Physical Layer power classification and has

    the ability for the PSE and PD to participate in dynamic power

    allocation wherein allocated power to the PD may change one or

    more times during PD operation.

    'type1Pd'  \- A PD that advertises a power draw less than or 

                 equal to 12.95 W (at the PD).

    'type1Pse' \- A PSE that is designed to support a Type 1 PD.

    'type2Pd'  \- A PD that advertises a power draw greater than

                 12.95 W (at the PD).

    'type2Pse  \- A PSE that is designed to support either a Type 1

                 or a Type 2 PD.

    .. data:: type1Pd = 1

    .. data:: type1Pse = 2

    .. data:: type2Pd = 3

    .. data:: type2Pse = 4

    """

    type1Pd = Enum.YLeaf(1, "type1Pd")

    type1Pse = Enum.YLeaf(2, "type1Pse")

    type2Pd = Enum.YLeaf(3, "type2Pd")

    type2Pse = Enum.YLeaf(4, "type2Pse")


class CpeExtPwrPriority(Enum):
    """
    CpeExtPwrPriority (Enum Class)

    The power priority for the PD on the PSE port which implements

    the LLDP based Data Link Layer power classification.

    'critical' \- power priority is at critical level.

    'high'     \- power priority is at high level.

    'low'      \- power priority is at low level.

    'unknown'  \- power priority level is unknown.

    .. data:: critical = 1

    .. data:: high = 2

    .. data:: low = 3

    .. data:: unknown = 4

    """

    critical = Enum.YLeaf(1, "critical")

    high = Enum.YLeaf(2, "high")

    low = Enum.YLeaf(3, "low")

    unknown = Enum.YLeaf(4, "unknown")



class CISCOPOWERETHERNETEXTMIB(Entity):
    """
    
    
    .. attribute:: cpeextmibobjects
    
    	
    	**type**\:  :py:class:`CpeExtMIBObjects <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtMIBObjects>`
    
    .. attribute:: cpeextpdstatistics
    
    	
    	**type**\:  :py:class:`CpeExtPdStatistics <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPdStatistics>`
    
    .. attribute:: cpeextmainpsetable
    
    	This table contains the additional information for the main PSE group in pethMainPseTable
    	**type**\:  :py:class:`CpeExtMainPseTable <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable>`
    
    .. attribute:: cpeextpdstatstable
    
    	This table contains the statistics information of the powered devices fallen into different power classifications in the system
    	**type**\:  :py:class:`CpeExtPdStatsTable <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable>`
    
    .. attribute:: cpeextpseportlldptable
    
    	A table provides the Link Layer Discovery Protocol (LLDP) based Data Link Layer (DLL) power classification characteristics of PSE ports and PDs attached to them
    	**type**\:  :py:class:`CpeExtPsePortLldpTable <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable>`
    
    

    """

    _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
    _revision = '2018-01-19'

    def __init__(self):
        super(CISCOPOWERETHERNETEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-POWER-ETHERNET-EXT-MIB"
        self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpeExtMIBObjects", ("cpeextmibobjects", CISCOPOWERETHERNETEXTMIB.CpeExtMIBObjects)), ("cpeExtPdStatistics", ("cpeextpdstatistics", CISCOPOWERETHERNETEXTMIB.CpeExtPdStatistics)), ("cpeExtMainPseTable", ("cpeextmainpsetable", CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable)), ("cpeExtPdStatsTable", ("cpeextpdstatstable", CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable)), ("cpeExtPsePortLldpTable", ("cpeextpseportlldptable", CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable))])
        self._leafs = OrderedDict()

        self.cpeextmibobjects = CISCOPOWERETHERNETEXTMIB.CpeExtMIBObjects()
        self.cpeextmibobjects.parent = self
        self._children_name_map["cpeextmibobjects"] = "cpeExtMIBObjects"

        self.cpeextpdstatistics = CISCOPOWERETHERNETEXTMIB.CpeExtPdStatistics()
        self.cpeextpdstatistics.parent = self
        self._children_name_map["cpeextpdstatistics"] = "cpeExtPdStatistics"

        self.cpeextmainpsetable = CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable()
        self.cpeextmainpsetable.parent = self
        self._children_name_map["cpeextmainpsetable"] = "cpeExtMainPseTable"

        self.cpeextpdstatstable = CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable()
        self.cpeextpdstatstable.parent = self
        self._children_name_map["cpeextpdstatstable"] = "cpeExtPdStatsTable"

        self.cpeextpseportlldptable = CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable()
        self.cpeextpseportlldptable.parent = self
        self._children_name_map["cpeextpseportlldptable"] = "cpeExtPsePortLldpTable"
        self._segment_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOPOWERETHERNETEXTMIB, [], name, value)


    class CpeExtMIBObjects(Entity):
        """
        
        
        .. attribute:: cpeextdefaultallocation
        
        	This object indicates the default inline power allocation per port. This is a global configuration parameter that applies to all inline power capable ports in the system.  The system must consider this object as well as the per port configuration object, cpeExtPsePortPwrMax, when determining how much power to allocate to a port. The system will use the lower of the two numbers
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliwatts
        
        .. attribute:: cpeextpolicingnotifenable
        
        	This object is used to enable/disable the the cpeExtPolicingNotif notification
        	**type**\: bool
        
        .. attribute:: cpeextpowerpriorityenable
        
        	This object is the global control of the power priority feature on the device. 'true' indicates that the power priority feature is globally enabled. 'false' indicates that the power priority feature is globally disabled
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
        _revision = '2018-01-19'

        def __init__(self):
            super(CISCOPOWERETHERNETEXTMIB.CpeExtMIBObjects, self).__init__()

            self.yang_name = "cpeExtMIBObjects"
            self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpeextdefaultallocation', (YLeaf(YType.uint32, 'cpeExtDefaultAllocation'), ['int'])),
                ('cpeextpolicingnotifenable', (YLeaf(YType.boolean, 'cpeExtPolicingNotifEnable'), ['bool'])),
                ('cpeextpowerpriorityenable', (YLeaf(YType.boolean, 'cpeExtPowerPriorityEnable'), ['bool'])),
            ])
            self.cpeextdefaultallocation = None
            self.cpeextpolicingnotifenable = None
            self.cpeextpowerpriorityenable = None
            self._segment_path = lambda: "cpeExtMIBObjects"
            self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtMIBObjects, ['cpeextdefaultallocation', 'cpeextpolicingnotifenable', 'cpeextpowerpriorityenable'], name, value)


    class CpeExtPdStatistics(Entity):
        """
        
        
        .. attribute:: cpeextpdstatstotaldevices
        
        	This object indicates the total number of the powered devices with any power classifications in the system.  Classification is a way to tag different terminals on the Power over LAN network according to their power consumption. Devices such as IP telephones, WLAN access points and others, will be classified according to their power requirements
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
        _revision = '2018-01-19'

        def __init__(self):
            super(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatistics, self).__init__()

            self.yang_name = "cpeExtPdStatistics"
            self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpeextpdstatstotaldevices', (YLeaf(YType.uint32, 'cpeExtPdStatsTotalDevices'), ['int'])),
            ])
            self.cpeextpdstatstotaldevices = None
            self._segment_path = lambda: "cpeExtPdStatistics"
            self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatistics, ['cpeextpdstatstotaldevices'], name, value)


    class CpeExtMainPseTable(Entity):
        """
        This table contains the additional information for the
        main PSE group in pethMainPseTable.
        
        .. attribute:: cpeextmainpseentry
        
        	A cpeExtMainPseEntry contains information about a particular pethMainPseGroupIndex. An entry is created by the agent when a main PSE group is added to the pethMainPseTable. An entry is deleted by the agent when a main PSE group is removed from the pethMainPseTable
        	**type**\: list of  		 :py:class:`CpeExtMainPseEntry <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable.CpeExtMainPseEntry>`
        
        

        """

        _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
        _revision = '2018-01-19'

        def __init__(self):
            super(CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable, self).__init__()

            self.yang_name = "cpeExtMainPseTable"
            self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpeExtMainPseEntry", ("cpeextmainpseentry", CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable.CpeExtMainPseEntry))])
            self._leafs = OrderedDict()

            self.cpeextmainpseentry = YList(self)
            self._segment_path = lambda: "cpeExtMainPseTable"
            self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable, [], name, value)


        class CpeExtMainPseEntry(Entity):
            """
            A cpeExtMainPseEntry contains information about
            a particular pethMainPseGroupIndex. An entry is
            created by the agent when a main PSE group is added
            to the pethMainPseTable. An entry is deleted by the
            agent when a main PSE group is removed from the
            pethMainPseTable.
            
            .. attribute:: pethmainpsegroupindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`pethmainpsegroupindex <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry>`
            
            .. attribute:: cpeextmainpseentphyindex
            
            	The entPhysicalIndex value that uniquely identifies the main PSE group. If the main PSE group does not have a corresponding physical entry in entPhysicalTable or if the entPhysicalTable is not supported by the management system, then this object has the value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpeextmainpsedescr
            
            	A textual string containing information about the Power Source Equipment (PSE) group
            	**type**\: str
            
            .. attribute:: cpeextmainpsepwrmonitorcapable
            
            	This object indicates if the given group is capable of monitoring the power consumption of the interfaces that belong to the group. The value 'true' means that the group is capable. The value 'false' means that the group in not capable
            	**type**\: bool
            
            .. attribute:: cpeextmainpseusedpower
            
            	This object indicates used power expressed in miliwatts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: miliwatts
            
            .. attribute:: cpeextmainpseremainingpower
            
            	This object indicates remaining power expressed in miliwatts, this parameter is calculated as pethMainPsePower minus cpeExtMainPseUsedPower
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: miliwatts
            
            

            """

            _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
            _revision = '2018-01-19'

            def __init__(self):
                super(CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable.CpeExtMainPseEntry, self).__init__()

                self.yang_name = "cpeExtMainPseEntry"
                self.yang_parent_name = "cpeExtMainPseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pethmainpsegroupindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pethmainpsegroupindex', (YLeaf(YType.str, 'pethMainPseGroupIndex'), ['int'])),
                    ('cpeextmainpseentphyindex', (YLeaf(YType.int32, 'cpeExtMainPseEntPhyIndex'), ['int'])),
                    ('cpeextmainpsedescr', (YLeaf(YType.str, 'cpeExtMainPseDescr'), ['str'])),
                    ('cpeextmainpsepwrmonitorcapable', (YLeaf(YType.boolean, 'cpeExtMainPsePwrMonitorCapable'), ['bool'])),
                    ('cpeextmainpseusedpower', (YLeaf(YType.uint32, 'cpeExtMainPseUsedPower'), ['int'])),
                    ('cpeextmainpseremainingpower', (YLeaf(YType.uint32, 'cpeExtMainPseRemainingPower'), ['int'])),
                ])
                self.pethmainpsegroupindex = None
                self.cpeextmainpseentphyindex = None
                self.cpeextmainpsedescr = None
                self.cpeextmainpsepwrmonitorcapable = None
                self.cpeextmainpseusedpower = None
                self.cpeextmainpseremainingpower = None
                self._segment_path = lambda: "cpeExtMainPseEntry" + "[pethMainPseGroupIndex='" + str(self.pethmainpsegroupindex) + "']"
                self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/cpeExtMainPseTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtMainPseTable.CpeExtMainPseEntry, ['pethmainpsegroupindex', 'cpeextmainpseentphyindex', 'cpeextmainpsedescr', 'cpeextmainpsepwrmonitorcapable', 'cpeextmainpseusedpower', 'cpeextmainpseremainingpower'], name, value)


    class CpeExtPdStatsTable(Entity):
        """
        This table contains the statistics information
        of the powered devices fallen into different power
        classifications in the system.
        
        .. attribute:: cpeextpdstatsentry
        
        	A cpeExtPdStatsEntry contains the statistics information about a particular power classification defined in cpeExtPdStatsIndex
        	**type**\: list of  		 :py:class:`CpeExtPdStatsEntry <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable.CpeExtPdStatsEntry>`
        
        

        """

        _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
        _revision = '2018-01-19'

        def __init__(self):
            super(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable, self).__init__()

            self.yang_name = "cpeExtPdStatsTable"
            self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpeExtPdStatsEntry", ("cpeextpdstatsentry", CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable.CpeExtPdStatsEntry))])
            self._leafs = OrderedDict()

            self.cpeextpdstatsentry = YList(self)
            self._segment_path = lambda: "cpeExtPdStatsTable"
            self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable, [], name, value)


        class CpeExtPdStatsEntry(Entity):
            """
            A cpeExtPdStatsEntry contains the statistics
            information about a particular power classification
            defined in cpeExtPdStatsIndex.
            
            .. attribute:: cpeextpdstatsclass  (key)
            
            	The power classification as the index for the statistics information for powered devices.  A value of 'cisco' indicates that the powered devices are CISCO proprietary and their power  classification does not fall into any class in IEEE specifications.  A value of 'class0' indicates that the power  classification of the powered devices falls into class 0 in IEEE specifications.  A value of 'class1' indicates that the power classification of the powered devices falls into class 1 in IEEE specifications.  A value of 'class2' indicates that the power classification of the powered devices falls into class 2 in IEEE specifications.  A value of 'class3' indicates that the power classification of the powered devices falls into class 3 in IEEE specifications.  A value of 'class4' indicates that the power classification of the powered devices falls into class 4 in IEEE specifications
            	**type**\:  :py:class:`CpeExtPdStatsClass <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable.CpeExtPdStatsEntry.CpeExtPdStatsClass>`
            
            .. attribute:: cpeextpdstatsdevicecount
            
            	This object indicates the count of the powered devices whose power classification falls into  a specific value of cpeExtPdStatsIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
            _revision = '2018-01-19'

            def __init__(self):
                super(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable.CpeExtPdStatsEntry, self).__init__()

                self.yang_name = "cpeExtPdStatsEntry"
                self.yang_parent_name = "cpeExtPdStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpeextpdstatsclass']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpeextpdstatsclass', (YLeaf(YType.enumeration, 'cpeExtPdStatsClass'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CISCOPOWERETHERNETEXTMIB', 'CpeExtPdStatsTable.CpeExtPdStatsEntry.CpeExtPdStatsClass')])),
                    ('cpeextpdstatsdevicecount', (YLeaf(YType.uint32, 'cpeExtPdStatsDeviceCount'), ['int'])),
                ])
                self.cpeextpdstatsclass = None
                self.cpeextpdstatsdevicecount = None
                self._segment_path = lambda: "cpeExtPdStatsEntry" + "[cpeExtPdStatsClass='" + str(self.cpeextpdstatsclass) + "']"
                self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/cpeExtPdStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtPdStatsTable.CpeExtPdStatsEntry, ['cpeextpdstatsclass', 'cpeextpdstatsdevicecount'], name, value)

            class CpeExtPdStatsClass(Enum):
                """
                CpeExtPdStatsClass (Enum Class)

                The power classification as the index for the

                statistics information for powered devices.

                A value of 'cisco' indicates that the powered

                devices are CISCO proprietary and their power 

                classification does not fall into any class

                in IEEE specifications.

                A value of 'class0' indicates that the power 

                classification of the powered devices falls into

                class 0 in IEEE specifications.

                A value of 'class1' indicates that the power

                classification of the powered devices falls into

                class 1 in IEEE specifications.

                A value of 'class2' indicates that the power

                classification of the powered devices falls into

                class 2 in IEEE specifications.

                A value of 'class3' indicates that the power

                classification of the powered devices falls into

                class 3 in IEEE specifications.

                A value of 'class4' indicates that the power

                classification of the powered devices falls into

                class 4 in IEEE specifications.

                .. data:: cisco = 1

                .. data:: class0 = 2

                .. data:: class1 = 3

                .. data:: class2 = 4

                .. data:: class3 = 5

                .. data:: class4 = 6

                """

                cisco = Enum.YLeaf(1, "cisco")

                class0 = Enum.YLeaf(2, "class0")

                class1 = Enum.YLeaf(3, "class1")

                class2 = Enum.YLeaf(4, "class2")

                class3 = Enum.YLeaf(5, "class3")

                class4 = Enum.YLeaf(6, "class4")



    class CpeExtPsePortLldpTable(Entity):
        """
        A table provides the Link Layer Discovery Protocol (LLDP)
        based Data Link Layer (DLL) power classification
        characteristics of PSE ports and PDs attached to them.
        
        .. attribute:: cpeextpseportlldpentry
        
        	A cpeExtPsePortLldpEntry entry contains the LLDP based 802.3at DLL power classification characteristics for a particular PSE and the PD attached to it.   A PSE has its entry here when all of the following conditions are satisfied\: \- The LLDP power classification is globally enabled. \- It has a PD attached. \- LLDP is the operational power negotiation protocol between   the PSE and the PD attached
        	**type**\: list of  		 :py:class:`CpeExtPsePortLldpEntry <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry>`
        
        

        """

        _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
        _revision = '2018-01-19'

        def __init__(self):
            super(CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable, self).__init__()

            self.yang_name = "cpeExtPsePortLldpTable"
            self.yang_parent_name = "CISCO-POWER-ETHERNET-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpeExtPsePortLldpEntry", ("cpeextpseportlldpentry", CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry))])
            self._leafs = OrderedDict()

            self.cpeextpseportlldpentry = YList(self)
            self._segment_path = lambda: "cpeExtPsePortLldpTable"
            self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable, [], name, value)


        class CpeExtPsePortLldpEntry(Entity):
            """
            A cpeExtPsePortLldpEntry entry contains the LLDP
            based 802.3at DLL power classification characteristics for
            a particular PSE and the PD attached to it. 
            
            A PSE has its entry here when all of the following conditions
            are satisfied\:
            \- The LLDP power classification is globally enabled.
            \- It has a PD attached.
            \- LLDP is the operational power negotiation protocol between
              the PSE and the PD attached.
            
            .. attribute:: pethpseportgroupindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`pethpseportgroupindex <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry>`
            
            .. attribute:: pethpseportindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`pethpseportindex <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry>`
            
            .. attribute:: cpeextpseportlldppwrtype
            
            	The DTE Power via MDI type of the local system (PSE)
            	**type**\:  :py:class:`CpeExtLldpPwrType <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrType>`
            
            .. attribute:: cpeextpseportlldppdpwrtype
            
            	The DTE Power via MDI type of the remote system (PD)
            	**type**\:  :py:class:`CpeExtLldpPwrType <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrType>`
            
            .. attribute:: cpeextpseportlldppwrsrc
            
            	The power source of the local system (PSE)
            	**type**\:  :py:class:`CpeExtLldpPwrSrc <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrSrc>`
            
            .. attribute:: cpeextpseportlldppdpwrsrc
            
            	The power source of the remote system (PD)
            	**type**\:  :py:class:`CpeExtLldpPwrSrc <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrSrc>`
            
            .. attribute:: cpeextpseportlldppwrpriority
            
            	The power priority of the local system (PSE)
            	**type**\:  :py:class:`CpeExtPwrPriority <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtPwrPriority>`
            
            .. attribute:: cpeextpseportlldppdpwrpriority
            
            	The power priority of the remote system (PD)
            	**type**\:  :py:class:`CpeExtPwrPriority <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtPwrPriority>`
            
            .. attribute:: cpeextpseportlldppwrreq
            
            	The requested PD power value that the local system (PSE) mirrors back to the remote system (PD)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportlldppdpwrreq
            
            	The PD requested power value received from the remote system (PD)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportlldppwralloc
            
            	The PSE allocated power value for the remote system (PD)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportlldppdpwralloc
            
            	The PSE allocated power value received from the remote system (PD)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportlldppwrclass
            
            	The PSE power classification sent to the remote PD via MDI TLV in LLDP Protocol
            	**type**\:  :py:class:`CpeExtLldpPwrClassOrZero <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrClassOrZero>`
            
            .. attribute:: cpeextpseportlldppdpwrclass
            
            	This power classification received from the remote system (PD)
            	**type**\:  :py:class:`CpeExtLldpPwrClassOrZero <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CpeExtLldpPwrClassOrZero>`
            
            .. attribute:: cpeextpseportlldppdpwrsupport
            
            	This object indicates the power support mode received from the remote PD via MDI TLV in LLDP protocol.  'portClass'          \- This bit is set if the port is                        operating as PSE.  Otherwise, it is                        operating as PD.  'pseMdiPwrSupport'   \- This bit is set if power is supported in                        MDI TLV.  'pseMdiPwrState'     \- This bit is set if power is enabled.  'psePairCtrlAbility' \- This bit is set if pair selection can                        be controlled
            	**type**\:  :py:class:`CpeExtPsePortLldpPdPwrSupport <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry.CpeExtPsePortLldpPdPwrSupport>`
            
            .. attribute:: cpeextpseportlldppdpwrpairsorzero
            
            	This object indicates the pinout pairs in use received from the remote PD via MDI TLV in LLDP Protocol.  'unknown' \- information is not available  'signal'  \- the signal pairs are in use.  'spare'   \- the spare pairs are in use
            	**type**\:  :py:class:`CpeExtPsePortLldpPdPwrPairsOrZero <ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB.CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry.CpeExtPsePortLldpPdPwrPairsOrZero>`
            
            

            """

            _prefix = 'CISCO-POWER-ETHERNET-EXT-MIB'
            _revision = '2018-01-19'

            def __init__(self):
                super(CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry, self).__init__()

                self.yang_name = "cpeExtPsePortLldpEntry"
                self.yang_parent_name = "cpeExtPsePortLldpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pethpseportgroupindex','pethpseportindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pethpseportgroupindex', (YLeaf(YType.str, 'pethPsePortGroupIndex'), ['int'])),
                    ('pethpseportindex', (YLeaf(YType.str, 'pethPsePortIndex'), ['int'])),
                    ('cpeextpseportlldppwrtype', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPwrType'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrType', '')])),
                    ('cpeextpseportlldppdpwrtype', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPdPwrType'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrType', '')])),
                    ('cpeextpseportlldppwrsrc', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPwrSrc'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrSrc', '')])),
                    ('cpeextpseportlldppdpwrsrc', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPdPwrSrc'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrSrc', '')])),
                    ('cpeextpseportlldppwrpriority', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPwrPriority'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtPwrPriority', '')])),
                    ('cpeextpseportlldppdpwrpriority', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPdPwrPriority'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtPwrPriority', '')])),
                    ('cpeextpseportlldppwrreq', (YLeaf(YType.uint32, 'cpeExtPsePortLldpPwrReq'), ['int'])),
                    ('cpeextpseportlldppdpwrreq', (YLeaf(YType.uint32, 'cpeExtPsePortLldpPdPwrReq'), ['int'])),
                    ('cpeextpseportlldppwralloc', (YLeaf(YType.uint32, 'cpeExtPsePortLldpPwrAlloc'), ['int'])),
                    ('cpeextpseportlldppdpwralloc', (YLeaf(YType.uint32, 'cpeExtPsePortLldpPdPwrAlloc'), ['int'])),
                    ('cpeextpseportlldppwrclass', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPwrClass'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrClassOrZero', '')])),
                    ('cpeextpseportlldppdpwrclass', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPdPwrClass'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CpeExtLldpPwrClassOrZero', '')])),
                    ('cpeextpseportlldppdpwrsupport', (YLeaf(YType.bits, 'cpeExtPsePortLldpPdPwrSupport'), ['Bits'])),
                    ('cpeextpseportlldppdpwrpairsorzero', (YLeaf(YType.enumeration, 'cpeExtPsePortLldpPdPwrPairsOrZero'), [('ydk.models.cisco_ios_xe.CISCO_POWER_ETHERNET_EXT_MIB', 'CISCOPOWERETHERNETEXTMIB', 'CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry.CpeExtPsePortLldpPdPwrPairsOrZero')])),
                ])
                self.pethpseportgroupindex = None
                self.pethpseportindex = None
                self.cpeextpseportlldppwrtype = None
                self.cpeextpseportlldppdpwrtype = None
                self.cpeextpseportlldppwrsrc = None
                self.cpeextpseportlldppdpwrsrc = None
                self.cpeextpseportlldppwrpriority = None
                self.cpeextpseportlldppdpwrpriority = None
                self.cpeextpseportlldppwrreq = None
                self.cpeextpseportlldppdpwrreq = None
                self.cpeextpseportlldppwralloc = None
                self.cpeextpseportlldppdpwralloc = None
                self.cpeextpseportlldppwrclass = None
                self.cpeextpseportlldppdpwrclass = None
                self.cpeextpseportlldppdpwrsupport = Bits()
                self.cpeextpseportlldppdpwrpairsorzero = None
                self._segment_path = lambda: "cpeExtPsePortLldpEntry" + "[pethPsePortGroupIndex='" + str(self.pethpseportgroupindex) + "']" + "[pethPsePortIndex='" + str(self.pethpseportindex) + "']"
                self._absolute_path = lambda: "CISCO-POWER-ETHERNET-EXT-MIB:CISCO-POWER-ETHERNET-EXT-MIB/cpeExtPsePortLldpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPOWERETHERNETEXTMIB.CpeExtPsePortLldpTable.CpeExtPsePortLldpEntry, ['pethpseportgroupindex', 'pethpseportindex', 'cpeextpseportlldppwrtype', 'cpeextpseportlldppdpwrtype', 'cpeextpseportlldppwrsrc', 'cpeextpseportlldppdpwrsrc', 'cpeextpseportlldppwrpriority', 'cpeextpseportlldppdpwrpriority', 'cpeextpseportlldppwrreq', 'cpeextpseportlldppdpwrreq', 'cpeextpseportlldppwralloc', 'cpeextpseportlldppdpwralloc', 'cpeextpseportlldppwrclass', 'cpeextpseportlldppdpwrclass', 'cpeextpseportlldppdpwrsupport', 'cpeextpseportlldppdpwrpairsorzero'], name, value)

            class CpeExtPsePortLldpPdPwrPairsOrZero(Enum):
                """
                CpeExtPsePortLldpPdPwrPairsOrZero (Enum Class)

                This object indicates the pinout pairs in use received

                from the remote PD via MDI TLV in LLDP Protocol.

                'unknown' \- information is not available

                'signal'  \- the signal pairs are in use.

                'spare'   \- the spare pairs are in use.

                .. data:: unknown = 0

                .. data:: signal = 1

                .. data:: spare = 2

                """

                unknown = Enum.YLeaf(0, "unknown")

                signal = Enum.YLeaf(1, "signal")

                spare = Enum.YLeaf(2, "spare")


    def clone_ptr(self):
        self._top_entity = CISCOPOWERETHERNETEXTMIB()
        return self._top_entity

