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
    
    	
    	**type**\:  :py:class:`Mteresource <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteresource>`
    
    .. attribute:: mtetrigger
    
    	
    	**type**\:  :py:class:`Mtetrigger <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetrigger>`
    
    .. attribute:: mteevent
    
    	
    	**type**\:  :py:class:`Mteevent <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteevent>`
    
    .. attribute:: mtetriggertable
    
    	A table of management event trigger information
    	**type**\:  :py:class:`Mtetriggertable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable>`
    
    .. attribute:: mtetriggerdeltatable
    
    	A table of management event trigger information for delta sampling
    	**type**\:  :py:class:`Mtetriggerdeltatable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerdeltatable>`
    
    .. attribute:: mtetriggerexistencetable
    
    	A table of management event trigger information for existence triggers
    	**type**\:  :py:class:`Mtetriggerexistencetable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerexistencetable>`
    
    .. attribute:: mtetriggerbooleantable
    
    	A table of management event trigger information for boolean triggers
    	**type**\:  :py:class:`Mtetriggerbooleantable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerbooleantable>`
    
    .. attribute:: mtetriggerthresholdtable
    
    	A table of management event trigger information for threshold triggers
    	**type**\:  :py:class:`Mtetriggerthresholdtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerthresholdtable>`
    
    .. attribute:: mteobjectstable
    
    	A table of objects that can be added to notifications based on the trigger, trigger test, or event, as pointed to by entries in those tables
    	**type**\:  :py:class:`Mteobjectstable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteobjectstable>`
    
    .. attribute:: mteeventtable
    
    	A table of management event action information
    	**type**\:  :py:class:`Mteeventtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventtable>`
    
    .. attribute:: mteeventnotificationtable
    
    	A table of information about notifications to be sent as a consequence of management events
    	**type**\:  :py:class:`Mteeventnotificationtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventnotificationtable>`
    
    .. attribute:: mteeventsettable
    
    	A table of management event action information
    	**type**\:  :py:class:`Mteeventsettable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventsettable>`
    
    

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
        self._child_container_classes = OrderedDict([("mteResource", ("mteresource", DISMANEVENTMIB.Mteresource)), ("mteTrigger", ("mtetrigger", DISMANEVENTMIB.Mtetrigger)), ("mteEvent", ("mteevent", DISMANEVENTMIB.Mteevent)), ("mteTriggerTable", ("mtetriggertable", DISMANEVENTMIB.Mtetriggertable)), ("mteTriggerDeltaTable", ("mtetriggerdeltatable", DISMANEVENTMIB.Mtetriggerdeltatable)), ("mteTriggerExistenceTable", ("mtetriggerexistencetable", DISMANEVENTMIB.Mtetriggerexistencetable)), ("mteTriggerBooleanTable", ("mtetriggerbooleantable", DISMANEVENTMIB.Mtetriggerbooleantable)), ("mteTriggerThresholdTable", ("mtetriggerthresholdtable", DISMANEVENTMIB.Mtetriggerthresholdtable)), ("mteObjectsTable", ("mteobjectstable", DISMANEVENTMIB.Mteobjectstable)), ("mteEventTable", ("mteeventtable", DISMANEVENTMIB.Mteeventtable)), ("mteEventNotificationTable", ("mteeventnotificationtable", DISMANEVENTMIB.Mteeventnotificationtable)), ("mteEventSetTable", ("mteeventsettable", DISMANEVENTMIB.Mteeventsettable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.mteresource = DISMANEVENTMIB.Mteresource()
        self.mteresource.parent = self
        self._children_name_map["mteresource"] = "mteResource"
        self._children_yang_names.add("mteResource")

        self.mtetrigger = DISMANEVENTMIB.Mtetrigger()
        self.mtetrigger.parent = self
        self._children_name_map["mtetrigger"] = "mteTrigger"
        self._children_yang_names.add("mteTrigger")

        self.mteevent = DISMANEVENTMIB.Mteevent()
        self.mteevent.parent = self
        self._children_name_map["mteevent"] = "mteEvent"
        self._children_yang_names.add("mteEvent")

        self.mtetriggertable = DISMANEVENTMIB.Mtetriggertable()
        self.mtetriggertable.parent = self
        self._children_name_map["mtetriggertable"] = "mteTriggerTable"
        self._children_yang_names.add("mteTriggerTable")

        self.mtetriggerdeltatable = DISMANEVENTMIB.Mtetriggerdeltatable()
        self.mtetriggerdeltatable.parent = self
        self._children_name_map["mtetriggerdeltatable"] = "mteTriggerDeltaTable"
        self._children_yang_names.add("mteTriggerDeltaTable")

        self.mtetriggerexistencetable = DISMANEVENTMIB.Mtetriggerexistencetable()
        self.mtetriggerexistencetable.parent = self
        self._children_name_map["mtetriggerexistencetable"] = "mteTriggerExistenceTable"
        self._children_yang_names.add("mteTriggerExistenceTable")

        self.mtetriggerbooleantable = DISMANEVENTMIB.Mtetriggerbooleantable()
        self.mtetriggerbooleantable.parent = self
        self._children_name_map["mtetriggerbooleantable"] = "mteTriggerBooleanTable"
        self._children_yang_names.add("mteTriggerBooleanTable")

        self.mtetriggerthresholdtable = DISMANEVENTMIB.Mtetriggerthresholdtable()
        self.mtetriggerthresholdtable.parent = self
        self._children_name_map["mtetriggerthresholdtable"] = "mteTriggerThresholdTable"
        self._children_yang_names.add("mteTriggerThresholdTable")

        self.mteobjectstable = DISMANEVENTMIB.Mteobjectstable()
        self.mteobjectstable.parent = self
        self._children_name_map["mteobjectstable"] = "mteObjectsTable"
        self._children_yang_names.add("mteObjectsTable")

        self.mteeventtable = DISMANEVENTMIB.Mteeventtable()
        self.mteeventtable.parent = self
        self._children_name_map["mteeventtable"] = "mteEventTable"
        self._children_yang_names.add("mteEventTable")

        self.mteeventnotificationtable = DISMANEVENTMIB.Mteeventnotificationtable()
        self.mteeventnotificationtable.parent = self
        self._children_name_map["mteeventnotificationtable"] = "mteEventNotificationTable"
        self._children_yang_names.add("mteEventNotificationTable")

        self.mteeventsettable = DISMANEVENTMIB.Mteeventsettable()
        self.mteeventsettable.parent = self
        self._children_name_map["mteeventsettable"] = "mteEventSetTable"
        self._children_yang_names.add("mteEventSetTable")
        self._segment_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB"


    class Mteresource(Entity):
        """
        
        
        .. attribute:: mteresourcesampleminimum
        
        	The minimum mteTriggerFrequency this system will accept.  A system may use the larger values of this minimum to lessen the impact of constant sampling.  For larger sampling intervals the system samples less often and suffers less overhead.  This object provides a way to enforce such lower overhead for all triggers created after it is set.  Unless explicitly resource limited, a system's value for this object SHOULD be 1, allowing as small as a 1 second interval for ongoing trigger sampling.  Changing this value will not invalidate an existing setting of mteTriggerFrequency
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        .. attribute:: mteresourcesampleinstancemaximum
        
        	The maximum number of instance entries this system will support for sampling.  These are the entries that maintain state, one for each instance of each sampled object as selected by mteTriggerValueID.  Note that wildcarded objects result in multiple instances of this state.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object SHOULD be 0.  Changing this value will not eliminate or inhibit existing sample state but could prevent allocation of additional state information
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstances
        
        	The number of currently active instance entries as defined for mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstanceshigh
        
        	The highest value of mteResourceSampleInstances that has occurred since initialization of the management system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstancelacks
        
        	The number of times this system could not take a new sample because that allocation would have exceeded the limit set by mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteresource, self).__init__()

            self.yang_name = "mteResource"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mteresourcesampleminimum', YLeaf(YType.int32, 'mteResourceSampleMinimum')),
                ('mteresourcesampleinstancemaximum', YLeaf(YType.uint32, 'mteResourceSampleInstanceMaximum')),
                ('mteresourcesampleinstances', YLeaf(YType.uint32, 'mteResourceSampleInstances')),
                ('mteresourcesampleinstanceshigh', YLeaf(YType.uint32, 'mteResourceSampleInstancesHigh')),
                ('mteresourcesampleinstancelacks', YLeaf(YType.uint32, 'mteResourceSampleInstanceLacks')),
            ])
            self.mteresourcesampleminimum = None
            self.mteresourcesampleinstancemaximum = None
            self.mteresourcesampleinstances = None
            self.mteresourcesampleinstanceshigh = None
            self.mteresourcesampleinstancelacks = None
            self._segment_path = lambda: "mteResource"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteresource, ['mteresourcesampleminimum', 'mteresourcesampleinstancemaximum', 'mteresourcesampleinstances', 'mteresourcesampleinstanceshigh', 'mteresourcesampleinstancelacks'], name, value)


    class Mtetrigger(Entity):
        """
        
        
        .. attribute:: mtetriggerfailures
        
        	The number of times an attempt to check for a trigger condition has failed.  This counts individually for each attempt in a group of targets or each attempt for a  wildcarded object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: failures
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetrigger, self).__init__()

            self.yang_name = "mteTrigger"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mtetriggerfailures', YLeaf(YType.uint32, 'mteTriggerFailures')),
            ])
            self.mtetriggerfailures = None
            self._segment_path = lambda: "mteTrigger"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetrigger, ['mtetriggerfailures'], name, value)


    class Mteevent(Entity):
        """
        
        
        .. attribute:: mteeventfailures
        
        	The number of times an attempt to invoke an event has failed.  This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteevent, self).__init__()

            self.yang_name = "mteEvent"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mteeventfailures', YLeaf(YType.uint32, 'mteEventFailures')),
            ])
            self.mteeventfailures = None
            self._segment_path = lambda: "mteEvent"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteevent, ['mteeventfailures'], name, value)


    class Mtetriggertable(Entity):
        """
        A table of management event trigger information.
        
        .. attribute:: mtetriggerentry
        
        	Information about a single trigger.  Applications create and delete entries using mteTriggerEntryStatus
        	**type**\: list of  		 :py:class:`Mtetriggerentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetriggertable, self).__init__()

            self.yang_name = "mteTriggerTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteTriggerEntry", ("mtetriggerentry", DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry))])
            self._leafs = OrderedDict()

            self.mtetriggerentry = YList(self)
            self._segment_path = lambda: "mteTriggerTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetriggertable, [], name, value)


        class Mtetriggerentry(Entity):
            """
            Information about a single trigger.  Applications create and
            delete entries using mteTriggerEntryStatus.
            
            .. attribute:: mteowner  (key)
            
            	The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggername  (key)
            
            	A locally\-unique, administratively assigned name for the trigger within the scope of mteOwner
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: mtetriggercomment
            
            	A description of the trigger's function and use
            	**type**\: str
            
            .. attribute:: mtetriggertest
            
            	The type of trigger test to perform.  For 'boolean' and 'threshold'  tests, the object at mteTriggerValueID MUST evaluate to an integer, that is, anything that ends up encoded for transmission (that is, in BER, not ASN.1) as an integer.  For 'existence', the specific test is as selected by mteTriggerExistenceTest.  When an object appears, vanishes or changes value, the trigger fires. If the object's appearance caused the trigger firing, the object MUST vanish before the trigger can be fired again for it, and vice versa. If the trigger fired due to a change in the object's value, it will be fired again on every successive value change for that object.  For 'boolean', the specific test is as selected by mteTriggerBooleanTest.  If the test result is true the trigger fires.  The trigger will not fire again until the value has become false and come back to true.  For 'threshold' the test works as described below for  mteTriggerThresholdStartup, mteTriggerThresholdRising, and mteTriggerThresholdFalling.  Note that combining 'boolean' and 'threshold' tests on the same object may be somewhat redundant
            	**type**\:  :py:class:`Mtetriggertest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry.Mtetriggertest>`
            
            .. attribute:: mtetriggersampletype
            
            	The type of sampling to perform.  An 'absoluteValue' sample requires only a single sample to be meaningful, and is exactly the value of the object at mteTriggerValueID at the sample time.  A 'deltaValue' requires two samples to be meaningful and is thus not available for testing until the second and subsequent samples after the object at mteTriggerValueID is first found to exist.  It is the difference between the two samples.  For unsigned values it is always positive, based on unsigned arithmetic.  For signed values it can be positive or negative.  For SNMP counters to be meaningful they should be sampled as a 'deltaValue'.  For 'deltaValue' mteTriggerDeltaTable contains further parameters.  If only 'existence' is set in mteTriggerTest this object has no meaning
            	**type**\:  :py:class:`Mtetriggersampletype <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry.Mtetriggersampletype>`
            
            .. attribute:: mtetriggervalueid
            
            	The object identifier of the MIB object to sample to see if the trigger should fire.  This may be wildcarded by truncating all or part of the instance portion, in which case the value is obtained as if with a GetNext function, checking multiple values  if they exist.  If such wildcarding is applied, mteTriggerValueIDWildcard must be 'true' and if not it must be 'false'.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteTriggerValueIDWildcard result in operation as one would expect when providing the wrong identifier to a Get or GetNext operation.  The Get will fail or get the wrong object.  The GetNext will indeed get whatever is next, proceeding until it runs past the initial part of the identifier and perhaps many unintended objects for confusing results.  If the value syntax of those objects is not usable, that results in a 'badType' error that terminates the scan.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggervalueidwildcard
            
            	Control for whether mteTriggerValueID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            .. attribute:: mtetriggertargettag
            
            	The tag for the target(s) from which to obtain the condition for a trigger check.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteTriggerValueID is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security  parameters resulting from the tag
            	**type**\: str
            
            .. attribute:: mtetriggercontextname
            
            	The management context from which to obtain mteTriggerValueID.  This may be wildcarded by leaving characters off the end.  For example use 'Repeater' to wildcard to 'Repeater1', 'Repeater2', 'Repeater\-999.87b', and so on.  To indicate such wildcarding is intended, mteTriggerContextNameWildcard must be 'true'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Operation of this feature assumes that the local system has a list of available contexts against which to apply the wildcard.  If the objects are being read from the local system, this is clearly the system's own list of contexts. For a remote system a local version of such a list is not defined by any current standard and may not be available, so this function MAY not be supported
            	**type**\: str
            
            .. attribute:: mtetriggercontextnamewildcard
            
            	Control for whether mteTriggerContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            .. attribute:: mtetriggerfrequency
            
            	The number of seconds to wait between trigger samples.  To encourage consistency in sampling, the interval is measured from the beginning of one check to the beginning of the next and the timer is restarted immediately when it expires, not when the check completes.  If the next sample begins before the previous one completed the system may either attempt to make the check or treat this as an error condition with the error 'sampleOverrun'.  A frequency of 0 indicates instantaneous recognition of the condition.  This is not possible in many cases, but may be supported in cases where it makes sense and the system is able to do so.  This feature allows the MIB to be used in implementations where such interrupt\-driven behavior is possible and is not likely to be supported for all MIB objects even then since such sampling generally has to be tightly integrated into low\-level code.  Systems that can support this SHOULD document those cases where it can be used.  In cases where it can not, setting this object to 0 should be disallowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: mtetriggerobjectsowner
            
            	To go with mteTriggerObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger.  A list of objects may also be added based on the event or on the value of mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerenabled
            
            	A control to allow a trigger to be configured but not used. When the value is 'false' the trigger is not sampled
            	**type**\: bool
            
            .. attribute:: mtetriggerentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry may not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry, self).__init__()

                self.yang_name = "mteTriggerEntry"
                self.yang_parent_name = "mteTriggerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mtetriggername', YLeaf(YType.str, 'mteTriggerName')),
                    ('mtetriggercomment', YLeaf(YType.str, 'mteTriggerComment')),
                    ('mtetriggertest', YLeaf(YType.bits, 'mteTriggerTest')),
                    ('mtetriggersampletype', YLeaf(YType.enumeration, 'mteTriggerSampleType')),
                    ('mtetriggervalueid', YLeaf(YType.str, 'mteTriggerValueID')),
                    ('mtetriggervalueidwildcard', YLeaf(YType.boolean, 'mteTriggerValueIDWildcard')),
                    ('mtetriggertargettag', YLeaf(YType.str, 'mteTriggerTargetTag')),
                    ('mtetriggercontextname', YLeaf(YType.str, 'mteTriggerContextName')),
                    ('mtetriggercontextnamewildcard', YLeaf(YType.boolean, 'mteTriggerContextNameWildcard')),
                    ('mtetriggerfrequency', YLeaf(YType.uint32, 'mteTriggerFrequency')),
                    ('mtetriggerobjectsowner', YLeaf(YType.str, 'mteTriggerObjectsOwner')),
                    ('mtetriggerobjects', YLeaf(YType.str, 'mteTriggerObjects')),
                    ('mtetriggerenabled', YLeaf(YType.boolean, 'mteTriggerEnabled')),
                    ('mtetriggerentrystatus', YLeaf(YType.enumeration, 'mteTriggerEntryStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry, ['mteowner', 'mtetriggername', 'mtetriggercomment', 'mtetriggertest', 'mtetriggersampletype', 'mtetriggervalueid', 'mtetriggervalueidwildcard', 'mtetriggertargettag', 'mtetriggercontextname', 'mtetriggercontextnamewildcard', 'mtetriggerfrequency', 'mtetriggerobjectsowner', 'mtetriggerobjects', 'mtetriggerenabled', 'mtetriggerentrystatus'], name, value)

            class Mtetriggersampletype(Enum):
                """
                Mtetriggersampletype (Enum Class)

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



    class Mtetriggerdeltatable(Entity):
        """
        A table of management event trigger information for delta
        sampling.
        
        .. attribute:: mtetriggerdeltaentry
        
        	Information about a single trigger's delta sampling.  Entries automatically exist in this this table for each mteTriggerEntry that has mteTriggerSampleType set to 'deltaValue'
        	**type**\: list of  		 :py:class:`Mtetriggerdeltaentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerdeltatable.Mtetriggerdeltaentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetriggerdeltatable, self).__init__()

            self.yang_name = "mteTriggerDeltaTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteTriggerDeltaEntry", ("mtetriggerdeltaentry", DISMANEVENTMIB.Mtetriggerdeltatable.Mtetriggerdeltaentry))])
            self._leafs = OrderedDict()

            self.mtetriggerdeltaentry = YList(self)
            self._segment_path = lambda: "mteTriggerDeltaTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetriggerdeltatable, [], name, value)


        class Mtetriggerdeltaentry(Entity):
            """
            Information about a single trigger's delta sampling.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has mteTriggerSampleType set to 'deltaValue'.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at mteTriggerValueID.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match mteTriggerValueID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking MUST still check sysUpTime for an overall discontinuity.  If the object identified is not accessible the sample attempt is in error, with the error code as from an SNMP request.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the value syntax of those objects is not usable, that results in an error that terminates the sample with a 'badType' error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggerdeltadiscontinuityidwildcard
            
            	Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding  mteTriggerSampleType is 'deltaValue'
            	**type**\: bool
            
            .. attribute:: mtetriggerdeltadiscontinuityidtype
            
            	The value 'timeTicks' indicates the mteTriggerDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp. The value 'dateAndTime' indicates syntax DateAndTime
            	**type**\:  :py:class:`Mtetriggerdeltadiscontinuityidtype <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerdeltatable.Mtetriggerdeltaentry.Mtetriggerdeltadiscontinuityidtype>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mtetriggerdeltatable.Mtetriggerdeltaentry, self).__init__()

                self.yang_name = "mteTriggerDeltaEntry"
                self.yang_parent_name = "mteTriggerDeltaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mtetriggername', YLeaf(YType.str, 'mteTriggerName')),
                    ('mtetriggerdeltadiscontinuityid', YLeaf(YType.str, 'mteTriggerDeltaDiscontinuityID')),
                    ('mtetriggerdeltadiscontinuityidwildcard', YLeaf(YType.boolean, 'mteTriggerDeltaDiscontinuityIDWildcard')),
                    ('mtetriggerdeltadiscontinuityidtype', YLeaf(YType.enumeration, 'mteTriggerDeltaDiscontinuityIDType')),
                ])
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerdeltadiscontinuityid = None
                self.mtetriggerdeltadiscontinuityidwildcard = None
                self.mtetriggerdeltadiscontinuityidtype = None
                self._segment_path = lambda: "mteTriggerDeltaEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteTriggerName='" + str(self.mtetriggername) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerDeltaTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mtetriggerdeltatable.Mtetriggerdeltaentry, ['mteowner', 'mtetriggername', 'mtetriggerdeltadiscontinuityid', 'mtetriggerdeltadiscontinuityidwildcard', 'mtetriggerdeltadiscontinuityidtype'], name, value)

            class Mtetriggerdeltadiscontinuityidtype(Enum):
                """
                Mtetriggerdeltadiscontinuityidtype (Enum Class)

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



    class Mtetriggerexistencetable(Entity):
        """
        A table of management event trigger information for existence
        triggers.
        
        .. attribute:: mtetriggerexistenceentry
        
        	Information about a single existence trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'existence' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`Mtetriggerexistenceentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetriggerexistencetable, self).__init__()

            self.yang_name = "mteTriggerExistenceTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteTriggerExistenceEntry", ("mtetriggerexistenceentry", DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry))])
            self._leafs = OrderedDict()

            self.mtetriggerexistenceentry = YList(self)
            self._segment_path = lambda: "mteTriggerExistenceTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetriggerexistencetable, [], name, value)


        class Mtetriggerexistenceentry(Entity):
            """
            Information about a single existence trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'existence' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerexistencetest
            
            	The type of existence test to perform.  The trigger fires when the object at mteTriggerValueID is seen to go from present to absent, from absent to present, or to have it's value changed, depending on which tests are selected\:  present(0) \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from absent to present.  absent(1)  \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from present to absent. changed(2) \- when this test is selected, the trigger fires the mteTriggerValueID object value changes.  Once the trigger has fired for either presence or absence it will not fire again for that state until the object has been to the other state. 
            	**type**\:  :py:class:`Mtetriggerexistencetest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencetest>`
            
            .. attribute:: mtetriggerexistencestartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' and the test specified by mteTriggerExistenceTest is true.  Setting an option causes that trigger to fire when its test is true
            	**type**\:  :py:class:`Mtetriggerexistencestartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencestartup>`
            
            .. attribute:: mtetriggerexistenceobjectsowner
            
            	To go with mteTriggerExistenceObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceeventowner
            
            	To go with mteTriggerExistenceEvent, the mteOwner of an event entry from the mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'existence' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry, self).__init__()

                self.yang_name = "mteTriggerExistenceEntry"
                self.yang_parent_name = "mteTriggerExistenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mtetriggername', YLeaf(YType.str, 'mteTriggerName')),
                    ('mtetriggerexistencetest', YLeaf(YType.bits, 'mteTriggerExistenceTest')),
                    ('mtetriggerexistencestartup', YLeaf(YType.bits, 'mteTriggerExistenceStartup')),
                    ('mtetriggerexistenceobjectsowner', YLeaf(YType.str, 'mteTriggerExistenceObjectsOwner')),
                    ('mtetriggerexistenceobjects', YLeaf(YType.str, 'mteTriggerExistenceObjects')),
                    ('mtetriggerexistenceeventowner', YLeaf(YType.str, 'mteTriggerExistenceEventOwner')),
                    ('mtetriggerexistenceevent', YLeaf(YType.str, 'mteTriggerExistenceEvent')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mtetriggerexistencetable.Mtetriggerexistenceentry, ['mteowner', 'mtetriggername', 'mtetriggerexistencetest', 'mtetriggerexistencestartup', 'mtetriggerexistenceobjectsowner', 'mtetriggerexistenceobjects', 'mtetriggerexistenceeventowner', 'mtetriggerexistenceevent'], name, value)


    class Mtetriggerbooleantable(Entity):
        """
        A table of management event trigger information for boolean
        triggers.
        
        .. attribute:: mtetriggerbooleanentry
        
        	Information about a single boolean trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'boolean' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`Mtetriggerbooleanentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerbooleantable.Mtetriggerbooleanentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetriggerbooleantable, self).__init__()

            self.yang_name = "mteTriggerBooleanTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteTriggerBooleanEntry", ("mtetriggerbooleanentry", DISMANEVENTMIB.Mtetriggerbooleantable.Mtetriggerbooleanentry))])
            self._leafs = OrderedDict()

            self.mtetriggerbooleanentry = YList(self)
            self._segment_path = lambda: "mteTriggerBooleanTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetriggerbooleantable, [], name, value)


        class Mtetriggerbooleanentry(Entity):
            """
            Information about a single boolean trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'boolean' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerbooleancomparison
            
            	The type of boolean comparison to perform.  The value at mteTriggerValueID is compared to mteTriggerBooleanValue, so for example if mteTriggerBooleanComparison is 'less' the result would be true if the value at mteTriggerValueID is less than the value of mteTriggerBooleanValue
            	**type**\:  :py:class:`Mtetriggerbooleancomparison <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerbooleantable.Mtetriggerbooleanentry.Mtetriggerbooleancomparison>`
            
            .. attribute:: mtetriggerbooleanvalue
            
            	The value to use for the test specified by mteTriggerBooleanTest
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerbooleanstartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' or a new instance of the object at mteTriggerValueID is found and the test specified by mteTriggerBooleanComparison is true.  In that case an event is triggered if mteTriggerBooleanStartup is 'true'
            	**type**\: bool
            
            .. attribute:: mtetriggerbooleanobjectsowner
            
            	To go with mteTriggerBooleanObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleanobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleaneventowner
            
            	To go with mteTriggerBooleanEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleanevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'boolean' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mtetriggerbooleantable.Mtetriggerbooleanentry, self).__init__()

                self.yang_name = "mteTriggerBooleanEntry"
                self.yang_parent_name = "mteTriggerBooleanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mtetriggername', YLeaf(YType.str, 'mteTriggerName')),
                    ('mtetriggerbooleancomparison', YLeaf(YType.enumeration, 'mteTriggerBooleanComparison')),
                    ('mtetriggerbooleanvalue', YLeaf(YType.int32, 'mteTriggerBooleanValue')),
                    ('mtetriggerbooleanstartup', YLeaf(YType.boolean, 'mteTriggerBooleanStartup')),
                    ('mtetriggerbooleanobjectsowner', YLeaf(YType.str, 'mteTriggerBooleanObjectsOwner')),
                    ('mtetriggerbooleanobjects', YLeaf(YType.str, 'mteTriggerBooleanObjects')),
                    ('mtetriggerbooleaneventowner', YLeaf(YType.str, 'mteTriggerBooleanEventOwner')),
                    ('mtetriggerbooleanevent', YLeaf(YType.str, 'mteTriggerBooleanEvent')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mtetriggerbooleantable.Mtetriggerbooleanentry, ['mteowner', 'mtetriggername', 'mtetriggerbooleancomparison', 'mtetriggerbooleanvalue', 'mtetriggerbooleanstartup', 'mtetriggerbooleanobjectsowner', 'mtetriggerbooleanobjects', 'mtetriggerbooleaneventowner', 'mtetriggerbooleanevent'], name, value)

            class Mtetriggerbooleancomparison(Enum):
                """
                Mtetriggerbooleancomparison (Enum Class)

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



    class Mtetriggerthresholdtable(Entity):
        """
        A table of management event trigger information for threshold
        triggers.
        
        .. attribute:: mtetriggerthresholdentry
        
        	Information about a single threshold trigger.  Entries automatically exist in this table for each mteTriggerEntry that has 'threshold' set in mteTriggerTest
        	**type**\: list of  		 :py:class:`Mtetriggerthresholdentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerthresholdtable.Mtetriggerthresholdentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mtetriggerthresholdtable, self).__init__()

            self.yang_name = "mteTriggerThresholdTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteTriggerThresholdEntry", ("mtetriggerthresholdentry", DISMANEVENTMIB.Mtetriggerthresholdtable.Mtetriggerthresholdentry))])
            self._leafs = OrderedDict()

            self.mtetriggerthresholdentry = YList(self)
            self._segment_path = lambda: "mteTriggerThresholdTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mtetriggerthresholdtable, [], name, value)


        class Mtetriggerthresholdentry(Entity):
            """
            Information about a single threshold trigger.  Entries
            automatically exist in this table for each mteTriggerEntry
            that has 'threshold' set in mteTriggerTest.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerthresholdstartup
            
            	The event that may be triggered when this entry is first set to 'active' and a new instance of the object at mteTriggerValueID is found.  If the first sample after this instance becomes active is greater than or equal to mteTriggerThresholdRising and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance. If the first sample after this entry becomes active is less than or equal to mteTriggerThresholdFalling and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance
            	**type**\:  :py:class:`Mtetriggerthresholdstartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggerthresholdtable.Mtetriggerthresholdentry.Mtetriggerthresholdstartup>`
            
            .. attribute:: mtetriggerthresholdrising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, one mteTriggerThresholdRisingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is greater than or equal to this threshold and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling'.  After a rising event is generated, another such event is not triggered until the sampled value falls below this threshold and reaches mteTriggerThresholdFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdfalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, one mteTriggerThresholdFallingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is less than or equal to this threshold and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling'.  After a falling event is generated, another such event is not triggered until the sampled value rises above this threshold and reaches mteTriggerThresholdRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltarising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is greater than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was less than this threshold, one mteTriggerThresholdDeltaRisingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is greater than or equal to this threshold.  After a rising event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltafalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is less than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was greater than this threshold, one mteTriggerThresholdDeltaFallingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is less than or equal to this threshold.  After a falling event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdobjectsowner
            
            	To go with mteTriggerThresholdObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall  trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdrisingeventowner
            
            	To go with mteTriggerThresholdRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdrisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdRising.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdfallingeventowner
            
            	To go with mteTriggerThresholdFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdfallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarisingeventowner
            
            	To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaRising. A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltafallingeventowner
            
            	To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltafallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mtetriggerthresholdtable.Mtetriggerthresholdentry, self).__init__()

                self.yang_name = "mteTriggerThresholdEntry"
                self.yang_parent_name = "mteTriggerThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mtetriggername']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mtetriggername', YLeaf(YType.str, 'mteTriggerName')),
                    ('mtetriggerthresholdstartup', YLeaf(YType.enumeration, 'mteTriggerThresholdStartup')),
                    ('mtetriggerthresholdrising', YLeaf(YType.int32, 'mteTriggerThresholdRising')),
                    ('mtetriggerthresholdfalling', YLeaf(YType.int32, 'mteTriggerThresholdFalling')),
                    ('mtetriggerthresholddeltarising', YLeaf(YType.int32, 'mteTriggerThresholdDeltaRising')),
                    ('mtetriggerthresholddeltafalling', YLeaf(YType.int32, 'mteTriggerThresholdDeltaFalling')),
                    ('mtetriggerthresholdobjectsowner', YLeaf(YType.str, 'mteTriggerThresholdObjectsOwner')),
                    ('mtetriggerthresholdobjects', YLeaf(YType.str, 'mteTriggerThresholdObjects')),
                    ('mtetriggerthresholdrisingeventowner', YLeaf(YType.str, 'mteTriggerThresholdRisingEventOwner')),
                    ('mtetriggerthresholdrisingevent', YLeaf(YType.str, 'mteTriggerThresholdRisingEvent')),
                    ('mtetriggerthresholdfallingeventowner', YLeaf(YType.str, 'mteTriggerThresholdFallingEventOwner')),
                    ('mtetriggerthresholdfallingevent', YLeaf(YType.str, 'mteTriggerThresholdFallingEvent')),
                    ('mtetriggerthresholddeltarisingeventowner', YLeaf(YType.str, 'mteTriggerThresholdDeltaRisingEventOwner')),
                    ('mtetriggerthresholddeltarisingevent', YLeaf(YType.str, 'mteTriggerThresholdDeltaRisingEvent')),
                    ('mtetriggerthresholddeltafallingeventowner', YLeaf(YType.str, 'mteTriggerThresholdDeltaFallingEventOwner')),
                    ('mtetriggerthresholddeltafallingevent', YLeaf(YType.str, 'mteTriggerThresholdDeltaFallingEvent')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mtetriggerthresholdtable.Mtetriggerthresholdentry, ['mteowner', 'mtetriggername', 'mtetriggerthresholdstartup', 'mtetriggerthresholdrising', 'mtetriggerthresholdfalling', 'mtetriggerthresholddeltarising', 'mtetriggerthresholddeltafalling', 'mtetriggerthresholdobjectsowner', 'mtetriggerthresholdobjects', 'mtetriggerthresholdrisingeventowner', 'mtetriggerthresholdrisingevent', 'mtetriggerthresholdfallingeventowner', 'mtetriggerthresholdfallingevent', 'mtetriggerthresholddeltarisingeventowner', 'mtetriggerthresholddeltarisingevent', 'mtetriggerthresholddeltafallingeventowner', 'mtetriggerthresholddeltafallingevent'], name, value)

            class Mtetriggerthresholdstartup(Enum):
                """
                Mtetriggerthresholdstartup (Enum Class)

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



    class Mteobjectstable(Entity):
        """
        A table of objects that can be added to notifications based
        on the trigger, trigger test, or event, as pointed to by
        entries in those tables.
        
        .. attribute:: mteobjectsentry
        
        	A group of objects.  Applications create and delete entries using mteObjectsEntryStatus.  When adding objects to a notification they are added in the lexical order of their index in this table.  Those associated with a trigger come first, then trigger test, then event
        	**type**\: list of  		 :py:class:`Mteobjectsentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteobjectstable.Mteobjectsentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteobjectstable, self).__init__()

            self.yang_name = "mteObjectsTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteObjectsEntry", ("mteobjectsentry", DISMANEVENTMIB.Mteobjectstable.Mteobjectsentry))])
            self._leafs = OrderedDict()

            self.mteobjectsentry = YList(self)
            self._segment_path = lambda: "mteObjectsTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteobjectstable, [], name, value)


        class Mteobjectsentry(Entity):
            """
            A group of objects.  Applications create and delete entries
            using mteObjectsEntryStatus.
            
            When adding objects to a notification they are added in the
            lexical order of their index in this table.  Those associated
            with a trigger come first, then trigger test, then event.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteobjectsname  (key)
            
            	A locally\-unique, administratively assigned name for a group of objects
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: mteobjectsindex  (key)
            
            	An arbitrary integer for the purpose of identifying individual objects within a mteObjectsName group.  Objects within a group are placed in the notification in the numerical order of this index.  Groups are placed in the notification in the order of the selections for overall trigger, trigger test, and event. Within trigger test they are in the same order as the numerical values of the bits defined for mteTriggerTest.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the object is not available it is omitted from the notification
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mteobjectsid
            
            	The object identifier of a MIB object to add to a Notification that results from the firing of a trigger.  This may be wildcarded by truncating all or part of the instance portion, in which case the instance portion of the OID for obtaining this object will be the same as that used in obtaining the mteTriggerValueID that fired.  If such wildcarding is applied, mteObjectsIDWildcard must be 'true' and if not it must be 'false'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteobjectsidwildcard
            
            	Control for whether mteObjectsID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            .. attribute:: mteobjectsentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mteobjectstable.Mteobjectsentry, self).__init__()

                self.yang_name = "mteObjectsEntry"
                self.yang_parent_name = "mteObjectsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteobjectsname','mteobjectsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mteobjectsname', YLeaf(YType.str, 'mteObjectsName')),
                    ('mteobjectsindex', YLeaf(YType.uint32, 'mteObjectsIndex')),
                    ('mteobjectsid', YLeaf(YType.str, 'mteObjectsID')),
                    ('mteobjectsidwildcard', YLeaf(YType.boolean, 'mteObjectsIDWildcard')),
                    ('mteobjectsentrystatus', YLeaf(YType.enumeration, 'mteObjectsEntryStatus')),
                ])
                self.mteowner = None
                self.mteobjectsname = None
                self.mteobjectsindex = None
                self.mteobjectsid = None
                self.mteobjectsidwildcard = None
                self.mteobjectsentrystatus = None
                self._segment_path = lambda: "mteObjectsEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteObjectsName='" + str(self.mteobjectsname) + "']" + "[mteObjectsIndex='" + str(self.mteobjectsindex) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteObjectsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mteobjectstable.Mteobjectsentry, ['mteowner', 'mteobjectsname', 'mteobjectsindex', 'mteobjectsid', 'mteobjectsidwildcard', 'mteobjectsentrystatus'], name, value)


    class Mteeventtable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteevententry
        
        	Information about a single event.  Applications create and delete entries using mteEventEntryStatus
        	**type**\: list of  		 :py:class:`Mteevententry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventtable.Mteevententry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteeventtable, self).__init__()

            self.yang_name = "mteEventTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteEventEntry", ("mteevententry", DISMANEVENTMIB.Mteeventtable.Mteevententry))])
            self._leafs = OrderedDict()

            self.mteevententry = YList(self)
            self._segment_path = lambda: "mteEventTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteeventtable, [], name, value)


        class Mteevententry(Entity):
            """
            Information about a single event.  Applications create and
            delete entries using mteEventEntryStatus.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  (key)
            
            	A locally\-unique, administratively assigned name for the event
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: mteeventcomment
            
            	A description of the event's function and use
            	**type**\: str
            
            .. attribute:: mteeventactions
            
            	The actions to perform when this event occurs.  For 'notification', Traps and/or Informs are sent according to the configuration in the SNMP Notification MIB.  For 'set', an SNMP Set operation is performed according to control values in this entry
            	**type**\:  :py:class:`Mteeventactions <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventtable.Mteevententry.Mteeventactions>`
            
            .. attribute:: mteeventenabled
            
            	A control to allow an event to be configured but not used. When the value is 'false' the event does not execute even if  triggered
            	**type**\: bool
            
            .. attribute:: mteevententrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mteeventtable.Mteevententry, self).__init__()

                self.yang_name = "mteEventEntry"
                self.yang_parent_name = "mteEventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mteeventname', YLeaf(YType.str, 'mteEventName')),
                    ('mteeventcomment', YLeaf(YType.str, 'mteEventComment')),
                    ('mteeventactions', YLeaf(YType.bits, 'mteEventActions')),
                    ('mteeventenabled', YLeaf(YType.boolean, 'mteEventEnabled')),
                    ('mteevententrystatus', YLeaf(YType.enumeration, 'mteEventEntryStatus')),
                ])
                self.mteowner = None
                self.mteeventname = None
                self.mteeventcomment = None
                self.mteeventactions = Bits()
                self.mteeventenabled = None
                self.mteevententrystatus = None
                self._segment_path = lambda: "mteEventEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteEventName='" + str(self.mteeventname) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mteeventtable.Mteevententry, ['mteowner', 'mteeventname', 'mteeventcomment', 'mteeventactions', 'mteeventenabled', 'mteevententrystatus'], name, value)


    class Mteeventnotificationtable(Entity):
        """
        A table of information about notifications to be sent as a
        consequence of management events.
        
        .. attribute:: mteeventnotificationentry
        
        	Information about a single event's notification.  Entries automatically exist in this this table for each mteEventEntry that has 'notification' set in mteEventActions
        	**type**\: list of  		 :py:class:`Mteeventnotificationentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventnotificationtable.Mteeventnotificationentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteeventnotificationtable, self).__init__()

            self.yang_name = "mteEventNotificationTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteEventNotificationEntry", ("mteeventnotificationentry", DISMANEVENTMIB.Mteeventnotificationtable.Mteeventnotificationentry))])
            self._leafs = OrderedDict()

            self.mteeventnotificationentry = YList(self)
            self._segment_path = lambda: "mteEventNotificationTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteeventnotificationtable, [], name, value)


        class Mteeventnotificationentry(Entity):
            """
            Information about a single event's notification.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'notification' set in mteEventActions.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventtable.Mteevententry>`
            
            .. attribute:: mteeventnotification
            
            	The object identifier from the NOTIFICATION\-TYPE for the notification to use if metEventActions has 'notification' set
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventnotificationobjectsowner
            
            	To go with mteEventNotificationObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mteeventnotificationobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable if mteEventActions has 'notification' set. These objects are to be added to any Notification generated by this event.  Objects may also be added based on the trigger that stimulated the event.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mteeventnotificationtable.Mteeventnotificationentry, self).__init__()

                self.yang_name = "mteEventNotificationEntry"
                self.yang_parent_name = "mteEventNotificationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mteeventname', YLeaf(YType.str, 'mteEventName')),
                    ('mteeventnotification', YLeaf(YType.str, 'mteEventNotification')),
                    ('mteeventnotificationobjectsowner', YLeaf(YType.str, 'mteEventNotificationObjectsOwner')),
                    ('mteeventnotificationobjects', YLeaf(YType.str, 'mteEventNotificationObjects')),
                ])
                self.mteowner = None
                self.mteeventname = None
                self.mteeventnotification = None
                self.mteeventnotificationobjectsowner = None
                self.mteeventnotificationobjects = None
                self._segment_path = lambda: "mteEventNotificationEntry" + "[mteOwner='" + str(self.mteowner) + "']" + "[mteEventName='" + str(self.mteeventname) + "']"
                self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventNotificationTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mteeventnotificationtable.Mteeventnotificationentry, ['mteowner', 'mteeventname', 'mteeventnotification', 'mteeventnotificationobjectsowner', 'mteeventnotificationobjects'], name, value)


    class Mteeventsettable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteeventsetentry
        
        	Information about a single event's set option.  Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions
        	**type**\: list of  		 :py:class:`Mteeventsetentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventsettable.Mteeventsetentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEVENTMIB.Mteeventsettable, self).__init__()

            self.yang_name = "mteEventSetTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mteEventSetEntry", ("mteeventsetentry", DISMANEVENTMIB.Mteeventsettable.Mteeventsetentry))])
            self._leafs = OrderedDict()

            self.mteeventsetentry = YList(self)
            self._segment_path = lambda: "mteEventSetTable"
            self._absolute_path = lambda: "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEVENTMIB.Mteeventsettable, [], name, value)


        class Mteeventsetentry(Entity):
            """
            Information about a single event's set option.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'set' set in mteEventActions.
            
            .. attribute:: mteowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DISMANEVENTMIB.Mteeventtable.Mteevententry>`
            
            .. attribute:: mteeventsetobject
            
            	The object identifier from the MIB object to set if mteEventActions has 'set' set.  This object identifier may be wildcarded by leaving sub\-identifiers off the end, in which case nteEventSetObjectWildCard must be 'true'.  If mteEventSetObject is wildcarded the instance used to set the object to which it points is the same as the instance from the value of mteTriggerValueID that triggered the event.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteSetObjectWildcard result in operation as one would expect when providing the wrong identifier to a Set operation.  The Set will fail or set the wrong object.  If the value syntax of the destination object is not correct, the Set fails with the normal SNMP error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventsetobjectwildcard
            
            	Control over whether mteEventSetObject is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            .. attribute:: mteeventsetvalue
            
            	The value to which to set the object at mteEventSetObject if mteEventActions has 'set' set
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mteeventsettargettag
            
            	The tag for the target(s) at which to set the object at mteEventSetObject to mteEventSetValue if mteEventActions has 'set' set.  Systems limited to self management MAY reject a non\-zero length for the value of this object.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteEventSetObject is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security parameters resulting from the tag
            	**type**\: str
            
            .. attribute:: mteeventsetcontextname
            
            	The management context in which to set mteEventObjectID. if mteEventActions has 'set' set.  This may be wildcarded by leaving characters off the end.  To indicate such wildcarding mteEventSetContextNameWildcard must be 'true'.  If this context name is wildcarded the value used to complete the wildcarding of mteTriggerContextName will be appended
            	**type**\: str
            
            .. attribute:: mteeventsetcontextnamewildcard
            
            	Control for whether mteEventSetContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEVENTMIB.Mteeventsettable.Mteeventsetentry, self).__init__()

                self.yang_name = "mteEventSetEntry"
                self.yang_parent_name = "mteEventSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mteowner','mteeventname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mteowner', YLeaf(YType.str, 'mteOwner')),
                    ('mteeventname', YLeaf(YType.str, 'mteEventName')),
                    ('mteeventsetobject', YLeaf(YType.str, 'mteEventSetObject')),
                    ('mteeventsetobjectwildcard', YLeaf(YType.boolean, 'mteEventSetObjectWildcard')),
                    ('mteeventsetvalue', YLeaf(YType.int32, 'mteEventSetValue')),
                    ('mteeventsettargettag', YLeaf(YType.str, 'mteEventSetTargetTag')),
                    ('mteeventsetcontextname', YLeaf(YType.str, 'mteEventSetContextName')),
                    ('mteeventsetcontextnamewildcard', YLeaf(YType.boolean, 'mteEventSetContextNameWildcard')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEVENTMIB.Mteeventsettable.Mteeventsetentry, ['mteowner', 'mteeventname', 'mteeventsetobject', 'mteeventsetobjectwildcard', 'mteeventsetvalue', 'mteeventsettargettag', 'mteeventsetcontextname', 'mteeventsetcontextnamewildcard'], name, value)

    def clone_ptr(self):
        self._top_entity = DISMANEVENTMIB()
        return self._top_entity

