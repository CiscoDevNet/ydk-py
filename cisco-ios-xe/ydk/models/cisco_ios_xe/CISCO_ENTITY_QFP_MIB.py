""" CISCO_ENTITY_QFP_MIB 

This MIB module defines managed objects that facilitate the
management of Quantum Flow Processors (QFP), which are listed
in the ENTITY\-MIB (RFC 4133) entPhysicalTable as an
entPhysicalClass of 'cpu'.

The Quantum Flow Processors (QFP) technology is an architecture
family developed by Cisco, which has fully integrated and
programmable networking chip set that controls different
functions of a system such as packet forwarding.

This module contains objects to monitor various QFP
statistics such as system, utilization, memory, etc.

The utilization statistics can be used for future capacity
planning. The calculation of this statistics may vary by
devices which host QFPs, hence the user must refer to the
specific device document of interest for the exact method
of calculation. The utilization statistics have the following
terminology.

o Input \- Communication channel where packets arrive on the
          QFP.

o Output \- Communication channel where packets leave the QFP.

o Priority \- A classification applied to packets indicating
             they should be treated with greater urgency.

o Non\-Priority \- A classification applied to packets indicating
                 they should be treated with lesser urgency.

o Processing Load \- The percentage of time over some interval
                    that the QFP has spent forwarding packets,
                    relative to the total time spent both 
                    forwarding packets and being idle.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscoqfpmemoryresource(Enum):
    """
    Ciscoqfpmemoryresource

    An enumerated integer\-value describing various memory resources

    used by the QFP.

    dram (1) \- Dynamic Random Access Memory (DRAM) memory resource

    .. data:: dram = 1

    """

    dram = Enum.YLeaf(1, "dram")


class Ciscoqfptimeinterval(Enum):
    """
    Ciscoqfptimeinterval

    An enumerated integer\-value describing the available interval

    values for which the periodic statistics are to be collected.

    fiveSeconds (1)   \- Interval to collect last 5 seconds       

                        statistics

    oneMinute(2)      \- Interval to collect last 1 minute

                        statistics

    fiveMinutes(3)    \- Interval to collect last 5 minutes       

                        statistics

    sixtyMinutes(4)   \- Interval to collect last 60 minutes       

                        statistics

    .. data:: fiveSeconds = 1

    .. data:: oneMinute = 2

    .. data:: fiveMinutes = 3

    .. data:: sixtyMinutes = 4

    """

    fiveSeconds = Enum.YLeaf(1, "fiveSeconds")

    oneMinute = Enum.YLeaf(2, "oneMinute")

    fiveMinutes = Enum.YLeaf(3, "fiveMinutes")

    sixtyMinutes = Enum.YLeaf(4, "sixtyMinutes")



class CiscoEntityQfpMib(Entity):
    """
    
    
    .. attribute:: ceqfpmemoryresourcetable
    
    	This table maintains the memory resources statistics for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity and its supported memory resource type upon detection of a physical entity supporting the memory  resource statistics for a memory resource type.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity and its supported memory resource type upon removal of the QFP host physical entity or it does not receive memory resource statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfpmemoryresourcetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpmemoryresourcetable>`
    
    .. attribute:: ceqfpsystemtable
    
    	This table maintains the QFP system information for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP system information.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpsystemtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable>`
    
    .. attribute:: ceqfpthroughputtable
    
    	This table maintains the throughput information for each QFP physical entity.          An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP throughput information.          An agent destroys a conceptual row from this table       corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpthroughputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable>`
    
    .. attribute:: ceqfputilizationtable
    
    	This table maintains the utilization statistics collected by each QFP physical entity at various time interval such as last 5 seconds, 1 minute, etc.  An agent creates a conceptual row to this table corresponding to a QFP physical entity for a time interval upon detection of a physical entity supporting the utilization statistics for a time interval.  The agent destroys a conceptual row from this table        corresponding to a QFP physical entity for a time interval upon removal of the QFP host physical entity or it does not receive the utilization statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfputilizationtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfputilizationtable>`
    
    .. attribute:: ciscoentityqfp
    
    	
    	**type**\:   :py:class:`Ciscoentityqfp <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp>`
    
    .. attribute:: ciscoentityqfpnotif
    
    	
    	**type**\:   :py:class:`Ciscoentityqfpnotif <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfpnotif>`
    
    

    """

    _prefix = 'CISCO-ENTITY-QFP-MIB'
    _revision = '2014-06-18'

    def __init__(self):
        super(CiscoEntityQfpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-QFP-MIB"
        self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

        self.ceqfpmemoryresourcetable = CiscoEntityQfpMib.Ceqfpmemoryresourcetable()
        self.ceqfpmemoryresourcetable.parent = self
        self._children_name_map["ceqfpmemoryresourcetable"] = "ceqfpMemoryResourceTable"
        self._children_yang_names.add("ceqfpMemoryResourceTable")

        self.ceqfpsystemtable = CiscoEntityQfpMib.Ceqfpsystemtable()
        self.ceqfpsystemtable.parent = self
        self._children_name_map["ceqfpsystemtable"] = "ceqfpSystemTable"
        self._children_yang_names.add("ceqfpSystemTable")

        self.ceqfpthroughputtable = CiscoEntityQfpMib.Ceqfpthroughputtable()
        self.ceqfpthroughputtable.parent = self
        self._children_name_map["ceqfpthroughputtable"] = "ceqfpThroughputTable"
        self._children_yang_names.add("ceqfpThroughputTable")

        self.ceqfputilizationtable = CiscoEntityQfpMib.Ceqfputilizationtable()
        self.ceqfputilizationtable.parent = self
        self._children_name_map["ceqfputilizationtable"] = "ceqfpUtilizationTable"
        self._children_yang_names.add("ceqfpUtilizationTable")

        self.ciscoentityqfp = CiscoEntityQfpMib.Ciscoentityqfp()
        self.ciscoentityqfp.parent = self
        self._children_name_map["ciscoentityqfp"] = "ciscoEntityQfp"
        self._children_yang_names.add("ciscoEntityQfp")

        self.ciscoentityqfpnotif = CiscoEntityQfpMib.Ciscoentityqfpnotif()
        self.ciscoentityqfpnotif.parent = self
        self._children_name_map["ciscoentityqfpnotif"] = "ciscoEntityQfpNotif"
        self._children_yang_names.add("ciscoEntityQfpNotif")


    class Ciscoentityqfp(Entity):
        """
        
        
        .. attribute:: ceqfpfiveminutesutilalgo
        
        	This objects represents the method used to calculate 5 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 60 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfpfiveminutesutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.Ceqfpfiveminutesutilalgo>`
        
        .. attribute:: ceqfpfivesecondutilalgo
        
        	This objects represents the method used to calculate 5 Second interval utilization data. The enumerated values are described below.  unknown       (1) \- The calculation method is unknown fiveSecSample (2) \- The value is calculated based on the last                     5 second sampling period of utilization                     data
        	**type**\:   :py:class:`Ceqfpfivesecondutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.Ceqfpfivesecondutilalgo>`
        
        .. attribute:: ceqfponeminuteutilalgo
        
        	This objects represents the method used to calculate 1 Minute interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 12 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfponeminuteutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.Ceqfponeminuteutilalgo>`
        
        .. attribute:: ceqfpsixtyminutesutilalgo
        
        	This objects represents the method used to calculate 60 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (1) \- The value is calculated using Simple Moving                    Average of last 720 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfpsixtyminutesutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.Ceqfpsixtyminutesutilalgo>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ciscoentityqfp, self).__init__()

            self.yang_name = "ciscoEntityQfp"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfpfiveminutesutilalgo = YLeaf(YType.enumeration, "ceqfpFiveMinutesUtilAlgo")

            self.ceqfpfivesecondutilalgo = YLeaf(YType.enumeration, "ceqfpFiveSecondUtilAlgo")

            self.ceqfponeminuteutilalgo = YLeaf(YType.enumeration, "ceqfpOneMinuteUtilAlgo")

            self.ceqfpsixtyminutesutilalgo = YLeaf(YType.enumeration, "ceqfpSixtyMinutesUtilAlgo")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ceqfpfiveminutesutilalgo",
                            "ceqfpfivesecondutilalgo",
                            "ceqfponeminuteutilalgo",
                            "ceqfpsixtyminutesutilalgo") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntityQfpMib.Ciscoentityqfp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ciscoentityqfp, self).__setattr__(name, value)

        class Ceqfpfiveminutesutilalgo(Enum):
            """
            Ceqfpfiveminutesutilalgo

            This objects represents the method used to calculate 5 Minutes

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (2) \- The value is calculated using Simple Moving  

                             Average of last 60 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")


        class Ceqfpfivesecondutilalgo(Enum):
            """
            Ceqfpfivesecondutilalgo

            This objects represents the method used to calculate 5 Second

            interval utilization data. The enumerated values are described

            below.

            unknown       (1) \- The calculation method is unknown

            fiveSecSample (2) \- The value is calculated based on the last

                                5 second sampling period of utilization

                                data.

            .. data:: unknown = 1

            .. data:: fiveSecSample = 2

            """

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSample = Enum.YLeaf(2, "fiveSecSample")


        class Ceqfponeminuteutilalgo(Enum):
            """
            Ceqfponeminuteutilalgo

            This objects represents the method used to calculate 1 Minute

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (2) \- The value is calculated using Simple Moving  

                             Average of last 12 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")


        class Ceqfpsixtyminutesutilalgo(Enum):
            """
            Ceqfpsixtyminutesutilalgo

            This objects represents the method used to calculate 60 Minutes

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (1) \- The value is calculated using Simple Moving  

                             Average of last 720 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")


        def has_data(self):
            return (
                self.ceqfpfiveminutesutilalgo.is_set or
                self.ceqfpfivesecondutilalgo.is_set or
                self.ceqfponeminuteutilalgo.is_set or
                self.ceqfpsixtyminutesutilalgo.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ceqfpfiveminutesutilalgo.yfilter != YFilter.not_set or
                self.ceqfpfivesecondutilalgo.yfilter != YFilter.not_set or
                self.ceqfponeminuteutilalgo.yfilter != YFilter.not_set or
                self.ceqfpsixtyminutesutilalgo.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEntityQfp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ceqfpfiveminutesutilalgo.is_set or self.ceqfpfiveminutesutilalgo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfpfiveminutesutilalgo.get_name_leafdata())
            if (self.ceqfpfivesecondutilalgo.is_set or self.ceqfpfivesecondutilalgo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfpfivesecondutilalgo.get_name_leafdata())
            if (self.ceqfponeminuteutilalgo.is_set or self.ceqfponeminuteutilalgo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfponeminuteutilalgo.get_name_leafdata())
            if (self.ceqfpsixtyminutesutilalgo.is_set or self.ceqfpsixtyminutesutilalgo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfpsixtyminutesutilalgo.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpFiveMinutesUtilAlgo" or name == "ceqfpFiveSecondUtilAlgo" or name == "ceqfpOneMinuteUtilAlgo" or name == "ceqfpSixtyMinutesUtilAlgo"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ceqfpFiveMinutesUtilAlgo"):
                self.ceqfpfiveminutesutilalgo = value
                self.ceqfpfiveminutesutilalgo.value_namespace = name_space
                self.ceqfpfiveminutesutilalgo.value_namespace_prefix = name_space_prefix
            if(value_path == "ceqfpFiveSecondUtilAlgo"):
                self.ceqfpfivesecondutilalgo = value
                self.ceqfpfivesecondutilalgo.value_namespace = name_space
                self.ceqfpfivesecondutilalgo.value_namespace_prefix = name_space_prefix
            if(value_path == "ceqfpOneMinuteUtilAlgo"):
                self.ceqfponeminuteutilalgo = value
                self.ceqfponeminuteutilalgo.value_namespace = name_space
                self.ceqfponeminuteutilalgo.value_namespace_prefix = name_space_prefix
            if(value_path == "ceqfpSixtyMinutesUtilAlgo"):
                self.ceqfpsixtyminutesutilalgo = value
                self.ceqfpsixtyminutesutilalgo.value_namespace = name_space
                self.ceqfpsixtyminutesutilalgo.value_namespace_prefix = name_space_prefix


    class Ciscoentityqfpnotif(Entity):
        """
        
        
        .. attribute:: ceqfpmemoryresthreshnotifenabled
        
        	This object controls memory resource rising and falling threshold notification.  When this object contains a value 'true', then generation of memory resource threshold notification is enabled. If this object contains a value 'false', then generation of memory resource threshold notification is disabled
        	**type**\:  bool
        
        .. attribute:: ceqfpthroughputnotifenabled
        
        	This object controls throughput rate notification.  When this object contains a value 'true', then generation of ceqfpThroughputNotif is enabled. If this object contains a value 'false', then generation of ceqfpThroughputNotif is disabled
        	**type**\:  int
        
        	**range:** 0..2
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ciscoentityqfpnotif, self).__init__()

            self.yang_name = "ciscoEntityQfpNotif"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfpmemoryresthreshnotifenabled = YLeaf(YType.boolean, "ceqfpMemoryResThreshNotifEnabled")

            self.ceqfpthroughputnotifenabled = YLeaf(YType.uint32, "ceqfpThroughputNotifEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ceqfpmemoryresthreshnotifenabled",
                            "ceqfpthroughputnotifenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntityQfpMib.Ciscoentityqfpnotif, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ciscoentityqfpnotif, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ceqfpmemoryresthreshnotifenabled.is_set or
                self.ceqfpthroughputnotifenabled.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ceqfpmemoryresthreshnotifenabled.yfilter != YFilter.not_set or
                self.ceqfpthroughputnotifenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEntityQfpNotif" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ceqfpmemoryresthreshnotifenabled.is_set or self.ceqfpmemoryresthreshnotifenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfpmemoryresthreshnotifenabled.get_name_leafdata())
            if (self.ceqfpthroughputnotifenabled.is_set or self.ceqfpthroughputnotifenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceqfpthroughputnotifenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpMemoryResThreshNotifEnabled" or name == "ceqfpThroughputNotifEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ceqfpMemoryResThreshNotifEnabled"):
                self.ceqfpmemoryresthreshnotifenabled = value
                self.ceqfpmemoryresthreshnotifenabled.value_namespace = name_space
                self.ceqfpmemoryresthreshnotifenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "ceqfpThroughputNotifEnabled"):
                self.ceqfpthroughputnotifenabled = value
                self.ceqfpthroughputnotifenabled.value_namespace = name_space
                self.ceqfpthroughputnotifenabled.value_namespace_prefix = name_space_prefix


    class Ceqfpsystemtable(Entity):
        """
        This table maintains the QFP system information for each QFP
        physical entity.
        
        An agent creates a conceptual row to this table corresponding
        to a QFP physical entity upon detection of a physical entity
        supporting the QFP system information.
        
        An agent destroys a conceptual row from this table       
        corresponding to a QFP physical entity upon removal
        of the QFP host physical entity.
        
        .. attribute:: ceqfpsystementry
        
        	A conceptual row in the ceqfpSystemTable. There is an entry in this table for each QFP entity, as defined by a value of entPhysicalIndex
        	**type**\: list of    :py:class:`Ceqfpsystementry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ceqfpsystemtable, self).__init__()

            self.yang_name = "ceqfpSystemTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfpsystementry = YList(self)

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
                        super(CiscoEntityQfpMib.Ceqfpsystemtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ceqfpsystemtable, self).__setattr__(name, value)


        class Ceqfpsystementry(Entity):
            """
            A conceptual row in the ceqfpSystemTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpnumbersystemloads
            
            	This object represents the number of times the QFP is loaded, since the QFP host is up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpsystemlastloadtime
            
            	This object represents the QFP last load time
            	**type**\:  str
            
            .. attribute:: ceqfpsystemstate
            
            	This object represents the current QFP state. The enumerated values are described below.  unknown (1)    \- The state of the QFP is unknown reset (2)      \- The QFP is reset init (3)       \- The QFP is being initialized active (4)     \- The QFP is active in a system with redundant                  QFP activeSolo (5) \- The QFP is active and there is no redundant                  QFP in the system standby (6)    \- The QFP is standby in a redundant system. hotStandby (7) \- The QFP is standby and synchronized with                  active, so that a switchover in this state                  will preserve state of the active. Stateful                   datapath features are synchronized between the                  active QFP and standby QFP
            	**type**\:   :py:class:`Ceqfpsystemstate <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.Ceqfpsystemstate>`
            
            .. attribute:: ceqfpsystemtrafficdirection
            
            	This object represents the traffic direction that this QFP is assigned to process. The enumerated values are described below.  none (1)    \- The QFP is not assigned to processes any traffic               yet ingress (2) \- The QFP processes inbound traffic egress (3)  \- The QFP processes outbound traffic both (4)    \- The QFP processes both inbound and outbound               traffic
            	**type**\:   :py:class:`Ceqfpsystemtrafficdirection <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.Ceqfpsystemtrafficdirection>`
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                super(CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry, self).__init__()

                self.yang_name = "ceqfpSystemEntry"
                self.yang_parent_name = "ceqfpSystemTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpnumbersystemloads = YLeaf(YType.uint32, "ceqfpNumberSystemLoads")

                self.ceqfpsystemlastloadtime = YLeaf(YType.str, "ceqfpSystemLastLoadTime")

                self.ceqfpsystemstate = YLeaf(YType.enumeration, "ceqfpSystemState")

                self.ceqfpsystemtrafficdirection = YLeaf(YType.enumeration, "ceqfpSystemTrafficDirection")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceqfpnumbersystemloads",
                                "ceqfpsystemlastloadtime",
                                "ceqfpsystemstate",
                                "ceqfpsystemtrafficdirection") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry, self).__setattr__(name, value)

            class Ceqfpsystemstate(Enum):
                """
                Ceqfpsystemstate

                This object represents the current QFP state. The enumerated

                values are described below.

                unknown (1)    \- The state of the QFP is unknown

                reset (2)      \- The QFP is reset

                init (3)       \- The QFP is being initialized

                active (4)     \- The QFP is active in a system with redundant

                                 QFP

                activeSolo (5) \- The QFP is active and there is no redundant

                                 QFP in the system

                standby (6)    \- The QFP is standby in a redundant system.

                hotStandby (7) \- The QFP is standby and synchronized with

                                 active, so that a switchover in this state

                                 will preserve state of the active. Stateful 

                                 datapath features are synchronized between the

                                 active QFP and standby QFP

                .. data:: unknown = 1

                .. data:: reset = 2

                .. data:: init = 3

                .. data:: active = 4

                .. data:: activeSolo = 5

                .. data:: standby = 6

                .. data:: hotStandby = 7

                """

                unknown = Enum.YLeaf(1, "unknown")

                reset = Enum.YLeaf(2, "reset")

                init = Enum.YLeaf(3, "init")

                active = Enum.YLeaf(4, "active")

                activeSolo = Enum.YLeaf(5, "activeSolo")

                standby = Enum.YLeaf(6, "standby")

                hotStandby = Enum.YLeaf(7, "hotStandby")


            class Ceqfpsystemtrafficdirection(Enum):
                """
                Ceqfpsystemtrafficdirection

                This object represents the traffic direction that this QFP is

                assigned to process. The enumerated values are described below.

                none (1)    \- The QFP is not assigned to processes any traffic

                              yet

                ingress (2) \- The QFP processes inbound traffic

                egress (3)  \- The QFP processes outbound traffic

                both (4)    \- The QFP processes both inbound and outbound

                              traffic

                .. data:: none = 1

                .. data:: ingress = 2

                .. data:: egress = 3

                .. data:: both = 4

                """

                none = Enum.YLeaf(1, "none")

                ingress = Enum.YLeaf(2, "ingress")

                egress = Enum.YLeaf(3, "egress")

                both = Enum.YLeaf(4, "both")


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceqfpnumbersystemloads.is_set or
                    self.ceqfpsystemlastloadtime.is_set or
                    self.ceqfpsystemstate.is_set or
                    self.ceqfpsystemtrafficdirection.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceqfpnumbersystemloads.yfilter != YFilter.not_set or
                    self.ceqfpsystemlastloadtime.yfilter != YFilter.not_set or
                    self.ceqfpsystemstate.yfilter != YFilter.not_set or
                    self.ceqfpsystemtrafficdirection.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceqfpSystemEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpSystemTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceqfpnumbersystemloads.is_set or self.ceqfpnumbersystemloads.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpnumbersystemloads.get_name_leafdata())
                if (self.ceqfpsystemlastloadtime.is_set or self.ceqfpsystemlastloadtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpsystemlastloadtime.get_name_leafdata())
                if (self.ceqfpsystemstate.is_set or self.ceqfpsystemstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpsystemstate.get_name_leafdata())
                if (self.ceqfpsystemtrafficdirection.is_set or self.ceqfpsystemtrafficdirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpsystemtrafficdirection.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceqfpNumberSystemLoads" or name == "ceqfpSystemLastLoadTime" or name == "ceqfpSystemState" or name == "ceqfpSystemTrafficDirection"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpNumberSystemLoads"):
                    self.ceqfpnumbersystemloads = value
                    self.ceqfpnumbersystemloads.value_namespace = name_space
                    self.ceqfpnumbersystemloads.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpSystemLastLoadTime"):
                    self.ceqfpsystemlastloadtime = value
                    self.ceqfpsystemlastloadtime.value_namespace = name_space
                    self.ceqfpsystemlastloadtime.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpSystemState"):
                    self.ceqfpsystemstate = value
                    self.ceqfpsystemstate.value_namespace = name_space
                    self.ceqfpsystemstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpSystemTrafficDirection"):
                    self.ceqfpsystemtrafficdirection = value
                    self.ceqfpsystemtrafficdirection.value_namespace = name_space
                    self.ceqfpsystemtrafficdirection.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceqfpsystementry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceqfpsystementry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceqfpSystemTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceqfpSystemEntry"):
                for c in self.ceqfpsystementry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceqfpsystementry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpSystemEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceqfputilizationtable(Entity):
        """
        This table maintains the utilization statistics collected
        by each QFP physical entity at various time interval such as
        last 5 seconds, 1 minute, etc.
        
        An agent creates a conceptual row to this table corresponding
        to a QFP physical entity for a time interval upon detection of
        a physical entity supporting the utilization statistics for a
        time interval.
        
        The agent destroys a conceptual row from this table       
        corresponding to a QFP physical entity for a time interval
        upon removal of the QFP host physical entity or it does not
        receive the utilization statistics update for a certain time
        period. The time period to wait before deleting an entry from
        this table would be the discretion of the supporting device.
        
        .. attribute:: ceqfputilizationentry
        
        	A conceptual row in the ceqfpUtilizationTable. There is an entry in this table for each QFP entity by a value of entPhysicalIndex and the supported time interval by a value  of ceqfpUtilTimeInterval.  The method of utilization data calculation for each interval period can be identified through the respective interval scalar objects. For example the utilizaiton data calculation method for 'fiveSecond' interval can be identified by ceqfpFiveSecondUtilAlgo
        	**type**\: list of    :py:class:`Ceqfputilizationentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ceqfputilizationtable, self).__init__()

            self.yang_name = "ceqfpUtilizationTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfputilizationentry = YList(self)

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
                        super(CiscoEntityQfpMib.Ceqfputilizationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ceqfputilizationtable, self).__setattr__(name, value)


        class Ceqfputilizationentry(Entity):
            """
            A conceptual row in the ceqfpUtilizationTable. There is
            an entry in this table for each QFP entity by a value of
            entPhysicalIndex and the supported time interval by a value 
            of ceqfpUtilTimeInterval.
            
            The method of utilization data calculation for each interval
            period can be identified through the respective interval
            scalar objects. For example the utilizaiton data calculation
            method for 'fiveSecond' interval can be identified by
            ceqfpFiveSecondUtilAlgo.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfputiltimeinterval  <key>
            
            	This object identifies the time interval for which the utilization statistics being collected. The interval  values can be 5 second, 1 minute, etc. as specified in  the CiscoQfpTimeInterval
            	**type**\:   :py:class:`Ciscoqfptimeinterval <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.Ciscoqfptimeinterval>`
            
            .. attribute:: ceqfputilinputnonprioritybitrate
            
            	This object represents the QFP input channel non\-priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputnonprioritypktrate
            
            	This object represents the QFP input channel non\-priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilinputprioritybitrate
            
            	This object represents the QFP input channel priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputprioritypktrate
            
            	This object represents the QFP input channel priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilinputtotalbitrate
            
            	This object represents the QFP input channel total bit rate during this interval, which includes both priority and non\-priority input bit rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputtotalpktrate
            
            	This object represents the QFP input channel total packet rate during this interval, which includes both priority and non\-priority input packet rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputnonprioritybitrate
            
            	This object represents the QFP output channel non\-priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputnonprioritypktrate
            
            	This object represents the QFP output channel non\-priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputprioritybitrate
            
            	This object represents the QFP output channel priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputprioritypktrate
            
            	This object represents the QFP output channel priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputtotalbitrate
            
            	This object represents the QFP output channel total bit rate during this interval, which includes both priority and non\-priority bit rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputtotalpktrate
            
            	This object represents the QFP output channel total packet rate during this interval, which includes both priority and non\-priority output packet rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilprocessingload
            
            	This object represents the QFP processing load during this interval
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                super(CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry, self).__init__()

                self.yang_name = "ceqfpUtilizationEntry"
                self.yang_parent_name = "ceqfpUtilizationTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfputiltimeinterval = YLeaf(YType.enumeration, "ceqfpUtilTimeInterval")

                self.ceqfputilinputnonprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilInputNonPriorityBitRate")

                self.ceqfputilinputnonprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilInputNonPriorityPktRate")

                self.ceqfputilinputprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilInputPriorityBitRate")

                self.ceqfputilinputprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilInputPriorityPktRate")

                self.ceqfputilinputtotalbitrate = YLeaf(YType.uint64, "ceqfpUtilInputTotalBitRate")

                self.ceqfputilinputtotalpktrate = YLeaf(YType.uint64, "ceqfpUtilInputTotalPktRate")

                self.ceqfputiloutputnonprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilOutputNonPriorityBitRate")

                self.ceqfputiloutputnonprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilOutputNonPriorityPktRate")

                self.ceqfputiloutputprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilOutputPriorityBitRate")

                self.ceqfputiloutputprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilOutputPriorityPktRate")

                self.ceqfputiloutputtotalbitrate = YLeaf(YType.uint64, "ceqfpUtilOutputTotalBitRate")

                self.ceqfputiloutputtotalpktrate = YLeaf(YType.uint64, "ceqfpUtilOutputTotalPktRate")

                self.ceqfputilprocessingload = YLeaf(YType.uint32, "ceqfpUtilProcessingLoad")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceqfputiltimeinterval",
                                "ceqfputilinputnonprioritybitrate",
                                "ceqfputilinputnonprioritypktrate",
                                "ceqfputilinputprioritybitrate",
                                "ceqfputilinputprioritypktrate",
                                "ceqfputilinputtotalbitrate",
                                "ceqfputilinputtotalpktrate",
                                "ceqfputiloutputnonprioritybitrate",
                                "ceqfputiloutputnonprioritypktrate",
                                "ceqfputiloutputprioritybitrate",
                                "ceqfputiloutputprioritypktrate",
                                "ceqfputiloutputtotalbitrate",
                                "ceqfputiloutputtotalpktrate",
                                "ceqfputilprocessingload") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceqfputiltimeinterval.is_set or
                    self.ceqfputilinputnonprioritybitrate.is_set or
                    self.ceqfputilinputnonprioritypktrate.is_set or
                    self.ceqfputilinputprioritybitrate.is_set or
                    self.ceqfputilinputprioritypktrate.is_set or
                    self.ceqfputilinputtotalbitrate.is_set or
                    self.ceqfputilinputtotalpktrate.is_set or
                    self.ceqfputiloutputnonprioritybitrate.is_set or
                    self.ceqfputiloutputnonprioritypktrate.is_set or
                    self.ceqfputiloutputprioritybitrate.is_set or
                    self.ceqfputiloutputprioritypktrate.is_set or
                    self.ceqfputiloutputtotalbitrate.is_set or
                    self.ceqfputiloutputtotalpktrate.is_set or
                    self.ceqfputilprocessingload.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceqfputiltimeinterval.yfilter != YFilter.not_set or
                    self.ceqfputilinputnonprioritybitrate.yfilter != YFilter.not_set or
                    self.ceqfputilinputnonprioritypktrate.yfilter != YFilter.not_set or
                    self.ceqfputilinputprioritybitrate.yfilter != YFilter.not_set or
                    self.ceqfputilinputprioritypktrate.yfilter != YFilter.not_set or
                    self.ceqfputilinputtotalbitrate.yfilter != YFilter.not_set or
                    self.ceqfputilinputtotalpktrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputnonprioritybitrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputnonprioritypktrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputprioritybitrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputprioritypktrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputtotalbitrate.yfilter != YFilter.not_set or
                    self.ceqfputiloutputtotalpktrate.yfilter != YFilter.not_set or
                    self.ceqfputilprocessingload.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceqfpUtilizationEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ceqfpUtilTimeInterval='" + self.ceqfputiltimeinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpUtilizationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceqfputiltimeinterval.is_set or self.ceqfputiltimeinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiltimeinterval.get_name_leafdata())
                if (self.ceqfputilinputnonprioritybitrate.is_set or self.ceqfputilinputnonprioritybitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputnonprioritybitrate.get_name_leafdata())
                if (self.ceqfputilinputnonprioritypktrate.is_set or self.ceqfputilinputnonprioritypktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputnonprioritypktrate.get_name_leafdata())
                if (self.ceqfputilinputprioritybitrate.is_set or self.ceqfputilinputprioritybitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputprioritybitrate.get_name_leafdata())
                if (self.ceqfputilinputprioritypktrate.is_set or self.ceqfputilinputprioritypktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputprioritypktrate.get_name_leafdata())
                if (self.ceqfputilinputtotalbitrate.is_set or self.ceqfputilinputtotalbitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputtotalbitrate.get_name_leafdata())
                if (self.ceqfputilinputtotalpktrate.is_set or self.ceqfputilinputtotalpktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilinputtotalpktrate.get_name_leafdata())
                if (self.ceqfputiloutputnonprioritybitrate.is_set or self.ceqfputiloutputnonprioritybitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputnonprioritybitrate.get_name_leafdata())
                if (self.ceqfputiloutputnonprioritypktrate.is_set or self.ceqfputiloutputnonprioritypktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputnonprioritypktrate.get_name_leafdata())
                if (self.ceqfputiloutputprioritybitrate.is_set or self.ceqfputiloutputprioritybitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputprioritybitrate.get_name_leafdata())
                if (self.ceqfputiloutputprioritypktrate.is_set or self.ceqfputiloutputprioritypktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputprioritypktrate.get_name_leafdata())
                if (self.ceqfputiloutputtotalbitrate.is_set or self.ceqfputiloutputtotalbitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputtotalbitrate.get_name_leafdata())
                if (self.ceqfputiloutputtotalpktrate.is_set or self.ceqfputiloutputtotalpktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputiloutputtotalpktrate.get_name_leafdata())
                if (self.ceqfputilprocessingload.is_set or self.ceqfputilprocessingload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfputilprocessingload.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceqfpUtilTimeInterval" or name == "ceqfpUtilInputNonPriorityBitRate" or name == "ceqfpUtilInputNonPriorityPktRate" or name == "ceqfpUtilInputPriorityBitRate" or name == "ceqfpUtilInputPriorityPktRate" or name == "ceqfpUtilInputTotalBitRate" or name == "ceqfpUtilInputTotalPktRate" or name == "ceqfpUtilOutputNonPriorityBitRate" or name == "ceqfpUtilOutputNonPriorityPktRate" or name == "ceqfpUtilOutputPriorityBitRate" or name == "ceqfpUtilOutputPriorityPktRate" or name == "ceqfpUtilOutputTotalBitRate" or name == "ceqfpUtilOutputTotalPktRate" or name == "ceqfpUtilProcessingLoad"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilTimeInterval"):
                    self.ceqfputiltimeinterval = value
                    self.ceqfputiltimeinterval.value_namespace = name_space
                    self.ceqfputiltimeinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputNonPriorityBitRate"):
                    self.ceqfputilinputnonprioritybitrate = value
                    self.ceqfputilinputnonprioritybitrate.value_namespace = name_space
                    self.ceqfputilinputnonprioritybitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputNonPriorityPktRate"):
                    self.ceqfputilinputnonprioritypktrate = value
                    self.ceqfputilinputnonprioritypktrate.value_namespace = name_space
                    self.ceqfputilinputnonprioritypktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputPriorityBitRate"):
                    self.ceqfputilinputprioritybitrate = value
                    self.ceqfputilinputprioritybitrate.value_namespace = name_space
                    self.ceqfputilinputprioritybitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputPriorityPktRate"):
                    self.ceqfputilinputprioritypktrate = value
                    self.ceqfputilinputprioritypktrate.value_namespace = name_space
                    self.ceqfputilinputprioritypktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputTotalBitRate"):
                    self.ceqfputilinputtotalbitrate = value
                    self.ceqfputilinputtotalbitrate.value_namespace = name_space
                    self.ceqfputilinputtotalbitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilInputTotalPktRate"):
                    self.ceqfputilinputtotalpktrate = value
                    self.ceqfputilinputtotalpktrate.value_namespace = name_space
                    self.ceqfputilinputtotalpktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputNonPriorityBitRate"):
                    self.ceqfputiloutputnonprioritybitrate = value
                    self.ceqfputiloutputnonprioritybitrate.value_namespace = name_space
                    self.ceqfputiloutputnonprioritybitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputNonPriorityPktRate"):
                    self.ceqfputiloutputnonprioritypktrate = value
                    self.ceqfputiloutputnonprioritypktrate.value_namespace = name_space
                    self.ceqfputiloutputnonprioritypktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputPriorityBitRate"):
                    self.ceqfputiloutputprioritybitrate = value
                    self.ceqfputiloutputprioritybitrate.value_namespace = name_space
                    self.ceqfputiloutputprioritybitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputPriorityPktRate"):
                    self.ceqfputiloutputprioritypktrate = value
                    self.ceqfputiloutputprioritypktrate.value_namespace = name_space
                    self.ceqfputiloutputprioritypktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputTotalBitRate"):
                    self.ceqfputiloutputtotalbitrate = value
                    self.ceqfputiloutputtotalbitrate.value_namespace = name_space
                    self.ceqfputiloutputtotalbitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilOutputTotalPktRate"):
                    self.ceqfputiloutputtotalpktrate = value
                    self.ceqfputiloutputtotalpktrate.value_namespace = name_space
                    self.ceqfputiloutputtotalpktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpUtilProcessingLoad"):
                    self.ceqfputilprocessingload = value
                    self.ceqfputilprocessingload.value_namespace = name_space
                    self.ceqfputilprocessingload.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceqfputilizationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceqfputilizationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceqfpUtilizationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceqfpUtilizationEntry"):
                for c in self.ceqfputilizationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceqfputilizationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpUtilizationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceqfpmemoryresourcetable(Entity):
        """
        This table maintains the memory resources statistics for
        each QFP physical entity.
        
        An agent creates a conceptual row to this table corresponding
        to a QFP physical entity and its supported memory resource type
        upon detection of a physical entity supporting the memory 
        resource statistics for a memory resource type.
        
        An agent destroys a conceptual row from this table       
        corresponding to a QFP physical entity and its supported
        memory resource type upon removal of the QFP host physical
        entity or it does not receive memory resource statistics
        update for a certain time period. The time period to wait
        before deleting an entry from this table would be the
        discretion of the supporting device.
        
        .. attribute:: ceqfpmemoryresourceentry
        
        	A conceptual row in the ceqfpMemoryResourceTable. There is an entry in this table for each QFP entity by a value  of entPhysicalIndex and the supported memory resource type  by a value of ceqfpMemoryResType
        	**type**\: list of    :py:class:`Ceqfpmemoryresourceentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable, self).__init__()

            self.yang_name = "ceqfpMemoryResourceTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfpmemoryresourceentry = YList(self)

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
                        super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable, self).__setattr__(name, value)


        class Ceqfpmemoryresourceentry(Entity):
            """
            A conceptual row in the ceqfpMemoryResourceTable. There
            is an entry in this table for each QFP entity by a value 
            of entPhysicalIndex and the supported memory resource type 
            by a value of ceqfpMemoryResType.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpmemoryrestype  <key>
            
            	This object indicates the type of the memory resource used by the QFP. This object is one of the indices to uniquely identify the QFP memory resource type
            	**type**\:   :py:class:`Ciscoqfpmemoryresource <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.Ciscoqfpmemoryresource>`
            
            .. attribute:: ceqfpmemoryhcresfree
            
            	This object is a 64\-bit version of ceqfpMemoryResFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcresinuse
            
            	This object is a 64\-bit version of ceqfpMemoryInRes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcreslowfreewatermark
            
            	This object is a 64\-bit version of ceqfpMemoryResLowFreeWatermark
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcrestotal
            
            	This object is a 64\-bit version of ceqfpMemoryResTotal
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresfallingthreshold
            
            	This object represents the falling threshold value for this memory resource. A value of zero means that the falling threshold is not supported for this memory resource.  The value of this object can not be set to higher than or equal to ceqfpMemoryResRisingThreshold.  A falling (ceqfpMemoryResRisingThreshNotif) notification  will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or lesser than this value.  After a falling notification is generated, another  such notification will not be generated until the  ceqfpMemoryResInUse rises above this value and reaches  the ceqfpMemoryResRisingThreshold
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: ceqfpmemoryresfree
            
            	This object represents the memory which is currently free on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresfreeovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResFree. This object needs to be supported only when the value of ceqfpMemoryResFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresinuse
            
            	This object represents the memory which is currently under use on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresinuseovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResInUse. This object needs to be supported only when the value of ceqfpMemoryResInUse exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryreslowfreewatermark
            
            	This object represents lowest free water mark on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryreslowfreewatermarkovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResLowFreeWatermark. This object needs to be supported only when the value of ceqfpMemoryResLowFreeWatermark exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresrisingthreshold
            
            	This object represents the rising threshold value for this memory resource. A value of zero means that the rising threshold is not supported for this memory resource.  The value of this object can not be set to lower than or equal to ceqfpMemoryResFallingThreshold.  A rising (ceqfpMemoryResRisingThreshNotif) notification will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or greater than this value.  After a rising notification is generated, another such  notification will not be generated until the  ceqfpMemoryResInUse falls below this value and reaches  the ceqfpMemoryResFallingThreshold
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: ceqfpmemoryrestotal
            
            	This object represents total memory available on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryrestotalovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResTotal. This object needs to be supported only when the value of ceqfpMemoryResTotal exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry, self).__init__()

                self.yang_name = "ceqfpMemoryResourceEntry"
                self.yang_parent_name = "ceqfpMemoryResourceTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpmemoryrestype = YLeaf(YType.enumeration, "ceqfpMemoryResType")

                self.ceqfpmemoryhcresfree = YLeaf(YType.uint64, "ceqfpMemoryHCResFree")

                self.ceqfpmemoryhcresinuse = YLeaf(YType.uint64, "ceqfpMemoryHCResInUse")

                self.ceqfpmemoryhcreslowfreewatermark = YLeaf(YType.uint64, "ceqfpMemoryHCResLowFreeWatermark")

                self.ceqfpmemoryhcrestotal = YLeaf(YType.uint64, "ceqfpMemoryHCResTotal")

                self.ceqfpmemoryresfallingthreshold = YLeaf(YType.uint32, "ceqfpMemoryResFallingThreshold")

                self.ceqfpmemoryresfree = YLeaf(YType.uint32, "ceqfpMemoryResFree")

                self.ceqfpmemoryresfreeovrflw = YLeaf(YType.uint32, "ceqfpMemoryResFreeOvrflw")

                self.ceqfpmemoryresinuse = YLeaf(YType.uint32, "ceqfpMemoryResInUse")

                self.ceqfpmemoryresinuseovrflw = YLeaf(YType.uint32, "ceqfpMemoryResInUseOvrflw")

                self.ceqfpmemoryreslowfreewatermark = YLeaf(YType.uint32, "ceqfpMemoryResLowFreeWatermark")

                self.ceqfpmemoryreslowfreewatermarkovrflw = YLeaf(YType.uint32, "ceqfpMemoryResLowFreeWatermarkOvrflw")

                self.ceqfpmemoryresrisingthreshold = YLeaf(YType.uint32, "ceqfpMemoryResRisingThreshold")

                self.ceqfpmemoryrestotal = YLeaf(YType.uint32, "ceqfpMemoryResTotal")

                self.ceqfpmemoryrestotalovrflw = YLeaf(YType.uint32, "ceqfpMemoryResTotalOvrflw")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceqfpmemoryrestype",
                                "ceqfpmemoryhcresfree",
                                "ceqfpmemoryhcresinuse",
                                "ceqfpmemoryhcreslowfreewatermark",
                                "ceqfpmemoryhcrestotal",
                                "ceqfpmemoryresfallingthreshold",
                                "ceqfpmemoryresfree",
                                "ceqfpmemoryresfreeovrflw",
                                "ceqfpmemoryresinuse",
                                "ceqfpmemoryresinuseovrflw",
                                "ceqfpmemoryreslowfreewatermark",
                                "ceqfpmemoryreslowfreewatermarkovrflw",
                                "ceqfpmemoryresrisingthreshold",
                                "ceqfpmemoryrestotal",
                                "ceqfpmemoryrestotalovrflw") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceqfpmemoryrestype.is_set or
                    self.ceqfpmemoryhcresfree.is_set or
                    self.ceqfpmemoryhcresinuse.is_set or
                    self.ceqfpmemoryhcreslowfreewatermark.is_set or
                    self.ceqfpmemoryhcrestotal.is_set or
                    self.ceqfpmemoryresfallingthreshold.is_set or
                    self.ceqfpmemoryresfree.is_set or
                    self.ceqfpmemoryresfreeovrflw.is_set or
                    self.ceqfpmemoryresinuse.is_set or
                    self.ceqfpmemoryresinuseovrflw.is_set or
                    self.ceqfpmemoryreslowfreewatermark.is_set or
                    self.ceqfpmemoryreslowfreewatermarkovrflw.is_set or
                    self.ceqfpmemoryresrisingthreshold.is_set or
                    self.ceqfpmemoryrestotal.is_set or
                    self.ceqfpmemoryrestotalovrflw.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceqfpmemoryrestype.yfilter != YFilter.not_set or
                    self.ceqfpmemoryhcresfree.yfilter != YFilter.not_set or
                    self.ceqfpmemoryhcresinuse.yfilter != YFilter.not_set or
                    self.ceqfpmemoryhcreslowfreewatermark.yfilter != YFilter.not_set or
                    self.ceqfpmemoryhcrestotal.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresfallingthreshold.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresfree.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresfreeovrflw.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresinuse.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresinuseovrflw.yfilter != YFilter.not_set or
                    self.ceqfpmemoryreslowfreewatermark.yfilter != YFilter.not_set or
                    self.ceqfpmemoryreslowfreewatermarkovrflw.yfilter != YFilter.not_set or
                    self.ceqfpmemoryresrisingthreshold.yfilter != YFilter.not_set or
                    self.ceqfpmemoryrestotal.yfilter != YFilter.not_set or
                    self.ceqfpmemoryrestotalovrflw.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceqfpMemoryResourceEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ceqfpMemoryResType='" + self.ceqfpmemoryrestype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpMemoryResourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceqfpmemoryrestype.is_set or self.ceqfpmemoryrestype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryrestype.get_name_leafdata())
                if (self.ceqfpmemoryhcresfree.is_set or self.ceqfpmemoryhcresfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryhcresfree.get_name_leafdata())
                if (self.ceqfpmemoryhcresinuse.is_set or self.ceqfpmemoryhcresinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryhcresinuse.get_name_leafdata())
                if (self.ceqfpmemoryhcreslowfreewatermark.is_set or self.ceqfpmemoryhcreslowfreewatermark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryhcreslowfreewatermark.get_name_leafdata())
                if (self.ceqfpmemoryhcrestotal.is_set or self.ceqfpmemoryhcrestotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryhcrestotal.get_name_leafdata())
                if (self.ceqfpmemoryresfallingthreshold.is_set or self.ceqfpmemoryresfallingthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresfallingthreshold.get_name_leafdata())
                if (self.ceqfpmemoryresfree.is_set or self.ceqfpmemoryresfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresfree.get_name_leafdata())
                if (self.ceqfpmemoryresfreeovrflw.is_set or self.ceqfpmemoryresfreeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresfreeovrflw.get_name_leafdata())
                if (self.ceqfpmemoryresinuse.is_set or self.ceqfpmemoryresinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresinuse.get_name_leafdata())
                if (self.ceqfpmemoryresinuseovrflw.is_set or self.ceqfpmemoryresinuseovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresinuseovrflw.get_name_leafdata())
                if (self.ceqfpmemoryreslowfreewatermark.is_set or self.ceqfpmemoryreslowfreewatermark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryreslowfreewatermark.get_name_leafdata())
                if (self.ceqfpmemoryreslowfreewatermarkovrflw.is_set or self.ceqfpmemoryreslowfreewatermarkovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryreslowfreewatermarkovrflw.get_name_leafdata())
                if (self.ceqfpmemoryresrisingthreshold.is_set or self.ceqfpmemoryresrisingthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryresrisingthreshold.get_name_leafdata())
                if (self.ceqfpmemoryrestotal.is_set or self.ceqfpmemoryrestotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryrestotal.get_name_leafdata())
                if (self.ceqfpmemoryrestotalovrflw.is_set or self.ceqfpmemoryrestotalovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpmemoryrestotalovrflw.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceqfpMemoryResType" or name == "ceqfpMemoryHCResFree" or name == "ceqfpMemoryHCResInUse" or name == "ceqfpMemoryHCResLowFreeWatermark" or name == "ceqfpMemoryHCResTotal" or name == "ceqfpMemoryResFallingThreshold" or name == "ceqfpMemoryResFree" or name == "ceqfpMemoryResFreeOvrflw" or name == "ceqfpMemoryResInUse" or name == "ceqfpMemoryResInUseOvrflw" or name == "ceqfpMemoryResLowFreeWatermark" or name == "ceqfpMemoryResLowFreeWatermarkOvrflw" or name == "ceqfpMemoryResRisingThreshold" or name == "ceqfpMemoryResTotal" or name == "ceqfpMemoryResTotalOvrflw"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResType"):
                    self.ceqfpmemoryrestype = value
                    self.ceqfpmemoryrestype.value_namespace = name_space
                    self.ceqfpmemoryrestype.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryHCResFree"):
                    self.ceqfpmemoryhcresfree = value
                    self.ceqfpmemoryhcresfree.value_namespace = name_space
                    self.ceqfpmemoryhcresfree.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryHCResInUse"):
                    self.ceqfpmemoryhcresinuse = value
                    self.ceqfpmemoryhcresinuse.value_namespace = name_space
                    self.ceqfpmemoryhcresinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryHCResLowFreeWatermark"):
                    self.ceqfpmemoryhcreslowfreewatermark = value
                    self.ceqfpmemoryhcreslowfreewatermark.value_namespace = name_space
                    self.ceqfpmemoryhcreslowfreewatermark.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryHCResTotal"):
                    self.ceqfpmemoryhcrestotal = value
                    self.ceqfpmemoryhcrestotal.value_namespace = name_space
                    self.ceqfpmemoryhcrestotal.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResFallingThreshold"):
                    self.ceqfpmemoryresfallingthreshold = value
                    self.ceqfpmemoryresfallingthreshold.value_namespace = name_space
                    self.ceqfpmemoryresfallingthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResFree"):
                    self.ceqfpmemoryresfree = value
                    self.ceqfpmemoryresfree.value_namespace = name_space
                    self.ceqfpmemoryresfree.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResFreeOvrflw"):
                    self.ceqfpmemoryresfreeovrflw = value
                    self.ceqfpmemoryresfreeovrflw.value_namespace = name_space
                    self.ceqfpmemoryresfreeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResInUse"):
                    self.ceqfpmemoryresinuse = value
                    self.ceqfpmemoryresinuse.value_namespace = name_space
                    self.ceqfpmemoryresinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResInUseOvrflw"):
                    self.ceqfpmemoryresinuseovrflw = value
                    self.ceqfpmemoryresinuseovrflw.value_namespace = name_space
                    self.ceqfpmemoryresinuseovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResLowFreeWatermark"):
                    self.ceqfpmemoryreslowfreewatermark = value
                    self.ceqfpmemoryreslowfreewatermark.value_namespace = name_space
                    self.ceqfpmemoryreslowfreewatermark.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResLowFreeWatermarkOvrflw"):
                    self.ceqfpmemoryreslowfreewatermarkovrflw = value
                    self.ceqfpmemoryreslowfreewatermarkovrflw.value_namespace = name_space
                    self.ceqfpmemoryreslowfreewatermarkovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResRisingThreshold"):
                    self.ceqfpmemoryresrisingthreshold = value
                    self.ceqfpmemoryresrisingthreshold.value_namespace = name_space
                    self.ceqfpmemoryresrisingthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResTotal"):
                    self.ceqfpmemoryrestotal = value
                    self.ceqfpmemoryrestotal.value_namespace = name_space
                    self.ceqfpmemoryrestotal.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpMemoryResTotalOvrflw"):
                    self.ceqfpmemoryrestotalovrflw = value
                    self.ceqfpmemoryrestotalovrflw.value_namespace = name_space
                    self.ceqfpmemoryrestotalovrflw.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceqfpmemoryresourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceqfpmemoryresourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceqfpMemoryResourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceqfpMemoryResourceEntry"):
                for c in self.ceqfpmemoryresourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceqfpmemoryresourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpMemoryResourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceqfpthroughputtable(Entity):
        """
        This table maintains the throughput information for each
        QFP physical entity.
        
                An agent creates a conceptual row to this table
        corresponding to a QFP physical entity upon detection of a
        physical entity supporting the QFP throughput information.
        
                An agent destroys a conceptual row from this table     
        
        corresponding to a QFP physical entity upon removal of the QFP
        host physical entity.
        
        .. attribute:: ceqfpthroughputentry
        
        	A conceptual row in the ceqfpThroughputTable. There is an entry in this table for each QFP entity, as defined by a value of entPhysicalIndex
        	**type**\: list of    :py:class:`Ceqfpthroughputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CiscoEntityQfpMib.Ceqfpthroughputtable, self).__init__()

            self.yang_name = "ceqfpThroughputTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"

            self.ceqfpthroughputentry = YList(self)

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
                        super(CiscoEntityQfpMib.Ceqfpthroughputtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityQfpMib.Ceqfpthroughputtable, self).__setattr__(name, value)


        class Ceqfpthroughputentry(Entity):
            """
            A conceptual row in the ceqfpThroughputTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpthroughputavgrate
            
            	The object represents the average throughput rate in the interval ceqfpThroughputInterval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfpthroughputinterval
            
            	The object represents the configured time interval at which the ceqfpThroughputLevel is checked
            	**type**\:  int
            
            	**range:** 10..86400
            
            	**units**\: seconds
            
            .. attribute:: ceqfpthroughputlevel
            
            	This object represents the current throughput level for installed throughput license.                  normal  (1) \- Throughput usage is normal                 warning (2) \- Throughput usage has crossed the                               configured threshold limit                 exceed  (3) \- Throughput usage has exceeded the                               total licensed bandwidth
            	**type**\:   :py:class:`Ceqfpthroughputlevel <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry.Ceqfpthroughputlevel>`
            
            .. attribute:: ceqfpthroughputlicensedbw
            
            	This object represents the bandwidth for installed throughput license
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfpthroughputthreshold
            
            	The object represents the configured throughput threshold
            	**type**\:  int
            
            	**range:** 75..95
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                super(CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry, self).__init__()

                self.yang_name = "ceqfpThroughputEntry"
                self.yang_parent_name = "ceqfpThroughputTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpthroughputavgrate = YLeaf(YType.uint64, "ceqfpThroughputAvgRate")

                self.ceqfpthroughputinterval = YLeaf(YType.int32, "ceqfpThroughputInterval")

                self.ceqfpthroughputlevel = YLeaf(YType.enumeration, "ceqfpThroughputLevel")

                self.ceqfpthroughputlicensedbw = YLeaf(YType.uint64, "ceqfpThroughputLicensedBW")

                self.ceqfpthroughputthreshold = YLeaf(YType.int32, "ceqfpThroughputThreshold")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceqfpthroughputavgrate",
                                "ceqfpthroughputinterval",
                                "ceqfpthroughputlevel",
                                "ceqfpthroughputlicensedbw",
                                "ceqfpthroughputthreshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry, self).__setattr__(name, value)

            class Ceqfpthroughputlevel(Enum):
                """
                Ceqfpthroughputlevel

                This object represents the current throughput level for

                installed throughput license.

                                normal  (1) \- Throughput usage is normal

                                warning (2) \- Throughput usage has crossed the

                                              configured threshold limit

                                exceed  (3) \- Throughput usage has exceeded the

                                              total licensed bandwidth

                .. data:: normal = 1

                .. data:: warning = 2

                .. data:: exceed = 3

                """

                normal = Enum.YLeaf(1, "normal")

                warning = Enum.YLeaf(2, "warning")

                exceed = Enum.YLeaf(3, "exceed")


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceqfpthroughputavgrate.is_set or
                    self.ceqfpthroughputinterval.is_set or
                    self.ceqfpthroughputlevel.is_set or
                    self.ceqfpthroughputlicensedbw.is_set or
                    self.ceqfpthroughputthreshold.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceqfpthroughputavgrate.yfilter != YFilter.not_set or
                    self.ceqfpthroughputinterval.yfilter != YFilter.not_set or
                    self.ceqfpthroughputlevel.yfilter != YFilter.not_set or
                    self.ceqfpthroughputlicensedbw.yfilter != YFilter.not_set or
                    self.ceqfpthroughputthreshold.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceqfpThroughputEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpThroughputTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceqfpthroughputavgrate.is_set or self.ceqfpthroughputavgrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpthroughputavgrate.get_name_leafdata())
                if (self.ceqfpthroughputinterval.is_set or self.ceqfpthroughputinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpthroughputinterval.get_name_leafdata())
                if (self.ceqfpthroughputlevel.is_set or self.ceqfpthroughputlevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpthroughputlevel.get_name_leafdata())
                if (self.ceqfpthroughputlicensedbw.is_set or self.ceqfpthroughputlicensedbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpthroughputlicensedbw.get_name_leafdata())
                if (self.ceqfpthroughputthreshold.is_set or self.ceqfpthroughputthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceqfpthroughputthreshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceqfpThroughputAvgRate" or name == "ceqfpThroughputInterval" or name == "ceqfpThroughputLevel" or name == "ceqfpThroughputLicensedBW" or name == "ceqfpThroughputThreshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpThroughputAvgRate"):
                    self.ceqfpthroughputavgrate = value
                    self.ceqfpthroughputavgrate.value_namespace = name_space
                    self.ceqfpthroughputavgrate.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpThroughputInterval"):
                    self.ceqfpthroughputinterval = value
                    self.ceqfpthroughputinterval.value_namespace = name_space
                    self.ceqfpthroughputinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpThroughputLevel"):
                    self.ceqfpthroughputlevel = value
                    self.ceqfpthroughputlevel.value_namespace = name_space
                    self.ceqfpthroughputlevel.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpThroughputLicensedBW"):
                    self.ceqfpthroughputlicensedbw = value
                    self.ceqfpthroughputlicensedbw.value_namespace = name_space
                    self.ceqfpthroughputlicensedbw.value_namespace_prefix = name_space_prefix
                if(value_path == "ceqfpThroughputThreshold"):
                    self.ceqfpthroughputthreshold = value
                    self.ceqfpthroughputthreshold.value_namespace = name_space
                    self.ceqfpthroughputthreshold.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceqfpthroughputentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceqfpthroughputentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceqfpThroughputTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceqfpThroughputEntry"):
                for c in self.ceqfpthroughputentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceqfpthroughputentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceqfpThroughputEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ceqfpmemoryresourcetable is not None and self.ceqfpmemoryresourcetable.has_data()) or
            (self.ceqfpsystemtable is not None and self.ceqfpsystemtable.has_data()) or
            (self.ceqfpthroughputtable is not None and self.ceqfpthroughputtable.has_data()) or
            (self.ceqfputilizationtable is not None and self.ceqfputilizationtable.has_data()) or
            (self.ciscoentityqfp is not None and self.ciscoentityqfp.has_data()) or
            (self.ciscoentityqfpnotif is not None and self.ciscoentityqfpnotif.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ceqfpmemoryresourcetable is not None and self.ceqfpmemoryresourcetable.has_operation()) or
            (self.ceqfpsystemtable is not None and self.ceqfpsystemtable.has_operation()) or
            (self.ceqfpthroughputtable is not None and self.ceqfpthroughputtable.has_operation()) or
            (self.ceqfputilizationtable is not None and self.ceqfputilizationtable.has_operation()) or
            (self.ciscoentityqfp is not None and self.ciscoentityqfp.has_operation()) or
            (self.ciscoentityqfpnotif is not None and self.ciscoentityqfpnotif.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB" + path_buffer

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

        if (child_yang_name == "ceqfpMemoryResourceTable"):
            if (self.ceqfpmemoryresourcetable is None):
                self.ceqfpmemoryresourcetable = CiscoEntityQfpMib.Ceqfpmemoryresourcetable()
                self.ceqfpmemoryresourcetable.parent = self
                self._children_name_map["ceqfpmemoryresourcetable"] = "ceqfpMemoryResourceTable"
            return self.ceqfpmemoryresourcetable

        if (child_yang_name == "ceqfpSystemTable"):
            if (self.ceqfpsystemtable is None):
                self.ceqfpsystemtable = CiscoEntityQfpMib.Ceqfpsystemtable()
                self.ceqfpsystemtable.parent = self
                self._children_name_map["ceqfpsystemtable"] = "ceqfpSystemTable"
            return self.ceqfpsystemtable

        if (child_yang_name == "ceqfpThroughputTable"):
            if (self.ceqfpthroughputtable is None):
                self.ceqfpthroughputtable = CiscoEntityQfpMib.Ceqfpthroughputtable()
                self.ceqfpthroughputtable.parent = self
                self._children_name_map["ceqfpthroughputtable"] = "ceqfpThroughputTable"
            return self.ceqfpthroughputtable

        if (child_yang_name == "ceqfpUtilizationTable"):
            if (self.ceqfputilizationtable is None):
                self.ceqfputilizationtable = CiscoEntityQfpMib.Ceqfputilizationtable()
                self.ceqfputilizationtable.parent = self
                self._children_name_map["ceqfputilizationtable"] = "ceqfpUtilizationTable"
            return self.ceqfputilizationtable

        if (child_yang_name == "ciscoEntityQfp"):
            if (self.ciscoentityqfp is None):
                self.ciscoentityqfp = CiscoEntityQfpMib.Ciscoentityqfp()
                self.ciscoentityqfp.parent = self
                self._children_name_map["ciscoentityqfp"] = "ciscoEntityQfp"
            return self.ciscoentityqfp

        if (child_yang_name == "ciscoEntityQfpNotif"):
            if (self.ciscoentityqfpnotif is None):
                self.ciscoentityqfpnotif = CiscoEntityQfpMib.Ciscoentityqfpnotif()
                self.ciscoentityqfpnotif.parent = self
                self._children_name_map["ciscoentityqfpnotif"] = "ciscoEntityQfpNotif"
            return self.ciscoentityqfpnotif

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ceqfpMemoryResourceTable" or name == "ceqfpSystemTable" or name == "ceqfpThroughputTable" or name == "ceqfpUtilizationTable" or name == "ciscoEntityQfp" or name == "ciscoEntityQfpNotif"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEntityQfpMib()
        return self._top_entity

