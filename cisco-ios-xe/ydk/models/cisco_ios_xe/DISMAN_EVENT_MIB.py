""" DISMAN_EVENT_MIB 

The MIB module for defining event triggers and actions
for network management purposes.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class FailurereasonEnum(Enum):
    """
    FailurereasonEnum

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

    sampleOverrun = -6

    badType = -5

    noResponse = -4

    destinationUnreachable = -3

    badDestination = -2

    localResourceLack = -1

    noError = 0

    tooBig = 1

    noSuchName = 2

    badValue = 3

    readOnly = 4

    genErr = 5

    noAccess = 6

    wrongType = 7

    wrongLength = 8

    wrongEncoding = 9

    wrongValue = 10

    noCreation = 11

    inconsistentValue = 12

    resourceUnavailable = 13

    commitFailed = 14

    undoFailed = 15

    authorizationError = 16

    notWritable = 17

    inconsistentName = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
        return meta._meta_table['FailurereasonEnum']



class DismanEventMib(object):
    """
    
    
    .. attribute:: mteevent
    
    	
    	**type**\:   :py:class:`Mteevent <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteevent>`
    
    .. attribute:: mteeventnotificationtable
    
    	A table of information about notifications to be sent as a consequence of management events
    	**type**\:   :py:class:`Mteeventnotificationtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventnotificationtable>`
    
    .. attribute:: mteeventsettable
    
    	A table of management event action information
    	**type**\:   :py:class:`Mteeventsettable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventsettable>`
    
    .. attribute:: mteeventtable
    
    	A table of management event action information
    	**type**\:   :py:class:`Mteeventtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable>`
    
    .. attribute:: mteobjectstable
    
    	A table of objects that can be added to notifications based on the trigger, trigger test, or event, as pointed to by entries in those tables
    	**type**\:   :py:class:`Mteobjectstable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteobjectstable>`
    
    .. attribute:: mteresource
    
    	
    	**type**\:   :py:class:`Mteresource <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteresource>`
    
    .. attribute:: mtetrigger
    
    	
    	**type**\:   :py:class:`Mtetrigger <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetrigger>`
    
    .. attribute:: mtetriggerbooleantable
    
    	A table of management event trigger information for boolean triggers
    	**type**\:   :py:class:`Mtetriggerbooleantable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerbooleantable>`
    
    .. attribute:: mtetriggerdeltatable
    
    	A table of management event trigger information for delta sampling
    	**type**\:   :py:class:`Mtetriggerdeltatable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerdeltatable>`
    
    .. attribute:: mtetriggerexistencetable
    
    	A table of management event trigger information for existence triggers
    	**type**\:   :py:class:`Mtetriggerexistencetable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerexistencetable>`
    
    .. attribute:: mtetriggertable
    
    	A table of management event trigger information
    	**type**\:   :py:class:`Mtetriggertable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable>`
    
    .. attribute:: mtetriggerthresholdtable
    
    	A table of management event trigger information for threshold triggers
    	**type**\:   :py:class:`Mtetriggerthresholdtable <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerthresholdtable>`
    
    

    """

    _prefix = 'DISMAN-EVENT-MIB'
    _revision = '2000-10-16'

    def __init__(self):
        self.mteevent = DismanEventMib.Mteevent()
        self.mteevent.parent = self
        self.mteeventnotificationtable = DismanEventMib.Mteeventnotificationtable()
        self.mteeventnotificationtable.parent = self
        self.mteeventsettable = DismanEventMib.Mteeventsettable()
        self.mteeventsettable.parent = self
        self.mteeventtable = DismanEventMib.Mteeventtable()
        self.mteeventtable.parent = self
        self.mteobjectstable = DismanEventMib.Mteobjectstable()
        self.mteobjectstable.parent = self
        self.mteresource = DismanEventMib.Mteresource()
        self.mteresource.parent = self
        self.mtetrigger = DismanEventMib.Mtetrigger()
        self.mtetrigger.parent = self
        self.mtetriggerbooleantable = DismanEventMib.Mtetriggerbooleantable()
        self.mtetriggerbooleantable.parent = self
        self.mtetriggerdeltatable = DismanEventMib.Mtetriggerdeltatable()
        self.mtetriggerdeltatable.parent = self
        self.mtetriggerexistencetable = DismanEventMib.Mtetriggerexistencetable()
        self.mtetriggerexistencetable.parent = self
        self.mtetriggertable = DismanEventMib.Mtetriggertable()
        self.mtetriggertable.parent = self
        self.mtetriggerthresholdtable = DismanEventMib.Mtetriggerthresholdtable()
        self.mtetriggerthresholdtable.parent = self


    class Mteresource(object):
        """
        
        
        .. attribute:: mteresourcesampleinstancelacks
        
        	The number of times this system could not take a new sample because that allocation would have exceeded the limit set by mteResourceSampleInstanceMaximum
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstancemaximum
        
        	The maximum number of instance entries this system will support for sampling.  These are the entries that maintain state, one for each instance of each sampled object as selected by mteTriggerValueID.  Note that wildcarded objects result in multiple instances of this state.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object SHOULD be 0.  Changing this value will not eliminate or inhibit existing sample state but could prevent allocation of additional state information
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstances
        
        	The number of currently active instance entries as defined for mteResourceSampleInstanceMaximum
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleinstanceshigh
        
        	The highest value of mteResourceSampleInstances that has occurred since initialization of the management system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: mteresourcesampleminimum
        
        	The minimum mteTriggerFrequency this system will accept.  A system may use the larger values of this minimum to lessen the impact of constant sampling.  For larger sampling intervals the system samples less often and suffers less overhead.  This object provides a way to enforce such lower overhead for all triggers created after it is set.  Unless explicitly resource limited, a system's value for this object SHOULD be 1, allowing as small as a 1 second interval for ongoing trigger sampling.  Changing this value will not invalidate an existing setting of mteTriggerFrequency
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteresourcesampleinstancelacks = None
            self.mteresourcesampleinstancemaximum = None
            self.mteresourcesampleinstances = None
            self.mteresourcesampleinstanceshigh = None
            self.mteresourcesampleminimum = None

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteResource'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteresourcesampleinstancelacks is not None:
                return True

            if self.mteresourcesampleinstancemaximum is not None:
                return True

            if self.mteresourcesampleinstances is not None:
                return True

            if self.mteresourcesampleinstanceshigh is not None:
                return True

            if self.mteresourcesampleminimum is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteresource']['meta_info']


    class Mtetrigger(object):
        """
        
        
        .. attribute:: mtetriggerfailures
        
        	The number of times an attempt to check for a trigger condition has failed.  This counts individually for each attempt in a group of targets or each attempt for a  wildcarded object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: failures
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerfailures = None

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTrigger'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerfailures is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetrigger']['meta_info']


    class Mteevent(object):
        """
        
        
        .. attribute:: mteeventfailures
        
        	The number of times an attempt to invoke an event has failed.  This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteeventfailures = None

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEvent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteeventfailures is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteevent']['meta_info']


    class Mtetriggertable(object):
        """
        A table of management event trigger information.
        
        .. attribute:: mtetriggerentry
        
        	Information about a single trigger.  Applications create and delete entries using mteTriggerEntryStatus
        	**type**\: list of    :py:class:`Mtetriggerentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerentry = YList()
            self.mtetriggerentry.parent = self
            self.mtetriggerentry.name = 'mtetriggerentry'


        class Mtetriggerentry(object):
            """
            Information about a single trigger.  Applications create and
            delete entries using mteTriggerEntryStatus.
            
            .. attribute:: mteowner  <key>
            
            	The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggername  <key>
            
            	A locally\-unique, administratively assigned name for the trigger within the scope of mteOwner
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: mtetriggercomment
            
            	A description of the trigger's function and use
            	**type**\:  str
            
            .. attribute:: mtetriggercontextname
            
            	The management context from which to obtain mteTriggerValueID.  This may be wildcarded by leaving characters off the end.  For example use 'Repeater' to wildcard to 'Repeater1', 'Repeater2', 'Repeater\-999.87b', and so on.  To indicate such wildcarding is intended, mteTriggerContextNameWildcard must be 'true'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Operation of this feature assumes that the local system has a list of available contexts against which to apply the wildcard.  If the objects are being read from the local system, this is clearly the system's own list of contexts. For a remote system a local version of such a list is not defined by any current standard and may not be available, so this function MAY not be supported
            	**type**\:  str
            
            .. attribute:: mtetriggercontextnamewildcard
            
            	Control for whether mteTriggerContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\:  bool
            
            .. attribute:: mtetriggerenabled
            
            	A control to allow a trigger to be configured but not used. When the value is 'false' the trigger is not sampled
            	**type**\:  bool
            
            .. attribute:: mtetriggerentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry may not be modified except to delete it
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mtetriggerfrequency
            
            	The number of seconds to wait between trigger samples.  To encourage consistency in sampling, the interval is measured from the beginning of one check to the beginning of the next and the timer is restarted immediately when it expires, not when the check completes.  If the next sample begins before the previous one completed the system may either attempt to make the check or treat this as an error condition with the error 'sampleOverrun'.  A frequency of 0 indicates instantaneous recognition of the condition.  This is not possible in many cases, but may be supported in cases where it makes sense and the system is able to do so.  This feature allows the MIB to be used in implementations where such interrupt\-driven behavior is possible and is not likely to be supported for all MIB objects even then since such sampling generally has to be tightly integrated into low\-level code.  Systems that can support this SHOULD document those cases where it can be used.  In cases where it can not, setting this object to 0 should be disallowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: mtetriggerobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger.  A list of objects may also be added based on the event or on the value of mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerobjectsowner
            
            	To go with mteTriggerObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggersampletype
            
            	The type of sampling to perform.  An 'absoluteValue' sample requires only a single sample to be meaningful, and is exactly the value of the object at mteTriggerValueID at the sample time.  A 'deltaValue' requires two samples to be meaningful and is thus not available for testing until the second and subsequent samples after the object at mteTriggerValueID is first found to exist.  It is the difference between the two samples.  For unsigned values it is always positive, based on unsigned arithmetic.  For signed values it can be positive or negative.  For SNMP counters to be meaningful they should be sampled as a 'deltaValue'.  For 'deltaValue' mteTriggerDeltaTable contains further parameters.  If only 'existence' is set in mteTriggerTest this object has no meaning
            	**type**\:   :py:class:`MtetriggersampletypeEnum <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry.MtetriggersampletypeEnum>`
            
            .. attribute:: mtetriggertargettag
            
            	The tag for the target(s) from which to obtain the condition for a trigger check.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteTriggerValueID is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security  parameters resulting from the tag
            	**type**\:  str
            
            .. attribute:: mtetriggertest
            
            	The type of trigger test to perform.  For 'boolean' and 'threshold'  tests, the object at mteTriggerValueID MUST evaluate to an integer, that is, anything that ends up encoded for transmission (that is, in BER, not ASN.1) as an integer.  For 'existence', the specific test is as selected by mteTriggerExistenceTest.  When an object appears, vanishes or changes value, the trigger fires. If the object's appearance caused the trigger firing, the object MUST vanish before the trigger can be fired again for it, and vice versa. If the trigger fired due to a change in the object's value, it will be fired again on every successive value change for that object.  For 'boolean', the specific test is as selected by mteTriggerBooleanTest.  If the test result is true the trigger fires.  The trigger will not fire again until the value has become false and come back to true.  For 'threshold' the test works as described below for  mteTriggerThresholdStartup, mteTriggerThresholdRising, and mteTriggerThresholdFalling.  Note that combining 'boolean' and 'threshold' tests on the same object may be somewhat redundant
            	**type**\:   :py:class:`Mtetriggertest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry.Mtetriggertest>`
            
            .. attribute:: mtetriggervalueid
            
            	The object identifier of the MIB object to sample to see if the trigger should fire.  This may be wildcarded by truncating all or part of the instance portion, in which case the value is obtained as if with a GetNext function, checking multiple values  if they exist.  If such wildcarding is applied, mteTriggerValueIDWildcard must be 'true' and if not it must be 'false'.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteTriggerValueIDWildcard result in operation as one would expect when providing the wrong identifier to a Get or GetNext operation.  The Get will fail or get the wrong object.  The GetNext will indeed get whatever is next, proceeding until it runs past the initial part of the identifier and perhaps many unintended objects for confusing results.  If the value syntax of those objects is not usable, that results in a 'badType' error that terminates the scan.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggervalueidwildcard
            
            	Control for whether mteTriggerValueID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\:  bool
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggercomment = None
                self.mtetriggercontextname = None
                self.mtetriggercontextnamewildcard = None
                self.mtetriggerenabled = None
                self.mtetriggerentrystatus = None
                self.mtetriggerfrequency = None
                self.mtetriggerobjects = None
                self.mtetriggerobjectsowner = None
                self.mtetriggersampletype = None
                self.mtetriggertargettag = None
                self.mtetriggertest = DismanEventMib.Mtetriggertable.Mtetriggerentry.Mtetriggertest()
                self.mtetriggervalueid = None
                self.mtetriggervalueidwildcard = None

            class MtetriggersampletypeEnum(Enum):
                """
                MtetriggersampletypeEnum

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

                absoluteValue = 1

                deltaValue = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DismanEventMib.Mtetriggertable.Mtetriggerentry.MtetriggersampletypeEnum']


            class Mtetriggertest(FixedBitsDict):
                """
                Mtetriggertest

                The type of trigger test to perform.  For 'boolean' and
                'threshold'  tests, the object at mteTriggerValueID MUST
                evaluate to an integer, that is, anything that ends up encoded
                for transmission (that is, in BER, not ASN.1) as an integer.
                
                For 'existence', the specific test is as selected by
                mteTriggerExistenceTest.  When an object appears, vanishes
                or changes value, the trigger fires. If the object's
                appearance caused the trigger firing, the object MUST
                vanish before the trigger can be fired again for it, and
                vice versa. If the trigger fired due to a change in the
                object's value, it will be fired again on every successive
                value change for that object.
                
                For 'boolean', the specific test is as selected by
                mteTriggerBooleanTest.  If the test result is true the trigger
                fires.  The trigger will not fire again until the value has
                become false and come back to true.
                
                For 'threshold' the test works as described below for
                
                mteTriggerThresholdStartup, mteTriggerThresholdRising, and
                mteTriggerThresholdFalling.
                
                Note that combining 'boolean' and 'threshold' tests on the
                same object may be somewhat redundant.
                Keys are:- boolean , existence , threshold

                """

                def __init__(self):
                    self._dictionary = { 
                        'boolean':False,
                        'existence':False,
                        'threshold':False,
                    }
                    self._pos_map = { 
                        'boolean':1,
                        'existence':0,
                        'threshold':2,
                    }

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYModelError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerTable/DISMAN-EVENT-MIB:mteTriggerEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mtetriggername is not None:
                    return True

                if self.mtetriggercomment is not None:
                    return True

                if self.mtetriggercontextname is not None:
                    return True

                if self.mtetriggercontextnamewildcard is not None:
                    return True

                if self.mtetriggerenabled is not None:
                    return True

                if self.mtetriggerentrystatus is not None:
                    return True

                if self.mtetriggerfrequency is not None:
                    return True

                if self.mtetriggerobjects is not None:
                    return True

                if self.mtetriggerobjectsowner is not None:
                    return True

                if self.mtetriggersampletype is not None:
                    return True

                if self.mtetriggertargettag is not None:
                    return True

                if self.mtetriggertest is not None:
                    if self.mtetriggertest._has_data():
                        return True

                if self.mtetriggervalueid is not None:
                    return True

                if self.mtetriggervalueidwildcard is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mtetriggertable.Mtetriggerentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerentry is not None:
                for child_ref in self.mtetriggerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetriggertable']['meta_info']


    class Mtetriggerdeltatable(object):
        """
        A table of management event trigger information for delta
        sampling.
        
        .. attribute:: mtetriggerdeltaentry
        
        	Information about a single trigger's delta sampling.  Entries automatically exist in this this table for each mteTriggerEntry that has mteTriggerSampleType set to 'deltaValue'
        	**type**\: list of    :py:class:`Mtetriggerdeltaentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerdeltaentry = YList()
            self.mtetriggerdeltaentry.parent = self
            self.mtetriggerdeltaentry.name = 'mtetriggerdeltaentry'


        class Mtetriggerdeltaentry(object):
            """
            Information about a single trigger's delta sampling.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has mteTriggerSampleType set to 'deltaValue'.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at mteTriggerValueID.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match mteTriggerValueID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking MUST still check sysUpTime for an overall discontinuity.  If the object identified is not accessible the sample attempt is in error, with the error code as from an SNMP request.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the value syntax of those objects is not usable, that results in an error that terminates the sample with a 'badType' error code
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggerdeltadiscontinuityidtype
            
            	The value 'timeTicks' indicates the mteTriggerDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp. The value 'dateAndTime' indicates syntax DateAndTime
            	**type**\:   :py:class:`MtetriggerdeltadiscontinuityidtypeEnum <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry.MtetriggerdeltadiscontinuityidtypeEnum>`
            
            .. attribute:: mtetriggerdeltadiscontinuityidwildcard
            
            	Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding  mteTriggerSampleType is 'deltaValue'
            	**type**\:  bool
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerdeltadiscontinuityid = None
                self.mtetriggerdeltadiscontinuityidtype = None
                self.mtetriggerdeltadiscontinuityidwildcard = None

            class MtetriggerdeltadiscontinuityidtypeEnum(Enum):
                """
                MtetriggerdeltadiscontinuityidtypeEnum

                The value 'timeTicks' indicates the

                mteTriggerDeltaDiscontinuityID of this row is of syntax

                TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp.

                The value 'dateAndTime' indicates syntax DateAndTime.

                .. data:: timeTicks = 1

                .. data:: timeStamp = 2

                .. data:: dateAndTime = 3

                """

                timeTicks = 1

                timeStamp = 2

                dateAndTime = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry.MtetriggerdeltadiscontinuityidtypeEnum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYModelError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerDeltaTable/DISMAN-EVENT-MIB:mteTriggerDeltaEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mtetriggername is not None:
                    return True

                if self.mtetriggerdeltadiscontinuityid is not None:
                    return True

                if self.mtetriggerdeltadiscontinuityidtype is not None:
                    return True

                if self.mtetriggerdeltadiscontinuityidwildcard is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerDeltaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerdeltaentry is not None:
                for child_ref in self.mtetriggerdeltaentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetriggerdeltatable']['meta_info']


    class Mtetriggerexistencetable(object):
        """
        A table of management event trigger information for existence
        triggers.
        
        .. attribute:: mtetriggerexistenceentry
        
        	Information about a single existence trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'existence' set in mteTriggerTest
        	**type**\: list of    :py:class:`Mtetriggerexistenceentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerexistenceentry = YList()
            self.mtetriggerexistenceentry.parent = self
            self.mtetriggerexistenceentry.name = 'mtetriggerexistenceentry'


        class Mtetriggerexistenceentry(object):
            """
            Information about a single existence trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'existence' set in mteTriggerTest.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerexistenceevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'existence' and this trigger fires.  A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceeventowner
            
            	To go with mteTriggerExistenceEvent, the mteOwner of an event entry from the mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistenceobjectsowner
            
            	To go with mteTriggerExistenceObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerexistencestartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' and the test specified by mteTriggerExistenceTest is true.  Setting an option causes that trigger to fire when its test is true
            	**type**\:   :py:class:`Mtetriggerexistencestartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencestartup>`
            
            .. attribute:: mtetriggerexistencetest
            
            	The type of existence test to perform.  The trigger fires when the object at mteTriggerValueID is seen to go from present to absent, from absent to present, or to have it's value changed, depending on which tests are selected\:  present(0) \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from absent to present.  absent(1)  \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from present to absent. changed(2) \- when this test is selected, the trigger fires the mteTriggerValueID object value changes.  Once the trigger has fired for either presence or absence it will not fire again for that state until the object has been to the other state. 
            	**type**\:   :py:class:`Mtetriggerexistencetest <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencetest>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerexistenceevent = None
                self.mtetriggerexistenceeventowner = None
                self.mtetriggerexistenceobjects = None
                self.mtetriggerexistenceobjectsowner = None
                self.mtetriggerexistencestartup = DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencestartup()
                self.mtetriggerexistencetest = DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencetest()

            class Mtetriggerexistencestartup(FixedBitsDict):
                """
                Mtetriggerexistencestartup

                Control for whether an event may be triggered when this entry
                is first set to 'active' and the test specified by
                mteTriggerExistenceTest is true.  Setting an option causes
                that trigger to fire when its test is true.
                Keys are:- present , absent

                """

                def __init__(self):
                    self._dictionary = { 
                        'present':False,
                        'absent':False,
                    }
                    self._pos_map = { 
                        'present':0,
                        'absent':1,
                    }

            class Mtetriggerexistencetest(FixedBitsDict):
                """
                Mtetriggerexistencetest

                The type of existence test to perform.  The trigger fires
                when the object at mteTriggerValueID is seen to go from
                present to absent, from absent to present, or to have it's
                value changed, depending on which tests are selected\:
                
                present(0) \- when this test is selected, the trigger fires
                when the mteTriggerValueID object goes from absent to present.
                
                absent(1)  \- when this test is selected, the trigger fires
                when the mteTriggerValueID object goes from present to absent.
                changed(2) \- when this test is selected, the trigger fires
                the mteTriggerValueID object value changes.
                
                Once the trigger has fired for either presence or absence it
                will not fire again for that state until the object has been
                to the other state. 
                Keys are:- present , absent , changed

                """

                def __init__(self):
                    self._dictionary = { 
                        'present':False,
                        'absent':False,
                        'changed':False,
                    }
                    self._pos_map = { 
                        'present':0,
                        'absent':1,
                        'changed':2,
                    }

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYModelError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerExistenceTable/DISMAN-EVENT-MIB:mteTriggerExistenceEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mtetriggername is not None:
                    return True

                if self.mtetriggerexistenceevent is not None:
                    return True

                if self.mtetriggerexistenceeventowner is not None:
                    return True

                if self.mtetriggerexistenceobjects is not None:
                    return True

                if self.mtetriggerexistenceobjectsowner is not None:
                    return True

                if self.mtetriggerexistencestartup is not None:
                    if self.mtetriggerexistencestartup._has_data():
                        return True

                if self.mtetriggerexistencetest is not None:
                    if self.mtetriggerexistencetest._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerExistenceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerexistenceentry is not None:
                for child_ref in self.mtetriggerexistenceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetriggerexistencetable']['meta_info']


    class Mtetriggerbooleantable(object):
        """
        A table of management event trigger information for boolean
        triggers.
        
        .. attribute:: mtetriggerbooleanentry
        
        	Information about a single boolean trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'boolean' set in mteTriggerTest
        	**type**\: list of    :py:class:`Mtetriggerbooleanentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerbooleanentry = YList()
            self.mtetriggerbooleanentry.parent = self
            self.mtetriggerbooleanentry.name = 'mtetriggerbooleanentry'


        class Mtetriggerbooleanentry(object):
            """
            Information about a single boolean trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'boolean' set in mteTriggerTest.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerbooleancomparison
            
            	The type of boolean comparison to perform.  The value at mteTriggerValueID is compared to mteTriggerBooleanValue, so for example if mteTriggerBooleanComparison is 'less' the result would be true if the value at mteTriggerValueID is less than the value of mteTriggerBooleanValue
            	**type**\:   :py:class:`MtetriggerbooleancomparisonEnum <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry.MtetriggerbooleancomparisonEnum>`
            
            .. attribute:: mtetriggerbooleanevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'boolean' and this trigger fires.  A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleaneventowner
            
            	To go with mteTriggerBooleanEvent, the mteOwner of an event entry from mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleanobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleanobjectsowner
            
            	To go with mteTriggerBooleanObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerbooleanstartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' or a new instance of the object at mteTriggerValueID is found and the test specified by mteTriggerBooleanComparison is true.  In that case an event is triggered if mteTriggerBooleanStartup is 'true'
            	**type**\:  bool
            
            .. attribute:: mtetriggerbooleanvalue
            
            	The value to use for the test specified by mteTriggerBooleanTest
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerbooleancomparison = None
                self.mtetriggerbooleanevent = None
                self.mtetriggerbooleaneventowner = None
                self.mtetriggerbooleanobjects = None
                self.mtetriggerbooleanobjectsowner = None
                self.mtetriggerbooleanstartup = None
                self.mtetriggerbooleanvalue = None

            class MtetriggerbooleancomparisonEnum(Enum):
                """
                MtetriggerbooleancomparisonEnum

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

                unequal = 1

                equal = 2

                less = 3

                lessOrEqual = 4

                greater = 5

                greaterOrEqual = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry.MtetriggerbooleancomparisonEnum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYModelError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerBooleanTable/DISMAN-EVENT-MIB:mteTriggerBooleanEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mtetriggername is not None:
                    return True

                if self.mtetriggerbooleancomparison is not None:
                    return True

                if self.mtetriggerbooleanevent is not None:
                    return True

                if self.mtetriggerbooleaneventowner is not None:
                    return True

                if self.mtetriggerbooleanobjects is not None:
                    return True

                if self.mtetriggerbooleanobjectsowner is not None:
                    return True

                if self.mtetriggerbooleanstartup is not None:
                    return True

                if self.mtetriggerbooleanvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerBooleanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerbooleanentry is not None:
                for child_ref in self.mtetriggerbooleanentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetriggerbooleantable']['meta_info']


    class Mtetriggerthresholdtable(object):
        """
        A table of management event trigger information for threshold
        triggers.
        
        .. attribute:: mtetriggerthresholdentry
        
        	Information about a single threshold trigger.  Entries automatically exist in this table for each mteTriggerEntry that has 'threshold' set in mteTriggerTest
        	**type**\: list of    :py:class:`Mtetriggerthresholdentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerthresholdentry = YList()
            self.mtetriggerthresholdentry.parent = self
            self.mtetriggerthresholdentry.name = 'mtetriggerthresholdentry'


        class Mtetriggerthresholdentry(object):
            """
            Information about a single threshold trigger.  Entries
            automatically exist in this table for each mteTriggerEntry
            that has 'threshold' set in mteTriggerTest.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggername  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mtetriggername <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mtetriggerthresholddeltafalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is less than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was greater than this threshold, one mteTriggerThresholdDeltaFallingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is less than or equal to this threshold.  After a falling event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaRising
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltafallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaFalling.  A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltafallingeventowner
            
            	To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is greater than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was less than this threshold, one mteTriggerThresholdDeltaRisingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is greater than or equal to this threshold.  After a rising event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaFalling
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltarisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaRising. A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarisingeventowner
            
            	To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdfalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, one mteTriggerThresholdFallingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is less than or equal to this threshold and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling'.  After a falling event is generated, another such event is not triggered until the sampled value rises above this threshold and reaches mteTriggerThresholdRising
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdfallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdFalling.  A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdfallingeventowner
            
            	To go with mteTriggerThresholdFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall  trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdobjectsowner
            
            	To go with mteTriggerThresholdObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdrising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, one mteTriggerThresholdRisingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is greater than or equal to this threshold and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling'.  After a rising event is generated, another such event is not triggered until the sampled value falls below this threshold and reaches mteTriggerThresholdFalling
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdrisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdRising.  A length of 0 indicates no event
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdrisingeventowner
            
            	To go with mteTriggerThresholdRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mtetriggerthresholdstartup
            
            	The event that may be triggered when this entry is first set to 'active' and a new instance of the object at mteTriggerValueID is found.  If the first sample after this instance becomes active is greater than or equal to mteTriggerThresholdRising and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance. If the first sample after this entry becomes active is less than or equal to mteTriggerThresholdFalling and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance
            	**type**\:   :py:class:`MtetriggerthresholdstartupEnum <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry.MtetriggerthresholdstartupEnum>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerthresholddeltafalling = None
                self.mtetriggerthresholddeltafallingevent = None
                self.mtetriggerthresholddeltafallingeventowner = None
                self.mtetriggerthresholddeltarising = None
                self.mtetriggerthresholddeltarisingevent = None
                self.mtetriggerthresholddeltarisingeventowner = None
                self.mtetriggerthresholdfalling = None
                self.mtetriggerthresholdfallingevent = None
                self.mtetriggerthresholdfallingeventowner = None
                self.mtetriggerthresholdobjects = None
                self.mtetriggerthresholdobjectsowner = None
                self.mtetriggerthresholdrising = None
                self.mtetriggerthresholdrisingevent = None
                self.mtetriggerthresholdrisingeventowner = None
                self.mtetriggerthresholdstartup = None

            class MtetriggerthresholdstartupEnum(Enum):
                """
                MtetriggerthresholdstartupEnum

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

                rising = 1

                falling = 2

                risingOrFalling = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry.MtetriggerthresholdstartupEnum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYModelError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerThresholdTable/DISMAN-EVENT-MIB:mteTriggerThresholdEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mtetriggername is not None:
                    return True

                if self.mtetriggerthresholddeltafalling is not None:
                    return True

                if self.mtetriggerthresholddeltafallingevent is not None:
                    return True

                if self.mtetriggerthresholddeltafallingeventowner is not None:
                    return True

                if self.mtetriggerthresholddeltarising is not None:
                    return True

                if self.mtetriggerthresholddeltarisingevent is not None:
                    return True

                if self.mtetriggerthresholddeltarisingeventowner is not None:
                    return True

                if self.mtetriggerthresholdfalling is not None:
                    return True

                if self.mtetriggerthresholdfallingevent is not None:
                    return True

                if self.mtetriggerthresholdfallingeventowner is not None:
                    return True

                if self.mtetriggerthresholdobjects is not None:
                    return True

                if self.mtetriggerthresholdobjectsowner is not None:
                    return True

                if self.mtetriggerthresholdrising is not None:
                    return True

                if self.mtetriggerthresholdrisingevent is not None:
                    return True

                if self.mtetriggerthresholdrisingeventowner is not None:
                    return True

                if self.mtetriggerthresholdstartup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerThresholdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mtetriggerthresholdentry is not None:
                for child_ref in self.mtetriggerthresholdentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mtetriggerthresholdtable']['meta_info']


    class Mteobjectstable(object):
        """
        A table of objects that can be added to notifications based
        on the trigger, trigger test, or event, as pointed to by
        entries in those tables.
        
        .. attribute:: mteobjectsentry
        
        	A group of objects.  Applications create and delete entries using mteObjectsEntryStatus.  When adding objects to a notification they are added in the lexical order of their index in this table.  Those associated with a trigger come first, then trigger test, then event
        	**type**\: list of    :py:class:`Mteobjectsentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteobjectstable.Mteobjectsentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteobjectsentry = YList()
            self.mteobjectsentry.parent = self
            self.mteobjectsentry.name = 'mteobjectsentry'


        class Mteobjectsentry(object):
            """
            A group of objects.  Applications create and delete entries
            using mteObjectsEntryStatus.
            
            When adding objects to a notification they are added in the
            lexical order of their index in this table.  Those associated
            with a trigger come first, then trigger test, then event.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteobjectsname  <key>
            
            	A locally\-unique, administratively assigned name for a group of objects
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: mteobjectsindex  <key>
            
            	An arbitrary integer for the purpose of identifying individual objects within a mteObjectsName group.  Objects within a group are placed in the notification in the numerical order of this index.  Groups are placed in the notification in the order of the selections for overall trigger, trigger test, and event. Within trigger test they are in the same order as the numerical values of the bits defined for mteTriggerTest.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the object is not available it is omitted from the notification
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mteobjectsentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mteobjectsid
            
            	The object identifier of a MIB object to add to a Notification that results from the firing of a trigger.  This may be wildcarded by truncating all or part of the instance portion, in which case the instance portion of the OID for obtaining this object will be the same as that used in obtaining the mteTriggerValueID that fired.  If such wildcarding is applied, mteObjectsIDWildcard must be 'true' and if not it must be 'false'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteobjectsidwildcard
            
            	Control for whether mteObjectsID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\:  bool
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mteobjectsname = None
                self.mteobjectsindex = None
                self.mteobjectsentrystatus = None
                self.mteobjectsid = None
                self.mteobjectsidwildcard = None

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mteobjectsname is None:
                    raise YPYModelError('Key property mteobjectsname is None')
                if self.mteobjectsindex is None:
                    raise YPYModelError('Key property mteobjectsindex is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteObjectsTable/DISMAN-EVENT-MIB:mteObjectsEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteObjectsName = ' + str(self.mteobjectsname) + '][DISMAN-EVENT-MIB:mteObjectsIndex = ' + str(self.mteobjectsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mteobjectsname is not None:
                    return True

                if self.mteobjectsindex is not None:
                    return True

                if self.mteobjectsentrystatus is not None:
                    return True

                if self.mteobjectsid is not None:
                    return True

                if self.mteobjectsidwildcard is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mteobjectstable.Mteobjectsentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteObjectsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteobjectsentry is not None:
                for child_ref in self.mteobjectsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteobjectstable']['meta_info']


    class Mteeventtable(object):
        """
        A table of management event action information.
        
        .. attribute:: mteevententry
        
        	Information about a single event.  Applications create and delete entries using mteEventEntryStatus
        	**type**\: list of    :py:class:`Mteevententry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable.Mteevententry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteevententry = YList()
            self.mteevententry.parent = self
            self.mteevententry.name = 'mteevententry'


        class Mteevententry(object):
            """
            Information about a single event.  Applications create and
            delete entries using mteEventEntryStatus.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  <key>
            
            	A locally\-unique, administratively assigned name for the event
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: mteeventactions
            
            	The actions to perform when this event occurs.  For 'notification', Traps and/or Informs are sent according to the configuration in the SNMP Notification MIB.  For 'set', an SNMP Set operation is performed according to control values in this entry
            	**type**\:   :py:class:`Mteeventactions <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable.Mteevententry.Mteeventactions>`
            
            .. attribute:: mteeventcomment
            
            	A description of the event's function and use
            	**type**\:  str
            
            .. attribute:: mteeventenabled
            
            	A control to allow an event to be configured but not used. When the value is 'false' the event does not execute even if  triggered
            	**type**\:  bool
            
            .. attribute:: mteevententrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mteeventname = None
                self.mteeventactions = DismanEventMib.Mteeventtable.Mteevententry.Mteeventactions()
                self.mteeventcomment = None
                self.mteeventenabled = None
                self.mteevententrystatus = None

            class Mteeventactions(FixedBitsDict):
                """
                Mteeventactions

                The actions to perform when this event occurs.
                
                For 'notification', Traps and/or Informs are sent according
                to the configuration in the SNMP Notification MIB.
                
                For 'set', an SNMP Set operation is performed according to
                control values in this entry.
                Keys are:- notification , set

                """

                def __init__(self):
                    self._dictionary = { 
                        'notification':False,
                        'set':False,
                    }
                    self._pos_map = { 
                        'notification':0,
                        'set':1,
                    }

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mteeventname is None:
                    raise YPYModelError('Key property mteeventname is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventTable/DISMAN-EVENT-MIB:mteEventEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mteeventname is not None:
                    return True

                if self.mteeventactions is not None:
                    if self.mteeventactions._has_data():
                        return True

                if self.mteeventcomment is not None:
                    return True

                if self.mteeventenabled is not None:
                    return True

                if self.mteevententrystatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mteeventtable.Mteevententry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteevententry is not None:
                for child_ref in self.mteevententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteeventtable']['meta_info']


    class Mteeventnotificationtable(object):
        """
        A table of information about notifications to be sent as a
        consequence of management events.
        
        .. attribute:: mteeventnotificationentry
        
        	Information about a single event's notification.  Entries automatically exist in this this table for each mteEventEntry that has 'notification' set in mteEventActions
        	**type**\: list of    :py:class:`Mteeventnotificationentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteeventnotificationentry = YList()
            self.mteeventnotificationentry.parent = self
            self.mteeventnotificationentry.name = 'mteeventnotificationentry'


        class Mteeventnotificationentry(object):
            """
            Information about a single event's notification.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'notification' set in mteEventActions.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable.Mteevententry>`
            
            .. attribute:: mteeventnotification
            
            	The object identifier from the NOTIFICATION\-TYPE for the notification to use if metEventActions has 'notification' set
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventnotificationobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable if mteEventActions has 'notification' set. These objects are to be added to any Notification generated by this event.  Objects may also be added based on the trigger that stimulated the event.  A length of 0 indicates no additional objects
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mteeventnotificationobjectsowner
            
            	To go with mteEventNotificationObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mteeventname = None
                self.mteeventnotification = None
                self.mteeventnotificationobjects = None
                self.mteeventnotificationobjectsowner = None

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mteeventname is None:
                    raise YPYModelError('Key property mteeventname is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventNotificationTable/DISMAN-EVENT-MIB:mteEventNotificationEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mteeventname is not None:
                    return True

                if self.mteeventnotification is not None:
                    return True

                if self.mteeventnotificationobjects is not None:
                    return True

                if self.mteeventnotificationobjectsowner is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventNotificationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteeventnotificationentry is not None:
                for child_ref in self.mteeventnotificationentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteeventnotificationtable']['meta_info']


    class Mteeventsettable(object):
        """
        A table of management event action information.
        
        .. attribute:: mteeventsetentry
        
        	Information about a single event's set option.  Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions
        	**type**\: list of    :py:class:`Mteeventsetentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventsettable.Mteeventsetentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteeventsetentry = YList()
            self.mteeventsetentry.parent = self
            self.mteeventsetentry.name = 'mteeventsetentry'


        class Mteeventsetentry(object):
            """
            Information about a single event's set option.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'set' set in mteEventActions.
            
            .. attribute:: mteowner  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`mteowner <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
            
            .. attribute:: mteeventname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`mteeventname <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable.Mteevententry>`
            
            .. attribute:: mteeventsetcontextname
            
            	The management context in which to set mteEventObjectID. if mteEventActions has 'set' set.  This may be wildcarded by leaving characters off the end.  To indicate such wildcarding mteEventSetContextNameWildcard must be 'true'.  If this context name is wildcarded the value used to complete the wildcarding of mteTriggerContextName will be appended
            	**type**\:  str
            
            .. attribute:: mteeventsetcontextnamewildcard
            
            	Control for whether mteEventSetContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\:  bool
            
            .. attribute:: mteeventsetobject
            
            	The object identifier from the MIB object to set if mteEventActions has 'set' set.  This object identifier may be wildcarded by leaving sub\-identifiers off the end, in which case nteEventSetObjectWildCard must be 'true'.  If mteEventSetObject is wildcarded the instance used to set the object to which it points is the same as the instance from the value of mteTriggerValueID that triggered the event.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteSetObjectWildcard result in operation as one would expect when providing the wrong identifier to a Set operation.  The Set will fail or set the wrong object.  If the value syntax of the destination object is not correct, the Set fails with the normal SNMP error code
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventsetobjectwildcard
            
            	Control over whether mteEventSetObject is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\:  bool
            
            .. attribute:: mteeventsettargettag
            
            	The tag for the target(s) at which to set the object at mteEventSetObject to mteEventSetValue if mteEventActions has 'set' set.  Systems limited to self management MAY reject a non\-zero length for the value of this object.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteEventSetObject is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security parameters resulting from the tag
            	**type**\:  str
            
            .. attribute:: mteeventsetvalue
            
            	The value to which to set the object at mteEventSetObject if mteEventActions has 'set' set
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mteeventname = None
                self.mteeventsetcontextname = None
                self.mteeventsetcontextnamewildcard = None
                self.mteeventsetobject = None
                self.mteeventsetobjectwildcard = None
                self.mteeventsettargettag = None
                self.mteeventsetvalue = None

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYModelError('Key property mteowner is None')
                if self.mteeventname is None:
                    raise YPYModelError('Key property mteeventname is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventSetTable/DISMAN-EVENT-MIB:mteEventSetEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mteowner is not None:
                    return True

                if self.mteeventname is not None:
                    return True

                if self.mteeventsetcontextname is not None:
                    return True

                if self.mteeventsetcontextnamewildcard is not None:
                    return True

                if self.mteeventsetobject is not None:
                    return True

                if self.mteeventsetobjectwildcard is not None:
                    return True

                if self.mteeventsettargettag is not None:
                    return True

                if self.mteeventsetvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DismanEventMib.Mteeventsettable.Mteeventsetentry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mteeventsetentry is not None:
                for child_ref in self.mteeventsetentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DismanEventMib.Mteeventsettable']['meta_info']

    @property
    def _common_path(self):

        return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mteevent is not None and self.mteevent._has_data():
            return True

        if self.mteeventnotificationtable is not None and self.mteeventnotificationtable._has_data():
            return True

        if self.mteeventsettable is not None and self.mteeventsettable._has_data():
            return True

        if self.mteeventtable is not None and self.mteeventtable._has_data():
            return True

        if self.mteobjectstable is not None and self.mteobjectstable._has_data():
            return True

        if self.mteresource is not None and self.mteresource._has_data():
            return True

        if self.mtetrigger is not None and self.mtetrigger._has_data():
            return True

        if self.mtetriggerbooleantable is not None and self.mtetriggerbooleantable._has_data():
            return True

        if self.mtetriggerdeltatable is not None and self.mtetriggerdeltatable._has_data():
            return True

        if self.mtetriggerexistencetable is not None and self.mtetriggerexistencetable._has_data():
            return True

        if self.mtetriggertable is not None and self.mtetriggertable._has_data():
            return True

        if self.mtetriggerthresholdtable is not None and self.mtetriggerthresholdtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DISMAN_EVENT_MIB as meta
        return meta._meta_table['DismanEventMib']['meta_info']


