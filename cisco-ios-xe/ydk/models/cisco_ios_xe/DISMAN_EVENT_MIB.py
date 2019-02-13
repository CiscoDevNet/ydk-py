""" DISMAN_EVENT_MIB 

The MIB module for defining event triggers and actions
for network management purposes.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FailureReason(Enum):
    """
    FailureReason (Enum Class)

    Reasons for failures in an attempt to perform a management

    request.

    The first group of errors, numbered less than 0, are related

    to problems in sending the request.  The existence of a

    particular error code here does not imply that all

    implementations are capable of sensing that error and

    returning that code.

    The second group, numbered greater than 0, are copied

    directly from SNMP protocol operations and are intended to

    carry exactly the meanings defined for the protocol as returned

    in an SNMP response.

    localResourceLack       some local resource such as memory

                            lacking or

                            mteResourceSampleInstanceMaximum

                            exceeded

    badDestination          unrecognized domain name or otherwise

                            invalid destination address

    destinationUnreachable  can't get to destination address

    noResponse              no response to SNMP request

    badType                 the data syntax of a retrieved object

                            as not as expected

    sampleOverrun           another sample attempt occurred before

                            the previous one completed

    .. data:: sampleOverrun = -6

    .. data:: badType = -5

    .. data:: noResponse = -4

    .. data:: destinationUnreachable = -3

    .. data:: badDestination = -2

    .. data:: localResourceLack = -1

    .. data:: noError = 0

    .. data:: tooBig = 1

    .. data:: noSuchName = 2

    .. data:: badValue = 3

    .. data:: readOnly = 4

    .. data:: genErr = 5

    .. data:: noAccess = 6

    .. data:: wrongType = 7

    .. data:: wrongLength = 8

    .. data:: wrongEncoding = 9

    .. data:: wrongValue = 10

    .. data:: noCreation = 11

    .. data:: inconsistentValue = 12

    .. data:: resourceUnavailable = 13

    .. data:: commitFailed = 14

    .. data:: undoFailed = 15

    .. data:: authorizationError = 16

    .. data:: notWritable = 17

    .. data:: inconsistentName = 18

    """

    sampleOverrun = Enum.YLeaf(-6, "sampleOverrun")

    badType = Enum.YLeaf(-5, "badType")

    noResponse = Enum.YLeaf(-4, "noResponse")

    destinationUnreachable = Enum.YLeaf(-3, "destinationUnreachable")

    badDestination = Enum.YLeaf(-2, "badDestination")

    localResourceLack = Enum.YLeaf(-1, "localResourceLack")

    noError = Enum.YLeaf(0, "noError")

    tooBig = Enum.YLeaf(1, "tooBig")

    noSuchName = Enum.YLeaf(2, "noSuchName")

    badValue = Enum.YLeaf(3, "badValue")

    readOnly = Enum.YLeaf(4, "readOnly")

    genErr = Enum.YLeaf(5, "genErr")

    noAccess = Enum.YLeaf(6, "noAccess")

    wrongType = Enum.YLeaf(7, "wrongType")

    wrongLength = Enum.YLeaf(8, "wrongLength")

    wrongEncoding = Enum.YLeaf(9, "wrongEncoding")

    wrongValue = Enum.YLeaf(10, "wrongValue")

    noCreation = Enum.YLeaf(11, "noCreation")

    inconsistentValue = Enum.YLeaf(12, "inconsistentValue")

    resourceUnavailable = Enum.YLeaf(13, "resourceUnavailable")

    commitFailed = Enum.YLeaf(14, "commitFailed")

    undoFailed = Enum.YLeaf(15, "undoFailed")

    authorizationError = Enum.YLeaf(16, "authorizationError")

    notWritable = Enum.YLeaf(17, "notWritable")

    inconsistentName = Enum.YLeaf(18, "inconsistentName")



class DISMANEVENTMIB(Entity):
    """
    
    
    .. attribute:: mteresource
    
    	
    	**type**\:  :py:class:`MteResource <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteResource>`
    
    	**config**\: False
    
    .. attribute:: mtetrigger
    
    	
    	**type**\:  :py:class:`MteTrigger <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTrigger>`
    
    	**config**\: False
    
    .. attribute:: mteevent
    
    	
    	**type**\:  :py:class:`MteEvent <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEvent>`
    
    	**config**\: False
    
    .. attribute:: mtetriggertable
    
    	A table of management event trigger information
    	**type**\:  :py:class:`MteTriggerTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable>`
    
    	**config**\: False
    
    .. attribute:: mtetriggerdeltatable
    
    	A table of management event trigger information for delta sampling
    	**type**\:  :py:class:`MteTriggerDeltaTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable>`
    
    	**config**\: False
    
    .. attribute:: mtetriggerexistencetable
    
    	A table of management event trigger information for existence triggers
    	**type**\:  :py:class:`MteTriggerExistenceTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable>`
    
    	**config**\: False
    
    .. attribute:: mtetriggerbooleantable
    
    	A table of management event trigger information for boolean triggers
    	**type**\:  :py:class:`MteTriggerBooleanTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable>`
    
    	**config**\: False
    
    .. attribute:: mtetriggerthresholdtable
    
    	A table of management event trigger information for threshold triggers
    	**type**\:  :py:class:`MteTriggerThresholdTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable>`
    
    	**config**\: False
    
    .. attribute:: mteobjectstable
    
    	A table of objects that can be added to notifications based on the trigger, trigger test, or event, as pointed to by entries in those tables
    	**type**\:  :py:class:`MteObjectsTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteObjectsTable>`
    
    	**config**\: False
    
    .. attribute:: mteeventtable
    
    	A table of management event action information
    	**type**\:  :py:class:`MteEventTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable>`
    
    	**config**\: False
    
    .. attribute:: mteeventnotificationtable
    
    	A table of information about notifications to be sent as a consequence of management events
    	**type**\:  :py:class:`MteEventNotificationTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventNotificationTable>`
    
    	**config**\: False
    
    .. attribute:: mteeventsettable
    
    	A table of management event action information
    	**type**\:  :py:class:`MteEventSetTable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventSetTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'DISMAN-EVENT-MIB'
    _revision = '2000-10-16'

    def __init__(self):
        super(DISMANEVENTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DISMAN-EVENT-MIB"
        self.yang_parent_name = "DISMAN-EVENT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mteResource", ("mteresource", DISMANEVENTMIB.MteResource)), ("mteTrigger", ("mtetrigger", DISMANEVENTMIB.MteTrigger)), ("mteEvent", ("mteevent", DISMANEVENTMIB.MteEvent)), ("mteTriggerTable", ("mtetriggertable", DISMANEVENTMIB.MteTriggerTable)), ("mteTriggerDeltaTable", ("mtetriggerdeltatable", DISMANEVENTMIB.MteTriggerDeltaTable)), ("mteTriggerExistenceTable", ("mtetriggerexistencetable", DISMANEVENTMIB.MteTriggerExistenceTable)), ("mteTriggerBooleanTable", ("mtetriggerbooleantable", DISMANEVENTMIB.MteTriggerBooleanTable)), ("mteTriggerThresholdTable", ("mtetriggerthresholdtable", DISMANEVENTMIB.MteTriggerThresholdTable)), ("mteObjectsTable", ("mteobjectstable", DISMANEVENTMIB.MteObjectsTable)), ("mteEventTable", ("mteeventtable", DISMANEVENTMIB.MteEventTable)), ("mteEventNotificationTable", ("mteeventnotificationtable", DISMANEVENTMIB.MteEventNotificationTable)), ("mteEventSetTable", ("mteeventsettable", DISMANEVENTMIB.MteEventSetTable))])
        self._leafs = OrderedDict()

        self.mteresource = DISMANEVENTMIB.MteResource()
        self.mteresource.parent = self
        self._children_name_map["mteresource"] = "mteResource"

        self.mtetrigger = DISMANEVENTMIB.MteTrigger()
        self.mtetrigger.parent = self
        self._children_name_map["mtetrigger"] = "mteTrigger"

        self.mteevent = DISMANEVENTMIB.MteEvent()
        self.mteevent.parent = self
        self._children_name_map["mteevent"] = "mteEvent"

        self.mtetriggertable = DISMANEVENTMIB.MteTriggerTable()
        self.mtetriggertable.parent = self
        self._children_name_map["mtetriggertable"] = "mteTriggerTable"

        self.mtetriggerdeltatable = DISMANEVENTMIB.MteTriggerDeltaTable()
        self.mtetriggerdeltatable.parent = self
        self._children_name_map["mtetriggerdeltatable"] = "mteTriggerDeltaTable"

        self.mtetriggerexistencetable = DISMANEVENTMIB.MteTriggerExistenceTable()
        self.mtetriggerexistencetable.parent = self
        self._children_name_map["mtetriggerexistencetable"] = "mteTriggerExistenceTable"

        self.mtetriggerbooleantable = DISMANEVENTMIB.MteTriggerBooleanTable()
        self.mtetriggerbooleantable.parent = self
        self._children_name_map["mtetriggerbooleantable"] = "mteTriggerBooleanTable"

        self.mtetriggerthresholdtable = DISMANEVENTMIB.MteTriggerThresholdTable()
        self.mtetriggerthresholdtable.parent = self
        self._children_name_map["mtetriggerthresholdtable"] = "mteTriggerThresholdTable"

        self.mteobjectstable = DISMANEVENTMIB.MteObjectsTable()
        self.mteobjectstable.parent = self
        self._children_name_map["mteobjectstable"] = "mteObjectsTable"

        self.mteeventtable = DISMANEVENTMIB.MteEventTable()
        self.mteeventtable.parent = self
        self._children_name_map["mteeventtable"] = "mteEventTable"

        self.mteeventnotificationtable = DISMANEVENTMIB.MteEventNotificationTable()
        self.mteeventnotificationtable.parent = self
        self._children_name_map["mteeventnotificationtable"] = "mteEventNotificationTable"

        self.mteeventsettable = DISMANEVENTMIB.MteEventSetTable()
        self.mteeventsettable.parent = self
        self._children_name_map["mteeventsettable"] = "mteEventSetTable"
        self._segment_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DISMANEVENTMIB, [], name, value)


    class MteResource(Entity):
        """
        
        
        .. attribute:: mteresourcesampleminimum
        
        	The minimum mteTriggerFrequency this system will accept.  A system may use the larger values of this minimum to lessen the impact of constant sampling.  For larger sampling intervals the system samples less often and suffers less overhead.  This object provides a way to enforce such lower overhead for all triggers created after it is set.  Unless explicitly resource limited, a system's value for this object SHOULD be 1, allowing as small as a 1 second interval for ongoing trigger sampling.  Changing this value will not invalidate an existing setting of mteTriggerFrequency
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: mteresourcesampleinstancemaximum
        
        	The maximum number of instance entries this system will support for sampling.  These are the entries that maintain state, one for each instance of each sampled object as selected by mteTriggerValueID.  Note that wildcarded objects result in multiple instances of this state.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object SHOULD be 0.  Changing this value will not eliminate or inhibit existing sample state but could prevent allocation of additional state information
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstances
        
        	The number of currently active instance entries as defined for mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstanceshigh
        
        	The highest value of mteResourceSampleInstances that has occurred since initialization of the management system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstancelacks
        
        	The number of times this system could not take a new sample because that allocation would have exceeded the limit set by mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteResource, self).__init__()

            self.yang_name = "mteResource"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mteresourcesampleminimum', (YLeaf(YType.int32, 'mteResourceSampleMinimum'), ['int'])),
                ('mteresourcesampleinstancemaximum', (YLeaf(YType.uint32, 'mteResourceSampleInstanceMaximum'), ['int'])),
                ('mteresourcesampleinstances', (YLeaf(YType.uint32, 'mteResourceSampleInstances'), ['int'])),
                ('mteresourcesampleinstanceshigh', (YLeaf(YType.uint32, 'mteResourceSampleInstancesHigh'), ['int'])),
                ('mteresourcesampleinstancelacks', (YLeaf(YType.uint32, 'mteResourceSampleInstanceLacks'), ['int'])),
            ])
            self.mteresourcesampleminimum = None
            self.mteresourcesampleinstancemaximum = None
            self.mteresourcesampleinstances = None
            self.mteresourcesampleinstanceshigh = None
            self.mteresourcesampleinstancelacks = None
            self._segment_path = lambda: "mteResource"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteResource, ['mteresourcesampleminimum', 'mteresourcesampleinstancemaximum', 'mteresourcesampleinstances', 'mteresourcesampleinstanceshigh', 'mteresourcesampleinstancelacks'], name, value)



    class MteTrigger(Entity):
        """
        
        
        .. attribute:: mtetriggerfailures
        
        	The number of times an attempt to check for a trigger condition has failed.  This counts individually for each attempt in a group of targets or each attempt for a  wildcarded object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: failures
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTrigger, self).__init__()

            self.yang_name = "mteTrigger"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mtetriggerfailures', (YLeaf(YType.uint32, 'mteTriggerFailures'), ['int'])),
            ])
            self.mtetriggerfailures = None
            self._segment_path = lambda: "mteTrigger"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTrigger, ['mtetriggerfailures'], name, value)



    class MteEvent(Entity):
        """
        
        
        .. attribute:: mteeventfailures
        
        	The number of times an attempt to invoke an event has failed.  This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteEvent, self).__init__()

            self.yang_name = "mteEvent"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mteeventfailures', (YLeaf(YType.uint32, 'mteEventFailures'), ['int'])),
            ])
            self.mteeventfailures = None
            self._segment_path = lambda: "mteEvent"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteEvent, ['mteeventfailures'], name, value)



    class MteTriggerTable(Entity):
        """
        A table of management event trigger information.
        
        .. attribute:: mtetriggerentry
        
        	Information about a single trigger.  Applications create and delete entries using mteTriggerEntryStatus
        	**type**\: list of  		 :py:class:`MteTriggerEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTriggerTable, self).__init__()

            self.yang_name = "mteTriggerTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteTriggerEntry", ("mtetriggerentry", DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry))])
            self._leafs = OrderedDict()

            self.mtetriggerentry = YList(self)
            self._segment_path = lambda: "mteTriggerTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTriggerTable, [], name, value)


        class MteTriggerEntry(Entity):
            """
            Information about a single trigger.  Applications create and
            delete entries using mteTriggerEntryStatus.
            
            .. attribute:: mteowner  (key)
            
            	The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggername  (key)
            
            	A locally\-unique, administratively assigned name for the trigger within the scope of mteOwner
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: mtetriggercomment
            
            	A description of the trigger's function and use
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mtetriggertest
            
            	The type of trigger test to perform.  For 'boolean' and 'threshold'  tests, the object at mteTriggerValueID MUST evaluate to an integer, that is, anything that ends up encoded for transmission (that is, in BER, not ASN.1) as an integer.  For 'existence', the specific test is as selected by mteTriggerExistenceTest.  When an object appears, vanishes or changes value, the trigger fires. If the object's appearance caused the trigger firing, the object MUST vanish before the trigger can be fired again for it, and vice versa. If the trigger fired due to a change in the object's value, it will be fired again on every successive value change for that object.  For 'boolean', the specific test is as selected by mteTriggerBooleanTest.  If the test result is true the trigger fires.  The trigger will not fire again until the value has become false and come back to true.  For 'threshold' the test works as described below for  mteTriggerThresholdStartup, mteTriggerThresholdRising, and mteTriggerThresholdFalling.  Note that combining 'boolean' and 'threshold' tests on the same object may be somewhat redundant
            	**type**\:  :py:class:`MteTriggerTest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerTest>`
            
            	**config**\: False
            
            .. attribute:: mtetriggersampletype
            
            	The type of sampling to perform.  An 'absoluteValue' sample requires only a single sample to be meaningful, and is exactly the value of the object at mteTriggerValueID at the sample time.  A 'deltaValue' requires two samples to be meaningful and is thus not available for testing until the second and subsequent samples after the object at mteTriggerValueID is first found to exist.  It is the difference between the two samples.  For unsigned values it is always positive, based on unsigned arithmetic.  For signed values it can be positive or negative.  For SNMP counters to be meaningful they should be sampled as a 'deltaValue'.  For 'deltaValue' mteTriggerDeltaTable contains further parameters.  If only 'existence' is set in mteTriggerTest this object has no meaning
            	**type**\:  :py:class:`MteTriggerSampleType <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerSampleType>`
            
            	**config**\: False
            
            .. attribute:: mtetriggervalueid
            
            	The object identifier of the MIB object to sample to see if the trigger should fire.  This may be wildcarded by truncating all or part of the instance portion, in which case the value is obtained as if with a GetNext function, checking multiple values  if they exist.  If such wildcarding is applied, mteTriggerValueIDWildcard must be 'true' and if not it must be 'false'.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteTriggerValueIDWildcard result in operation as one would expect when providing the wrong identifier to a Get or GetNext operation.  The Get will fail or get the wrong object.  The GetNext will indeed get whatever is next, proceeding until it runs past the initial part of the identifier and perhaps many unintended objects for confusing results.  If the value syntax of those objects is not usable, that results in a 'badType' error that terminates the scan.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: mtetriggervalueidwildcard
            
            	Control for whether mteTriggerValueID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mtetriggertargettag
            
            	The tag for the target(s) from which to obtain the condition for a trigger check.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteTriggerValueID is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security  parameters resulting from the tag
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mtetriggercontextname
            
            	The management context from which to obtain mteTriggerValueID.  This may be wildcarded by leaving characters off the end.  For example use 'Repeater' to wildcard to 'Repeater1', 'Repeater2', 'Repeater\-999.87b', and so on.  To indicate such wildcarding is intended, mteTriggerContextNameWildcard must be 'true'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Operation of this feature assumes that the local system has a list of available contexts against which to apply the wildcard.  If the objects are being read from the local system, this is clearly the system's own list of contexts. For a remote system a local version of such a list is not defined by any current standard and may not be available, so this function MAY not be supported
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mtetriggercontextnamewildcard
            
            	Control for whether mteTriggerContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mtetriggerfrequency
            
            	The number of seconds to wait between trigger samples.  To encourage consistency in sampling, the interval is measured from the beginning of one check to the beginning of the next and the timer is restarted immediately when it expires, not when the check completes.  If the next sample begins before the previous one completed the system may either attempt to make the check or treat this as an error condition with the error 'sampleOverrun'.  A frequency of 0 indicates instantaneous recognition of the condition.  This is not possible in many cases, but may be supported in cases where it makes sense and the system is able to do so.  This feature allows the MIB to be used in implementations where such interrupt\-driven behavior is possible and is not likely to be supported for all MIB objects even then since such sampling generally has to be tightly integrated into low\-level code.  Systems that can support this SHOULD document those cases where it can be used.  In cases where it can not, setting this object to 0 should be disallowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: mtetriggerobjectsowner
            
            	To go with mteTriggerObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger.  A list of objects may also be added based on the event or on the value of mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerenabled
            
            	A control to allow a trigger to be configured but not used. When the value is 'false' the trigger is not sampled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mtetriggerentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry may not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry, self).__init__()

                self.yang_name = "mteTriggerEntry"
                self.yang_parent_name = "mteTriggerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mtetriggername', (YLeaf(YType.str, 'mteTriggerName'), ['str'])),
                    ('mtetriggercomment', (YLeaf(YType.str, 'mteTriggerComment'), ['str'])),
                    ('mtetriggertest', (YLeaf(YType.bits, 'mteTriggerTest'), ['Bits'])),
                    ('mtetriggersampletype', (YLeaf(YType.enumeration, 'mteTriggerSampleType'), [('ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DISMANEVENTMIB', 'MteTriggerTable.MteTriggerEntry.MteTriggerSampleType')])),
                    ('mtetriggervalueid', (YLeaf(YType.str, 'mteTriggerValueID'), ['str'])),
                    ('mtetriggervalueidwildcard', (YLeaf(YType.boolean, 'mteTriggerValueIDWildcard'), ['bool'])),
                    ('mtetriggertargettag', (YLeaf(YType.str, 'mteTriggerTargetTag'), ['str'])),
                    ('mtetriggercontextname', (YLeaf(YType.str, 'mteTriggerContextName'), ['str'])),
                    ('mtetriggercontextnamewildcard', (YLeaf(YType.boolean, 'mteTriggerContextNameWildcard'), ['bool'])),
                    ('mtetriggerfrequency', (YLeaf(YType.uint32, 'mteTriggerFrequency'), ['int'])),
                    ('mtetriggerobjectsowner', (YLeaf(YType.str, 'mteTriggerObjectsOwner'), ['str'])),
                    ('mtetriggerobjects', (YLeaf(YType.str, 'mteTriggerObjects'), ['str'])),
                    ('mtetriggerenabled', (YLeaf(YType.boolean, 'mteTriggerEnabled'), ['bool'])),
                    ('mtetriggerentrystatus', (YLeaf(YType.enumeration, 'mteTriggerEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggercomment = None
                self.mtetriggertest = Bits()
                self.mtetriggersampletype = None
                self.mtetriggervalueid = None
                self.mtetriggervalueidwildcard = None
                self.mtetriggertargettag = None
                self.mtetriggercontextname = None
                self.mtetriggercontextnamewildcard = None
                self.mtetriggerfrequency = None
                self.mtetriggerobjectsowner = None
                self.mtetriggerobjects = None
                self.mtetriggerenabled = None
                self.mtetriggerentrystatus = None
                self._segment_path = lambda: "mteTriggerEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry, ['mteowner', 'mtetriggername', 'mtetriggercomment', 'mtetriggertest', 'mtetriggersampletype', 'mtetriggervalueid', 'mtetriggervalueidwildcard', 'mtetriggertargettag', 'mtetriggercontextname', 'mtetriggercontextnamewildcard', 'mtetriggerfrequency', 'mtetriggerobjectsowner', 'mtetriggerobjects', 'mtetriggerenabled', 'mtetriggerentrystatus'], name, value)

            class MteTriggerSampleType(Enum):
                """
                MteTriggerSampleType (Enum Class)

                The type of sampling to perform.

                An 'absoluteValue' sample requires only a single sample to be

                meaningful, and is exactly the value of the object at

                mteTriggerValueID at the sample time.

                A 'deltaValue' requires two samples to be meaningful and is

                thus not available for testing until the second and subsequent

                samples after the object at mteTriggerValueID is first found

                to exist.  It is the difference between the two samples.  For

                unsigned values it is always positive, based on unsigned

                arithmetic.  For signed values it can be positive or negative.

                For SNMP counters to be meaningful they should be sampled as a

                'deltaValue'.

                For 'deltaValue' mteTriggerDeltaTable contains further

                parameters.

                If only 'existence' is set in mteTriggerTest this object has

                no meaning.

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")





    class MteTriggerDeltaTable(Entity):
        """
        A table of management event trigger information for delta
        sampling.
        
        .. attribute:: mtetriggerdeltaentry
        
        	Information about a single trigger's delta sampling.  Entries automatically exist in this this table for each mteTriggerEntry that has mteTriggerSampleType set to 'deltaValue'
        	**type**\: list of  		 :py:class:`MteTriggerDeltaEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTriggerDeltaTable, self).__init__()

            self.yang_name = "mteTriggerDeltaTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteTriggerDeltaEntry", ("mtetriggerdeltaentry", DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry))])
            self._leafs = OrderedDict()

            self.mtetriggerdeltaentry = YList(self)
            self._segment_path = lambda: "mteTriggerDeltaTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTriggerDeltaTable, [], name, value)


        class MteTriggerDeltaEntry(Entity):
            """
            Information about a single trigger's delta sampling.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has mteTriggerSampleType set to 'deltaValue'.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at mteTriggerValueID.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match mteTriggerValueID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking MUST still check sysUpTime for an overall discontinuity.  If the object identified is not accessible the sample attempt is in error, with the error code as from an SNMP request.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the value syntax of those objects is not usable, that results in an error that terminates the sample with a 'badType' error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: mtetriggerdeltadiscontinuityidwildcard
            
            	Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding  mteTriggerSampleType is 'deltaValue'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mtetriggerdeltadiscontinuityidtype
            
            	The value 'timeTicks' indicates the mteTriggerDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp. The value 'dateAndTime' indicates syntax DateAndTime
            	**type**\:  :py:class:`MteTriggerDeltaDiscontinuityIDType <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry.MteTriggerDeltaDiscontinuityIDType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry, self).__init__()

                self.yang_name = "mteTriggerDeltaEntry"
                self.yang_parent_name = "mteTriggerDeltaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mtetriggername', (YLeaf(YType.str, 'mteTriggerName'), ['str'])),
                    ('mtetriggerdeltadiscontinuityid', (YLeaf(YType.str, 'mteTriggerDeltaDiscontinuityID'), ['str'])),
                    ('mtetriggerdeltadiscontinuityidwildcard', (YLeaf(YType.boolean, 'mteTriggerDeltaDiscontinuityIDWildcard'), ['bool'])),
                    ('mtetriggerdeltadiscontinuityidtype', (YLeaf(YType.enumeration, 'mteTriggerDeltaDiscontinuityIDType'), [('ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DISMANEVENTMIB', 'MteTriggerDeltaTable.MteTriggerDeltaEntry.MteTriggerDeltaDiscontinuityIDType')])),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerdeltadiscontinuityid = None
                self.mtetriggerdeltadiscontinuityidwildcard = None
                self.mtetriggerdeltadiscontinuityidtype = None
                self._segment_path = lambda: "mteTriggerDeltaEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerDeltaTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry, ['mteowner', 'mtetriggername', 'mtetriggerdeltadiscontinuityid', 'mtetriggerdeltadiscontinuityidwildcard', 'mtetriggerdeltadiscontinuityidtype'], name, value)

            class MteTriggerDeltaDiscontinuityIDType(Enum):
                """
                MteTriggerDeltaDiscontinuityIDType (Enum Class)

                The value 'timeTicks' indicates the

                mteTriggerDeltaDiscontinuityID of this row is of syntax

                TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp.

                The value 'dateAndTime' indicates syntax DateAndTime.

                .. data:: timeTicks = 1

                .. data:: timeStamp = 2

                .. data:: dateAndTime = 3

                """

                timeTicks = Enum.YLeaf(1, "timeTicks")

                timeStamp = Enum.YLeaf(2, "timeStamp")

                dateAndTime = Enum.YLeaf(3, "dateAndTime")





    class MteTriggerExistenceTable(Entity):
        """
        A table of management event trigger information for existence
        triggers.
        
        .. attribute:: mtetriggerexistenceentry
        
        	Information about a single existence trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'existence' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`MteTriggerExistenceEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTriggerExistenceTable, self).__init__()

            self.yang_name = "mteTriggerExistenceTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteTriggerExistenceEntry", ("mtetriggerexistenceentry", DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry))])
            self._leafs = OrderedDict()

            self.mtetriggerexistenceentry = YList(self)
            self._segment_path = lambda: "mteTriggerExistenceTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTriggerExistenceTable, [], name, value)


        class MteTriggerExistenceEntry(Entity):
            """
            Information about a single existence trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'existence' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistencetest
            
            	The type of existence test to perform.  The trigger fires when the object at mteTriggerValueID is seen to go from present to absent, from absent to present, or to have it's value changed, depending on which tests are selected\:  present(0) \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from absent to present.  absent(1)  \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from present to absent. changed(2) \- when this test is selected, the trigger fires the mteTriggerValueID object value changes.  Once the trigger has fired for either presence or absence it will not fire again for that state until the object has been to the other state. 
            	**type**\:  :py:class:`MteTriggerExistenceTest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceTest>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistencestartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' and the test specified by mteTriggerExistenceTest is true.  Setting an option causes that trigger to fire when its test is true
            	**type**\:  :py:class:`MteTriggerExistenceStartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceStartup>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistenceobjectsowner
            
            	To go with mteTriggerExistenceObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistenceobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistenceeventowner
            
            	To go with mteTriggerExistenceEvent, the mteOwner of an event entry from the mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerexistenceevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'existence' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry, self).__init__()

                self.yang_name = "mteTriggerExistenceEntry"
                self.yang_parent_name = "mteTriggerExistenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mtetriggername', (YLeaf(YType.str, 'mteTriggerName'), ['str'])),
                    ('mtetriggerexistencetest', (YLeaf(YType.bits, 'mteTriggerExistenceTest'), ['Bits'])),
                    ('mtetriggerexistencestartup', (YLeaf(YType.bits, 'mteTriggerExistenceStartup'), ['Bits'])),
                    ('mtetriggerexistenceobjectsowner', (YLeaf(YType.str, 'mteTriggerExistenceObjectsOwner'), ['str'])),
                    ('mtetriggerexistenceobjects', (YLeaf(YType.str, 'mteTriggerExistenceObjects'), ['str'])),
                    ('mtetriggerexistenceeventowner', (YLeaf(YType.str, 'mteTriggerExistenceEventOwner'), ['str'])),
                    ('mtetriggerexistenceevent', (YLeaf(YType.str, 'mteTriggerExistenceEvent'), ['str'])),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerexistencetest = Bits()
                self.mtetriggerexistencestartup = Bits()
                self.mtetriggerexistenceobjectsowner = None
                self.mtetriggerexistenceobjects = None
                self.mtetriggerexistenceeventowner = None
                self.mtetriggerexistenceevent = None
                self._segment_path = lambda: "mteTriggerExistenceEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerExistenceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry, ['mteowner', 'mtetriggername', 'mtetriggerexistencetest', 'mtetriggerexistencestartup', 'mtetriggerexistenceobjectsowner', 'mtetriggerexistenceobjects', 'mtetriggerexistenceeventowner', 'mtetriggerexistenceevent'], name, value)




    class MteTriggerBooleanTable(Entity):
        """
        A table of management event trigger information for boolean
        triggers.
        
        .. attribute:: mtetriggerbooleanentry
        
        	Information about a single boolean trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'boolean' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`MteTriggerBooleanEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTriggerBooleanTable, self).__init__()

            self.yang_name = "mteTriggerBooleanTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteTriggerBooleanEntry", ("mtetriggerbooleanentry", DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry))])
            self._leafs = OrderedDict()

            self.mtetriggerbooleanentry = YList(self)
            self._segment_path = lambda: "mteTriggerBooleanTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTriggerBooleanTable, [], name, value)


        class MteTriggerBooleanEntry(Entity):
            """
            Information about a single boolean trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'boolean' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleancomparison
            
            	The type of boolean comparison to perform.  The value at mteTriggerValueID is compared to mteTriggerBooleanValue, so for example if mteTriggerBooleanComparison is 'less' the result would be true if the value at mteTriggerValueID is less than the value of mteTriggerBooleanValue
            	**type**\:  :py:class:`MteTriggerBooleanComparison <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry.MteTriggerBooleanComparison>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleanvalue
            
            	The value to use for the test specified by mteTriggerBooleanTest
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleanstartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' or a new instance of the object at mteTriggerValueID is found and the test specified by mteTriggerBooleanComparison is true.  In that case an event is triggered if mteTriggerBooleanStartup is 'true'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleanobjectsowner
            
            	To go with mteTriggerBooleanObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleanobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleaneventowner
            
            	To go with mteTriggerBooleanEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerbooleanevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'boolean' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry, self).__init__()

                self.yang_name = "mteTriggerBooleanEntry"
                self.yang_parent_name = "mteTriggerBooleanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mtetriggername', (YLeaf(YType.str, 'mteTriggerName'), ['str'])),
                    ('mtetriggerbooleancomparison', (YLeaf(YType.enumeration, 'mteTriggerBooleanComparison'), [('ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DISMANEVENTMIB', 'MteTriggerBooleanTable.MteTriggerBooleanEntry.MteTriggerBooleanComparison')])),
                    ('mtetriggerbooleanvalue', (YLeaf(YType.int32, 'mteTriggerBooleanValue'), ['int'])),
                    ('mtetriggerbooleanstartup', (YLeaf(YType.boolean, 'mteTriggerBooleanStartup'), ['bool'])),
                    ('mtetriggerbooleanobjectsowner', (YLeaf(YType.str, 'mteTriggerBooleanObjectsOwner'), ['str'])),
                    ('mtetriggerbooleanobjects', (YLeaf(YType.str, 'mteTriggerBooleanObjects'), ['str'])),
                    ('mtetriggerbooleaneventowner', (YLeaf(YType.str, 'mteTriggerBooleanEventOwner'), ['str'])),
                    ('mtetriggerbooleanevent', (YLeaf(YType.str, 'mteTriggerBooleanEvent'), ['str'])),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerbooleancomparison = None
                self.mtetriggerbooleanvalue = None
                self.mtetriggerbooleanstartup = None
                self.mtetriggerbooleanobjectsowner = None
                self.mtetriggerbooleanobjects = None
                self.mtetriggerbooleaneventowner = None
                self.mtetriggerbooleanevent = None
                self._segment_path = lambda: "mteTriggerBooleanEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerBooleanTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry, ['mteowner', 'mtetriggername', 'mtetriggerbooleancomparison', 'mtetriggerbooleanvalue', 'mtetriggerbooleanstartup', 'mtetriggerbooleanobjectsowner', 'mtetriggerbooleanobjects', 'mtetriggerbooleaneventowner', 'mtetriggerbooleanevent'], name, value)

            class MteTriggerBooleanComparison(Enum):
                """
                MteTriggerBooleanComparison (Enum Class)

                The type of boolean comparison to perform.

                The value at mteTriggerValueID is compared to

                mteTriggerBooleanValue, so for example if

                mteTriggerBooleanComparison is 'less' the result would be true

                if the value at mteTriggerValueID is less than the value of

                mteTriggerBooleanValue.

                .. data:: unequal = 1

                .. data:: equal = 2

                .. data:: less = 3

                .. data:: lessOrEqual = 4

                .. data:: greater = 5

                .. data:: greaterOrEqual = 6

                """

                unequal = Enum.YLeaf(1, "unequal")

                equal = Enum.YLeaf(2, "equal")

                less = Enum.YLeaf(3, "less")

                lessOrEqual = Enum.YLeaf(4, "lessOrEqual")

                greater = Enum.YLeaf(5, "greater")

                greaterOrEqual = Enum.YLeaf(6, "greaterOrEqual")





    class MteTriggerThresholdTable(Entity):
        """
        A table of management event trigger information for threshold
        triggers.
        
        .. attribute:: mtetriggerthresholdentry
        
        	Information about a single threshold trigger.  Entries automatically exist in this table for each mteTriggerEntry that has 'threshold' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`MteTriggerThresholdEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteTriggerThresholdTable, self).__init__()

            self.yang_name = "mteTriggerThresholdTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteTriggerThresholdEntry", ("mtetriggerthresholdentry", DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry))])
            self._leafs = OrderedDict()

            self.mtetriggerthresholdentry = YList(self)
            self._segment_path = lambda: "mteTriggerThresholdTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteTriggerThresholdTable, [], name, value)


        class MteTriggerThresholdEntry(Entity):
            """
            Information about a single threshold trigger.  Entries
            automatically exist in this table for each mteTriggerEntry
            that has 'threshold' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdstartup
            
            	The event that may be triggered when this entry is first set to 'active' and a new instance of the object at mteTriggerValueID is found.  If the first sample after this instance becomes active is greater than or equal to mteTriggerThresholdRising and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance. If the first sample after this entry becomes active is less than or equal to mteTriggerThresholdFalling and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance
            	**type**\:  :py:class:`MteTriggerThresholdStartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry.MteTriggerThresholdStartup>`
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdrising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, one mteTriggerThresholdRisingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is greater than or equal to this threshold and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling'.  After a rising event is generated, another such event is not triggered until the sampled value falls below this threshold and reaches mteTriggerThresholdFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdfalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, one mteTriggerThresholdFallingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is less than or equal to this threshold and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling'.  After a falling event is generated, another such event is not triggered until the sampled value rises above this threshold and reaches mteTriggerThresholdRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltarising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is greater than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was less than this threshold, one mteTriggerThresholdDeltaRisingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is greater than or equal to this threshold.  After a rising event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltafalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is less than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was greater than this threshold, one mteTriggerThresholdDeltaFallingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is less than or equal to this threshold.  After a falling event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdobjectsowner
            
            	To go with mteTriggerThresholdObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall  trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdrisingeventowner
            
            	To go with mteTriggerThresholdRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdrisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdRising.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdfallingeventowner
            
            	To go with mteTriggerThresholdFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholdfallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltarisingeventowner
            
            	To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltarisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaRising. A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltafallingeventowner
            
            	To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mtetriggerthresholddeltafallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry, self).__init__()

                self.yang_name = "mteTriggerThresholdEntry"
                self.yang_parent_name = "mteTriggerThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mtetriggername', (YLeaf(YType.str, 'mteTriggerName'), ['str'])),
                    ('mtetriggerthresholdstartup', (YLeaf(YType.enumeration, 'mteTriggerThresholdStartup'), [('ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DISMANEVENTMIB', 'MteTriggerThresholdTable.MteTriggerThresholdEntry.MteTriggerThresholdStartup')])),
                    ('mtetriggerthresholdrising', (YLeaf(YType.int32, 'mteTriggerThresholdRising'), ['int'])),
                    ('mtetriggerthresholdfalling', (YLeaf(YType.int32, 'mteTriggerThresholdFalling'), ['int'])),
                    ('mtetriggerthresholddeltarising', (YLeaf(YType.int32, 'mteTriggerThresholdDeltaRising'), ['int'])),
                    ('mtetriggerthresholddeltafalling', (YLeaf(YType.int32, 'mteTriggerThresholdDeltaFalling'), ['int'])),
                    ('mtetriggerthresholdobjectsowner', (YLeaf(YType.str, 'mteTriggerThresholdObjectsOwner'), ['str'])),
                    ('mtetriggerthresholdobjects', (YLeaf(YType.str, 'mteTriggerThresholdObjects'), ['str'])),
                    ('mtetriggerthresholdrisingeventowner', (YLeaf(YType.str, 'mteTriggerThresholdRisingEventOwner'), ['str'])),
                    ('mtetriggerthresholdrisingevent', (YLeaf(YType.str, 'mteTriggerThresholdRisingEvent'), ['str'])),
                    ('mtetriggerthresholdfallingeventowner', (YLeaf(YType.str, 'mteTriggerThresholdFallingEventOwner'), ['str'])),
                    ('mtetriggerthresholdfallingevent', (YLeaf(YType.str, 'mteTriggerThresholdFallingEvent'), ['str'])),
                    ('mtetriggerthresholddeltarisingeventowner', (YLeaf(YType.str, 'mteTriggerThresholdDeltaRisingEventOwner'), ['str'])),
                    ('mtetriggerthresholddeltarisingevent', (YLeaf(YType.str, 'mteTriggerThresholdDeltaRisingEvent'), ['str'])),
                    ('mtetriggerthresholddeltafallingeventowner', (YLeaf(YType.str, 'mteTriggerThresholdDeltaFallingEventOwner'), ['str'])),
                    ('mtetriggerthresholddeltafallingevent', (YLeaf(YType.str, 'mteTriggerThresholdDeltaFallingEvent'), ['str'])),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerthresholdstartup = None
                self.mtetriggerthresholdrising = None
                self.mtetriggerthresholdfalling = None
                self.mtetriggerthresholddeltarising = None
                self.mtetriggerthresholddeltafalling = None
                self.mtetriggerthresholdobjectsowner = None
                self.mtetriggerthresholdobjects = None
                self.mtetriggerthresholdrisingeventowner = None
                self.mtetriggerthresholdrisingevent = None
                self.mtetriggerthresholdfallingeventowner = None
                self.mtetriggerthresholdfallingevent = None
                self.mtetriggerthresholddeltarisingeventowner = None
                self.mtetriggerthresholddeltarisingevent = None
                self.mtetriggerthresholddeltafallingeventowner = None
                self.mtetriggerthresholddeltafallingevent = None
                self._segment_path = lambda: "mteTriggerThresholdEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerThresholdTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry, ['mteowner', 'mtetriggername', 'mtetriggerthresholdstartup', 'mtetriggerthresholdrising', 'mtetriggerthresholdfalling', 'mtetriggerthresholddeltarising', 'mtetriggerthresholddeltafalling', 'mtetriggerthresholdobjectsowner', 'mtetriggerthresholdobjects', 'mtetriggerthresholdrisingeventowner', 'mtetriggerthresholdrisingevent', 'mtetriggerthresholdfallingeventowner', 'mtetriggerthresholdfallingevent', 'mtetriggerthresholddeltarisingeventowner', 'mtetriggerthresholddeltarisingevent', 'mtetriggerthresholddeltafallingeventowner', 'mtetriggerthresholddeltafallingevent'], name, value)

            class MteTriggerThresholdStartup(Enum):
                """
                MteTriggerThresholdStartup (Enum Class)

                The event that may be triggered when this entry is first

                set to 'active' and a new instance of the object at

                mteTriggerValueID is found.  If the first sample after this

                instance becomes active is greater than or equal to

                mteTriggerThresholdRising and mteTriggerThresholdStartup is

                equal to 'rising' or 'risingOrFalling', then one

                mteTriggerThresholdRisingEvent is triggered for that instance.

                If the first sample after this entry becomes active is less

                than or equal to mteTriggerThresholdFalling and

                mteTriggerThresholdStartup is equal to 'falling' or

                'risingOrFalling', then one mteTriggerThresholdRisingEvent is

                triggered for that instance.

                .. data:: rising = 1

                .. data:: falling = 2

                .. data:: risingOrFalling = 3

                """

                rising = Enum.YLeaf(1, "rising")

                falling = Enum.YLeaf(2, "falling")

                risingOrFalling = Enum.YLeaf(3, "risingOrFalling")





    class MteObjectsTable(Entity):
        """
        A table of objects that can be added to notifications based
        on the trigger, trigger test, or event, as pointed to by
        entries in those tables.
        
        .. attribute:: mteobjectsentry
        
        	A group of objects.  Applications create and delete entries using mteObjectsEntryStatus.  When adding objects to a notification they are added in the lexical order of their index in this table.  Those associated with a trigger come first, then trigger test, then event
        	**type**\: list of  		 :py:class:`MteObjectsEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteObjectsTable, self).__init__()

            self.yang_name = "mteObjectsTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteObjectsEntry", ("mteobjectsentry", DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry))])
            self._leafs = OrderedDict()

            self.mteobjectsentry = YList(self)
            self._segment_path = lambda: "mteObjectsTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteObjectsTable, [], name, value)


        class MteObjectsEntry(Entity):
            """
            A group of objects.  Applications create and delete entries
            using mteObjectsEntryStatus.
            
            When adding objects to a notification they are added in the
            lexical order of their index in this table.  Those associated
            with a trigger come first, then trigger test, then event.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mteobjectsname  (key)
            
            	A locally\-unique, administratively assigned name for a group of objects
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: mteobjectsindex  (key)
            
            	An arbitrary integer for the purpose of identifying individual objects within a mteObjectsName group.  Objects within a group are placed in the notification in the numerical order of this index.  Groups are placed in the notification in the order of the selections for overall trigger, trigger test, and event. Within trigger test they are in the same order as the numerical values of the bits defined for mteTriggerTest.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the object is not available it is omitted from the notification
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mteobjectsid
            
            	The object identifier of a MIB object to add to a Notification that results from the firing of a trigger.  This may be wildcarded by truncating all or part of the instance portion, in which case the instance portion of the OID for obtaining this object will be the same as that used in obtaining the mteTriggerValueID that fired.  If such wildcarding is applied, mteObjectsIDWildcard must be 'true' and if not it must be 'false'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: mteobjectsidwildcard
            
            	Control for whether mteObjectsID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mteobjectsentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry, self).__init__()

                self.yang_name = "mteObjectsEntry"
                self.yang_parent_name = "mteObjectsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteobjectsname','mteobjectsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mteobjectsname', (YLeaf(YType.str, 'mteObjectsName'), ['str'])),
                    ('mteobjectsindex', (YLeaf(YType.uint32, 'mteObjectsIndex'), ['int'])),
                    ('mteobjectsid', (YLeaf(YType.str, 'mteObjectsID'), ['str'])),
                    ('mteobjectsidwildcard', (YLeaf(YType.boolean, 'mteObjectsIDWildcard'), ['bool'])),
                    ('mteobjectsentrystatus', (YLeaf(YType.enumeration, 'mteObjectsEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.mteowner = None
                self.mteobjectsname = None
                self.mteobjectsindex = None
                self.mteobjectsid = None
                self.mteobjectsidwildcard = None
                self.mteobjectsentrystatus = None
                self._segment_path = lambda: "mteObjectsEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteObjectsName='" + str(self.mteobjectsname) + "']" + "[mteObjectsIndex='" + str(self.mteobjectsindex) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteObjectsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry, ['mteowner', 'mteobjectsname', 'mteobjectsindex', 'mteobjectsid', 'mteobjectsidwildcard', 'mteobjectsentrystatus'], name, value)




    class MteEventTable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteevententry
        
        	Information about a single event.  Applications create and delete entries using mteEventEntryStatus
        	**type**\: list of  		 :py:class:`MteEventEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteEventTable, self).__init__()

            self.yang_name = "mteEventTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteEventEntry", ("mteevententry", DISMANEVENTMIB.MteEventTable.MteEventEntry))])
            self._leafs = OrderedDict()

            self.mteevententry = YList(self)
            self._segment_path = lambda: "mteEventTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteEventTable, [], name, value)


        class MteEventEntry(Entity):
            """
            Information about a single event.  Applications create and
            delete entries using mteEventEntryStatus.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mteeventname  (key)
            
            	A locally\-unique, administratively assigned name for the event
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: mteeventcomment
            
            	A description of the event's function and use
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mteeventactions
            
            	The actions to perform when this event occurs.  For 'notification', Traps and/or Informs are sent according to the configuration in the SNMP Notification MIB.  For 'set', an SNMP Set operation is performed according to control values in this entry
            	**type**\:  :py:class:`MteEventActions <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry.MteEventActions>`
            
            	**config**\: False
            
            .. attribute:: mteeventenabled
            
            	A control to allow an event to be configured but not used. When the value is 'false' the event does not execute even if  triggered
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mteevententrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteEventTable.MteEventEntry, self).__init__()

                self.yang_name = "mteEventEntry"
                self.yang_parent_name = "mteEventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mteeventname', (YLeaf(YType.str, 'mteEventName'), ['str'])),
                    ('mteeventcomment', (YLeaf(YType.str, 'mteEventComment'), ['str'])),
                    ('mteeventactions', (YLeaf(YType.bits, 'mteEventActions'), ['Bits'])),
                    ('mteeventenabled', (YLeaf(YType.boolean, 'mteEventEnabled'), ['bool'])),
                    ('mteevententrystatus', (YLeaf(YType.enumeration, 'mteEventEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.mteowner = None
                self.mteeventname = None
                self.mteeventcomment = None
                self.mteeventactions = Bits()
                self.mteeventenabled = None
                self.mteevententrystatus = None
                self._segment_path = lambda: "mteEventEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteEventName='" + str(self.mteeventname) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteEventTable.MteEventEntry, ['mteowner', 'mteeventname', 'mteeventcomment', 'mteeventactions', 'mteeventenabled', 'mteevententrystatus'], name, value)




    class MteEventNotificationTable(Entity):
        """
        A table of information about notifications to be sent as a
        consequence of management events.
        
        .. attribute:: mteeventnotificationentry
        
        	Information about a single event's notification.  Entries automatically exist in this this table for each mteEventEntry that has 'notification' set in mteEventActions
        	**type**\: list of  		 :py:class:`MteEventNotificationEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteEventNotificationTable, self).__init__()

            self.yang_name = "mteEventNotificationTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteEventNotificationEntry", ("mteeventnotificationentry", DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry))])
            self._leafs = OrderedDict()

            self.mteeventnotificationentry = YList(self)
            self._segment_path = lambda: "mteEventNotificationTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteEventNotificationTable, [], name, value)


        class MteEventNotificationEntry(Entity):
            """
            Information about a single event's notification.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'notification' set in mteEventActions.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mteeventname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry>`
            
            	**config**\: False
            
            .. attribute:: mteeventnotification
            
            	The object identifier from the NOTIFICATION\-TYPE for the notification to use if metEventActions has 'notification' set
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: mteeventnotificationobjectsowner
            
            	To go with mteEventNotificationObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: mteeventnotificationobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable if mteEventActions has 'notification' set. These objects are to be added to any Notification generated by this event.  Objects may also be added based on the trigger that stimulated the event.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry, self).__init__()

                self.yang_name = "mteEventNotificationEntry"
                self.yang_parent_name = "mteEventNotificationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mteeventname', (YLeaf(YType.str, 'mteEventName'), ['str'])),
                    ('mteeventnotification', (YLeaf(YType.str, 'mteEventNotification'), ['str'])),
                    ('mteeventnotificationobjectsowner', (YLeaf(YType.str, 'mteEventNotificationObjectsOwner'), ['str'])),
                    ('mteeventnotificationobjects', (YLeaf(YType.str, 'mteEventNotificationObjects'), ['str'])),
                ])
                self.mteowner = None
                self.mteeventname = None
                self.mteeventnotification = None
                self.mteeventnotificationobjectsowner = None
                self.mteeventnotificationobjects = None
                self._segment_path = lambda: "mteEventNotificationEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteEventName='" + str(self.mteeventname) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventNotificationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry, ['mteowner', 'mteeventname', 'mteeventnotification', 'mteeventnotificationobjectsowner', 'mteeventnotificationobjects'], name, value)




    class MteEventSetTable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteeventsetentry
        
        	Information about a single event's set option.  Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions
        	**type**\: list of  		 :py:class:`MteEventSetEntry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.MteEventSetTable, self).__init__()

            self.yang_name = "mteEventSetTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mteEventSetEntry", ("mteeventsetentry", DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry))])
            self._leafs = OrderedDict()

            self.mteeventsetentry = YList(self)
            self._segment_path = lambda: "mteEventSetTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.MteEventSetTable, [], name, value)


        class MteEventSetEntry(Entity):
            """
            Information about a single event's set option.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'set' set in mteEventActions.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
            
            	**config**\: False
            
            .. attribute:: mteeventname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry>`
            
            	**config**\: False
            
            .. attribute:: mteeventsetobject
            
            	The object identifier from the MIB object to set if mteEventActions has 'set' set.  This object identifier may be wildcarded by leaving sub\-identifiers off the end, in which case nteEventSetObjectWildCard must be 'true'.  If mteEventSetObject is wildcarded the instance used to set the object to which it points is the same as the instance from the value of mteTriggerValueID that triggered the event.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteSetObjectWildcard result in operation as one would expect when providing the wrong identifier to a Set operation.  The Set will fail or set the wrong object.  If the value syntax of the destination object is not correct, the Set fails with the normal SNMP error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: mteeventsetobjectwildcard
            
            	Control over whether mteEventSetObject is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mteeventsetvalue
            
            	The value to which to set the object at mteEventSetObject if mteEventActions has 'set' set
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: mteeventsettargettag
            
            	The tag for the target(s) at which to set the object at mteEventSetObject to mteEventSetValue if mteEventActions has 'set' set.  Systems limited to self management MAY reject a non\-zero length for the value of this object.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteEventSetObject is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security parameters resulting from the tag
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mteeventsetcontextname
            
            	The management context in which to set mteEventObjectID. if mteEventActions has 'set' set.  This may be wildcarded by leaving characters off the end.  To indicate such wildcarding mteEventSetContextNameWildcard must be 'true'.  If this context name is wildcarded the value used to complete the wildcarding of mteTriggerContextName will be appended
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mteeventsetcontextnamewildcard
            
            	Control for whether mteEventSetContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry, self).__init__()

                self.yang_name = "mteEventSetEntry"
                self.yang_parent_name = "mteEventSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', (YLeaf(YType.str, 'mteOwner'), ['str'])),
                    ('mteeventname', (YLeaf(YType.str, 'mteEventName'), ['str'])),
                    ('mteeventsetobject', (YLeaf(YType.str, 'mteEventSetObject'), ['str'])),
                    ('mteeventsetobjectwildcard', (YLeaf(YType.boolean, 'mteEventSetObjectWildcard'), ['bool'])),
                    ('mteeventsetvalue', (YLeaf(YType.int32, 'mteEventSetValue'), ['int'])),
                    ('mteeventsettargettag', (YLeaf(YType.str, 'mteEventSetTargetTag'), ['str'])),
                    ('mteeventsetcontextname', (YLeaf(YType.str, 'mteEventSetContextName'), ['str'])),
                    ('mteeventsetcontextnamewildcard', (YLeaf(YType.boolean, 'mteEventSetContextNameWildcard'), ['bool'])),
                ])
                self.mteowner = None
                self.mteeventname = None
                self.mteeventsetobject = None
                self.mteeventsetobjectwildcard = None
                self.mteeventsetvalue = None
                self.mteeventsettargettag = None
                self.mteeventsetcontextname = None
                self.mteeventsetcontextnamewildcard = None
                self._segment_path = lambda: "mteEventSetEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteEventName='" + str(self.mteeventname) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventSetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry, ['mteowner', 'mteeventname', 'mteeventsetobject', 'mteeventsetobjectwildcard', 'mteeventsetvalue', 'mteeventsettargettag', 'mteeventsetcontextname', 'mteeventsetcontextnamewildcard'], name, value)



    def clone_ptr(self):
        self._top_entity = DISMANEVENTMIB()
        return self._top_entity



