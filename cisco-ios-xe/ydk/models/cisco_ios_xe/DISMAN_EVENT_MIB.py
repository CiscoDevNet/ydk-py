""" DISMAN_EVENT_MIB 

The MIB module for defining event triggers and actions
for network management purposes.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Failurereason(Enum):
    """
    Failurereason

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



class DismanEventMib(Entity):
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
        super(DismanEventMib, self).__init__()
        self._top_entity = None

        self.yang_name = "DISMAN-EVENT-MIB"
        self.yang_parent_name = "DISMAN-EVENT-MIB"

        self.mteevent = DismanEventMib.Mteevent()
        self.mteevent.parent = self
        self._children_name_map["mteevent"] = "mteEvent"
        self._children_yang_names.add("mteEvent")

        self.mteeventnotificationtable = DismanEventMib.Mteeventnotificationtable()
        self.mteeventnotificationtable.parent = self
        self._children_name_map["mteeventnotificationtable"] = "mteEventNotificationTable"
        self._children_yang_names.add("mteEventNotificationTable")

        self.mteeventsettable = DismanEventMib.Mteeventsettable()
        self.mteeventsettable.parent = self
        self._children_name_map["mteeventsettable"] = "mteEventSetTable"
        self._children_yang_names.add("mteEventSetTable")

        self.mteeventtable = DismanEventMib.Mteeventtable()
        self.mteeventtable.parent = self
        self._children_name_map["mteeventtable"] = "mteEventTable"
        self._children_yang_names.add("mteEventTable")

        self.mteobjectstable = DismanEventMib.Mteobjectstable()
        self.mteobjectstable.parent = self
        self._children_name_map["mteobjectstable"] = "mteObjectsTable"
        self._children_yang_names.add("mteObjectsTable")

        self.mteresource = DismanEventMib.Mteresource()
        self.mteresource.parent = self
        self._children_name_map["mteresource"] = "mteResource"
        self._children_yang_names.add("mteResource")

        self.mtetrigger = DismanEventMib.Mtetrigger()
        self.mtetrigger.parent = self
        self._children_name_map["mtetrigger"] = "mteTrigger"
        self._children_yang_names.add("mteTrigger")

        self.mtetriggerbooleantable = DismanEventMib.Mtetriggerbooleantable()
        self.mtetriggerbooleantable.parent = self
        self._children_name_map["mtetriggerbooleantable"] = "mteTriggerBooleanTable"
        self._children_yang_names.add("mteTriggerBooleanTable")

        self.mtetriggerdeltatable = DismanEventMib.Mtetriggerdeltatable()
        self.mtetriggerdeltatable.parent = self
        self._children_name_map["mtetriggerdeltatable"] = "mteTriggerDeltaTable"
        self._children_yang_names.add("mteTriggerDeltaTable")

        self.mtetriggerexistencetable = DismanEventMib.Mtetriggerexistencetable()
        self.mtetriggerexistencetable.parent = self
        self._children_name_map["mtetriggerexistencetable"] = "mteTriggerExistenceTable"
        self._children_yang_names.add("mteTriggerExistenceTable")

        self.mtetriggertable = DismanEventMib.Mtetriggertable()
        self.mtetriggertable.parent = self
        self._children_name_map["mtetriggertable"] = "mteTriggerTable"
        self._children_yang_names.add("mteTriggerTable")

        self.mtetriggerthresholdtable = DismanEventMib.Mtetriggerthresholdtable()
        self.mtetriggerthresholdtable.parent = self
        self._children_name_map["mtetriggerthresholdtable"] = "mteTriggerThresholdTable"
        self._children_yang_names.add("mteTriggerThresholdTable")


    class Mteresource(Entity):
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
            super(DismanEventMib.Mteresource, self).__init__()

            self.yang_name = "mteResource"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteresourcesampleinstancelacks = YLeaf(YType.uint32, "mteResourceSampleInstanceLacks")

            self.mteresourcesampleinstancemaximum = YLeaf(YType.uint32, "mteResourceSampleInstanceMaximum")

            self.mteresourcesampleinstances = YLeaf(YType.uint32, "mteResourceSampleInstances")

            self.mteresourcesampleinstanceshigh = YLeaf(YType.uint32, "mteResourceSampleInstancesHigh")

            self.mteresourcesampleminimum = YLeaf(YType.int32, "mteResourceSampleMinimum")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mteresourcesampleinstancelacks",
                            "mteresourcesampleinstancemaximum",
                            "mteresourcesampleinstances",
                            "mteresourcesampleinstanceshigh",
                            "mteresourcesampleminimum") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DismanEventMib.Mteresource, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteresource, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mteresourcesampleinstancelacks.is_set or
                self.mteresourcesampleinstancemaximum.is_set or
                self.mteresourcesampleinstances.is_set or
                self.mteresourcesampleinstanceshigh.is_set or
                self.mteresourcesampleminimum.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mteresourcesampleinstancelacks.yfilter != YFilter.not_set or
                self.mteresourcesampleinstancemaximum.yfilter != YFilter.not_set or
                self.mteresourcesampleinstances.yfilter != YFilter.not_set or
                self.mteresourcesampleinstanceshigh.yfilter != YFilter.not_set or
                self.mteresourcesampleminimum.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteResource" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mteresourcesampleinstancelacks.is_set or self.mteresourcesampleinstancelacks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteresourcesampleinstancelacks.get_name_leafdata())
            if (self.mteresourcesampleinstancemaximum.is_set or self.mteresourcesampleinstancemaximum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteresourcesampleinstancemaximum.get_name_leafdata())
            if (self.mteresourcesampleinstances.is_set or self.mteresourcesampleinstances.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteresourcesampleinstances.get_name_leafdata())
            if (self.mteresourcesampleinstanceshigh.is_set or self.mteresourcesampleinstanceshigh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteresourcesampleinstanceshigh.get_name_leafdata())
            if (self.mteresourcesampleminimum.is_set or self.mteresourcesampleminimum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteresourcesampleminimum.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteResourceSampleInstanceLacks" or name == "mteResourceSampleInstanceMaximum" or name == "mteResourceSampleInstances" or name == "mteResourceSampleInstancesHigh" or name == "mteResourceSampleMinimum"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mteResourceSampleInstanceLacks"):
                self.mteresourcesampleinstancelacks = value
                self.mteresourcesampleinstancelacks.value_namespace = name_space
                self.mteresourcesampleinstancelacks.value_namespace_prefix = name_space_prefix
            if(value_path == "mteResourceSampleInstanceMaximum"):
                self.mteresourcesampleinstancemaximum = value
                self.mteresourcesampleinstancemaximum.value_namespace = name_space
                self.mteresourcesampleinstancemaximum.value_namespace_prefix = name_space_prefix
            if(value_path == "mteResourceSampleInstances"):
                self.mteresourcesampleinstances = value
                self.mteresourcesampleinstances.value_namespace = name_space
                self.mteresourcesampleinstances.value_namespace_prefix = name_space_prefix
            if(value_path == "mteResourceSampleInstancesHigh"):
                self.mteresourcesampleinstanceshigh = value
                self.mteresourcesampleinstanceshigh.value_namespace = name_space
                self.mteresourcesampleinstanceshigh.value_namespace_prefix = name_space_prefix
            if(value_path == "mteResourceSampleMinimum"):
                self.mteresourcesampleminimum = value
                self.mteresourcesampleminimum.value_namespace = name_space
                self.mteresourcesampleminimum.value_namespace_prefix = name_space_prefix


    class Mtetrigger(Entity):
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
            super(DismanEventMib.Mtetrigger, self).__init__()

            self.yang_name = "mteTrigger"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerfailures = YLeaf(YType.uint32, "mteTriggerFailures")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mtetriggerfailures") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DismanEventMib.Mtetrigger, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetrigger, self).__setattr__(name, value)

        def has_data(self):
            return self.mtetriggerfailures.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mtetriggerfailures.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTrigger" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mtetriggerfailures.is_set or self.mtetriggerfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mtetriggerfailures.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerFailures"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mteTriggerFailures"):
                self.mtetriggerfailures = value
                self.mtetriggerfailures.value_namespace = name_space
                self.mtetriggerfailures.value_namespace_prefix = name_space_prefix


    class Mteevent(Entity):
        """
        
        
        .. attribute:: mteeventfailures
        
        	The number of times an attempt to invoke an event has failed.  This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DismanEventMib.Mteevent, self).__init__()

            self.yang_name = "mteEvent"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteeventfailures = YLeaf(YType.uint32, "mteEventFailures")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mteeventfailures") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DismanEventMib.Mteevent, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteevent, self).__setattr__(name, value)

        def has_data(self):
            return self.mteeventfailures.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mteeventfailures.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteEvent" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mteeventfailures.is_set or self.mteeventfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mteeventfailures.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteEventFailures"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mteEventFailures"):
                self.mteeventfailures = value
                self.mteeventfailures.value_namespace = name_space
                self.mteeventfailures.value_namespace_prefix = name_space_prefix


    class Mtetriggertable(Entity):
        """
        A table of management event trigger information.
        
        .. attribute:: mtetriggerentry
        
        	Information about a single trigger.  Applications create and delete entries using mteTriggerEntryStatus
        	**type**\: list of    :py:class:`Mtetriggerentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DismanEventMib.Mtetriggertable, self).__init__()

            self.yang_name = "mteTriggerTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerentry = YList(self)

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
                        super(DismanEventMib.Mtetriggertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetriggertable, self).__setattr__(name, value)


        class Mtetriggerentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
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
            	**type**\:   :py:class:`Mtetriggersampletype <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggertable.Mtetriggerentry.Mtetriggersampletype>`
            
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
                super(DismanEventMib.Mtetriggertable.Mtetriggerentry, self).__init__()

                self.yang_name = "mteTriggerEntry"
                self.yang_parent_name = "mteTriggerTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mtetriggername = YLeaf(YType.str, "mteTriggerName")

                self.mtetriggercomment = YLeaf(YType.str, "mteTriggerComment")

                self.mtetriggercontextname = YLeaf(YType.str, "mteTriggerContextName")

                self.mtetriggercontextnamewildcard = YLeaf(YType.boolean, "mteTriggerContextNameWildcard")

                self.mtetriggerenabled = YLeaf(YType.boolean, "mteTriggerEnabled")

                self.mtetriggerentrystatus = YLeaf(YType.enumeration, "mteTriggerEntryStatus")

                self.mtetriggerfrequency = YLeaf(YType.uint32, "mteTriggerFrequency")

                self.mtetriggerobjects = YLeaf(YType.str, "mteTriggerObjects")

                self.mtetriggerobjectsowner = YLeaf(YType.str, "mteTriggerObjectsOwner")

                self.mtetriggersampletype = YLeaf(YType.enumeration, "mteTriggerSampleType")

                self.mtetriggertargettag = YLeaf(YType.str, "mteTriggerTargetTag")

                self.mtetriggertest = YLeaf(YType.bits, "mteTriggerTest")

                self.mtetriggervalueid = YLeaf(YType.str, "mteTriggerValueID")

                self.mtetriggervalueidwildcard = YLeaf(YType.boolean, "mteTriggerValueIDWildcard")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mtetriggername",
                                "mtetriggercomment",
                                "mtetriggercontextname",
                                "mtetriggercontextnamewildcard",
                                "mtetriggerenabled",
                                "mtetriggerentrystatus",
                                "mtetriggerfrequency",
                                "mtetriggerobjects",
                                "mtetriggerobjectsowner",
                                "mtetriggersampletype",
                                "mtetriggertargettag",
                                "mtetriggertest",
                                "mtetriggervalueid",
                                "mtetriggervalueidwildcard") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mtetriggertable.Mtetriggerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mtetriggertable.Mtetriggerentry, self).__setattr__(name, value)

            class Mtetriggersampletype(Enum):
                """
                Mtetriggersampletype

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


            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mtetriggername.is_set or
                    self.mtetriggercomment.is_set or
                    self.mtetriggercontextname.is_set or
                    self.mtetriggercontextnamewildcard.is_set or
                    self.mtetriggerenabled.is_set or
                    self.mtetriggerentrystatus.is_set or
                    self.mtetriggerfrequency.is_set or
                    self.mtetriggerobjects.is_set or
                    self.mtetriggerobjectsowner.is_set or
                    self.mtetriggersampletype.is_set or
                    self.mtetriggertargettag.is_set or
                    self.mtetriggertest.is_set or
                    self.mtetriggervalueid.is_set or
                    self.mtetriggervalueidwildcard.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mtetriggername.yfilter != YFilter.not_set or
                    self.mtetriggercomment.yfilter != YFilter.not_set or
                    self.mtetriggercontextname.yfilter != YFilter.not_set or
                    self.mtetriggercontextnamewildcard.yfilter != YFilter.not_set or
                    self.mtetriggerenabled.yfilter != YFilter.not_set or
                    self.mtetriggerentrystatus.yfilter != YFilter.not_set or
                    self.mtetriggerfrequency.yfilter != YFilter.not_set or
                    self.mtetriggerobjects.yfilter != YFilter.not_set or
                    self.mtetriggerobjectsowner.yfilter != YFilter.not_set or
                    self.mtetriggersampletype.yfilter != YFilter.not_set or
                    self.mtetriggertargettag.yfilter != YFilter.not_set or
                    self.mtetriggertest.yfilter != YFilter.not_set or
                    self.mtetriggervalueid.yfilter != YFilter.not_set or
                    self.mtetriggervalueidwildcard.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteTriggerEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteTriggerName='" + self.mtetriggername.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mtetriggername.is_set or self.mtetriggername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggername.get_name_leafdata())
                if (self.mtetriggercomment.is_set or self.mtetriggercomment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggercomment.get_name_leafdata())
                if (self.mtetriggercontextname.is_set or self.mtetriggercontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggercontextname.get_name_leafdata())
                if (self.mtetriggercontextnamewildcard.is_set or self.mtetriggercontextnamewildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggercontextnamewildcard.get_name_leafdata())
                if (self.mtetriggerenabled.is_set or self.mtetriggerenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerenabled.get_name_leafdata())
                if (self.mtetriggerentrystatus.is_set or self.mtetriggerentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerentrystatus.get_name_leafdata())
                if (self.mtetriggerfrequency.is_set or self.mtetriggerfrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerfrequency.get_name_leafdata())
                if (self.mtetriggerobjects.is_set or self.mtetriggerobjects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerobjects.get_name_leafdata())
                if (self.mtetriggerobjectsowner.is_set or self.mtetriggerobjectsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerobjectsowner.get_name_leafdata())
                if (self.mtetriggersampletype.is_set or self.mtetriggersampletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggersampletype.get_name_leafdata())
                if (self.mtetriggertargettag.is_set or self.mtetriggertargettag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggertargettag.get_name_leafdata())
                if (self.mtetriggertest.is_set or self.mtetriggertest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggertest.get_name_leafdata())
                if (self.mtetriggervalueid.is_set or self.mtetriggervalueid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggervalueid.get_name_leafdata())
                if (self.mtetriggervalueidwildcard.is_set or self.mtetriggervalueidwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggervalueidwildcard.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteTriggerName" or name == "mteTriggerComment" or name == "mteTriggerContextName" or name == "mteTriggerContextNameWildcard" or name == "mteTriggerEnabled" or name == "mteTriggerEntryStatus" or name == "mteTriggerFrequency" or name == "mteTriggerObjects" or name == "mteTriggerObjectsOwner" or name == "mteTriggerSampleType" or name == "mteTriggerTargetTag" or name == "mteTriggerTest" or name == "mteTriggerValueID" or name == "mteTriggerValueIDWildcard"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerName"):
                    self.mtetriggername = value
                    self.mtetriggername.value_namespace = name_space
                    self.mtetriggername.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerComment"):
                    self.mtetriggercomment = value
                    self.mtetriggercomment.value_namespace = name_space
                    self.mtetriggercomment.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerContextName"):
                    self.mtetriggercontextname = value
                    self.mtetriggercontextname.value_namespace = name_space
                    self.mtetriggercontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerContextNameWildcard"):
                    self.mtetriggercontextnamewildcard = value
                    self.mtetriggercontextnamewildcard.value_namespace = name_space
                    self.mtetriggercontextnamewildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerEnabled"):
                    self.mtetriggerenabled = value
                    self.mtetriggerenabled.value_namespace = name_space
                    self.mtetriggerenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerEntryStatus"):
                    self.mtetriggerentrystatus = value
                    self.mtetriggerentrystatus.value_namespace = name_space
                    self.mtetriggerentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerFrequency"):
                    self.mtetriggerfrequency = value
                    self.mtetriggerfrequency.value_namespace = name_space
                    self.mtetriggerfrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerObjects"):
                    self.mtetriggerobjects = value
                    self.mtetriggerobjects.value_namespace = name_space
                    self.mtetriggerobjects.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerObjectsOwner"):
                    self.mtetriggerobjectsowner = value
                    self.mtetriggerobjectsowner.value_namespace = name_space
                    self.mtetriggerobjectsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerSampleType"):
                    self.mtetriggersampletype = value
                    self.mtetriggersampletype.value_namespace = name_space
                    self.mtetriggersampletype.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerTargetTag"):
                    self.mtetriggertargettag = value
                    self.mtetriggertargettag.value_namespace = name_space
                    self.mtetriggertargettag.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerTest"):
                    self.mtetriggertest[value] = True
                if(value_path == "mteTriggerValueID"):
                    self.mtetriggervalueid = value
                    self.mtetriggervalueid.value_namespace = name_space
                    self.mtetriggervalueid.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerValueIDWildcard"):
                    self.mtetriggervalueidwildcard = value
                    self.mtetriggervalueidwildcard.value_namespace = name_space
                    self.mtetriggervalueidwildcard.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mtetriggerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mtetriggerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTriggerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteTriggerEntry"):
                for c in self.mtetriggerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mtetriggertable.Mtetriggerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mtetriggerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mtetriggerdeltatable(Entity):
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
            super(DismanEventMib.Mtetriggerdeltatable, self).__init__()

            self.yang_name = "mteTriggerDeltaTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerdeltaentry = YList(self)

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
                        super(DismanEventMib.Mtetriggerdeltatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetriggerdeltatable, self).__setattr__(name, value)


        class Mtetriggerdeltaentry(Entity):
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
            	**type**\:   :py:class:`Mtetriggerdeltadiscontinuityidtype <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry.Mtetriggerdeltadiscontinuityidtype>`
            
            .. attribute:: mtetriggerdeltadiscontinuityidwildcard
            
            	Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully\-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding  mteTriggerSampleType is 'deltaValue'
            	**type**\:  bool
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry, self).__init__()

                self.yang_name = "mteTriggerDeltaEntry"
                self.yang_parent_name = "mteTriggerDeltaTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mtetriggername = YLeaf(YType.str, "mteTriggerName")

                self.mtetriggerdeltadiscontinuityid = YLeaf(YType.str, "mteTriggerDeltaDiscontinuityID")

                self.mtetriggerdeltadiscontinuityidtype = YLeaf(YType.enumeration, "mteTriggerDeltaDiscontinuityIDType")

                self.mtetriggerdeltadiscontinuityidwildcard = YLeaf(YType.boolean, "mteTriggerDeltaDiscontinuityIDWildcard")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mtetriggername",
                                "mtetriggerdeltadiscontinuityid",
                                "mtetriggerdeltadiscontinuityidtype",
                                "mtetriggerdeltadiscontinuityidwildcard") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry, self).__setattr__(name, value)

            class Mtetriggerdeltadiscontinuityidtype(Enum):
                """
                Mtetriggerdeltadiscontinuityidtype

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


            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mtetriggername.is_set or
                    self.mtetriggerdeltadiscontinuityid.is_set or
                    self.mtetriggerdeltadiscontinuityidtype.is_set or
                    self.mtetriggerdeltadiscontinuityidwildcard.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mtetriggername.yfilter != YFilter.not_set or
                    self.mtetriggerdeltadiscontinuityid.yfilter != YFilter.not_set or
                    self.mtetriggerdeltadiscontinuityidtype.yfilter != YFilter.not_set or
                    self.mtetriggerdeltadiscontinuityidwildcard.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteTriggerDeltaEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteTriggerName='" + self.mtetriggername.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerDeltaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mtetriggername.is_set or self.mtetriggername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggername.get_name_leafdata())
                if (self.mtetriggerdeltadiscontinuityid.is_set or self.mtetriggerdeltadiscontinuityid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerdeltadiscontinuityid.get_name_leafdata())
                if (self.mtetriggerdeltadiscontinuityidtype.is_set or self.mtetriggerdeltadiscontinuityidtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerdeltadiscontinuityidtype.get_name_leafdata())
                if (self.mtetriggerdeltadiscontinuityidwildcard.is_set or self.mtetriggerdeltadiscontinuityidwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerdeltadiscontinuityidwildcard.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteTriggerName" or name == "mteTriggerDeltaDiscontinuityID" or name == "mteTriggerDeltaDiscontinuityIDType" or name == "mteTriggerDeltaDiscontinuityIDWildcard"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerName"):
                    self.mtetriggername = value
                    self.mtetriggername.value_namespace = name_space
                    self.mtetriggername.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerDeltaDiscontinuityID"):
                    self.mtetriggerdeltadiscontinuityid = value
                    self.mtetriggerdeltadiscontinuityid.value_namespace = name_space
                    self.mtetriggerdeltadiscontinuityid.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerDeltaDiscontinuityIDType"):
                    self.mtetriggerdeltadiscontinuityidtype = value
                    self.mtetriggerdeltadiscontinuityidtype.value_namespace = name_space
                    self.mtetriggerdeltadiscontinuityidtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerDeltaDiscontinuityIDWildcard"):
                    self.mtetriggerdeltadiscontinuityidwildcard = value
                    self.mtetriggerdeltadiscontinuityidwildcard.value_namespace = name_space
                    self.mtetriggerdeltadiscontinuityidwildcard.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mtetriggerdeltaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mtetriggerdeltaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTriggerDeltaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteTriggerDeltaEntry"):
                for c in self.mtetriggerdeltaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mtetriggerdeltatable.Mtetriggerdeltaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mtetriggerdeltaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerDeltaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mtetriggerexistencetable(Entity):
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
            super(DismanEventMib.Mtetriggerexistencetable, self).__init__()

            self.yang_name = "mteTriggerExistenceTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerexistenceentry = YList(self)

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
                        super(DismanEventMib.Mtetriggerexistencetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetriggerexistencetable, self).__setattr__(name, value)


        class Mtetriggerexistenceentry(Entity):
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
                super(DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry, self).__init__()

                self.yang_name = "mteTriggerExistenceEntry"
                self.yang_parent_name = "mteTriggerExistenceTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mtetriggername = YLeaf(YType.str, "mteTriggerName")

                self.mtetriggerexistenceevent = YLeaf(YType.str, "mteTriggerExistenceEvent")

                self.mtetriggerexistenceeventowner = YLeaf(YType.str, "mteTriggerExistenceEventOwner")

                self.mtetriggerexistenceobjects = YLeaf(YType.str, "mteTriggerExistenceObjects")

                self.mtetriggerexistenceobjectsowner = YLeaf(YType.str, "mteTriggerExistenceObjectsOwner")

                self.mtetriggerexistencestartup = YLeaf(YType.bits, "mteTriggerExistenceStartup")

                self.mtetriggerexistencetest = YLeaf(YType.bits, "mteTriggerExistenceTest")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mtetriggername",
                                "mtetriggerexistenceevent",
                                "mtetriggerexistenceeventowner",
                                "mtetriggerexistenceobjects",
                                "mtetriggerexistenceobjectsowner",
                                "mtetriggerexistencestartup",
                                "mtetriggerexistencetest") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mtetriggername.is_set or
                    self.mtetriggerexistenceevent.is_set or
                    self.mtetriggerexistenceeventowner.is_set or
                    self.mtetriggerexistenceobjects.is_set or
                    self.mtetriggerexistenceobjectsowner.is_set or
                    self.mtetriggerexistencestartup.is_set or
                    self.mtetriggerexistencetest.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mtetriggername.yfilter != YFilter.not_set or
                    self.mtetriggerexistenceevent.yfilter != YFilter.not_set or
                    self.mtetriggerexistenceeventowner.yfilter != YFilter.not_set or
                    self.mtetriggerexistenceobjects.yfilter != YFilter.not_set or
                    self.mtetriggerexistenceobjectsowner.yfilter != YFilter.not_set or
                    self.mtetriggerexistencestartup.yfilter != YFilter.not_set or
                    self.mtetriggerexistencetest.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteTriggerExistenceEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteTriggerName='" + self.mtetriggername.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerExistenceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mtetriggername.is_set or self.mtetriggername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggername.get_name_leafdata())
                if (self.mtetriggerexistenceevent.is_set or self.mtetriggerexistenceevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistenceevent.get_name_leafdata())
                if (self.mtetriggerexistenceeventowner.is_set or self.mtetriggerexistenceeventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistenceeventowner.get_name_leafdata())
                if (self.mtetriggerexistenceobjects.is_set or self.mtetriggerexistenceobjects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistenceobjects.get_name_leafdata())
                if (self.mtetriggerexistenceobjectsowner.is_set or self.mtetriggerexistenceobjectsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistenceobjectsowner.get_name_leafdata())
                if (self.mtetriggerexistencestartup.is_set or self.mtetriggerexistencestartup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistencestartup.get_name_leafdata())
                if (self.mtetriggerexistencetest.is_set or self.mtetriggerexistencetest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerexistencetest.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteTriggerName" or name == "mteTriggerExistenceEvent" or name == "mteTriggerExistenceEventOwner" or name == "mteTriggerExistenceObjects" or name == "mteTriggerExistenceObjectsOwner" or name == "mteTriggerExistenceStartup" or name == "mteTriggerExistenceTest"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerName"):
                    self.mtetriggername = value
                    self.mtetriggername.value_namespace = name_space
                    self.mtetriggername.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerExistenceEvent"):
                    self.mtetriggerexistenceevent = value
                    self.mtetriggerexistenceevent.value_namespace = name_space
                    self.mtetriggerexistenceevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerExistenceEventOwner"):
                    self.mtetriggerexistenceeventowner = value
                    self.mtetriggerexistenceeventowner.value_namespace = name_space
                    self.mtetriggerexistenceeventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerExistenceObjects"):
                    self.mtetriggerexistenceobjects = value
                    self.mtetriggerexistenceobjects.value_namespace = name_space
                    self.mtetriggerexistenceobjects.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerExistenceObjectsOwner"):
                    self.mtetriggerexistenceobjectsowner = value
                    self.mtetriggerexistenceobjectsowner.value_namespace = name_space
                    self.mtetriggerexistenceobjectsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerExistenceStartup"):
                    self.mtetriggerexistencestartup[value] = True
                if(value_path == "mteTriggerExistenceTest"):
                    self.mtetriggerexistencetest[value] = True

        def has_data(self):
            for c in self.mtetriggerexistenceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mtetriggerexistenceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTriggerExistenceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteTriggerExistenceEntry"):
                for c in self.mtetriggerexistenceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mtetriggerexistencetable.Mtetriggerexistenceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mtetriggerexistenceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerExistenceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mtetriggerbooleantable(Entity):
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
            super(DismanEventMib.Mtetriggerbooleantable, self).__init__()

            self.yang_name = "mteTriggerBooleanTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerbooleanentry = YList(self)

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
                        super(DismanEventMib.Mtetriggerbooleantable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetriggerbooleantable, self).__setattr__(name, value)


        class Mtetriggerbooleanentry(Entity):
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
            	**type**\:   :py:class:`Mtetriggerbooleancomparison <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry.Mtetriggerbooleancomparison>`
            
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
                super(DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry, self).__init__()

                self.yang_name = "mteTriggerBooleanEntry"
                self.yang_parent_name = "mteTriggerBooleanTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mtetriggername = YLeaf(YType.str, "mteTriggerName")

                self.mtetriggerbooleancomparison = YLeaf(YType.enumeration, "mteTriggerBooleanComparison")

                self.mtetriggerbooleanevent = YLeaf(YType.str, "mteTriggerBooleanEvent")

                self.mtetriggerbooleaneventowner = YLeaf(YType.str, "mteTriggerBooleanEventOwner")

                self.mtetriggerbooleanobjects = YLeaf(YType.str, "mteTriggerBooleanObjects")

                self.mtetriggerbooleanobjectsowner = YLeaf(YType.str, "mteTriggerBooleanObjectsOwner")

                self.mtetriggerbooleanstartup = YLeaf(YType.boolean, "mteTriggerBooleanStartup")

                self.mtetriggerbooleanvalue = YLeaf(YType.int32, "mteTriggerBooleanValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mtetriggername",
                                "mtetriggerbooleancomparison",
                                "mtetriggerbooleanevent",
                                "mtetriggerbooleaneventowner",
                                "mtetriggerbooleanobjects",
                                "mtetriggerbooleanobjectsowner",
                                "mtetriggerbooleanstartup",
                                "mtetriggerbooleanvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry, self).__setattr__(name, value)

            class Mtetriggerbooleancomparison(Enum):
                """
                Mtetriggerbooleancomparison

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


            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mtetriggername.is_set or
                    self.mtetriggerbooleancomparison.is_set or
                    self.mtetriggerbooleanevent.is_set or
                    self.mtetriggerbooleaneventowner.is_set or
                    self.mtetriggerbooleanobjects.is_set or
                    self.mtetriggerbooleanobjectsowner.is_set or
                    self.mtetriggerbooleanstartup.is_set or
                    self.mtetriggerbooleanvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mtetriggername.yfilter != YFilter.not_set or
                    self.mtetriggerbooleancomparison.yfilter != YFilter.not_set or
                    self.mtetriggerbooleanevent.yfilter != YFilter.not_set or
                    self.mtetriggerbooleaneventowner.yfilter != YFilter.not_set or
                    self.mtetriggerbooleanobjects.yfilter != YFilter.not_set or
                    self.mtetriggerbooleanobjectsowner.yfilter != YFilter.not_set or
                    self.mtetriggerbooleanstartup.yfilter != YFilter.not_set or
                    self.mtetriggerbooleanvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteTriggerBooleanEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteTriggerName='" + self.mtetriggername.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerBooleanTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mtetriggername.is_set or self.mtetriggername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggername.get_name_leafdata())
                if (self.mtetriggerbooleancomparison.is_set or self.mtetriggerbooleancomparison.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleancomparison.get_name_leafdata())
                if (self.mtetriggerbooleanevent.is_set or self.mtetriggerbooleanevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleanevent.get_name_leafdata())
                if (self.mtetriggerbooleaneventowner.is_set or self.mtetriggerbooleaneventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleaneventowner.get_name_leafdata())
                if (self.mtetriggerbooleanobjects.is_set or self.mtetriggerbooleanobjects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleanobjects.get_name_leafdata())
                if (self.mtetriggerbooleanobjectsowner.is_set or self.mtetriggerbooleanobjectsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleanobjectsowner.get_name_leafdata())
                if (self.mtetriggerbooleanstartup.is_set or self.mtetriggerbooleanstartup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleanstartup.get_name_leafdata())
                if (self.mtetriggerbooleanvalue.is_set or self.mtetriggerbooleanvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerbooleanvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteTriggerName" or name == "mteTriggerBooleanComparison" or name == "mteTriggerBooleanEvent" or name == "mteTriggerBooleanEventOwner" or name == "mteTriggerBooleanObjects" or name == "mteTriggerBooleanObjectsOwner" or name == "mteTriggerBooleanStartup" or name == "mteTriggerBooleanValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerName"):
                    self.mtetriggername = value
                    self.mtetriggername.value_namespace = name_space
                    self.mtetriggername.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanComparison"):
                    self.mtetriggerbooleancomparison = value
                    self.mtetriggerbooleancomparison.value_namespace = name_space
                    self.mtetriggerbooleancomparison.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanEvent"):
                    self.mtetriggerbooleanevent = value
                    self.mtetriggerbooleanevent.value_namespace = name_space
                    self.mtetriggerbooleanevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanEventOwner"):
                    self.mtetriggerbooleaneventowner = value
                    self.mtetriggerbooleaneventowner.value_namespace = name_space
                    self.mtetriggerbooleaneventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanObjects"):
                    self.mtetriggerbooleanobjects = value
                    self.mtetriggerbooleanobjects.value_namespace = name_space
                    self.mtetriggerbooleanobjects.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanObjectsOwner"):
                    self.mtetriggerbooleanobjectsowner = value
                    self.mtetriggerbooleanobjectsowner.value_namespace = name_space
                    self.mtetriggerbooleanobjectsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanStartup"):
                    self.mtetriggerbooleanstartup = value
                    self.mtetriggerbooleanstartup.value_namespace = name_space
                    self.mtetriggerbooleanstartup.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerBooleanValue"):
                    self.mtetriggerbooleanvalue = value
                    self.mtetriggerbooleanvalue.value_namespace = name_space
                    self.mtetriggerbooleanvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mtetriggerbooleanentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mtetriggerbooleanentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTriggerBooleanTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteTriggerBooleanEntry"):
                for c in self.mtetriggerbooleanentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mtetriggerbooleantable.Mtetriggerbooleanentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mtetriggerbooleanentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerBooleanEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mtetriggerthresholdtable(Entity):
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
            super(DismanEventMib.Mtetriggerthresholdtable, self).__init__()

            self.yang_name = "mteTriggerThresholdTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mtetriggerthresholdentry = YList(self)

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
                        super(DismanEventMib.Mtetriggerthresholdtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mtetriggerthresholdtable, self).__setattr__(name, value)


        class Mtetriggerthresholdentry(Entity):
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
            	**type**\:   :py:class:`Mtetriggerthresholdstartup <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry.Mtetriggerthresholdstartup>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry, self).__init__()

                self.yang_name = "mteTriggerThresholdEntry"
                self.yang_parent_name = "mteTriggerThresholdTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mtetriggername = YLeaf(YType.str, "mteTriggerName")

                self.mtetriggerthresholddeltafalling = YLeaf(YType.int32, "mteTriggerThresholdDeltaFalling")

                self.mtetriggerthresholddeltafallingevent = YLeaf(YType.str, "mteTriggerThresholdDeltaFallingEvent")

                self.mtetriggerthresholddeltafallingeventowner = YLeaf(YType.str, "mteTriggerThresholdDeltaFallingEventOwner")

                self.mtetriggerthresholddeltarising = YLeaf(YType.int32, "mteTriggerThresholdDeltaRising")

                self.mtetriggerthresholddeltarisingevent = YLeaf(YType.str, "mteTriggerThresholdDeltaRisingEvent")

                self.mtetriggerthresholddeltarisingeventowner = YLeaf(YType.str, "mteTriggerThresholdDeltaRisingEventOwner")

                self.mtetriggerthresholdfalling = YLeaf(YType.int32, "mteTriggerThresholdFalling")

                self.mtetriggerthresholdfallingevent = YLeaf(YType.str, "mteTriggerThresholdFallingEvent")

                self.mtetriggerthresholdfallingeventowner = YLeaf(YType.str, "mteTriggerThresholdFallingEventOwner")

                self.mtetriggerthresholdobjects = YLeaf(YType.str, "mteTriggerThresholdObjects")

                self.mtetriggerthresholdobjectsowner = YLeaf(YType.str, "mteTriggerThresholdObjectsOwner")

                self.mtetriggerthresholdrising = YLeaf(YType.int32, "mteTriggerThresholdRising")

                self.mtetriggerthresholdrisingevent = YLeaf(YType.str, "mteTriggerThresholdRisingEvent")

                self.mtetriggerthresholdrisingeventowner = YLeaf(YType.str, "mteTriggerThresholdRisingEventOwner")

                self.mtetriggerthresholdstartup = YLeaf(YType.enumeration, "mteTriggerThresholdStartup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mtetriggername",
                                "mtetriggerthresholddeltafalling",
                                "mtetriggerthresholddeltafallingevent",
                                "mtetriggerthresholddeltafallingeventowner",
                                "mtetriggerthresholddeltarising",
                                "mtetriggerthresholddeltarisingevent",
                                "mtetriggerthresholddeltarisingeventowner",
                                "mtetriggerthresholdfalling",
                                "mtetriggerthresholdfallingevent",
                                "mtetriggerthresholdfallingeventowner",
                                "mtetriggerthresholdobjects",
                                "mtetriggerthresholdobjectsowner",
                                "mtetriggerthresholdrising",
                                "mtetriggerthresholdrisingevent",
                                "mtetriggerthresholdrisingeventowner",
                                "mtetriggerthresholdstartup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry, self).__setattr__(name, value)

            class Mtetriggerthresholdstartup(Enum):
                """
                Mtetriggerthresholdstartup

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


            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mtetriggername.is_set or
                    self.mtetriggerthresholddeltafalling.is_set or
                    self.mtetriggerthresholddeltafallingevent.is_set or
                    self.mtetriggerthresholddeltafallingeventowner.is_set or
                    self.mtetriggerthresholddeltarising.is_set or
                    self.mtetriggerthresholddeltarisingevent.is_set or
                    self.mtetriggerthresholddeltarisingeventowner.is_set or
                    self.mtetriggerthresholdfalling.is_set or
                    self.mtetriggerthresholdfallingevent.is_set or
                    self.mtetriggerthresholdfallingeventowner.is_set or
                    self.mtetriggerthresholdobjects.is_set or
                    self.mtetriggerthresholdobjectsowner.is_set or
                    self.mtetriggerthresholdrising.is_set or
                    self.mtetriggerthresholdrisingevent.is_set or
                    self.mtetriggerthresholdrisingeventowner.is_set or
                    self.mtetriggerthresholdstartup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mtetriggername.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltafalling.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltafallingevent.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltafallingeventowner.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltarising.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltarisingevent.yfilter != YFilter.not_set or
                    self.mtetriggerthresholddeltarisingeventowner.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdfalling.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdfallingevent.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdfallingeventowner.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdobjects.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdobjectsowner.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdrising.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdrisingevent.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdrisingeventowner.yfilter != YFilter.not_set or
                    self.mtetriggerthresholdstartup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteTriggerThresholdEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteTriggerName='" + self.mtetriggername.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteTriggerThresholdTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mtetriggername.is_set or self.mtetriggername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggername.get_name_leafdata())
                if (self.mtetriggerthresholddeltafalling.is_set or self.mtetriggerthresholddeltafalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltafalling.get_name_leafdata())
                if (self.mtetriggerthresholddeltafallingevent.is_set or self.mtetriggerthresholddeltafallingevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltafallingevent.get_name_leafdata())
                if (self.mtetriggerthresholddeltafallingeventowner.is_set or self.mtetriggerthresholddeltafallingeventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltafallingeventowner.get_name_leafdata())
                if (self.mtetriggerthresholddeltarising.is_set or self.mtetriggerthresholddeltarising.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltarising.get_name_leafdata())
                if (self.mtetriggerthresholddeltarisingevent.is_set or self.mtetriggerthresholddeltarisingevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltarisingevent.get_name_leafdata())
                if (self.mtetriggerthresholddeltarisingeventowner.is_set or self.mtetriggerthresholddeltarisingeventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholddeltarisingeventowner.get_name_leafdata())
                if (self.mtetriggerthresholdfalling.is_set or self.mtetriggerthresholdfalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdfalling.get_name_leafdata())
                if (self.mtetriggerthresholdfallingevent.is_set or self.mtetriggerthresholdfallingevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdfallingevent.get_name_leafdata())
                if (self.mtetriggerthresholdfallingeventowner.is_set or self.mtetriggerthresholdfallingeventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdfallingeventowner.get_name_leafdata())
                if (self.mtetriggerthresholdobjects.is_set or self.mtetriggerthresholdobjects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdobjects.get_name_leafdata())
                if (self.mtetriggerthresholdobjectsowner.is_set or self.mtetriggerthresholdobjectsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdobjectsowner.get_name_leafdata())
                if (self.mtetriggerthresholdrising.is_set or self.mtetriggerthresholdrising.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdrising.get_name_leafdata())
                if (self.mtetriggerthresholdrisingevent.is_set or self.mtetriggerthresholdrisingevent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdrisingevent.get_name_leafdata())
                if (self.mtetriggerthresholdrisingeventowner.is_set or self.mtetriggerthresholdrisingeventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdrisingeventowner.get_name_leafdata())
                if (self.mtetriggerthresholdstartup.is_set or self.mtetriggerthresholdstartup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtetriggerthresholdstartup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteTriggerName" or name == "mteTriggerThresholdDeltaFalling" or name == "mteTriggerThresholdDeltaFallingEvent" or name == "mteTriggerThresholdDeltaFallingEventOwner" or name == "mteTriggerThresholdDeltaRising" or name == "mteTriggerThresholdDeltaRisingEvent" or name == "mteTriggerThresholdDeltaRisingEventOwner" or name == "mteTriggerThresholdFalling" or name == "mteTriggerThresholdFallingEvent" or name == "mteTriggerThresholdFallingEventOwner" or name == "mteTriggerThresholdObjects" or name == "mteTriggerThresholdObjectsOwner" or name == "mteTriggerThresholdRising" or name == "mteTriggerThresholdRisingEvent" or name == "mteTriggerThresholdRisingEventOwner" or name == "mteTriggerThresholdStartup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerName"):
                    self.mtetriggername = value
                    self.mtetriggername.value_namespace = name_space
                    self.mtetriggername.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaFalling"):
                    self.mtetriggerthresholddeltafalling = value
                    self.mtetriggerthresholddeltafalling.value_namespace = name_space
                    self.mtetriggerthresholddeltafalling.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaFallingEvent"):
                    self.mtetriggerthresholddeltafallingevent = value
                    self.mtetriggerthresholddeltafallingevent.value_namespace = name_space
                    self.mtetriggerthresholddeltafallingevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaFallingEventOwner"):
                    self.mtetriggerthresholddeltafallingeventowner = value
                    self.mtetriggerthresholddeltafallingeventowner.value_namespace = name_space
                    self.mtetriggerthresholddeltafallingeventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaRising"):
                    self.mtetriggerthresholddeltarising = value
                    self.mtetriggerthresholddeltarising.value_namespace = name_space
                    self.mtetriggerthresholddeltarising.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaRisingEvent"):
                    self.mtetriggerthresholddeltarisingevent = value
                    self.mtetriggerthresholddeltarisingevent.value_namespace = name_space
                    self.mtetriggerthresholddeltarisingevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdDeltaRisingEventOwner"):
                    self.mtetriggerthresholddeltarisingeventowner = value
                    self.mtetriggerthresholddeltarisingeventowner.value_namespace = name_space
                    self.mtetriggerthresholddeltarisingeventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdFalling"):
                    self.mtetriggerthresholdfalling = value
                    self.mtetriggerthresholdfalling.value_namespace = name_space
                    self.mtetriggerthresholdfalling.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdFallingEvent"):
                    self.mtetriggerthresholdfallingevent = value
                    self.mtetriggerthresholdfallingevent.value_namespace = name_space
                    self.mtetriggerthresholdfallingevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdFallingEventOwner"):
                    self.mtetriggerthresholdfallingeventowner = value
                    self.mtetriggerthresholdfallingeventowner.value_namespace = name_space
                    self.mtetriggerthresholdfallingeventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdObjects"):
                    self.mtetriggerthresholdobjects = value
                    self.mtetriggerthresholdobjects.value_namespace = name_space
                    self.mtetriggerthresholdobjects.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdObjectsOwner"):
                    self.mtetriggerthresholdobjectsowner = value
                    self.mtetriggerthresholdobjectsowner.value_namespace = name_space
                    self.mtetriggerthresholdobjectsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdRising"):
                    self.mtetriggerthresholdrising = value
                    self.mtetriggerthresholdrising.value_namespace = name_space
                    self.mtetriggerthresholdrising.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdRisingEvent"):
                    self.mtetriggerthresholdrisingevent = value
                    self.mtetriggerthresholdrisingevent.value_namespace = name_space
                    self.mtetriggerthresholdrisingevent.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdRisingEventOwner"):
                    self.mtetriggerthresholdrisingeventowner = value
                    self.mtetriggerthresholdrisingeventowner.value_namespace = name_space
                    self.mtetriggerthresholdrisingeventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteTriggerThresholdStartup"):
                    self.mtetriggerthresholdstartup = value
                    self.mtetriggerthresholdstartup.value_namespace = name_space
                    self.mtetriggerthresholdstartup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mtetriggerthresholdentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mtetriggerthresholdentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteTriggerThresholdTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteTriggerThresholdEntry"):
                for c in self.mtetriggerthresholdentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mtetriggerthresholdtable.Mtetriggerthresholdentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mtetriggerthresholdentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteTriggerThresholdEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mteobjectstable(Entity):
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
            super(DismanEventMib.Mteobjectstable, self).__init__()

            self.yang_name = "mteObjectsTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteobjectsentry = YList(self)

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
                        super(DismanEventMib.Mteobjectstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteobjectstable, self).__setattr__(name, value)


        class Mteobjectsentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
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
                super(DismanEventMib.Mteobjectstable.Mteobjectsentry, self).__init__()

                self.yang_name = "mteObjectsEntry"
                self.yang_parent_name = "mteObjectsTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mteobjectsname = YLeaf(YType.str, "mteObjectsName")

                self.mteobjectsindex = YLeaf(YType.uint32, "mteObjectsIndex")

                self.mteobjectsentrystatus = YLeaf(YType.enumeration, "mteObjectsEntryStatus")

                self.mteobjectsid = YLeaf(YType.str, "mteObjectsID")

                self.mteobjectsidwildcard = YLeaf(YType.boolean, "mteObjectsIDWildcard")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mteobjectsname",
                                "mteobjectsindex",
                                "mteobjectsentrystatus",
                                "mteobjectsid",
                                "mteobjectsidwildcard") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mteobjectstable.Mteobjectsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mteobjectstable.Mteobjectsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mteobjectsname.is_set or
                    self.mteobjectsindex.is_set or
                    self.mteobjectsentrystatus.is_set or
                    self.mteobjectsid.is_set or
                    self.mteobjectsidwildcard.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mteobjectsname.yfilter != YFilter.not_set or
                    self.mteobjectsindex.yfilter != YFilter.not_set or
                    self.mteobjectsentrystatus.yfilter != YFilter.not_set or
                    self.mteobjectsid.yfilter != YFilter.not_set or
                    self.mteobjectsidwildcard.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteObjectsEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteObjectsName='" + self.mteobjectsname.get() + "']" + "[mteObjectsIndex='" + self.mteobjectsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteObjectsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mteobjectsname.is_set or self.mteobjectsname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteobjectsname.get_name_leafdata())
                if (self.mteobjectsindex.is_set or self.mteobjectsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteobjectsindex.get_name_leafdata())
                if (self.mteobjectsentrystatus.is_set or self.mteobjectsentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteobjectsentrystatus.get_name_leafdata())
                if (self.mteobjectsid.is_set or self.mteobjectsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteobjectsid.get_name_leafdata())
                if (self.mteobjectsidwildcard.is_set or self.mteobjectsidwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteobjectsidwildcard.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteObjectsName" or name == "mteObjectsIndex" or name == "mteObjectsEntryStatus" or name == "mteObjectsID" or name == "mteObjectsIDWildcard"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteObjectsName"):
                    self.mteobjectsname = value
                    self.mteobjectsname.value_namespace = name_space
                    self.mteobjectsname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteObjectsIndex"):
                    self.mteobjectsindex = value
                    self.mteobjectsindex.value_namespace = name_space
                    self.mteobjectsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mteObjectsEntryStatus"):
                    self.mteobjectsentrystatus = value
                    self.mteobjectsentrystatus.value_namespace = name_space
                    self.mteobjectsentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mteObjectsID"):
                    self.mteobjectsid = value
                    self.mteobjectsid.value_namespace = name_space
                    self.mteobjectsid.value_namespace_prefix = name_space_prefix
                if(value_path == "mteObjectsIDWildcard"):
                    self.mteobjectsidwildcard = value
                    self.mteobjectsidwildcard.value_namespace = name_space
                    self.mteobjectsidwildcard.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mteobjectsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mteobjectsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteObjectsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteObjectsEntry"):
                for c in self.mteobjectsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mteobjectstable.Mteobjectsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mteobjectsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteObjectsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mteeventtable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteevententry
        
        	Information about a single event.  Applications create and delete entries using mteEventEntryStatus
        	**type**\: list of    :py:class:`Mteevententry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventtable.Mteevententry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DismanEventMib.Mteeventtable, self).__init__()

            self.yang_name = "mteEventTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteevententry = YList(self)

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
                        super(DismanEventMib.Mteeventtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteeventtable, self).__setattr__(name, value)


        class Mteevententry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'DISMAN-EVENT-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DismanEventMib.Mteeventtable.Mteevententry, self).__init__()

                self.yang_name = "mteEventEntry"
                self.yang_parent_name = "mteEventTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mteeventname = YLeaf(YType.str, "mteEventName")

                self.mteeventactions = YLeaf(YType.bits, "mteEventActions")

                self.mteeventcomment = YLeaf(YType.str, "mteEventComment")

                self.mteeventenabled = YLeaf(YType.boolean, "mteEventEnabled")

                self.mteevententrystatus = YLeaf(YType.enumeration, "mteEventEntryStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mteeventname",
                                "mteeventactions",
                                "mteeventcomment",
                                "mteeventenabled",
                                "mteevententrystatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mteeventtable.Mteevententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mteeventtable.Mteevententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mteeventname.is_set or
                    self.mteeventactions.is_set or
                    self.mteeventcomment.is_set or
                    self.mteeventenabled.is_set or
                    self.mteevententrystatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mteeventname.yfilter != YFilter.not_set or
                    self.mteeventactions.yfilter != YFilter.not_set or
                    self.mteeventcomment.yfilter != YFilter.not_set or
                    self.mteeventenabled.yfilter != YFilter.not_set or
                    self.mteevententrystatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteEventEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteEventName='" + self.mteeventname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mteeventname.is_set or self.mteeventname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventname.get_name_leafdata())
                if (self.mteeventactions.is_set or self.mteeventactions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventactions.get_name_leafdata())
                if (self.mteeventcomment.is_set or self.mteeventcomment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventcomment.get_name_leafdata())
                if (self.mteeventenabled.is_set or self.mteeventenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventenabled.get_name_leafdata())
                if (self.mteevententrystatus.is_set or self.mteevententrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteevententrystatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteEventName" or name == "mteEventActions" or name == "mteEventComment" or name == "mteEventEnabled" or name == "mteEventEntryStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventName"):
                    self.mteeventname = value
                    self.mteeventname.value_namespace = name_space
                    self.mteeventname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventActions"):
                    self.mteeventactions[value] = True
                if(value_path == "mteEventComment"):
                    self.mteeventcomment = value
                    self.mteeventcomment.value_namespace = name_space
                    self.mteeventcomment.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventEnabled"):
                    self.mteeventenabled = value
                    self.mteeventenabled.value_namespace = name_space
                    self.mteeventenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventEntryStatus"):
                    self.mteevententrystatus = value
                    self.mteevententrystatus.value_namespace = name_space
                    self.mteevententrystatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mteevententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mteevententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteEventTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteEventEntry"):
                for c in self.mteevententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mteeventtable.Mteevententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mteevententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteEventEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mteeventnotificationtable(Entity):
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
            super(DismanEventMib.Mteeventnotificationtable, self).__init__()

            self.yang_name = "mteEventNotificationTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteeventnotificationentry = YList(self)

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
                        super(DismanEventMib.Mteeventnotificationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteeventnotificationtable, self).__setattr__(name, value)


        class Mteeventnotificationentry(Entity):
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
                super(DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry, self).__init__()

                self.yang_name = "mteEventNotificationEntry"
                self.yang_parent_name = "mteEventNotificationTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mteeventname = YLeaf(YType.str, "mteEventName")

                self.mteeventnotification = YLeaf(YType.str, "mteEventNotification")

                self.mteeventnotificationobjects = YLeaf(YType.str, "mteEventNotificationObjects")

                self.mteeventnotificationobjectsowner = YLeaf(YType.str, "mteEventNotificationObjectsOwner")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mteeventname",
                                "mteeventnotification",
                                "mteeventnotificationobjects",
                                "mteeventnotificationobjectsowner") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mteeventname.is_set or
                    self.mteeventnotification.is_set or
                    self.mteeventnotificationobjects.is_set or
                    self.mteeventnotificationobjectsowner.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mteeventname.yfilter != YFilter.not_set or
                    self.mteeventnotification.yfilter != YFilter.not_set or
                    self.mteeventnotificationobjects.yfilter != YFilter.not_set or
                    self.mteeventnotificationobjectsowner.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteEventNotificationEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteEventName='" + self.mteeventname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventNotificationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mteeventname.is_set or self.mteeventname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventname.get_name_leafdata())
                if (self.mteeventnotification.is_set or self.mteeventnotification.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventnotification.get_name_leafdata())
                if (self.mteeventnotificationobjects.is_set or self.mteeventnotificationobjects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventnotificationobjects.get_name_leafdata())
                if (self.mteeventnotificationobjectsowner.is_set or self.mteeventnotificationobjectsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventnotificationobjectsowner.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteEventName" or name == "mteEventNotification" or name == "mteEventNotificationObjects" or name == "mteEventNotificationObjectsOwner"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventName"):
                    self.mteeventname = value
                    self.mteeventname.value_namespace = name_space
                    self.mteeventname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventNotification"):
                    self.mteeventnotification = value
                    self.mteeventnotification.value_namespace = name_space
                    self.mteeventnotification.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventNotificationObjects"):
                    self.mteeventnotificationobjects = value
                    self.mteeventnotificationobjects.value_namespace = name_space
                    self.mteeventnotificationobjects.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventNotificationObjectsOwner"):
                    self.mteeventnotificationobjectsowner = value
                    self.mteeventnotificationobjectsowner.value_namespace = name_space
                    self.mteeventnotificationobjectsowner.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mteeventnotificationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mteeventnotificationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteEventNotificationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteEventNotificationEntry"):
                for c in self.mteeventnotificationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mteeventnotificationtable.Mteeventnotificationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mteeventnotificationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteEventNotificationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mteeventsettable(Entity):
        """
        A table of management event action information.
        
        .. attribute:: mteeventsetentry
        
        	Information about a single event's set option.  Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions
        	**type**\: list of    :py:class:`Mteeventsetentry <ydk.models.cisco_ios_xe.DISMAN_EVENT_MIB.DismanEventMib.Mteeventsettable.Mteeventsetentry>`
        
        

        """

        _prefix = 'DISMAN-EVENT-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DismanEventMib.Mteeventsettable, self).__init__()

            self.yang_name = "mteEventSetTable"
            self.yang_parent_name = "DISMAN-EVENT-MIB"

            self.mteeventsetentry = YList(self)

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
                        super(DismanEventMib.Mteeventsettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DismanEventMib.Mteeventsettable, self).__setattr__(name, value)


        class Mteeventsetentry(Entity):
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
                super(DismanEventMib.Mteeventsettable.Mteeventsetentry, self).__init__()

                self.yang_name = "mteEventSetEntry"
                self.yang_parent_name = "mteEventSetTable"

                self.mteowner = YLeaf(YType.str, "mteOwner")

                self.mteeventname = YLeaf(YType.str, "mteEventName")

                self.mteeventsetcontextname = YLeaf(YType.str, "mteEventSetContextName")

                self.mteeventsetcontextnamewildcard = YLeaf(YType.boolean, "mteEventSetContextNameWildcard")

                self.mteeventsetobject = YLeaf(YType.str, "mteEventSetObject")

                self.mteeventsetobjectwildcard = YLeaf(YType.boolean, "mteEventSetObjectWildcard")

                self.mteeventsettargettag = YLeaf(YType.str, "mteEventSetTargetTag")

                self.mteeventsetvalue = YLeaf(YType.int32, "mteEventSetValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mteowner",
                                "mteeventname",
                                "mteeventsetcontextname",
                                "mteeventsetcontextnamewildcard",
                                "mteeventsetobject",
                                "mteeventsetobjectwildcard",
                                "mteeventsettargettag",
                                "mteeventsetvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DismanEventMib.Mteeventsettable.Mteeventsetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DismanEventMib.Mteeventsettable.Mteeventsetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mteowner.is_set or
                    self.mteeventname.is_set or
                    self.mteeventsetcontextname.is_set or
                    self.mteeventsetcontextnamewildcard.is_set or
                    self.mteeventsetobject.is_set or
                    self.mteeventsetobjectwildcard.is_set or
                    self.mteeventsettargettag.is_set or
                    self.mteeventsetvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mteowner.yfilter != YFilter.not_set or
                    self.mteeventname.yfilter != YFilter.not_set or
                    self.mteeventsetcontextname.yfilter != YFilter.not_set or
                    self.mteeventsetcontextnamewildcard.yfilter != YFilter.not_set or
                    self.mteeventsetobject.yfilter != YFilter.not_set or
                    self.mteeventsetobjectwildcard.yfilter != YFilter.not_set or
                    self.mteeventsettargettag.yfilter != YFilter.not_set or
                    self.mteeventsetvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mteEventSetEntry" + "[mteOwner='" + self.mteowner.get() + "']" + "[mteEventName='" + self.mteeventname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/mteEventSetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mteowner.is_set or self.mteowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteowner.get_name_leafdata())
                if (self.mteeventname.is_set or self.mteeventname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventname.get_name_leafdata())
                if (self.mteeventsetcontextname.is_set or self.mteeventsetcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsetcontextname.get_name_leafdata())
                if (self.mteeventsetcontextnamewildcard.is_set or self.mteeventsetcontextnamewildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsetcontextnamewildcard.get_name_leafdata())
                if (self.mteeventsetobject.is_set or self.mteeventsetobject.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsetobject.get_name_leafdata())
                if (self.mteeventsetobjectwildcard.is_set or self.mteeventsetobjectwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsetobjectwildcard.get_name_leafdata())
                if (self.mteeventsettargettag.is_set or self.mteeventsettargettag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsettargettag.get_name_leafdata())
                if (self.mteeventsetvalue.is_set or self.mteeventsetvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mteeventsetvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mteOwner" or name == "mteEventName" or name == "mteEventSetContextName" or name == "mteEventSetContextNameWildcard" or name == "mteEventSetObject" or name == "mteEventSetObjectWildcard" or name == "mteEventSetTargetTag" or name == "mteEventSetValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mteOwner"):
                    self.mteowner = value
                    self.mteowner.value_namespace = name_space
                    self.mteowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventName"):
                    self.mteeventname = value
                    self.mteeventname.value_namespace = name_space
                    self.mteeventname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetContextName"):
                    self.mteeventsetcontextname = value
                    self.mteeventsetcontextname.value_namespace = name_space
                    self.mteeventsetcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetContextNameWildcard"):
                    self.mteeventsetcontextnamewildcard = value
                    self.mteeventsetcontextnamewildcard.value_namespace = name_space
                    self.mteeventsetcontextnamewildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetObject"):
                    self.mteeventsetobject = value
                    self.mteeventsetobject.value_namespace = name_space
                    self.mteeventsetobject.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetObjectWildcard"):
                    self.mteeventsetobjectwildcard = value
                    self.mteeventsetobjectwildcard.value_namespace = name_space
                    self.mteeventsetobjectwildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetTargetTag"):
                    self.mteeventsettargettag = value
                    self.mteeventsettargettag.value_namespace = name_space
                    self.mteeventsettargettag.value_namespace_prefix = name_space_prefix
                if(value_path == "mteEventSetValue"):
                    self.mteeventsetvalue = value
                    self.mteeventsetvalue.value_namespace = name_space
                    self.mteeventsetvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mteeventsetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mteeventsetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mteEventSetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mteEventSetEntry"):
                for c in self.mteeventsetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DismanEventMib.Mteeventsettable.Mteeventsetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mteeventsetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mteEventSetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mteevent is not None and self.mteevent.has_data()) or
            (self.mteeventnotificationtable is not None and self.mteeventnotificationtable.has_data()) or
            (self.mteeventsettable is not None and self.mteeventsettable.has_data()) or
            (self.mteeventtable is not None and self.mteeventtable.has_data()) or
            (self.mteobjectstable is not None and self.mteobjectstable.has_data()) or
            (self.mteresource is not None and self.mteresource.has_data()) or
            (self.mtetrigger is not None and self.mtetrigger.has_data()) or
            (self.mtetriggerbooleantable is not None and self.mtetriggerbooleantable.has_data()) or
            (self.mtetriggerdeltatable is not None and self.mtetriggerdeltatable.has_data()) or
            (self.mtetriggerexistencetable is not None and self.mtetriggerexistencetable.has_data()) or
            (self.mtetriggertable is not None and self.mtetriggertable.has_data()) or
            (self.mtetriggerthresholdtable is not None and self.mtetriggerthresholdtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mteevent is not None and self.mteevent.has_operation()) or
            (self.mteeventnotificationtable is not None and self.mteeventnotificationtable.has_operation()) or
            (self.mteeventsettable is not None and self.mteeventsettable.has_operation()) or
            (self.mteeventtable is not None and self.mteeventtable.has_operation()) or
            (self.mteobjectstable is not None and self.mteobjectstable.has_operation()) or
            (self.mteresource is not None and self.mteresource.has_operation()) or
            (self.mtetrigger is not None and self.mtetrigger.has_operation()) or
            (self.mtetriggerbooleantable is not None and self.mtetriggerbooleantable.has_operation()) or
            (self.mtetriggerdeltatable is not None and self.mtetriggerdeltatable.has_operation()) or
            (self.mtetriggerexistencetable is not None and self.mtetriggerexistencetable.has_operation()) or
            (self.mtetriggertable is not None and self.mtetriggertable.has_operation()) or
            (self.mtetriggerthresholdtable is not None and self.mtetriggerthresholdtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DISMAN-EVENT-MIB:DISMAN-EVENT-MIB" + path_buffer

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

        if (child_yang_name == "mteEvent"):
            if (self.mteevent is None):
                self.mteevent = DismanEventMib.Mteevent()
                self.mteevent.parent = self
                self._children_name_map["mteevent"] = "mteEvent"
            return self.mteevent

        if (child_yang_name == "mteEventNotificationTable"):
            if (self.mteeventnotificationtable is None):
                self.mteeventnotificationtable = DismanEventMib.Mteeventnotificationtable()
                self.mteeventnotificationtable.parent = self
                self._children_name_map["mteeventnotificationtable"] = "mteEventNotificationTable"
            return self.mteeventnotificationtable

        if (child_yang_name == "mteEventSetTable"):
            if (self.mteeventsettable is None):
                self.mteeventsettable = DismanEventMib.Mteeventsettable()
                self.mteeventsettable.parent = self
                self._children_name_map["mteeventsettable"] = "mteEventSetTable"
            return self.mteeventsettable

        if (child_yang_name == "mteEventTable"):
            if (self.mteeventtable is None):
                self.mteeventtable = DismanEventMib.Mteeventtable()
                self.mteeventtable.parent = self
                self._children_name_map["mteeventtable"] = "mteEventTable"
            return self.mteeventtable

        if (child_yang_name == "mteObjectsTable"):
            if (self.mteobjectstable is None):
                self.mteobjectstable = DismanEventMib.Mteobjectstable()
                self.mteobjectstable.parent = self
                self._children_name_map["mteobjectstable"] = "mteObjectsTable"
            return self.mteobjectstable

        if (child_yang_name == "mteResource"):
            if (self.mteresource is None):
                self.mteresource = DismanEventMib.Mteresource()
                self.mteresource.parent = self
                self._children_name_map["mteresource"] = "mteResource"
            return self.mteresource

        if (child_yang_name == "mteTrigger"):
            if (self.mtetrigger is None):
                self.mtetrigger = DismanEventMib.Mtetrigger()
                self.mtetrigger.parent = self
                self._children_name_map["mtetrigger"] = "mteTrigger"
            return self.mtetrigger

        if (child_yang_name == "mteTriggerBooleanTable"):
            if (self.mtetriggerbooleantable is None):
                self.mtetriggerbooleantable = DismanEventMib.Mtetriggerbooleantable()
                self.mtetriggerbooleantable.parent = self
                self._children_name_map["mtetriggerbooleantable"] = "mteTriggerBooleanTable"
            return self.mtetriggerbooleantable

        if (child_yang_name == "mteTriggerDeltaTable"):
            if (self.mtetriggerdeltatable is None):
                self.mtetriggerdeltatable = DismanEventMib.Mtetriggerdeltatable()
                self.mtetriggerdeltatable.parent = self
                self._children_name_map["mtetriggerdeltatable"] = "mteTriggerDeltaTable"
            return self.mtetriggerdeltatable

        if (child_yang_name == "mteTriggerExistenceTable"):
            if (self.mtetriggerexistencetable is None):
                self.mtetriggerexistencetable = DismanEventMib.Mtetriggerexistencetable()
                self.mtetriggerexistencetable.parent = self
                self._children_name_map["mtetriggerexistencetable"] = "mteTriggerExistenceTable"
            return self.mtetriggerexistencetable

        if (child_yang_name == "mteTriggerTable"):
            if (self.mtetriggertable is None):
                self.mtetriggertable = DismanEventMib.Mtetriggertable()
                self.mtetriggertable.parent = self
                self._children_name_map["mtetriggertable"] = "mteTriggerTable"
            return self.mtetriggertable

        if (child_yang_name == "mteTriggerThresholdTable"):
            if (self.mtetriggerthresholdtable is None):
                self.mtetriggerthresholdtable = DismanEventMib.Mtetriggerthresholdtable()
                self.mtetriggerthresholdtable.parent = self
                self._children_name_map["mtetriggerthresholdtable"] = "mteTriggerThresholdTable"
            return self.mtetriggerthresholdtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mteEvent" or name == "mteEventNotificationTable" or name == "mteEventSetTable" or name == "mteEventTable" or name == "mteObjectsTable" or name == "mteResource" or name == "mteTrigger" or name == "mteTriggerBooleanTable" or name == "mteTriggerDeltaTable" or name == "mteTriggerExistenceTable" or name == "mteTriggerTable" or name == "mteTriggerThresholdTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DismanEventMib()
        return self._top_entity

