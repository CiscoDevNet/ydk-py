""" CISCO_QOS_PIB_MIB 

The Cisco QOS Policy PIB for provisioning QOS policy.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class QosInterfaceQueueType(Enum):
    """
    QosInterfaceQueueType (Enum Class)

    An enumerated type for all the known interface types.  The

    interface types are currently limited to a predefined

    combination of queues and thresholds such that the product of

    queues and thresholds does not exceed 64 (i.e., the total

    number of DSCPs.

    .. data:: oneQ1t = 1

    .. data:: oneQ2t = 2

    .. data:: oneQ4t = 3

    .. data:: oneQ8t = 4

    .. data:: twoQ1t = 5

    .. data:: twoQ2t = 6

    .. data:: twoQ4t = 7

    .. data:: twoQ8t = 8

    .. data:: threeQ1t = 9

    .. data:: threeQ2t = 10

    .. data:: threeQ4t = 11

    .. data:: threeQ8t = 12

    .. data:: fourQ1t = 13

    .. data:: fourQ2t = 14

    .. data:: fourQ4t = 15

    .. data:: fourQ8t = 16

    .. data:: eightQ1t = 17

    .. data:: eightQ2t = 18

    .. data:: eightQ4t = 19

    .. data:: eightQ8t = 20

    .. data:: sixteenQ1t = 21

    .. data:: sixteenQ2t = 22

    .. data:: sixteenQ4t = 23

    .. data:: sixtyfourQ1t = 24

    .. data:: sixtyfourQ2t = 25

    .. data:: sixtyfourQ4t = 26

    .. data:: oneP1Q0t = 27

    .. data:: oneP1Q4t = 28

    .. data:: oneP1Q8t = 29

    .. data:: oneP2Q1t = 30

    .. data:: oneP2Q2t = 31

    .. data:: oneP3Q1t = 32

    .. data:: oneP7Q8t = 33

    .. data:: oneP3Q8t = 34

    .. data:: sixteenQ8t = 35

    .. data:: oneP15Q8t = 36

    .. data:: oneP15Q1t = 37

    .. data:: oneP7Q1t = 38

    .. data:: oneP31Q1t = 39

    .. data:: thirtytwoQ1t = 40

    .. data:: thirtytwoQ8t = 41

    .. data:: oneP31Q8t = 42

    .. data:: oneP7Q4t = 43

    .. data:: oneP3Q4t = 44

    .. data:: oneP7Q2t = 45

    """

    oneQ1t = Enum.YLeaf(1, "oneQ1t")

    oneQ2t = Enum.YLeaf(2, "oneQ2t")

    oneQ4t = Enum.YLeaf(3, "oneQ4t")

    oneQ8t = Enum.YLeaf(4, "oneQ8t")

    twoQ1t = Enum.YLeaf(5, "twoQ1t")

    twoQ2t = Enum.YLeaf(6, "twoQ2t")

    twoQ4t = Enum.YLeaf(7, "twoQ4t")

    twoQ8t = Enum.YLeaf(8, "twoQ8t")

    threeQ1t = Enum.YLeaf(9, "threeQ1t")

    threeQ2t = Enum.YLeaf(10, "threeQ2t")

    threeQ4t = Enum.YLeaf(11, "threeQ4t")

    threeQ8t = Enum.YLeaf(12, "threeQ8t")

    fourQ1t = Enum.YLeaf(13, "fourQ1t")

    fourQ2t = Enum.YLeaf(14, "fourQ2t")

    fourQ4t = Enum.YLeaf(15, "fourQ4t")

    fourQ8t = Enum.YLeaf(16, "fourQ8t")

    eightQ1t = Enum.YLeaf(17, "eightQ1t")

    eightQ2t = Enum.YLeaf(18, "eightQ2t")

    eightQ4t = Enum.YLeaf(19, "eightQ4t")

    eightQ8t = Enum.YLeaf(20, "eightQ8t")

    sixteenQ1t = Enum.YLeaf(21, "sixteenQ1t")

    sixteenQ2t = Enum.YLeaf(22, "sixteenQ2t")

    sixteenQ4t = Enum.YLeaf(23, "sixteenQ4t")

    sixtyfourQ1t = Enum.YLeaf(24, "sixtyfourQ1t")

    sixtyfourQ2t = Enum.YLeaf(25, "sixtyfourQ2t")

    sixtyfourQ4t = Enum.YLeaf(26, "sixtyfourQ4t")

    oneP1Q0t = Enum.YLeaf(27, "oneP1Q0t")

    oneP1Q4t = Enum.YLeaf(28, "oneP1Q4t")

    oneP1Q8t = Enum.YLeaf(29, "oneP1Q8t")

    oneP2Q1t = Enum.YLeaf(30, "oneP2Q1t")

    oneP2Q2t = Enum.YLeaf(31, "oneP2Q2t")

    oneP3Q1t = Enum.YLeaf(32, "oneP3Q1t")

    oneP7Q8t = Enum.YLeaf(33, "oneP7Q8t")

    oneP3Q8t = Enum.YLeaf(34, "oneP3Q8t")

    sixteenQ8t = Enum.YLeaf(35, "sixteenQ8t")

    oneP15Q8t = Enum.YLeaf(36, "oneP15Q8t")

    oneP15Q1t = Enum.YLeaf(37, "oneP15Q1t")

    oneP7Q1t = Enum.YLeaf(38, "oneP7Q1t")

    oneP31Q1t = Enum.YLeaf(39, "oneP31Q1t")

    thirtytwoQ1t = Enum.YLeaf(40, "thirtytwoQ1t")

    thirtytwoQ8t = Enum.YLeaf(41, "thirtytwoQ8t")

    oneP31Q8t = Enum.YLeaf(42, "oneP31Q8t")

    oneP7Q4t = Enum.YLeaf(43, "oneP7Q4t")

    oneP3Q4t = Enum.YLeaf(44, "oneP3Q4t")

    oneP7Q2t = Enum.YLeaf(45, "oneP7Q2t")


class QueueRange(Enum):
    """
    QueueRange (Enum Class)

    An integer that is limited to the number of queues per

    interface supported by the PIB.  Limited to 64 which is the

    number of codepoints.

    .. data:: oneQ = 1

    .. data:: twoQ = 2

    .. data:: threeQ = 3

    .. data:: fourQ = 4

    .. data:: eightQ = 8

    .. data:: sixteenQ = 16

    .. data:: thirtyTwoQ = 32

    .. data:: sixtyFourQ = 64

    """

    oneQ = Enum.YLeaf(1, "oneQ")

    twoQ = Enum.YLeaf(2, "twoQ")

    threeQ = Enum.YLeaf(3, "threeQ")

    fourQ = Enum.YLeaf(4, "fourQ")

    eightQ = Enum.YLeaf(8, "eightQ")

    sixteenQ = Enum.YLeaf(16, "sixteenQ")

    thirtyTwoQ = Enum.YLeaf(32, "thirtyTwoQ")

    sixtyFourQ = Enum.YLeaf(64, "sixtyFourQ")


class ThresholdSetRange(Enum):
    """
    ThresholdSetRange (Enum Class)

    An integer that is limited to the number of threshold sets

    per queue supported by the PIB. A threshold set is a

    collection of parameters describing queue threshold.  The

    parameters of a threshold set depend on the drop mechanism the

    queue implements.  For example, the threshold set for

    tail\-drop  comprises a single parameter, the percentage of

    queue size at which dropping occurs.  The threshold set for

    WRED comprises two parameters; within the range of the two

    parameters packets are randomly dropped.

    .. data:: zeroT = 0

    .. data:: oneT = 1

    .. data:: twoT = 2

    .. data:: fourT = 4

    .. data:: eightT = 8

    """

    zeroT = Enum.YLeaf(0, "zeroT")

    oneT = Enum.YLeaf(1, "oneT")

    twoT = Enum.YLeaf(2, "twoT")

    fourT = Enum.YLeaf(4, "fourT")

    eightT = Enum.YLeaf(8, "eightT")



class CISCOQOSPIBMIB(Entity):
    """
    
    
    .. attribute:: qosdevicepibincarnationtable
    
    	This class contains a single policy instance that identifies the current incarnation of the PIB and the PDP that installed this incarnation.  The instance of this class is reported to the PDP at client connect time so that the PDP can (attempt to) ascertain the current state of the PIB
    	**type**\:  :py:class:`Qosdevicepibincarnationtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdevicepibincarnationtable>`
    
    .. attribute:: qosdeviceattributetable
    
    	The single instance of this class indicates specific attributes of the device.  These include configuration values such as the configured PDP addresses, the maximum message size, and specific device capabilities.  The latter include input port\-based and output port\-based classification and/or policing, support for flow based policing, aggregate based policing, traffic shaping capabilities, etc
    	**type**\:  :py:class:`Qosdeviceattributetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdeviceattributetable>`
    
    .. attribute:: qosinterfacetypetable
    
    	This class describes the interface types of the interfaces that exist on the device.  It includes the queue type, role combination and capabilities of interfaces.  The PEP does not report which specific interfaces have which characteristics
    	**type**\:  :py:class:`Qosinterfacetypetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosinterfacetypetable>`
    
    .. attribute:: qosdiffservmappingtable
    
    	Maps each DSCP to a marked\-down DSCP.  Also maps each DSCP to an IP precedence and QosLayer2Cos.  When configured for the first time, all 64 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:  :py:class:`Qosdiffservmappingtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdiffservmappingtable>`
    
    .. attribute:: qoscostodscptable
    
    	Maps each of eight CoS values to a DSCP.  When configured for the first time, all 8 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:  :py:class:`Qoscostodscptable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qoscostodscptable>`
    
    .. attribute:: qosunmatchedpolicytable
    
    	A policy class that specifies what QoS to apply to a packet that does not match any other policy configured for this role combination for a particular direction of traffic
    	**type**\:  :py:class:`Qosunmatchedpolicytable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosunmatchedpolicytable>`
    
    .. attribute:: qospolicertable
    
    	A class specifying policing parameters for both microflows and aggregate flows.  This table is designed for policing according to a token bucket scheme where an average rate and burst size is specified
    	**type**\:  :py:class:`Qospolicertable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qospolicertable>`
    
    .. attribute:: qosaggregatetable
    
    	Instances of this class identify aggregate flows and the policer to apply to each
    	**type**\:  :py:class:`Qosaggregatetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosaggregatetable>`
    
    .. attribute:: qosmacclassificationtable
    
    	A class of MAC/Vlan tuples and their associated CoS values
    	**type**\:  :py:class:`Qosmacclassificationtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosmacclassificationtable>`
    
    .. attribute:: qosipacetable
    
    	ACE definitions
    	**type**\:  :py:class:`Qosipacetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipacetable>`
    
    .. attribute:: qosipacldefinitiontable
    
    	A class that defines a set of ACLs each being an ordered list of ACEs
    	**type**\:  :py:class:`Qosipacldefinitiontable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipacldefinitiontable>`
    
    .. attribute:: qosipaclactiontable
    
    	A class that applies a set of ACLs to interfaces specifying, for each interface the order of the ACL with respect to other ACLs applied to the same interface and, for each ACL the action to take for a packet that matches a permit ACE in that ACL.  Interfaces are specified abstractly in terms of interface role combinations
    	**type**\:  :py:class:`Qosipaclactiontable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipaclactiontable>`
    
    .. attribute:: qosifschedulingpreferencestable
    
    	This class specifies the scheduling preference an interface chooses if it supports multiple scheduling types.  Higher values are preferred over lower values
    	**type**\:  :py:class:`Qosifschedulingpreferencestable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifschedulingpreferencestable>`
    
    .. attribute:: qosifdroppreferencetable
    
    	This class specifies the preference of the drop mechanism an interface chooses if it supports multiple drop mechanisms. Higher values are preferred over lower values
    	**type**\:  :py:class:`Qosifdroppreferencetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifdroppreferencetable>`
    
    .. attribute:: qosifdscpassignmenttable
    
    	The assignment of each DSCP to a queue and threshold for each interface queue type
    	**type**\:  :py:class:`Qosifdscpassignmenttable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifdscpassignmenttable>`
    
    .. attribute:: qosifredtable
    
    	A class of lower and upper values for each threshold set in a queue supporting WRED.  If the size of the queue for a given threshold is below the lower value then packets assigned to that threshold are always accepted into the queue.  If the size of the queue is above upper value then packets are always dropped.  If the size of the queue is between the lower and the upper then packets are randomly dropped
    	**type**\:  :py:class:`Qosifredtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifredtable>`
    
    .. attribute:: qosiftaildroptable
    
    	A class for threshold sets in a queue supporting tail drop. If the size of the queue for a given threshold set is at or below the specified value then packets assigned to that threshold set are always accepted into the queue.  If the size of the queue is above the specified value then packets are always dropped
    	**type**\:  :py:class:`Qosiftaildroptable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosiftaildroptable>`
    
    .. attribute:: qosifweightstable
    
    	A class of scheduling weights for each queue of an interface that supports weighted round robin scheduling or a mix of priority queueing and weighted round robin.  For a queue with N priority queues, the N highest queue numbers are the priority queues with the highest queue number having the highest priority.  WRR is applied to the non\-priority queues
    	**type**\:  :py:class:`Qosifweightstable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifweightstable>`
    
    

    """

    _prefix = 'CISCO-QOS-PIB-MIB'
    _revision = '2007-08-29'

    def __init__(self):
        super(CISCOQOSPIBMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-QOS-PIB-MIB"
        self.yang_parent_name = "CISCO-QOS-PIB-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("qosDevicePibIncarnationTable", ("qosdevicepibincarnationtable", CISCOQOSPIBMIB.Qosdevicepibincarnationtable)), ("qosDeviceAttributeTable", ("qosdeviceattributetable", CISCOQOSPIBMIB.Qosdeviceattributetable)), ("qosInterfaceTypeTable", ("qosinterfacetypetable", CISCOQOSPIBMIB.Qosinterfacetypetable)), ("qosDiffServMappingTable", ("qosdiffservmappingtable", CISCOQOSPIBMIB.Qosdiffservmappingtable)), ("qosCosToDscpTable", ("qoscostodscptable", CISCOQOSPIBMIB.Qoscostodscptable)), ("qosUnmatchedPolicyTable", ("qosunmatchedpolicytable", CISCOQOSPIBMIB.Qosunmatchedpolicytable)), ("qosPolicerTable", ("qospolicertable", CISCOQOSPIBMIB.Qospolicertable)), ("qosAggregateTable", ("qosaggregatetable", CISCOQOSPIBMIB.Qosaggregatetable)), ("qosMacClassificationTable", ("qosmacclassificationtable", CISCOQOSPIBMIB.Qosmacclassificationtable)), ("qosIpAceTable", ("qosipacetable", CISCOQOSPIBMIB.Qosipacetable)), ("qosIpAclDefinitionTable", ("qosipacldefinitiontable", CISCOQOSPIBMIB.Qosipacldefinitiontable)), ("qosIpAclActionTable", ("qosipaclactiontable", CISCOQOSPIBMIB.Qosipaclactiontable)), ("qosIfSchedulingPreferencesTable", ("qosifschedulingpreferencestable", CISCOQOSPIBMIB.Qosifschedulingpreferencestable)), ("qosIfDropPreferenceTable", ("qosifdroppreferencetable", CISCOQOSPIBMIB.Qosifdroppreferencetable)), ("qosIfDscpAssignmentTable", ("qosifdscpassignmenttable", CISCOQOSPIBMIB.Qosifdscpassignmenttable)), ("qosIfRedTable", ("qosifredtable", CISCOQOSPIBMIB.Qosifredtable)), ("qosIfTailDropTable", ("qosiftaildroptable", CISCOQOSPIBMIB.Qosiftaildroptable)), ("qosIfWeightsTable", ("qosifweightstable", CISCOQOSPIBMIB.Qosifweightstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.qosdevicepibincarnationtable = CISCOQOSPIBMIB.Qosdevicepibincarnationtable()
        self.qosdevicepibincarnationtable.parent = self
        self._children_name_map["qosdevicepibincarnationtable"] = "qosDevicePibIncarnationTable"
        self._children_yang_names.add("qosDevicePibIncarnationTable")

        self.qosdeviceattributetable = CISCOQOSPIBMIB.Qosdeviceattributetable()
        self.qosdeviceattributetable.parent = self
        self._children_name_map["qosdeviceattributetable"] = "qosDeviceAttributeTable"
        self._children_yang_names.add("qosDeviceAttributeTable")

        self.qosinterfacetypetable = CISCOQOSPIBMIB.Qosinterfacetypetable()
        self.qosinterfacetypetable.parent = self
        self._children_name_map["qosinterfacetypetable"] = "qosInterfaceTypeTable"
        self._children_yang_names.add("qosInterfaceTypeTable")

        self.qosdiffservmappingtable = CISCOQOSPIBMIB.Qosdiffservmappingtable()
        self.qosdiffservmappingtable.parent = self
        self._children_name_map["qosdiffservmappingtable"] = "qosDiffServMappingTable"
        self._children_yang_names.add("qosDiffServMappingTable")

        self.qoscostodscptable = CISCOQOSPIBMIB.Qoscostodscptable()
        self.qoscostodscptable.parent = self
        self._children_name_map["qoscostodscptable"] = "qosCosToDscpTable"
        self._children_yang_names.add("qosCosToDscpTable")

        self.qosunmatchedpolicytable = CISCOQOSPIBMIB.Qosunmatchedpolicytable()
        self.qosunmatchedpolicytable.parent = self
        self._children_name_map["qosunmatchedpolicytable"] = "qosUnmatchedPolicyTable"
        self._children_yang_names.add("qosUnmatchedPolicyTable")

        self.qospolicertable = CISCOQOSPIBMIB.Qospolicertable()
        self.qospolicertable.parent = self
        self._children_name_map["qospolicertable"] = "qosPolicerTable"
        self._children_yang_names.add("qosPolicerTable")

        self.qosaggregatetable = CISCOQOSPIBMIB.Qosaggregatetable()
        self.qosaggregatetable.parent = self
        self._children_name_map["qosaggregatetable"] = "qosAggregateTable"
        self._children_yang_names.add("qosAggregateTable")

        self.qosmacclassificationtable = CISCOQOSPIBMIB.Qosmacclassificationtable()
        self.qosmacclassificationtable.parent = self
        self._children_name_map["qosmacclassificationtable"] = "qosMacClassificationTable"
        self._children_yang_names.add("qosMacClassificationTable")

        self.qosipacetable = CISCOQOSPIBMIB.Qosipacetable()
        self.qosipacetable.parent = self
        self._children_name_map["qosipacetable"] = "qosIpAceTable"
        self._children_yang_names.add("qosIpAceTable")

        self.qosipacldefinitiontable = CISCOQOSPIBMIB.Qosipacldefinitiontable()
        self.qosipacldefinitiontable.parent = self
        self._children_name_map["qosipacldefinitiontable"] = "qosIpAclDefinitionTable"
        self._children_yang_names.add("qosIpAclDefinitionTable")

        self.qosipaclactiontable = CISCOQOSPIBMIB.Qosipaclactiontable()
        self.qosipaclactiontable.parent = self
        self._children_name_map["qosipaclactiontable"] = "qosIpAclActionTable"
        self._children_yang_names.add("qosIpAclActionTable")

        self.qosifschedulingpreferencestable = CISCOQOSPIBMIB.Qosifschedulingpreferencestable()
        self.qosifschedulingpreferencestable.parent = self
        self._children_name_map["qosifschedulingpreferencestable"] = "qosIfSchedulingPreferencesTable"
        self._children_yang_names.add("qosIfSchedulingPreferencesTable")

        self.qosifdroppreferencetable = CISCOQOSPIBMIB.Qosifdroppreferencetable()
        self.qosifdroppreferencetable.parent = self
        self._children_name_map["qosifdroppreferencetable"] = "qosIfDropPreferenceTable"
        self._children_yang_names.add("qosIfDropPreferenceTable")

        self.qosifdscpassignmenttable = CISCOQOSPIBMIB.Qosifdscpassignmenttable()
        self.qosifdscpassignmenttable.parent = self
        self._children_name_map["qosifdscpassignmenttable"] = "qosIfDscpAssignmentTable"
        self._children_yang_names.add("qosIfDscpAssignmentTable")

        self.qosifredtable = CISCOQOSPIBMIB.Qosifredtable()
        self.qosifredtable.parent = self
        self._children_name_map["qosifredtable"] = "qosIfRedTable"
        self._children_yang_names.add("qosIfRedTable")

        self.qosiftaildroptable = CISCOQOSPIBMIB.Qosiftaildroptable()
        self.qosiftaildroptable.parent = self
        self._children_name_map["qosiftaildroptable"] = "qosIfTailDropTable"
        self._children_yang_names.add("qosIfTailDropTable")

        self.qosifweightstable = CISCOQOSPIBMIB.Qosifweightstable()
        self.qosifweightstable.parent = self
        self._children_name_map["qosifweightstable"] = "qosIfWeightsTable"
        self._children_yang_names.add("qosIfWeightsTable")
        self._segment_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB"


    class Qosdevicepibincarnationtable(Entity):
        """
        This class contains a single policy instance that identifies
        the current incarnation of the PIB and the PDP that installed
        this incarnation.  The instance of this class is reported to
        the PDP at client connect time so that the PDP can (attempt
        to) ascertain the current state of the PIB.
        
        .. attribute:: qosdevicepibincarnationentry
        
        	The single policy instance of this class identifies the current incarnation of the PIB and the PDP that installed this incarnation
        	**type**\: list of  		 :py:class:`Qosdevicepibincarnationentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosdevicepibincarnationtable, self).__init__()

            self.yang_name = "qosDevicePibIncarnationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosDevicePibIncarnationEntry", ("qosdevicepibincarnationentry", CISCOQOSPIBMIB.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry))])
            self._leafs = OrderedDict()

            self.qosdevicepibincarnationentry = YList(self)
            self._segment_path = lambda: "qosDevicePibIncarnationTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosdevicepibincarnationtable, [], name, value)


        class Qosdevicepibincarnationentry(Entity):
            """
            The single policy instance of this class identifies the
            current incarnation of the PIB and the PDP that installed
            this incarnation.
            
            .. attribute:: qosdeviceincarnationid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicepdpname
            
            	The name of the PDP that installed the current incarnation of the PIB into the device.  By default it is the zero length string
            	**type**\: str
            
            .. attribute:: qosdevicepibincarnation
            
            	An octet string to identify the current incarnation.  It has meaning to the PDP that installed the PIB and perhaps its standby PDPs. By default the empty string
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: qosdevicepibttl
            
            	The number of seconds after a client close or TCP timeout for which the PEP continues to enforce the policy in the PIB. After this interval, the PIB is consired expired and the device no longer enforces the policy installed in the PIB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry, self).__init__()

                self.yang_name = "qosDevicePibIncarnationEntry"
                self.yang_parent_name = "qosDevicePibIncarnationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdeviceincarnationid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosdeviceincarnationid', YLeaf(YType.uint32, 'qosDeviceIncarnationId')),
                    ('qosdevicepdpname', YLeaf(YType.str, 'qosDevicePdpName')),
                    ('qosdevicepibincarnation', YLeaf(YType.str, 'qosDevicePibIncarnation')),
                    ('qosdevicepibttl', YLeaf(YType.uint32, 'qosDevicePibTtl')),
                ])
                self.qosdeviceincarnationid = None
                self.qosdevicepdpname = None
                self.qosdevicepibincarnation = None
                self.qosdevicepibttl = None
                self._segment_path = lambda: "qosDevicePibIncarnationEntry" + "[qosDeviceIncarnationId='" + str(self.qosdeviceincarnationid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDevicePibIncarnationTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry, ['qosdeviceincarnationid', 'qosdevicepdpname', 'qosdevicepibincarnation', 'qosdevicepibttl'], name, value)


    class Qosdeviceattributetable(Entity):
        """
        The single instance of this class indicates specific
        attributes of the device.  These include configuration values
        such as the configured PDP addresses, the maximum message
        size, and specific device capabilities.  The latter include
        input port\-based and output port\-based classification and/or
        policing, support for flow based policing, aggregate based
        policing, traffic shaping capabilities, etc.
        
        .. attribute:: qosdeviceattributeentry
        
        	The single instance of this class indicates specific attributes of the device
        	**type**\: list of  		 :py:class:`Qosdeviceattributeentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdeviceattributetable.Qosdeviceattributeentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosdeviceattributetable, self).__init__()

            self.yang_name = "qosDeviceAttributeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosDeviceAttributeEntry", ("qosdeviceattributeentry", CISCOQOSPIBMIB.Qosdeviceattributetable.Qosdeviceattributeentry))])
            self._leafs = OrderedDict()

            self.qosdeviceattributeentry = YList(self)
            self._segment_path = lambda: "qosDeviceAttributeTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosdeviceattributetable, [], name, value)


        class Qosdeviceattributeentry(Entity):
            """
            The single instance of this class indicates specific
            attributes of the device.
            
            .. attribute:: qosdeviceattributeid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicepepdomain
            
            	The QoS domain that this device belongs to.  This is configured locally on the device (perhaps by some management protocol such as SNMP).  By default, it is the zero\-length string
            	**type**\: str
            
            .. attribute:: qosdeviceprimarypdp
            
            	The address of the PDP configured to be the primary PDP for the device
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosdevicesecondarypdp
            
            	The address of the PDP configured to be the secondary PDP for the device.  An address of zero indicates no secondary is configured
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosdevicemaxmessagesize
            
            	The maximum size message that this PEP is capable of receiving in bytes.  A value of zero means that the maximum message size is unspecified (but does not mean it is unlimited).  A message greater than this maximum results in a MessageTooBig error on a 'no commit' REP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicecapabilities
            
            	An enumeration of device capabilities.  Used by the PDP to select policies and configuration to push to the PEP
            	**type**\:  :py:class:`Qosdevicecapabilities <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdeviceattributetable.Qosdeviceattributeentry.Qosdevicecapabilities>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosdeviceattributetable.Qosdeviceattributeentry, self).__init__()

                self.yang_name = "qosDeviceAttributeEntry"
                self.yang_parent_name = "qosDeviceAttributeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdeviceattributeid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosdeviceattributeid', YLeaf(YType.uint32, 'qosDeviceAttributeId')),
                    ('qosdevicepepdomain', YLeaf(YType.str, 'qosDevicePepDomain')),
                    ('qosdeviceprimarypdp', YLeaf(YType.str, 'qosDevicePrimaryPdp')),
                    ('qosdevicesecondarypdp', YLeaf(YType.str, 'qosDeviceSecondaryPdp')),
                    ('qosdevicemaxmessagesize', YLeaf(YType.uint32, 'qosDeviceMaxMessageSize')),
                    ('qosdevicecapabilities', YLeaf(YType.bits, 'qosDeviceCapabilities')),
                ])
                self.qosdeviceattributeid = None
                self.qosdevicepepdomain = None
                self.qosdeviceprimarypdp = None
                self.qosdevicesecondarypdp = None
                self.qosdevicemaxmessagesize = None
                self.qosdevicecapabilities = Bits()
                self._segment_path = lambda: "qosDeviceAttributeEntry" + "[qosDeviceAttributeId='" + str(self.qosdeviceattributeid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDeviceAttributeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosdeviceattributetable.Qosdeviceattributeentry, ['qosdeviceattributeid', 'qosdevicepepdomain', 'qosdeviceprimarypdp', 'qosdevicesecondarypdp', 'qosdevicemaxmessagesize', 'qosdevicecapabilities'], name, value)


    class Qosinterfacetypetable(Entity):
        """
        This class describes the interface types of the interfaces
        that exist on the device.  It includes the queue type, role
        combination and capabilities of interfaces.  The PEP does not
        report which specific interfaces have which characteristics.
        
        .. attribute:: qosinterfacetypeentry
        
        	An instance of this class describes a role combination for an interface type of an interface that exists on the device
        	**type**\: list of  		 :py:class:`Qosinterfacetypeentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosinterfacetypetable.Qosinterfacetypeentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosinterfacetypetable, self).__init__()

            self.yang_name = "qosInterfaceTypeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosInterfaceTypeEntry", ("qosinterfacetypeentry", CISCOQOSPIBMIB.Qosinterfacetypetable.Qosinterfacetypeentry))])
            self._leafs = OrderedDict()

            self.qosinterfacetypeentry = YList(self)
            self._segment_path = lambda: "qosInterfaceTypeTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosinterfacetypetable, [], name, value)


        class Qosinterfacetypeentry(Entity):
            """
            An instance of this class describes a role combination for
            an interface type of an interface that exists on the device.
            
            .. attribute:: qosinterfacetypeid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosinterfacequeuetype
            
            	The interface type in terms of number of queues and thresholds
            	**type**\:  :py:class:`QosInterfaceQueueType <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosInterfaceQueueType>`
            
            .. attribute:: qosinterfacetyperoles
            
            	A combination of roles on at least one interface of type qosInterfaceType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosinterfacetypecapabilities
            
            	An enumeration of interface capabilities.  Used by the PDP to select policies and configuration to push to the PEP
            	**type**\:  :py:class:`QosInterfaceTypeCapabilities <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosInterfaceTypeCapabilities>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosinterfacetypetable.Qosinterfacetypeentry, self).__init__()

                self.yang_name = "qosInterfaceTypeEntry"
                self.yang_parent_name = "qosInterfaceTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosinterfacetypeid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosinterfacetypeid', YLeaf(YType.uint32, 'qosInterfaceTypeId')),
                    ('qosinterfacequeuetype', YLeaf(YType.enumeration, 'qosInterfaceQueueType')),
                    ('qosinterfacetyperoles', YLeaf(YType.str, 'qosInterfaceTypeRoles')),
                    ('qosinterfacetypecapabilities', YLeaf(YType.bits, 'qosInterfaceTypeCapabilities')),
                ])
                self.qosinterfacetypeid = None
                self.qosinterfacequeuetype = None
                self.qosinterfacetyperoles = None
                self.qosinterfacetypecapabilities = Bits()
                self._segment_path = lambda: "qosInterfaceTypeEntry" + "[qosInterfaceTypeId='" + str(self.qosinterfacetypeid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosInterfaceTypeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosinterfacetypetable.Qosinterfacetypeentry, ['qosinterfacetypeid', 'qosinterfacequeuetype', 'qosinterfacetyperoles', 'qosinterfacetypecapabilities'], name, value)


    class Qosdiffservmappingtable(Entity):
        """
        Maps each DSCP to a marked\-down DSCP.  Also maps each DSCP to
        an IP precedence and QosLayer2Cos.  When configured for the
        first time, all 64 entries of the table must be
        specified. Thereafter, instances may be modified (with a
        delete and install in a single decision) but not deleted
        unless all instances are deleted.
        
        .. attribute:: qosdiffservmappingentry
        
        	An instance of this class represents mappings from a DSCP
        	**type**\: list of  		 :py:class:`Qosdiffservmappingentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosdiffservmappingtable.Qosdiffservmappingentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosdiffservmappingtable, self).__init__()

            self.yang_name = "qosDiffServMappingTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosDiffServMappingEntry", ("qosdiffservmappingentry", CISCOQOSPIBMIB.Qosdiffservmappingtable.Qosdiffservmappingentry))])
            self._leafs = OrderedDict()

            self.qosdiffservmappingentry = YList(self)
            self._segment_path = lambda: "qosDiffServMappingTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosdiffservmappingtable, [], name, value)


        class Qosdiffservmappingentry(Entity):
            """
            An instance of this class represents mappings from a DSCP.
            
            .. attribute:: qosdscp  (key)
            
            	A DSCP for which this entry contains mappings
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosmarkeddscp
            
            	The DSCP to use instead of the qosDscp when the packet is out of profile and hence marked as such
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosl2cos
            
            	The L2 CoS value to use when mapping this DSCP to layer 2 CoS
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosdiffservmappingtable.Qosdiffservmappingentry, self).__init__()

                self.yang_name = "qosDiffServMappingEntry"
                self.yang_parent_name = "qosDiffServMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdscp']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosdscp', YLeaf(YType.int32, 'qosDscp')),
                    ('qosmarkeddscp', YLeaf(YType.int32, 'qosMarkedDscp')),
                    ('qosl2cos', YLeaf(YType.int32, 'qosL2Cos')),
                ])
                self.qosdscp = None
                self.qosmarkeddscp = None
                self.qosl2cos = None
                self._segment_path = lambda: "qosDiffServMappingEntry" + "[qosDscp='" + str(self.qosdscp) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDiffServMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosdiffservmappingtable.Qosdiffservmappingentry, ['qosdscp', 'qosmarkeddscp', 'qosl2cos'], name, value)


    class Qoscostodscptable(Entity):
        """
        Maps each of eight CoS values to a DSCP.  When configured for
        the first time, all 8 entries of the table must be
        specified. Thereafter, instances may be modified (with a
        delete and install in a single decision) but not deleted
        unless all instances are deleted.
        
        .. attribute:: qoscostodscpentry
        
        	An instance of this class maps a CoS value to a DSCP
        	**type**\: list of  		 :py:class:`Qoscostodscpentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qoscostodscptable.Qoscostodscpentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qoscostodscptable, self).__init__()

            self.yang_name = "qosCosToDscpTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosCosToDscpEntry", ("qoscostodscpentry", CISCOQOSPIBMIB.Qoscostodscptable.Qoscostodscpentry))])
            self._leafs = OrderedDict()

            self.qoscostodscpentry = YList(self)
            self._segment_path = lambda: "qosCosToDscpTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qoscostodscptable, [], name, value)


        class Qoscostodscpentry(Entity):
            """
            An instance of this class maps a CoS value to a DSCP.
            
            .. attribute:: qoscostodscpcos  (key)
            
            	The L2 CoS value that is being mapped
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: qoscostodscpdscp
            
            	The DSCP value to use when mapping the L2 CoS to a DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qoscostodscptable.Qoscostodscpentry, self).__init__()

                self.yang_name = "qosCosToDscpEntry"
                self.yang_parent_name = "qosCosToDscpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qoscostodscpcos']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qoscostodscpcos', YLeaf(YType.int32, 'qosCosToDscpCos')),
                    ('qoscostodscpdscp', YLeaf(YType.int32, 'qosCosToDscpDscp')),
                ])
                self.qoscostodscpcos = None
                self.qoscostodscpdscp = None
                self._segment_path = lambda: "qosCosToDscpEntry" + "[qosCosToDscpCos='" + str(self.qoscostodscpcos) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosCosToDscpTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qoscostodscptable.Qoscostodscpentry, ['qoscostodscpcos', 'qoscostodscpdscp'], name, value)


    class Qosunmatchedpolicytable(Entity):
        """
        A policy class that specifies what QoS to apply to a packet
        that does not match any other policy configured for this role
        combination for a particular direction of traffic.
        
        .. attribute:: qosunmatchedpolicyentry
        
        	An instance of this class specifies the unmatched policy for a particular role combination for incoming or outgoing traffic
        	**type**\: list of  		 :py:class:`Qosunmatchedpolicyentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosunmatchedpolicytable.Qosunmatchedpolicyentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosunmatchedpolicytable, self).__init__()

            self.yang_name = "qosUnmatchedPolicyTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosUnmatchedPolicyEntry", ("qosunmatchedpolicyentry", CISCOQOSPIBMIB.Qosunmatchedpolicytable.Qosunmatchedpolicyentry))])
            self._leafs = OrderedDict()

            self.qosunmatchedpolicyentry = YList(self)
            self._segment_path = lambda: "qosUnmatchedPolicyTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosunmatchedpolicytable, [], name, value)


        class Qosunmatchedpolicyentry(Entity):
            """
            An instance of this class specifies the unmatched policy
            for a particular role combination for incoming or outgoing
            traffic.
            
            .. attribute:: qosunmatchedpolicyid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosunmatchedpolicyrole
            
            	Role combination for which this instance applies
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosunmatchedpolicydirection
            
            	The direction of packet flow at the interface in question to which this instance applies
            	**type**\:  :py:class:`Qosunmatchedpolicydirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.Qosunmatchedpolicydirection>`
            
            .. attribute:: qosunmatchedpolicydscp
            
            	The DSCP to classify the unmatched packet with.  This must be specified even if qosUnmatchedPolicyDscpTrusted is true
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosunmatchedpolicydscptrusted
            
            	If this attribute is true, then the Dscp associated with the packet is trusted, i.e., it is assumed to have already been set.  In this case, the Dscp is not rewritten with qosUnmatchedPolicyDscp (qosUnmatchedPolicyDscp is ignored) unless this is a non\-IP packet and arrives untagged.  The packet is still policed as part of its micro flow and its aggregate flow.  When a trusted action is applied to an input interface, the Dscp (for an IP packet) or CoS (for a non\-IP packet) associated with the packet is the one contained in the packet. When a trusted action is applied to an output interface, the Dscp associated with the packet is the one that is the result of the input classification and policing
            	**type**\: bool
            
            .. attribute:: qosunmatchpolmicroflowpolicerid
            
            	An index identifying the instance of policer to apply to unmatched packets.  It must correspond to the integer index of an instance of class qosPolicerTable or be zero.  If zero, the microflow is not policed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosunmatchedpolicyaggregateid
            
            	An index identifying the aggregate that the packet belongs to.  It must correspond to the integer index of an instance of class qosAggregateTable or be zero.  If zero, the microflow does not belong to any aggregate and is not policed as part of any aggregate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosunmatchedpolicytable.Qosunmatchedpolicyentry, self).__init__()

                self.yang_name = "qosUnmatchedPolicyEntry"
                self.yang_parent_name = "qosUnmatchedPolicyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosunmatchedpolicyid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosunmatchedpolicyid', YLeaf(YType.uint32, 'qosUnmatchedPolicyId')),
                    ('qosunmatchedpolicyrole', YLeaf(YType.str, 'qosUnmatchedPolicyRole')),
                    ('qosunmatchedpolicydirection', YLeaf(YType.enumeration, 'qosUnmatchedPolicyDirection')),
                    ('qosunmatchedpolicydscp', YLeaf(YType.int32, 'qosUnmatchedPolicyDscp')),
                    ('qosunmatchedpolicydscptrusted', YLeaf(YType.boolean, 'qosUnmatchedPolicyDscpTrusted')),
                    ('qosunmatchpolmicroflowpolicerid', YLeaf(YType.uint32, 'qosUnmatchPolMicroFlowPolicerId')),
                    ('qosunmatchedpolicyaggregateid', YLeaf(YType.uint32, 'qosUnmatchedPolicyAggregateId')),
                ])
                self.qosunmatchedpolicyid = None
                self.qosunmatchedpolicyrole = None
                self.qosunmatchedpolicydirection = None
                self.qosunmatchedpolicydscp = None
                self.qosunmatchedpolicydscptrusted = None
                self.qosunmatchpolmicroflowpolicerid = None
                self.qosunmatchedpolicyaggregateid = None
                self._segment_path = lambda: "qosUnmatchedPolicyEntry" + "[qosUnmatchedPolicyId='" + str(self.qosunmatchedpolicyid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosUnmatchedPolicyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosunmatchedpolicytable.Qosunmatchedpolicyentry, ['qosunmatchedpolicyid', 'qosunmatchedpolicyrole', 'qosunmatchedpolicydirection', 'qosunmatchedpolicydscp', 'qosunmatchedpolicydscptrusted', 'qosunmatchpolmicroflowpolicerid', 'qosunmatchedpolicyaggregateid'], name, value)

            class Qosunmatchedpolicydirection(Enum):
                """
                Qosunmatchedpolicydirection (Enum Class)

                The direction of packet flow at the interface in question to

                which this instance applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")



    class Qospolicertable(Entity):
        """
        A class specifying policing parameters for both microflows
        and aggregate flows.  This table is designed for policing
        according to a token bucket scheme where an average rate and
        burst size is specified.
        
        .. attribute:: qospolicerentry
        
        	An instance of this class specifies a set of policing parameters
        	**type**\: list of  		 :py:class:`Qospolicerentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qospolicertable.Qospolicerentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qospolicertable, self).__init__()

            self.yang_name = "qosPolicerTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosPolicerEntry", ("qospolicerentry", CISCOQOSPIBMIB.Qospolicertable.Qospolicerentry))])
            self._leafs = OrderedDict()

            self.qospolicerentry = YList(self)
            self._segment_path = lambda: "qosPolicerTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qospolicertable, [], name, value)


        class Qospolicerentry(Entity):
            """
            An instance of this class specifies a set of policing
            parameters.
            
            .. attribute:: qospolicerid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospolicerrate
            
            	The token rate.  It is specified in units of bit/s. A rate of zero means that all packets will be out of profile.  If the qosPolicerAction is set to drop then this effectively denies any service to packets policed by this policer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospolicernormalburst
            
            	The normal size of a burst in terms of bits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospolicerexcessburst
            
            	The excess size of a burst in terms of bits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospoliceraction
            
            	An indication of how to handle out of profile packets.  When the shape action is chosen then traffic is shaped to the rate specified by qosPolicerRate
            	**type**\:  :py:class:`Qospoliceraction <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qospolicertable.Qospolicerentry.Qospoliceraction>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qospolicertable.Qospolicerentry, self).__init__()

                self.yang_name = "qosPolicerEntry"
                self.yang_parent_name = "qosPolicerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qospolicerid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qospolicerid', YLeaf(YType.uint32, 'qosPolicerId')),
                    ('qospolicerrate', YLeaf(YType.uint32, 'qosPolicerRate')),
                    ('qospolicernormalburst', YLeaf(YType.uint32, 'qosPolicerNormalBurst')),
                    ('qospolicerexcessburst', YLeaf(YType.uint32, 'qosPolicerExcessBurst')),
                    ('qospoliceraction', YLeaf(YType.enumeration, 'qosPolicerAction')),
                ])
                self.qospolicerid = None
                self.qospolicerrate = None
                self.qospolicernormalburst = None
                self.qospolicerexcessburst = None
                self.qospoliceraction = None
                self._segment_path = lambda: "qosPolicerEntry" + "[qosPolicerId='" + str(self.qospolicerid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosPolicerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qospolicertable.Qospolicerentry, ['qospolicerid', 'qospolicerrate', 'qospolicernormalburst', 'qospolicerexcessburst', 'qospoliceraction'], name, value)

            class Qospoliceraction(Enum):
                """
                Qospoliceraction (Enum Class)

                An indication of how to handle out of profile packets.  When

                the shape action is chosen then traffic is shaped to the rate

                specified by qosPolicerRate.

                .. data:: drop = 0

                .. data:: mark = 1

                .. data:: shape = 2

                """

                drop = Enum.YLeaf(0, "drop")

                mark = Enum.YLeaf(1, "mark")

                shape = Enum.YLeaf(2, "shape")



    class Qosaggregatetable(Entity):
        """
        Instances of this class identify aggregate flows and the
        policer to apply to each.
        
        .. attribute:: qosaggregateentry
        
        	An instance of this class specifies the policer to apply to an aggregate flow
        	**type**\: list of  		 :py:class:`Qosaggregateentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosaggregatetable.Qosaggregateentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosaggregatetable, self).__init__()

            self.yang_name = "qosAggregateTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosAggregateEntry", ("qosaggregateentry", CISCOQOSPIBMIB.Qosaggregatetable.Qosaggregateentry))])
            self._leafs = OrderedDict()

            self.qosaggregateentry = YList(self)
            self._segment_path = lambda: "qosAggregateTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosaggregatetable, [], name, value)


        class Qosaggregateentry(Entity):
            """
            An instance of this class specifies the policer to apply to
            an aggregate flow.
            
            .. attribute:: qosaggregateid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosaggregatepolicerid
            
            	An index identifying the instance of policer to apply to the aggregate.  It must correspond to the integer index of an instance of class qosPolicerTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosaggregatetable.Qosaggregateentry, self).__init__()

                self.yang_name = "qosAggregateEntry"
                self.yang_parent_name = "qosAggregateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosaggregateid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosaggregateid', YLeaf(YType.uint32, 'qosAggregateId')),
                    ('qosaggregatepolicerid', YLeaf(YType.uint32, 'qosAggregatePolicerId')),
                ])
                self.qosaggregateid = None
                self.qosaggregatepolicerid = None
                self._segment_path = lambda: "qosAggregateEntry" + "[qosAggregateId='" + str(self.qosaggregateid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosAggregateTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosaggregatetable.Qosaggregateentry, ['qosaggregateid', 'qosaggregatepolicerid'], name, value)


    class Qosmacclassificationtable(Entity):
        """
        A class of MAC/Vlan tuples and their associated CoS values.
        
        .. attribute:: qosmacclassificationentry
        
        	An instance of this class specifies the mapping of a VLAN and a MAC address to a CoS value
        	**type**\: list of  		 :py:class:`Qosmacclassificationentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosmacclassificationtable.Qosmacclassificationentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosmacclassificationtable, self).__init__()

            self.yang_name = "qosMacClassificationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosMacClassificationEntry", ("qosmacclassificationentry", CISCOQOSPIBMIB.Qosmacclassificationtable.Qosmacclassificationentry))])
            self._leafs = OrderedDict()

            self.qosmacclassificationentry = YList(self)
            self._segment_path = lambda: "qosMacClassificationTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosmacclassificationtable, [], name, value)


        class Qosmacclassificationentry(Entity):
            """
            An instance of this class specifies the mapping of a VLAN
            and a MAC address to a CoS value.
            
            .. attribute:: qosmacclassificationid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdstmacvlan
            
            	The VLAN of the destination MAC address of the L2 frame
            	**type**\: int
            
            	**range:** 1..4095
            
            .. attribute:: qosdstmacaddress
            
            	The destination MAC address of the L2 frame
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: qosdstmaccos
            
            	The CoS to assign the packet with the associated MAC/VLAN tuple.  Note that this CoS is overridden by the policies to classify the frame at layer 3 if there are any
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosmacclassificationtable.Qosmacclassificationentry, self).__init__()

                self.yang_name = "qosMacClassificationEntry"
                self.yang_parent_name = "qosMacClassificationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosmacclassificationid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosmacclassificationid', YLeaf(YType.uint32, 'qosMacClassificationId')),
                    ('qosdstmacvlan', YLeaf(YType.int32, 'qosDstMacVlan')),
                    ('qosdstmacaddress', YLeaf(YType.str, 'qosDstMacAddress')),
                    ('qosdstmaccos', YLeaf(YType.int32, 'qosDstMacCos')),
                ])
                self.qosmacclassificationid = None
                self.qosdstmacvlan = None
                self.qosdstmacaddress = None
                self.qosdstmaccos = None
                self._segment_path = lambda: "qosMacClassificationEntry" + "[qosMacClassificationId='" + str(self.qosmacclassificationid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosMacClassificationTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosmacclassificationtable.Qosmacclassificationentry, ['qosmacclassificationid', 'qosdstmacvlan', 'qosdstmacaddress', 'qosdstmaccos'], name, value)


    class Qosipacetable(Entity):
        """
        ACE definitions.
        
        .. attribute:: qosipaceentry
        
        	An instance of this class specifies an ACE
        	**type**\: list of  		 :py:class:`Qosipaceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipacetable.Qosipaceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosipacetable, self).__init__()

            self.yang_name = "qosIpAceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIpAceEntry", ("qosipaceentry", CISCOQOSPIBMIB.Qosipacetable.Qosipaceentry))])
            self._leafs = OrderedDict()

            self.qosipaceentry = YList(self)
            self._segment_path = lambda: "qosIpAceTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosipacetable, [], name, value)


        class Qosipaceentry(Entity):
            """
            An instance of this class specifies an ACE.
            
            .. attribute:: qosipaceid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacedstaddr
            
            	The IP address to match against the packet's destination IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacedstaddrmask
            
            	A mask for the matching of the destination IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacesrcaddr
            
            	The IP address to match against the packet's source IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacesrcaddrmask
            
            	A mask for the matching of the source IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacedscpmin
            
            	The minimum value that the DSCP in the packet can have and match this ACE
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosipacedscpmax
            
            	The maximum value that the DSCP in the packet can have and match this ACE
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosipaceprotocol
            
            	The IP protocol to match against the packet's protocol. A value of zero means match all
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: qosipacedstl4portmin
            
            	The minimum value that the packet's layer 4 dest port number can have and match this ACE
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacedstl4portmax
            
            	The maximum value that the packet's layer 4 dest port number can have and match this ACE
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacesrcl4portmin
            
            	The minimum value that the packet's layer 4 source port number can have and match this ACE
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacesrcl4portmax
            
            	The maximum value that the packet's layer 4 source port number can have and match this ACE
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacepermit
            
            	If the packet matches this ACE and the value of this attribute is true, then the matching process terminates and the QoS associated with this ACE (indirectly through the ACL) is applied to the packet.  If the value of this attribute is false, then no more ACEs in this ACL are compared to this packet and matching continues with the first ACE of the next ACL
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosipacetable.Qosipaceentry, self).__init__()

                self.yang_name = "qosIpAceEntry"
                self.yang_parent_name = "qosIpAceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipaceid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosipaceid', YLeaf(YType.uint32, 'qosIpAceId')),
                    ('qosipacedstaddr', YLeaf(YType.str, 'qosIpAceDstAddr')),
                    ('qosipacedstaddrmask', YLeaf(YType.str, 'qosIpAceDstAddrMask')),
                    ('qosipacesrcaddr', YLeaf(YType.str, 'qosIpAceSrcAddr')),
                    ('qosipacesrcaddrmask', YLeaf(YType.str, 'qosIpAceSrcAddrMask')),
                    ('qosipacedscpmin', YLeaf(YType.int32, 'qosIpAceDscpMin')),
                    ('qosipacedscpmax', YLeaf(YType.int32, 'qosIpAceDscpMax')),
                    ('qosipaceprotocol', YLeaf(YType.int32, 'qosIpAceProtocol')),
                    ('qosipacedstl4portmin', YLeaf(YType.int32, 'qosIpAceDstL4PortMin')),
                    ('qosipacedstl4portmax', YLeaf(YType.int32, 'qosIpAceDstL4PortMax')),
                    ('qosipacesrcl4portmin', YLeaf(YType.int32, 'qosIpAceSrcL4PortMin')),
                    ('qosipacesrcl4portmax', YLeaf(YType.int32, 'qosIpAceSrcL4PortMax')),
                    ('qosipacepermit', YLeaf(YType.boolean, 'qosIpAcePermit')),
                ])
                self.qosipaceid = None
                self.qosipacedstaddr = None
                self.qosipacedstaddrmask = None
                self.qosipacesrcaddr = None
                self.qosipacesrcaddrmask = None
                self.qosipacedscpmin = None
                self.qosipacedscpmax = None
                self.qosipaceprotocol = None
                self.qosipacedstl4portmin = None
                self.qosipacedstl4portmax = None
                self.qosipacesrcl4portmin = None
                self.qosipacesrcl4portmax = None
                self.qosipacepermit = None
                self._segment_path = lambda: "qosIpAceEntry" + "[qosIpAceId='" + str(self.qosipaceid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosipacetable.Qosipaceentry, ['qosipaceid', 'qosipacedstaddr', 'qosipacedstaddrmask', 'qosipacesrcaddr', 'qosipacesrcaddrmask', 'qosipacedscpmin', 'qosipacedscpmax', 'qosipaceprotocol', 'qosipacedstl4portmin', 'qosipacedstl4portmax', 'qosipacesrcl4portmin', 'qosipacesrcl4portmax', 'qosipacepermit'], name, value)


    class Qosipacldefinitiontable(Entity):
        """
        A class that defines a set of ACLs each being an ordered list
        of ACEs.
        
        .. attribute:: qosipacldefinitionentry
        
        	An instance of this class specifies an ACE in an ACL and its order with respect to other ACEs in the same ACL
        	**type**\: list of  		 :py:class:`Qosipacldefinitionentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipacldefinitiontable.Qosipacldefinitionentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosipacldefinitiontable, self).__init__()

            self.yang_name = "qosIpAclDefinitionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIpAclDefinitionEntry", ("qosipacldefinitionentry", CISCOQOSPIBMIB.Qosipacldefinitiontable.Qosipacldefinitionentry))])
            self._leafs = OrderedDict()

            self.qosipacldefinitionentry = YList(self)
            self._segment_path = lambda: "qosIpAclDefinitionTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosipacldefinitiontable, [], name, value)


        class Qosipacldefinitionentry(Entity):
            """
            An instance of this class specifies an ACE in an ACL and its
            order with respect to other ACEs in the same ACL.
            
            .. attribute:: qosipacldefinitionid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclid
            
            	An index for this ACL.  There will be one instance of policy class qosIpAclDefinition with this integer index for each ACE in the ACL per role combination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaceorder
            
            	An integer that determines the position of this ACE in the ACL. An ACE with a given order is positioned in the access contol list before one with a higher order
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacldefaceid
            
            	This attribute specifies the ACE in the qosIpAceTable that is in the ACL specified by qosIpAclId at the position specified by qosIpAceOrder
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosipacldefinitiontable.Qosipacldefinitionentry, self).__init__()

                self.yang_name = "qosIpAclDefinitionEntry"
                self.yang_parent_name = "qosIpAclDefinitionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipacldefinitionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosipacldefinitionid', YLeaf(YType.uint32, 'qosIpAclDefinitionId')),
                    ('qosipaclid', YLeaf(YType.uint32, 'qosIpAclId')),
                    ('qosipaceorder', YLeaf(YType.uint32, 'qosIpAceOrder')),
                    ('qosipacldefaceid', YLeaf(YType.uint32, 'qosIpAclDefAceId')),
                ])
                self.qosipacldefinitionid = None
                self.qosipaclid = None
                self.qosipaceorder = None
                self.qosipacldefaceid = None
                self._segment_path = lambda: "qosIpAclDefinitionEntry" + "[qosIpAclDefinitionId='" + str(self.qosipacldefinitionid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAclDefinitionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosipacldefinitiontable.Qosipacldefinitionentry, ['qosipacldefinitionid', 'qosipaclid', 'qosipaceorder', 'qosipacldefaceid'], name, value)


    class Qosipaclactiontable(Entity):
        """
        A class that applies a set of ACLs to interfaces specifying,
        for each interface the order of the ACL with respect to other
        ACLs applied to the same interface and, for each ACL the
        action to take for a packet that matches a permit ACE in that
        ACL.  Interfaces are specified abstractly in terms of
        interface role combinations.
        
        .. attribute:: qosipaclactionentry
        
        	An instance of this class applies an ACL to traffic in a particular direction on an interface with a particular role combination, and specifies the action for packets which match the ACL
        	**type**\: list of  		 :py:class:`Qosipaclactionentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipaclactiontable.Qosipaclactionentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosipaclactiontable, self).__init__()

            self.yang_name = "qosIpAclActionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIpAclActionEntry", ("qosipaclactionentry", CISCOQOSPIBMIB.Qosipaclactiontable.Qosipaclactionentry))])
            self._leafs = OrderedDict()

            self.qosipaclactionentry = YList(self)
            self._segment_path = lambda: "qosIpAclActionTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosipaclactiontable, [], name, value)


        class Qosipaclactionentry(Entity):
            """
            An instance of this class applies an ACL to traffic in a
            particular direction on an interface with a particular role
            combination, and specifies the action for packets which match
            the ACL.
            
            .. attribute:: qosipaclactionid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclactaclid
            
            	The ACL associated with this action
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclinterfaceroles
            
            	The interfaces to which this ACL applies specified in terms of a set of roles
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosipaclinterfacedirection
            
            	The direction of packet flow at the interface in question to which this ACL applies
            	**type**\:  :py:class:`Qosipaclinterfacedirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosipaclactiontable.Qosipaclactionentry.Qosipaclinterfacedirection>`
            
            .. attribute:: qosipaclorder
            
            	An integer that determines the order of this ACL in the list of ACLs applied to interfaces of the specified role combination. An ACL with a given order is positioned in the list before one with a higher order
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacldscp
            
            	The DSCP to classify the packet with in the event that the packet matches an ACE in this ACL and the ACE is a permit
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosipacldscptrusted
            
            	If this attribute is true, then the Dscp associated with the packet is trusted, i.e., it is assumed to have already been set.  In this case, the Dscp is not rewritten with qosIpAclDscp (qosIpAclDscp is ignored).  The packet is still policed as part of its micro flow and its aggregate flow.  When a trusted action is applied to an input interface, the Dscp associated with the packet is the one contained in the packet.  When a trusted action is applied to an output interface, the Dscp associated with the packet is the one that is the result of the input classification and policing
            	**type**\: bool
            
            .. attribute:: qosipaclmicroflowpolicerid
            
            	An index identifying the instance of policer to apply to the microflow.  It must correspond to the integer index of an instance of class qosPolicerTableor be zero.  If zero, the microflow is not policed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclaggregateid
            
            	An index identifying the aggregate that the packet belongs to.  It must correspond to the integer index of an instance of class qosAggregateTable or be zero.  If zero, the microflow does not belong to any aggregate and is not policed as part of any aggregate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosipaclactiontable.Qosipaclactionentry, self).__init__()

                self.yang_name = "qosIpAclActionEntry"
                self.yang_parent_name = "qosIpAclActionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipaclactionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosipaclactionid', YLeaf(YType.uint32, 'qosIpAclActionId')),
                    ('qosipaclactaclid', YLeaf(YType.uint32, 'qosIpAclActAclId')),
                    ('qosipaclinterfaceroles', YLeaf(YType.str, 'qosIpAclInterfaceRoles')),
                    ('qosipaclinterfacedirection', YLeaf(YType.enumeration, 'qosIpAclInterfaceDirection')),
                    ('qosipaclorder', YLeaf(YType.uint32, 'qosIpAclOrder')),
                    ('qosipacldscp', YLeaf(YType.int32, 'qosIpAclDscp')),
                    ('qosipacldscptrusted', YLeaf(YType.boolean, 'qosIpAclDscpTrusted')),
                    ('qosipaclmicroflowpolicerid', YLeaf(YType.uint32, 'qosIpAclMicroFlowPolicerId')),
                    ('qosipaclaggregateid', YLeaf(YType.uint32, 'qosIpAclAggregateId')),
                ])
                self.qosipaclactionid = None
                self.qosipaclactaclid = None
                self.qosipaclinterfaceroles = None
                self.qosipaclinterfacedirection = None
                self.qosipaclorder = None
                self.qosipacldscp = None
                self.qosipacldscptrusted = None
                self.qosipaclmicroflowpolicerid = None
                self.qosipaclaggregateid = None
                self._segment_path = lambda: "qosIpAclActionEntry" + "[qosIpAclActionId='" + str(self.qosipaclactionid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAclActionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosipaclactiontable.Qosipaclactionentry, ['qosipaclactionid', 'qosipaclactaclid', 'qosipaclinterfaceroles', 'qosipaclinterfacedirection', 'qosipaclorder', 'qosipacldscp', 'qosipacldscptrusted', 'qosipaclmicroflowpolicerid', 'qosipaclaggregateid'], name, value)

            class Qosipaclinterfacedirection(Enum):
                """
                Qosipaclinterfacedirection (Enum Class)

                The direction of packet flow at the interface in question to

                which this ACL applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")



    class Qosifschedulingpreferencestable(Entity):
        """
        This class specifies the scheduling preference an interface
        chooses if it supports multiple scheduling types.  Higher
        values are preferred over lower values.
        
        .. attribute:: qosifschedulingpreferenceentry
        
        	An instance of this class specifies a scheduling preference for a queue\-type on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`Qosifschedulingpreferenceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosifschedulingpreferencestable, self).__init__()

            self.yang_name = "qosIfSchedulingPreferencesTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfSchedulingPreferenceEntry", ("qosifschedulingpreferenceentry", CISCOQOSPIBMIB.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry))])
            self._leafs = OrderedDict()

            self.qosifschedulingpreferenceentry = YList(self)
            self._segment_path = lambda: "qosIfSchedulingPreferencesTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosifschedulingpreferencestable, [], name, value)


        class Qosifschedulingpreferenceentry(Entity):
            """
            An instance of this class specifies a scheduling preference
            for a queue\-type on an interface with a particular role
            combination.
            
            .. attribute:: qosifschedulingpreferenceid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifschedulingroles
            
            	The combination of roles the interface must have for this policy instance to apply to that interface
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosifschedulingpreference
            
            	The preference to use this scheduling discipline and queue type.  A higher value means a higher preference.  If two disciplines have the same preference the choice is a local decision
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: qosifschedulingdiscipline
            
            	An enumerate type for all the known scheduling disciplines
            	**type**\:  :py:class:`Qosifschedulingdiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.Qosifschedulingdiscipline>`
            
            .. attribute:: qosifschedulingqueuetype
            
            	The queue type of this preference
            	**type**\:  :py:class:`QosInterfaceQueueType <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosInterfaceQueueType>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry, self).__init__()

                self.yang_name = "qosIfSchedulingPreferenceEntry"
                self.yang_parent_name = "qosIfSchedulingPreferencesTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifschedulingpreferenceid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosifschedulingpreferenceid', YLeaf(YType.uint32, 'qosIfSchedulingPreferenceId')),
                    ('qosifschedulingroles', YLeaf(YType.str, 'qosIfSchedulingRoles')),
                    ('qosifschedulingpreference', YLeaf(YType.int32, 'qosIfSchedulingPreference')),
                    ('qosifschedulingdiscipline', YLeaf(YType.enumeration, 'qosIfSchedulingDiscipline')),
                    ('qosifschedulingqueuetype', YLeaf(YType.enumeration, 'qosIfSchedulingQueueType')),
                ])
                self.qosifschedulingpreferenceid = None
                self.qosifschedulingroles = None
                self.qosifschedulingpreference = None
                self.qosifschedulingdiscipline = None
                self.qosifschedulingqueuetype = None
                self._segment_path = lambda: "qosIfSchedulingPreferenceEntry" + "[qosIfSchedulingPreferenceId='" + str(self.qosifschedulingpreferenceid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfSchedulingPreferencesTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry, ['qosifschedulingpreferenceid', 'qosifschedulingroles', 'qosifschedulingpreference', 'qosifschedulingdiscipline', 'qosifschedulingqueuetype'], name, value)

            class Qosifschedulingdiscipline(Enum):
                """
                Qosifschedulingdiscipline (Enum Class)

                An enumerate type for all the known scheduling disciplines.

                .. data:: weightedFairQueueing = 1

                .. data:: weightedRoundRobin = 2

                .. data:: customQueueing = 3

                .. data:: priorityQueueing = 4

                .. data:: classBasedWFQ = 5

                .. data:: fifo = 6

                .. data:: pqWrr = 7

                .. data:: pqCbwfq = 8

                """

                weightedFairQueueing = Enum.YLeaf(1, "weightedFairQueueing")

                weightedRoundRobin = Enum.YLeaf(2, "weightedRoundRobin")

                customQueueing = Enum.YLeaf(3, "customQueueing")

                priorityQueueing = Enum.YLeaf(4, "priorityQueueing")

                classBasedWFQ = Enum.YLeaf(5, "classBasedWFQ")

                fifo = Enum.YLeaf(6, "fifo")

                pqWrr = Enum.YLeaf(7, "pqWrr")

                pqCbwfq = Enum.YLeaf(8, "pqCbwfq")



    class Qosifdroppreferencetable(Entity):
        """
        This class specifies the preference of the drop mechanism an
        interface chooses if it supports multiple drop mechanisms.
        Higher values are preferred over lower values.
        
        .. attribute:: qosifdroppreferenceentry
        
        	An instance of this class specifies a drop preference for a drop mechanism on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`Qosifdroppreferenceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifdroppreferencetable.Qosifdroppreferenceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosifdroppreferencetable, self).__init__()

            self.yang_name = "qosIfDropPreferenceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfDropPreferenceEntry", ("qosifdroppreferenceentry", CISCOQOSPIBMIB.Qosifdroppreferencetable.Qosifdroppreferenceentry))])
            self._leafs = OrderedDict()

            self.qosifdroppreferenceentry = YList(self)
            self._segment_path = lambda: "qosIfDropPreferenceTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosifdroppreferencetable, [], name, value)


        class Qosifdroppreferenceentry(Entity):
            """
            An instance of this class specifies a drop preference for
            a drop mechanism on an interface with a particular role
            combination.
            
            .. attribute:: qosifdroppreferenceid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifdroproles
            
            	The combination of roles the interface must have for this policy instance to apply to that interface
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosifdroppreference
            
            	The preference to use this drop mechanism.  A higher value means a higher preference.  If two mechanisms have the same preference the choice is a local decision
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: qosifdropdiscipline
            
            	An enumerate type for all the known drop mechanisms
            	**type**\:  :py:class:`Qosifdropdiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifdroppreferencetable.Qosifdroppreferenceentry.Qosifdropdiscipline>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosifdroppreferencetable.Qosifdroppreferenceentry, self).__init__()

                self.yang_name = "qosIfDropPreferenceEntry"
                self.yang_parent_name = "qosIfDropPreferenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifdroppreferenceid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosifdroppreferenceid', YLeaf(YType.uint32, 'qosIfDropPreferenceId')),
                    ('qosifdroproles', YLeaf(YType.str, 'qosIfDropRoles')),
                    ('qosifdroppreference', YLeaf(YType.int32, 'qosIfDropPreference')),
                    ('qosifdropdiscipline', YLeaf(YType.enumeration, 'qosIfDropDiscipline')),
                ])
                self.qosifdroppreferenceid = None
                self.qosifdroproles = None
                self.qosifdroppreference = None
                self.qosifdropdiscipline = None
                self._segment_path = lambda: "qosIfDropPreferenceEntry" + "[qosIfDropPreferenceId='" + str(self.qosifdroppreferenceid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfDropPreferenceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosifdroppreferencetable.Qosifdroppreferenceentry, ['qosifdroppreferenceid', 'qosifdroproles', 'qosifdroppreference', 'qosifdropdiscipline'], name, value)

            class Qosifdropdiscipline(Enum):
                """
                Qosifdropdiscipline (Enum Class)

                An enumerate type for all the known drop mechanisms.

                .. data:: qosIfDropWRED = 1

                .. data:: qosIfDropTailDrop = 2

                """

                qosIfDropWRED = Enum.YLeaf(1, "qosIfDropWRED")

                qosIfDropTailDrop = Enum.YLeaf(2, "qosIfDropTailDrop")



    class Qosifdscpassignmenttable(Entity):
        """
        The assignment of each DSCP to a queue and threshold for each
        interface queue type.
        
        .. attribute:: qosifdscpassignmententry
        
        	An instance of this class specifies the queue and threshold set for a packet with a particular DSCP on an interface of a particular type with a particular role combination
        	**type**\: list of  		 :py:class:`Qosifdscpassignmententry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifdscpassignmenttable.Qosifdscpassignmententry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosifdscpassignmenttable, self).__init__()

            self.yang_name = "qosIfDscpAssignmentTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfDscpAssignmentEntry", ("qosifdscpassignmententry", CISCOQOSPIBMIB.Qosifdscpassignmenttable.Qosifdscpassignmententry))])
            self._leafs = OrderedDict()

            self.qosifdscpassignmententry = YList(self)
            self._segment_path = lambda: "qosIfDscpAssignmentTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosifdscpassignmenttable, [], name, value)


        class Qosifdscpassignmententry(Entity):
            """
            An instance of this class specifies the queue and threshold
            set for a packet with a particular DSCP on an interface of
            a particular type with a particular role combination.
            
            .. attribute:: qosifdscpassignmentid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifdscproles
            
            	The role combination the interface must be configured with
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosifqueuetype
            
            	The interface queue type to which this row applies
            	**type**\:  :py:class:`QosInterfaceQueueType <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosInterfaceQueueType>`
            
            .. attribute:: qosifdscp
            
            	The DSCP to which this row applies
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: qosifqueue
            
            	The queue to which the DSCP applies for the given interface type
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: qosifthresholdset
            
            	The threshold set of the specified queue to which the DSCP applies for the given interface type
            	**type**\: int
            
            	**range:** 1..8
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosifdscpassignmenttable.Qosifdscpassignmententry, self).__init__()

                self.yang_name = "qosIfDscpAssignmentEntry"
                self.yang_parent_name = "qosIfDscpAssignmentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifdscpassignmentid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosifdscpassignmentid', YLeaf(YType.uint32, 'qosIfDscpAssignmentId')),
                    ('qosifdscproles', YLeaf(YType.str, 'qosIfDscpRoles')),
                    ('qosifqueuetype', YLeaf(YType.enumeration, 'qosIfQueueType')),
                    ('qosifdscp', YLeaf(YType.int32, 'qosIfDscp')),
                    ('qosifqueue', YLeaf(YType.int32, 'qosIfQueue')),
                    ('qosifthresholdset', YLeaf(YType.int32, 'qosIfThresholdSet')),
                ])
                self.qosifdscpassignmentid = None
                self.qosifdscproles = None
                self.qosifqueuetype = None
                self.qosifdscp = None
                self.qosifqueue = None
                self.qosifthresholdset = None
                self._segment_path = lambda: "qosIfDscpAssignmentEntry" + "[qosIfDscpAssignmentId='" + str(self.qosifdscpassignmentid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfDscpAssignmentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosifdscpassignmenttable.Qosifdscpassignmententry, ['qosifdscpassignmentid', 'qosifdscproles', 'qosifqueuetype', 'qosifdscp', 'qosifqueue', 'qosifthresholdset'], name, value)


    class Qosifredtable(Entity):
        """
        A class of lower and upper values for each threshold set in a
        queue supporting WRED.  If the size of the queue for a given
        threshold is below the lower value then packets assigned to
        that threshold are always accepted into the queue.  If the
        size of the queue is above upper value then packets are always
        dropped.  If the size of the queue is between the lower and
        the upper then packets are randomly dropped.
        
        .. attribute:: qosifredentry
        
        	An instance of this class specifies threshold limits for a particular RED threshold of a given threshold set on an interface and with a particular role combination
        	**type**\: list of  		 :py:class:`Qosifredentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifredtable.Qosifredentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosifredtable, self).__init__()

            self.yang_name = "qosIfRedTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfRedEntry", ("qosifredentry", CISCOQOSPIBMIB.Qosifredtable.Qosifredentry))])
            self._leafs = OrderedDict()

            self.qosifredentry = YList(self)
            self._segment_path = lambda: "qosIfRedTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosifredtable, [], name, value)


        class Qosifredentry(Entity):
            """
            An instance of this class specifies threshold limits for a
            particular RED threshold of a given threshold set on an
            interface and with a particular role combination.
            
            .. attribute:: qosifredid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifredroles
            
            	The role combination the interface must be configured with
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosifrednumthresholdsets
            
            	The values in this entry apply only to queues with the number of thresholds specified by this attribute
            	**type**\:  :py:class:`ThresholdSetRange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.ThresholdSetRange>`
            
            .. attribute:: qosifredthresholdset
            
            	The threshold set to which the lower and upper values apply. It must be in the range 1 through qosIfRedNumThresholdSets. There must be exactly one PRI for each value in this range
            	**type**\: int
            
            	**range:** 1..8
            
            .. attribute:: qosifredthresholdsetlower
            
            	The threshold value below which no packets are dropped
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: qosifredthresholdsetupper
            
            	The threshold value above which all packets are dropped
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosifredtable.Qosifredentry, self).__init__()

                self.yang_name = "qosIfRedEntry"
                self.yang_parent_name = "qosIfRedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifredid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosifredid', YLeaf(YType.uint32, 'qosIfRedId')),
                    ('qosifredroles', YLeaf(YType.str, 'qosIfRedRoles')),
                    ('qosifrednumthresholdsets', YLeaf(YType.enumeration, 'qosIfRedNumThresholdSets')),
                    ('qosifredthresholdset', YLeaf(YType.int32, 'qosIfRedThresholdSet')),
                    ('qosifredthresholdsetlower', YLeaf(YType.int32, 'qosIfRedThresholdSetLower')),
                    ('qosifredthresholdsetupper', YLeaf(YType.int32, 'qosIfRedThresholdSetUpper')),
                ])
                self.qosifredid = None
                self.qosifredroles = None
                self.qosifrednumthresholdsets = None
                self.qosifredthresholdset = None
                self.qosifredthresholdsetlower = None
                self.qosifredthresholdsetupper = None
                self._segment_path = lambda: "qosIfRedEntry" + "[qosIfRedId='" + str(self.qosifredid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfRedTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosifredtable.Qosifredentry, ['qosifredid', 'qosifredroles', 'qosifrednumthresholdsets', 'qosifredthresholdset', 'qosifredthresholdsetlower', 'qosifredthresholdsetupper'], name, value)


    class Qosiftaildroptable(Entity):
        """
        A class for threshold sets in a queue supporting tail drop.
        If the size of the queue for a given threshold set is at or
        below the specified value then packets assigned to that
        threshold set are always accepted into the queue.  If the size
        of the queue is above the specified value then packets are
        always dropped.
        
        .. attribute:: qosiftaildropentry
        
        	An instance of this class specifies the queue depth for a particular tail\-drop threshold set on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`Qosiftaildropentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosiftaildroptable.Qosiftaildropentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosiftaildroptable, self).__init__()

            self.yang_name = "qosIfTailDropTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfTailDropEntry", ("qosiftaildropentry", CISCOQOSPIBMIB.Qosiftaildroptable.Qosiftaildropentry))])
            self._leafs = OrderedDict()

            self.qosiftaildropentry = YList(self)
            self._segment_path = lambda: "qosIfTailDropTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosiftaildroptable, [], name, value)


        class Qosiftaildropentry(Entity):
            """
            An instance of this class specifies the queue depth for a
            particular tail\-drop threshold set on an interface with a
            particular role combination.
            
            .. attribute:: qosiftaildropid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosiftaildroproles
            
            	The role combination the interface must be configured with
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosiftaildropnumthresholdsets
            
            	The value in this entry applies only to queues with the number of thresholds specified by this attribute
            	**type**\:  :py:class:`ThresholdSetRange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.ThresholdSetRange>`
            
            .. attribute:: qosiftaildropthresholdset
            
            	The threshold set to which the threshold value applies
            	**type**\: int
            
            	**range:** 1..8
            
            .. attribute:: qosiftaildropthresholdsetvalue
            
            	The threshold value above which packets are dropped
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosiftaildroptable.Qosiftaildropentry, self).__init__()

                self.yang_name = "qosIfTailDropEntry"
                self.yang_parent_name = "qosIfTailDropTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosiftaildropid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosiftaildropid', YLeaf(YType.uint32, 'qosIfTailDropId')),
                    ('qosiftaildroproles', YLeaf(YType.str, 'qosIfTailDropRoles')),
                    ('qosiftaildropnumthresholdsets', YLeaf(YType.enumeration, 'qosIfTailDropNumThresholdSets')),
                    ('qosiftaildropthresholdset', YLeaf(YType.int32, 'qosIfTailDropThresholdSet')),
                    ('qosiftaildropthresholdsetvalue', YLeaf(YType.int32, 'qosIfTailDropThresholdSetValue')),
                ])
                self.qosiftaildropid = None
                self.qosiftaildroproles = None
                self.qosiftaildropnumthresholdsets = None
                self.qosiftaildropthresholdset = None
                self.qosiftaildropthresholdsetvalue = None
                self._segment_path = lambda: "qosIfTailDropEntry" + "[qosIfTailDropId='" + str(self.qosiftaildropid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfTailDropTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosiftaildroptable.Qosiftaildropentry, ['qosiftaildropid', 'qosiftaildroproles', 'qosiftaildropnumthresholdsets', 'qosiftaildropthresholdset', 'qosiftaildropthresholdsetvalue'], name, value)


    class Qosifweightstable(Entity):
        """
        A class of scheduling weights for each queue of an interface
        that supports weighted round robin scheduling or a mix of
        priority queueing and weighted round robin.  For a queue with
        N priority queues, the N highest queue numbers are the
        priority queues with the highest queue number having the
        highest priority.  WRR is applied to the non\-priority queues.
        
        .. attribute:: qosifweightsentry
        
        	An instance of this class specifies the scheduling weight for a particular queue of an interface with a particular number of queues and with a particular role combination
        	**type**\: list of  		 :py:class:`Qosifweightsentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.Qosifweightstable.Qosifweightsentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.Qosifweightstable, self).__init__()

            self.yang_name = "qosIfWeightsTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("qosIfWeightsEntry", ("qosifweightsentry", CISCOQOSPIBMIB.Qosifweightstable.Qosifweightsentry))])
            self._leafs = OrderedDict()

            self.qosifweightsentry = YList(self)
            self._segment_path = lambda: "qosIfWeightsTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.Qosifweightstable, [], name, value)


        class Qosifweightsentry(Entity):
            """
            An instance of this class specifies the scheduling weight for
            a particular queue of an interface with a particular number
            of queues and with a particular role combination.
            
            .. attribute:: qosifweightsid  (key)
            
            	An integer index to identify the instance of the policy class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifweightsroles
            
            	The role combination the interface must be configured with
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: qosifweightsnumqueues
            
            	The value of the weight in this instance applies only to interfaces with the number of queues specified by this attribute
            	**type**\:  :py:class:`QueueRange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QueueRange>`
            
            .. attribute:: qosifweightsqueue
            
            	The queue to which the weight applies
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: qosifweightsdrainsize
            
            	The maximum number of bytes that may be drained from the queue in one cycle.  The percentage of the bandwith allocated to this queue can be calculated from this attribute and the sum of the drain sizes of all the non\-priority queues of the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifweightsqueuesize
            
            	The size of the queue in bytes.  Some devices set queue size in terms of packets.  These devices must calculate the queue size in packets by assuming an average packet size suitable for the particular interface.  Some devices have a fixed size buffer to be shared among all queues.  These devices must allocate a fraction of the total buffer space to this queue calculated as the the ratio of the queue size to the sum of the queue sizes for the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.Qosifweightstable.Qosifweightsentry, self).__init__()

                self.yang_name = "qosIfWeightsEntry"
                self.yang_parent_name = "qosIfWeightsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifweightsid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosifweightsid', YLeaf(YType.uint32, 'qosIfWeightsId')),
                    ('qosifweightsroles', YLeaf(YType.str, 'qosIfWeightsRoles')),
                    ('qosifweightsnumqueues', YLeaf(YType.enumeration, 'qosIfWeightsNumQueues')),
                    ('qosifweightsqueue', YLeaf(YType.int32, 'qosIfWeightsQueue')),
                    ('qosifweightsdrainsize', YLeaf(YType.uint32, 'qosIfWeightsDrainSize')),
                    ('qosifweightsqueuesize', YLeaf(YType.uint32, 'qosIfWeightsQueueSize')),
                ])
                self.qosifweightsid = None
                self.qosifweightsroles = None
                self.qosifweightsnumqueues = None
                self.qosifweightsqueue = None
                self.qosifweightsdrainsize = None
                self.qosifweightsqueuesize = None
                self._segment_path = lambda: "qosIfWeightsEntry" + "[qosIfWeightsId='" + str(self.qosifweightsid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfWeightsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.Qosifweightstable.Qosifweightsentry, ['qosifweightsid', 'qosifweightsroles', 'qosifweightsnumqueues', 'qosifweightsqueue', 'qosifweightsdrainsize', 'qosifweightsqueuesize'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOQOSPIBMIB()
        return self._top_entity

