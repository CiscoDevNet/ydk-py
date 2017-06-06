""" CISCO_QOS_PIB_MIB 

The Cisco QOS Policy PIB for provisioning QOS policy.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class QosinterfacequeuetypeEnum(Enum):
    """
    QosinterfacequeuetypeEnum

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

    oneQ1t = 1

    oneQ2t = 2

    oneQ4t = 3

    oneQ8t = 4

    twoQ1t = 5

    twoQ2t = 6

    twoQ4t = 7

    twoQ8t = 8

    threeQ1t = 9

    threeQ2t = 10

    threeQ4t = 11

    threeQ8t = 12

    fourQ1t = 13

    fourQ2t = 14

    fourQ4t = 15

    fourQ8t = 16

    eightQ1t = 17

    eightQ2t = 18

    eightQ4t = 19

    eightQ8t = 20

    sixteenQ1t = 21

    sixteenQ2t = 22

    sixteenQ4t = 23

    sixtyfourQ1t = 24

    sixtyfourQ2t = 25

    sixtyfourQ4t = 26

    oneP1Q0t = 27

    oneP1Q4t = 28

    oneP1Q8t = 29

    oneP2Q1t = 30

    oneP2Q2t = 31

    oneP3Q1t = 32

    oneP7Q8t = 33

    oneP3Q8t = 34

    sixteenQ8t = 35

    oneP15Q8t = 36

    oneP15Q1t = 37

    oneP7Q1t = 38

    oneP31Q1t = 39

    thirtytwoQ1t = 40

    thirtytwoQ8t = 41

    oneP31Q8t = 42

    oneP7Q4t = 43

    oneP3Q4t = 44

    oneP7Q2t = 45


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
        return meta._meta_table['QosinterfacequeuetypeEnum']


class QueuerangeEnum(Enum):
    """
    QueuerangeEnum

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

    oneQ = 1

    twoQ = 2

    threeQ = 3

    fourQ = 4

    eightQ = 8

    sixteenQ = 16

    thirtyTwoQ = 32

    sixtyFourQ = 64


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
        return meta._meta_table['QueuerangeEnum']


class ThresholdsetrangeEnum(Enum):
    """
    ThresholdsetrangeEnum

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

    zeroT = 0

    oneT = 1

    twoT = 2

    fourT = 4

    eightT = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
        return meta._meta_table['ThresholdsetrangeEnum']


class Qosinterfacetypecapabilities(FixedBitsDict):
    """
    Qosinterfacetypecapabilities

    An enumeration of interface capabilities.  Used by the PDP to
    select policies and configuration to push to the PEP.
    Keys are:- outputL2Classification , unspecified , inputAggregatePolicing , outputAggregateShaping , outputUflowPolicing , pq , wred , tailDrop , outputPortClassification , fifo , wfq , outputAggregatePolicing , cbwfq , outputIpClassification , inputPortClassification , wrr , cq , inputIpClassification , pqWrr , inputUflowPolicing , policeByDropping , policeByMarkingDown , pqCbwfq , inputUflowShaping , inputL2Classification , inputAggregateShaping , outputUflowShaping

    """

    def __init__(self):
        self._dictionary = { 
            'outputL2Classification':False,
            'unspecified':False,
            'inputAggregatePolicing':False,
            'outputAggregateShaping':False,
            'outputUflowPolicing':False,
            'pq':False,
            'wred':False,
            'tailDrop':False,
            'outputPortClassification':False,
            'fifo':False,
            'wfq':False,
            'outputAggregatePolicing':False,
            'cbwfq':False,
            'outputIpClassification':False,
            'inputPortClassification':False,
            'wrr':False,
            'cq':False,
            'inputIpClassification':False,
            'pqWrr':False,
            'inputUflowPolicing':False,
            'policeByDropping':False,
            'policeByMarkingDown':False,
            'pqCbwfq':False,
            'inputUflowShaping':False,
            'inputL2Classification':False,
            'inputAggregateShaping':False,
            'outputUflowShaping':False,
        }
        self._pos_map = { 
            'outputL2Classification':3,
            'unspecified':0,
            'inputAggregatePolicing':6,
            'outputAggregateShaping':24,
            'outputUflowPolicing':7,
            'pq':15,
            'wred':18,
            'tailDrop':17,
            'outputPortClassification':20,
            'fifo':11,
            'wfq':13,
            'outputAggregatePolicing':8,
            'cbwfq':16,
            'outputIpClassification':4,
            'inputPortClassification':19,
            'wrr':12,
            'cq':14,
            'inputIpClassification':2,
            'pqWrr':25,
            'inputUflowPolicing':5,
            'policeByDropping':10,
            'policeByMarkingDown':9,
            'pqCbwfq':26,
            'inputUflowShaping':21,
            'inputL2Classification':1,
            'inputAggregateShaping':22,
            'outputUflowShaping':23,
        }


