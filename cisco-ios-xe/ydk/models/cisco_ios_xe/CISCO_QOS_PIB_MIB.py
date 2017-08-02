""" CISCO_QOS_PIB_MIB 

The Cisco QOS Policy PIB for provisioning QOS policy.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Qosinterfacequeuetype(Enum):
    """
    Qosinterfacequeuetype

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


class Queuerange(Enum):
    """
    Queuerange

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


class Thresholdsetrange(Enum):
    """
    Thresholdsetrange

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


class Qosinterfacetypecapabilities(Bits):
    """
    Qosinterfacetypecapabilities

    An enumeration of interface capabilities.  Used by the PDP to
    select policies and configuration to push to the PEP.
    Keys are:- wfq , outputL2Classification , inputUflowPolicing , outputAggregateShaping , cq , unspecified , pq , cbwfq , tailDrop , outputAggregatePolicing , inputL2Classification , inputAggregateShaping , outputPortClassification , pqWrr , policeByMarkingDown , inputUflowShaping , inputAggregatePolicing , fifo , policeByDropping , inputPortClassification , outputUflowShaping , outputIpClassification , wred , outputUflowPolicing , inputIpClassification , wrr , pqCbwfq

    """

    def __init__(self):
        super(Qosinterfacetypecapabilities, self).__init__()


