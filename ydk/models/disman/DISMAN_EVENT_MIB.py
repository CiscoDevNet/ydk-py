""" DISMAN_EVENT_MIB 

The MIB module for defining event triggers and actions
for network management purposes.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class FailureReason_Enum(Enum):
    """
    FailureReason_Enum

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

    """

    SAMPLEOVERRUN = -6

    BADTYPE = -5

    NORESPONSE = -4

    DESTINATIONUNREACHABLE = -3

    BADDESTINATION = -2

    LOCALRESOURCELACK = -1

    NOERROR = 0

    TOOBIG = 1

    NOSUCHNAME = 2

    BADVALUE = 3

    READONLY = 4

    GENERR = 5

    NOACCESS = 6

    WRONGTYPE = 7

    WRONGLENGTH = 8

    WRONGENCODING = 9

    WRONGVALUE = 10

    NOCREATION = 11

    INCONSISTENTVALUE = 12

    RESOURCEUNAVAILABLE = 13

    COMMITFAILED = 14

    UNDOFAILED = 15

    AUTHORIZATIONERROR = 16

    NOTWRITABLE = 17

    INCONSISTENTNAME = 18


    @staticmethod
    def _meta_info():
        from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
        return meta._meta_table['FailureReason_Enum']



class DISMANEVENTMIB(object):
    """
    
    
    .. attribute:: mteevent
    
    	
    	**type**\: :py:class:`MteEvent <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEvent>`
    
    .. attribute:: mteeventnotificationtable
    
    	A table of information about notifications to be sent as a consequence of management events
    	**type**\: :py:class:`MteEventNotificationTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventNotificationTable>`
    
    .. attribute:: mteeventsettable
    
    	A table of management event action information
    	**type**\: :py:class:`MteEventSetTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventSetTable>`
    
    .. attribute:: mteeventtable
    
    	A table of management event action information
    	**type**\: :py:class:`MteEventTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable>`
    
    .. attribute:: mteobjectstable
    
    	A table of objects that can be added to notifications based on the trigger, trigger test, or event, as pointed to by entries in those tables
    	**type**\: :py:class:`MteObjectsTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteObjectsTable>`
    
    .. attribute:: mteresource
    
    	
    	**type**\: :py:class:`MteResource <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteResource>`
    
    .. attribute:: mtetrigger
    
    	
    	**type**\: :py:class:`MteTrigger <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTrigger>`
    
    .. attribute:: mtetriggerbooleantable
    
    	A table of management event trigger information for boolean triggers
    	**type**\: :py:class:`MteTriggerBooleanTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable>`
    
    .. attribute:: mtetriggerdeltatable
    
    	A table of management event trigger information for delta sampling
    	**type**\: :py:class:`MteTriggerDeltaTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable>`
    
    .. attribute:: mtetriggerexistencetable
    
    	A table of management event trigger information for existence triggers
    	**type**\: :py:class:`MteTriggerExistenceTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable>`
    
    .. attribute:: mtetriggertable
    
    	A table of management event trigger information
    	**type**\: :py:class:`MteTriggerTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable>`
    
    .. attribute:: mtetriggerthresholdtable
    
    	A table of management event trigger information for threshold triggers
    	**type**\: :py:class:`MteTriggerThresholdTable <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable>`
    
    

    """

    _prefix = 'disman-event'
    _revision = '2000-10-16'

    def __init__(self):
        self.mteevent = DISMANEVENTMIB.MteEvent()
        self.mteevent.parent = self
        self.mteeventnotificationtable = DISMANEVENTMIB.MteEventNotificationTable()
        self.mteeventnotificationtable.parent = self
        self.mteeventsettable = DISMANEVENTMIB.MteEventSetTable()
        self.mteeventsettable.parent = self
        self.mteeventtable = DISMANEVENTMIB.MteEventTable()
        self.mteeventtable.parent = self
        self.mteobjectstable = DISMANEVENTMIB.MteObjectsTable()
        self.mteobjectstable.parent = self
        self.mteresource = DISMANEVENTMIB.MteResource()
        self.mteresource.parent = self
        self.mtetrigger = DISMANEVENTMIB.MteTrigger()
        self.mtetrigger.parent = self
        self.mtetriggerbooleantable = DISMANEVENTMIB.MteTriggerBooleanTable()
        self.mtetriggerbooleantable.parent = self
        self.mtetriggerdeltatable = DISMANEVENTMIB.MteTriggerDeltaTable()
        self.mtetriggerdeltatable.parent = self
        self.mtetriggerexistencetable = DISMANEVENTMIB.MteTriggerExistenceTable()
        self.mtetriggerexistencetable.parent = self
        self.mtetriggertable = DISMANEVENTMIB.MteTriggerTable()
        self.mtetriggertable.parent = self
        self.mtetriggerthresholdtable = DISMANEVENTMIB.MteTriggerThresholdTable()
        self.mtetriggerthresholdtable.parent = self


    class MteEvent(object):
        """
        
        
        .. attribute:: mteeventfailures
        
        	The number of times an attempt to invoke an event has failed.  This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'disman-event'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mteeventfailures is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteEvent']['meta_info']


    class MteEventNotificationTable(object):
        """
        A table of information about notifications to be sent as a
        consequence of management events.
        
        .. attribute:: mteeventnotificationentry
        
        	Information about a single event's notification.  Entries automatically exist in this this table for each mteEventEntry that has 'notification' set in mteEventActions
        	**type**\: list of :py:class:`MteEventNotificationEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteeventnotificationentry = YList()
            self.mteeventnotificationentry.parent = self
            self.mteeventnotificationentry.name = 'mteeventnotificationentry'


        class MteEventNotificationEntry(object):
            """
            Information about a single event's notification.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'notification' set in mteEventActions.
            
            .. attribute:: mteeventname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mteeventnotification
            
            	The object identifier from the NOTIFICATION\-TYPE for the notification to use if metEventActions has 'notification' set
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventnotificationobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable if mteEventActions has 'notification' set. These objects are to be added to any Notification generated by this event.  Objects may also be added based on the trigger that stimulated the event.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mteeventnotificationobjectsowner
            
            	To go with mteEventNotificationObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteeventname = None
                self.mteowner = None
                self.mteeventnotification = None
                self.mteeventnotificationobjects = None
                self.mteeventnotificationobjectsowner = None

            @property
            def _common_path(self):
                if self.mteeventname is None:
                    raise YPYDataValidationError('Key property mteeventname is None')
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventNotificationTable/DISMAN-EVENT-MIB:mteEventNotificationEntry[DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + '][DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mteeventname is not None:
                    return True

                if self.mteowner is not None:
                    return True

                if self.mteeventnotification is not None:
                    return True

                if self.mteeventnotificationobjects is not None:
                    return True

                if self.mteeventnotificationobjectsowner is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteEventNotificationTable.MteEventNotificationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventNotificationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mteeventnotificationentry is not None:
                for child_ref in self.mteeventnotificationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteEventNotificationTable']['meta_info']


    class MteEventSetTable(object):
        """
        A table of management event action information.
        
        .. attribute:: mteeventsetentry
        
        	Information about a single event's set option.  Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions
        	**type**\: list of :py:class:`MteEventSetEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteeventsetentry = YList()
            self.mteeventsetentry.parent = self
            self.mteeventsetentry.name = 'mteeventsetentry'


        class MteEventSetEntry(object):
            """
            Information about a single event's set option.  Entries
            automatically exist in this this table for each mteEventEntry
            that has 'set' set in mteEventActions.
            
            .. attribute:: mteeventname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mteeventsetcontextname
            
            	The management context in which to set mteEventObjectID. if mteEventActions has 'set' set.  This may be wildcarded by leaving characters off the end.  To indicate such wildcarding mteEventSetContextNameWildcard must be 'true'.  If this context name is wildcarded the value used to complete the wildcarding of mteTriggerContextName will be appended
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mteeventsetcontextnamewildcard
            
            	Control for whether mteEventSetContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            .. attribute:: mteeventsetobject
            
            	The object identifier from the MIB object to set if mteEventActions has 'set' set.  This object identifier may be wildcarded by leaving sub\-identifiers off the end, in which case nteEventSetObjectWildCard must be 'true'.  If mteEventSetObject is wildcarded the instance used to set the object to which it points is the same as the instance from the value of mteTriggerValueID that triggered the event.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteSetObjectWildcard result in operation as one would expect when providing the wrong identifier to a Set operation.  The Set will fail or set the wrong object.  If the value syntax of the destination object is not correct, the Set fails with the normal SNMP error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteeventsetobjectwildcard
            
            	Control over whether mteEventSetObject is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set
            	**type**\: bool
            
            .. attribute:: mteeventsettargettag
            
            	The tag for the target(s) at which to set the object at mteEventSetObject to mteEventSetValue if mteEventActions has 'set' set.  Systems limited to self management MAY reject a non\-zero length for the value of this object.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteEventSetObject is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security parameters resulting from the tag
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mteeventsetvalue
            
            	The value to which to set the object at mteEventSetObject if mteEventActions has 'set' set
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteeventname = None
                self.mteowner = None
                self.mteeventsetcontextname = None
                self.mteeventsetcontextnamewildcard = None
                self.mteeventsetobject = None
                self.mteeventsetobjectwildcard = None
                self.mteeventsettargettag = None
                self.mteeventsetvalue = None

            @property
            def _common_path(self):
                if self.mteeventname is None:
                    raise YPYDataValidationError('Key property mteeventname is None')
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventSetTable/DISMAN-EVENT-MIB:mteEventSetEntry[DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + '][DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mteeventname is not None:
                    return True

                if self.mteowner is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteEventSetTable.MteEventSetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mteeventsetentry is not None:
                for child_ref in self.mteeventsetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteEventSetTable']['meta_info']


    class MteEventTable(object):
        """
        A table of management event action information.
        
        .. attribute:: mteevententry
        
        	Information about a single event.  Applications create and delete entries using mteEventEntryStatus
        	**type**\: list of :py:class:`MteEventEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteevententry = YList()
            self.mteevententry.parent = self
            self.mteevententry.name = 'mteevententry'


        class MteEventEntry(object):
            """
            Information about a single event.  Applications create and
            delete entries using mteEventEntryStatus.
            
            .. attribute:: mteeventname
            
            	A locally\-unique, administratively assigned name for the event
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mteeventactions
            
            	The actions to perform when this event occurs.  For 'notification', Traps and/or Informs are sent according to the configuration in the SNMP Notification MIB.  For 'set', an SNMP Set operation is performed according to control values in this entry
            	**type**\: :py:class:`MteEventActions_Bits <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteEventTable.MteEventEntry.MteEventActions_Bits>`
            
            .. attribute:: mteeventcomment
            
            	A description of the event's function and use
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mteeventenabled
            
            	A control to allow an event to be configured but not used. When the value is 'false' the event does not execute even if  triggered
            	**type**\: bool
            
            .. attribute:: mteevententrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteeventname = None
                self.mteowner = None
                self.mteeventactions = DISMANEVENTMIB.MteEventTable.MteEventEntry.MteEventActions_Bits()
                self.mteeventcomment = None
                self.mteeventenabled = None
                self.mteevententrystatus = None

            class MteEventActions_Bits(FixedBitsDict):
                """
                MteEventActions_Bits

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
                if self.mteeventname is None:
                    raise YPYDataValidationError('Key property mteeventname is None')
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventTable/DISMAN-EVENT-MIB:mteEventEntry[DISMAN-EVENT-MIB:mteEventName = ' + str(self.mteeventname) + '][DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mteeventname is not None:
                    return True

                if self.mteowner is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteEventTable.MteEventEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteEventTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mteevententry is not None:
                for child_ref in self.mteevententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteEventTable']['meta_info']


    class MteObjectsTable(object):
        """
        A table of objects that can be added to notifications based
        on the trigger, trigger test, or event, as pointed to by
        entries in those tables.
        
        .. attribute:: mteobjectsentry
        
        	A group of objects.  Applications create and delete entries using mteObjectsEntryStatus.  When adding objects to a notification they are added in the lexical order of their index in this table.  Those associated with a trigger come first, then trigger test, then event
        	**type**\: list of :py:class:`MteObjectsEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mteobjectsentry = YList()
            self.mteobjectsentry.parent = self
            self.mteobjectsentry.name = 'mteobjectsentry'


        class MteObjectsEntry(object):
            """
            A group of objects.  Applications create and delete entries
            using mteObjectsEntryStatus.
            
            When adding objects to a notification they are added in the
            lexical order of their index in this table.  Those associated
            with a trigger come first, then trigger test, then event.
            
            .. attribute:: mteobjectsindex
            
            	An arbitrary integer for the purpose of identifying individual objects within a mteObjectsName group.  Objects within a group are placed in the notification in the numerical order of this index.  Groups are placed in the notification in the order of the selections for overall trigger, trigger test, and event. Within trigger test they are in the same order as the numerical values of the bits defined for mteTriggerTest.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the object is not available it is omitted from the notification
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mteobjectsname
            
            	A locally\-unique, administratively assigned name for a group of objects
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mteobjectsentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mteobjectsid
            
            	The object identifier of a MIB object to add to a Notification that results from the firing of a trigger.  This may be wildcarded by truncating all or part of the instance portion, in which case the instance portion of the OID for obtaining this object will be the same as that used in obtaining the mteTriggerValueID that fired.  If such wildcarding is applied, mteObjectsIDWildcard must be 'true' and if not it must be 'false'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mteobjectsidwildcard
            
            	Control for whether mteObjectsID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteobjectsindex = None
                self.mteobjectsname = None
                self.mteowner = None
                self.mteobjectsentrystatus = None
                self.mteobjectsid = None
                self.mteobjectsidwildcard = None

            @property
            def _common_path(self):
                if self.mteobjectsindex is None:
                    raise YPYDataValidationError('Key property mteobjectsindex is None')
                if self.mteobjectsname is None:
                    raise YPYDataValidationError('Key property mteobjectsname is None')
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteObjectsTable/DISMAN-EVENT-MIB:mteObjectsEntry[DISMAN-EVENT-MIB:mteObjectsIndex = ' + str(self.mteobjectsindex) + '][DISMAN-EVENT-MIB:mteObjectsName = ' + str(self.mteobjectsname) + '][DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mteobjectsindex is not None:
                    return True

                if self.mteobjectsname is not None:
                    return True

                if self.mteowner is not None:
                    return True

                if self.mteobjectsentrystatus is not None:
                    return True

                if self.mteobjectsid is not None:
                    return True

                if self.mteobjectsidwildcard is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteObjectsTable.MteObjectsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteObjectsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mteobjectsentry is not None:
                for child_ref in self.mteobjectsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteObjectsTable']['meta_info']


    class MteResource(object):
        """
        
        
        .. attribute:: mteresourcesampleinstancelacks
        
        	The number of times this system could not take a new sample because that allocation would have exceeded the limit set by mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mteresourcesampleinstancemaximum
        
        	The maximum number of instance entries this system will support for sampling.  These are the entries that maintain state, one for each instance of each sampled object as selected by mteTriggerValueID.  Note that wildcarded objects result in multiple instances of this state.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object SHOULD be 0.  Changing this value will not eliminate or inhibit existing sample state but could prevent allocation of additional state information
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mteresourcesampleinstances
        
        	The number of currently active instance entries as defined for mteResourceSampleInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mteresourcesampleinstanceshigh
        
        	The highest value of mteResourceSampleInstances that has occurred since initialization of the management system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mteresourcesampleminimum
        
        	The minimum mteTriggerFrequency this system will accept.  A system may use the larger values of this minimum to lessen the impact of constant sampling.  For larger sampling intervals the system samples less often and suffers less overhead.  This object provides a way to enforce such lower overhead for all triggers created after it is set.  Unless explicitly resource limited, a system's value for this object SHOULD be 1, allowing as small as a 1 second interval for ongoing trigger sampling.  Changing this value will not invalidate an existing setting of mteTriggerFrequency
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'disman-event'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
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

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteResource']['meta_info']


    class MteTrigger(object):
        """
        
        
        .. attribute:: mtetriggerfailures
        
        	The number of times an attempt to check for a trigger condition has failed.  This counts individually for each attempt in a group of targets or each attempt for a  wildcarded object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'disman-event'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerfailures is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTrigger']['meta_info']


    class MteTriggerBooleanTable(object):
        """
        A table of management event trigger information for boolean
        triggers.
        
        .. attribute:: mtetriggerbooleanentry
        
        	Information about a single boolean trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'boolean' set in mteTriggerTest
        	**type**\: list of :py:class:`MteTriggerBooleanEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerbooleanentry = YList()
            self.mtetriggerbooleanentry.parent = self
            self.mtetriggerbooleanentry.name = 'mtetriggerbooleanentry'


        class MteTriggerBooleanEntry(object):
            """
            Information about a single boolean trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'boolean' set in mteTriggerTest.
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggername
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mtetriggerbooleancomparison
            
            	The type of boolean comparison to perform.  The value at mteTriggerValueID is compared to mteTriggerBooleanValue, so for example if mteTriggerBooleanComparison is 'less' the result would be true if the value at mteTriggerValueID is less than the value of mteTriggerBooleanValue
            	**type**\: :py:class:`MteTriggerBooleanComparison_Enum <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry.MteTriggerBooleanComparison_Enum>`
            
            .. attribute:: mtetriggerbooleanevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'boolean' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerbooleaneventowner
            
            	To go with mteTriggerBooleanEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerbooleanobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerbooleanobjectsowner
            
            	To go with mteTriggerBooleanObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerbooleanstartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' or a new instance of the object at mteTriggerValueID is found and the test specified by mteTriggerBooleanComparison is true.  In that case an event is triggered if mteTriggerBooleanStartup is 'true'
            	**type**\: bool
            
            .. attribute:: mtetriggerbooleanvalue
            
            	The value to use for the test specified by mteTriggerBooleanTest
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'disman-event'
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

            class MteTriggerBooleanComparison_Enum(Enum):
                """
                MteTriggerBooleanComparison_Enum

                The type of boolean comparison to perform.
                
                The value at mteTriggerValueID is compared to
                mteTriggerBooleanValue, so for example if
                mteTriggerBooleanComparison is 'less' the result would be true
                if the value at mteTriggerValueID is less than the value of
                mteTriggerBooleanValue.

                """

                UNEQUAL = 1

                EQUAL = 2

                LESS = 3

                LESSOREQUAL = 4

                GREATER = 5

                GREATEROREQUAL = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry.MteTriggerBooleanComparison_Enum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYDataValidationError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerBooleanTable/DISMAN-EVENT-MIB:mteTriggerBooleanEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteTriggerBooleanTable.MteTriggerBooleanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerBooleanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerbooleanentry is not None:
                for child_ref in self.mtetriggerbooleanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTriggerBooleanTable']['meta_info']


    class MteTriggerDeltaTable(object):
        """
        A table of management event trigger information for delta
        sampling.
        
        .. attribute:: mtetriggerdeltaentry
        
        	Information about a single trigger's delta sampling.  Entries automatically exist in this this table for each mteTriggerEntry that has mteTriggerSampleType set to 'deltaValue'
        	**type**\: list of :py:class:`MteTriggerDeltaEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerdeltaentry = YList()
            self.mtetriggerdeltaentry.parent = self
            self.mtetriggerdeltaentry.name = 'mtetriggerdeltaentry'


        class MteTriggerDeltaEntry(object):
            """
            Information about a single trigger's delta sampling.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has mteTriggerSampleType set to 'deltaValue'.
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggername
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mtetriggerdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at mteTriggerValueID.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match mteTriggerValueID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking MUST still check sysUpTime for an overall discontinuity.  If the object identified is not accessible the sample attempt is in error, with the error code as from an SNMP request.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation.  The Get will fail or get the wrong object.  If the value syntax of those objects is not usable, that results in an error that terminates the sample with a 'badType' error code
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggerdeltadiscontinuityidtype
            
            	The value 'timeTicks' indicates the mteTriggerDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp. The value 'dateAndTime' indicates syntax DateAndTime
            	**type**\: :py:class:`MteTriggerDeltaDiscontinuityIDType_Enum <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry.MteTriggerDeltaDiscontinuityIDType_Enum>`
            
            .. attribute:: mtetriggerdeltadiscontinuityidwildcard
            
            	Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding  mteTriggerSampleType is 'deltaValue'
            	**type**\: bool
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerdeltadiscontinuityid = None
                self.mtetriggerdeltadiscontinuityidtype = None
                self.mtetriggerdeltadiscontinuityidwildcard = None

            class MteTriggerDeltaDiscontinuityIDType_Enum(Enum):
                """
                MteTriggerDeltaDiscontinuityIDType_Enum

                The value 'timeTicks' indicates the
                mteTriggerDeltaDiscontinuityID of this row is of syntax
                TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp.
                The value 'dateAndTime' indicates syntax DateAndTime.

                """

                TIMETICKS = 1

                TIMESTAMP = 2

                DATEANDTIME = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry.MteTriggerDeltaDiscontinuityIDType_Enum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYDataValidationError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerDeltaTable/DISMAN-EVENT-MIB:mteTriggerDeltaEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteTriggerDeltaTable.MteTriggerDeltaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerDeltaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerdeltaentry is not None:
                for child_ref in self.mtetriggerdeltaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTriggerDeltaTable']['meta_info']


    class MteTriggerExistenceTable(object):
        """
        A table of management event trigger information for existence
        triggers.
        
        .. attribute:: mtetriggerexistenceentry
        
        	Information about a single existence trigger.  Entries automatically exist in this this table for each mteTriggerEntry that has 'existence' set in mteTriggerTest
        	**type**\: list of :py:class:`MteTriggerExistenceEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerexistenceentry = YList()
            self.mtetriggerexistenceentry.parent = self
            self.mtetriggerexistenceentry.name = 'mtetriggerexistenceentry'


        class MteTriggerExistenceEntry(object):
            """
            Information about a single existence trigger.  Entries
            automatically exist in this this table for each mteTriggerEntry
            that has 'existence' set in mteTriggerTest.
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggername
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mtetriggerexistenceevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'existence' and this trigger fires.  A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerexistenceeventowner
            
            	To go with mteTriggerExistenceEvent, the mteOwner of an event entry from the mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerexistenceobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerexistenceobjectsowner
            
            	To go with mteTriggerExistenceObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerexistencestartup
            
            	Control for whether an event may be triggered when this entry is first set to 'active' and the test specified by mteTriggerExistenceTest is true.  Setting an option causes that trigger to fire when its test is true
            	**type**\: :py:class:`MteTriggerExistenceStartup_Bits <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceStartup_Bits>`
            
            .. attribute:: mtetriggerexistencetest
            
            	The type of existence test to perform.  The trigger fires when the object at mteTriggerValueID is seen to go from present to absent, from absent to present, or to have it's value changed, depending on which tests are selected\:  present(0) \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from absent to present.  absent(1)  \- when this test is selected, the trigger fires when the mteTriggerValueID object goes from present to absent. changed(2) \- when this test is selected, the trigger fires the mteTriggerValueID object value changes.  Once the trigger has fired for either presence or absence it will not fire again for that state until the object has been to the other state. 
            	**type**\: :py:class:`MteTriggerExistenceTest_Bits <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceTest_Bits>`
            
            

            """

            _prefix = 'disman-event'
            _revision = '2000-10-16'

            def __init__(self):
                self.parent = None
                self.mteowner = None
                self.mtetriggername = None
                self.mtetriggerexistenceevent = None
                self.mtetriggerexistenceeventowner = None
                self.mtetriggerexistenceobjects = None
                self.mtetriggerexistenceobjectsowner = None
                self.mtetriggerexistencestartup = DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceStartup_Bits()
                self.mtetriggerexistencetest = DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry.MteTriggerExistenceTest_Bits()

            class MteTriggerExistenceStartup_Bits(FixedBitsDict):
                """
                MteTriggerExistenceStartup_Bits

                Control for whether an event may be triggered when this entry
                is first set to 'active' and the test specified by
                mteTriggerExistenceTest is true.  Setting an option causes
                that trigger to fire when its test is true.
                Keys are:- absent , present

                """

                def __init__(self):
                    self._dictionary = { 
                        'absent':False,
                        'present':False,
                    }
                    self._pos_map = { 
                        'absent':1,
                        'present':0,
                    }

            class MteTriggerExistenceTest_Bits(FixedBitsDict):
                """
                MteTriggerExistenceTest_Bits

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
                Keys are:- absent , changed , present

                """

                def __init__(self):
                    self._dictionary = { 
                        'absent':False,
                        'changed':False,
                        'present':False,
                    }
                    self._pos_map = { 
                        'absent':1,
                        'changed':2,
                        'present':0,
                    }

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYDataValidationError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerExistenceTable/DISMAN-EVENT-MIB:mteTriggerExistenceEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteTriggerExistenceTable.MteTriggerExistenceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerExistenceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerexistenceentry is not None:
                for child_ref in self.mtetriggerexistenceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTriggerExistenceTable']['meta_info']


    class MteTriggerTable(object):
        """
        A table of management event trigger information.
        
        .. attribute:: mtetriggerentry
        
        	Information about a single trigger.  Applications create and delete entries using mteTriggerEntryStatus
        	**type**\: list of :py:class:`MteTriggerEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerentry = YList()
            self.mtetriggerentry.parent = self
            self.mtetriggerentry.name = 'mtetriggerentry'


        class MteTriggerEntry(object):
            """
            Information about a single trigger.  Applications create and
            delete entries using mteTriggerEntryStatus.
            
            .. attribute:: mteowner
            
            	The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggername
            
            	A locally\-unique, administratively assigned name for the trigger within the scope of mteOwner
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mtetriggercomment
            
            	A description of the trigger's function and use
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mtetriggercontextname
            
            	The management context from which to obtain mteTriggerValueID.  This may be wildcarded by leaving characters off the end.  For example use 'Repeater' to wildcard to 'Repeater1', 'Repeater2', 'Repeater\-999.87b', and so on.  To indicate such wildcarding is intended, mteTriggerContextNameWildcard must be 'true'.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.  Operation of this feature assumes that the local system has a list of available contexts against which to apply the wildcard.  If the objects are being read from the local system, this is clearly the system's own list of contexts. For a remote system a local version of such a list is not defined by any current standard and may not be available, so this function MAY not be supported
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mtetriggercontextnamewildcard
            
            	Control for whether mteTriggerContextName is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            .. attribute:: mtetriggerenabled
            
            	A control to allow a trigger to be configured but not used. When the value is 'false' the trigger is not sampled
            	**type**\: bool
            
            .. attribute:: mtetriggerentrystatus
            
            	The control that allows creation and deletion of entries. Once made active an entry may not be modified except to delete it
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mtetriggerfrequency
            
            	The number of seconds to wait between trigger samples.  To encourage consistency in sampling, the interval is measured from the beginning of one check to the beginning of the next and the timer is restarted immediately when it expires, not when the check completes.  If the next sample begins before the previous one completed the system may either attempt to make the check or treat this as an error condition with the error 'sampleOverrun'.  A frequency of 0 indicates instantaneous recognition of the condition.  This is not possible in many cases, but may be supported in cases where it makes sense and the system is able to do so.  This feature allows the MIB to be used in implementations where such interrupt\-driven behavior is possible and is not likely to be supported for all MIB objects even then since such sampling generally has to be tightly integrated into low\-level code.  Systems that can support this SHOULD document those cases where it can be used.  In cases where it can not, setting this object to 0 should be disallowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mtetriggerobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger.  A list of objects may also be added based on the event or on the value of mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerobjectsowner
            
            	To go with mteTriggerObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggersampletype
            
            	The type of sampling to perform.  An 'absoluteValue' sample requires only a single sample to be meaningful, and is exactly the value of the object at mteTriggerValueID at the sample time.  A 'deltaValue' requires two samples to be meaningful and is thus not available for testing until the second and subsequent samples after the object at mteTriggerValueID is first found to exist.  It is the difference between the two samples.  For unsigned values it is always positive, based on unsigned arithmetic.  For signed values it can be positive or negative.  For SNMP counters to be meaningful they should be sampled as a 'deltaValue'.  For 'deltaValue' mteTriggerDeltaTable contains further parameters.  If only 'existence' is set in mteTriggerTest this object has no meaning
            	**type**\: :py:class:`MteTriggerSampleType_Enum <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerSampleType_Enum>`
            
            .. attribute:: mtetriggertargettag
            
            	The tag for the target(s) from which to obtain the condition for a trigger check.  A length of 0 indicates the local system.  In this case, access to the objects indicated by mteTriggerValueID is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'.  Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise access rights are checked according to the security  parameters resulting from the tag
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mtetriggertest
            
            	The type of trigger test to perform.  For 'boolean' and 'threshold'  tests, the object at mteTriggerValueID MUST evaluate to an integer, that is, anything that ends up encoded for transmission (that is, in BER, not ASN.1) as an integer.  For 'existence', the specific test is as selected by mteTriggerExistenceTest.  When an object appears, vanishes or changes value, the trigger fires. If the object's appearance caused the trigger firing, the object MUST vanish before the trigger can be fired again for it, and vice versa. If the trigger fired due to a change in the object's value, it will be fired again on every successive value change for that object.  For 'boolean', the specific test is as selected by mteTriggerBooleanTest.  If the test result is true the trigger fires.  The trigger will not fire again until the value has become false and come back to true.  For 'threshold' the test works as described below for  mteTriggerThresholdStartup, mteTriggerThresholdRising, and mteTriggerThresholdFalling.  Note that combining 'boolean' and 'threshold' tests on the same object may be somewhat redundant
            	**type**\: :py:class:`MteTriggerTest_Bits <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerTest_Bits>`
            
            .. attribute:: mtetriggervalueid
            
            	The object identifier of the MIB object to sample to see if the trigger should fire.  This may be wildcarded by truncating all or part of the instance portion, in which case the value is obtained as if with a GetNext function, checking multiple values  if they exist.  If such wildcarding is applied, mteTriggerValueIDWildcard must be 'true' and if not it must be 'false'.  Bad object identifiers or a mismatch between truncating the identifier and the value of mteTriggerValueIDWildcard result in operation as one would expect when providing the wrong identifier to a Get or GetNext operation.  The Get will fail or get the wrong object.  The GetNext will indeed get whatever is next, proceeding until it runs past the initial part of the identifier and perhaps many unintended objects for confusing results.  If the value syntax of those objects is not usable, that results in a 'badType' error that terminates the scan.  Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mtetriggervalueidwildcard
            
            	Control for whether mteTriggerValueID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard
            	**type**\: bool
            
            

            """

            _prefix = 'disman-event'
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
                self.mtetriggertest = DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerTest_Bits()
                self.mtetriggervalueid = None
                self.mtetriggervalueidwildcard = None

            class MteTriggerSampleType_Enum(Enum):
                """
                MteTriggerSampleType_Enum

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

                """

                ABSOLUTEVALUE = 1

                DELTAVALUE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry.MteTriggerSampleType_Enum']


            class MteTriggerTest_Bits(FixedBitsDict):
                """
                MteTriggerTest_Bits

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
                Keys are:- threshold , existence , boolean

                """

                def __init__(self):
                    self._dictionary = { 
                        'threshold':False,
                        'existence':False,
                        'boolean':False,
                    }
                    self._pos_map = { 
                        'threshold':2,
                        'existence':0,
                        'boolean':1,
                    }

            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYDataValidationError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerTable/DISMAN-EVENT-MIB:mteTriggerEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteTriggerTable.MteTriggerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerentry is not None:
                for child_ref in self.mtetriggerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTriggerTable']['meta_info']


    class MteTriggerThresholdTable(object):
        """
        A table of management event trigger information for threshold
        triggers.
        
        .. attribute:: mtetriggerthresholdentry
        
        	Information about a single threshold trigger.  Entries automatically exist in this table for each mteTriggerEntry that has 'threshold' set in mteTriggerTest
        	**type**\: list of :py:class:`MteTriggerThresholdEntry <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry>`
        
        

        """

        _prefix = 'disman-event'
        _revision = '2000-10-16'

        def __init__(self):
            self.parent = None
            self.mtetriggerthresholdentry = YList()
            self.mtetriggerthresholdentry.parent = self
            self.mtetriggerthresholdentry.name = 'mtetriggerthresholdentry'


        class MteTriggerThresholdEntry(object):
            """
            Information about a single threshold trigger.  Entries
            automatically exist in this table for each mteTriggerEntry
            that has 'threshold' set in mteTriggerTest.
            
            .. attribute:: mteowner
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggername
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: mtetriggerthresholddeltafalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is less than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was greater than this threshold, one mteTriggerThresholdDeltaFallingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is less than or equal to this threshold.  After a falling event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltafallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholddeltafallingeventowner
            
            	To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n\-1)) is greater than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n\-1) \- value(n\-2)) was less than this threshold, one mteTriggerThresholdDeltaRisingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) \- value(1), where value(1) is the first sample taken of that instance, is greater than or equal to this threshold.  After a rising event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholddeltarisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaRising. A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholddeltarisingeventowner
            
            	To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdfalling
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, one mteTriggerThresholdFallingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is less than or equal to this threshold and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling'.  After a falling event is generated, another such event is not triggered until the sampled value rises above this threshold and reaches mteTriggerThresholdRising
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdfallingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdFalling.  A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdfallingeventowner
            
            	To go with mteTriggerThresholdFallingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdobjects
            
            	The mteObjectsName of a group of objects from mteObjectsTable.  These objects are to be added to any Notification resulting from the firing of this trigger for this test.  A list of objects may also be added based on the overall  trigger, the event or other settings in mteTriggerTest.  A length of 0 indicates no additional objects
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdobjectsowner
            
            	To go with mteTriggerThresholdObjects, the mteOwner of a group of objects from mteObjectsTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdrising
            
            	A threshold value to check against if mteTriggerType is 'threshold'.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, one mteTriggerThresholdRisingEvent is triggered.  That event is also triggered if the first sample after this entry becomes active is greater than or equal to this threshold and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling'.  After a rising event is generated, another such event is not triggered until the sampled value falls below this threshold and reaches mteTriggerThresholdFalling
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mtetriggerthresholdrisingevent
            
            	The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdRising.  A length of 0 indicates no event
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdrisingeventowner
            
            	To go with mteTriggerThresholdRisingEvent, the mteOwner of an event entry from mteEventTable
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mtetriggerthresholdstartup
            
            	The event that may be triggered when this entry is first set to 'active' and a new instance of the object at mteTriggerValueID is found.  If the first sample after this instance becomes active is greater than or equal to mteTriggerThresholdRising and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance. If the first sample after this entry becomes active is less than or equal to mteTriggerThresholdFalling and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance
            	**type**\: :py:class:`MteTriggerThresholdStartup_Enum <ydk.models.disman.DISMAN_EVENT_MIB.DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry.MteTriggerThresholdStartup_Enum>`
            
            

            """

            _prefix = 'disman-event'
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

            class MteTriggerThresholdStartup_Enum(Enum):
                """
                MteTriggerThresholdStartup_Enum

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

                """

                RISING = 1

                FALLING = 2

                RISINGORFALLING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                    return meta._meta_table['DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry.MteTriggerThresholdStartup_Enum']


            @property
            def _common_path(self):
                if self.mteowner is None:
                    raise YPYDataValidationError('Key property mteowner is None')
                if self.mtetriggername is None:
                    raise YPYDataValidationError('Key property mtetriggername is None')

                return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerThresholdTable/DISMAN-EVENT-MIB:mteTriggerThresholdEntry[DISMAN-EVENT-MIB:mteOwner = ' + str(self.mteowner) + '][DISMAN-EVENT-MIB:mteTriggerName = ' + str(self.mtetriggername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
                return meta._meta_table['DISMANEVENTMIB.MteTriggerThresholdTable.MteTriggerThresholdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/DISMAN-EVENT-MIB:mteTriggerThresholdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mtetriggerthresholdentry is not None:
                for child_ref in self.mtetriggerthresholdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
            return meta._meta_table['DISMANEVENTMIB.MteTriggerThresholdTable']['meta_info']

    @property
    def _common_path(self):

        return '/DISMAN-EVENT-MIB:DISMAN-EVENT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.mteevent is not None and self.mteevent._has_data():
            return True

        if self.mteevent is not None and self.mteevent.is_presence():
            return True

        if self.mteeventnotificationtable is not None and self.mteeventnotificationtable._has_data():
            return True

        if self.mteeventnotificationtable is not None and self.mteeventnotificationtable.is_presence():
            return True

        if self.mteeventsettable is not None and self.mteeventsettable._has_data():
            return True

        if self.mteeventsettable is not None and self.mteeventsettable.is_presence():
            return True

        if self.mteeventtable is not None and self.mteeventtable._has_data():
            return True

        if self.mteeventtable is not None and self.mteeventtable.is_presence():
            return True

        if self.mteobjectstable is not None and self.mteobjectstable._has_data():
            return True

        if self.mteobjectstable is not None and self.mteobjectstable.is_presence():
            return True

        if self.mteresource is not None and self.mteresource._has_data():
            return True

        if self.mteresource is not None and self.mteresource.is_presence():
            return True

        if self.mtetrigger is not None and self.mtetrigger._has_data():
            return True

        if self.mtetrigger is not None and self.mtetrigger.is_presence():
            return True

        if self.mtetriggerbooleantable is not None and self.mtetriggerbooleantable._has_data():
            return True

        if self.mtetriggerbooleantable is not None and self.mtetriggerbooleantable.is_presence():
            return True

        if self.mtetriggerdeltatable is not None and self.mtetriggerdeltatable._has_data():
            return True

        if self.mtetriggerdeltatable is not None and self.mtetriggerdeltatable.is_presence():
            return True

        if self.mtetriggerexistencetable is not None and self.mtetriggerexistencetable._has_data():
            return True

        if self.mtetriggerexistencetable is not None and self.mtetriggerexistencetable.is_presence():
            return True

        if self.mtetriggertable is not None and self.mtetriggertable._has_data():
            return True

        if self.mtetriggertable is not None and self.mtetriggertable.is_presence():
            return True

        if self.mtetriggerthresholdtable is not None and self.mtetriggerthresholdtable._has_data():
            return True

        if self.mtetriggerthresholdtable is not None and self.mtetriggerthresholdtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.disman._meta import _DISMAN_EVENT_MIB as meta
        return meta._meta_table['DISMANEVENTMIB']['meta_info']