class CiscoQosPibMib(object):
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
        self.qosaggregatetable = CiscoQosPibMib.Qosaggregatetable()
        self.qosaggregatetable.parent = self
        self.qoscostodscptable = CiscoQosPibMib.Qoscostodscptable()
        self.qoscostodscptable.parent = self
        self.qosdeviceattributetable = CiscoQosPibMib.Qosdeviceattributetable()
        self.qosdeviceattributetable.parent = self
        self.qosdevicepibincarnationtable = CiscoQosPibMib.Qosdevicepibincarnationtable()
        self.qosdevicepibincarnationtable.parent = self
        self.qosdiffservmappingtable = CiscoQosPibMib.Qosdiffservmappingtable()
        self.qosdiffservmappingtable.parent = self
        self.qosifdroppreferencetable = CiscoQosPibMib.Qosifdroppreferencetable()
        self.qosifdroppreferencetable.parent = self
        self.qosifdscpassignmenttable = CiscoQosPibMib.Qosifdscpassignmenttable()
        self.qosifdscpassignmenttable.parent = self
        self.qosifredtable = CiscoQosPibMib.Qosifredtable()
        self.qosifredtable.parent = self
        self.qosifschedulingpreferencestable = CiscoQosPibMib.Qosifschedulingpreferencestable()
        self.qosifschedulingpreferencestable.parent = self
        self.qosiftaildroptable = CiscoQosPibMib.Qosiftaildroptable()
        self.qosiftaildroptable.parent = self
        self.qosifweightstable = CiscoQosPibMib.Qosifweightstable()
        self.qosifweightstable.parent = self
        self.qosinterfacetypetable = CiscoQosPibMib.Qosinterfacetypetable()
        self.qosinterfacetypetable.parent = self
        self.qosipacetable = CiscoQosPibMib.Qosipacetable()
        self.qosipacetable.parent = self
        self.qosipaclactiontable = CiscoQosPibMib.Qosipaclactiontable()
        self.qosipaclactiontable.parent = self
        self.qosipacldefinitiontable = CiscoQosPibMib.Qosipacldefinitiontable()
        self.qosipacldefinitiontable.parent = self
        self.qosmacclassificationtable = CiscoQosPibMib.Qosmacclassificationtable()
        self.qosmacclassificationtable.parent = self
        self.qospolicertable = CiscoQosPibMib.Qospolicertable()
        self.qospolicertable.parent = self
        self.qosunmatchedpolicytable = CiscoQosPibMib.Qosunmatchedpolicytable()
        self.qosunmatchedpolicytable.parent = self


    class Qosdevicepibincarnationtable(object):
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
            self.parent = None
            self.qosdevicepibincarnationentry = YList()
            self.qosdevicepibincarnationentry.parent = self
            self.qosdevicepibincarnationentry.name = 'qosdevicepibincarnationentry'


        class Qosdevicepibincarnationentry(object):
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
                self.parent = None
                self.qosdeviceincarnationid = None
                self.qosdevicepdpname = None
                self.qosdevicepibincarnation = None
                self.qosdevicepibttl = None

            @property
            def _common_path(self):
                if self.qosdeviceincarnationid is None:
                    raise YPYModelError('Key property qosdeviceincarnationid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDevicePibIncarnationTable/CISCO-QOS-PIB-MIB:qosDevicePibIncarnationEntry[CISCO-QOS-PIB-MIB:qosDeviceIncarnationId = ' + str(self.qosdeviceincarnationid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosdeviceincarnationid is not None:
                    return True

                if self.qosdevicepdpname is not None:
                    return True

                if self.qosdevicepibincarnation is not None:
                    return True

                if self.qosdevicepibttl is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDevicePibIncarnationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosdevicepibincarnationentry is not None:
                for child_ref in self.qosdevicepibincarnationentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosdevicepibincarnationtable']['meta_info']


    class Qosdeviceattributetable(object):
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
            self.parent = None
            self.qosdeviceattributeentry = YList()
            self.qosdeviceattributeentry.parent = self
            self.qosdeviceattributeentry.name = 'qosdeviceattributeentry'


        class Qosdeviceattributeentry(object):
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
                self.parent = None
                self.qosdeviceattributeid = None
                self.qosdevicecapabilities = CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry.Qosdevicecapabilities()
                self.qosdevicemaxmessagesize = None
                self.qosdevicepepdomain = None
                self.qosdeviceprimarypdp = None
                self.qosdevicesecondarypdp = None

            class Qosdevicecapabilities(FixedBitsDict):
                """
                Qosdevicecapabilities

                An enumeration of device capabilities.  Used by the PDP to
                select policies and configuration to push to the PEP.
                Keys are:- dscp , unspecified , ipPrecedence , layer2Cos

                """

                def __init__(self):
                    self._dictionary = { 
                        'dscp':False,
                        'unspecified':False,
                        'ipPrecedence':False,
                        'layer2Cos':False,
                    }
                    self._pos_map = { 
                        'dscp':3,
                        'unspecified':0,
                        'ipPrecedence':2,
                        'layer2Cos':1,
                    }

            @property
            def _common_path(self):
                if self.qosdeviceattributeid is None:
                    raise YPYModelError('Key property qosdeviceattributeid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDeviceAttributeTable/CISCO-QOS-PIB-MIB:qosDeviceAttributeEntry[CISCO-QOS-PIB-MIB:qosDeviceAttributeId = ' + str(self.qosdeviceattributeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosdeviceattributeid is not None:
                    return True

                if self.qosdevicecapabilities is not None:
                    if self.qosdevicecapabilities._has_data():
                        return True

                if self.qosdevicemaxmessagesize is not None:
                    return True

                if self.qosdevicepepdomain is not None:
                    return True

                if self.qosdeviceprimarypdp is not None:
                    return True

                if self.qosdevicesecondarypdp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDeviceAttributeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosdeviceattributeentry is not None:
                for child_ref in self.qosdeviceattributeentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosdeviceattributetable']['meta_info']


    class Qosinterfacetypetable(object):
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
            self.parent = None
            self.qosinterfacetypeentry = YList()
            self.qosinterfacetypeentry.parent = self
            self.qosinterfacetypeentry.name = 'qosinterfacetypeentry'


        class Qosinterfacetypeentry(object):
            """
            An instance of this class describes a role combination for
            an interface type of an interface that exists on the device.
            
            .. attribute:: qosinterfacetypeid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qosinterfacequeuetype
            
            	The interface type in terms of number of queues and thresholds
            	**type**\:   :py:class:`QosinterfacequeuetypeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosinterfacequeuetypeEnum>`
            
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
                self.parent = None
                self.qosinterfacetypeid = None
                self.qosinterfacequeuetype = None
                self.qosinterfacetypecapabilities = Qosinterfacetypecapabilities()
                self.qosinterfacetyperoles = None

            @property
            def _common_path(self):
                if self.qosinterfacetypeid is None:
                    raise YPYModelError('Key property qosinterfacetypeid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosInterfaceTypeTable/CISCO-QOS-PIB-MIB:qosInterfaceTypeEntry[CISCO-QOS-PIB-MIB:qosInterfaceTypeId = ' + str(self.qosinterfacetypeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosinterfacetypeid is not None:
                    return True

                if self.qosinterfacequeuetype is not None:
                    return True

                if self.qosinterfacetypecapabilities is not None:
                    if self.qosinterfacetypecapabilities._has_data():
                        return True

                if self.qosinterfacetyperoles is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosInterfaceTypeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosinterfacetypeentry is not None:
                for child_ref in self.qosinterfacetypeentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosinterfacetypetable']['meta_info']


    class Qosdiffservmappingtable(object):
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
            self.parent = None
            self.qosdiffservmappingentry = YList()
            self.qosdiffservmappingentry.parent = self
            self.qosdiffservmappingentry.name = 'qosdiffservmappingentry'


        class Qosdiffservmappingentry(object):
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
                self.parent = None
                self.qosdscp = None
                self.qosl2cos = None
                self.qosmarkeddscp = None

            @property
            def _common_path(self):
                if self.qosdscp is None:
                    raise YPYModelError('Key property qosdscp is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDiffServMappingTable/CISCO-QOS-PIB-MIB:qosDiffServMappingEntry[CISCO-QOS-PIB-MIB:qosDscp = ' + str(self.qosdscp) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosdscp is not None:
                    return True

                if self.qosl2cos is not None:
                    return True

                if self.qosmarkeddscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosDiffServMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosdiffservmappingentry is not None:
                for child_ref in self.qosdiffservmappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosdiffservmappingtable']['meta_info']


    class Qoscostodscptable(object):
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
            self.parent = None
            self.qoscostodscpentry = YList()
            self.qoscostodscpentry.parent = self
            self.qoscostodscpentry.name = 'qoscostodscpentry'


        class Qoscostodscpentry(object):
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
                self.parent = None
                self.qoscostodscpcos = None
                self.qoscostodscpdscp = None

            @property
            def _common_path(self):
                if self.qoscostodscpcos is None:
                    raise YPYModelError('Key property qoscostodscpcos is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosCosToDscpTable/CISCO-QOS-PIB-MIB:qosCosToDscpEntry[CISCO-QOS-PIB-MIB:qosCosToDscpCos = ' + str(self.qoscostodscpcos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qoscostodscpcos is not None:
                    return True

                if self.qoscostodscpdscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosCosToDscpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qoscostodscpentry is not None:
                for child_ref in self.qoscostodscpentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qoscostodscptable']['meta_info']


    class Qosunmatchedpolicytable(object):
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
            self.parent = None
            self.qosunmatchedpolicyentry = YList()
            self.qosunmatchedpolicyentry.parent = self
            self.qosunmatchedpolicyentry.name = 'qosunmatchedpolicyentry'


        class Qosunmatchedpolicyentry(object):
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
            	**type**\:   :py:class:`QosunmatchedpolicydirectionEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.QosunmatchedpolicydirectionEnum>`
            
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
                self.parent = None
                self.qosunmatchedpolicyid = None
                self.qosunmatchedpolicyaggregateid = None
                self.qosunmatchedpolicydirection = None
                self.qosunmatchedpolicydscp = None
                self.qosunmatchedpolicydscptrusted = None
                self.qosunmatchedpolicyrole = None
                self.qosunmatchpolmicroflowpolicerid = None

            class QosunmatchedpolicydirectionEnum(Enum):
                """
                QosunmatchedpolicydirectionEnum

                The direction of packet flow at the interface in question to

                which this instance applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = 0

                out = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                    return meta._meta_table['CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.QosunmatchedpolicydirectionEnum']


            @property
            def _common_path(self):
                if self.qosunmatchedpolicyid is None:
                    raise YPYModelError('Key property qosunmatchedpolicyid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosUnmatchedPolicyTable/CISCO-QOS-PIB-MIB:qosUnmatchedPolicyEntry[CISCO-QOS-PIB-MIB:qosUnmatchedPolicyId = ' + str(self.qosunmatchedpolicyid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosunmatchedpolicyid is not None:
                    return True

                if self.qosunmatchedpolicyaggregateid is not None:
                    return True

                if self.qosunmatchedpolicydirection is not None:
                    return True

                if self.qosunmatchedpolicydscp is not None:
                    return True

                if self.qosunmatchedpolicydscptrusted is not None:
                    return True

                if self.qosunmatchedpolicyrole is not None:
                    return True

                if self.qosunmatchpolmicroflowpolicerid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosUnmatchedPolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosunmatchedpolicyentry is not None:
                for child_ref in self.qosunmatchedpolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosunmatchedpolicytable']['meta_info']


    class Qospolicertable(object):
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
            self.parent = None
            self.qospolicerentry = YList()
            self.qospolicerentry.parent = self
            self.qospolicerentry.name = 'qospolicerentry'


        class Qospolicerentry(object):
            """
            An instance of this class specifies a set of policing
            parameters.
            
            .. attribute:: qospolicerid  <key>
            
            	An integer index to identify the instance of the policy class
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qospoliceraction
            
            	An indication of how to handle out of profile packets.  When the shape action is chosen then traffic is shaped to the rate specified by qosPolicerRate
            	**type**\:   :py:class:`QospoliceractionEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qospolicertable.Qospolicerentry.QospoliceractionEnum>`
            
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
                self.parent = None
                self.qospolicerid = None
                self.qospoliceraction = None
                self.qospolicerexcessburst = None
                self.qospolicernormalburst = None
                self.qospolicerrate = None

            class QospoliceractionEnum(Enum):
                """
                QospoliceractionEnum

                An indication of how to handle out of profile packets.  When

                the shape action is chosen then traffic is shaped to the rate

                specified by qosPolicerRate.

                .. data:: drop = 0

                .. data:: mark = 1

                .. data:: shape = 2

                """

                drop = 0

                mark = 1

                shape = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                    return meta._meta_table['CiscoQosPibMib.Qospolicertable.Qospolicerentry.QospoliceractionEnum']


            @property
            def _common_path(self):
                if self.qospolicerid is None:
                    raise YPYModelError('Key property qospolicerid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosPolicerTable/CISCO-QOS-PIB-MIB:qosPolicerEntry[CISCO-QOS-PIB-MIB:qosPolicerId = ' + str(self.qospolicerid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qospolicerid is not None:
                    return True

                if self.qospoliceraction is not None:
                    return True

                if self.qospolicerexcessburst is not None:
                    return True

                if self.qospolicernormalburst is not None:
                    return True

                if self.qospolicerrate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qospolicertable.Qospolicerentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosPolicerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qospolicerentry is not None:
                for child_ref in self.qospolicerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qospolicertable']['meta_info']


    class Qosaggregatetable(object):
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
            self.parent = None
            self.qosaggregateentry = YList()
            self.qosaggregateentry.parent = self
            self.qosaggregateentry.name = 'qosaggregateentry'


        class Qosaggregateentry(object):
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
                self.parent = None
                self.qosaggregateid = None
                self.qosaggregatepolicerid = None

            @property
            def _common_path(self):
                if self.qosaggregateid is None:
                    raise YPYModelError('Key property qosaggregateid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosAggregateTable/CISCO-QOS-PIB-MIB:qosAggregateEntry[CISCO-QOS-PIB-MIB:qosAggregateId = ' + str(self.qosaggregateid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosaggregateid is not None:
                    return True

                if self.qosaggregatepolicerid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosAggregateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosaggregateentry is not None:
                for child_ref in self.qosaggregateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosaggregatetable']['meta_info']


    class Qosmacclassificationtable(object):
        """
        A class of MAC/Vlan tuples and their associated CoS values.
        
        .. attribute:: qosmacclassificationentry
        
        	An instance of this class specifies the mapping of a VLAN and a MAC address to a CoS value
        	**type**\: list of    :py:class:`Qosmacclassificationentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            self.parent = None
            self.qosmacclassificationentry = YList()
            self.qosmacclassificationentry.parent = self
            self.qosmacclassificationentry.name = 'qosmacclassificationentry'


        class Qosmacclassificationentry(object):
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
                self.parent = None
                self.qosmacclassificationid = None
                self.qosdstmacaddress = None
                self.qosdstmaccos = None
                self.qosdstmacvlan = None

            @property
            def _common_path(self):
                if self.qosmacclassificationid is None:
                    raise YPYModelError('Key property qosmacclassificationid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosMacClassificationTable/CISCO-QOS-PIB-MIB:qosMacClassificationEntry[CISCO-QOS-PIB-MIB:qosMacClassificationId = ' + str(self.qosmacclassificationid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosmacclassificationid is not None:
                    return True

                if self.qosdstmacaddress is not None:
                    return True

                if self.qosdstmaccos is not None:
                    return True

                if self.qosdstmacvlan is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosMacClassificationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosmacclassificationentry is not None:
                for child_ref in self.qosmacclassificationentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosmacclassificationtable']['meta_info']


    class Qosipacetable(object):
        """
        ACE definitions.
        
        .. attribute:: qosipaceentry
        
        	An instance of this class specifies an ACE
        	**type**\: list of    :py:class:`Qosipaceentry <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipacetable.Qosipaceentry>`
        
        

        """

        _prefix = 'CISCO-QOS-PIB-MIB'
        _revision = '2007-08-29'

        def __init__(self):
            self.parent = None
            self.qosipaceentry = YList()
            self.qosipaceentry.parent = self
            self.qosipaceentry.name = 'qosipaceentry'


        class Qosipaceentry(object):
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
                self.parent = None
                self.qosipaceid = None
                self.qosipacedscpmax = None
                self.qosipacedscpmin = None
                self.qosipacedstaddr = None
                self.qosipacedstaddrmask = None
                self.qosipacedstl4portmax = None
                self.qosipacedstl4portmin = None
                self.qosipacepermit = None
                self.qosipaceprotocol = None
                self.qosipacesrcaddr = None
                self.qosipacesrcaddrmask = None
                self.qosipacesrcl4portmax = None
                self.qosipacesrcl4portmin = None

            @property
            def _common_path(self):
                if self.qosipaceid is None:
                    raise YPYModelError('Key property qosipaceid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAceTable/CISCO-QOS-PIB-MIB:qosIpAceEntry[CISCO-QOS-PIB-MIB:qosIpAceId = ' + str(self.qosipaceid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosipaceid is not None:
                    return True

                if self.qosipacedscpmax is not None:
                    return True

                if self.qosipacedscpmin is not None:
                    return True

                if self.qosipacedstaddr is not None:
                    return True

                if self.qosipacedstaddrmask is not None:
                    return True

                if self.qosipacedstl4portmax is not None:
                    return True

                if self.qosipacedstl4portmin is not None:
                    return True

                if self.qosipacepermit is not None:
                    return True

                if self.qosipaceprotocol is not None:
                    return True

                if self.qosipacesrcaddr is not None:
                    return True

                if self.qosipacesrcaddrmask is not None:
                    return True

                if self.qosipacesrcl4portmax is not None:
                    return True

                if self.qosipacesrcl4portmin is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosipacetable.Qosipaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosipaceentry is not None:
                for child_ref in self.qosipaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosipacetable']['meta_info']


    class Qosipacldefinitiontable(object):
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
            self.parent = None
            self.qosipacldefinitionentry = YList()
            self.qosipacldefinitionentry.parent = self
            self.qosipacldefinitionentry.name = 'qosipacldefinitionentry'


        class Qosipacldefinitionentry(object):
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
                self.parent = None
                self.qosipacldefinitionid = None
                self.qosipaceorder = None
                self.qosipacldefaceid = None
                self.qosipaclid = None

            @property
            def _common_path(self):
                if self.qosipacldefinitionid is None:
                    raise YPYModelError('Key property qosipacldefinitionid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAclDefinitionTable/CISCO-QOS-PIB-MIB:qosIpAclDefinitionEntry[CISCO-QOS-PIB-MIB:qosIpAclDefinitionId = ' + str(self.qosipacldefinitionid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosipacldefinitionid is not None:
                    return True

                if self.qosipaceorder is not None:
                    return True

                if self.qosipacldefaceid is not None:
                    return True

                if self.qosipaclid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAclDefinitionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosipacldefinitionentry is not None:
                for child_ref in self.qosipacldefinitionentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosipacldefinitiontable']['meta_info']


    class Qosipaclactiontable(object):
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
            self.parent = None
            self.qosipaclactionentry = YList()
            self.qosipaclactionentry.parent = self
            self.qosipaclactionentry.name = 'qosipaclactionentry'


        class Qosipaclactionentry(object):
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
            	**type**\:   :py:class:`QosipaclinterfacedirectionEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry.QosipaclinterfacedirectionEnum>`
            
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
                self.parent = None
                self.qosipaclactionid = None
                self.qosipaclactaclid = None
                self.qosipaclaggregateid = None
                self.qosipacldscp = None
                self.qosipacldscptrusted = None
                self.qosipaclinterfacedirection = None
                self.qosipaclinterfaceroles = None
                self.qosipaclmicroflowpolicerid = None
                self.qosipaclorder = None

            class QosipaclinterfacedirectionEnum(Enum):
                """
                QosipaclinterfacedirectionEnum

                The direction of packet flow at the interface in question to

                which this ACL applies.

                .. data:: in_ = 0

                .. data:: out = 1

                """

                in_ = 0

                out = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                    return meta._meta_table['CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry.QosipaclinterfacedirectionEnum']


            @property
            def _common_path(self):
                if self.qosipaclactionid is None:
                    raise YPYModelError('Key property qosipaclactionid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAclActionTable/CISCO-QOS-PIB-MIB:qosIpAclActionEntry[CISCO-QOS-PIB-MIB:qosIpAclActionId = ' + str(self.qosipaclactionid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosipaclactionid is not None:
                    return True

                if self.qosipaclactaclid is not None:
                    return True

                if self.qosipaclaggregateid is not None:
                    return True

                if self.qosipacldscp is not None:
                    return True

                if self.qosipacldscptrusted is not None:
                    return True

                if self.qosipaclinterfacedirection is not None:
                    return True

                if self.qosipaclinterfaceroles is not None:
                    return True

                if self.qosipaclmicroflowpolicerid is not None:
                    return True

                if self.qosipaclorder is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIpAclActionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosipaclactionentry is not None:
                for child_ref in self.qosipaclactionentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosipaclactiontable']['meta_info']


    class Qosifschedulingpreferencestable(object):
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
            self.parent = None
            self.qosifschedulingpreferenceentry = YList()
            self.qosifschedulingpreferenceentry.parent = self
            self.qosifschedulingpreferenceentry.name = 'qosifschedulingpreferenceentry'


        class Qosifschedulingpreferenceentry(object):
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
            	**type**\:   :py:class:`QosifschedulingdisciplineEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.QosifschedulingdisciplineEnum>`
            
            .. attribute:: qosifschedulingpreference
            
            	The preference to use this scheduling discipline and queue type.  A higher value means a higher preference.  If two disciplines have the same preference the choice is a local decision
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: qosifschedulingqueuetype
            
            	The queue type of this preference
            	**type**\:   :py:class:`QosinterfacequeuetypeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosinterfacequeuetypeEnum>`
            
            .. attribute:: qosifschedulingroles
            
            	The combination of roles the interface must have for this policy instance to apply to that interface
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                self.parent = None
                self.qosifschedulingpreferenceid = None
                self.qosifschedulingdiscipline = None
                self.qosifschedulingpreference = None
                self.qosifschedulingqueuetype = None
                self.qosifschedulingroles = None

            class QosifschedulingdisciplineEnum(Enum):
                """
                QosifschedulingdisciplineEnum

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

                weightedFairQueueing = 1

                weightedRoundRobin = 2

                customQueueing = 3

                priorityQueueing = 4

                classBasedWFQ = 5

                fifo = 6

                pqWrr = 7

                pqCbwfq = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                    return meta._meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.QosifschedulingdisciplineEnum']


            @property
            def _common_path(self):
                if self.qosifschedulingpreferenceid is None:
                    raise YPYModelError('Key property qosifschedulingpreferenceid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfSchedulingPreferencesTable/CISCO-QOS-PIB-MIB:qosIfSchedulingPreferenceEntry[CISCO-QOS-PIB-MIB:qosIfSchedulingPreferenceId = ' + str(self.qosifschedulingpreferenceid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosifschedulingpreferenceid is not None:
                    return True

                if self.qosifschedulingdiscipline is not None:
                    return True

                if self.qosifschedulingpreference is not None:
                    return True

                if self.qosifschedulingqueuetype is not None:
                    return True

                if self.qosifschedulingroles is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfSchedulingPreferencesTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosifschedulingpreferenceentry is not None:
                for child_ref in self.qosifschedulingpreferenceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable']['meta_info']


    class Qosifdroppreferencetable(object):
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
            self.parent = None
            self.qosifdroppreferenceentry = YList()
            self.qosifdroppreferenceentry.parent = self
            self.qosifdroppreferenceentry.name = 'qosifdroppreferenceentry'


        class Qosifdroppreferenceentry(object):
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
            	**type**\:   :py:class:`QosifdropdisciplineEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry.QosifdropdisciplineEnum>`
            
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
                self.parent = None
                self.qosifdroppreferenceid = None
                self.qosifdropdiscipline = None
                self.qosifdroppreference = None
                self.qosifdroproles = None

            class QosifdropdisciplineEnum(Enum):
                """
                QosifdropdisciplineEnum

                An enumerate type for all the known drop mechanisms.

                .. data:: qosIfDropWRED = 1

                .. data:: qosIfDropTailDrop = 2

                """

                qosIfDropWRED = 1

                qosIfDropTailDrop = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                    return meta._meta_table['CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry.QosifdropdisciplineEnum']


            @property
            def _common_path(self):
                if self.qosifdroppreferenceid is None:
                    raise YPYModelError('Key property qosifdroppreferenceid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfDropPreferenceTable/CISCO-QOS-PIB-MIB:qosIfDropPreferenceEntry[CISCO-QOS-PIB-MIB:qosIfDropPreferenceId = ' + str(self.qosifdroppreferenceid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosifdroppreferenceid is not None:
                    return True

                if self.qosifdropdiscipline is not None:
                    return True

                if self.qosifdroppreference is not None:
                    return True

                if self.qosifdroproles is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfDropPreferenceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosifdroppreferenceentry is not None:
                for child_ref in self.qosifdroppreferenceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosifdroppreferencetable']['meta_info']


    class Qosifdscpassignmenttable(object):
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
            self.parent = None
            self.qosifdscpassignmententry = YList()
            self.qosifdscpassignmententry.parent = self
            self.qosifdscpassignmententry.name = 'qosifdscpassignmententry'


        class Qosifdscpassignmententry(object):
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
            	**type**\:   :py:class:`QosinterfacequeuetypeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QosinterfacequeuetypeEnum>`
            
            .. attribute:: qosifthresholdset
            
            	The threshold set of the specified queue to which the DSCP applies for the given interface type
            	**type**\:  int
            
            	**range:** 1..8
            
            

            """

            _prefix = 'CISCO-QOS-PIB-MIB'
            _revision = '2007-08-29'

            def __init__(self):
                self.parent = None
                self.qosifdscpassignmentid = None
                self.qosifdscp = None
                self.qosifdscproles = None
                self.qosifqueue = None
                self.qosifqueuetype = None
                self.qosifthresholdset = None

            @property
            def _common_path(self):
                if self.qosifdscpassignmentid is None:
                    raise YPYModelError('Key property qosifdscpassignmentid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfDscpAssignmentTable/CISCO-QOS-PIB-MIB:qosIfDscpAssignmentEntry[CISCO-QOS-PIB-MIB:qosIfDscpAssignmentId = ' + str(self.qosifdscpassignmentid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosifdscpassignmentid is not None:
                    return True

                if self.qosifdscp is not None:
                    return True

                if self.qosifdscproles is not None:
                    return True

                if self.qosifqueue is not None:
                    return True

                if self.qosifqueuetype is not None:
                    return True

                if self.qosifthresholdset is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfDscpAssignmentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosifdscpassignmententry is not None:
                for child_ref in self.qosifdscpassignmententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosifdscpassignmenttable']['meta_info']


    class Qosifredtable(object):
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
            self.parent = None
            self.qosifredentry = YList()
            self.qosifredentry.parent = self
            self.qosifredentry.name = 'qosifredentry'


        class Qosifredentry(object):
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
            	**type**\:   :py:class:`ThresholdsetrangeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.ThresholdsetrangeEnum>`
            
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
                self.parent = None
                self.qosifredid = None
                self.qosifrednumthresholdsets = None
                self.qosifredroles = None
                self.qosifredthresholdset = None
                self.qosifredthresholdsetlower = None
                self.qosifredthresholdsetupper = None

            @property
            def _common_path(self):
                if self.qosifredid is None:
                    raise YPYModelError('Key property qosifredid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfRedTable/CISCO-QOS-PIB-MIB:qosIfRedEntry[CISCO-QOS-PIB-MIB:qosIfRedId = ' + str(self.qosifredid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosifredid is not None:
                    return True

                if self.qosifrednumthresholdsets is not None:
                    return True

                if self.qosifredroles is not None:
                    return True

                if self.qosifredthresholdset is not None:
                    return True

                if self.qosifredthresholdsetlower is not None:
                    return True

                if self.qosifredthresholdsetupper is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosifredtable.Qosifredentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfRedTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosifredentry is not None:
                for child_ref in self.qosifredentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosifredtable']['meta_info']


    class Qosiftaildroptable(object):
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
            self.parent = None
            self.qosiftaildropentry = YList()
            self.qosiftaildropentry.parent = self
            self.qosiftaildropentry.name = 'qosiftaildropentry'


        class Qosiftaildropentry(object):
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
            	**type**\:   :py:class:`ThresholdsetrangeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.ThresholdsetrangeEnum>`
            
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
                self.parent = None
                self.qosiftaildropid = None
                self.qosiftaildropnumthresholdsets = None
                self.qosiftaildroproles = None
                self.qosiftaildropthresholdset = None
                self.qosiftaildropthresholdsetvalue = None

            @property
            def _common_path(self):
                if self.qosiftaildropid is None:
                    raise YPYModelError('Key property qosiftaildropid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfTailDropTable/CISCO-QOS-PIB-MIB:qosIfTailDropEntry[CISCO-QOS-PIB-MIB:qosIfTailDropId = ' + str(self.qosiftaildropid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosiftaildropid is not None:
                    return True

                if self.qosiftaildropnumthresholdsets is not None:
                    return True

                if self.qosiftaildroproles is not None:
                    return True

                if self.qosiftaildropthresholdset is not None:
                    return True

                if self.qosiftaildropthresholdsetvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfTailDropTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosiftaildropentry is not None:
                for child_ref in self.qosiftaildropentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosiftaildroptable']['meta_info']


    class Qosifweightstable(object):
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
            self.parent = None
            self.qosifweightsentry = YList()
            self.qosifweightsentry.parent = self
            self.qosifweightsentry.name = 'qosifweightsentry'


        class Qosifweightsentry(object):
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
            	**type**\:   :py:class:`QueuerangeEnum <ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB.QueuerangeEnum>`
            
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
                self.parent = None
                self.qosifweightsid = None
                self.qosifweightsdrainsize = None
                self.qosifweightsnumqueues = None
                self.qosifweightsqueue = None
                self.qosifweightsqueuesize = None
                self.qosifweightsroles = None

            @property
            def _common_path(self):
                if self.qosifweightsid is None:
                    raise YPYModelError('Key property qosifweightsid is None')

                return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfWeightsTable/CISCO-QOS-PIB-MIB:qosIfWeightsEntry[CISCO-QOS-PIB-MIB:qosIfWeightsId = ' + str(self.qosifweightsid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.qosifweightsid is not None:
                    return True

                if self.qosifweightsdrainsize is not None:
                    return True

                if self.qosifweightsnumqueues is not None:
                    return True

                if self.qosifweightsqueue is not None:
                    return True

                if self.qosifweightsqueuesize is not None:
                    return True

                if self.qosifweightsroles is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
                return meta._meta_table['CiscoQosPibMib.Qosifweightstable.Qosifweightsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB/CISCO-QOS-PIB-MIB:qosIfWeightsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.qosifweightsentry is not None:
                for child_ref in self.qosifweightsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
            return meta._meta_table['CiscoQosPibMib.Qosifweightstable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-QOS-PIB-MIB:CISCO-QOS-PIB-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.qosaggregatetable is not None and self.qosaggregatetable._has_data():
            return True

        if self.qoscostodscptable is not None and self.qoscostodscptable._has_data():
            return True

        if self.qosdeviceattributetable is not None and self.qosdeviceattributetable._has_data():
            return True

        if self.qosdevicepibincarnationtable is not None and self.qosdevicepibincarnationtable._has_data():
            return True

        if self.qosdiffservmappingtable is not None and self.qosdiffservmappingtable._has_data():
            return True

        if self.qosifdroppreferencetable is not None and self.qosifdroppreferencetable._has_data():
            return True

        if self.qosifdscpassignmenttable is not None and self.qosifdscpassignmenttable._has_data():
            return True

        if self.qosifredtable is not None and self.qosifredtable._has_data():
            return True

        if self.qosifschedulingpreferencestable is not None and self.qosifschedulingpreferencestable._has_data():
            return True

        if self.qosiftaildroptable is not None and self.qosiftaildroptable._has_data():
            return True

        if self.qosifweightstable is not None and self.qosifweightstable._has_data():
            return True

        if self.qosinterfacetypetable is not None and self.qosinterfacetypetable._has_data():
            return True

        if self.qosipacetable is not None and self.qosipacetable._has_data():
            return True

        if self.qosipaclactiontable is not None and self.qosipaclactiontable._has_data():
            return True

        if self.qosipacldefinitiontable is not None and self.qosipacldefinitiontable._has_data():
            return True

        if self.qosmacclassificationtable is not None and self.qosmacclassificationtable._has_data():
            return True

        if self.qospolicertable is not None and self.qospolicertable._has_data():
            return True

        if self.qosunmatchedpolicytable is not None and self.qosunmatchedpolicytable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_QOS_PIB_MIB as meta
        return meta._meta_table['CiscoQosPibMib']['meta_info']


