


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FailurereasonEnum' : _MetaInfoEnum('FailurereasonEnum', 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB',
        {
            'sampleOverrun':'sampleOverrun',
            'badType':'badType',
            'noResponse':'noResponse',
            'destinationUnreachable':'destinationUnreachable',
            'badDestination':'badDestination',
            'localResourceLack':'localResourceLack',
            'noError':'noError',
            'tooBig':'tooBig',
            'noSuchName':'noSuchName',
            'badValue':'badValue',
            'readOnly':'readOnly',
            'genErr':'genErr',
            'noAccess':'noAccess',
            'wrongType':'wrongType',
            'wrongLength':'wrongLength',
            'wrongEncoding':'wrongEncoding',
            'wrongValue':'wrongValue',
            'noCreation':'noCreation',
            'inconsistentValue':'inconsistentValue',
            'resourceUnavailable':'resourceUnavailable',
            'commitFailed':'commitFailed',
            'undoFailed':'undoFailed',
            'authorizationError':'authorizationError',
            'notWritable':'notWritable',
            'inconsistentName':'inconsistentName',
        }, 'DISMAN-EVENT-MIB', _yang_ns._namespaces['DISMAN-EVENT-MIB']),
    'DismanEventMib.Mteresource' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteresource',
            False, 
            [
            _MetaInfoClassMember('mteResourceSampleInstanceLacks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this system could not take a new sample
                because that allocation would have exceeded the limit set by
                mteResourceSampleInstanceMaximum.
                ''',
                'mteresourcesampleinstancelacks',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteResourceSampleInstanceMaximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of instance entries this system will
                support for sampling.
                
                These are the entries that maintain state, one for each
                instance of each sampled object as selected by
                mteTriggerValueID.  Note that wildcarded objects result
                in multiple instances of this state.
                
                A value of 0 indicates no preset limit, that is, the limit
                is dynamic based on system operation and resources.
                
                Unless explicitly resource limited, a system's value for
                this object SHOULD be 0.
                
                Changing this value will not eliminate or inhibit existing
                sample state but could prevent allocation of additional state
                information.
                ''',
                'mteresourcesampleinstancemaximum',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteResourceSampleInstances', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of currently active instance entries as
                defined for mteResourceSampleInstanceMaximum.
                ''',
                'mteresourcesampleinstances',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteResourceSampleInstancesHigh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The highest value of mteResourceSampleInstances that has
                occurred since initialization of the management system.
                ''',
                'mteresourcesampleinstanceshigh',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteResourceSampleMinimum', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The minimum mteTriggerFrequency this system will
                accept.  A system may use the larger values of this minimum to
                lessen the impact of constant sampling.  For larger
                sampling intervals the system samples less often and
                suffers less overhead.  This object provides a way to enforce
                such lower overhead for all triggers created after it is
                set.
                
                Unless explicitly resource limited, a system's value for
                this object SHOULD be 1, allowing as small as a 1 second
                interval for ongoing trigger sampling.
                
                Changing this value will not invalidate an existing setting
                of mteTriggerFrequency.
                ''',
                'mteresourcesampleminimum',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteResource',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetrigger' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetrigger',
            False, 
            [
            _MetaInfoClassMember('mteTriggerFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times an attempt to check for a trigger
                condition has failed.  This counts individually for each
                attempt in a group of targets or each attempt for a
                
                wildcarded object.
                ''',
                'mtetriggerfailures',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTrigger',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteevent' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteevent',
            False, 
            [
            _MetaInfoClassMember('mteEventFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times an attempt to invoke an event
                has failed.  This counts individually for each
                attempt in a group of targets or each attempt for a
                wildcarded trigger object.
                ''',
                'mteeventfailures',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEvent',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggertable.Mtetriggerentry.MtetriggersampletypeEnum' : _MetaInfoEnum('MtetriggersampletypeEnum', 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB',
        {
            'absoluteValue':'absoluteValue',
            'deltaValue':'deltaValue',
        }, 'DISMAN-EVENT-MIB', _yang_ns._namespaces['DISMAN-EVENT-MIB']),
    'DismanEventMib.Mtetriggertable.Mtetriggerentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggertable.Mtetriggerentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The owner of this entry. The exact semantics of this
                string are subject to the security policy defined by the
                security administrator.
                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A locally-unique, administratively assigned name for the
                trigger within the scope of mteOwner.
                ''',
                'mtetriggername',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerComment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A description of the trigger's function and use.
                ''',
                'mtetriggercomment',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerContextName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The management context from which to obtain mteTriggerValueID.
                
                This may be wildcarded by leaving characters off the end.  For
                example use 'Repeater' to wildcard to 'Repeater1',
                'Repeater2', 'Repeater-999.87b', and so on.  To indicate such
                wildcarding is intended, mteTriggerContextNameWildcard must
                be 'true'.
                
                Each instance that fills the wildcard is independent of any
                additional instances, that is, wildcarded objects operate
                as if there were a separate table entry for each instance
                that fills the wildcard without having to actually predict
                all possible instances ahead of time.
                
                Operation of this feature assumes that the local system has a
                list of available contexts against which to apply the
                wildcard.  If the objects are being read from the local
                system, this is clearly the system's own list of contexts.
                For a remote system a local version of such a list is not
                defined by any current standard and may not be available, so
                this function MAY not be supported.
                ''',
                'mtetriggercontextname',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerContextNameWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether mteTriggerContextName is to be treated as
                fully-specified or wildcarded, with 'true' indicating wildcard.
                ''',
                'mtetriggercontextnamewildcard',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A control to allow a trigger to be configured but not used.
                When the value is 'false' the trigger is not sampled.
                ''',
                'mtetriggerenabled',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows creation and deletion of entries.
                Once made active an entry may not be modified except to
                delete it.
                ''',
                'mtetriggerentrystatus',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerFrequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of seconds to wait between trigger samples.  To
                encourage consistency in sampling, the interval is measured
                from the beginning of one check to the beginning of the next
                and the timer is restarted immediately when it expires, not
                when the check completes.
                
                If the next sample begins before the previous one completed the
                system may either attempt to make the check or treat this as an
                error condition with the error 'sampleOverrun'.
                
                A frequency of 0 indicates instantaneous recognition of the
                condition.  This is not possible in many cases, but may
                be supported in cases where it makes sense and the system is
                able to do so.  This feature allows the MIB to be used in
                implementations where such interrupt-driven behavior is
                possible and is not likely to be supported for all MIB objects
                even then since such sampling generally has to be tightly
                integrated into low-level code.
                
                Systems that can support this SHOULD document those cases
                where it can be used.  In cases where it can not, setting this
                object to 0 should be disallowed.
                ''',
                'mtetriggerfrequency',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerObjects', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteObjectsName of a group of objects from
                mteObjectsTable.  These objects are to be added to any
                Notification resulting from the firing of this trigger.
                
                A list of objects may also be added based on the event or on
                the value of mteTriggerTest.
                
                A length of 0 indicates no additional objects.
                ''',
                'mtetriggerobjects',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerObjectsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerObjects, the mteOwner of a group of
                objects from mteObjectsTable.
                ''',
                'mtetriggerobjectsowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerSampleType', REFERENCE_ENUM_CLASS, 'MtetriggersampletypeEnum' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggertable.Mtetriggerentry.MtetriggersampletypeEnum', 
                [], [], 
                '''                The type of sampling to perform.
                
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
                ''',
                'mtetriggersampletype',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerTargetTag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tag for the target(s) from which to obtain the condition
                for a trigger check.
                
                A length of 0 indicates the local system.  In this case,
                access to the objects indicated by mteTriggerValueID is under
                the security credentials of the requester that set
                mteTriggerEntryStatus to 'active'.  Those credentials are the
                input parameters for isAccessAllowed from the Architecture for
                Describing SNMP Management Frameworks.
                
                Otherwise access rights are checked according to the security
                
                parameters resulting from the tag.
                ''',
                'mtetriggertargettag',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerTest', REFERENCE_BITS, 'Mtetriggertest' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggertable.Mtetriggerentry.Mtetriggertest', 
                [], [], 
                '''                The type of trigger test to perform.  For 'boolean' and
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
                ''',
                'mtetriggertest',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerValueID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of the MIB object to sample to see
                if the trigger should fire.
                
                This may be wildcarded by truncating all or part of the
                instance portion, in which case the value is obtained
                as if with a GetNext function, checking multiple values
                
                if they exist.  If such wildcarding is applied,
                mteTriggerValueIDWildcard must be 'true' and if not it must
                be 'false'.
                
                Bad object identifiers or a mismatch between truncating the
                identifier and the value of mteTriggerValueIDWildcard result
                in operation as one would expect when providing the wrong
                identifier to a Get or GetNext operation.  The Get will fail
                or get the wrong object.  The GetNext will indeed get whatever
                is next, proceeding until it runs past the initial part of the
                identifier and perhaps many unintended objects for confusing
                results.  If the value syntax of those objects is not usable,
                that results in a 'badType' error that terminates the scan.
                
                Each instance that fills the wildcard is independent of any
                additional instances, that is, wildcarded objects operate
                as if there were a separate table entry for each instance
                that fills the wildcard without having to actually predict
                all possible instances ahead of time.
                ''',
                'mtetriggervalueid',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerValueIDWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether mteTriggerValueID is to be treated as
                fully-specified or wildcarded, with 'true' indicating wildcard.
                ''',
                'mtetriggervalueidwildcard',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggertable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggertable',
            False, 
            [
            _MetaInfoClassMember('mteTriggerEntry', REFERENCE_LIST, 'Mtetriggerentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggertable.Mtetriggerentry', 
                [], [], 
                '''                Information about a single trigger.  Applications create and
                delete entries using mteTriggerEntryStatus.
                ''',
                'mtetriggerentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry.MtetriggerdeltadiscontinuityidtypeEnum' : _MetaInfoEnum('MtetriggerdeltadiscontinuityidtypeEnum', 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB',
        {
            'timeTicks':'timeTicks',
            'timeStamp':'timeStamp',
            'dateAndTime':'dateAndTime',
        }, 'DISMAN-EVENT-MIB', _yang_ns._namespaces['DISMAN-EVENT-MIB']),
    'DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mtetriggername',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerDeltaDiscontinuityID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or
                DateAndTime object that indicates a discontinuity in the value
                at mteTriggerValueID.
                
                The OID may be for a leaf object (e.g. sysUpTime.0) or may
                be wildcarded to match mteTriggerValueID.
                
                This object supports normal checking for a discontinuity in a
                counter.  Note that if this object does not point to sysUpTime
                discontinuity checking MUST still check sysUpTime for an overall
                discontinuity.
                
                If the object identified is not accessible the sample attempt
                is in error, with the error code as from an SNMP request.
                
                Bad object identifiers or a mismatch between truncating the
                identifier and the value of mteDeltaDiscontinuityIDWildcard
                result in operation as one would expect when providing the
                wrong identifier to a Get operation.  The Get will fail or get
                the wrong object.  If the value syntax of those objects is not
                usable, that results in an error that terminates the sample
                with a 'badType' error code.
                ''',
                'mtetriggerdeltadiscontinuityid',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerDeltaDiscontinuityIDType', REFERENCE_ENUM_CLASS, 'MtetriggerdeltadiscontinuityidtypeEnum' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry.MtetriggerdeltadiscontinuityidtypeEnum', 
                [], [], 
                '''                The value 'timeTicks' indicates the
                mteTriggerDeltaDiscontinuityID of this row is of syntax
                TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp.
                The value 'dateAndTime' indicates syntax DateAndTime.
                ''',
                'mtetriggerdeltadiscontinuityidtype',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerDeltaDiscontinuityIDWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether mteTriggerDeltaDiscontinuityID is to be
                treated as fully-specified or wildcarded, with 'true'
                indicating wildcard. Note that the value of this object will
                be the same as that of the corresponding instance of
                mteTriggerValueIDWildcard when the corresponding
                
                mteTriggerSampleType is 'deltaValue'.
                ''',
                'mtetriggerdeltadiscontinuityidwildcard',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerDeltaEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerdeltatable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerdeltatable',
            False, 
            [
            _MetaInfoClassMember('mteTriggerDeltaEntry', REFERENCE_LIST, 'Mtetriggerdeltaentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry', 
                [], [], 
                '''                Information about a single trigger's delta sampling.  Entries
                automatically exist in this this table for each mteTriggerEntry
                that has mteTriggerSampleType set to 'deltaValue'.
                ''',
                'mtetriggerdeltaentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerDeltaTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mtetriggername',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerExistenceEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'existence' and this trigger fires.  A length of 0 indicates no
                event.
                ''',
                'mtetriggerexistenceevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerExistenceEvent, the mteOwner of an event
                entry from the mteEventTable.
                ''',
                'mtetriggerexistenceeventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceObjects', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteObjectsName of a group of objects from
                mteObjectsTable.  These objects are to be added to any
                Notification resulting from the firing of this trigger for
                this test.
                
                A list of objects may also be added based on the overall
                trigger, the event or other settings in mteTriggerTest.
                
                A length of 0 indicates no additional objects.
                ''',
                'mtetriggerexistenceobjects',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceObjectsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerExistenceObjects, the mteOwner of a
                group of objects from mteObjectsTable.
                ''',
                'mtetriggerexistenceobjectsowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceStartup', REFERENCE_BITS, 'Mtetriggerexistencestartup' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencestartup', 
                [], [], 
                '''                Control for whether an event may be triggered when this entry
                is first set to 'active' and the test specified by
                mteTriggerExistenceTest is true.  Setting an option causes
                that trigger to fire when its test is true.
                ''',
                'mtetriggerexistencestartup',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceTest', REFERENCE_BITS, 'Mtetriggerexistencetest' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry.Mtetriggerexistencetest', 
                [], [], 
                '''                The type of existence test to perform.  The trigger fires
                when the object at mteTriggerValueID is seen to go from
                present to absent, from absent to present, or to have it's
                value changed, depending on which tests are selected:
                
                present(0) - when this test is selected, the trigger fires
                when the mteTriggerValueID object goes from absent to present.
                
                absent(1)  - when this test is selected, the trigger fires
                when the mteTriggerValueID object goes from present to absent.
                changed(2) - when this test is selected, the trigger fires
                the mteTriggerValueID object value changes.
                
                Once the trigger has fired for either presence or absence it
                will not fire again for that state until the object has been
                to the other state. 
                ''',
                'mtetriggerexistencetest',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerExistenceEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerexistencetable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerexistencetable',
            False, 
            [
            _MetaInfoClassMember('mteTriggerExistenceEntry', REFERENCE_LIST, 'Mtetriggerexistenceentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry', 
                [], [], 
                '''                Information about a single existence trigger.  Entries
                automatically exist in this this table for each mteTriggerEntry
                that has 'existence' set in mteTriggerTest.
                ''',
                'mtetriggerexistenceentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerExistenceTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry.MtetriggerbooleancomparisonEnum' : _MetaInfoEnum('MtetriggerbooleancomparisonEnum', 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB',
        {
            'unequal':'unequal',
            'equal':'equal',
            'less':'less',
            'lessOrEqual':'lessOrEqual',
            'greater':'greater',
            'greaterOrEqual':'greaterOrEqual',
        }, 'DISMAN-EVENT-MIB', _yang_ns._namespaces['DISMAN-EVENT-MIB']),
    'DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mtetriggername',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerBooleanComparison', REFERENCE_ENUM_CLASS, 'MtetriggerbooleancomparisonEnum' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry.MtetriggerbooleancomparisonEnum', 
                [], [], 
                '''                The type of boolean comparison to perform.
                
                The value at mteTriggerValueID is compared to
                mteTriggerBooleanValue, so for example if
                mteTriggerBooleanComparison is 'less' the result would be true
                if the value at mteTriggerValueID is less than the value of
                mteTriggerBooleanValue.
                ''',
                'mtetriggerbooleancomparison',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'boolean' and this trigger fires.  A length of 0 indicates no
                event.
                ''',
                'mtetriggerbooleanevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerBooleanEvent, the mteOwner of an event
                entry from mteEventTable.
                ''',
                'mtetriggerbooleaneventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanObjects', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteObjectsName of a group of objects from
                mteObjectsTable.  These objects are to be added to any
                Notification resulting from the firing of this trigger for
                this test.
                
                A list of objects may also be added based on the overall
                trigger, the event or other settings in mteTriggerTest.
                
                A length of 0 indicates no additional objects.
                ''',
                'mtetriggerbooleanobjects',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanObjectsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerBooleanObjects, the mteOwner of a group
                of objects from mteObjectsTable.
                ''',
                'mtetriggerbooleanobjectsowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanStartup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether an event may be triggered when this entry
                is first set to 'active' or a new instance of the object at
                mteTriggerValueID is found and the test specified by
                mteTriggerBooleanComparison is true.  In that case an event is
                triggered if mteTriggerBooleanStartup is 'true'.
                ''',
                'mtetriggerbooleanstartup',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanValue', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value to use for the test specified by
                mteTriggerBooleanTest.
                ''',
                'mtetriggerbooleanvalue',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerBooleanEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerbooleantable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerbooleantable',
            False, 
            [
            _MetaInfoClassMember('mteTriggerBooleanEntry', REFERENCE_LIST, 'Mtetriggerbooleanentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry', 
                [], [], 
                '''                Information about a single boolean trigger.  Entries
                automatically exist in this this table for each mteTriggerEntry
                that has 'boolean' set in mteTriggerTest.
                ''',
                'mtetriggerbooleanentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerBooleanTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry.MtetriggerthresholdstartupEnum' : _MetaInfoEnum('MtetriggerthresholdstartupEnum', 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB',
        {
            'rising':'rising',
            'falling':'falling',
            'risingOrFalling':'risingOrFalling',
        }, 'DISMAN-EVENT-MIB', _yang_ns._namespaces['DISMAN-EVENT-MIB']),
    'DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mtetriggername',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteTriggerThresholdDeltaFalling', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold value to check against if mteTriggerType is
                'threshold'.
                
                When the delta value (difference) between the current sampled
                value (value(n)) and the previous sampled value (value(n-1))
                is less than or equal to this threshold,
                and the delta value calculated at the last sampling interval
                (i.e. value(n-1) - value(n-2)) was greater than this threshold,
                one mteTriggerThresholdDeltaFallingEvent is triggered. That event
                is also triggered if the first delta value calculated after this
                entry becomes active, i.e. value(2) - value(1), where value(1)
                is the first sample taken of that instance, is less than or
                equal to this threshold.
                
                After a falling event is generated, another such event is not
                triggered until the delta value falls below this threshold and
                reaches mteTriggerThresholdDeltaRising.
                ''',
                'mtetriggerthresholddeltafalling',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdDeltaFallingEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'threshold' and this trigger fires based on
                mteTriggerThresholdDeltaFalling.  A length of 0 indicates
                no event.
                ''',
                'mtetriggerthresholddeltafallingevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdDeltaFallingEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner
                of an event entry from mteEventTable.
                ''',
                'mtetriggerthresholddeltafallingeventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdDeltaRising', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold value to check against if mteTriggerType is
                'threshold'.
                
                When the delta value (difference) between the current sampled
                value (value(n)) and the previous sampled value (value(n-1))
                is greater than or equal to this threshold,
                and the delta value calculated at the last sampling interval
                (i.e. value(n-1) - value(n-2)) was less than this threshold,
                one mteTriggerThresholdDeltaRisingEvent is triggered. That event
                is also triggered if the first delta value calculated after this
                entry becomes active, i.e. value(2) - value(1), where value(1)
                is the first sample taken of that instance, is greater than or
                equal to this threshold.
                
                After a rising event is generated, another such event is not
                triggered until the delta value falls below this threshold and
                reaches mteTriggerThresholdDeltaFalling.
                ''',
                'mtetriggerthresholddeltarising',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdDeltaRisingEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'threshold' and this trigger fires based on
                mteTriggerThresholdDeltaRising. A length of 0 indicates
                no event.
                ''',
                'mtetriggerthresholddeltarisingevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdDeltaRisingEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner
                of an event entry from mteEventTable.
                ''',
                'mtetriggerthresholddeltarisingeventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdFalling', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold value to check against if mteTriggerType is
                'threshold'.
                
                When the current sampled value is less than or equal to this
                threshold, and the value at the last sampling interval was
                greater than this threshold, one
                mteTriggerThresholdFallingEvent is triggered.  That event is
                also triggered if the first sample after this entry becomes
                active is less than or equal to this threshold and
                mteTriggerThresholdStartup is equal to 'falling' or
                'risingOrFalling'.
                
                After a falling event is generated, another such event is not
                triggered until the sampled value rises above this threshold
                and reaches mteTriggerThresholdRising.
                ''',
                'mtetriggerthresholdfalling',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdFallingEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'threshold' and this trigger fires based on
                mteTriggerThresholdFalling.  A length of 0 indicates no event.
                ''',
                'mtetriggerthresholdfallingevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdFallingEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerThresholdFallingEvent, the mteOwner of an
                event entry from mteEventTable.
                ''',
                'mtetriggerthresholdfallingeventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdObjects', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteObjectsName of a group of objects from
                mteObjectsTable.  These objects are to be added to any
                Notification resulting from the firing of this trigger for
                this test.
                
                A list of objects may also be added based on the overall
                
                trigger, the event or other settings in mteTriggerTest.
                
                A length of 0 indicates no additional objects.
                ''',
                'mtetriggerthresholdobjects',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdObjectsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerThresholdObjects, the mteOwner of a group
                of objects from mteObjectsTable.
                ''',
                'mtetriggerthresholdobjectsowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdRising', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold value to check against if mteTriggerType is
                'threshold'.
                
                When the current sampled value is greater than or equal to
                this threshold, and the value at the last sampling interval
                was less than this threshold, one
                mteTriggerThresholdRisingEvent is triggered.  That event is
                also triggered if the first sample after this entry becomes
                active is greater than or equal to this threshold and
                mteTriggerThresholdStartup is equal to 'rising' or
                'risingOrFalling'.
                
                After a rising event is generated, another such event is not
                triggered until the sampled value falls below this threshold
                and reaches mteTriggerThresholdFalling.
                ''',
                'mtetriggerthresholdrising',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdRisingEvent', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteEventName of the event to invoke when mteTriggerType is
                'threshold' and this trigger fires based on
                mteTriggerThresholdRising.  A length of 0 indicates no event.
                ''',
                'mtetriggerthresholdrisingevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdRisingEventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteTriggerThresholdRisingEvent, the mteOwner of an
                event entry from mteEventTable.
                ''',
                'mtetriggerthresholdrisingeventowner',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdStartup', REFERENCE_ENUM_CLASS, 'MtetriggerthresholdstartupEnum' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry.MtetriggerthresholdstartupEnum', 
                [], [], 
                '''                The event that may be triggered when this entry is first
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
                ''',
                'mtetriggerthresholdstartup',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerThresholdEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mtetriggerthresholdtable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mtetriggerthresholdtable',
            False, 
            [
            _MetaInfoClassMember('mteTriggerThresholdEntry', REFERENCE_LIST, 'Mtetriggerthresholdentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry', 
                [], [], 
                '''                Information about a single threshold trigger.  Entries
                automatically exist in this table for each mteTriggerEntry
                that has 'threshold' set in mteTriggerTest.
                ''',
                'mtetriggerthresholdentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteTriggerThresholdTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteobjectstable.Mteobjectsentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteobjectstable.Mteobjectsentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteObjectsName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A locally-unique, administratively assigned name for a group
                of objects.
                ''',
                'mteobjectsname',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteObjectsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer for the purpose of identifying
                individual objects within a mteObjectsName group.
                
                Objects within a group are placed in the notification in the
                numerical order of this index.
                
                Groups are placed in the notification in the order of the
                selections for overall trigger, trigger test, and event.
                Within trigger test they are in the same order as the
                numerical values of the bits defined for mteTriggerTest.
                
                Bad object identifiers or a mismatch between truncating the
                identifier and the value of mteDeltaDiscontinuityIDWildcard
                result in operation as one would expect when providing the
                wrong identifier to a Get operation.  The Get will fail or get
                the wrong object.  If the object is not available it is omitted
                from the notification.
                ''',
                'mteobjectsindex',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteObjectsEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows creation and deletion of entries.
                Once made active an entry MAY not be modified except to
                delete it.
                ''',
                'mteobjectsentrystatus',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteObjectsID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of a MIB object to add to a
                Notification that results from the firing of a trigger.
                
                This may be wildcarded by truncating all or part of the
                instance portion, in which case the instance portion of the
                OID for obtaining this object will be the same as that used
                in obtaining the mteTriggerValueID that fired.  If such
                wildcarding is applied, mteObjectsIDWildcard must be
                'true' and if not it must be 'false'.
                
                Each instance that fills the wildcard is independent of any
                additional instances, that is, wildcarded objects operate
                as if there were a separate table entry for each instance
                that fills the wildcard without having to actually predict
                all possible instances ahead of time.
                ''',
                'mteobjectsid',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteObjectsIDWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether mteObjectsID is to be treated as
                fully-specified or wildcarded, with 'true' indicating wildcard.
                ''',
                'mteobjectsidwildcard',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteObjectsEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteobjectstable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteobjectstable',
            False, 
            [
            _MetaInfoClassMember('mteObjectsEntry', REFERENCE_LIST, 'Mteobjectsentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteobjectstable.Mteobjectsentry', 
                [], [], 
                '''                A group of objects.  Applications create and delete entries
                using mteObjectsEntryStatus.
                
                When adding objects to a notification they are added in the
                lexical order of their index in this table.  Those associated
                with a trigger come first, then trigger test, then event.
                ''',
                'mteobjectsentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteObjectsTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventtable.Mteevententry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventtable.Mteevententry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A locally-unique, administratively assigned name for the
                event.
                ''',
                'mteeventname',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventActions', REFERENCE_BITS, 'Mteeventactions' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventtable.Mteevententry.Mteeventactions', 
                [], [], 
                '''                The actions to perform when this event occurs.
                
                For 'notification', Traps and/or Informs are sent according
                to the configuration in the SNMP Notification MIB.
                
                For 'set', an SNMP Set operation is performed according to
                control values in this entry.
                ''',
                'mteeventactions',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventComment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A description of the event's function and use.
                ''',
                'mteeventcomment',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A control to allow an event to be configured but not used.
                When the value is 'false' the event does not execute even if
                
                triggered.
                ''',
                'mteeventenabled',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows creation and deletion of entries.
                Once made active an entry MAY not be modified except to
                delete it.
                ''',
                'mteevententrystatus',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventtable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventtable',
            False, 
            [
            _MetaInfoClassMember('mteEventEntry', REFERENCE_LIST, 'Mteevententry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventtable.Mteevententry', 
                [], [], 
                '''                Information about a single event.  Applications create and
                delete entries using mteEventEntryStatus.
                ''',
                'mteevententry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mteeventname',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventNotification', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier from the NOTIFICATION-TYPE for the
                notification to use if metEventActions has 'notification' set.
                ''',
                'mteeventnotification',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventNotificationObjects', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The mteObjectsName of a group of objects from
                mteObjectsTable if mteEventActions has 'notification' set.
                These objects are to be added to any Notification generated by
                this event.
                
                Objects may also be added based on the trigger that stimulated
                the event.
                
                A length of 0 indicates no additional objects.
                ''',
                'mteeventnotificationobjects',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventNotificationObjectsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                To go with mteEventNotificationObjects, the mteOwner of a
                group of objects from mteObjectsTable.
                ''',
                'mteeventnotificationobjectsowner',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventNotificationEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventnotificationtable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventnotificationtable',
            False, 
            [
            _MetaInfoClassMember('mteEventNotificationEntry', REFERENCE_LIST, 'Mteeventnotificationentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry', 
                [], [], 
                '''                Information about a single event's notification.  Entries
                automatically exist in this this table for each mteEventEntry
                that has 'notification' set in mteEventActions.
                ''',
                'mteeventnotificationentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventNotificationTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventsettable.Mteeventsetentry' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventsettable.Mteeventsetentry',
            False, 
            [
            _MetaInfoClassMember('mteOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'mteowner',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'mteeventname',
                'DISMAN-EVENT-MIB', True),
            _MetaInfoClassMember('mteEventSetContextName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The management context in which to set mteEventObjectID.
                if mteEventActions has 'set' set.
                
                This may be wildcarded by leaving characters off the end.  To
                indicate such wildcarding mteEventSetContextNameWildcard must
                be 'true'.
                
                If this context name is wildcarded the value used to complete
                the wildcarding of mteTriggerContextName will be appended.
                ''',
                'mteeventsetcontextname',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetContextNameWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control for whether mteEventSetContextName is to be treated as
                fully-specified or wildcarded, with 'true' indicating wildcard
                if mteEventActions has 'set' set.
                ''',
                'mteeventsetcontextnamewildcard',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetObject', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier from the MIB object to set if
                mteEventActions has 'set' set.
                
                This object identifier may be wildcarded by leaving
                sub-identifiers off the end, in which case
                nteEventSetObjectWildCard must be 'true'.
                
                If mteEventSetObject is wildcarded the instance used to set the
                object to which it points is the same as the instance from the
                value of mteTriggerValueID that triggered the event.
                
                Each instance that fills the wildcard is independent of any
                additional instances, that is, wildcarded objects operate
                as if there were a separate table entry for each instance
                that fills the wildcard without having to actually predict
                all possible instances ahead of time.
                
                Bad object identifiers or a mismatch between truncating the
                identifier and the value of mteSetObjectWildcard
                result in operation as one would expect when providing the
                wrong identifier to a Set operation.  The Set will fail or set
                the wrong object.  If the value syntax of the destination
                object is not correct, the Set fails with the normal SNMP
                error code.
                ''',
                'mteeventsetobject',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetObjectWildcard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control over whether mteEventSetObject is to be treated as
                fully-specified or wildcarded, with 'true' indicating wildcard
                if mteEventActions has 'set' set.
                ''',
                'mteeventsetobjectwildcard',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetTargetTag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tag for the target(s) at which to set the object at
                mteEventSetObject to mteEventSetValue if mteEventActions
                has 'set' set.
                
                Systems limited to self management MAY reject a non-zero
                length for the value of this object.
                
                A length of 0 indicates the local system.  In this case,
                access to the objects indicated by mteEventSetObject is under
                the security credentials of the requester that set
                mteTriggerEntryStatus to 'active'.  Those credentials are the
                input parameters for isAccessAllowed from the Architecture for
                Describing SNMP Management Frameworks.
                
                Otherwise access rights are checked according to the security
                parameters resulting from the tag.
                ''',
                'mteeventsettargettag',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetValue', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value to which to set the object at mteEventSetObject
                if mteEventActions has 'set' set.
                ''',
                'mteeventsetvalue',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventSetEntry',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib.Mteeventsettable' : {
        'meta_info' : _MetaInfoClass('DismanEventMib.Mteeventsettable',
            False, 
            [
            _MetaInfoClassMember('mteEventSetEntry', REFERENCE_LIST, 'Mteeventsetentry' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventsettable.Mteeventsetentry', 
                [], [], 
                '''                Information about a single event's set option.  Entries
                automatically exist in this this table for each mteEventEntry
                that has 'set' set in mteEventActions.
                ''',
                'mteeventsetentry',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'mteEventSetTable',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
    'DismanEventMib' : {
        'meta_info' : _MetaInfoClass('DismanEventMib',
            False, 
            [
            _MetaInfoClassMember('mteEvent', REFERENCE_CLASS, 'Mteevent' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteevent', 
                [], [], 
                '''                ''',
                'mteevent',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventNotificationTable', REFERENCE_CLASS, 'Mteeventnotificationtable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventnotificationtable', 
                [], [], 
                '''                A table of information about notifications to be sent as a
                consequence of management events.
                ''',
                'mteeventnotificationtable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventSetTable', REFERENCE_CLASS, 'Mteeventsettable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventsettable', 
                [], [], 
                '''                A table of management event action information.
                ''',
                'mteeventsettable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteEventTable', REFERENCE_CLASS, 'Mteeventtable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteeventtable', 
                [], [], 
                '''                A table of management event action information.
                ''',
                'mteeventtable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteObjectsTable', REFERENCE_CLASS, 'Mteobjectstable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteobjectstable', 
                [], [], 
                '''                A table of objects that can be added to notifications based
                on the trigger, trigger test, or event, as pointed to by
                entries in those tables.
                ''',
                'mteobjectstable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteResource', REFERENCE_CLASS, 'Mteresource' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mteresource', 
                [], [], 
                '''                ''',
                'mteresource',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTrigger', REFERENCE_CLASS, 'Mtetrigger' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetrigger', 
                [], [], 
                '''                ''',
                'mtetrigger',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerBooleanTable', REFERENCE_CLASS, 'Mtetriggerbooleantable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerbooleantable', 
                [], [], 
                '''                A table of management event trigger information for boolean
                triggers.
                ''',
                'mtetriggerbooleantable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerDeltaTable', REFERENCE_CLASS, 'Mtetriggerdeltatable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerdeltatable', 
                [], [], 
                '''                A table of management event trigger information for delta
                sampling.
                ''',
                'mtetriggerdeltatable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerExistenceTable', REFERENCE_CLASS, 'Mtetriggerexistencetable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerexistencetable', 
                [], [], 
                '''                A table of management event trigger information for existence
                triggers.
                ''',
                'mtetriggerexistencetable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerTable', REFERENCE_CLASS, 'Mtetriggertable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggertable', 
                [], [], 
                '''                A table of management event trigger information.
                ''',
                'mtetriggertable',
                'DISMAN-EVENT-MIB', False),
            _MetaInfoClassMember('mteTriggerThresholdTable', REFERENCE_CLASS, 'Mtetriggerthresholdtable' , 'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB', 'DismanEventMib.Mtetriggerthresholdtable', 
                [], [], 
                '''                A table of management event trigger information for threshold
                triggers.
                ''',
                'mtetriggerthresholdtable',
                'DISMAN-EVENT-MIB', False),
            ],
            'DISMAN-EVENT-MIB',
            'DISMAN-EVENT-MIB',
            _yang_ns._namespaces['DISMAN-EVENT-MIB'],
        'ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB'
        ),
    },
}
_meta_table['DismanEventMib.Mtetriggertable.Mtetriggerentry']['meta_info'].parent =_meta_table['DismanEventMib.Mtetriggertable']['meta_info']
_meta_table['DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry']['meta_info'].parent =_meta_table['DismanEventMib.Mtetriggerdeltatable']['meta_info']
_meta_table['DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry']['meta_info'].parent =_meta_table['DismanEventMib.Mtetriggerexistencetable']['meta_info']
_meta_table['DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry']['meta_info'].parent =_meta_table['DismanEventMib.Mtetriggerbooleantable']['meta_info']
_meta_table['DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry']['meta_info'].parent =_meta_table['DismanEventMib.Mtetriggerthresholdtable']['meta_info']
_meta_table['DismanEventMib.Mteobjectstable.Mteobjectsentry']['meta_info'].parent =_meta_table['DismanEventMib.Mteobjectstable']['meta_info']
_meta_table['DismanEventMib.Mteeventtable.Mteevententry']['meta_info'].parent =_meta_table['DismanEventMib.Mteeventtable']['meta_info']
_meta_table['DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry']['meta_info'].parent =_meta_table['DismanEventMib.Mteeventnotificationtable']['meta_info']
_meta_table['DismanEventMib.Mteeventsettable.Mteeventsetentry']['meta_info'].parent =_meta_table['DismanEventMib.Mteeventsettable']['meta_info']
_meta_table['DismanEventMib.Mteresource']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetrigger']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mteevent']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetriggertable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetriggerdeltatable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetriggerexistencetable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetriggerbooleantable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mtetriggerthresholdtable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mteobjectstable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mteeventtable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mteeventnotificationtable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
_meta_table['DismanEventMib.Mteeventsettable']['meta_info'].parent =_meta_table['DismanEventMib']['meta_info']
