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
    	**type**\:  :py:class:`QosDevicePibIncarnationTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDevicePibIncarnationTable>`
    
    .. attribute:: qosdeviceattributetable
    
    	The single instance of this class indicates specific attributes of the device.  These include configuration values such as the configured PDP addresses, the maximum message size, and specific device capabilities.  The latter include input port\-based and output port\-based classification and/or policing, support for flow based policing, aggregate based policing, traffic shaping capabilities, etc
    	**type**\:  :py:class:`QosDeviceAttributeTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDeviceAttributeTable>`
    
    .. attribute:: qosinterfacetypetable
    
    	This class describes the interface types of the interfaces that exist on the device.  It includes the queue type, role combination and capabilities of interfaces.  The PEP does not report which specific interfaces have which characteristics
    	**type**\:  :py:class:`QosInterfaceTypeTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosInterfaceTypeTable>`
    
    .. attribute:: qosdiffservmappingtable
    
    	Maps each DSCP to a marked\-down DSCP.  Also maps each DSCP to an IP precedence and QosLayer2Cos.  When configured for the first time, all 64 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:  :py:class:`QosDiffServMappingTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDiffServMappingTable>`
    
    .. attribute:: qoscostodscptable
    
    	Maps each of eight CoS values to a DSCP.  When configured for the first time, all 8 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:  :py:class:`QosCosToDscpTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosCosToDscpTable>`
    
    .. attribute:: qosunmatchedpolicytable
    
    	A policy class that specifies what QoS to apply to a packet that does not match any other policy configured for this role combination for a particular direction of traffic
    	**type**\:  :py:class:`QosUnmatchedPolicyTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosUnmatchedPolicyTable>`
    
    .. attribute:: qospolicertable
    
    	A class specifying policing parameters for both microflows and aggregate flows.  This table is designed for policing according to a token bucket scheme where an average rate and burst size is specified
    	**type**\:  :py:class:`QosPolicerTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosPolicerTable>`
    
    .. attribute:: qosaggregatetable
    
    	Instances of this class identify aggregate flows and the policer to apply to each
    	**type**\:  :py:class:`QosAggregateTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosAggregateTable>`
    
    .. attribute:: qosmacclassificationtable
    
    	A class of MAC/Vlan tuples and their associated CoS values
    	**type**\:  :py:class:`QosMacClassificationTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosMacClassificationTable>`
    
    .. attribute:: qosipacetable
    
    	ACE definitions
    	**type**\:  :py:class:`QosIpAceTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAceTable>`
    
    .. attribute:: qosipacldefinitiontable
    
    	A class that defines a set of ACLs each being an ordered list of ACEs
    	**type**\:  :py:class:`QosIpAclDefinitionTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAclDefinitionTable>`
    
    .. attribute:: qosipaclactiontable
    
    	A class that applies a set of ACLs to interfaces specifying, for each interface the order of the ACL with respect to other ACLs applied to the same interface and, for each ACL the action to take for a packet that matches a permit ACE in that ACL.  Interfaces are specified abstractly in terms of interface role combinations
    	**type**\:  :py:class:`QosIpAclActionTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAclActionTable>`
    
    .. attribute:: qosifschedulingpreferencestable
    
    	This class specifies the scheduling preference an interface chooses if it supports multiple scheduling types.  Higher values are preferred over lower values
    	**type**\:  :py:class:`QosIfSchedulingPreferencesTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable>`
    
    .. attribute:: qosifdroppreferencetable
    
    	This class specifies the preference of the drop mechanism an interface chooses if it supports multiple drop mechanisms. Higher values are preferred over lower values
    	**type**\:  :py:class:`QosIfDropPreferenceTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfDropPreferenceTable>`
    
    .. attribute:: qosifdscpassignmenttable
    
    	The assignment of each DSCP to a queue and threshold for each interface queue type
    	**type**\:  :py:class:`QosIfDscpAssignmentTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfDscpAssignmentTable>`
    
    .. attribute:: qosifredtable
    
    	A class of lower and upper values for each threshold set in a queue supporting WRED.  If the size of the queue for a given threshold is below the lower value then packets assigned to that threshold are always accepted into the queue.  If the size of the queue is above upper value then packets are always dropped.  If the size of the queue is between the lower and the upper then packets are randomly dropped
    	**type**\:  :py:class:`QosIfRedTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfRedTable>`
    
    .. attribute:: qosiftaildroptable
    
    	A class for threshold sets in a queue supporting tail drop. If the size of the queue for a given threshold set is at or below the specified value then packets assigned to that threshold set are always accepted into the queue.  If the size of the queue is above the specified value then packets are always dropped
    	**type**\:  :py:class:`QosIfTailDropTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfTailDropTable>`
    
    .. attribute:: qosifweightstable
    
    	A class of scheduling weights for each queue of an interface that supports weighted round robin scheduling or a mix of priority queueing and weighted round robin.  For a queue with N priority queues, the N highest queue numbers are the priority queues with the highest queue number having the highest priority.  WRR is applied to the non\-priority queues
    	**type**\:  :py:class:`QosIfWeightsTable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfWeightsTable>`
    
    

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
        self._child_classes = OrderedDict([("qosDevicePibIncarnationTable", ("qosdevicepibincarnationtable", CISCOQOSPIBMIB.QosDevicePibIncarnationTable)), ("qosDeviceAttributeTable", ("qosdeviceattributetable", CISCOQOSPIBMIB.QosDeviceAttributeTable)), ("qosInterfaceTypeTable", ("qosinterfacetypetable", CISCOQOSPIBMIB.QosInterfaceTypeTable)), ("qosDiffServMappingTable", ("qosdiffservmappingtable", CISCOQOSPIBMIB.QosDiffServMappingTable)), ("qosCosToDscpTable", ("qoscostodscptable", CISCOQOSPIBMIB.QosCosToDscpTable)), ("qosUnmatchedPolicyTable", ("qosunmatchedpolicytable", CISCOQOSPIBMIB.QosUnmatchedPolicyTable)), ("qosPolicerTable", ("qospolicertable", CISCOQOSPIBMIB.QosPolicerTable)), ("qosAggregateTable", ("qosaggregatetable", CISCOQOSPIBMIB.QosAggregateTable)), ("qosMacClassificationTable", ("qosmacclassificationtable", CISCOQOSPIBMIB.QosMacClassificationTable)), ("qosIpAceTable", ("qosipacetable", CISCOQOSPIBMIB.QosIpAceTable)), ("qosIpAclDefinitionTable", ("qosipacldefinitiontable", CISCOQOSPIBMIB.QosIpAclDefinitionTable)), ("qosIpAclActionTable", ("qosipaclactiontable", CISCOQOSPIBMIB.QosIpAclActionTable)), ("qosIfSchedulingPreferencesTable", ("qosifschedulingpreferencestable", CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable)), ("qosIfDropPreferenceTable", ("qosifdroppreferencetable", CISCOQOSPIBMIB.QosIfDropPreferenceTable)), ("qosIfDscpAssignmentTable", ("qosifdscpassignmenttable", CISCOQOSPIBMIB.QosIfDscpAssignmentTable)), ("qosIfRedTable", ("qosifredtable", CISCOQOSPIBMIB.QosIfRedTable)), ("qosIfTailDropTable", ("qosiftaildroptable", CISCOQOSPIBMIB.QosIfTailDropTable)), ("qosIfWeightsTable", ("qosifweightstable", CISCOQOSPIBMIB.QosIfWeightsTable))])
        self._leafs = OrderedDict()

        self.qosdevicepibincarnationtable = CISCOQOSPIBMIB.QosDevicePibIncarnationTable()
        self.qosdevicepibincarnationtable.parent = self
        self._children_name_map["qosdevicepibincarnationtable"] = "qosDevicePibIncarnationTable"

        self.qosdeviceattributetable = CISCOQOSPIBMIB.QosDeviceAttributeTable()
        self.qosdeviceattributetable.parent = self
        self._children_name_map["qosdeviceattributetable"] = "qosDeviceAttributeTable"

        self.qosinterfacetypetable = CISCOQOSPIBMIB.QosInterfaceTypeTable()
        self.qosinterfacetypetable.parent = self
        self._children_name_map["qosinterfacetypetable"] = "qosInterfaceTypeTable"

        self.qosdiffservmappingtable = CISCOQOSPIBMIB.QosDiffServMappingTable()
        self.qosdiffservmappingtable.parent = self
        self._children_name_map["qosdiffservmappingtable"] = "qosDiffServMappingTable"

        self.qoscostodscptable = CISCOQOSPIBMIB.QosCosToDscpTable()
        self.qoscostodscptable.parent = self
        self._children_name_map["qoscostodscptable"] = "qosCosToDscpTable"

        self.qosunmatchedpolicytable = CISCOQOSPIBMIB.QosUnmatchedPolicyTable()
        self.qosunmatchedpolicytable.parent = self
        self._children_name_map["qosunmatchedpolicytable"] = "qosUnmatchedPolicyTable"

        self.qospolicertable = CISCOQOSPIBMIB.QosPolicerTable()
        self.qospolicertable.parent = self
        self._children_name_map["qospolicertable"] = "qosPolicerTable"

        self.qosaggregatetable = CISCOQOSPIBMIB.QosAggregateTable()
        self.qosaggregatetable.parent = self
        self._children_name_map["qosaggregatetable"] = "qosAggregateTable"

        self.qosmacclassificationtable = CISCOQOSPIBMIB.QosMacClassificationTable()
        self.qosmacclassificationtable.parent = self
        self._children_name_map["qosmacclassificationtable"] = "qosMacClassificationTable"

        self.qosipacetable = CISCOQOSPIBMIB.QosIpAceTable()
        self.qosipacetable.parent = self
        self._children_name_map["qosipacetable"] = "qosIpAceTable"

        self.qosipacldefinitiontable = CISCOQOSPIBMIB.QosIpAclDefinitionTable()
        self.qosipacldefinitiontable.parent = self
        self._children_name_map["qosipacldefinitiontable"] = "qosIpAclDefinitionTable"

        self.qosipaclactiontable = CISCOQOSPIBMIB.QosIpAclActionTable()
        self.qosipaclactiontable.parent = self
        self._children_name_map["qosipaclactiontable"] = "qosIpAclActionTable"

        self.qosifschedulingpreferencestable = CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable()
        self.qosifschedulingpreferencestable.parent = self
        self._children_name_map["qosifschedulingpreferencestable"] = "qosIfSchedulingPreferencesTable"

        self.qosifdroppreferencetable = CISCOQOSPIBMIB.QosIfDropPreferenceTable()
        self.qosifdroppreferencetable.parent = self
        self._children_name_map["qosifdroppreferencetable"] = "qosIfDropPreferenceTable"

        self.qosifdscpassignmenttable = CISCOQOSPIBMIB.QosIfDscpAssignmentTable()
        self.qosifdscpassignmenttable.parent = self
        self._children_name_map["qosifdscpassignmenttable"] = "qosIfDscpAssignmentTable"

        self.qosifredtable = CISCOQOSPIBMIB.QosIfRedTable()
        self.qosifredtable.parent = self
        self._children_name_map["qosifredtable"] = "qosIfRedTable"

        self.qosiftaildroptable = CISCOQOSPIBMIB.QosIfTailDropTable()
        self.qosiftaildroptable.parent = self
        self._children_name_map["qosiftaildroptable"] = "qosIfTailDropTable"

        self.qosifweightstable = CISCOQOSPIBMIB.QosIfWeightsTable()
        self.qosifweightstable.parent = self
        self._children_name_map["qosifweightstable"] = "qosIfWeightsTable"
        self._segment_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB"

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOQOSPIBMIB, [], name, value)


    class QosDevicePibIncarnationTable(Entity):
        """
        This class contains a single policy instance that identifies
        the current incarnation of the PIB and the PDP that installed
        this incarnation.  The instance of this class is reported to
        the PDP at client connect time so that the PDP can (attempt
        to) ascertain the current state of the PIB.
        
        .. attribute:: qosdevicepibincarnationentry
        
        	The single policy instance of this class identifies the current incarnation of the PIB and the PDP that installed this incarnation
        	**type**\: list of  		 :py:class:`QosDevicePibIncarnationEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosDevicePibIncarnationTable, self).__init__()

            self.yang_name = "qosDevicePibIncarnationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosDevicePibIncarnationEntry", ("qosdevicepibincarnationentry", CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry))])
            self._leafs = OrderedDict()

            self.qosdevicepibincarnationentry = YList(self)
            self._segment_path = lambda: "qosDevicePibIncarnationTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosDevicePibIncarnationTable, [], name, value)


        class QosDevicePibIncarnationEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry, self).__init__()

                self.yang_name = "qosDevicePibIncarnationEntry"
                self.yang_parent_name = "qosDevicePibIncarnationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdeviceincarnationid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry, [u'qosdeviceincarnationid', u'qosdevicepdpname', u'qosdevicepibincarnation', u'qosdevicepibttl'], name, value)


    class QosDeviceAttributeTable(Entity):
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
        	**type**\: list of  		 :py:class:`QosDeviceAttributeEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosDeviceAttributeTable, self).__init__()

            self.yang_name = "qosDeviceAttributeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosDeviceAttributeEntry", ("qosdeviceattributeentry", CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry))])
            self._leafs = OrderedDict()

            self.qosdeviceattributeentry = YList(self)
            self._segment_path = lambda: "qosDeviceAttributeTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosDeviceAttributeTable, [], name, value)


        class QosDeviceAttributeEntry(Entity):
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
            	**type**\:  :py:class:`QosDeviceCapabilities <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry.QosDeviceCapabilities>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry, self).__init__()

                self.yang_name = "qosDeviceAttributeEntry"
                self.yang_parent_name = "qosDeviceAttributeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdeviceattributeid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry, [u'qosdeviceattributeid', u'qosdevicepepdomain', u'qosdeviceprimarypdp', u'qosdevicesecondarypdp', u'qosdevicemaxmessagesize', u'qosdevicecapabilities'], name, value)


    class QosInterfaceTypeTable(Entity):
        """
        This class describes the interface types of the interfaces
        that exist on the device.  It includes the queue type, role
        combination and capabilities of interfaces.  The PEP does not
        report which specific interfaces have which characteristics.
        
        .. attribute:: qosinterfacetypeentry
        
        	An instance of this class describes a role combination for an interface type of an interface that exists on the device
        	**type**\: list of  		 :py:class:`QosInterfaceTypeEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosInterfaceTypeTable, self).__init__()

            self.yang_name = "qosInterfaceTypeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosInterfaceTypeEntry", ("qosinterfacetypeentry", CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry))])
            self._leafs = OrderedDict()

            self.qosinterfacetypeentry = YList(self)
            self._segment_path = lambda: "qosInterfaceTypeTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosInterfaceTypeTable, [], name, value)


        class QosInterfaceTypeEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry, self).__init__()

                self.yang_name = "qosInterfaceTypeEntry"
                self.yang_parent_name = "qosInterfaceTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosinterfacetypeid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry, [u'qosinterfacetypeid', u'qosinterfacequeuetype', u'qosinterfacetyperoles', u'qosinterfacetypecapabilities'], name, value)


    class QosDiffServMappingTable(Entity):
        """
        Maps each DSCP to a marked\-down DSCP.  Also maps each DSCP to
        an IP precedence and QosLayer2Cos.  When configured for the
        first time, all 64 entries of the table must be
        specified. Thereafter, instances may be modified (with a
        delete and install in a single decision) but not deleted
        unless all instances are deleted.
        
        .. attribute:: qosdiffservmappingentry
        
        	An instance of this class represents mappings from a DSCP
        	**type**\: list of  		 :py:class:`QosDiffServMappingEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosDiffServMappingTable, self).__init__()

            self.yang_name = "qosDiffServMappingTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosDiffServMappingEntry", ("qosdiffservmappingentry", CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry))])
            self._leafs = OrderedDict()

            self.qosdiffservmappingentry = YList(self)
            self._segment_path = lambda: "qosDiffServMappingTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosDiffServMappingTable, [], name, value)


        class QosDiffServMappingEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry, self).__init__()

                self.yang_name = "qosDiffServMappingEntry"
                self.yang_parent_name = "qosDiffServMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosdscp']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry, [u'qosdscp', u'qosmarkeddscp', u'qosl2cos'], name, value)


    class QosCosToDscpTable(Entity):
        """
        Maps each of eight CoS values to a DSCP.  When configured for
        the first time, all 8 entries of the table must be
        specified. Thereafter, instances may be modified (with a
        delete and install in a single decision) but not deleted
        unless all instances are deleted.
        
        .. attribute:: qoscostodscpentry
        
        	An instance of this class maps a CoS value to a DSCP
        	**type**\: list of  		 :py:class:`QosCosToDscpEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosCosToDscpTable, self).__init__()

            self.yang_name = "qosCosToDscpTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosCosToDscpEntry", ("qoscostodscpentry", CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry))])
            self._leafs = OrderedDict()

            self.qoscostodscpentry = YList(self)
            self._segment_path = lambda: "qosCosToDscpTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosCosToDscpTable, [], name, value)


        class QosCosToDscpEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry, self).__init__()

                self.yang_name = "qosCosToDscpEntry"
                self.yang_parent_name = "qosCosToDscpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qoscostodscpcos']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qoscostodscpcos', YLeaf(YType.int32, 'qosCosToDscpCos')),
                    ('qoscostodscpdscp', YLeaf(YType.int32, 'qosCosToDscpDscp')),
                ])
                self.qoscostodscpcos = None
                self.qoscostodscpdscp = None
                self._segment_path = lambda: "qosCosToDscpEntry" + "[qosCosToDscpCos='" + str(self.qoscostodscpcos) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosCosToDscpTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry, [u'qoscostodscpcos', u'qoscostodscpdscp'], name, value)


    class QosUnmatchedPolicyTable(Entity):
        """
        A policy class that specifies what QoS to apply to a packet
        that does not match any other policy configured for this role
        combination for a particular direction of traffic.
        
        .. attribute:: qosunmatchedpolicyentry
        
        	An instance of this class specifies the unmatched policy for a particular role combination for incoming or outgoing traffic
        	**type**\: list of  		 :py:class:`QosUnmatchedPolicyEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosUnmatchedPolicyTable, self).__init__()

            self.yang_name = "qosUnmatchedPolicyTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosUnmatchedPolicyEntry", ("qosunmatchedpolicyentry", CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry))])
            self._leafs = OrderedDict()

            self.qosunmatchedpolicyentry = YList(self)
            self._segment_path = lambda: "qosUnmatchedPolicyTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosUnmatchedPolicyTable, [], name, value)


        class QosUnmatchedPolicyEntry(Entity):
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
            	**type**\:  :py:class:`QosUnmatchedPolicyDirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry.QosUnmatchedPolicyDirection>`
            
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
                super(CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry, self).__init__()

                self.yang_name = "qosUnmatchedPolicyEntry"
                self.yang_parent_name = "qosUnmatchedPolicyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosunmatchedpolicyid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry, [u'qosunmatchedpolicyid', u'qosunmatchedpolicyrole', u'qosunmatchedpolicydirection', u'qosunmatchedpolicydscp', u'qosunmatchedpolicydscptrusted', u'qosunmatchpolmicroflowpolicerid', u'qosunmatchedpolicyaggregateid'], name, value)

            class QosUnmatchedPolicyDirection(Enum):
                """
                QosUnmatchedPolicyDirection (Enum Class)

                The direction of packet flow at the interface in question to

                which this instance applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")



    class QosPolicerTable(Entity):
        """
        A class specifying policing parameters for both microflows
        and aggregate flows.  This table is designed for policing
        according to a token bucket scheme where an average rate and
        burst size is specified.
        
        .. attribute:: qospolicerentry
        
        	An instance of this class specifies a set of policing parameters
        	**type**\: list of  		 :py:class:`QosPolicerEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosPolicerTable, self).__init__()

            self.yang_name = "qosPolicerTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosPolicerEntry", ("qospolicerentry", CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry))])
            self._leafs = OrderedDict()

            self.qospolicerentry = YList(self)
            self._segment_path = lambda: "qosPolicerTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosPolicerTable, [], name, value)


        class QosPolicerEntry(Entity):
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
            	**type**\:  :py:class:`QosPolicerAction <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry.QosPolicerAction>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry, self).__init__()

                self.yang_name = "qosPolicerEntry"
                self.yang_parent_name = "qosPolicerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qospolicerid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry, [u'qospolicerid', u'qospolicerrate', u'qospolicernormalburst', u'qospolicerexcessburst', u'qospoliceraction'], name, value)

            class QosPolicerAction(Enum):
                """
                QosPolicerAction (Enum Class)

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



    class QosAggregateTable(Entity):
        """
        Instances of this class identify aggregate flows and the
        policer to apply to each.
        
        .. attribute:: qosaggregateentry
        
        	An instance of this class specifies the policer to apply to an aggregate flow
        	**type**\: list of  		 :py:class:`QosAggregateEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosAggregateTable, self).__init__()

            self.yang_name = "qosAggregateTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosAggregateEntry", ("qosaggregateentry", CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry))])
            self._leafs = OrderedDict()

            self.qosaggregateentry = YList(self)
            self._segment_path = lambda: "qosAggregateTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosAggregateTable, [], name, value)


        class QosAggregateEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry, self).__init__()

                self.yang_name = "qosAggregateEntry"
                self.yang_parent_name = "qosAggregateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosaggregateid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('qosaggregateid', YLeaf(YType.uint32, 'qosAggregateId')),
                    ('qosaggregatepolicerid', YLeaf(YType.uint32, 'qosAggregatePolicerId')),
                ])
                self.qosaggregateid = None
                self.qosaggregatepolicerid = None
                self._segment_path = lambda: "qosAggregateEntry" + "[qosAggregateId='" + str(self.qosaggregateid) + "']"
                self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosAggregateTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry, [u'qosaggregateid', u'qosaggregatepolicerid'], name, value)


    class QosMacClassificationTable(Entity):
        """
        A class of MAC/Vlan tuples and their associated CoS values.
        
        .. attribute:: qosmacclassificationentry
        
        	An instance of this class specifies the mapping of a VLAN and a MAC address to a CoS value
        	**type**\: list of  		 :py:class:`QosMacClassificationEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosMacClassificationTable, self).__init__()

            self.yang_name = "qosMacClassificationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosMacClassificationEntry", ("qosmacclassificationentry", CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry))])
            self._leafs = OrderedDict()

            self.qosmacclassificationentry = YList(self)
            self._segment_path = lambda: "qosMacClassificationTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosMacClassificationTable, [], name, value)


        class QosMacClassificationEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry, self).__init__()

                self.yang_name = "qosMacClassificationEntry"
                self.yang_parent_name = "qosMacClassificationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosmacclassificationid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry, [u'qosmacclassificationid', u'qosdstmacvlan', u'qosdstmacaddress', u'qosdstmaccos'], name, value)


    class QosIpAceTable(Entity):
        """
        ACE definitions.
        
        .. attribute:: qosipaceentry
        
        	An instance of this class specifies an ACE
        	**type**\: list of  		 :py:class:`QosIpAceEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIpAceTable, self).__init__()

            self.yang_name = "qosIpAceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIpAceEntry", ("qosipaceentry", CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry))])
            self._leafs = OrderedDict()

            self.qosipaceentry = YList(self)
            self._segment_path = lambda: "qosIpAceTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIpAceTable, [], name, value)


        class QosIpAceEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry, self).__init__()

                self.yang_name = "qosIpAceEntry"
                self.yang_parent_name = "qosIpAceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipaceid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry, [u'qosipaceid', u'qosipacedstaddr', u'qosipacedstaddrmask', u'qosipacesrcaddr', u'qosipacesrcaddrmask', u'qosipacedscpmin', u'qosipacedscpmax', u'qosipaceprotocol', u'qosipacedstl4portmin', u'qosipacedstl4portmax', u'qosipacesrcl4portmin', u'qosipacesrcl4portmax', u'qosipacepermit'], name, value)


    class QosIpAclDefinitionTable(Entity):
        """
        A class that defines a set of ACLs each being an ordered list
        of ACEs.
        
        .. attribute:: qosipacldefinitionentry
        
        	An instance of this class specifies an ACE in an ACL and its order with respect to other ACEs in the same ACL
        	**type**\: list of  		 :py:class:`QosIpAclDefinitionEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIpAclDefinitionTable, self).__init__()

            self.yang_name = "qosIpAclDefinitionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIpAclDefinitionEntry", ("qosipacldefinitionentry", CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry))])
            self._leafs = OrderedDict()

            self.qosipacldefinitionentry = YList(self)
            self._segment_path = lambda: "qosIpAclDefinitionTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIpAclDefinitionTable, [], name, value)


        class QosIpAclDefinitionEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry, self).__init__()

                self.yang_name = "qosIpAclDefinitionEntry"
                self.yang_parent_name = "qosIpAclDefinitionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipacldefinitionid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry, [u'qosipacldefinitionid', u'qosipaclid', u'qosipaceorder', u'qosipacldefaceid'], name, value)


    class QosIpAclActionTable(Entity):
        """
        A class that applies a set of ACLs to interfaces specifying,
        for each interface the order of the ACL with respect to other
        ACLs applied to the same interface and, for each ACL the
        action to take for a packet that matches a permit ACE in that
        ACL.  Interfaces are specified abstractly in terms of
        interface role combinations.
        
        .. attribute:: qosipaclactionentry
        
        	An instance of this class applies an ACL to traffic in a particular direction on an interface with a particular role combination, and specifies the action for packets which match the ACL
        	**type**\: list of  		 :py:class:`QosIpAclActionEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIpAclActionTable, self).__init__()

            self.yang_name = "qosIpAclActionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIpAclActionEntry", ("qosipaclactionentry", CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry))])
            self._leafs = OrderedDict()

            self.qosipaclactionentry = YList(self)
            self._segment_path = lambda: "qosIpAclActionTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIpAclActionTable, [], name, value)


        class QosIpAclActionEntry(Entity):
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
            	**type**\:  :py:class:`QosIpAclInterfaceDirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry.QosIpAclInterfaceDirection>`
            
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
                super(CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry, self).__init__()

                self.yang_name = "qosIpAclActionEntry"
                self.yang_parent_name = "qosIpAclActionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosipaclactionid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry, [u'qosipaclactionid', u'qosipaclactaclid', u'qosipaclinterfaceroles', u'qosipaclinterfacedirection', u'qosipaclorder', u'qosipacldscp', u'qosipacldscptrusted', u'qosipaclmicroflowpolicerid', u'qosipaclaggregateid'], name, value)

            class QosIpAclInterfaceDirection(Enum):
                """
                QosIpAclInterfaceDirection (Enum Class)

                The direction of packet flow at the interface in question to

                which this ACL applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")



    class QosIfSchedulingPreferencesTable(Entity):
        """
        This class specifies the scheduling preference an interface
        chooses if it supports multiple scheduling types.  Higher
        values are preferred over lower values.
        
        .. attribute:: qosifschedulingpreferenceentry
        
        	An instance of this class specifies a scheduling preference for a queue\-type on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`QosIfSchedulingPreferenceEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable, self).__init__()

            self.yang_name = "qosIfSchedulingPreferencesTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfSchedulingPreferenceEntry", ("qosifschedulingpreferenceentry", CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry))])
            self._leafs = OrderedDict()

            self.qosifschedulingpreferenceentry = YList(self)
            self._segment_path = lambda: "qosIfSchedulingPreferencesTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable, [], name, value)


        class QosIfSchedulingPreferenceEntry(Entity):
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
            	**type**\:  :py:class:`QosIfSchedulingDiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry.QosIfSchedulingDiscipline>`
            
            .. attribute:: qosifschedulingqueuetype
            
            	The queue type of this preference
            	**type**\:  :py:class:`QosInterfaceQueueType <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosInterfaceQueueType>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry, self).__init__()

                self.yang_name = "qosIfSchedulingPreferenceEntry"
                self.yang_parent_name = "qosIfSchedulingPreferencesTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifschedulingpreferenceid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry, [u'qosifschedulingpreferenceid', u'qosifschedulingroles', u'qosifschedulingpreference', u'qosifschedulingdiscipline', u'qosifschedulingqueuetype'], name, value)

            class QosIfSchedulingDiscipline(Enum):
                """
                QosIfSchedulingDiscipline (Enum Class)

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



    class QosIfDropPreferenceTable(Entity):
        """
        This class specifies the preference of the drop mechanism an
        interface chooses if it supports multiple drop mechanisms.
        Higher values are preferred over lower values.
        
        .. attribute:: qosifdroppreferenceentry
        
        	An instance of this class specifies a drop preference for a drop mechanism on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`QosIfDropPreferenceEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfDropPreferenceTable, self).__init__()

            self.yang_name = "qosIfDropPreferenceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfDropPreferenceEntry", ("qosifdroppreferenceentry", CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry))])
            self._leafs = OrderedDict()

            self.qosifdroppreferenceentry = YList(self)
            self._segment_path = lambda: "qosIfDropPreferenceTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfDropPreferenceTable, [], name, value)


        class QosIfDropPreferenceEntry(Entity):
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
            	**type**\:  :py:class:`QosIfDropDiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry.QosIfDropDiscipline>`
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry, self).__init__()

                self.yang_name = "qosIfDropPreferenceEntry"
                self.yang_parent_name = "qosIfDropPreferenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifdroppreferenceid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry, [u'qosifdroppreferenceid', u'qosifdroproles', u'qosifdroppreference', u'qosifdropdiscipline'], name, value)

            class QosIfDropDiscipline(Enum):
                """
                QosIfDropDiscipline (Enum Class)

                An enumerate type for all the known drop mechanisms.

                .. data:: qosIfDropWRED = 1

                .. data:: qosIfDropTailDrop = 2

                """

                qosIfDropWRED = Enum.YLeaf(1, "qosIfDropWRED")

                qosIfDropTailDrop = Enum.YLeaf(2, "qosIfDropTailDrop")



    class QosIfDscpAssignmentTable(Entity):
        """
        The assignment of each DSCP to a queue and threshold for each
        interface queue type.
        
        .. attribute:: qosifdscpassignmententry
        
        	An instance of this class specifies the queue and threshold set for a packet with a particular DSCP on an interface of a particular type with a particular role combination
        	**type**\: list of  		 :py:class:`QosIfDscpAssignmentEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfDscpAssignmentTable, self).__init__()

            self.yang_name = "qosIfDscpAssignmentTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfDscpAssignmentEntry", ("qosifdscpassignmententry", CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry))])
            self._leafs = OrderedDict()

            self.qosifdscpassignmententry = YList(self)
            self._segment_path = lambda: "qosIfDscpAssignmentTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfDscpAssignmentTable, [], name, value)


        class QosIfDscpAssignmentEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry, self).__init__()

                self.yang_name = "qosIfDscpAssignmentEntry"
                self.yang_parent_name = "qosIfDscpAssignmentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifdscpassignmentid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry, [u'qosifdscpassignmentid', u'qosifdscproles', u'qosifqueuetype', u'qosifdscp', u'qosifqueue', u'qosifthresholdset'], name, value)


    class QosIfRedTable(Entity):
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
        	**type**\: list of  		 :py:class:`QosIfRedEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfRedTable, self).__init__()

            self.yang_name = "qosIfRedTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfRedEntry", ("qosifredentry", CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry))])
            self._leafs = OrderedDict()

            self.qosifredentry = YList(self)
            self._segment_path = lambda: "qosIfRedTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfRedTable, [], name, value)


        class QosIfRedEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry, self).__init__()

                self.yang_name = "qosIfRedEntry"
                self.yang_parent_name = "qosIfRedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifredid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry, [u'qosifredid', u'qosifredroles', u'qosifrednumthresholdsets', u'qosifredthresholdset', u'qosifredthresholdsetlower', u'qosifredthresholdsetupper'], name, value)


    class QosIfTailDropTable(Entity):
        """
        A class for threshold sets in a queue supporting tail drop.
        If the size of the queue for a given threshold set is at or
        below the specified value then packets assigned to that
        threshold set are always accepted into the queue.  If the size
        of the queue is above the specified value then packets are
        always dropped.
        
        .. attribute:: qosiftaildropentry
        
        	An instance of this class specifies the queue depth for a particular tail\-drop threshold set on an interface with a particular role combination
        	**type**\: list of  		 :py:class:`QosIfTailDropEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfTailDropTable, self).__init__()

            self.yang_name = "qosIfTailDropTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfTailDropEntry", ("qosiftaildropentry", CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry))])
            self._leafs = OrderedDict()

            self.qosiftaildropentry = YList(self)
            self._segment_path = lambda: "qosIfTailDropTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfTailDropTable, [], name, value)


        class QosIfTailDropEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry, self).__init__()

                self.yang_name = "qosIfTailDropEntry"
                self.yang_parent_name = "qosIfTailDropTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosiftaildropid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry, [u'qosiftaildropid', u'qosiftaildroproles', u'qosiftaildropnumthresholdsets', u'qosiftaildropthresholdset', u'qosiftaildropthresholdsetvalue'], name, value)


    class QosIfWeightsTable(Entity):
        """
        A class of scheduling weights for each queue of an interface
        that supports weighted round robin scheduling or a mix of
        priority queueing and weighted round robin.  For a queue with
        N priority queues, the N highest queue numbers are the
        priority queues with the highest queue number having the
        highest priority.  WRR is applied to the non\-priority queues.
        
        .. attribute:: qosifweightsentry
        
        	An instance of this class specifies the scheduling weight for a particular queue of an interface with a particular number of queues and with a particular role combination
        	**type**\: list of  		 :py:class:`QosIfWeightsEntry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CISCOQOSPIBMIB.QosIfWeightsTable, self).__init__()

            self.yang_name = "qosIfWeightsTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qosIfWeightsEntry", ("qosifweightsentry", CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry))])
            self._leafs = OrderedDict()

            self.qosifweightsentry = YList(self)
            self._segment_path = lambda: "qosIfWeightsTable"
            self._absolute_path = lambda: "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOQOSPIBMIB.QosIfWeightsTable, [], name, value)


        class QosIfWeightsEntry(Entity):
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
                super(CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry, self).__init__()

                self.yang_name = "qosIfWeightsEntry"
                self.yang_parent_name = "qosIfWeightsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['qosifweightsid']
                self._child_classes = OrderedDict([])
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
                self._perform_setattr(CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry, [u'qosifweightsid', u'qosifweightsroles', u'qosifweightsnumqueues', u'qosifweightsqueue', u'qosifweightsdrainsize', u'qosifweightsqueuesize'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOQOSPIBMIB()
        return self._top_entity