class CiscoQosPibMib(Entity):
    """
    
    
    .. attribute:: qosaggregatetable
    
    	Instances of this class identify aggregate flows and the policer to apply to each
    	**type**\:   :py:class:`Qosaggregatetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosaggregatetable>`
    
    .. attribute:: qoscostodscptable
    
    	Maps each of eight CoS values to a DSCP.  When configured for the first time, all 8 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:   :py:class:`Qoscostodscptable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qoscostodscptable>`
    
    .. attribute:: qosdeviceattributetable
    
    	The single instance of this class indicates specific attributes of the device.  These include configuration values such as the configured PDP addresses, the maximum message size, and specific device capabilities.  The latter include input port\-based and output port\-based classification and/or policing, support for flow based policing, aggregate based policing, traffic shaping capabilities, etc
    	**type**\:   :py:class:`Qosdeviceattributetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdeviceattributetable>`
    
    .. attribute:: qosdevicepibincarnationtable
    
    	This class contains a single policy instance that identifies the current incarnation of the PIB and the PDP that installed this incarnation.  The instance of this class is reported to the PDP at client connect time so that the PDP can (attempt to) ascertain the current state of the PIB
    	**type**\:   :py:class:`Qosdevicepibincarnationtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdevicepibincarnationtable>`
    
    .. attribute:: qosdiffservmappingtable
    
    	Maps each DSCP to a marked\-down DSCP.  Also maps each DSCP to an IP precedence and QosLayer2Cos.  When configured for the first time, all 64 entries of the table must be specified. Thereafter, instances may be modified (with a delete and install in a single decision) but not deleted unless all instances are deleted
    	**type**\:   :py:class:`Qosdiffservmappingtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdiffservmappingtable>`
    
    .. attribute:: qosifdroppreferencetable
    
    	This class specifies the preference of the drop mechanism an interface chooses if it supports multiple drop mechanisms. Higher values are preferred over lower values
    	**type**\:   :py:class:`Qosifdroppreferencetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdroppreferencetable>`
    
    .. attribute:: qosifdscpassignmenttable
    
    	The assignment of each DSCP to a queue and threshold for each interface queue type
    	**type**\:   :py:class:`Qosifdscpassignmenttable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdscpassignmenttable>`
    
    .. attribute:: qosifredtable
    
    	A class of lower and upper values for each threshold set in a queue supporting WRED.  If the size of the queue for a given threshold is below the lower value then packets assigned to that threshold are always accepted into the queue.  If the size of the queue is above upper value then packets are always dropped.  If the size of the queue is between the lower and the upper then packets are randomly dropped
    	**type**\:   :py:class:`Qosifredtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifredtable>`
    
    .. attribute:: qosifschedulingpreferencestable
    
    	This class specifies the scheduling preference an interface chooses if it supports multiple scheduling types.  Higher values are preferred over lower values
    	**type**\:   :py:class:`Qosifschedulingpreferencestable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifschedulingpreferencestable>`
    
    .. attribute:: qosiftaildroptable
    
    	A class for threshold sets in a queue supporting tail drop. If the size of the queue for a given threshold set is at or below the specified value then packets assigned to that threshold set are always accepted into the queue.  If the size of the queue is above the specified value then packets are always dropped
    	**type**\:   :py:class:`Qosiftaildroptable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosiftaildroptable>`
    
    .. attribute:: qosifweightstable
    
    	A class of scheduling weights for each queue of an interface that supports weighted round robin scheduling or a mix of priority queueing and weighted round robin.  For a queue with N priority queues, the N highest queue numbers are the priority queues with the highest queue number having the highest priority.  WRR is applied to the non\-priority queues
    	**type**\:   :py:class:`Qosifweightstable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifweightstable>`
    
    .. attribute:: qosinterfacetypetable
    
    	This class describes the interface types of the interfaces that exist on the device.  It includes the queue type, role combination and capabilities of interfaces.  The PEP does not report which specific interfaces have which characteristics
    	**type**\:   :py:class:`Qosinterfacetypetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosinterfacetypetable>`
    
    .. attribute:: qosipacetable
    
    	ACE definitions
    	**type**\:   :py:class:`Qosipacetable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipacetable>`
    
    .. attribute:: qosipaclactiontable
    
    	A class that applies a set of ACLs to interfaces specifying, for each interface the order of the ACL with respect to other ACLs applied to the same interface and, for each ACL the action to take for a packet that matches a permit ACE in that ACL.  Interfaces are specified abstractly in terms of interface role combinations
    	**type**\:   :py:class:`Qosipaclactiontable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipaclactiontable>`
    
    .. attribute:: qosipacldefinitiontable
    
    	A class that defines a set of ACLs each being an ordered list of ACEs
    	**type**\:   :py:class:`Qosipacldefinitiontable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipacldefinitiontable>`
    
    .. attribute:: qosmacclassificationtable
    
    	A class of MAC/Vlan tuples and their associated CoS values
    	**type**\:   :py:class:`Qosmacclassificationtable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosmacclassificationtable>`
    
    .. attribute:: qospolicertable
    
    	A class specifying policing parameters for both microflows and aggregate flows.  This table is designed for policing according to a token bucket scheme where an average rate and burst size is specified
    	**type**\:   :py:class:`Qospolicertable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qospolicertable>`
    
    .. attribute:: qosunmatchedpolicytable
    
    	A policy class that specifies what QoS to apply to a packet that does not match any other policy configured for this role combination for a particular direction of traffic
    	**type**\:   :py:class:`Qosunmatchedpolicytable <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosunmatchedpolicytable>`
    
    

    """

    _prefix = 'CISCO-QOS-PIB-MIB'
    _revision = '2007-08-29'

    def __init__(self):
        super(CiscoQosPibMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-QOS-PIB-MIB"
        self.yang_parent_name = "CISCO-QOS-PIB-MIB"

        self.qosaggregatetable = CiscoQosPibMib.Qosaggregatetable()
        self.qosaggregatetable.parent = self
        self._children_name_map["qosaggregatetable"] = "qosAggregateTable"
        self._children_yang_names.add("qosAggregateTable")

        self.qoscostodscptable = CiscoQosPibMib.Qoscostodscptable()
        self.qoscostodscptable.parent = self
        self._children_name_map["qoscostodscptable"] = "qosCosToDscpTable"
        self._children_yang_names.add("qosCosToDscpTable")

        self.qosdeviceattributetable = CiscoQosPibMib.Qosdeviceattributetable()
        self.qosdeviceattributetable.parent = self
        self._children_name_map["qosdeviceattributetable"] = "qosDeviceAttributeTable"
        self._children_yang_names.add("qosDeviceAttributeTable")

        self.qosdevicepibincarnationtable = CiscoQosPibMib.Qosdevicepibincarnationtable()
        self.qosdevicepibincarnationtable.parent = self
        self._children_name_map["qosdevicepibincarnationtable"] = "qosDevicePibIncarnationTable"
        self._children_yang_names.add("qosDevicePibIncarnationTable")

        self.qosdiffservmappingtable = CiscoQosPibMib.Qosdiffservmappingtable()
        self.qosdiffservmappingtable.parent = self
        self._children_name_map["qosdiffservmappingtable"] = "qosDiffServMappingTable"
        self._children_yang_names.add("qosDiffServMappingTable")

        self.qosifdroppreferencetable = CiscoQosPibMib.Qosifdroppreferencetable()
        self.qosifdroppreferencetable.parent = self
        self._children_name_map["qosifdroppreferencetable"] = "qosIfDropPreferenceTable"
        self._children_yang_names.add("qosIfDropPreferenceTable")

        self.qosifdscpassignmenttable = CiscoQosPibMib.Qosifdscpassignmenttable()
        self.qosifdscpassignmenttable.parent = self
        self._children_name_map["qosifdscpassignmenttable"] = "qosIfDscpAssignmentTable"
        self._children_yang_names.add("qosIfDscpAssignmentTable")

        self.qosifredtable = CiscoQosPibMib.Qosifredtable()
        self.qosifredtable.parent = self
        self._children_name_map["qosifredtable"] = "qosIfRedTable"
        self._children_yang_names.add("qosIfRedTable")

        self.qosifschedulingpreferencestable = CiscoQosPibMib.Qosifschedulingpreferencestable()
        self.qosifschedulingpreferencestable.parent = self
        self._children_name_map["qosifschedulingpreferencestable"] = "qosIfSchedulingPreferencesTable"
        self._children_yang_names.add("qosIfSchedulingPreferencesTable")

        self.qosiftaildroptable = CiscoQosPibMib.Qosiftaildroptable()
        self.qosiftaildroptable.parent = self
        self._children_name_map["qosiftaildroptable"] = "qosIfTailDropTable"
        self._children_yang_names.add("qosIfTailDropTable")

        self.qosifweightstable = CiscoQosPibMib.Qosifweightstable()
        self.qosifweightstable.parent = self
        self._children_name_map["qosifweightstable"] = "qosIfWeightsTable"
        self._children_yang_names.add("qosIfWeightsTable")

        self.qosinterfacetypetable = CiscoQosPibMib.Qosinterfacetypetable()
        self.qosinterfacetypetable.parent = self
        self._children_name_map["qosinterfacetypetable"] = "qosInterfaceTypeTable"
        self._children_yang_names.add("qosInterfaceTypeTable")

        self.qosipacetable = CiscoQosPibMib.Qosipacetable()
        self.qosipacetable.parent = self
        self._children_name_map["qosipacetable"] = "qosIpAceTable"
        self._children_yang_names.add("qosIpAceTable")

        self.qosipaclactiontable = CiscoQosPibMib.Qosipaclactiontable()
        self.qosipaclactiontable.parent = self
        self._children_name_map["qosipaclactiontable"] = "qosIpAclActionTable"
        self._children_yang_names.add("qosIpAclActionTable")

        self.qosipacldefinitiontable = CiscoQosPibMib.Qosipacldefinitiontable()
        self.qosipacldefinitiontable.parent = self
        self._children_name_map["qosipacldefinitiontable"] = "qosIpAclDefinitionTable"
        self._children_yang_names.add("qosIpAclDefinitionTable")

        self.qosmacclassificationtable = CiscoQosPibMib.Qosmacclassificationtable()
        self.qosmacclassificationtable.parent = self
        self._children_name_map["qosmacclassificationtable"] = "qosMacClassificationTable"
        self._children_yang_names.add("qosMacClassificationTable")

        self.qospolicertable = CiscoQosPibMib.Qospolicertable()
        self.qospolicertable.parent = self
        self._children_name_map["qospolicertable"] = "qosPolicerTable"
        self._children_yang_names.add("qosPolicerTable")

        self.qosunmatchedpolicytable = CiscoQosPibMib.Qosunmatchedpolicytable()
        self.qosunmatchedpolicytable.parent = self
        self._children_name_map["qosunmatchedpolicytable"] = "qosUnmatchedPolicyTable"
        self._children_yang_names.add("qosUnmatchedPolicyTable")


    class Qosdevicepibincarnationtable(Entity):
        """
        This class contains a single policy instance that identifies
        the current incarnation of the PIB and the PDP that installed
        this incarnation.  The instance of this class is reported to
        the PDP at client connect time so that the PDP can (attempt
        to) ascertain the current state of the PIB.
        
        .. attribute:: qosdevicepibincarnationentry
        
        	The single policy instance of this class identifies the current incarnation of the PIB and the PDP that installed this incarnation
        	**type**\: list of    :py:class:`Qosdevicepibincarnationentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosdevicepibincarnationtable, self).__init__()

            self.yang_name = "qosDevicePibIncarnationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosdevicepibincarnationentry = YList(self)

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
                        super(CiscoQosPibMib.Qosdevicepibincarnationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosdevicepibincarnationtable, self).__setattr__(name, value)


        class Qosdevicepibincarnationentry(Entity):
            """
            The single policy instance of this class identifies the
            current incarnation of the PIB and the PDP that installed
            this incarnation.
            
            .. attribute:: qosdeviceincarnationid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicepdpname
            
            	The name of the PDP that installed the current incarnation of the PIB into the device.  By default it is the zero length string
            	**type**\:  str
            
            .. attribute:: qosdevicepibincarnation
            
            	An octet string to identify the current incarnation.  It has meaning to the PDP that installed the PIB and perhaps its standby PDPs. By default the empty string
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: qosdevicepibttl
            
            	The number of seconds after a client close or TCP timeout for which the PEP continues to enforce the policy in the PIB. After this interval, the PIB is consired expired and the device no longer enforces the policy installed in the PIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry, self).__init__()

                self.yang_name = "qosDevicePibIncarnationEntry"
                self.yang_parent_name = "qosDevicePibIncarnationTable"

                self.qosdeviceincarnationid = YLeaf(YType.uint32, "qosDeviceIncarnationId")

                self.qosdevicepdpname = YLeaf(YType.str, "qosDevicePdpName")

                self.qosdevicepibincarnation = YLeaf(YType.str, "qosDevicePibIncarnation")

                self.qosdevicepibttl = YLeaf(YType.uint32, "qosDevicePibTtl")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosdeviceincarnationid",
                                "qosdevicepdpname",
                                "qosdevicepibincarnation",
                                "qosdevicepibttl") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosdeviceincarnationid.is_set or
                    self.qosdevicepdpname.is_set or
                    self.qosdevicepibincarnation.is_set or
                    self.qosdevicepibttl.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosdeviceincarnationid.yfilter != YFilter.not_set or
                    self.qosdevicepdpname.yfilter != YFilter.not_set or
                    self.qosdevicepibincarnation.yfilter != YFilter.not_set or
                    self.qosdevicepibttl.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosDevicePibIncarnationEntry" + "[qosDeviceIncarnationId='" + self.qosdeviceincarnationid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDevicePibIncarnationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosdeviceincarnationid.is_set or self.qosdeviceincarnationid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdeviceincarnationid.get_name_leafdata())
                if (self.qosdevicepdpname.is_set or self.qosdevicepdpname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicepdpname.get_name_leafdata())
                if (self.qosdevicepibincarnation.is_set or self.qosdevicepibincarnation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicepibincarnation.get_name_leafdata())
                if (self.qosdevicepibttl.is_set or self.qosdevicepibttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicepibttl.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosDeviceIncarnationId" or name == "qosDevicePdpName" or name == "qosDevicePibIncarnation" or name == "qosDevicePibTtl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosDeviceIncarnationId"):
                    self.qosdeviceincarnationid = value
                    self.qosdeviceincarnationid.value_namespace = name_space
                    self.qosdeviceincarnationid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDevicePdpName"):
                    self.qosdevicepdpname = value
                    self.qosdevicepdpname.value_namespace = name_space
                    self.qosdevicepdpname.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDevicePibIncarnation"):
                    self.qosdevicepibincarnation = value
                    self.qosdevicepibincarnation.value_namespace = name_space
                    self.qosdevicepibincarnation.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDevicePibTtl"):
                    self.qosdevicepibttl = value
                    self.qosdevicepibttl.value_namespace = name_space
                    self.qosdevicepibttl.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosdevicepibincarnationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosdevicepibincarnationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosDevicePibIncarnationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosDevicePibIncarnationEntry"):
                for c in self.qosdevicepibincarnationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosdevicepibincarnationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosDevicePibIncarnationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosdeviceattributeentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosdeviceattributetable, self).__init__()

            self.yang_name = "qosDeviceAttributeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosdeviceattributeentry = YList(self)

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
                        super(CiscoQosPibMib.Qosdeviceattributetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosdeviceattributetable, self).__setattr__(name, value)


        class Qosdeviceattributeentry(Entity):
            """
            The single instance of this class indicates specific
            attributes of the device.
            
            .. attribute:: qosdeviceattributeid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicecapabilities
            
            	An enumeration of device capabilities.  Used by the PDP to select policies and configuration to push to the PEP
            	**type**\:   :py:class:`Qosdevicecapabilities <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry.Qosdevicecapabilities>`
            
            .. attribute:: qosdevicemaxmessagesize
            
            	The maximum size message that this PEP is capable of receiving in bytes.  A value of zero means that the maximum message size is unspecified (but does not mean it is unlimited).  A message greater than this maximum results in a MessageTooBig error on a 'no commit' REP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdevicepepdomain
            
            	The QoS domain that this device belongs to.  This is configured locally on the device (perhaps by some management protocol such as SNMP).  By default, it is the zero\-length string
            	**type**\:  str
            
            .. attribute:: qosdeviceprimarypdp
            
            	The address of the PDP configured to be the primary PDP for the device
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosdevicesecondarypdp
            
            	The address of the PDP configured to be the secondary PDP for the device.  An address of zero indicates no secondary is configured
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry, self).__init__()

                self.yang_name = "qosDeviceAttributeEntry"
                self.yang_parent_name = "qosDeviceAttributeTable"

                self.qosdeviceattributeid = YLeaf(YType.uint32, "qosDeviceAttributeId")

                self.qosdevicecapabilities = YLeaf(YType.bits, "qosDeviceCapabilities")

                self.qosdevicemaxmessagesize = YLeaf(YType.uint32, "qosDeviceMaxMessageSize")

                self.qosdevicepepdomain = YLeaf(YType.str, "qosDevicePepDomain")

                self.qosdeviceprimarypdp = YLeaf(YType.str, "qosDevicePrimaryPdp")

                self.qosdevicesecondarypdp = YLeaf(YType.str, "qosDeviceSecondaryPdp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosdeviceattributeid",
                                "qosdevicecapabilities",
                                "qosdevicemaxmessagesize",
                                "qosdevicepepdomain",
                                "qosdeviceprimarypdp",
                                "qosdevicesecondarypdp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosdeviceattributeid.is_set or
                    self.qosdevicecapabilities.is_set or
                    self.qosdevicemaxmessagesize.is_set or
                    self.qosdevicepepdomain.is_set or
                    self.qosdeviceprimarypdp.is_set or
                    self.qosdevicesecondarypdp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosdeviceattributeid.yfilter != YFilter.not_set or
                    self.qosdevicecapabilities.yfilter != YFilter.not_set or
                    self.qosdevicemaxmessagesize.yfilter != YFilter.not_set or
                    self.qosdevicepepdomain.yfilter != YFilter.not_set or
                    self.qosdeviceprimarypdp.yfilter != YFilter.not_set or
                    self.qosdevicesecondarypdp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosDeviceAttributeEntry" + "[qosDeviceAttributeId='" + self.qosdeviceattributeid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDeviceAttributeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosdeviceattributeid.is_set or self.qosdeviceattributeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdeviceattributeid.get_name_leafdata())
                if (self.qosdevicecapabilities.is_set or self.qosdevicecapabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicecapabilities.get_name_leafdata())
                if (self.qosdevicemaxmessagesize.is_set or self.qosdevicemaxmessagesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicemaxmessagesize.get_name_leafdata())
                if (self.qosdevicepepdomain.is_set or self.qosdevicepepdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicepepdomain.get_name_leafdata())
                if (self.qosdeviceprimarypdp.is_set or self.qosdeviceprimarypdp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdeviceprimarypdp.get_name_leafdata())
                if (self.qosdevicesecondarypdp.is_set or self.qosdevicesecondarypdp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdevicesecondarypdp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosDeviceAttributeId" or name == "qosDeviceCapabilities" or name == "qosDeviceMaxMessageSize" or name == "qosDevicePepDomain" or name == "qosDevicePrimaryPdp" or name == "qosDeviceSecondaryPdp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosDeviceAttributeId"):
                    self.qosdeviceattributeid = value
                    self.qosdeviceattributeid.value_namespace = name_space
                    self.qosdeviceattributeid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDeviceCapabilities"):
                    self.qosdevicecapabilities[value] = True
                if(value_path == "qosDeviceMaxMessageSize"):
                    self.qosdevicemaxmessagesize = value
                    self.qosdevicemaxmessagesize.value_namespace = name_space
                    self.qosdevicemaxmessagesize.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDevicePepDomain"):
                    self.qosdevicepepdomain = value
                    self.qosdevicepepdomain.value_namespace = name_space
                    self.qosdevicepepdomain.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDevicePrimaryPdp"):
                    self.qosdeviceprimarypdp = value
                    self.qosdeviceprimarypdp.value_namespace = name_space
                    self.qosdeviceprimarypdp.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDeviceSecondaryPdp"):
                    self.qosdevicesecondarypdp = value
                    self.qosdevicesecondarypdp.value_namespace = name_space
                    self.qosdevicesecondarypdp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosdeviceattributeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosdeviceattributeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosDeviceAttributeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosDeviceAttributeEntry"):
                for c in self.qosdeviceattributeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosdeviceattributeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosDeviceAttributeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosinterfacetypetable(Entity):
        """
        This class describes the interface types of the interfaces
        that exist on the device.  It includes the queue type, role
        combination and capabilities of interfaces.  The PEP does not
        report which specific interfaces have which characteristics.
        
        .. attribute:: qosinterfacetypeentry
        
        	An instance of this class describes a role combination for an interface type of an interface that exists on the device
        	**type**\: list of    :py:class:`Qosinterfacetypeentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosinterfacetypetable, self).__init__()

            self.yang_name = "qosInterfaceTypeTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosinterfacetypeentry = YList(self)

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
                        super(CiscoQosPibMib.Qosinterfacetypetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosinterfacetypetable, self).__setattr__(name, value)


        class Qosinterfacetypeentry(Entity):
            """
            An instance of this class describes a role combination for
            an interface type of an interface that exists on the device.
            
            .. attribute:: qosinterfacetypeid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosinterfacequeuetype
            
            	The interface type in terms of number of queues and thresholds
            	**type**\:   :py:class:`Qosinterfacequeuetype <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Qosinterfacequeuetype>`
            
            .. attribute:: qosinterfacetypecapabilities
            
            	An enumeration of interface capabilities.  Used by the PDP to select policies and configuration to push to the PEP
            	**type**\:   :py:class:`Qosinterfacetypecapabilities <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Qosinterfacetypecapabilities>`
            
            .. attribute:: qosinterfacetyperoles
            
            	A combination of roles on at least one interface of type qosInterfaceType
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry, self).__init__()

                self.yang_name = "qosInterfaceTypeEntry"
                self.yang_parent_name = "qosInterfaceTypeTable"

                self.qosinterfacetypeid = YLeaf(YType.uint32, "qosInterfaceTypeId")

                self.qosinterfacequeuetype = YLeaf(YType.enumeration, "qosInterfaceQueueType")

                self.qosinterfacetypecapabilities = YLeaf(YType.bits, "qosInterfaceTypeCapabilities")

                self.qosinterfacetyperoles = YLeaf(YType.str, "qosInterfaceTypeRoles")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosinterfacetypeid",
                                "qosinterfacequeuetype",
                                "qosinterfacetypecapabilities",
                                "qosinterfacetyperoles") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosinterfacetypeid.is_set or
                    self.qosinterfacequeuetype.is_set or
                    self.qosinterfacetypecapabilities.is_set or
                    self.qosinterfacetyperoles.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosinterfacetypeid.yfilter != YFilter.not_set or
                    self.qosinterfacequeuetype.yfilter != YFilter.not_set or
                    self.qosinterfacetypecapabilities.yfilter != YFilter.not_set or
                    self.qosinterfacetyperoles.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosInterfaceTypeEntry" + "[qosInterfaceTypeId='" + self.qosinterfacetypeid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosInterfaceTypeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosinterfacetypeid.is_set or self.qosinterfacetypeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosinterfacetypeid.get_name_leafdata())
                if (self.qosinterfacequeuetype.is_set or self.qosinterfacequeuetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosinterfacequeuetype.get_name_leafdata())
                if (self.qosinterfacetypecapabilities.is_set or self.qosinterfacetypecapabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosinterfacetypecapabilities.get_name_leafdata())
                if (self.qosinterfacetyperoles.is_set or self.qosinterfacetyperoles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosinterfacetyperoles.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosInterfaceTypeId" or name == "qosInterfaceQueueType" or name == "qosInterfaceTypeCapabilities" or name == "qosInterfaceTypeRoles"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosInterfaceTypeId"):
                    self.qosinterfacetypeid = value
                    self.qosinterfacetypeid.value_namespace = name_space
                    self.qosinterfacetypeid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosInterfaceQueueType"):
                    self.qosinterfacequeuetype = value
                    self.qosinterfacequeuetype.value_namespace = name_space
                    self.qosinterfacequeuetype.value_namespace_prefix = name_space_prefix
                if(value_path == "qosInterfaceTypeCapabilities"):
                    self.qosinterfacetypecapabilities[value] = True
                if(value_path == "qosInterfaceTypeRoles"):
                    self.qosinterfacetyperoles = value
                    self.qosinterfacetyperoles.value_namespace = name_space
                    self.qosinterfacetyperoles.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosinterfacetypeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosinterfacetypeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosInterfaceTypeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosInterfaceTypeEntry"):
                for c in self.qosinterfacetypeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosinterfacetypeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosInterfaceTypeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosdiffservmappingentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosdiffservmappingtable, self).__init__()

            self.yang_name = "qosDiffServMappingTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosdiffservmappingentry = YList(self)

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
                        super(CiscoQosPibMib.Qosdiffservmappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosdiffservmappingtable, self).__setattr__(name, value)


        class Qosdiffservmappingentry(Entity):
            """
            An instance of this class represents mappings from a DSCP.
            
            .. attribute:: qosdscp  <key>
            
            	A DSCP for which this entry contains mappings
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosl2cos
            
            	The L2 CoS value to use when mapping this DSCP to layer 2 CoS
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: qosmarkeddscp
            
            	The DSCP to use instead of the qosDscp when the packet is out of profile and hence marked as such
            	**type**\:  int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry, self).__init__()

                self.yang_name = "qosDiffServMappingEntry"
                self.yang_parent_name = "qosDiffServMappingTable"

                self.qosdscp = YLeaf(YType.int32, "qosDscp")

                self.qosl2cos = YLeaf(YType.int32, "qosL2Cos")

                self.qosmarkeddscp = YLeaf(YType.int32, "qosMarkedDscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosdscp",
                                "qosl2cos",
                                "qosmarkeddscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosdscp.is_set or
                    self.qosl2cos.is_set or
                    self.qosmarkeddscp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosdscp.yfilter != YFilter.not_set or
                    self.qosl2cos.yfilter != YFilter.not_set or
                    self.qosmarkeddscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosDiffServMappingEntry" + "[qosDscp='" + self.qosdscp.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosDiffServMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosdscp.is_set or self.qosdscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdscp.get_name_leafdata())
                if (self.qosl2cos.is_set or self.qosl2cos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosl2cos.get_name_leafdata())
                if (self.qosmarkeddscp.is_set or self.qosmarkeddscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosmarkeddscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosDscp" or name == "qosL2Cos" or name == "qosMarkedDscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosDscp"):
                    self.qosdscp = value
                    self.qosdscp.value_namespace = name_space
                    self.qosdscp.value_namespace_prefix = name_space_prefix
                if(value_path == "qosL2Cos"):
                    self.qosl2cos = value
                    self.qosl2cos.value_namespace = name_space
                    self.qosl2cos.value_namespace_prefix = name_space_prefix
                if(value_path == "qosMarkedDscp"):
                    self.qosmarkeddscp = value
                    self.qosmarkeddscp.value_namespace = name_space
                    self.qosmarkeddscp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosdiffservmappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosdiffservmappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosDiffServMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosDiffServMappingEntry"):
                for c in self.qosdiffservmappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosdiffservmappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosDiffServMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qoscostodscptable(Entity):
        """
        Maps each of eight CoS values to a DSCP.  When configured for
        the first time, all 8 entries of the table must be
        specified. Thereafter, instances may be modified (with a
        delete and install in a single decision) but not deleted
        unless all instances are deleted.
        
        .. attribute:: qoscostodscpentry
        
        	An instance of this class maps a CoS value to a DSCP
        	**type**\: list of    :py:class:`Qoscostodscpentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qoscostodscptable, self).__init__()

            self.yang_name = "qosCosToDscpTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qoscostodscpentry = YList(self)

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
                        super(CiscoQosPibMib.Qoscostodscptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qoscostodscptable, self).__setattr__(name, value)


        class Qoscostodscpentry(Entity):
            """
            An instance of this class maps a CoS value to a DSCP.
            
            .. attribute:: qoscostodscpcos  <key>
            
            	The L2 CoS value that is being mapped
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: qoscostodscpdscp
            
            	The DSCP value to use when mapping the L2 CoS to a DSCP
            	**type**\:  int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry, self).__init__()

                self.yang_name = "qosCosToDscpEntry"
                self.yang_parent_name = "qosCosToDscpTable"

                self.qoscostodscpcos = YLeaf(YType.int32, "qosCosToDscpCos")

                self.qoscostodscpdscp = YLeaf(YType.int32, "qosCosToDscpDscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qoscostodscpcos",
                                "qoscostodscpdscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qoscostodscpcos.is_set or
                    self.qoscostodscpdscp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qoscostodscpcos.yfilter != YFilter.not_set or
                    self.qoscostodscpdscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosCosToDscpEntry" + "[qosCosToDscpCos='" + self.qoscostodscpcos.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosCosToDscpTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qoscostodscpcos.is_set or self.qoscostodscpcos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qoscostodscpcos.get_name_leafdata())
                if (self.qoscostodscpdscp.is_set or self.qoscostodscpdscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qoscostodscpdscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosCosToDscpCos" or name == "qosCosToDscpDscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosCosToDscpCos"):
                    self.qoscostodscpcos = value
                    self.qoscostodscpcos.value_namespace = name_space
                    self.qoscostodscpcos.value_namespace_prefix = name_space_prefix
                if(value_path == "qosCosToDscpDscp"):
                    self.qoscostodscpdscp = value
                    self.qoscostodscpdscp.value_namespace = name_space
                    self.qoscostodscpdscp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qoscostodscpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qoscostodscpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosCosToDscpTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosCosToDscpEntry"):
                for c in self.qoscostodscpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qoscostodscpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosCosToDscpEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosunmatchedpolicytable(Entity):
        """
        A policy class that specifies what QoS to apply to a packet
        that does not match any other policy configured for this role
        combination for a particular direction of traffic.
        
        .. attribute:: qosunmatchedpolicyentry
        
        	An instance of this class specifies the unmatched policy for a particular role combination for incoming or outgoing traffic
        	**type**\: list of    :py:class:`Qosunmatchedpolicyentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosunmatchedpolicytable, self).__init__()

            self.yang_name = "qosUnmatchedPolicyTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosunmatchedpolicyentry = YList(self)

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
                        super(CiscoQosPibMib.Qosunmatchedpolicytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosunmatchedpolicytable, self).__setattr__(name, value)


        class Qosunmatchedpolicyentry(Entity):
            """
            An instance of this class specifies the unmatched policy
            for a particular role combination for incoming or outgoing
            traffic.
            
            .. attribute:: qosunmatchedpolicyid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosunmatchedpolicyaggregateid
            
            	An index identifying the aggregate that the packet belongs to.  It must correspond to the integer index of an instance of class qosAggregateTable or be zero.  If zero, the microflow does not belong to any aggregate and is not policed as part of any aggregate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosunmatchedpolicydirection
            
            	The direction of packet flow at the interface in question to which this instance applies
            	**type**\:   :py:class:`Qosunmatchedpolicydirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.Qosunmatchedpolicydirection>`
            
            .. attribute:: qosunmatchedpolicydscp
            
            	The DSCP to classify the unmatched packet with.  This must be specified even if qosUnmatchedPolicyDscpTrusted is true
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosunmatchedpolicydscptrusted
            
            	If this attribute is true, then the Dscp associated with the packet is trusted, i.e., it is assumed to have already been set.  In this case, the Dscp is not rewritten with qosUnmatchedPolicyDscp (qosUnmatchedPolicyDscp is ignored) unless this is a non\-IP packet and arrives untagged.  The packet is still policed as part of its micro flow and its aggregate flow.  When a trusted action is applied to an input interface, the Dscp (for an IP packet) or CoS (for a non\-IP packet) associated with the packet is the one contained in the packet. When a trusted action is applied to an output interface, the Dscp associated with the packet is the one that is the result of the input classification and policing
            	**type**\:  bool
            
            .. attribute:: qosunmatchedpolicyrole
            
            	Role combination for which this instance applies
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: qosunmatchpolmicroflowpolicerid
            
            	An index identifying the instance of policer to apply to unmatched packets.  It must correspond to the integer index of an instance of class qosPolicerTable or be zero.  If zero, the microflow is not policed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry, self).__init__()

                self.yang_name = "qosUnmatchedPolicyEntry"
                self.yang_parent_name = "qosUnmatchedPolicyTable"

                self.qosunmatchedpolicyid = YLeaf(YType.uint32, "qosUnmatchedPolicyId")

                self.qosunmatchedpolicyaggregateid = YLeaf(YType.uint32, "qosUnmatchedPolicyAggregateId")

                self.qosunmatchedpolicydirection = YLeaf(YType.enumeration, "qosUnmatchedPolicyDirection")

                self.qosunmatchedpolicydscp = YLeaf(YType.int32, "qosUnmatchedPolicyDscp")

                self.qosunmatchedpolicydscptrusted = YLeaf(YType.boolean, "qosUnmatchedPolicyDscpTrusted")

                self.qosunmatchedpolicyrole = YLeaf(YType.str, "qosUnmatchedPolicyRole")

                self.qosunmatchpolmicroflowpolicerid = YLeaf(YType.uint32, "qosUnmatchPolMicroFlowPolicerId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosunmatchedpolicyid",
                                "qosunmatchedpolicyaggregateid",
                                "qosunmatchedpolicydirection",
                                "qosunmatchedpolicydscp",
                                "qosunmatchedpolicydscptrusted",
                                "qosunmatchedpolicyrole",
                                "qosunmatchpolmicroflowpolicerid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry, self).__setattr__(name, value)

            class Qosunmatchedpolicydirection(Enum):
                """
                Qosunmatchedpolicydirection

                The direction of packet flow at the interface in question to

                which this instance applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")


            def has_data(self):
                return (
                    self.qosunmatchedpolicyid.is_set or
                    self.qosunmatchedpolicyaggregateid.is_set or
                    self.qosunmatchedpolicydirection.is_set or
                    self.qosunmatchedpolicydscp.is_set or
                    self.qosunmatchedpolicydscptrusted.is_set or
                    self.qosunmatchedpolicyrole.is_set or
                    self.qosunmatchpolmicroflowpolicerid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicyid.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicyaggregateid.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicydirection.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicydscp.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicydscptrusted.yfilter != YFilter.not_set or
                    self.qosunmatchedpolicyrole.yfilter != YFilter.not_set or
                    self.qosunmatchpolmicroflowpolicerid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosUnmatchedPolicyEntry" + "[qosUnmatchedPolicyId='" + self.qosunmatchedpolicyid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosUnmatchedPolicyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosunmatchedpolicyid.is_set or self.qosunmatchedpolicyid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicyid.get_name_leafdata())
                if (self.qosunmatchedpolicyaggregateid.is_set or self.qosunmatchedpolicyaggregateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicyaggregateid.get_name_leafdata())
                if (self.qosunmatchedpolicydirection.is_set or self.qosunmatchedpolicydirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicydirection.get_name_leafdata())
                if (self.qosunmatchedpolicydscp.is_set or self.qosunmatchedpolicydscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicydscp.get_name_leafdata())
                if (self.qosunmatchedpolicydscptrusted.is_set or self.qosunmatchedpolicydscptrusted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicydscptrusted.get_name_leafdata())
                if (self.qosunmatchedpolicyrole.is_set or self.qosunmatchedpolicyrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchedpolicyrole.get_name_leafdata())
                if (self.qosunmatchpolmicroflowpolicerid.is_set or self.qosunmatchpolmicroflowpolicerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosunmatchpolmicroflowpolicerid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosUnmatchedPolicyId" or name == "qosUnmatchedPolicyAggregateId" or name == "qosUnmatchedPolicyDirection" or name == "qosUnmatchedPolicyDscp" or name == "qosUnmatchedPolicyDscpTrusted" or name == "qosUnmatchedPolicyRole" or name == "qosUnmatchPolMicroFlowPolicerId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosUnmatchedPolicyId"):
                    self.qosunmatchedpolicyid = value
                    self.qosunmatchedpolicyid.value_namespace = name_space
                    self.qosunmatchedpolicyid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchedPolicyAggregateId"):
                    self.qosunmatchedpolicyaggregateid = value
                    self.qosunmatchedpolicyaggregateid.value_namespace = name_space
                    self.qosunmatchedpolicyaggregateid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchedPolicyDirection"):
                    self.qosunmatchedpolicydirection = value
                    self.qosunmatchedpolicydirection.value_namespace = name_space
                    self.qosunmatchedpolicydirection.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchedPolicyDscp"):
                    self.qosunmatchedpolicydscp = value
                    self.qosunmatchedpolicydscp.value_namespace = name_space
                    self.qosunmatchedpolicydscp.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchedPolicyDscpTrusted"):
                    self.qosunmatchedpolicydscptrusted = value
                    self.qosunmatchedpolicydscptrusted.value_namespace = name_space
                    self.qosunmatchedpolicydscptrusted.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchedPolicyRole"):
                    self.qosunmatchedpolicyrole = value
                    self.qosunmatchedpolicyrole.value_namespace = name_space
                    self.qosunmatchedpolicyrole.value_namespace_prefix = name_space_prefix
                if(value_path == "qosUnmatchPolMicroFlowPolicerId"):
                    self.qosunmatchpolmicroflowpolicerid = value
                    self.qosunmatchpolmicroflowpolicerid.value_namespace = name_space
                    self.qosunmatchpolmicroflowpolicerid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosunmatchedpolicyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosunmatchedpolicyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosUnmatchedPolicyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosUnmatchedPolicyEntry"):
                for c in self.qosunmatchedpolicyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosunmatchedpolicyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosUnmatchedPolicyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qospolicertable(Entity):
        """
        A class specifying policing parameters for both microflows
        and aggregate flows.  This table is designed for policing
        according to a token bucket scheme where an average rate and
        burst size is specified.
        
        .. attribute:: qospolicerentry
        
        	An instance of this class specifies a set of policing parameters
        	**type**\: list of    :py:class:`Qospolicerentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qospolicertable.Qospolicerentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qospolicertable, self).__init__()

            self.yang_name = "qosPolicerTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qospolicerentry = YList(self)

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
                        super(CiscoQosPibMib.Qospolicertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qospolicertable, self).__setattr__(name, value)


        class Qospolicerentry(Entity):
            """
            An instance of this class specifies a set of policing
            parameters.
            
            .. attribute:: qospolicerid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospoliceraction
            
            	An indication of how to handle out of profile packets.  When the shape action is chosen then traffic is shaped to the rate specified by qosPolicerRate
            	**type**\:   :py:class:`Qospoliceraction <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qospolicertable.Qospolicerentry.Qospoliceraction>`
            
            .. attribute:: qospolicerexcessburst
            
            	The excess size of a burst in terms of bits
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospolicernormalburst
            
            	The normal size of a burst in terms of bits
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospolicerrate
            
            	The token rate.  It is specified in units of bit/s. A rate of zero means that all packets will be out of profile.  If the qosPolicerAction is set to drop then this effectively denies any service to packets policed by this policer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qospolicertable.Qospolicerentry, self).__init__()

                self.yang_name = "qosPolicerEntry"
                self.yang_parent_name = "qosPolicerTable"

                self.qospolicerid = YLeaf(YType.uint32, "qosPolicerId")

                self.qospoliceraction = YLeaf(YType.enumeration, "qosPolicerAction")

                self.qospolicerexcessburst = YLeaf(YType.uint32, "qosPolicerExcessBurst")

                self.qospolicernormalburst = YLeaf(YType.uint32, "qosPolicerNormalBurst")

                self.qospolicerrate = YLeaf(YType.uint32, "qosPolicerRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qospolicerid",
                                "qospoliceraction",
                                "qospolicerexcessburst",
                                "qospolicernormalburst",
                                "qospolicerrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qospolicertable.Qospolicerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qospolicertable.Qospolicerentry, self).__setattr__(name, value)

            class Qospoliceraction(Enum):
                """
                Qospoliceraction

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


            def has_data(self):
                return (
                    self.qospolicerid.is_set or
                    self.qospoliceraction.is_set or
                    self.qospolicerexcessburst.is_set or
                    self.qospolicernormalburst.is_set or
                    self.qospolicerrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qospolicerid.yfilter != YFilter.not_set or
                    self.qospoliceraction.yfilter != YFilter.not_set or
                    self.qospolicerexcessburst.yfilter != YFilter.not_set or
                    self.qospolicernormalburst.yfilter != YFilter.not_set or
                    self.qospolicerrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosPolicerEntry" + "[qosPolicerId='" + self.qospolicerid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosPolicerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qospolicerid.is_set or self.qospolicerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qospolicerid.get_name_leafdata())
                if (self.qospoliceraction.is_set or self.qospoliceraction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qospoliceraction.get_name_leafdata())
                if (self.qospolicerexcessburst.is_set or self.qospolicerexcessburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qospolicerexcessburst.get_name_leafdata())
                if (self.qospolicernormalburst.is_set or self.qospolicernormalburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qospolicernormalburst.get_name_leafdata())
                if (self.qospolicerrate.is_set or self.qospolicerrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qospolicerrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosPolicerId" or name == "qosPolicerAction" or name == "qosPolicerExcessBurst" or name == "qosPolicerNormalBurst" or name == "qosPolicerRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosPolicerId"):
                    self.qospolicerid = value
                    self.qospolicerid.value_namespace = name_space
                    self.qospolicerid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosPolicerAction"):
                    self.qospoliceraction = value
                    self.qospoliceraction.value_namespace = name_space
                    self.qospoliceraction.value_namespace_prefix = name_space_prefix
                if(value_path == "qosPolicerExcessBurst"):
                    self.qospolicerexcessburst = value
                    self.qospolicerexcessburst.value_namespace = name_space
                    self.qospolicerexcessburst.value_namespace_prefix = name_space_prefix
                if(value_path == "qosPolicerNormalBurst"):
                    self.qospolicernormalburst = value
                    self.qospolicernormalburst.value_namespace = name_space
                    self.qospolicernormalburst.value_namespace_prefix = name_space_prefix
                if(value_path == "qosPolicerRate"):
                    self.qospolicerrate = value
                    self.qospolicerrate.value_namespace = name_space
                    self.qospolicerrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qospolicerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qospolicerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosPolicerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosPolicerEntry"):
                for c in self.qospolicerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qospolicertable.Qospolicerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qospolicerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosPolicerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosaggregatetable(Entity):
        """
        Instances of this class identify aggregate flows and the
        policer to apply to each.
        
        .. attribute:: qosaggregateentry
        
        	An instance of this class specifies the policer to apply to an aggregate flow
        	**type**\: list of    :py:class:`Qosaggregateentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosaggregatetable, self).__init__()

            self.yang_name = "qosAggregateTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosaggregateentry = YList(self)

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
                        super(CiscoQosPibMib.Qosaggregatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosaggregatetable, self).__setattr__(name, value)


        class Qosaggregateentry(Entity):
            """
            An instance of this class specifies the policer to apply to
            an aggregate flow.
            
            .. attribute:: qosaggregateid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosaggregatepolicerid
            
            	An index identifying the instance of policer to apply to the aggregate.  It must correspond to the integer index of an instance of class qosPolicerTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry, self).__init__()

                self.yang_name = "qosAggregateEntry"
                self.yang_parent_name = "qosAggregateTable"

                self.qosaggregateid = YLeaf(YType.uint32, "qosAggregateId")

                self.qosaggregatepolicerid = YLeaf(YType.uint32, "qosAggregatePolicerId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosaggregateid",
                                "qosaggregatepolicerid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosaggregateid.is_set or
                    self.qosaggregatepolicerid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosaggregateid.yfilter != YFilter.not_set or
                    self.qosaggregatepolicerid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosAggregateEntry" + "[qosAggregateId='" + self.qosaggregateid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosAggregateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosaggregateid.is_set or self.qosaggregateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosaggregateid.get_name_leafdata())
                if (self.qosaggregatepolicerid.is_set or self.qosaggregatepolicerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosaggregatepolicerid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosAggregateId" or name == "qosAggregatePolicerId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosAggregateId"):
                    self.qosaggregateid = value
                    self.qosaggregateid.value_namespace = name_space
                    self.qosaggregateid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosAggregatePolicerId"):
                    self.qosaggregatepolicerid = value
                    self.qosaggregatepolicerid.value_namespace = name_space
                    self.qosaggregatepolicerid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosaggregateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosaggregateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosAggregateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosAggregateEntry"):
                for c in self.qosaggregateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosaggregateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosAggregateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosmacclassificationtable(Entity):
        """
        A class of MAC/Vlan tuples and their associated CoS values.
        
        .. attribute:: qosmacclassificationentry
        
        	An instance of this class specifies the mapping of a VLAN and a MAC address to a CoS value
        	**type**\: list of    :py:class:`Qosmacclassificationentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosmacclassificationtable, self).__init__()

            self.yang_name = "qosMacClassificationTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosmacclassificationentry = YList(self)

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
                        super(CiscoQosPibMib.Qosmacclassificationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosmacclassificationtable, self).__setattr__(name, value)


        class Qosmacclassificationentry(Entity):
            """
            An instance of this class specifies the mapping of a VLAN
            and a MAC address to a CoS value.
            
            .. attribute:: qosmacclassificationid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosdstmacaddress
            
            	The destination MAC address of the L2 frame
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: qosdstmaccos
            
            	The CoS to assign the packet with the associated MAC/VLAN tuple.  Note that this CoS is overridden by the policies to classify the frame at layer 3 if there are any
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: qosdstmacvlan
            
            	The VLAN of the destination MAC address of the L2 frame
            	**type**\:  int
            
            	**range:** 1..4095
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry, self).__init__()

                self.yang_name = "qosMacClassificationEntry"
                self.yang_parent_name = "qosMacClassificationTable"

                self.qosmacclassificationid = YLeaf(YType.uint32, "qosMacClassificationId")

                self.qosdstmacaddress = YLeaf(YType.str, "qosDstMacAddress")

                self.qosdstmaccos = YLeaf(YType.int32, "qosDstMacCos")

                self.qosdstmacvlan = YLeaf(YType.int32, "qosDstMacVlan")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosmacclassificationid",
                                "qosdstmacaddress",
                                "qosdstmaccos",
                                "qosdstmacvlan") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosmacclassificationid.is_set or
                    self.qosdstmacaddress.is_set or
                    self.qosdstmaccos.is_set or
                    self.qosdstmacvlan.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosmacclassificationid.yfilter != YFilter.not_set or
                    self.qosdstmacaddress.yfilter != YFilter.not_set or
                    self.qosdstmaccos.yfilter != YFilter.not_set or
                    self.qosdstmacvlan.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosMacClassificationEntry" + "[qosMacClassificationId='" + self.qosmacclassificationid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosMacClassificationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosmacclassificationid.is_set or self.qosmacclassificationid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosmacclassificationid.get_name_leafdata())
                if (self.qosdstmacaddress.is_set or self.qosdstmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdstmacaddress.get_name_leafdata())
                if (self.qosdstmaccos.is_set or self.qosdstmaccos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdstmaccos.get_name_leafdata())
                if (self.qosdstmacvlan.is_set or self.qosdstmacvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosdstmacvlan.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosMacClassificationId" or name == "qosDstMacAddress" or name == "qosDstMacCos" or name == "qosDstMacVlan"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosMacClassificationId"):
                    self.qosmacclassificationid = value
                    self.qosmacclassificationid.value_namespace = name_space
                    self.qosmacclassificationid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDstMacAddress"):
                    self.qosdstmacaddress = value
                    self.qosdstmacaddress.value_namespace = name_space
                    self.qosdstmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDstMacCos"):
                    self.qosdstmaccos = value
                    self.qosdstmaccos.value_namespace = name_space
                    self.qosdstmaccos.value_namespace_prefix = name_space_prefix
                if(value_path == "qosDstMacVlan"):
                    self.qosdstmacvlan = value
                    self.qosdstmacvlan.value_namespace = name_space
                    self.qosdstmacvlan.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosmacclassificationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosmacclassificationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosMacClassificationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosMacClassificationEntry"):
                for c in self.qosmacclassificationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosmacclassificationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosMacClassificationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosipacetable(Entity):
        """
        ACE definitions.
        
        .. attribute:: qosipaceentry
        
        	An instance of this class specifies an ACE
        	**type**\: list of    :py:class:`Qosipaceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipacetable.Qosipaceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosipacetable, self).__init__()

            self.yang_name = "qosIpAceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosipaceentry = YList(self)

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
                        super(CiscoQosPibMib.Qosipacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosipacetable, self).__setattr__(name, value)


        class Qosipaceentry(Entity):
            """
            An instance of this class specifies an ACE.
            
            .. attribute:: qosipaceid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacedscpmax
            
            	The maximum value that the DSCP in the packet can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosipacedscpmin
            
            	The minimum value that the DSCP in the packet can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosipacedstaddr
            
            	The IP address to match against the packet's destination IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacedstaddrmask
            
            	A mask for the matching of the destination IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacedstl4portmax
            
            	The maximum value that the packet's layer 4 dest port number can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacedstl4portmin
            
            	The minimum value that the packet's layer 4 dest port number can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacepermit
            
            	If the packet matches this ACE and the value of this attribute is true, then the matching process terminates and the QoS associated with this ACE (indirectly through the ACL) is applied to the packet.  If the value of this attribute is false, then no more ACEs in this ACL are compared to this packet and matching continues with the first ACE of the next ACL
            	**type**\:  bool
            
            .. attribute:: qosipaceprotocol
            
            	The IP protocol to match against the packet's protocol. A value of zero means match all
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: qosipacesrcaddr
            
            	The IP address to match against the packet's source IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacesrcaddrmask
            
            	A mask for the matching of the source IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: qosipacesrcl4portmax
            
            	The maximum value that the packet's layer 4 source port number can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: qosipacesrcl4portmin
            
            	The minimum value that the packet's layer 4 source port number can have and match this ACE
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosipacetable.Qosipaceentry, self).__init__()

                self.yang_name = "qosIpAceEntry"
                self.yang_parent_name = "qosIpAceTable"

                self.qosipaceid = YLeaf(YType.uint32, "qosIpAceId")

                self.qosipacedscpmax = YLeaf(YType.int32, "qosIpAceDscpMax")

                self.qosipacedscpmin = YLeaf(YType.int32, "qosIpAceDscpMin")

                self.qosipacedstaddr = YLeaf(YType.str, "qosIpAceDstAddr")

                self.qosipacedstaddrmask = YLeaf(YType.str, "qosIpAceDstAddrMask")

                self.qosipacedstl4portmax = YLeaf(YType.int32, "qosIpAceDstL4PortMax")

                self.qosipacedstl4portmin = YLeaf(YType.int32, "qosIpAceDstL4PortMin")

                self.qosipacepermit = YLeaf(YType.boolean, "qosIpAcePermit")

                self.qosipaceprotocol = YLeaf(YType.int32, "qosIpAceProtocol")

                self.qosipacesrcaddr = YLeaf(YType.str, "qosIpAceSrcAddr")

                self.qosipacesrcaddrmask = YLeaf(YType.str, "qosIpAceSrcAddrMask")

                self.qosipacesrcl4portmax = YLeaf(YType.int32, "qosIpAceSrcL4PortMax")

                self.qosipacesrcl4portmin = YLeaf(YType.int32, "qosIpAceSrcL4PortMin")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosipaceid",
                                "qosipacedscpmax",
                                "qosipacedscpmin",
                                "qosipacedstaddr",
                                "qosipacedstaddrmask",
                                "qosipacedstl4portmax",
                                "qosipacedstl4portmin",
                                "qosipacepermit",
                                "qosipaceprotocol",
                                "qosipacesrcaddr",
                                "qosipacesrcaddrmask",
                                "qosipacesrcl4portmax",
                                "qosipacesrcl4portmin") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosipacetable.Qosipaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosipacetable.Qosipaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosipaceid.is_set or
                    self.qosipacedscpmax.is_set or
                    self.qosipacedscpmin.is_set or
                    self.qosipacedstaddr.is_set or
                    self.qosipacedstaddrmask.is_set or
                    self.qosipacedstl4portmax.is_set or
                    self.qosipacedstl4portmin.is_set or
                    self.qosipacepermit.is_set or
                    self.qosipaceprotocol.is_set or
                    self.qosipacesrcaddr.is_set or
                    self.qosipacesrcaddrmask.is_set or
                    self.qosipacesrcl4portmax.is_set or
                    self.qosipacesrcl4portmin.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosipaceid.yfilter != YFilter.not_set or
                    self.qosipacedscpmax.yfilter != YFilter.not_set or
                    self.qosipacedscpmin.yfilter != YFilter.not_set or
                    self.qosipacedstaddr.yfilter != YFilter.not_set or
                    self.qosipacedstaddrmask.yfilter != YFilter.not_set or
                    self.qosipacedstl4portmax.yfilter != YFilter.not_set or
                    self.qosipacedstl4portmin.yfilter != YFilter.not_set or
                    self.qosipacepermit.yfilter != YFilter.not_set or
                    self.qosipaceprotocol.yfilter != YFilter.not_set or
                    self.qosipacesrcaddr.yfilter != YFilter.not_set or
                    self.qosipacesrcaddrmask.yfilter != YFilter.not_set or
                    self.qosipacesrcl4portmax.yfilter != YFilter.not_set or
                    self.qosipacesrcl4portmin.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIpAceEntry" + "[qosIpAceId='" + self.qosipaceid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosipaceid.is_set or self.qosipaceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaceid.get_name_leafdata())
                if (self.qosipacedscpmax.is_set or self.qosipacedscpmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedscpmax.get_name_leafdata())
                if (self.qosipacedscpmin.is_set or self.qosipacedscpmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedscpmin.get_name_leafdata())
                if (self.qosipacedstaddr.is_set or self.qosipacedstaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedstaddr.get_name_leafdata())
                if (self.qosipacedstaddrmask.is_set or self.qosipacedstaddrmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedstaddrmask.get_name_leafdata())
                if (self.qosipacedstl4portmax.is_set or self.qosipacedstl4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedstl4portmax.get_name_leafdata())
                if (self.qosipacedstl4portmin.is_set or self.qosipacedstl4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacedstl4portmin.get_name_leafdata())
                if (self.qosipacepermit.is_set or self.qosipacepermit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacepermit.get_name_leafdata())
                if (self.qosipaceprotocol.is_set or self.qosipaceprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaceprotocol.get_name_leafdata())
                if (self.qosipacesrcaddr.is_set or self.qosipacesrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacesrcaddr.get_name_leafdata())
                if (self.qosipacesrcaddrmask.is_set or self.qosipacesrcaddrmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacesrcaddrmask.get_name_leafdata())
                if (self.qosipacesrcl4portmax.is_set or self.qosipacesrcl4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacesrcl4portmax.get_name_leafdata())
                if (self.qosipacesrcl4portmin.is_set or self.qosipacesrcl4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacesrcl4portmin.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIpAceId" or name == "qosIpAceDscpMax" or name == "qosIpAceDscpMin" or name == "qosIpAceDstAddr" or name == "qosIpAceDstAddrMask" or name == "qosIpAceDstL4PortMax" or name == "qosIpAceDstL4PortMin" or name == "qosIpAcePermit" or name == "qosIpAceProtocol" or name == "qosIpAceSrcAddr" or name == "qosIpAceSrcAddrMask" or name == "qosIpAceSrcL4PortMax" or name == "qosIpAceSrcL4PortMin"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIpAceId"):
                    self.qosipaceid = value
                    self.qosipaceid.value_namespace = name_space
                    self.qosipaceid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDscpMax"):
                    self.qosipacedscpmax = value
                    self.qosipacedscpmax.value_namespace = name_space
                    self.qosipacedscpmax.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDscpMin"):
                    self.qosipacedscpmin = value
                    self.qosipacedscpmin.value_namespace = name_space
                    self.qosipacedscpmin.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDstAddr"):
                    self.qosipacedstaddr = value
                    self.qosipacedstaddr.value_namespace = name_space
                    self.qosipacedstaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDstAddrMask"):
                    self.qosipacedstaddrmask = value
                    self.qosipacedstaddrmask.value_namespace = name_space
                    self.qosipacedstaddrmask.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDstL4PortMax"):
                    self.qosipacedstl4portmax = value
                    self.qosipacedstl4portmax.value_namespace = name_space
                    self.qosipacedstl4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceDstL4PortMin"):
                    self.qosipacedstl4portmin = value
                    self.qosipacedstl4portmin.value_namespace = name_space
                    self.qosipacedstl4portmin.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAcePermit"):
                    self.qosipacepermit = value
                    self.qosipacepermit.value_namespace = name_space
                    self.qosipacepermit.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceProtocol"):
                    self.qosipaceprotocol = value
                    self.qosipaceprotocol.value_namespace = name_space
                    self.qosipaceprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceSrcAddr"):
                    self.qosipacesrcaddr = value
                    self.qosipacesrcaddr.value_namespace = name_space
                    self.qosipacesrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceSrcAddrMask"):
                    self.qosipacesrcaddrmask = value
                    self.qosipacesrcaddrmask.value_namespace = name_space
                    self.qosipacesrcaddrmask.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceSrcL4PortMax"):
                    self.qosipacesrcl4portmax = value
                    self.qosipacesrcl4portmax.value_namespace = name_space
                    self.qosipacesrcl4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceSrcL4PortMin"):
                    self.qosipacesrcl4portmin = value
                    self.qosipacesrcl4portmin.value_namespace = name_space
                    self.qosipacesrcl4portmin.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosipaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosipaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIpAceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIpAceEntry"):
                for c in self.qosipaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosipacetable.Qosipaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosipaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIpAceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosipacldefinitiontable(Entity):
        """
        A class that defines a set of ACLs each being an ordered list
        of ACEs.
        
        .. attribute:: qosipacldefinitionentry
        
        	An instance of this class specifies an ACE in an ACL and its order with respect to other ACEs in the same ACL
        	**type**\: list of    :py:class:`Qosipacldefinitionentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosipacldefinitiontable, self).__init__()

            self.yang_name = "qosIpAclDefinitionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosipacldefinitionentry = YList(self)

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
                        super(CiscoQosPibMib.Qosipacldefinitiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosipacldefinitiontable, self).__setattr__(name, value)


        class Qosipacldefinitionentry(Entity):
            """
            An instance of this class specifies an ACE in an ACL and its
            order with respect to other ACEs in the same ACL.
            
            .. attribute:: qosipacldefinitionid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaceorder
            
            	An integer that determines the position of this ACE in the ACL. An ACE with a given order is positioned in the access contol list before one with a higher order
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacldefaceid
            
            	This attribute specifies the ACE in the qosIpAceTable that is in the ACL specified by qosIpAclId at the position specified by qosIpAceOrder
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclid
            
            	An index for this ACL.  There will be one instance of policy class qosIpAclDefinition with this integer index for each ACE in the ACL per role combination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry, self).__init__()

                self.yang_name = "qosIpAclDefinitionEntry"
                self.yang_parent_name = "qosIpAclDefinitionTable"

                self.qosipacldefinitionid = YLeaf(YType.uint32, "qosIpAclDefinitionId")

                self.qosipaceorder = YLeaf(YType.uint32, "qosIpAceOrder")

                self.qosipacldefaceid = YLeaf(YType.uint32, "qosIpAclDefAceId")

                self.qosipaclid = YLeaf(YType.uint32, "qosIpAclId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosipacldefinitionid",
                                "qosipaceorder",
                                "qosipacldefaceid",
                                "qosipaclid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosipacldefinitionid.is_set or
                    self.qosipaceorder.is_set or
                    self.qosipacldefaceid.is_set or
                    self.qosipaclid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosipacldefinitionid.yfilter != YFilter.not_set or
                    self.qosipaceorder.yfilter != YFilter.not_set or
                    self.qosipacldefaceid.yfilter != YFilter.not_set or
                    self.qosipaclid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIpAclDefinitionEntry" + "[qosIpAclDefinitionId='" + self.qosipacldefinitionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAclDefinitionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosipacldefinitionid.is_set or self.qosipacldefinitionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacldefinitionid.get_name_leafdata())
                if (self.qosipaceorder.is_set or self.qosipaceorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaceorder.get_name_leafdata())
                if (self.qosipacldefaceid.is_set or self.qosipacldefaceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacldefaceid.get_name_leafdata())
                if (self.qosipaclid.is_set or self.qosipaclid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIpAclDefinitionId" or name == "qosIpAceOrder" or name == "qosIpAclDefAceId" or name == "qosIpAclId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIpAclDefinitionId"):
                    self.qosipacldefinitionid = value
                    self.qosipacldefinitionid.value_namespace = name_space
                    self.qosipacldefinitionid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAceOrder"):
                    self.qosipaceorder = value
                    self.qosipaceorder.value_namespace = name_space
                    self.qosipaceorder.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclDefAceId"):
                    self.qosipacldefaceid = value
                    self.qosipacldefaceid.value_namespace = name_space
                    self.qosipacldefaceid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclId"):
                    self.qosipaclid = value
                    self.qosipaclid.value_namespace = name_space
                    self.qosipaclid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosipacldefinitionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosipacldefinitionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIpAclDefinitionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIpAclDefinitionEntry"):
                for c in self.qosipacldefinitionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosipacldefinitionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIpAclDefinitionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosipaclactionentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosipaclactiontable, self).__init__()

            self.yang_name = "qosIpAclActionTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosipaclactionentry = YList(self)

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
                        super(CiscoQosPibMib.Qosipaclactiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosipaclactiontable, self).__setattr__(name, value)


        class Qosipaclactionentry(Entity):
            """
            An instance of this class applies an ACL to traffic in a
            particular direction on an interface with a particular role
            combination, and specifies the action for packets which match
            the ACL.
            
            .. attribute:: qosipaclactionid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclactaclid
            
            	The ACL associated with this action
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclaggregateid
            
            	An index identifying the aggregate that the packet belongs to.  It must correspond to the integer index of an instance of class qosAggregateTable or be zero.  If zero, the microflow does not belong to any aggregate and is not policed as part of any aggregate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipacldscp
            
            	The DSCP to classify the packet with in the event that the packet matches an ACE in this ACL and the ACE is a permit
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosipacldscptrusted
            
            	If this attribute is true, then the Dscp associated with the packet is trusted, i.e., it is assumed to have already been set.  In this case, the Dscp is not rewritten with qosIpAclDscp (qosIpAclDscp is ignored).  The packet is still policed as part of its micro flow and its aggregate flow.  When a trusted action is applied to an input interface, the Dscp associated with the packet is the one contained in the packet.  When a trusted action is applied to an output interface, the Dscp associated with the packet is the one that is the result of the input classification and policing
            	**type**\:  bool
            
            .. attribute:: qosipaclinterfacedirection
            
            	The direction of packet flow at the interface in question to which this ACL applies
            	**type**\:   :py:class:`Qosipaclinterfacedirection <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry.Qosipaclinterfacedirection>`
            
            .. attribute:: qosipaclinterfaceroles
            
            	The interfaces to which this ACL applies specified in terms of a set of roles
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: qosipaclmicroflowpolicerid
            
            	An index identifying the instance of policer to apply to the microflow.  It must correspond to the integer index of an instance of class qosPolicerTableor be zero.  If zero, the microflow is not policed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosipaclorder
            
            	An integer that determines the order of this ACL in the list of ACLs applied to interfaces of the specified role combination. An ACL with a given order is positioned in the list before one with a higher order
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry, self).__init__()

                self.yang_name = "qosIpAclActionEntry"
                self.yang_parent_name = "qosIpAclActionTable"

                self.qosipaclactionid = YLeaf(YType.uint32, "qosIpAclActionId")

                self.qosipaclactaclid = YLeaf(YType.uint32, "qosIpAclActAclId")

                self.qosipaclaggregateid = YLeaf(YType.uint32, "qosIpAclAggregateId")

                self.qosipacldscp = YLeaf(YType.int32, "qosIpAclDscp")

                self.qosipacldscptrusted = YLeaf(YType.boolean, "qosIpAclDscpTrusted")

                self.qosipaclinterfacedirection = YLeaf(YType.enumeration, "qosIpAclInterfaceDirection")

                self.qosipaclinterfaceroles = YLeaf(YType.str, "qosIpAclInterfaceRoles")

                self.qosipaclmicroflowpolicerid = YLeaf(YType.uint32, "qosIpAclMicroFlowPolicerId")

                self.qosipaclorder = YLeaf(YType.uint32, "qosIpAclOrder")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosipaclactionid",
                                "qosipaclactaclid",
                                "qosipaclaggregateid",
                                "qosipacldscp",
                                "qosipacldscptrusted",
                                "qosipaclinterfacedirection",
                                "qosipaclinterfaceroles",
                                "qosipaclmicroflowpolicerid",
                                "qosipaclorder") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry, self).__setattr__(name, value)

            class Qosipaclinterfacedirection(Enum):
                """
                Qosipaclinterfacedirection

                The direction of packet flow at the interface in question to

                which this ACL applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = Enum.YLeaf(0, "in")

                out = Enum.YLeaf(1, "out")


            def has_data(self):
                return (
                    self.qosipaclactionid.is_set or
                    self.qosipaclactaclid.is_set or
                    self.qosipaclaggregateid.is_set or
                    self.qosipacldscp.is_set or
                    self.qosipacldscptrusted.is_set or
                    self.qosipaclinterfacedirection.is_set or
                    self.qosipaclinterfaceroles.is_set or
                    self.qosipaclmicroflowpolicerid.is_set or
                    self.qosipaclorder.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosipaclactionid.yfilter != YFilter.not_set or
                    self.qosipaclactaclid.yfilter != YFilter.not_set or
                    self.qosipaclaggregateid.yfilter != YFilter.not_set or
                    self.qosipacldscp.yfilter != YFilter.not_set or
                    self.qosipacldscptrusted.yfilter != YFilter.not_set or
                    self.qosipaclinterfacedirection.yfilter != YFilter.not_set or
                    self.qosipaclinterfaceroles.yfilter != YFilter.not_set or
                    self.qosipaclmicroflowpolicerid.yfilter != YFilter.not_set or
                    self.qosipaclorder.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIpAclActionEntry" + "[qosIpAclActionId='" + self.qosipaclactionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIpAclActionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosipaclactionid.is_set or self.qosipaclactionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclactionid.get_name_leafdata())
                if (self.qosipaclactaclid.is_set or self.qosipaclactaclid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclactaclid.get_name_leafdata())
                if (self.qosipaclaggregateid.is_set or self.qosipaclaggregateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclaggregateid.get_name_leafdata())
                if (self.qosipacldscp.is_set or self.qosipacldscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacldscp.get_name_leafdata())
                if (self.qosipacldscptrusted.is_set or self.qosipacldscptrusted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipacldscptrusted.get_name_leafdata())
                if (self.qosipaclinterfacedirection.is_set or self.qosipaclinterfacedirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclinterfacedirection.get_name_leafdata())
                if (self.qosipaclinterfaceroles.is_set or self.qosipaclinterfaceroles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclinterfaceroles.get_name_leafdata())
                if (self.qosipaclmicroflowpolicerid.is_set or self.qosipaclmicroflowpolicerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclmicroflowpolicerid.get_name_leafdata())
                if (self.qosipaclorder.is_set or self.qosipaclorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosipaclorder.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIpAclActionId" or name == "qosIpAclActAclId" or name == "qosIpAclAggregateId" or name == "qosIpAclDscp" or name == "qosIpAclDscpTrusted" or name == "qosIpAclInterfaceDirection" or name == "qosIpAclInterfaceRoles" or name == "qosIpAclMicroFlowPolicerId" or name == "qosIpAclOrder"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIpAclActionId"):
                    self.qosipaclactionid = value
                    self.qosipaclactionid.value_namespace = name_space
                    self.qosipaclactionid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclActAclId"):
                    self.qosipaclactaclid = value
                    self.qosipaclactaclid.value_namespace = name_space
                    self.qosipaclactaclid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclAggregateId"):
                    self.qosipaclaggregateid = value
                    self.qosipaclaggregateid.value_namespace = name_space
                    self.qosipaclaggregateid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclDscp"):
                    self.qosipacldscp = value
                    self.qosipacldscp.value_namespace = name_space
                    self.qosipacldscp.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclDscpTrusted"):
                    self.qosipacldscptrusted = value
                    self.qosipacldscptrusted.value_namespace = name_space
                    self.qosipacldscptrusted.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclInterfaceDirection"):
                    self.qosipaclinterfacedirection = value
                    self.qosipaclinterfacedirection.value_namespace = name_space
                    self.qosipaclinterfacedirection.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclInterfaceRoles"):
                    self.qosipaclinterfaceroles = value
                    self.qosipaclinterfaceroles.value_namespace = name_space
                    self.qosipaclinterfaceroles.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclMicroFlowPolicerId"):
                    self.qosipaclmicroflowpolicerid = value
                    self.qosipaclmicroflowpolicerid.value_namespace = name_space
                    self.qosipaclmicroflowpolicerid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIpAclOrder"):
                    self.qosipaclorder = value
                    self.qosipaclorder.value_namespace = name_space
                    self.qosipaclorder.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosipaclactionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosipaclactionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIpAclActionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIpAclActionEntry"):
                for c in self.qosipaclactionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosipaclactionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIpAclActionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosifschedulingpreferencestable(Entity):
        """
        This class specifies the scheduling preference an interface
        chooses if it supports multiple scheduling types.  Higher
        values are preferred over lower values.
        
        .. attribute:: qosifschedulingpreferenceentry
        
        	An instance of this class specifies a scheduling preference for a queue\-type on an interface with a particular role combination
        	**type**\: list of    :py:class:`Qosifschedulingpreferenceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosifschedulingpreferencestable, self).__init__()

            self.yang_name = "qosIfSchedulingPreferencesTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosifschedulingpreferenceentry = YList(self)

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
                        super(CiscoQosPibMib.Qosifschedulingpreferencestable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosifschedulingpreferencestable, self).__setattr__(name, value)


        class Qosifschedulingpreferenceentry(Entity):
            """
            An instance of this class specifies a scheduling preference
            for a queue\-type on an interface with a particular role
            combination.
            
            .. attribute:: qosifschedulingpreferenceid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifschedulingdiscipline
            
            	An enumerate type for all the known scheduling disciplines
            	**type**\:   :py:class:`Qosifschedulingdiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.Qosifschedulingdiscipline>`
            
            .. attribute:: qosifschedulingpreference
            
            	The preference to use this scheduling discipline and queue type.  A higher value means a higher preference.  If two disciplines have the same preference the choice is a local decision
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: qosifschedulingqueuetype
            
            	The queue type of this preference
            	**type**\:   :py:class:`Qosinterfacequeuetype <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Qosinterfacequeuetype>`
            
            .. attribute:: qosifschedulingroles
            
            	The combination of roles the interface must have for this policy instance to apply to that interface
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry, self).__init__()

                self.yang_name = "qosIfSchedulingPreferenceEntry"
                self.yang_parent_name = "qosIfSchedulingPreferencesTable"

                self.qosifschedulingpreferenceid = YLeaf(YType.uint32, "qosIfSchedulingPreferenceId")

                self.qosifschedulingdiscipline = YLeaf(YType.enumeration, "qosIfSchedulingDiscipline")

                self.qosifschedulingpreference = YLeaf(YType.int32, "qosIfSchedulingPreference")

                self.qosifschedulingqueuetype = YLeaf(YType.enumeration, "qosIfSchedulingQueueType")

                self.qosifschedulingroles = YLeaf(YType.str, "qosIfSchedulingRoles")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosifschedulingpreferenceid",
                                "qosifschedulingdiscipline",
                                "qosifschedulingpreference",
                                "qosifschedulingqueuetype",
                                "qosifschedulingroles") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry, self).__setattr__(name, value)

            class Qosifschedulingdiscipline(Enum):
                """
                Qosifschedulingdiscipline

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


            def has_data(self):
                return (
                    self.qosifschedulingpreferenceid.is_set or
                    self.qosifschedulingdiscipline.is_set or
                    self.qosifschedulingpreference.is_set or
                    self.qosifschedulingqueuetype.is_set or
                    self.qosifschedulingroles.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosifschedulingpreferenceid.yfilter != YFilter.not_set or
                    self.qosifschedulingdiscipline.yfilter != YFilter.not_set or
                    self.qosifschedulingpreference.yfilter != YFilter.not_set or
                    self.qosifschedulingqueuetype.yfilter != YFilter.not_set or
                    self.qosifschedulingroles.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfSchedulingPreferenceEntry" + "[qosIfSchedulingPreferenceId='" + self.qosifschedulingpreferenceid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfSchedulingPreferencesTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosifschedulingpreferenceid.is_set or self.qosifschedulingpreferenceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifschedulingpreferenceid.get_name_leafdata())
                if (self.qosifschedulingdiscipline.is_set or self.qosifschedulingdiscipline.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifschedulingdiscipline.get_name_leafdata())
                if (self.qosifschedulingpreference.is_set or self.qosifschedulingpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifschedulingpreference.get_name_leafdata())
                if (self.qosifschedulingqueuetype.is_set or self.qosifschedulingqueuetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifschedulingqueuetype.get_name_leafdata())
                if (self.qosifschedulingroles.is_set or self.qosifschedulingroles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifschedulingroles.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfSchedulingPreferenceId" or name == "qosIfSchedulingDiscipline" or name == "qosIfSchedulingPreference" or name == "qosIfSchedulingQueueType" or name == "qosIfSchedulingRoles"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfSchedulingPreferenceId"):
                    self.qosifschedulingpreferenceid = value
                    self.qosifschedulingpreferenceid.value_namespace = name_space
                    self.qosifschedulingpreferenceid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfSchedulingDiscipline"):
                    self.qosifschedulingdiscipline = value
                    self.qosifschedulingdiscipline.value_namespace = name_space
                    self.qosifschedulingdiscipline.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfSchedulingPreference"):
                    self.qosifschedulingpreference = value
                    self.qosifschedulingpreference.value_namespace = name_space
                    self.qosifschedulingpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfSchedulingQueueType"):
                    self.qosifschedulingqueuetype = value
                    self.qosifschedulingqueuetype.value_namespace = name_space
                    self.qosifschedulingqueuetype.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfSchedulingRoles"):
                    self.qosifschedulingroles = value
                    self.qosifschedulingroles.value_namespace = name_space
                    self.qosifschedulingroles.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosifschedulingpreferenceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosifschedulingpreferenceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfSchedulingPreferencesTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfSchedulingPreferenceEntry"):
                for c in self.qosifschedulingpreferenceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosifschedulingpreferenceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfSchedulingPreferenceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosifdroppreferencetable(Entity):
        """
        This class specifies the preference of the drop mechanism an
        interface chooses if it supports multiple drop mechanisms.
        Higher values are preferred over lower values.
        
        .. attribute:: qosifdroppreferenceentry
        
        	An instance of this class specifies a drop preference for a drop mechanism on an interface with a particular role combination
        	**type**\: list of    :py:class:`Qosifdroppreferenceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosifdroppreferencetable, self).__init__()

            self.yang_name = "qosIfDropPreferenceTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosifdroppreferenceentry = YList(self)

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
                        super(CiscoQosPibMib.Qosifdroppreferencetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosifdroppreferencetable, self).__setattr__(name, value)


        class Qosifdroppreferenceentry(Entity):
            """
            An instance of this class specifies a drop preference for
            a drop mechanism on an interface with a particular role
            combination.
            
            .. attribute:: qosifdroppreferenceid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifdropdiscipline
            
            	An enumerate type for all the known drop mechanisms
            	**type**\:   :py:class:`Qosifdropdiscipline <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry.Qosifdropdiscipline>`
            
            .. attribute:: qosifdroppreference
            
            	The preference to use this drop mechanism.  A higher value means a higher preference.  If two mechanisms have the same preference the choice is a local decision
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: qosifdroproles
            
            	The combination of roles the interface must have for this policy instance to apply to that interface
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry, self).__init__()

                self.yang_name = "qosIfDropPreferenceEntry"
                self.yang_parent_name = "qosIfDropPreferenceTable"

                self.qosifdroppreferenceid = YLeaf(YType.uint32, "qosIfDropPreferenceId")

                self.qosifdropdiscipline = YLeaf(YType.enumeration, "qosIfDropDiscipline")

                self.qosifdroppreference = YLeaf(YType.int32, "qosIfDropPreference")

                self.qosifdroproles = YLeaf(YType.str, "qosIfDropRoles")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosifdroppreferenceid",
                                "qosifdropdiscipline",
                                "qosifdroppreference",
                                "qosifdroproles") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry, self).__setattr__(name, value)

            class Qosifdropdiscipline(Enum):
                """
                Qosifdropdiscipline

                An enumerate type for all the known drop mechanisms.

                .. data:: qosIfDropWRED = 1

                .. data:: qosIfDropTailDrop = 2

                """

                qosIfDropWRED = Enum.YLeaf(1, "qosIfDropWRED")

                qosIfDropTailDrop = Enum.YLeaf(2, "qosIfDropTailDrop")


            def has_data(self):
                return (
                    self.qosifdroppreferenceid.is_set or
                    self.qosifdropdiscipline.is_set or
                    self.qosifdroppreference.is_set or
                    self.qosifdroproles.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosifdroppreferenceid.yfilter != YFilter.not_set or
                    self.qosifdropdiscipline.yfilter != YFilter.not_set or
                    self.qosifdroppreference.yfilter != YFilter.not_set or
                    self.qosifdroproles.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfDropPreferenceEntry" + "[qosIfDropPreferenceId='" + self.qosifdroppreferenceid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfDropPreferenceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosifdroppreferenceid.is_set or self.qosifdroppreferenceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdroppreferenceid.get_name_leafdata())
                if (self.qosifdropdiscipline.is_set or self.qosifdropdiscipline.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdropdiscipline.get_name_leafdata())
                if (self.qosifdroppreference.is_set or self.qosifdroppreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdroppreference.get_name_leafdata())
                if (self.qosifdroproles.is_set or self.qosifdroproles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdroproles.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfDropPreferenceId" or name == "qosIfDropDiscipline" or name == "qosIfDropPreference" or name == "qosIfDropRoles"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfDropPreferenceId"):
                    self.qosifdroppreferenceid = value
                    self.qosifdroppreferenceid.value_namespace = name_space
                    self.qosifdroppreferenceid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfDropDiscipline"):
                    self.qosifdropdiscipline = value
                    self.qosifdropdiscipline.value_namespace = name_space
                    self.qosifdropdiscipline.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfDropPreference"):
                    self.qosifdroppreference = value
                    self.qosifdroppreference.value_namespace = name_space
                    self.qosifdroppreference.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfDropRoles"):
                    self.qosifdroproles = value
                    self.qosifdroproles.value_namespace = name_space
                    self.qosifdroproles.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosifdroppreferenceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosifdroppreferenceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfDropPreferenceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfDropPreferenceEntry"):
                for c in self.qosifdroppreferenceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosifdroppreferenceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfDropPreferenceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qosifdscpassignmenttable(Entity):
        """
        The assignment of each DSCP to a queue and threshold for each
        interface queue type.
        
        .. attribute:: qosifdscpassignmententry
        
        	An instance of this class specifies the queue and threshold set for a packet with a particular DSCP on an interface of a particular type with a particular role combination
        	**type**\: list of    :py:class:`Qosifdscpassignmententry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosifdscpassignmenttable, self).__init__()

            self.yang_name = "qosIfDscpAssignmentTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosifdscpassignmententry = YList(self)

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
                        super(CiscoQosPibMib.Qosifdscpassignmenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosifdscpassignmenttable, self).__setattr__(name, value)


        class Qosifdscpassignmententry(Entity):
            """
            An instance of this class specifies the queue and threshold
            set for a packet with a particular DSCP on an interface of
            a particular type with a particular role combination.
            
            .. attribute:: qosifdscpassignmentid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifdscp
            
            	The DSCP to which this row applies
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: qosifdscproles
            
            	The role combination the interface must be configured with
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: qosifqueue
            
            	The queue to which the DSCP applies for the given interface type
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: qosifqueuetype
            
            	The interface queue type to which this row applies
            	**type**\:   :py:class:`Qosinterfacequeuetype <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Qosinterfacequeuetype>`
            
            .. attribute:: qosifthresholdset
            
            	The threshold set of the specified queue to which the DSCP applies for the given interface type
            	**type**\:  int
            
            	**range:** 1..8
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry, self).__init__()

                self.yang_name = "qosIfDscpAssignmentEntry"
                self.yang_parent_name = "qosIfDscpAssignmentTable"

                self.qosifdscpassignmentid = YLeaf(YType.uint32, "qosIfDscpAssignmentId")

                self.qosifdscp = YLeaf(YType.int32, "qosIfDscp")

                self.qosifdscproles = YLeaf(YType.str, "qosIfDscpRoles")

                self.qosifqueue = YLeaf(YType.int32, "qosIfQueue")

                self.qosifqueuetype = YLeaf(YType.enumeration, "qosIfQueueType")

                self.qosifthresholdset = YLeaf(YType.int32, "qosIfThresholdSet")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosifdscpassignmentid",
                                "qosifdscp",
                                "qosifdscproles",
                                "qosifqueue",
                                "qosifqueuetype",
                                "qosifthresholdset") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosifdscpassignmentid.is_set or
                    self.qosifdscp.is_set or
                    self.qosifdscproles.is_set or
                    self.qosifqueue.is_set or
                    self.qosifqueuetype.is_set or
                    self.qosifthresholdset.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosifdscpassignmentid.yfilter != YFilter.not_set or
                    self.qosifdscp.yfilter != YFilter.not_set or
                    self.qosifdscproles.yfilter != YFilter.not_set or
                    self.qosifqueue.yfilter != YFilter.not_set or
                    self.qosifqueuetype.yfilter != YFilter.not_set or
                    self.qosifthresholdset.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfDscpAssignmentEntry" + "[qosIfDscpAssignmentId='" + self.qosifdscpassignmentid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfDscpAssignmentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosifdscpassignmentid.is_set or self.qosifdscpassignmentid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdscpassignmentid.get_name_leafdata())
                if (self.qosifdscp.is_set or self.qosifdscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdscp.get_name_leafdata())
                if (self.qosifdscproles.is_set or self.qosifdscproles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifdscproles.get_name_leafdata())
                if (self.qosifqueue.is_set or self.qosifqueue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifqueue.get_name_leafdata())
                if (self.qosifqueuetype.is_set or self.qosifqueuetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifqueuetype.get_name_leafdata())
                if (self.qosifthresholdset.is_set or self.qosifthresholdset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifthresholdset.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfDscpAssignmentId" or name == "qosIfDscp" or name == "qosIfDscpRoles" or name == "qosIfQueue" or name == "qosIfQueueType" or name == "qosIfThresholdSet"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfDscpAssignmentId"):
                    self.qosifdscpassignmentid = value
                    self.qosifdscpassignmentid.value_namespace = name_space
                    self.qosifdscpassignmentid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfDscp"):
                    self.qosifdscp = value
                    self.qosifdscp.value_namespace = name_space
                    self.qosifdscp.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfDscpRoles"):
                    self.qosifdscproles = value
                    self.qosifdscproles.value_namespace = name_space
                    self.qosifdscproles.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfQueue"):
                    self.qosifqueue = value
                    self.qosifqueue.value_namespace = name_space
                    self.qosifqueue.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfQueueType"):
                    self.qosifqueuetype = value
                    self.qosifqueuetype.value_namespace = name_space
                    self.qosifqueuetype.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfThresholdSet"):
                    self.qosifthresholdset = value
                    self.qosifthresholdset.value_namespace = name_space
                    self.qosifthresholdset.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosifdscpassignmententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosifdscpassignmententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfDscpAssignmentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfDscpAssignmentEntry"):
                for c in self.qosifdscpassignmententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosifdscpassignmententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfDscpAssignmentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosifredentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifredtable.Qosifredentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosifredtable, self).__init__()

            self.yang_name = "qosIfRedTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosifredentry = YList(self)

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
                        super(CiscoQosPibMib.Qosifredtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosifredtable, self).__setattr__(name, value)


        class Qosifredentry(Entity):
            """
            An instance of this class specifies threshold limits for a
            particular RED threshold of a given threshold set on an
            interface and with a particular role combination.
            
            .. attribute:: qosifredid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifrednumthresholdsets
            
            	The values in this entry apply only to queues with the number of thresholds specified by this attribute
            	**type**\:   :py:class:`Thresholdsetrange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Thresholdsetrange>`
            
            .. attribute:: qosifredroles
            
            	The role combination the interface must be configured with
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: qosifredthresholdset
            
            	The threshold set to which the lower and upper values apply. It must be in the range 1 through qosIfRedNumThresholdSets. There must be exactly one PRI for each value in this range
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: qosifredthresholdsetlower
            
            	The threshold value below which no packets are dropped
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: qosifredthresholdsetupper
            
            	The threshold value above which all packets are dropped
            	**type**\:  int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosifredtable.Qosifredentry, self).__init__()

                self.yang_name = "qosIfRedEntry"
                self.yang_parent_name = "qosIfRedTable"

                self.qosifredid = YLeaf(YType.uint32, "qosIfRedId")

                self.qosifrednumthresholdsets = YLeaf(YType.enumeration, "qosIfRedNumThresholdSets")

                self.qosifredroles = YLeaf(YType.str, "qosIfRedRoles")

                self.qosifredthresholdset = YLeaf(YType.int32, "qosIfRedThresholdSet")

                self.qosifredthresholdsetlower = YLeaf(YType.int32, "qosIfRedThresholdSetLower")

                self.qosifredthresholdsetupper = YLeaf(YType.int32, "qosIfRedThresholdSetUpper")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosifredid",
                                "qosifrednumthresholdsets",
                                "qosifredroles",
                                "qosifredthresholdset",
                                "qosifredthresholdsetlower",
                                "qosifredthresholdsetupper") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosifredtable.Qosifredentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosifredtable.Qosifredentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosifredid.is_set or
                    self.qosifrednumthresholdsets.is_set or
                    self.qosifredroles.is_set or
                    self.qosifredthresholdset.is_set or
                    self.qosifredthresholdsetlower.is_set or
                    self.qosifredthresholdsetupper.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosifredid.yfilter != YFilter.not_set or
                    self.qosifrednumthresholdsets.yfilter != YFilter.not_set or
                    self.qosifredroles.yfilter != YFilter.not_set or
                    self.qosifredthresholdset.yfilter != YFilter.not_set or
                    self.qosifredthresholdsetlower.yfilter != YFilter.not_set or
                    self.qosifredthresholdsetupper.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfRedEntry" + "[qosIfRedId='" + self.qosifredid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfRedTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosifredid.is_set or self.qosifredid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifredid.get_name_leafdata())
                if (self.qosifrednumthresholdsets.is_set or self.qosifrednumthresholdsets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifrednumthresholdsets.get_name_leafdata())
                if (self.qosifredroles.is_set or self.qosifredroles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifredroles.get_name_leafdata())
                if (self.qosifredthresholdset.is_set or self.qosifredthresholdset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifredthresholdset.get_name_leafdata())
                if (self.qosifredthresholdsetlower.is_set or self.qosifredthresholdsetlower.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifredthresholdsetlower.get_name_leafdata())
                if (self.qosifredthresholdsetupper.is_set or self.qosifredthresholdsetupper.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifredthresholdsetupper.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfRedId" or name == "qosIfRedNumThresholdSets" or name == "qosIfRedRoles" or name == "qosIfRedThresholdSet" or name == "qosIfRedThresholdSetLower" or name == "qosIfRedThresholdSetUpper"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfRedId"):
                    self.qosifredid = value
                    self.qosifredid.value_namespace = name_space
                    self.qosifredid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfRedNumThresholdSets"):
                    self.qosifrednumthresholdsets = value
                    self.qosifrednumthresholdsets.value_namespace = name_space
                    self.qosifrednumthresholdsets.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfRedRoles"):
                    self.qosifredroles = value
                    self.qosifredroles.value_namespace = name_space
                    self.qosifredroles.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfRedThresholdSet"):
                    self.qosifredthresholdset = value
                    self.qosifredthresholdset.value_namespace = name_space
                    self.qosifredthresholdset.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfRedThresholdSetLower"):
                    self.qosifredthresholdsetlower = value
                    self.qosifredthresholdsetlower.value_namespace = name_space
                    self.qosifredthresholdsetlower.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfRedThresholdSetUpper"):
                    self.qosifredthresholdsetupper = value
                    self.qosifredthresholdsetupper.value_namespace = name_space
                    self.qosifredthresholdsetupper.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosifredentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosifredentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfRedTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfRedEntry"):
                for c in self.qosifredentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosifredtable.Qosifredentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosifredentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfRedEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosiftaildropentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosiftaildroptable, self).__init__()

            self.yang_name = "qosIfTailDropTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosiftaildropentry = YList(self)

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
                        super(CiscoQosPibMib.Qosiftaildroptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosiftaildroptable, self).__setattr__(name, value)


        class Qosiftaildropentry(Entity):
            """
            An instance of this class specifies the queue depth for a
            particular tail\-drop threshold set on an interface with a
            particular role combination.
            
            .. attribute:: qosiftaildropid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosiftaildropnumthresholdsets
            
            	The value in this entry applies only to queues with the number of thresholds specified by this attribute
            	**type**\:   :py:class:`Thresholdsetrange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Thresholdsetrange>`
            
            .. attribute:: qosiftaildroproles
            
            	The role combination the interface must be configured with
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: qosiftaildropthresholdset
            
            	The threshold set to which the threshold value applies
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: qosiftaildropthresholdsetvalue
            
            	The threshold value above which packets are dropped
            	**type**\:  int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry, self).__init__()

                self.yang_name = "qosIfTailDropEntry"
                self.yang_parent_name = "qosIfTailDropTable"

                self.qosiftaildropid = YLeaf(YType.uint32, "qosIfTailDropId")

                self.qosiftaildropnumthresholdsets = YLeaf(YType.enumeration, "qosIfTailDropNumThresholdSets")

                self.qosiftaildroproles = YLeaf(YType.str, "qosIfTailDropRoles")

                self.qosiftaildropthresholdset = YLeaf(YType.int32, "qosIfTailDropThresholdSet")

                self.qosiftaildropthresholdsetvalue = YLeaf(YType.int32, "qosIfTailDropThresholdSetValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosiftaildropid",
                                "qosiftaildropnumthresholdsets",
                                "qosiftaildroproles",
                                "qosiftaildropthresholdset",
                                "qosiftaildropthresholdsetvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosiftaildropid.is_set or
                    self.qosiftaildropnumthresholdsets.is_set or
                    self.qosiftaildroproles.is_set or
                    self.qosiftaildropthresholdset.is_set or
                    self.qosiftaildropthresholdsetvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosiftaildropid.yfilter != YFilter.not_set or
                    self.qosiftaildropnumthresholdsets.yfilter != YFilter.not_set or
                    self.qosiftaildroproles.yfilter != YFilter.not_set or
                    self.qosiftaildropthresholdset.yfilter != YFilter.not_set or
                    self.qosiftaildropthresholdsetvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfTailDropEntry" + "[qosIfTailDropId='" + self.qosiftaildropid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfTailDropTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosiftaildropid.is_set or self.qosiftaildropid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosiftaildropid.get_name_leafdata())
                if (self.qosiftaildropnumthresholdsets.is_set or self.qosiftaildropnumthresholdsets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosiftaildropnumthresholdsets.get_name_leafdata())
                if (self.qosiftaildroproles.is_set or self.qosiftaildroproles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosiftaildroproles.get_name_leafdata())
                if (self.qosiftaildropthresholdset.is_set or self.qosiftaildropthresholdset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosiftaildropthresholdset.get_name_leafdata())
                if (self.qosiftaildropthresholdsetvalue.is_set or self.qosiftaildropthresholdsetvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosiftaildropthresholdsetvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfTailDropId" or name == "qosIfTailDropNumThresholdSets" or name == "qosIfTailDropRoles" or name == "qosIfTailDropThresholdSet" or name == "qosIfTailDropThresholdSetValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfTailDropId"):
                    self.qosiftaildropid = value
                    self.qosiftaildropid.value_namespace = name_space
                    self.qosiftaildropid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfTailDropNumThresholdSets"):
                    self.qosiftaildropnumthresholdsets = value
                    self.qosiftaildropnumthresholdsets.value_namespace = name_space
                    self.qosiftaildropnumthresholdsets.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfTailDropRoles"):
                    self.qosiftaildroproles = value
                    self.qosiftaildroproles.value_namespace = name_space
                    self.qosiftaildroproles.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfTailDropThresholdSet"):
                    self.qosiftaildropthresholdset = value
                    self.qosiftaildropthresholdset.value_namespace = name_space
                    self.qosiftaildropthresholdset.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfTailDropThresholdSetValue"):
                    self.qosiftaildropthresholdsetvalue = value
                    self.qosiftaildropthresholdsetvalue.value_namespace = name_space
                    self.qosiftaildropthresholdsetvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosiftaildropentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosiftaildropentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfTailDropTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfTailDropEntry"):
                for c in self.qosiftaildropentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosiftaildropentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfTailDropEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Qosifweightsentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifweightstable.Qosifweightsentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            super(CiscoQosPibMib.Qosifweightstable, self).__init__()

            self.yang_name = "qosIfWeightsTable"
            self.yang_parent_name = "CISCO-QOS-PIB-MIB"

            self.qosifweightsentry = YList(self)

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
                        super(CiscoQosPibMib.Qosifweightstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoQosPibMib.Qosifweightstable, self).__setattr__(name, value)


        class Qosifweightsentry(Entity):
            """
            An instance of this class specifies the scheduling weight for
            a particular queue of an interface with a particular number
            of queues and with a particular role combination.
            
            .. attribute:: qosifweightsid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifweightsdrainsize
            
            	The maximum number of bytes that may be drained from the queue in one cycle.  The percentage of the bandwith allocated to this queue can be calculated from this attribute and the sum of the drain sizes of all the non\-priority queues of the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifweightsnumqueues
            
            	The value of the weight in this instance applies only to interfaces with the number of queues specified by this attribute
            	**type**\:   :py:class:`Queuerange <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.Queuerange>`
            
            .. attribute:: qosifweightsqueue
            
            	The queue to which the weight applies
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: qosifweightsqueuesize
            
            	The size of the queue in bytes.  Some devices set queue size in terms of packets.  These devices must calculate the queue size in packets by assuming an average packet size suitable for the particular interface.  Some devices have a fixed size buffer to be shared among all queues.  These devices must allocate a fraction of the total buffer space to this queue calculated as the the ratio of the queue size to the sum of the queue sizes for the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosifweightsroles
            
            	The role combination the interface must be configured with
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                super(CiscoQosPibMib.Qosifweightstable.Qosifweightsentry, self).__init__()

                self.yang_name = "qosIfWeightsEntry"
                self.yang_parent_name = "qosIfWeightsTable"

                self.qosifweightsid = YLeaf(YType.uint32, "qosIfWeightsId")

                self.qosifweightsdrainsize = YLeaf(YType.uint32, "qosIfWeightsDrainSize")

                self.qosifweightsnumqueues = YLeaf(YType.enumeration, "qosIfWeightsNumQueues")

                self.qosifweightsqueue = YLeaf(YType.int32, "qosIfWeightsQueue")

                self.qosifweightsqueuesize = YLeaf(YType.uint32, "qosIfWeightsQueueSize")

                self.qosifweightsroles = YLeaf(YType.str, "qosIfWeightsRoles")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("qosifweightsid",
                                "qosifweightsdrainsize",
                                "qosifweightsnumqueues",
                                "qosifweightsqueue",
                                "qosifweightsqueuesize",
                                "qosifweightsroles") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoQosPibMib.Qosifweightstable.Qosifweightsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoQosPibMib.Qosifweightstable.Qosifweightsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.qosifweightsid.is_set or
                    self.qosifweightsdrainsize.is_set or
                    self.qosifweightsnumqueues.is_set or
                    self.qosifweightsqueue.is_set or
                    self.qosifweightsqueuesize.is_set or
                    self.qosifweightsroles.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.qosifweightsid.yfilter != YFilter.not_set or
                    self.qosifweightsdrainsize.yfilter != YFilter.not_set or
                    self.qosifweightsnumqueues.yfilter != YFilter.not_set or
                    self.qosifweightsqueue.yfilter != YFilter.not_set or
                    self.qosifweightsqueuesize.yfilter != YFilter.not_set or
                    self.qosifweightsroles.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qosIfWeightsEntry" + "[qosIfWeightsId='" + self.qosifweightsid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/qosIfWeightsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.qosifweightsid.is_set or self.qosifweightsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsid.get_name_leafdata())
                if (self.qosifweightsdrainsize.is_set or self.qosifweightsdrainsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsdrainsize.get_name_leafdata())
                if (self.qosifweightsnumqueues.is_set or self.qosifweightsnumqueues.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsnumqueues.get_name_leafdata())
                if (self.qosifweightsqueue.is_set or self.qosifweightsqueue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsqueue.get_name_leafdata())
                if (self.qosifweightsqueuesize.is_set or self.qosifweightsqueuesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsqueuesize.get_name_leafdata())
                if (self.qosifweightsroles.is_set or self.qosifweightsroles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qosifweightsroles.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "qosIfWeightsId" or name == "qosIfWeightsDrainSize" or name == "qosIfWeightsNumQueues" or name == "qosIfWeightsQueue" or name == "qosIfWeightsQueueSize" or name == "qosIfWeightsRoles"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "qosIfWeightsId"):
                    self.qosifweightsid = value
                    self.qosifweightsid.value_namespace = name_space
                    self.qosifweightsid.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfWeightsDrainSize"):
                    self.qosifweightsdrainsize = value
                    self.qosifweightsdrainsize.value_namespace = name_space
                    self.qosifweightsdrainsize.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfWeightsNumQueues"):
                    self.qosifweightsnumqueues = value
                    self.qosifweightsnumqueues.value_namespace = name_space
                    self.qosifweightsnumqueues.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfWeightsQueue"):
                    self.qosifweightsqueue = value
                    self.qosifweightsqueue.value_namespace = name_space
                    self.qosifweightsqueue.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfWeightsQueueSize"):
                    self.qosifweightsqueuesize = value
                    self.qosifweightsqueuesize.value_namespace = name_space
                    self.qosifweightsqueuesize.value_namespace_prefix = name_space_prefix
                if(value_path == "qosIfWeightsRoles"):
                    self.qosifweightsroles = value
                    self.qosifweightsroles.value_namespace = name_space
                    self.qosifweightsroles.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.qosifweightsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.qosifweightsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qosIfWeightsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qosIfWeightsEntry"):
                for c in self.qosifweightsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoQosPibMib.Qosifweightstable.Qosifweightsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.qosifweightsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qosIfWeightsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.qosaggregatetable is not None and self.qosaggregatetable.has_data()) or
            (self.qoscostodscptable is not None and self.qoscostodscptable.has_data()) or
            (self.qosdeviceattributetable is not None and self.qosdeviceattributetable.has_data()) or
            (self.qosdevicepibincarnationtable is not None and self.qosdevicepibincarnationtable.has_data()) or
            (self.qosdiffservmappingtable is not None and self.qosdiffservmappingtable.has_data()) or
            (self.qosifdroppreferencetable is not None and self.qosifdroppreferencetable.has_data()) or
            (self.qosifdscpassignmenttable is not None and self.qosifdscpassignmenttable.has_data()) or
            (self.qosifredtable is not None and self.qosifredtable.has_data()) or
            (self.qosifschedulingpreferencestable is not None and self.qosifschedulingpreferencestable.has_data()) or
            (self.qosiftaildroptable is not None and self.qosiftaildroptable.has_data()) or
            (self.qosifweightstable is not None and self.qosifweightstable.has_data()) or
            (self.qosinterfacetypetable is not None and self.qosinterfacetypetable.has_data()) or
            (self.qosipacetable is not None and self.qosipacetable.has_data()) or
            (self.qosipaclactiontable is not None and self.qosipaclactiontable.has_data()) or
            (self.qosipacldefinitiontable is not None and self.qosipacldefinitiontable.has_data()) or
            (self.qosmacclassificationtable is not None and self.qosmacclassificationtable.has_data()) or
            (self.qospolicertable is not None and self.qospolicertable.has_data()) or
            (self.qosunmatchedpolicytable is not None and self.qosunmatchedpolicytable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.qosaggregatetable is not None and self.qosaggregatetable.has_operation()) or
            (self.qoscostodscptable is not None and self.qoscostodscptable.has_operation()) or
            (self.qosdeviceattributetable is not None and self.qosdeviceattributetable.has_operation()) or
            (self.qosdevicepibincarnationtable is not None and self.qosdevicepibincarnationtable.has_operation()) or
            (self.qosdiffservmappingtable is not None and self.qosdiffservmappingtable.has_operation()) or
            (self.qosifdroppreferencetable is not None and self.qosifdroppreferencetable.has_operation()) or
            (self.qosifdscpassignmenttable is not None and self.qosifdscpassignmenttable.has_operation()) or
            (self.qosifredtable is not None and self.qosifredtable.has_operation()) or
            (self.qosifschedulingpreferencestable is not None and self.qosifschedulingpreferencestable.has_operation()) or
            (self.qosiftaildroptable is not None and self.qosiftaildroptable.has_operation()) or
            (self.qosifweightstable is not None and self.qosifweightstable.has_operation()) or
            (self.qosinterfacetypetable is not None and self.qosinterfacetypetable.has_operation()) or
            (self.qosipacetable is not None and self.qosipacetable.has_operation()) or
            (self.qosipaclactiontable is not None and self.qosipaclactiontable.has_operation()) or
            (self.qosipacldefinitiontable is not None and self.qosipacldefinitiontable.has_operation()) or
            (self.qosmacclassificationtable is not None and self.qosmacclassificationtable.has_operation()) or
            (self.qospolicertable is not None and self.qospolicertable.has_operation()) or
            (self.qosunmatchedpolicytable is not None and self.qosunmatchedpolicytable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB" + path_buffer

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

        if (child_yang_name == "qosAggregateTable"):
            if (self.qosaggregatetable is None):
                self.qosaggregatetable = CiscoQosPibMib.Qosaggregatetable()
                self.qosaggregatetable.parent = self
                self._children_name_map["qosaggregatetable"] = "qosAggregateTable"
            return self.qosaggregatetable

        if (child_yang_name == "qosCosToDscpTable"):
            if (self.qoscostodscptable is None):
                self.qoscostodscptable = CiscoQosPibMib.Qoscostodscptable()
                self.qoscostodscptable.parent = self
                self._children_name_map["qoscostodscptable"] = "qosCosToDscpTable"
            return self.qoscostodscptable

        if (child_yang_name == "qosDeviceAttributeTable"):
            if (self.qosdeviceattributetable is None):
                self.qosdeviceattributetable = CiscoQosPibMib.Qosdeviceattributetable()
                self.qosdeviceattributetable.parent = self
                self._children_name_map["qosdeviceattributetable"] = "qosDeviceAttributeTable"
            return self.qosdeviceattributetable

        if (child_yang_name == "qosDevicePibIncarnationTable"):
            if (self.qosdevicepibincarnationtable is None):
                self.qosdevicepibincarnationtable = CiscoQosPibMib.Qosdevicepibincarnationtable()
                self.qosdevicepibincarnationtable.parent = self
                self._children_name_map["qosdevicepibincarnationtable"] = "qosDevicePibIncarnationTable"
            return self.qosdevicepibincarnationtable

        if (child_yang_name == "qosDiffServMappingTable"):
            if (self.qosdiffservmappingtable is None):
                self.qosdiffservmappingtable = CiscoQosPibMib.Qosdiffservmappingtable()
                self.qosdiffservmappingtable.parent = self
                self._children_name_map["qosdiffservmappingtable"] = "qosDiffServMappingTable"
            return self.qosdiffservmappingtable

        if (child_yang_name == "qosIfDropPreferenceTable"):
            if (self.qosifdroppreferencetable is None):
                self.qosifdroppreferencetable = CiscoQosPibMib.Qosifdroppreferencetable()
                self.qosifdroppreferencetable.parent = self
                self._children_name_map["qosifdroppreferencetable"] = "qosIfDropPreferenceTable"
            return self.qosifdroppreferencetable

        if (child_yang_name == "qosIfDscpAssignmentTable"):
            if (self.qosifdscpassignmenttable is None):
                self.qosifdscpassignmenttable = CiscoQosPibMib.Qosifdscpassignmenttable()
                self.qosifdscpassignmenttable.parent = self
                self._children_name_map["qosifdscpassignmenttable"] = "qosIfDscpAssignmentTable"
            return self.qosifdscpassignmenttable

        if (child_yang_name == "qosIfRedTable"):
            if (self.qosifredtable is None):
                self.qosifredtable = CiscoQosPibMib.Qosifredtable()
                self.qosifredtable.parent = self
                self._children_name_map["qosifredtable"] = "qosIfRedTable"
            return self.qosifredtable

        if (child_yang_name == "qosIfSchedulingPreferencesTable"):
            if (self.qosifschedulingpreferencestable is None):
                self.qosifschedulingpreferencestable = CiscoQosPibMib.Qosifschedulingpreferencestable()
                self.qosifschedulingpreferencestable.parent = self
                self._children_name_map["qosifschedulingpreferencestable"] = "qosIfSchedulingPreferencesTable"
            return self.qosifschedulingpreferencestable

        if (child_yang_name == "qosIfTailDropTable"):
            if (self.qosiftaildroptable is None):
                self.qosiftaildroptable = CiscoQosPibMib.Qosiftaildroptable()
                self.qosiftaildroptable.parent = self
                self._children_name_map["qosiftaildroptable"] = "qosIfTailDropTable"
            return self.qosiftaildroptable

        if (child_yang_name == "qosIfWeightsTable"):
            if (self.qosifweightstable is None):
                self.qosifweightstable = CiscoQosPibMib.Qosifweightstable()
                self.qosifweightstable.parent = self
                self._children_name_map["qosifweightstable"] = "qosIfWeightsTable"
            return self.qosifweightstable

        if (child_yang_name == "qosInterfaceTypeTable"):
            if (self.qosinterfacetypetable is None):
                self.qosinterfacetypetable = CiscoQosPibMib.Qosinterfacetypetable()
                self.qosinterfacetypetable.parent = self
                self._children_name_map["qosinterfacetypetable"] = "qosInterfaceTypeTable"
            return self.qosinterfacetypetable

        if (child_yang_name == "qosIpAceTable"):
            if (self.qosipacetable is None):
                self.qosipacetable = CiscoQosPibMib.Qosipacetable()
                self.qosipacetable.parent = self
                self._children_name_map["qosipacetable"] = "qosIpAceTable"
            return self.qosipacetable

        if (child_yang_name == "qosIpAclActionTable"):
            if (self.qosipaclactiontable is None):
                self.qosipaclactiontable = CiscoQosPibMib.Qosipaclactiontable()
                self.qosipaclactiontable.parent = self
                self._children_name_map["qosipaclactiontable"] = "qosIpAclActionTable"
            return self.qosipaclactiontable

        if (child_yang_name == "qosIpAclDefinitionTable"):
            if (self.qosipacldefinitiontable is None):
                self.qosipacldefinitiontable = CiscoQosPibMib.Qosipacldefinitiontable()
                self.qosipacldefinitiontable.parent = self
                self._children_name_map["qosipacldefinitiontable"] = "qosIpAclDefinitionTable"
            return self.qosipacldefinitiontable

        if (child_yang_name == "qosMacClassificationTable"):
            if (self.qosmacclassificationtable is None):
                self.qosmacclassificationtable = CiscoQosPibMib.Qosmacclassificationtable()
                self.qosmacclassificationtable.parent = self
                self._children_name_map["qosmacclassificationtable"] = "qosMacClassificationTable"
            return self.qosmacclassificationtable

        if (child_yang_name == "qosPolicerTable"):
            if (self.qospolicertable is None):
                self.qospolicertable = CiscoQosPibMib.Qospolicertable()
                self.qospolicertable.parent = self
                self._children_name_map["qospolicertable"] = "qosPolicerTable"
            return self.qospolicertable

        if (child_yang_name == "qosUnmatchedPolicyTable"):
            if (self.qosunmatchedpolicytable is None):
                self.qosunmatchedpolicytable = CiscoQosPibMib.Qosunmatchedpolicytable()
                self.qosunmatchedpolicytable.parent = self
                self._children_name_map["qosunmatchedpolicytable"] = "qosUnmatchedPolicyTable"
            return self.qosunmatchedpolicytable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "qosAggregateTable" or name == "qosCosToDscpTable" or name == "qosDeviceAttributeTable" or name == "qosDevicePibIncarnationTable" or name == "qosDiffServMappingTable" or name == "qosIfDropPreferenceTable" or name == "qosIfDscpAssignmentTable" or name == "qosIfRedTable" or name == "qosIfSchedulingPreferencesTable" or name == "qosIfTailDropTable" or name == "qosIfWeightsTable" or name == "qosInterfaceTypeTable" or name == "qosIpAceTable" or name == "qosIpAclActionTable" or name == "qosIpAclDefinitionTable" or name == "qosMacClassificationTable" or name == "qosPolicerTable" or name == "qosUnmatchedPolicyTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoQosPibMib()
        return self._top_entity

