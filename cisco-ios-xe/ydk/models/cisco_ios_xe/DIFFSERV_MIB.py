""" DIFFSERV_MIB 

This MIB defines the objects necessary to manage a device that
uses the Differentiated Services Architecture described in RFC
2475. The Conceptual Model of a Differentiated Services Router
provides supporting information on how such a router is modeled.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ifdirection(Enum):
    """
    Ifdirection

    IfDirection specifies a direction of data travel on an

    interface. 'inbound' traffic is operated on during reception from

    the interface, while 'outbound' traffic is operated on prior to

    transmission on the interface.

    .. data:: inbound = 1

    .. data:: outbound = 2

    """

    inbound = Enum.YLeaf(1, "inbound")

    outbound = Enum.YLeaf(2, "outbound")



class Diffservtbparamtswtcm(Identity):
    """
    Time Sliding Window Three Color Marker Metering as defined by
    RFC 2859.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamtswtcm, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamTswTCM")


class Diffservtbparamsrtcmblind(Identity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamsrtcmblind, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamSrTCMBlind")


class Diffservschedulerpriority(Identity):
    """
    For use with diffServSchedulerMethod to indicate the Priority
    scheduling method.  This is defined as an algorithm in which the
    presence of data in a queue or set of queues absolutely precludes
    dequeue from another queue or set of queues of lower priority.
    Note that attributes from diffServMinRateEntry of the
    queues/schedulers feeding this scheduler are used when
    determining the next packet to schedule.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservschedulerpriority, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServSchedulerPriority")


class Diffservtbparamavgrate(Identity):
    """
    Average Rate Meter as described in the Informal Differentiated
    Services Model section 5.2.1.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamavgrate, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamAvgRate")


class Diffservschedulerwfq(Identity):
    """
    For use with diffServSchedulerMethod to indicate the Weighted
    Fair Queuing scheduling method, defined as any algorithm in which
    a set of queues are conceptually visited in some order, to
    implement an average output rate by class. Notice attributes from
    diffServMinRateEntry of the queues/schedulers feeding this
    scheduler are used when determining the next packet to schedule.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservschedulerwfq, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServSchedulerWFQ")


class Diffservtbparamtrtcmaware(Identity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamtrtcmaware, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamTrTCMAware")


class Diffservschedulerwrr(Identity):
    """
    For use with diffServSchedulerMethod to indicate the Weighted
    Round Robin scheduling method, defined as any algorithm in which
    a set of queues are visited in a fixed order, and varying amounts
    of traffic are removed from each queue in turn to implement an
    average output rate by class. Notice attributes from
    diffServMinRateEntry of the queues/schedulers feeding this
    scheduler are used when determining the next packet to schedule.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservschedulerwrr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServSchedulerWRR")


class Diffservtbparamtrtcmblind(Identity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamtrtcmblind, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamTrTCMBlind")


class Diffservtbparamsimpletokenbucket(Identity):
    """
    Two Parameter Token Bucket Meter as described in the Informal
    Differentiated Services Model section 5.2.3.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamsimpletokenbucket, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamSimpleTokenBucket")


class Diffservtbparamsrtcmaware(Identity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(Diffservtbparamsrtcmaware, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", "DIFFSERV-MIB", "DIFFSERV-MIB:diffServTBParamSrTCMAware")


class DiffservMib(Entity):
    """
    
    
    .. attribute:: diffservaction
    
    	
    	**type**\:   :py:class:`Diffservaction <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservaction>`
    
    .. attribute:: diffservactiontable
    
    	The Action Table enumerates actions that can be performed to a stream of traffic. Multiple actions can be concatenated. For example, traffic exiting from a meter may be counted, marked, and potentially dropped before entering a queue.  Specific actions are indicated by diffServActionSpecific which points to an entry of a specific action type parameterizing the action in detail
    	**type**\:   :py:class:`Diffservactiontable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservactiontable>`
    
    .. attribute:: diffservalgdrop
    
    	
    	**type**\:   :py:class:`Diffservalgdrop <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservalgdrop>`
    
    .. attribute:: diffservalgdroptable
    
    	The algorithmic drop table contains entries describing an element that drops packets according to some algorithm
    	**type**\:   :py:class:`Diffservalgdroptable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservalgdroptable>`
    
    .. attribute:: diffservclassifier
    
    	
    	**type**\:   :py:class:`Diffservclassifier <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclassifier>`
    
    .. attribute:: diffservclfrelementtable
    
    	The classifier element table enumerates the relationship between classification patterns and subsequent downstream Differentiated Services Functional Data Path elements. diffServClfrElementSpecific points to a filter that specifies the classification parameters. A classifier may use filter tables of different types together.  One example of a filter table defined in this MIB is diffServMultiFieldClfrTable, for IP Multi\-Field Classifiers (MFCs). Such an entry might identify anything from a single micro\-flow (an identifiable sub\-session packet stream directed from one sending transport to the receiving transport or transports), or aggregates of those such as the traffic from a host, traffic for an application, or traffic between two hosts using an application and a given DSCP. The standard Behavior Aggregate used in the Differentiated Services Architecture is encoded as a degenerate case of such an aggregate \- the traffic using a particular DSCP value.  Filter tables for other filter types may be defined elsewhere
    	**type**\:   :py:class:`Diffservclfrelementtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclfrelementtable>`
    
    .. attribute:: diffservclfrtable
    
    	This table enumerates all the diffserv classifier functional data path elements of this device.  The actual classification definitions are defined in diffServClfrElementTable entries belonging to each classifier.  An entry in this table, pointed to by a RowPointer specifying an instance of diffServClfrStatus, is frequently used as the name for a set of classifier elements, which all use the index diffServClfrId. Per the semantics of the classifier element table, these entries constitute one or more unordered sets of tests which may be simultaneously applied to a message to    classify it.  The primary function of this table is to ensure that the value of diffServClfrId is unique before attempting to use it in creating a diffServClfrElementEntry. Therefore, the diffServClfrEntry must be created on the same SET as the diffServClfrElementEntry, or before the diffServClfrElementEntry is created
    	**type**\:   :py:class:`Diffservclfrtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclfrtable>`
    
    .. attribute:: diffservcountacttable
    
    	This table contains counters for all the traffic passing through an action element
    	**type**\:   :py:class:`Diffservcountacttable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservcountacttable>`
    
    .. attribute:: diffservdatapathtable
    
    	The data path table contains RowPointers indicating the start of the functional data path for each interface and traffic direction in this device. These may merge, or be separated into parallel data paths
    	**type**\:   :py:class:`Diffservdatapathtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservdatapathtable>`
    
    .. attribute:: diffservdscpmarkacttable
    
    	This table enumerates specific DSCPs used for marking or remarking the DSCP field of IP packets. The entries of this table may be referenced by a diffServActionSpecific attribute
    	**type**\:   :py:class:`Diffservdscpmarkacttable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservdscpmarkacttable>`
    
    .. attribute:: diffservmaxratetable
    
    	The Maximum Rate Parameter Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\:   :py:class:`Diffservmaxratetable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmaxratetable>`
    
    .. attribute:: diffservmeter
    
    	
    	**type**\:   :py:class:`Diffservmeter <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmeter>`
    
    .. attribute:: diffservmetertable
    
    	This table enumerates specific meters that a system may use to police a stream of traffic. The traffic stream to be metered is determined by the Differentiated Services Functional Data Path Element(s) upstream of the meter i.e. by the object(s) that point to each entry in this table.  This may include all traffic on an interface.  Specific meter details are to be found in table entry referenced by diffServMeterSpecific
    	**type**\:   :py:class:`Diffservmetertable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmetertable>`
    
    .. attribute:: diffservminratetable
    
    	The Minimum Rate Parameters Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\:   :py:class:`Diffservminratetable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservminratetable>`
    
    .. attribute:: diffservmultifieldclfrtable
    
    	A table of IP Multi\-field Classifier filter entries that a    system may use to identify IP traffic
    	**type**\:   :py:class:`Diffservmultifieldclfrtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmultifieldclfrtable>`
    
    .. attribute:: diffservqtable
    
    	The Queue Table enumerates the individual queues.  Note that the MIB models queuing systems as composed of individual queues, one per class of traffic, even though they may in fact be structured as classes of traffic scheduled using a common calendar queue, or in other ways
    	**type**\:   :py:class:`Diffservqtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservqtable>`
    
    .. attribute:: diffservqueue
    
    	
    	**type**\:   :py:class:`Diffservqueue <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservqueue>`
    
    .. attribute:: diffservrandomdroptable
    
    	The random drop table contains entries describing a process that drops packets randomly. Entries in this table are pointed to by diffServAlgDropSpecific
    	**type**\:   :py:class:`Diffservrandomdroptable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservrandomdroptable>`
    
    .. attribute:: diffservscheduler
    
    	
    	**type**\:   :py:class:`Diffservscheduler <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservscheduler>`
    
    .. attribute:: diffservschedulertable
    
    	The Scheduler Table enumerates packet schedulers. Multiple scheduling algorithms can be used on a given data path, with each algorithm described by one diffServSchedulerEntry
    	**type**\:   :py:class:`Diffservschedulertable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservschedulertable>`
    
    .. attribute:: diffservtbparam
    
    	
    	**type**\:   :py:class:`Diffservtbparam <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservtbparam>`
    
    .. attribute:: diffservtbparamtable
    
    	This table enumerates a single set of token bucket meter parameters that a system may use to police a stream of traffic. Such meters are modeled here as having a single rate and a single burst size. Multiple entries are used when multiple rates/burst sizes are needed
    	**type**\:   :py:class:`Diffservtbparamtable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservtbparamtable>`
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(DiffservMib, self).__init__()
        self._top_entity = None

        self.yang_name = "DIFFSERV-MIB"
        self.yang_parent_name = "DIFFSERV-MIB"

        self.diffservaction = DiffservMib.Diffservaction()
        self.diffservaction.parent = self
        self._children_name_map["diffservaction"] = "diffServAction"
        self._children_yang_names.add("diffServAction")

        self.diffservactiontable = DiffservMib.Diffservactiontable()
        self.diffservactiontable.parent = self
        self._children_name_map["diffservactiontable"] = "diffServActionTable"
        self._children_yang_names.add("diffServActionTable")

        self.diffservalgdrop = DiffservMib.Diffservalgdrop()
        self.diffservalgdrop.parent = self
        self._children_name_map["diffservalgdrop"] = "diffServAlgDrop"
        self._children_yang_names.add("diffServAlgDrop")

        self.diffservalgdroptable = DiffservMib.Diffservalgdroptable()
        self.diffservalgdroptable.parent = self
        self._children_name_map["diffservalgdroptable"] = "diffServAlgDropTable"
        self._children_yang_names.add("diffServAlgDropTable")

        self.diffservclassifier = DiffservMib.Diffservclassifier()
        self.diffservclassifier.parent = self
        self._children_name_map["diffservclassifier"] = "diffServClassifier"
        self._children_yang_names.add("diffServClassifier")

        self.diffservclfrelementtable = DiffservMib.Diffservclfrelementtable()
        self.diffservclfrelementtable.parent = self
        self._children_name_map["diffservclfrelementtable"] = "diffServClfrElementTable"
        self._children_yang_names.add("diffServClfrElementTable")

        self.diffservclfrtable = DiffservMib.Diffservclfrtable()
        self.diffservclfrtable.parent = self
        self._children_name_map["diffservclfrtable"] = "diffServClfrTable"
        self._children_yang_names.add("diffServClfrTable")

        self.diffservcountacttable = DiffservMib.Diffservcountacttable()
        self.diffservcountacttable.parent = self
        self._children_name_map["diffservcountacttable"] = "diffServCountActTable"
        self._children_yang_names.add("diffServCountActTable")

        self.diffservdatapathtable = DiffservMib.Diffservdatapathtable()
        self.diffservdatapathtable.parent = self
        self._children_name_map["diffservdatapathtable"] = "diffServDataPathTable"
        self._children_yang_names.add("diffServDataPathTable")

        self.diffservdscpmarkacttable = DiffservMib.Diffservdscpmarkacttable()
        self.diffservdscpmarkacttable.parent = self
        self._children_name_map["diffservdscpmarkacttable"] = "diffServDscpMarkActTable"
        self._children_yang_names.add("diffServDscpMarkActTable")

        self.diffservmaxratetable = DiffservMib.Diffservmaxratetable()
        self.diffservmaxratetable.parent = self
        self._children_name_map["diffservmaxratetable"] = "diffServMaxRateTable"
        self._children_yang_names.add("diffServMaxRateTable")

        self.diffservmeter = DiffservMib.Diffservmeter()
        self.diffservmeter.parent = self
        self._children_name_map["diffservmeter"] = "diffServMeter"
        self._children_yang_names.add("diffServMeter")

        self.diffservmetertable = DiffservMib.Diffservmetertable()
        self.diffservmetertable.parent = self
        self._children_name_map["diffservmetertable"] = "diffServMeterTable"
        self._children_yang_names.add("diffServMeterTable")

        self.diffservminratetable = DiffservMib.Diffservminratetable()
        self.diffservminratetable.parent = self
        self._children_name_map["diffservminratetable"] = "diffServMinRateTable"
        self._children_yang_names.add("diffServMinRateTable")

        self.diffservmultifieldclfrtable = DiffservMib.Diffservmultifieldclfrtable()
        self.diffservmultifieldclfrtable.parent = self
        self._children_name_map["diffservmultifieldclfrtable"] = "diffServMultiFieldClfrTable"
        self._children_yang_names.add("diffServMultiFieldClfrTable")

        self.diffservqtable = DiffservMib.Diffservqtable()
        self.diffservqtable.parent = self
        self._children_name_map["diffservqtable"] = "diffServQTable"
        self._children_yang_names.add("diffServQTable")

        self.diffservqueue = DiffservMib.Diffservqueue()
        self.diffservqueue.parent = self
        self._children_name_map["diffservqueue"] = "diffServQueue"
        self._children_yang_names.add("diffServQueue")

        self.diffservrandomdroptable = DiffservMib.Diffservrandomdroptable()
        self.diffservrandomdroptable.parent = self
        self._children_name_map["diffservrandomdroptable"] = "diffServRandomDropTable"
        self._children_yang_names.add("diffServRandomDropTable")

        self.diffservscheduler = DiffservMib.Diffservscheduler()
        self.diffservscheduler.parent = self
        self._children_name_map["diffservscheduler"] = "diffServScheduler"
        self._children_yang_names.add("diffServScheduler")

        self.diffservschedulertable = DiffservMib.Diffservschedulertable()
        self.diffservschedulertable.parent = self
        self._children_name_map["diffservschedulertable"] = "diffServSchedulerTable"
        self._children_yang_names.add("diffServSchedulerTable")

        self.diffservtbparam = DiffservMib.Diffservtbparam()
        self.diffservtbparam.parent = self
        self._children_name_map["diffservtbparam"] = "diffServTBParam"
        self._children_yang_names.add("diffServTBParam")

        self.diffservtbparamtable = DiffservMib.Diffservtbparamtable()
        self.diffservtbparamtable.parent = self
        self._children_name_map["diffservtbparamtable"] = "diffServTBParamTable"
        self._children_yang_names.add("diffServTBParamTable")


    class Diffservclassifier(Entity):
        """
        
        
        .. attribute:: diffservclfrelementnextfree
        
        	This object contains an unused value for diffServClfrElementId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservclfrnextfree
        
        	This object contains an unused value for diffServClfrId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservmultifieldclfrnextfree
        
        	This object contains an unused value for diffServMultiFieldClfrId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservclassifier, self).__init__()

            self.yang_name = "diffServClassifier"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservclfrelementnextfree = YLeaf(YType.uint32, "diffServClfrElementNextFree")

            self.diffservclfrnextfree = YLeaf(YType.uint32, "diffServClfrNextFree")

            self.diffservmultifieldclfrnextfree = YLeaf(YType.uint32, "diffServMultiFieldClfrNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservclfrelementnextfree",
                            "diffservclfrnextfree",
                            "diffservmultifieldclfrnextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservclassifier, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservclassifier, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.diffservclfrelementnextfree.is_set or
                self.diffservclfrnextfree.is_set or
                self.diffservmultifieldclfrnextfree.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservclfrelementnextfree.yfilter != YFilter.not_set or
                self.diffservclfrnextfree.yfilter != YFilter.not_set or
                self.diffservmultifieldclfrnextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServClassifier" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservclfrelementnextfree.is_set or self.diffservclfrelementnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservclfrelementnextfree.get_name_leafdata())
            if (self.diffservclfrnextfree.is_set or self.diffservclfrnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservclfrnextfree.get_name_leafdata())
            if (self.diffservmultifieldclfrnextfree.is_set or self.diffservmultifieldclfrnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservmultifieldclfrnextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServClfrElementNextFree" or name == "diffServClfrNextFree" or name == "diffServMultiFieldClfrNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServClfrElementNextFree"):
                self.diffservclfrelementnextfree = value
                self.diffservclfrelementnextfree.value_namespace = name_space
                self.diffservclfrelementnextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServClfrNextFree"):
                self.diffservclfrnextfree = value
                self.diffservclfrnextfree.value_namespace = name_space
                self.diffservclfrnextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServMultiFieldClfrNextFree"):
                self.diffservmultifieldclfrnextfree = value
                self.diffservmultifieldclfrnextfree.value_namespace = name_space
                self.diffservmultifieldclfrnextfree.value_namespace_prefix = name_space_prefix


    class Diffservmeter(Entity):
        """
        
        
        .. attribute:: diffservmeternextfree
        
        	This object contains an unused value for diffServMeterId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservmeter, self).__init__()

            self.yang_name = "diffServMeter"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservmeternextfree = YLeaf(YType.uint32, "diffServMeterNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservmeternextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservmeter, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservmeter, self).__setattr__(name, value)

        def has_data(self):
            return self.diffservmeternextfree.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservmeternextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServMeter" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservmeternextfree.is_set or self.diffservmeternextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservmeternextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMeterNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServMeterNextFree"):
                self.diffservmeternextfree = value
                self.diffservmeternextfree.value_namespace = name_space
                self.diffservmeternextfree.value_namespace_prefix = name_space_prefix


    class Diffservtbparam(Entity):
        """
        
        
        .. attribute:: diffservtbparamnextfree
        
        	This object contains an unused value for diffServTBParamId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservtbparam, self).__init__()

            self.yang_name = "diffServTBParam"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservtbparamnextfree = YLeaf(YType.uint32, "diffServTBParamNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservtbparamnextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservtbparam, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservtbparam, self).__setattr__(name, value)

        def has_data(self):
            return self.diffservtbparamnextfree.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservtbparamnextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServTBParam" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservtbparamnextfree.is_set or self.diffservtbparamnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservtbparamnextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServTBParamNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServTBParamNextFree"):
                self.diffservtbparamnextfree = value
                self.diffservtbparamnextfree.value_namespace = name_space
                self.diffservtbparamnextfree.value_namespace_prefix = name_space_prefix


    class Diffservaction(Entity):
        """
        
        
        .. attribute:: diffservactionnextfree
        
        	This object contains an unused value for diffServActionId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservcountactnextfree
        
        	This object contains an unused value for diffServCountActId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservaction, self).__init__()

            self.yang_name = "diffServAction"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservactionnextfree = YLeaf(YType.uint32, "diffServActionNextFree")

            self.diffservcountactnextfree = YLeaf(YType.uint32, "diffServCountActNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservactionnextfree",
                            "diffservcountactnextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservaction, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservaction, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.diffservactionnextfree.is_set or
                self.diffservcountactnextfree.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservactionnextfree.yfilter != YFilter.not_set or
                self.diffservcountactnextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServAction" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservactionnextfree.is_set or self.diffservactionnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservactionnextfree.get_name_leafdata())
            if (self.diffservcountactnextfree.is_set or self.diffservcountactnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservcountactnextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServActionNextFree" or name == "diffServCountActNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServActionNextFree"):
                self.diffservactionnextfree = value
                self.diffservactionnextfree.value_namespace = name_space
                self.diffservactionnextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServCountActNextFree"):
                self.diffservcountactnextfree = value
                self.diffservcountactnextfree.value_namespace = name_space
                self.diffservcountactnextfree.value_namespace_prefix = name_space_prefix


    class Diffservalgdrop(Entity):
        """
        
        
        .. attribute:: diffservalgdropnextfree
        
        	This object contains an unused value for diffServAlgDropId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservrandomdropnextfree
        
        	This object contains an unused value for diffServRandomDropId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservalgdrop, self).__init__()

            self.yang_name = "diffServAlgDrop"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservalgdropnextfree = YLeaf(YType.uint32, "diffServAlgDropNextFree")

            self.diffservrandomdropnextfree = YLeaf(YType.uint32, "diffServRandomDropNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservalgdropnextfree",
                            "diffservrandomdropnextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservalgdrop, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservalgdrop, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.diffservalgdropnextfree.is_set or
                self.diffservrandomdropnextfree.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservalgdropnextfree.yfilter != YFilter.not_set or
                self.diffservrandomdropnextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServAlgDrop" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservalgdropnextfree.is_set or self.diffservalgdropnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservalgdropnextfree.get_name_leafdata())
            if (self.diffservrandomdropnextfree.is_set or self.diffservrandomdropnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservrandomdropnextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServAlgDropNextFree" or name == "diffServRandomDropNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServAlgDropNextFree"):
                self.diffservalgdropnextfree = value
                self.diffservalgdropnextfree.value_namespace = name_space
                self.diffservalgdropnextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServRandomDropNextFree"):
                self.diffservrandomdropnextfree = value
                self.diffservrandomdropnextfree.value_namespace = name_space
                self.diffservrandomdropnextfree.value_namespace_prefix = name_space_prefix


    class Diffservqueue(Entity):
        """
        
        
        .. attribute:: diffservqnextfree
        
        	This object contains an unused value for diffServQId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservqueue, self).__init__()

            self.yang_name = "diffServQueue"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservqnextfree = YLeaf(YType.uint32, "diffServQNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservqnextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservqueue, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservqueue, self).__setattr__(name, value)

        def has_data(self):
            return self.diffservqnextfree.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservqnextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServQueue" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservqnextfree.is_set or self.diffservqnextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservqnextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServQNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServQNextFree"):
                self.diffservqnextfree = value
                self.diffservqnextfree.value_namespace = name_space
                self.diffservqnextfree.value_namespace_prefix = name_space_prefix


    class Diffservscheduler(Entity):
        """
        
        
        .. attribute:: diffservmaxratenextfree
        
        	This object contains an unused value for diffServMaxRateId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservminratenextfree
        
        	This object contains an unused value for diffServMinRateId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservschedulernextfree
        
        	This object contains an unused value for diffServSchedulerId, or a zero to indicate that none exist
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservscheduler, self).__init__()

            self.yang_name = "diffServScheduler"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservmaxratenextfree = YLeaf(YType.uint32, "diffServMaxRateNextFree")

            self.diffservminratenextfree = YLeaf(YType.uint32, "diffServMinRateNextFree")

            self.diffservschedulernextfree = YLeaf(YType.uint32, "diffServSchedulerNextFree")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diffservmaxratenextfree",
                            "diffservminratenextfree",
                            "diffservschedulernextfree") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DiffservMib.Diffservscheduler, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservscheduler, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.diffservmaxratenextfree.is_set or
                self.diffservminratenextfree.is_set or
                self.diffservschedulernextfree.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diffservmaxratenextfree.yfilter != YFilter.not_set or
                self.diffservminratenextfree.yfilter != YFilter.not_set or
                self.diffservschedulernextfree.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServScheduler" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diffservmaxratenextfree.is_set or self.diffservmaxratenextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservmaxratenextfree.get_name_leafdata())
            if (self.diffservminratenextfree.is_set or self.diffservminratenextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservminratenextfree.get_name_leafdata())
            if (self.diffservschedulernextfree.is_set or self.diffservschedulernextfree.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diffservschedulernextfree.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMaxRateNextFree" or name == "diffServMinRateNextFree" or name == "diffServSchedulerNextFree"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diffServMaxRateNextFree"):
                self.diffservmaxratenextfree = value
                self.diffservmaxratenextfree.value_namespace = name_space
                self.diffservmaxratenextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServMinRateNextFree"):
                self.diffservminratenextfree = value
                self.diffservminratenextfree.value_namespace = name_space
                self.diffservminratenextfree.value_namespace_prefix = name_space_prefix
            if(value_path == "diffServSchedulerNextFree"):
                self.diffservschedulernextfree = value
                self.diffservschedulernextfree.value_namespace = name_space
                self.diffservschedulernextfree.value_namespace_prefix = name_space_prefix


    class Diffservdatapathtable(Entity):
        """
        The data path table contains RowPointers indicating the start of
        the functional data path for each interface and traffic direction
        in this device. These may merge, or be separated into parallel
        data paths.
        
        .. attribute:: diffservdatapathentry
        
        	An entry in the data path table indicates the start of a single Differentiated Services Functional Data Path in this device.  These are associated with individual interfaces, logical or physical, and therefore are instantiated by ifIndex. Therefore, the interface index must have been assigned, according to the procedures applicable to that, before it can be meaningfully used. Generally, this means that the interface must exist.  When diffServDataPathStorage is of type nonVolatile, however, this may reflect the configuration for an interface whose ifIndex has been assigned but for which the supporting implementation is not currently present
        	**type**\: list of    :py:class:`Diffservdatapathentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservdatapathtable.Diffservdatapathentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservdatapathtable, self).__init__()

            self.yang_name = "diffServDataPathTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservdatapathentry = YList(self)

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
                        super(DiffservMib.Diffservdatapathtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservdatapathtable, self).__setattr__(name, value)


        class Diffservdatapathentry(Entity):
            """
            An entry in the data path table indicates the start of a single
            Differentiated Services Functional Data Path in this device.
            
            These are associated with individual interfaces, logical or
            physical, and therefore are instantiated by ifIndex. Therefore,
            the interface index must have been assigned, according to the
            procedures applicable to that, before it can be meaningfully
            used. Generally, this means that the interface must exist.
            
            When diffServDataPathStorage is of type nonVolatile, however,
            this may reflect the configuration for an interface whose ifIndex
            has been assigned but for which the supporting implementation is
            not currently present.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: diffservdatapathifdirection  <key>
            
            	IfDirection specifies whether the reception or transmission path for this interface is in view
            	**type**\:   :py:class:`Ifdirection <ydk.models.cisco_ios_xe.DIFFSERV_MIB.Ifdirection>`
            
            .. attribute:: diffservdatapathstart
            
            	This selects the first Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no Differentiated Services treatment is performed on traffic of this data path. A pointer with the value zeroDotZero normally terminates a functional data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservdatapathstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservdatapathstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservdatapathtable.Diffservdatapathentry, self).__init__()

                self.yang_name = "diffServDataPathEntry"
                self.yang_parent_name = "diffServDataPathTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.diffservdatapathifdirection = YLeaf(YType.enumeration, "diffServDataPathIfDirection")

                self.diffservdatapathstart = YLeaf(YType.str, "diffServDataPathStart")

                self.diffservdatapathstatus = YLeaf(YType.enumeration, "diffServDataPathStatus")

                self.diffservdatapathstorage = YLeaf(YType.enumeration, "diffServDataPathStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "diffservdatapathifdirection",
                                "diffservdatapathstart",
                                "diffservdatapathstatus",
                                "diffservdatapathstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservdatapathtable.Diffservdatapathentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservdatapathtable.Diffservdatapathentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.diffservdatapathifdirection.is_set or
                    self.diffservdatapathstart.is_set or
                    self.diffservdatapathstatus.is_set or
                    self.diffservdatapathstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.diffservdatapathifdirection.yfilter != YFilter.not_set or
                    self.diffservdatapathstart.yfilter != YFilter.not_set or
                    self.diffservdatapathstatus.yfilter != YFilter.not_set or
                    self.diffservdatapathstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServDataPathEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[diffServDataPathIfDirection='" + self.diffservdatapathifdirection.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServDataPathTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.diffservdatapathifdirection.is_set or self.diffservdatapathifdirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservdatapathifdirection.get_name_leafdata())
                if (self.diffservdatapathstart.is_set or self.diffservdatapathstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservdatapathstart.get_name_leafdata())
                if (self.diffservdatapathstatus.is_set or self.diffservdatapathstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservdatapathstatus.get_name_leafdata())
                if (self.diffservdatapathstorage.is_set or self.diffservdatapathstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservdatapathstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "diffServDataPathIfDirection" or name == "diffServDataPathStart" or name == "diffServDataPathStatus" or name == "diffServDataPathStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServDataPathIfDirection"):
                    self.diffservdatapathifdirection = value
                    self.diffservdatapathifdirection.value_namespace = name_space
                    self.diffservdatapathifdirection.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServDataPathStart"):
                    self.diffservdatapathstart = value
                    self.diffservdatapathstart.value_namespace = name_space
                    self.diffservdatapathstart.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServDataPathStatus"):
                    self.diffservdatapathstatus = value
                    self.diffservdatapathstatus.value_namespace = name_space
                    self.diffservdatapathstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServDataPathStorage"):
                    self.diffservdatapathstorage = value
                    self.diffservdatapathstorage.value_namespace = name_space
                    self.diffservdatapathstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservdatapathentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservdatapathentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServDataPathTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServDataPathEntry"):
                for c in self.diffservdatapathentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservdatapathtable.Diffservdatapathentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservdatapathentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServDataPathEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservclfrtable(Entity):
        """
        This table enumerates all the diffserv classifier functional
        data path elements of this device.  The actual classification
        definitions are defined in diffServClfrElementTable entries
        belonging to each classifier.
        
        An entry in this table, pointed to by a RowPointer specifying an
        instance of diffServClfrStatus, is frequently used as the name
        for a set of classifier elements, which all use the index
        diffServClfrId. Per the semantics of the classifier element
        table, these entries constitute one or more unordered sets of
        tests which may be simultaneously applied to a message to
        
        
        
        classify it.
        
        The primary function of this table is to ensure that the value of
        diffServClfrId is unique before attempting to use it in creating
        a diffServClfrElementEntry. Therefore, the diffServClfrEntry must
        be created on the same SET as the diffServClfrElementEntry, or
        before the diffServClfrElementEntry is created.
        
        .. attribute:: diffservclfrentry
        
        	An entry in the classifier table describes a single classifier. All classifier elements belonging to the same classifier use the classifier's diffServClfrId as part of their index
        	**type**\: list of    :py:class:`Diffservclfrentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclfrtable.Diffservclfrentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservclfrtable, self).__init__()

            self.yang_name = "diffServClfrTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservclfrentry = YList(self)

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
                        super(DiffservMib.Diffservclfrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservclfrtable, self).__setattr__(name, value)


        class Diffservclfrentry(Entity):
            """
            An entry in the classifier table describes a single classifier.
            All classifier elements belonging to the same classifier use the
            classifier's diffServClfrId as part of their index.
            
            .. attribute:: diffservclfrid  <key>
            
            	An index that enumerates the classifier entries.  Managers should obtain new values for row creation in this table by reading diffServClfrNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservclfrtable.Diffservclfrentry, self).__init__()

                self.yang_name = "diffServClfrEntry"
                self.yang_parent_name = "diffServClfrTable"

                self.diffservclfrid = YLeaf(YType.uint32, "diffServClfrId")

                self.diffservclfrstatus = YLeaf(YType.enumeration, "diffServClfrStatus")

                self.diffservclfrstorage = YLeaf(YType.enumeration, "diffServClfrStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservclfrid",
                                "diffservclfrstatus",
                                "diffservclfrstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservclfrtable.Diffservclfrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservclfrtable.Diffservclfrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservclfrid.is_set or
                    self.diffservclfrstatus.is_set or
                    self.diffservclfrstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservclfrid.yfilter != YFilter.not_set or
                    self.diffservclfrstatus.yfilter != YFilter.not_set or
                    self.diffservclfrstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServClfrEntry" + "[diffServClfrId='" + self.diffservclfrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServClfrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservclfrid.is_set or self.diffservclfrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrid.get_name_leafdata())
                if (self.diffservclfrstatus.is_set or self.diffservclfrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrstatus.get_name_leafdata())
                if (self.diffservclfrstorage.is_set or self.diffservclfrstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServClfrId" or name == "diffServClfrStatus" or name == "diffServClfrStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServClfrId"):
                    self.diffservclfrid = value
                    self.diffservclfrid.value_namespace = name_space
                    self.diffservclfrid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrStatus"):
                    self.diffservclfrstatus = value
                    self.diffservclfrstatus.value_namespace = name_space
                    self.diffservclfrstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrStorage"):
                    self.diffservclfrstorage = value
                    self.diffservclfrstorage.value_namespace = name_space
                    self.diffservclfrstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservclfrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservclfrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServClfrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServClfrEntry"):
                for c in self.diffservclfrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservclfrtable.Diffservclfrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservclfrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServClfrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservclfrelementtable(Entity):
        """
        The classifier element table enumerates the relationship between
        classification patterns and subsequent downstream Differentiated
        Services Functional Data Path elements.
        diffServClfrElementSpecific points to a filter that specifies the
        classification parameters. A classifier may use filter tables of
        different types together.
        
        One example of a filter table defined in this MIB is
        diffServMultiFieldClfrTable, for IP Multi\-Field Classifiers
        (MFCs). Such an entry might identify anything from a single
        micro\-flow (an identifiable sub\-session packet stream directed
        from one sending transport to the receiving transport or
        transports), or aggregates of those such as the traffic from a
        host, traffic for an application, or traffic between two hosts
        using an application and a given DSCP. The standard Behavior
        Aggregate used in the Differentiated Services Architecture is
        encoded as a degenerate case of such an aggregate \- the traffic
        using a particular DSCP value.
        
        Filter tables for other filter types may be defined elsewhere.
        
        .. attribute:: diffservclfrelemententry
        
        	An entry in the classifier element table describes a single element of the classifier
        	**type**\: list of    :py:class:`Diffservclfrelemententry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservclfrelementtable, self).__init__()

            self.yang_name = "diffServClfrElementTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservclfrelemententry = YList(self)

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
                        super(DiffservMib.Diffservclfrelementtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservclfrelementtable, self).__setattr__(name, value)


        class Diffservclfrelemententry(Entity):
            """
            An entry in the classifier element table describes a single
            element of the classifier.
            
            .. attribute:: diffservclfrid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`diffservclfrid <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservclfrtable.Diffservclfrentry>`
            
            .. attribute:: diffservclfrelementid  <key>
            
            	An index that enumerates the Classifier Element entries. Managers obtain new values for row creation in this table by reading diffServClfrElementNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementnext
            
            	This attribute provides one branch of the fan\-out functionality of a classifier described in the Informal Differentiated Services Model section 4.1.  This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementprecedence
            
            	The relative order in which classifier elements are applied\: higher numbers represent classifier element with higher precedence.  Classifier elements with the same order must be unambiguous i.e. they must define non\-overlapping patterns, and are considered to be applied simultaneously to the traffic stream. Classifier elements with different order may overlap in their filters\:  the classifier element with the highest order that matches is taken.  On a given interface, there must be a complete classifier in place at all times in the ingress direction.  This means one or more filters must match any possible pattern. There is no such    requirement in the egress direction
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementspecific
            
            	A pointer to a valid entry in another table, filter table, that describes the applicable classification parameters, e.g. an entry in diffServMultiFieldClfrTable.  The value zeroDotZero is interpreted to match anything not matched by another classifier element \- only one such entry may exist for each classifier.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or    becomes inactive by other means, the element is ignored
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservclfrelementstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry, self).__init__()

                self.yang_name = "diffServClfrElementEntry"
                self.yang_parent_name = "diffServClfrElementTable"

                self.diffservclfrid = YLeaf(YType.str, "diffServClfrId")

                self.diffservclfrelementid = YLeaf(YType.uint32, "diffServClfrElementId")

                self.diffservclfrelementnext = YLeaf(YType.str, "diffServClfrElementNext")

                self.diffservclfrelementprecedence = YLeaf(YType.uint32, "diffServClfrElementPrecedence")

                self.diffservclfrelementspecific = YLeaf(YType.str, "diffServClfrElementSpecific")

                self.diffservclfrelementstatus = YLeaf(YType.enumeration, "diffServClfrElementStatus")

                self.diffservclfrelementstorage = YLeaf(YType.enumeration, "diffServClfrElementStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservclfrid",
                                "diffservclfrelementid",
                                "diffservclfrelementnext",
                                "diffservclfrelementprecedence",
                                "diffservclfrelementspecific",
                                "diffservclfrelementstatus",
                                "diffservclfrelementstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservclfrid.is_set or
                    self.diffservclfrelementid.is_set or
                    self.diffservclfrelementnext.is_set or
                    self.diffservclfrelementprecedence.is_set or
                    self.diffservclfrelementspecific.is_set or
                    self.diffservclfrelementstatus.is_set or
                    self.diffservclfrelementstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservclfrid.yfilter != YFilter.not_set or
                    self.diffservclfrelementid.yfilter != YFilter.not_set or
                    self.diffservclfrelementnext.yfilter != YFilter.not_set or
                    self.diffservclfrelementprecedence.yfilter != YFilter.not_set or
                    self.diffservclfrelementspecific.yfilter != YFilter.not_set or
                    self.diffservclfrelementstatus.yfilter != YFilter.not_set or
                    self.diffservclfrelementstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServClfrElementEntry" + "[diffServClfrId='" + self.diffservclfrid.get() + "']" + "[diffServClfrElementId='" + self.diffservclfrelementid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServClfrElementTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservclfrid.is_set or self.diffservclfrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrid.get_name_leafdata())
                if (self.diffservclfrelementid.is_set or self.diffservclfrelementid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementid.get_name_leafdata())
                if (self.diffservclfrelementnext.is_set or self.diffservclfrelementnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementnext.get_name_leafdata())
                if (self.diffservclfrelementprecedence.is_set or self.diffservclfrelementprecedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementprecedence.get_name_leafdata())
                if (self.diffservclfrelementspecific.is_set or self.diffservclfrelementspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementspecific.get_name_leafdata())
                if (self.diffservclfrelementstatus.is_set or self.diffservclfrelementstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementstatus.get_name_leafdata())
                if (self.diffservclfrelementstorage.is_set or self.diffservclfrelementstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservclfrelementstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServClfrId" or name == "diffServClfrElementId" or name == "diffServClfrElementNext" or name == "diffServClfrElementPrecedence" or name == "diffServClfrElementSpecific" or name == "diffServClfrElementStatus" or name == "diffServClfrElementStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServClfrId"):
                    self.diffservclfrid = value
                    self.diffservclfrid.value_namespace = name_space
                    self.diffservclfrid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementId"):
                    self.diffservclfrelementid = value
                    self.diffservclfrelementid.value_namespace = name_space
                    self.diffservclfrelementid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementNext"):
                    self.diffservclfrelementnext = value
                    self.diffservclfrelementnext.value_namespace = name_space
                    self.diffservclfrelementnext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementPrecedence"):
                    self.diffservclfrelementprecedence = value
                    self.diffservclfrelementprecedence.value_namespace = name_space
                    self.diffservclfrelementprecedence.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementSpecific"):
                    self.diffservclfrelementspecific = value
                    self.diffservclfrelementspecific.value_namespace = name_space
                    self.diffservclfrelementspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementStatus"):
                    self.diffservclfrelementstatus = value
                    self.diffservclfrelementstatus.value_namespace = name_space
                    self.diffservclfrelementstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServClfrElementStorage"):
                    self.diffservclfrelementstorage = value
                    self.diffservclfrelementstorage.value_namespace = name_space
                    self.diffservclfrelementstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservclfrelemententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservclfrelemententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServClfrElementTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServClfrElementEntry"):
                for c in self.diffservclfrelemententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservclfrelemententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServClfrElementEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservmultifieldclfrtable(Entity):
        """
        A table of IP Multi\-field Classifier filter entries that a
        
        
        
        system may use to identify IP traffic.
        
        .. attribute:: diffservmultifieldclfrentry
        
        	An IP Multi\-field Classifier entry describes a single filter
        	**type**\: list of    :py:class:`Diffservmultifieldclfrentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservmultifieldclfrtable, self).__init__()

            self.yang_name = "diffServMultiFieldClfrTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservmultifieldclfrentry = YList(self)

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
                        super(DiffservMib.Diffservmultifieldclfrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservmultifieldclfrtable, self).__setattr__(name, value)


        class Diffservmultifieldclfrentry(Entity):
            """
            An IP Multi\-field Classifier entry describes a single filter.
            
            .. attribute:: diffservmultifieldclfrid  <key>
            
            	An index that enumerates the MultiField Classifier filter entries.  Managers obtain new values for row creation in this table by reading diffServMultiFieldClfrNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmultifieldclfraddrtype
            
            	The type of IP address used by this classifier entry.  While other types of addresses are defined in the InetAddressType    textual convention, and DNS names, a classifier can only look at packets on the wire. Therefore, this object is limited to IPv4 and IPv6 addresses
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: diffservmultifieldclfrdscp
            
            	The value that the DSCP in the packet must have to match this entry. A value of \-1 indicates that a specific DSCP value has not been defined and thus all DSCP values are considered a match
            	**type**\:  int
            
            	**range:** \-1..63
            
            .. attribute:: diffservmultifieldclfrdstaddr
            
            	The IP address to match against the packet's destination IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.  diffServMultiFieldClfrDstPrefixLength indicates the number of bits that are relevant
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: diffservmultifieldclfrdstl4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrDstL4PortMin
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrdstl4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrdstprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrDstAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\:  int
            
            	**range:** 0..2040
            
            	**units**\: bits
            
            .. attribute:: diffservmultifieldclfrflowid
            
            	The flow identifier in an IPv6 header
            	**type**\:  int
            
            	**range:** 0..1048575
            
            .. attribute:: diffservmultifieldclfrprotocol
            
            	The IP protocol to match against the IPv4 protocol number or the IPv6 Next\- Header number in the packet. A value of 255 means match all.  Note the protocol number of 255 is reserved by IANA, and Next\-Header number of 0 is used in IPv6
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: diffservmultifieldclfrsrcaddr
            
            	The IP address to match against the packet's source IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix. diffServMultiFieldClfrSrcPrefixLength indicates the number of bits that are relevant
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: diffservmultifieldclfrsrcl4portmax
            
            	The maximum value that the layer\-4 source port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrSrcL4PortMin
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcl4portmin
            
            	The minimum value that the layer\-4 source port number in the packet must have in order to match this classifier entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrSrcAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\:  int
            
            	**range:** 0..2040
            
            	**units**\: bits
            
            .. attribute:: diffservmultifieldclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservmultifieldclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry, self).__init__()

                self.yang_name = "diffServMultiFieldClfrEntry"
                self.yang_parent_name = "diffServMultiFieldClfrTable"

                self.diffservmultifieldclfrid = YLeaf(YType.uint32, "diffServMultiFieldClfrId")

                self.diffservmultifieldclfraddrtype = YLeaf(YType.enumeration, "diffServMultiFieldClfrAddrType")

                self.diffservmultifieldclfrdscp = YLeaf(YType.int32, "diffServMultiFieldClfrDscp")

                self.diffservmultifieldclfrdstaddr = YLeaf(YType.str, "diffServMultiFieldClfrDstAddr")

                self.diffservmultifieldclfrdstl4portmax = YLeaf(YType.uint16, "diffServMultiFieldClfrDstL4PortMax")

                self.diffservmultifieldclfrdstl4portmin = YLeaf(YType.uint16, "diffServMultiFieldClfrDstL4PortMin")

                self.diffservmultifieldclfrdstprefixlength = YLeaf(YType.uint32, "diffServMultiFieldClfrDstPrefixLength")

                self.diffservmultifieldclfrflowid = YLeaf(YType.uint32, "diffServMultiFieldClfrFlowId")

                self.diffservmultifieldclfrprotocol = YLeaf(YType.uint32, "diffServMultiFieldClfrProtocol")

                self.diffservmultifieldclfrsrcaddr = YLeaf(YType.str, "diffServMultiFieldClfrSrcAddr")

                self.diffservmultifieldclfrsrcl4portmax = YLeaf(YType.uint16, "diffServMultiFieldClfrSrcL4PortMax")

                self.diffservmultifieldclfrsrcl4portmin = YLeaf(YType.uint16, "diffServMultiFieldClfrSrcL4PortMin")

                self.diffservmultifieldclfrsrcprefixlength = YLeaf(YType.uint32, "diffServMultiFieldClfrSrcPrefixLength")

                self.diffservmultifieldclfrstatus = YLeaf(YType.enumeration, "diffServMultiFieldClfrStatus")

                self.diffservmultifieldclfrstorage = YLeaf(YType.enumeration, "diffServMultiFieldClfrStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservmultifieldclfrid",
                                "diffservmultifieldclfraddrtype",
                                "diffservmultifieldclfrdscp",
                                "diffservmultifieldclfrdstaddr",
                                "diffservmultifieldclfrdstl4portmax",
                                "diffservmultifieldclfrdstl4portmin",
                                "diffservmultifieldclfrdstprefixlength",
                                "diffservmultifieldclfrflowid",
                                "diffservmultifieldclfrprotocol",
                                "diffservmultifieldclfrsrcaddr",
                                "diffservmultifieldclfrsrcl4portmax",
                                "diffservmultifieldclfrsrcl4portmin",
                                "diffservmultifieldclfrsrcprefixlength",
                                "diffservmultifieldclfrstatus",
                                "diffservmultifieldclfrstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservmultifieldclfrid.is_set or
                    self.diffservmultifieldclfraddrtype.is_set or
                    self.diffservmultifieldclfrdscp.is_set or
                    self.diffservmultifieldclfrdstaddr.is_set or
                    self.diffservmultifieldclfrdstl4portmax.is_set or
                    self.diffservmultifieldclfrdstl4portmin.is_set or
                    self.diffservmultifieldclfrdstprefixlength.is_set or
                    self.diffservmultifieldclfrflowid.is_set or
                    self.diffservmultifieldclfrprotocol.is_set or
                    self.diffservmultifieldclfrsrcaddr.is_set or
                    self.diffservmultifieldclfrsrcl4portmax.is_set or
                    self.diffservmultifieldclfrsrcl4portmin.is_set or
                    self.diffservmultifieldclfrsrcprefixlength.is_set or
                    self.diffservmultifieldclfrstatus.is_set or
                    self.diffservmultifieldclfrstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrid.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfraddrtype.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrdscp.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrdstaddr.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrdstl4portmax.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrdstl4portmin.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrdstprefixlength.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrflowid.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrprotocol.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrsrcaddr.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrsrcl4portmax.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrsrcl4portmin.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrsrcprefixlength.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrstatus.yfilter != YFilter.not_set or
                    self.diffservmultifieldclfrstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServMultiFieldClfrEntry" + "[diffServMultiFieldClfrId='" + self.diffservmultifieldclfrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServMultiFieldClfrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservmultifieldclfrid.is_set or self.diffservmultifieldclfrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrid.get_name_leafdata())
                if (self.diffservmultifieldclfraddrtype.is_set or self.diffservmultifieldclfraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfraddrtype.get_name_leafdata())
                if (self.diffservmultifieldclfrdscp.is_set or self.diffservmultifieldclfrdscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrdscp.get_name_leafdata())
                if (self.diffservmultifieldclfrdstaddr.is_set or self.diffservmultifieldclfrdstaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrdstaddr.get_name_leafdata())
                if (self.diffservmultifieldclfrdstl4portmax.is_set or self.diffservmultifieldclfrdstl4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrdstl4portmax.get_name_leafdata())
                if (self.diffservmultifieldclfrdstl4portmin.is_set or self.diffservmultifieldclfrdstl4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrdstl4portmin.get_name_leafdata())
                if (self.diffservmultifieldclfrdstprefixlength.is_set or self.diffservmultifieldclfrdstprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrdstprefixlength.get_name_leafdata())
                if (self.diffservmultifieldclfrflowid.is_set or self.diffservmultifieldclfrflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrflowid.get_name_leafdata())
                if (self.diffservmultifieldclfrprotocol.is_set or self.diffservmultifieldclfrprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrprotocol.get_name_leafdata())
                if (self.diffservmultifieldclfrsrcaddr.is_set or self.diffservmultifieldclfrsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrsrcaddr.get_name_leafdata())
                if (self.diffservmultifieldclfrsrcl4portmax.is_set or self.diffservmultifieldclfrsrcl4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrsrcl4portmax.get_name_leafdata())
                if (self.diffservmultifieldclfrsrcl4portmin.is_set or self.diffservmultifieldclfrsrcl4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrsrcl4portmin.get_name_leafdata())
                if (self.diffservmultifieldclfrsrcprefixlength.is_set or self.diffservmultifieldclfrsrcprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrsrcprefixlength.get_name_leafdata())
                if (self.diffservmultifieldclfrstatus.is_set or self.diffservmultifieldclfrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrstatus.get_name_leafdata())
                if (self.diffservmultifieldclfrstorage.is_set or self.diffservmultifieldclfrstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmultifieldclfrstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServMultiFieldClfrId" or name == "diffServMultiFieldClfrAddrType" or name == "diffServMultiFieldClfrDscp" or name == "diffServMultiFieldClfrDstAddr" or name == "diffServMultiFieldClfrDstL4PortMax" or name == "diffServMultiFieldClfrDstL4PortMin" or name == "diffServMultiFieldClfrDstPrefixLength" or name == "diffServMultiFieldClfrFlowId" or name == "diffServMultiFieldClfrProtocol" or name == "diffServMultiFieldClfrSrcAddr" or name == "diffServMultiFieldClfrSrcL4PortMax" or name == "diffServMultiFieldClfrSrcL4PortMin" or name == "diffServMultiFieldClfrSrcPrefixLength" or name == "diffServMultiFieldClfrStatus" or name == "diffServMultiFieldClfrStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServMultiFieldClfrId"):
                    self.diffservmultifieldclfrid = value
                    self.diffservmultifieldclfrid.value_namespace = name_space
                    self.diffservmultifieldclfrid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrAddrType"):
                    self.diffservmultifieldclfraddrtype = value
                    self.diffservmultifieldclfraddrtype.value_namespace = name_space
                    self.diffservmultifieldclfraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrDscp"):
                    self.diffservmultifieldclfrdscp = value
                    self.diffservmultifieldclfrdscp.value_namespace = name_space
                    self.diffservmultifieldclfrdscp.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrDstAddr"):
                    self.diffservmultifieldclfrdstaddr = value
                    self.diffservmultifieldclfrdstaddr.value_namespace = name_space
                    self.diffservmultifieldclfrdstaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrDstL4PortMax"):
                    self.diffservmultifieldclfrdstl4portmax = value
                    self.diffservmultifieldclfrdstl4portmax.value_namespace = name_space
                    self.diffservmultifieldclfrdstl4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrDstL4PortMin"):
                    self.diffservmultifieldclfrdstl4portmin = value
                    self.diffservmultifieldclfrdstl4portmin.value_namespace = name_space
                    self.diffservmultifieldclfrdstl4portmin.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrDstPrefixLength"):
                    self.diffservmultifieldclfrdstprefixlength = value
                    self.diffservmultifieldclfrdstprefixlength.value_namespace = name_space
                    self.diffservmultifieldclfrdstprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrFlowId"):
                    self.diffservmultifieldclfrflowid = value
                    self.diffservmultifieldclfrflowid.value_namespace = name_space
                    self.diffservmultifieldclfrflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrProtocol"):
                    self.diffservmultifieldclfrprotocol = value
                    self.diffservmultifieldclfrprotocol.value_namespace = name_space
                    self.diffservmultifieldclfrprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrSrcAddr"):
                    self.diffservmultifieldclfrsrcaddr = value
                    self.diffservmultifieldclfrsrcaddr.value_namespace = name_space
                    self.diffservmultifieldclfrsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrSrcL4PortMax"):
                    self.diffservmultifieldclfrsrcl4portmax = value
                    self.diffservmultifieldclfrsrcl4portmax.value_namespace = name_space
                    self.diffservmultifieldclfrsrcl4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrSrcL4PortMin"):
                    self.diffservmultifieldclfrsrcl4portmin = value
                    self.diffservmultifieldclfrsrcl4portmin.value_namespace = name_space
                    self.diffservmultifieldclfrsrcl4portmin.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrSrcPrefixLength"):
                    self.diffservmultifieldclfrsrcprefixlength = value
                    self.diffservmultifieldclfrsrcprefixlength.value_namespace = name_space
                    self.diffservmultifieldclfrsrcprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrStatus"):
                    self.diffservmultifieldclfrstatus = value
                    self.diffservmultifieldclfrstatus.value_namespace = name_space
                    self.diffservmultifieldclfrstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMultiFieldClfrStorage"):
                    self.diffservmultifieldclfrstorage = value
                    self.diffservmultifieldclfrstorage.value_namespace = name_space
                    self.diffservmultifieldclfrstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservmultifieldclfrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservmultifieldclfrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServMultiFieldClfrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServMultiFieldClfrEntry"):
                for c in self.diffservmultifieldclfrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservmultifieldclfrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMultiFieldClfrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservmetertable(Entity):
        """
        This table enumerates specific meters that a system may use to
        police a stream of traffic. The traffic stream to be metered is
        determined by the Differentiated Services Functional Data Path
        Element(s) upstream of the meter i.e. by the object(s) that point
        to each entry in this table.  This may include all traffic on an
        interface.
        
        Specific meter details are to be found in table entry referenced
        by diffServMeterSpecific.
        
        .. attribute:: diffservmeterentry
        
        	An entry in the meter table describes a single conformance level of a meter
        	**type**\: list of    :py:class:`Diffservmeterentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmetertable.Diffservmeterentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservmetertable, self).__init__()

            self.yang_name = "diffServMeterTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservmeterentry = YList(self)

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
                        super(DiffservMib.Diffservmetertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservmetertable, self).__setattr__(name, value)


        class Diffservmeterentry(Entity):
            """
            An entry in the meter table describes a single conformance level
            of a meter.
            
            .. attribute:: diffservmeterid  <key>
            
            	An index that enumerates the Meter entries.  Managers obtain new values for row creation in this table by reading diffServMeterNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmeterfailnext
            
            	If the traffic does not conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry      diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterspecific
            
            	This indicates the behavior of the meter by pointing to an entry containing detailed parameters. Note that entries in that specific table must be managed explicitly.  For example, diffServMeterSpecific may point to an entry in diffServTBParamTable, which contains an instance of a single set of Token Bucket parameters.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the meter always succeeds
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservmeterstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: diffservmetersucceednext
            
            	If the traffic does conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservmetertable.Diffservmeterentry, self).__init__()

                self.yang_name = "diffServMeterEntry"
                self.yang_parent_name = "diffServMeterTable"

                self.diffservmeterid = YLeaf(YType.uint32, "diffServMeterId")

                self.diffservmeterfailnext = YLeaf(YType.str, "diffServMeterFailNext")

                self.diffservmeterspecific = YLeaf(YType.str, "diffServMeterSpecific")

                self.diffservmeterstatus = YLeaf(YType.enumeration, "diffServMeterStatus")

                self.diffservmeterstorage = YLeaf(YType.enumeration, "diffServMeterStorage")

                self.diffservmetersucceednext = YLeaf(YType.str, "diffServMeterSucceedNext")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservmeterid",
                                "diffservmeterfailnext",
                                "diffservmeterspecific",
                                "diffservmeterstatus",
                                "diffservmeterstorage",
                                "diffservmetersucceednext") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservmetertable.Diffservmeterentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservmetertable.Diffservmeterentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservmeterid.is_set or
                    self.diffservmeterfailnext.is_set or
                    self.diffservmeterspecific.is_set or
                    self.diffservmeterstatus.is_set or
                    self.diffservmeterstorage.is_set or
                    self.diffservmetersucceednext.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservmeterid.yfilter != YFilter.not_set or
                    self.diffservmeterfailnext.yfilter != YFilter.not_set or
                    self.diffservmeterspecific.yfilter != YFilter.not_set or
                    self.diffservmeterstatus.yfilter != YFilter.not_set or
                    self.diffservmeterstorage.yfilter != YFilter.not_set or
                    self.diffservmetersucceednext.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServMeterEntry" + "[diffServMeterId='" + self.diffservmeterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServMeterTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservmeterid.is_set or self.diffservmeterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmeterid.get_name_leafdata())
                if (self.diffservmeterfailnext.is_set or self.diffservmeterfailnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmeterfailnext.get_name_leafdata())
                if (self.diffservmeterspecific.is_set or self.diffservmeterspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmeterspecific.get_name_leafdata())
                if (self.diffservmeterstatus.is_set or self.diffservmeterstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmeterstatus.get_name_leafdata())
                if (self.diffservmeterstorage.is_set or self.diffservmeterstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmeterstorage.get_name_leafdata())
                if (self.diffservmetersucceednext.is_set or self.diffservmetersucceednext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmetersucceednext.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServMeterId" or name == "diffServMeterFailNext" or name == "diffServMeterSpecific" or name == "diffServMeterStatus" or name == "diffServMeterStorage" or name == "diffServMeterSucceedNext"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServMeterId"):
                    self.diffservmeterid = value
                    self.diffservmeterid.value_namespace = name_space
                    self.diffservmeterid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMeterFailNext"):
                    self.diffservmeterfailnext = value
                    self.diffservmeterfailnext.value_namespace = name_space
                    self.diffservmeterfailnext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMeterSpecific"):
                    self.diffservmeterspecific = value
                    self.diffservmeterspecific.value_namespace = name_space
                    self.diffservmeterspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMeterStatus"):
                    self.diffservmeterstatus = value
                    self.diffservmeterstatus.value_namespace = name_space
                    self.diffservmeterstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMeterStorage"):
                    self.diffservmeterstorage = value
                    self.diffservmeterstorage.value_namespace = name_space
                    self.diffservmeterstorage.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMeterSucceedNext"):
                    self.diffservmetersucceednext = value
                    self.diffservmetersucceednext.value_namespace = name_space
                    self.diffservmetersucceednext.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservmeterentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservmeterentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServMeterTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServMeterEntry"):
                for c in self.diffservmeterentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservmetertable.Diffservmeterentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservmeterentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMeterEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservtbparamtable(Entity):
        """
        This table enumerates a single set of token bucket meter
        parameters that a system may use to police a stream of traffic.
        Such meters are modeled here as having a single rate and a single
        burst size. Multiple entries are used when multiple rates/burst
        sizes are needed.
        
        .. attribute:: diffservtbparamentry
        
        	An entry that describes a single set of token bucket parameters
        	**type**\: list of    :py:class:`Diffservtbparamentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservtbparamtable.Diffservtbparamentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservtbparamtable, self).__init__()

            self.yang_name = "diffServTBParamTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservtbparamentry = YList(self)

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
                        super(DiffservMib.Diffservtbparamtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservtbparamtable, self).__setattr__(name, value)


        class Diffservtbparamentry(Entity):
            """
            An entry that describes a single set of token bucket
            parameters.
            
            .. attribute:: diffservtbparamid  <key>
            
            	An index that enumerates the Token Bucket Parameter entries. Managers obtain new values for row creation in this table by reading diffServTBParamNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservtbparamburstsize
            
            	The maximum number of bytes in a single transmission burst. This attribute is used for\: 1. CBS and EBS in RFC 2697 for srTCM 2. CBS and PBS in RFC 2698 for trTCM 3. Burst Size in RFC 3290
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: diffservtbparaminterval
            
            	The time interval used with the token bucket.  For\: 1. Average Rate Meter, the Informal Differentiated Services Model    section 5.2.1, \- Delta. 2. Simple Token Bucket Meter, the Informal Differentiated    Services Model section 5.1, \- time interval t. 3. RFC 2859 TSWTCM, \- AVG\_INTERVAL. 4. RFC 2697 srTCM, RFC 2698 trTCM, \- token bucket update time    interval
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: diffservtbparamrate
            
            	The token\-bucket rate, in kilobits per second (kbps). This attribute is used for\: 1. CIR in RFC 2697 for srTCM 2. CIR and PIR in RFC 2698 for trTCM 3. CTR and PTR in RFC 2859 for TSWTCM 4. AverageRate in RFC 3290
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservtbparamstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservtbparamstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: diffservtbparamtype
            
            	The Metering algorithm associated with the Token Bucket parameters.  zeroDotZero indicates this is unknown.  Standard values for generic algorithms\: diffServTBParamSimpleTokenBucket, diffServTBParamAvgRate, diffServTBParamSrTCMBlind, diffServTBParamSrTCMAware, diffServTBParamTrTCMBlind, diffServTBParamTrTCMAware, and diffServTBParamTswTCM are specified in this MIB as OBJECT\- IDENTITYs; additional values may be further specified in other MIBs
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservtbparamtable.Diffservtbparamentry, self).__init__()

                self.yang_name = "diffServTBParamEntry"
                self.yang_parent_name = "diffServTBParamTable"

                self.diffservtbparamid = YLeaf(YType.uint32, "diffServTBParamId")

                self.diffservtbparamburstsize = YLeaf(YType.int32, "diffServTBParamBurstSize")

                self.diffservtbparaminterval = YLeaf(YType.uint32, "diffServTBParamInterval")

                self.diffservtbparamrate = YLeaf(YType.uint32, "diffServTBParamRate")

                self.diffservtbparamstatus = YLeaf(YType.enumeration, "diffServTBParamStatus")

                self.diffservtbparamstorage = YLeaf(YType.enumeration, "diffServTBParamStorage")

                self.diffservtbparamtype = YLeaf(YType.str, "diffServTBParamType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservtbparamid",
                                "diffservtbparamburstsize",
                                "diffservtbparaminterval",
                                "diffservtbparamrate",
                                "diffservtbparamstatus",
                                "diffservtbparamstorage",
                                "diffservtbparamtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservtbparamtable.Diffservtbparamentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservtbparamtable.Diffservtbparamentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservtbparamid.is_set or
                    self.diffservtbparamburstsize.is_set or
                    self.diffservtbparaminterval.is_set or
                    self.diffservtbparamrate.is_set or
                    self.diffservtbparamstatus.is_set or
                    self.diffservtbparamstorage.is_set or
                    self.diffservtbparamtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservtbparamid.yfilter != YFilter.not_set or
                    self.diffservtbparamburstsize.yfilter != YFilter.not_set or
                    self.diffservtbparaminterval.yfilter != YFilter.not_set or
                    self.diffservtbparamrate.yfilter != YFilter.not_set or
                    self.diffservtbparamstatus.yfilter != YFilter.not_set or
                    self.diffservtbparamstorage.yfilter != YFilter.not_set or
                    self.diffservtbparamtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServTBParamEntry" + "[diffServTBParamId='" + self.diffservtbparamid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServTBParamTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservtbparamid.is_set or self.diffservtbparamid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamid.get_name_leafdata())
                if (self.diffservtbparamburstsize.is_set or self.diffservtbparamburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamburstsize.get_name_leafdata())
                if (self.diffservtbparaminterval.is_set or self.diffservtbparaminterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparaminterval.get_name_leafdata())
                if (self.diffservtbparamrate.is_set or self.diffservtbparamrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamrate.get_name_leafdata())
                if (self.diffservtbparamstatus.is_set or self.diffservtbparamstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamstatus.get_name_leafdata())
                if (self.diffservtbparamstorage.is_set or self.diffservtbparamstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamstorage.get_name_leafdata())
                if (self.diffservtbparamtype.is_set or self.diffservtbparamtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservtbparamtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServTBParamId" or name == "diffServTBParamBurstSize" or name == "diffServTBParamInterval" or name == "diffServTBParamRate" or name == "diffServTBParamStatus" or name == "diffServTBParamStorage" or name == "diffServTBParamType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServTBParamId"):
                    self.diffservtbparamid = value
                    self.diffservtbparamid.value_namespace = name_space
                    self.diffservtbparamid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamBurstSize"):
                    self.diffservtbparamburstsize = value
                    self.diffservtbparamburstsize.value_namespace = name_space
                    self.diffservtbparamburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamInterval"):
                    self.diffservtbparaminterval = value
                    self.diffservtbparaminterval.value_namespace = name_space
                    self.diffservtbparaminterval.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamRate"):
                    self.diffservtbparamrate = value
                    self.diffservtbparamrate.value_namespace = name_space
                    self.diffservtbparamrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamStatus"):
                    self.diffservtbparamstatus = value
                    self.diffservtbparamstatus.value_namespace = name_space
                    self.diffservtbparamstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamStorage"):
                    self.diffservtbparamstorage = value
                    self.diffservtbparamstorage.value_namespace = name_space
                    self.diffservtbparamstorage.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServTBParamType"):
                    self.diffservtbparamtype = value
                    self.diffservtbparamtype.value_namespace = name_space
                    self.diffservtbparamtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservtbparamentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservtbparamentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServTBParamTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServTBParamEntry"):
                for c in self.diffservtbparamentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservtbparamtable.Diffservtbparamentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservtbparamentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServTBParamEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservactiontable(Entity):
        """
        The Action Table enumerates actions that can be performed to a
        stream of traffic. Multiple actions can be concatenated. For
        example, traffic exiting from a meter may be counted, marked, and
        potentially dropped before entering a queue.
        
        Specific actions are indicated by diffServActionSpecific which
        points to an entry of a specific action type parameterizing the
        action in detail.
        
        .. attribute:: diffservactionentry
        
        	Each entry in the action table allows description of one specific action to be applied to traffic
        	**type**\: list of    :py:class:`Diffservactionentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservactiontable.Diffservactionentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservactiontable, self).__init__()

            self.yang_name = "diffServActionTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservactionentry = YList(self)

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
                        super(DiffservMib.Diffservactiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservactiontable, self).__setattr__(name, value)


        class Diffservactionentry(Entity):
            """
            Each entry in the action table allows description of one
            specific action to be applied to traffic.
            
            .. attribute:: diffservactionid  <key>
            
            	An index that enumerates the Action entries.  Managers obtain new values for row creation in this table by reading diffServActionNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservactioninterface
            
            	The interface index (value of ifIndex) that this action occurs on. This may be derived from the diffServDataPathStartEntry's index by extension through the various RowPointers. However, as this may be difficult for a network management station, it is placed here as well.  If this is indeterminate, the value is zero.  This is of especial relevance when reporting the counters which may apply to traffic crossing an interface\:    diffServCountActOctets,    diffServCountActPkts,    diffServAlgDropOctets,    diffServAlgDropPkts,    diffServAlgRandomDropOctets, and    diffServAlgRandomDropPkts.  It is also especially relevant to the queue and scheduler which may be subsequently applied
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: diffservactionnext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservactionspecific
            
            	A pointer to an object instance providing additional information for the type of action indicated by this action table entry.  For the standard actions defined by this MIB module, this should point to either a diffServDscpMarkActEntry or a diffServCountActEntry. For other actions, it may point to an object instance defined in some other MIB.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the Meter should be treated as if it were not present.  This may lead to incorrect policy behavior
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservactionstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservactionstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservactiontable.Diffservactionentry, self).__init__()

                self.yang_name = "diffServActionEntry"
                self.yang_parent_name = "diffServActionTable"

                self.diffservactionid = YLeaf(YType.uint32, "diffServActionId")

                self.diffservactioninterface = YLeaf(YType.int32, "diffServActionInterface")

                self.diffservactionnext = YLeaf(YType.str, "diffServActionNext")

                self.diffservactionspecific = YLeaf(YType.str, "diffServActionSpecific")

                self.diffservactionstatus = YLeaf(YType.enumeration, "diffServActionStatus")

                self.diffservactionstorage = YLeaf(YType.enumeration, "diffServActionStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservactionid",
                                "diffservactioninterface",
                                "diffservactionnext",
                                "diffservactionspecific",
                                "diffservactionstatus",
                                "diffservactionstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservactiontable.Diffservactionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservactiontable.Diffservactionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservactionid.is_set or
                    self.diffservactioninterface.is_set or
                    self.diffservactionnext.is_set or
                    self.diffservactionspecific.is_set or
                    self.diffservactionstatus.is_set or
                    self.diffservactionstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservactionid.yfilter != YFilter.not_set or
                    self.diffservactioninterface.yfilter != YFilter.not_set or
                    self.diffservactionnext.yfilter != YFilter.not_set or
                    self.diffservactionspecific.yfilter != YFilter.not_set or
                    self.diffservactionstatus.yfilter != YFilter.not_set or
                    self.diffservactionstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServActionEntry" + "[diffServActionId='" + self.diffservactionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServActionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservactionid.is_set or self.diffservactionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactionid.get_name_leafdata())
                if (self.diffservactioninterface.is_set or self.diffservactioninterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactioninterface.get_name_leafdata())
                if (self.diffservactionnext.is_set or self.diffservactionnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactionnext.get_name_leafdata())
                if (self.diffservactionspecific.is_set or self.diffservactionspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactionspecific.get_name_leafdata())
                if (self.diffservactionstatus.is_set or self.diffservactionstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactionstatus.get_name_leafdata())
                if (self.diffservactionstorage.is_set or self.diffservactionstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservactionstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServActionId" or name == "diffServActionInterface" or name == "diffServActionNext" or name == "diffServActionSpecific" or name == "diffServActionStatus" or name == "diffServActionStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServActionId"):
                    self.diffservactionid = value
                    self.diffservactionid.value_namespace = name_space
                    self.diffservactionid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServActionInterface"):
                    self.diffservactioninterface = value
                    self.diffservactioninterface.value_namespace = name_space
                    self.diffservactioninterface.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServActionNext"):
                    self.diffservactionnext = value
                    self.diffservactionnext.value_namespace = name_space
                    self.diffservactionnext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServActionSpecific"):
                    self.diffservactionspecific = value
                    self.diffservactionspecific.value_namespace = name_space
                    self.diffservactionspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServActionStatus"):
                    self.diffservactionstatus = value
                    self.diffservactionstatus.value_namespace = name_space
                    self.diffservactionstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServActionStorage"):
                    self.diffservactionstorage = value
                    self.diffservactionstorage.value_namespace = name_space
                    self.diffservactionstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservactionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservactionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServActionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServActionEntry"):
                for c in self.diffservactionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservactiontable.Diffservactionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservactionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServActionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservdscpmarkacttable(Entity):
        """
        This table enumerates specific DSCPs used for marking or
        remarking the DSCP field of IP packets. The entries of this table
        may be referenced by a diffServActionSpecific attribute.
        
        .. attribute:: diffservdscpmarkactentry
        
        	An entry in the DSCP mark action table that describes a single DSCP used for marking
        	**type**\: list of    :py:class:`Diffservdscpmarkactentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservdscpmarkacttable, self).__init__()

            self.yang_name = "diffServDscpMarkActTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservdscpmarkactentry = YList(self)

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
                        super(DiffservMib.Diffservdscpmarkacttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservdscpmarkacttable, self).__setattr__(name, value)


        class Diffservdscpmarkactentry(Entity):
            """
            An entry in the DSCP mark action table that describes a single
            DSCP used for marking.
            
            .. attribute:: diffservdscpmarkactdscp  <key>
            
            	The DSCP that this Action will store into the DSCP field of the subject. It is quite possible that the only packets subject to this Action are already marked with this DSCP. Note also that Differentiated Services processing may result in packet being marked on both ingress to a network and on egress from it, and that ingress and egress can occur in the same router
            	**type**\:  int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry, self).__init__()

                self.yang_name = "diffServDscpMarkActEntry"
                self.yang_parent_name = "diffServDscpMarkActTable"

                self.diffservdscpmarkactdscp = YLeaf(YType.uint8, "diffServDscpMarkActDscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservdscpmarkactdscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry, self).__setattr__(name, value)

            def has_data(self):
                return self.diffservdscpmarkactdscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservdscpmarkactdscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServDscpMarkActEntry" + "[diffServDscpMarkActDscp='" + self.diffservdscpmarkactdscp.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServDscpMarkActTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservdscpmarkactdscp.is_set or self.diffservdscpmarkactdscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservdscpmarkactdscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServDscpMarkActDscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServDscpMarkActDscp"):
                    self.diffservdscpmarkactdscp = value
                    self.diffservdscpmarkactdscp.value_namespace = name_space
                    self.diffservdscpmarkactdscp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservdscpmarkactentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservdscpmarkactentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServDscpMarkActTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServDscpMarkActEntry"):
                for c in self.diffservdscpmarkactentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservdscpmarkactentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServDscpMarkActEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservcountacttable(Entity):
        """
        This table contains counters for all the traffic passing through
        an action element.
        
        .. attribute:: diffservcountactentry
        
        	An entry in the count action table describes a single set of traffic counters
        	**type**\: list of    :py:class:`Diffservcountactentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservcountacttable.Diffservcountactentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservcountacttable, self).__init__()

            self.yang_name = "diffServCountActTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservcountactentry = YList(self)

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
                        super(DiffservMib.Diffservcountacttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservcountacttable, self).__setattr__(name, value)


        class Diffservcountactentry(Entity):
            """
            An entry in the count action table describes a single set of
            traffic counters.
            
            .. attribute:: diffservcountactid  <key>
            
            	An index that enumerates the Count Action entries.  Managers obtain new values for row creation in this table by reading    diffServCountActNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservcountactoctets
            
            	The number of octets at the Action data path element.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservcountactpkts
            
            	The number of packets at the Action data path element.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservcountactstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing    to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservcountactstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservcountacttable.Diffservcountactentry, self).__init__()

                self.yang_name = "diffServCountActEntry"
                self.yang_parent_name = "diffServCountActTable"

                self.diffservcountactid = YLeaf(YType.uint32, "diffServCountActId")

                self.diffservcountactoctets = YLeaf(YType.uint64, "diffServCountActOctets")

                self.diffservcountactpkts = YLeaf(YType.uint64, "diffServCountActPkts")

                self.diffservcountactstatus = YLeaf(YType.enumeration, "diffServCountActStatus")

                self.diffservcountactstorage = YLeaf(YType.enumeration, "diffServCountActStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservcountactid",
                                "diffservcountactoctets",
                                "diffservcountactpkts",
                                "diffservcountactstatus",
                                "diffservcountactstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservcountacttable.Diffservcountactentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservcountacttable.Diffservcountactentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservcountactid.is_set or
                    self.diffservcountactoctets.is_set or
                    self.diffservcountactpkts.is_set or
                    self.diffservcountactstatus.is_set or
                    self.diffservcountactstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservcountactid.yfilter != YFilter.not_set or
                    self.diffservcountactoctets.yfilter != YFilter.not_set or
                    self.diffservcountactpkts.yfilter != YFilter.not_set or
                    self.diffservcountactstatus.yfilter != YFilter.not_set or
                    self.diffservcountactstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServCountActEntry" + "[diffServCountActId='" + self.diffservcountactid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServCountActTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservcountactid.is_set or self.diffservcountactid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservcountactid.get_name_leafdata())
                if (self.diffservcountactoctets.is_set or self.diffservcountactoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservcountactoctets.get_name_leafdata())
                if (self.diffservcountactpkts.is_set or self.diffservcountactpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservcountactpkts.get_name_leafdata())
                if (self.diffservcountactstatus.is_set or self.diffservcountactstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservcountactstatus.get_name_leafdata())
                if (self.diffservcountactstorage.is_set or self.diffservcountactstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservcountactstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServCountActId" or name == "diffServCountActOctets" or name == "diffServCountActPkts" or name == "diffServCountActStatus" or name == "diffServCountActStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServCountActId"):
                    self.diffservcountactid = value
                    self.diffservcountactid.value_namespace = name_space
                    self.diffservcountactid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServCountActOctets"):
                    self.diffservcountactoctets = value
                    self.diffservcountactoctets.value_namespace = name_space
                    self.diffservcountactoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServCountActPkts"):
                    self.diffservcountactpkts = value
                    self.diffservcountactpkts.value_namespace = name_space
                    self.diffservcountactpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServCountActStatus"):
                    self.diffservcountactstatus = value
                    self.diffservcountactstatus.value_namespace = name_space
                    self.diffservcountactstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServCountActStorage"):
                    self.diffservcountactstorage = value
                    self.diffservcountactstorage.value_namespace = name_space
                    self.diffservcountactstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservcountactentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservcountactentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServCountActTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServCountActEntry"):
                for c in self.diffservcountactentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservcountacttable.Diffservcountactentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservcountactentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServCountActEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservalgdroptable(Entity):
        """
        The algorithmic drop table contains entries describing an
        element that drops packets according to some algorithm.
        
        .. attribute:: diffservalgdropentry
        
        	An entry describes a process that drops packets according to some algorithm. Further details of the algorithm type are to be found in diffServAlgDropType and with more detail parameter entry pointed to by diffServAlgDropSpecific when necessary
        	**type**\: list of    :py:class:`Diffservalgdropentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservalgdroptable.Diffservalgdropentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservalgdroptable, self).__init__()

            self.yang_name = "diffServAlgDropTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservalgdropentry = YList(self)

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
                        super(DiffservMib.Diffservalgdroptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservalgdroptable, self).__setattr__(name, value)


        class Diffservalgdropentry(Entity):
            """
            An entry describes a process that drops packets according to
            some algorithm. Further details of the algorithm type are to be
            found in diffServAlgDropType and with more detail parameter entry
            pointed to by diffServAlgDropSpecific when necessary.
            
            .. attribute:: diffservalgdropid  <key>
            
            	An index that enumerates the Algorithmic Dropper entries. Managers obtain new values for row creation in this table by reading diffServAlgDropNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservalgdropnext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  When diffServAlgDropType is alwaysDrop(5), this object is ignored.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropoctets
            
            	The number of octets that have been deterministically dropped by this drop process.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgdroppkts
            
            	The number of packets that have been deterministically dropped by this drop process.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgdropqmeasure
            
            	Points to an entry in the diffServQTable to indicate the queue that a drop algorithm is to monitor when deciding whether to drop a packet. If the row pointed to does not exist, the algorithmic dropper element is considered inactive.    Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropqthreshold
            
            	A threshold on the depth in bytes of the queue being measured at which a trigger is generated to the dropping algorithm, unless diffServAlgDropType is alwaysDrop(5) where this object is ignored.  For the tailDrop(2) or headDrop(3) algorithms, this represents the depth of the queue, pointed to by diffServAlgDropQMeasure, at which the drop action will take place. Other algorithms will need to define their own semantics for this threshold
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: Bytes
            
            .. attribute:: diffservalgdropspecific
            
            	Points to a table entry that provides further detail regarding a drop algorithm.  Entries with diffServAlgDropType equal to other(1) may have this point to a table defined in another MIB module.  Entries with diffServAlgDropType equal to randomDrop(4) must have this point to an entry in diffServRandomDropTable.  For all other algorithms specified in this MIB, this should take the value zeroDotZero.  The diffServAlgDropType is authoritative for the type of the drop algorithm and the specific parameters for the drop algorithm needs to be evaluated based on the diffServAlgDropType.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservalgdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: diffservalgdroptype
            
            	The type of algorithm used by this dropper. The value other(1) requires further specification in some other MIB module.  In the tailDrop(2) algorithm, diffServAlgDropQThreshold represents the maximum depth of the queue, pointed to by diffServAlgDropQMeasure, beyond which all newly arriving packets will be dropped.  In the headDrop(3) algorithm, if a packet arrives when the current depth of the queue, pointed to by diffServAlgDropQMeasure, is at diffServAlgDropQThreshold, packets currently at the head of the queue are dropped to make room for the new packet to be enqueued at the tail of the queue.  In the randomDrop(4) algorithm, on packet arrival, an Active Queue Management algorithm is executed which may randomly drop a packet. This algorithm may be proprietary, and it may drop either the arriving packet or another packet in the queue. diffServAlgDropSpecific points to a diffServRandomDropEntry that describes the algorithm. For this algorithm,    diffServAlgDropQThreshold is understood to be the absolute maximum size of the queue and additional parameters are described in diffServRandomDropTable.  The alwaysDrop(5) algorithm is as its name specifies; always drop. In this case, the other configuration values in this Entry are not meaningful; There is no useful 'next' processing step, there is no queue, and parameters describing the queue are not useful. Therefore, diffServAlgDropNext, diffServAlgDropMeasure, and diffServAlgDropSpecific are all zeroDotZero
            	**type**\:   :py:class:`Diffservalgdroptype <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservalgdroptable.Diffservalgdropentry.Diffservalgdroptype>`
            
            .. attribute:: diffservalgrandomdropoctets
            
            	The number of octets that have been randomly dropped by this drop process.  This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgrandomdroppkts
            
            	The number of packets that have been randomly dropped by this drop process. This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservalgdroptable.Diffservalgdropentry, self).__init__()

                self.yang_name = "diffServAlgDropEntry"
                self.yang_parent_name = "diffServAlgDropTable"

                self.diffservalgdropid = YLeaf(YType.uint32, "diffServAlgDropId")

                self.diffservalgdropnext = YLeaf(YType.str, "diffServAlgDropNext")

                self.diffservalgdropoctets = YLeaf(YType.uint64, "diffServAlgDropOctets")

                self.diffservalgdroppkts = YLeaf(YType.uint64, "diffServAlgDropPkts")

                self.diffservalgdropqmeasure = YLeaf(YType.str, "diffServAlgDropQMeasure")

                self.diffservalgdropqthreshold = YLeaf(YType.uint32, "diffServAlgDropQThreshold")

                self.diffservalgdropspecific = YLeaf(YType.str, "diffServAlgDropSpecific")

                self.diffservalgdropstatus = YLeaf(YType.enumeration, "diffServAlgDropStatus")

                self.diffservalgdropstorage = YLeaf(YType.enumeration, "diffServAlgDropStorage")

                self.diffservalgdroptype = YLeaf(YType.enumeration, "diffServAlgDropType")

                self.diffservalgrandomdropoctets = YLeaf(YType.uint64, "diffServAlgRandomDropOctets")

                self.diffservalgrandomdroppkts = YLeaf(YType.uint64, "diffServAlgRandomDropPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservalgdropid",
                                "diffservalgdropnext",
                                "diffservalgdropoctets",
                                "diffservalgdroppkts",
                                "diffservalgdropqmeasure",
                                "diffservalgdropqthreshold",
                                "diffservalgdropspecific",
                                "diffservalgdropstatus",
                                "diffservalgdropstorage",
                                "diffservalgdroptype",
                                "diffservalgrandomdropoctets",
                                "diffservalgrandomdroppkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservalgdroptable.Diffservalgdropentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservalgdroptable.Diffservalgdropentry, self).__setattr__(name, value)

            class Diffservalgdroptype(Enum):
                """
                Diffservalgdroptype

                The type of algorithm used by this dropper. The value other(1)

                requires further specification in some other MIB module.

                In the tailDrop(2) algorithm, diffServAlgDropQThreshold

                represents the maximum depth of the queue, pointed to by

                diffServAlgDropQMeasure, beyond which all newly arriving packets

                will be dropped.

                In the headDrop(3) algorithm, if a packet arrives when the

                current depth of the queue, pointed to by

                diffServAlgDropQMeasure, is at diffServAlgDropQThreshold, packets

                currently at the head of the queue are dropped to make room for

                the new packet to be enqueued at the tail of the queue.

                In the randomDrop(4) algorithm, on packet arrival, an Active

                Queue Management algorithm is executed which may randomly drop a

                packet. This algorithm may be proprietary, and it may drop either

                the arriving packet or another packet in the queue.

                diffServAlgDropSpecific points to a diffServRandomDropEntry that

                describes the algorithm. For this algorithm,

                diffServAlgDropQThreshold is understood to be the absolute

                maximum size of the queue and additional parameters are described

                in diffServRandomDropTable.

                The alwaysDrop(5) algorithm is as its name specifies; always

                drop. In this case, the other configuration values in this Entry

                are not meaningful; There is no useful 'next' processing step,

                there is no queue, and parameters describing the queue are not

                useful. Therefore, diffServAlgDropNext, diffServAlgDropMeasure,

                and diffServAlgDropSpecific are all zeroDotZero.

                .. data:: other = 1

                .. data:: tailDrop = 2

                .. data:: headDrop = 3

                .. data:: randomDrop = 4

                .. data:: alwaysDrop = 5

                """

                other = Enum.YLeaf(1, "other")

                tailDrop = Enum.YLeaf(2, "tailDrop")

                headDrop = Enum.YLeaf(3, "headDrop")

                randomDrop = Enum.YLeaf(4, "randomDrop")

                alwaysDrop = Enum.YLeaf(5, "alwaysDrop")


            def has_data(self):
                return (
                    self.diffservalgdropid.is_set or
                    self.diffservalgdropnext.is_set or
                    self.diffservalgdropoctets.is_set or
                    self.diffservalgdroppkts.is_set or
                    self.diffservalgdropqmeasure.is_set or
                    self.diffservalgdropqthreshold.is_set or
                    self.diffservalgdropspecific.is_set or
                    self.diffservalgdropstatus.is_set or
                    self.diffservalgdropstorage.is_set or
                    self.diffservalgdroptype.is_set or
                    self.diffservalgrandomdropoctets.is_set or
                    self.diffservalgrandomdroppkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservalgdropid.yfilter != YFilter.not_set or
                    self.diffservalgdropnext.yfilter != YFilter.not_set or
                    self.diffservalgdropoctets.yfilter != YFilter.not_set or
                    self.diffservalgdroppkts.yfilter != YFilter.not_set or
                    self.diffservalgdropqmeasure.yfilter != YFilter.not_set or
                    self.diffservalgdropqthreshold.yfilter != YFilter.not_set or
                    self.diffservalgdropspecific.yfilter != YFilter.not_set or
                    self.diffservalgdropstatus.yfilter != YFilter.not_set or
                    self.diffservalgdropstorage.yfilter != YFilter.not_set or
                    self.diffservalgdroptype.yfilter != YFilter.not_set or
                    self.diffservalgrandomdropoctets.yfilter != YFilter.not_set or
                    self.diffservalgrandomdroppkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServAlgDropEntry" + "[diffServAlgDropId='" + self.diffservalgdropid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServAlgDropTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservalgdropid.is_set or self.diffservalgdropid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropid.get_name_leafdata())
                if (self.diffservalgdropnext.is_set or self.diffservalgdropnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropnext.get_name_leafdata())
                if (self.diffservalgdropoctets.is_set or self.diffservalgdropoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropoctets.get_name_leafdata())
                if (self.diffservalgdroppkts.is_set or self.diffservalgdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdroppkts.get_name_leafdata())
                if (self.diffservalgdropqmeasure.is_set or self.diffservalgdropqmeasure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropqmeasure.get_name_leafdata())
                if (self.diffservalgdropqthreshold.is_set or self.diffservalgdropqthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropqthreshold.get_name_leafdata())
                if (self.diffservalgdropspecific.is_set or self.diffservalgdropspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropspecific.get_name_leafdata())
                if (self.diffservalgdropstatus.is_set or self.diffservalgdropstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropstatus.get_name_leafdata())
                if (self.diffservalgdropstorage.is_set or self.diffservalgdropstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdropstorage.get_name_leafdata())
                if (self.diffservalgdroptype.is_set or self.diffservalgdroptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgdroptype.get_name_leafdata())
                if (self.diffservalgrandomdropoctets.is_set or self.diffservalgrandomdropoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgrandomdropoctets.get_name_leafdata())
                if (self.diffservalgrandomdroppkts.is_set or self.diffservalgrandomdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservalgrandomdroppkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServAlgDropId" or name == "diffServAlgDropNext" or name == "diffServAlgDropOctets" or name == "diffServAlgDropPkts" or name == "diffServAlgDropQMeasure" or name == "diffServAlgDropQThreshold" or name == "diffServAlgDropSpecific" or name == "diffServAlgDropStatus" or name == "diffServAlgDropStorage" or name == "diffServAlgDropType" or name == "diffServAlgRandomDropOctets" or name == "diffServAlgRandomDropPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServAlgDropId"):
                    self.diffservalgdropid = value
                    self.diffservalgdropid.value_namespace = name_space
                    self.diffservalgdropid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropNext"):
                    self.diffservalgdropnext = value
                    self.diffservalgdropnext.value_namespace = name_space
                    self.diffservalgdropnext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropOctets"):
                    self.diffservalgdropoctets = value
                    self.diffservalgdropoctets.value_namespace = name_space
                    self.diffservalgdropoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropPkts"):
                    self.diffservalgdroppkts = value
                    self.diffservalgdroppkts.value_namespace = name_space
                    self.diffservalgdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropQMeasure"):
                    self.diffservalgdropqmeasure = value
                    self.diffservalgdropqmeasure.value_namespace = name_space
                    self.diffservalgdropqmeasure.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropQThreshold"):
                    self.diffservalgdropqthreshold = value
                    self.diffservalgdropqthreshold.value_namespace = name_space
                    self.diffservalgdropqthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropSpecific"):
                    self.diffservalgdropspecific = value
                    self.diffservalgdropspecific.value_namespace = name_space
                    self.diffservalgdropspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropStatus"):
                    self.diffservalgdropstatus = value
                    self.diffservalgdropstatus.value_namespace = name_space
                    self.diffservalgdropstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropStorage"):
                    self.diffservalgdropstorage = value
                    self.diffservalgdropstorage.value_namespace = name_space
                    self.diffservalgdropstorage.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgDropType"):
                    self.diffservalgdroptype = value
                    self.diffservalgdroptype.value_namespace = name_space
                    self.diffservalgdroptype.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgRandomDropOctets"):
                    self.diffservalgrandomdropoctets = value
                    self.diffservalgrandomdropoctets.value_namespace = name_space
                    self.diffservalgrandomdropoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServAlgRandomDropPkts"):
                    self.diffservalgrandomdroppkts = value
                    self.diffservalgrandomdroppkts.value_namespace = name_space
                    self.diffservalgrandomdroppkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservalgdropentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservalgdropentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServAlgDropTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServAlgDropEntry"):
                for c in self.diffservalgdropentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservalgdroptable.Diffservalgdropentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservalgdropentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServAlgDropEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservrandomdroptable(Entity):
        """
        The random drop table contains entries describing a process that
        drops packets randomly. Entries in this table are pointed to by
        diffServAlgDropSpecific.
        
        .. attribute:: diffservrandomdropentry
        
        	An entry describes a process that drops packets according to a random algorithm
        	**type**\: list of    :py:class:`Diffservrandomdropentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservrandomdroptable, self).__init__()

            self.yang_name = "diffServRandomDropTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservrandomdropentry = YList(self)

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
                        super(DiffservMib.Diffservrandomdroptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservrandomdroptable, self).__setattr__(name, value)


        class Diffservrandomdropentry(Entity):
            """
            An entry describes a process that drops packets according to a
            random algorithm.
            
            .. attribute:: diffservrandomdropid  <key>
            
            	An index that enumerates the Random Drop entries.  Managers obtain new values for row creation in this table by reading diffServRandomDropNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropmaxthreshbytes
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshPkts
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: diffservrandomdropmaxthreshpkts
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshBytes
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: packets
            
            .. attribute:: diffservrandomdropminthreshbytes
            
            	The average queue depth in bytes, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshPkts
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: diffservrandomdropminthreshpkts
            
            	The average queue depth in packets, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshBytes
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: packets
            
            .. attribute:: diffservrandomdropprobmax
            
            	The worst case random drop probability, expressed in drops per thousand packets.  For example, if in the worst case every arriving packet may be dropped (100%) for a period, this has the value 1000. Alternatively, if in the worst case only one percent (1%) of traffic may be dropped, it has the value 10
            	**type**\:  int
            
            	**range:** 0..1000
            
            .. attribute:: diffservrandomdropsamplingrate
            
            	The number of times per second the queue is sampled for queue average calculation.  A value of zero is used to mean that the queue is sampled approximately each time a packet is enqueued (or dequeued)
            	**type**\:  int
            
            	**range:** 0..1000000
            
            .. attribute:: diffservrandomdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservrandomdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: diffservrandomdropweight
            
            	The weighting of past history in affecting the Exponentially Weighted Moving Average function that calculates the current average queue depth.  The equation uses diffServRandomDropWeight/65536 as the coefficient for the new sample in the equation, and (65536 \- diffServRandomDropWeight)/65536 as the coefficient of the old value.  Implementations may limit the values of diffServRandomDropWeight to a subset of the possible range of values, such as powers of two. Doing this would facilitate implementation of the Exponentially Weighted Moving Average using shift instructions or registers
            	**type**\:  int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry, self).__init__()

                self.yang_name = "diffServRandomDropEntry"
                self.yang_parent_name = "diffServRandomDropTable"

                self.diffservrandomdropid = YLeaf(YType.uint32, "diffServRandomDropId")

                self.diffservrandomdropmaxthreshbytes = YLeaf(YType.uint32, "diffServRandomDropMaxThreshBytes")

                self.diffservrandomdropmaxthreshpkts = YLeaf(YType.uint32, "diffServRandomDropMaxThreshPkts")

                self.diffservrandomdropminthreshbytes = YLeaf(YType.uint32, "diffServRandomDropMinThreshBytes")

                self.diffservrandomdropminthreshpkts = YLeaf(YType.uint32, "diffServRandomDropMinThreshPkts")

                self.diffservrandomdropprobmax = YLeaf(YType.uint32, "diffServRandomDropProbMax")

                self.diffservrandomdropsamplingrate = YLeaf(YType.uint32, "diffServRandomDropSamplingRate")

                self.diffservrandomdropstatus = YLeaf(YType.enumeration, "diffServRandomDropStatus")

                self.diffservrandomdropstorage = YLeaf(YType.enumeration, "diffServRandomDropStorage")

                self.diffservrandomdropweight = YLeaf(YType.uint32, "diffServRandomDropWeight")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservrandomdropid",
                                "diffservrandomdropmaxthreshbytes",
                                "diffservrandomdropmaxthreshpkts",
                                "diffservrandomdropminthreshbytes",
                                "diffservrandomdropminthreshpkts",
                                "diffservrandomdropprobmax",
                                "diffservrandomdropsamplingrate",
                                "diffservrandomdropstatus",
                                "diffservrandomdropstorage",
                                "diffservrandomdropweight") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservrandomdropid.is_set or
                    self.diffservrandomdropmaxthreshbytes.is_set or
                    self.diffservrandomdropmaxthreshpkts.is_set or
                    self.diffservrandomdropminthreshbytes.is_set or
                    self.diffservrandomdropminthreshpkts.is_set or
                    self.diffservrandomdropprobmax.is_set or
                    self.diffservrandomdropsamplingrate.is_set or
                    self.diffservrandomdropstatus.is_set or
                    self.diffservrandomdropstorage.is_set or
                    self.diffservrandomdropweight.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservrandomdropid.yfilter != YFilter.not_set or
                    self.diffservrandomdropmaxthreshbytes.yfilter != YFilter.not_set or
                    self.diffservrandomdropmaxthreshpkts.yfilter != YFilter.not_set or
                    self.diffservrandomdropminthreshbytes.yfilter != YFilter.not_set or
                    self.diffservrandomdropminthreshpkts.yfilter != YFilter.not_set or
                    self.diffservrandomdropprobmax.yfilter != YFilter.not_set or
                    self.diffservrandomdropsamplingrate.yfilter != YFilter.not_set or
                    self.diffservrandomdropstatus.yfilter != YFilter.not_set or
                    self.diffservrandomdropstorage.yfilter != YFilter.not_set or
                    self.diffservrandomdropweight.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServRandomDropEntry" + "[diffServRandomDropId='" + self.diffservrandomdropid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServRandomDropTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservrandomdropid.is_set or self.diffservrandomdropid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropid.get_name_leafdata())
                if (self.diffservrandomdropmaxthreshbytes.is_set or self.diffservrandomdropmaxthreshbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropmaxthreshbytes.get_name_leafdata())
                if (self.diffservrandomdropmaxthreshpkts.is_set or self.diffservrandomdropmaxthreshpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropmaxthreshpkts.get_name_leafdata())
                if (self.diffservrandomdropminthreshbytes.is_set or self.diffservrandomdropminthreshbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropminthreshbytes.get_name_leafdata())
                if (self.diffservrandomdropminthreshpkts.is_set or self.diffservrandomdropminthreshpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropminthreshpkts.get_name_leafdata())
                if (self.diffservrandomdropprobmax.is_set or self.diffservrandomdropprobmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropprobmax.get_name_leafdata())
                if (self.diffservrandomdropsamplingrate.is_set or self.diffservrandomdropsamplingrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropsamplingrate.get_name_leafdata())
                if (self.diffservrandomdropstatus.is_set or self.diffservrandomdropstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropstatus.get_name_leafdata())
                if (self.diffservrandomdropstorage.is_set or self.diffservrandomdropstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropstorage.get_name_leafdata())
                if (self.diffservrandomdropweight.is_set or self.diffservrandomdropweight.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservrandomdropweight.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServRandomDropId" or name == "diffServRandomDropMaxThreshBytes" or name == "diffServRandomDropMaxThreshPkts" or name == "diffServRandomDropMinThreshBytes" or name == "diffServRandomDropMinThreshPkts" or name == "diffServRandomDropProbMax" or name == "diffServRandomDropSamplingRate" or name == "diffServRandomDropStatus" or name == "diffServRandomDropStorage" or name == "diffServRandomDropWeight"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServRandomDropId"):
                    self.diffservrandomdropid = value
                    self.diffservrandomdropid.value_namespace = name_space
                    self.diffservrandomdropid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropMaxThreshBytes"):
                    self.diffservrandomdropmaxthreshbytes = value
                    self.diffservrandomdropmaxthreshbytes.value_namespace = name_space
                    self.diffservrandomdropmaxthreshbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropMaxThreshPkts"):
                    self.diffservrandomdropmaxthreshpkts = value
                    self.diffservrandomdropmaxthreshpkts.value_namespace = name_space
                    self.diffservrandomdropmaxthreshpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropMinThreshBytes"):
                    self.diffservrandomdropminthreshbytes = value
                    self.diffservrandomdropminthreshbytes.value_namespace = name_space
                    self.diffservrandomdropminthreshbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropMinThreshPkts"):
                    self.diffservrandomdropminthreshpkts = value
                    self.diffservrandomdropminthreshpkts.value_namespace = name_space
                    self.diffservrandomdropminthreshpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropProbMax"):
                    self.diffservrandomdropprobmax = value
                    self.diffservrandomdropprobmax.value_namespace = name_space
                    self.diffservrandomdropprobmax.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropSamplingRate"):
                    self.diffservrandomdropsamplingrate = value
                    self.diffservrandomdropsamplingrate.value_namespace = name_space
                    self.diffservrandomdropsamplingrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropStatus"):
                    self.diffservrandomdropstatus = value
                    self.diffservrandomdropstatus.value_namespace = name_space
                    self.diffservrandomdropstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropStorage"):
                    self.diffservrandomdropstorage = value
                    self.diffservrandomdropstorage.value_namespace = name_space
                    self.diffservrandomdropstorage.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServRandomDropWeight"):
                    self.diffservrandomdropweight = value
                    self.diffservrandomdropweight.value_namespace = name_space
                    self.diffservrandomdropweight.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservrandomdropentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservrandomdropentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServRandomDropTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServRandomDropEntry"):
                for c in self.diffservrandomdropentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservrandomdropentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServRandomDropEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservqtable(Entity):
        """
        The Queue Table enumerates the individual queues.  Note that the
        MIB models queuing systems as composed of individual queues, one
        per class of traffic, even though they may in fact be structured
        as classes of traffic scheduled using a common calendar queue, or
        in other ways.
        
        .. attribute:: diffservqentry
        
        	An entry in the Queue Table describes a single queue or class of traffic
        	**type**\: list of    :py:class:`Diffservqentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservqtable.Diffservqentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservqtable, self).__init__()

            self.yang_name = "diffServQTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservqentry = YList(self)

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
                        super(DiffservMib.Diffservqtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservqtable, self).__setattr__(name, value)


        class Diffservqentry(Entity):
            """
            An entry in the Queue Table describes a single queue or class of
            traffic.
            
            .. attribute:: diffservqid  <key>
            
            	An index that enumerates the Queue entries.  Managers obtain new values for row creation in this table by reading diffServQNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservqmaxrate
            
            	This RowPointer indicates the diffServMaxRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the maximum rate is the line speed of the interface.     Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqminrate
            
            	This RowPointer indicates the diffServMinRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the minimum rate and priority is unspecified.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqnext
            
            	This selects the next Differentiated Services Scheduler.  The RowPointer must point to a diffServSchedulerEntry.  A value of zeroDotZero in this attribute indicates an incomplete diffServQEntry instance. In such a case, the entry has no operational effect, since it has no parameters to give it meaning.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservqstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservqtable.Diffservqentry, self).__init__()

                self.yang_name = "diffServQEntry"
                self.yang_parent_name = "diffServQTable"

                self.diffservqid = YLeaf(YType.uint32, "diffServQId")

                self.diffservqmaxrate = YLeaf(YType.str, "diffServQMaxRate")

                self.diffservqminrate = YLeaf(YType.str, "diffServQMinRate")

                self.diffservqnext = YLeaf(YType.str, "diffServQNext")

                self.diffservqstatus = YLeaf(YType.enumeration, "diffServQStatus")

                self.diffservqstorage = YLeaf(YType.enumeration, "diffServQStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservqid",
                                "diffservqmaxrate",
                                "diffservqminrate",
                                "diffservqnext",
                                "diffservqstatus",
                                "diffservqstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservqtable.Diffservqentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservqtable.Diffservqentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservqid.is_set or
                    self.diffservqmaxrate.is_set or
                    self.diffservqminrate.is_set or
                    self.diffservqnext.is_set or
                    self.diffservqstatus.is_set or
                    self.diffservqstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservqid.yfilter != YFilter.not_set or
                    self.diffservqmaxrate.yfilter != YFilter.not_set or
                    self.diffservqminrate.yfilter != YFilter.not_set or
                    self.diffservqnext.yfilter != YFilter.not_set or
                    self.diffservqstatus.yfilter != YFilter.not_set or
                    self.diffservqstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServQEntry" + "[diffServQId='" + self.diffservqid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServQTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservqid.is_set or self.diffservqid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqid.get_name_leafdata())
                if (self.diffservqmaxrate.is_set or self.diffservqmaxrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqmaxrate.get_name_leafdata())
                if (self.diffservqminrate.is_set or self.diffservqminrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqminrate.get_name_leafdata())
                if (self.diffservqnext.is_set or self.diffservqnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqnext.get_name_leafdata())
                if (self.diffservqstatus.is_set or self.diffservqstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqstatus.get_name_leafdata())
                if (self.diffservqstorage.is_set or self.diffservqstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservqstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServQId" or name == "diffServQMaxRate" or name == "diffServQMinRate" or name == "diffServQNext" or name == "diffServQStatus" or name == "diffServQStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServQId"):
                    self.diffservqid = value
                    self.diffservqid.value_namespace = name_space
                    self.diffservqid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServQMaxRate"):
                    self.diffservqmaxrate = value
                    self.diffservqmaxrate.value_namespace = name_space
                    self.diffservqmaxrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServQMinRate"):
                    self.diffservqminrate = value
                    self.diffservqminrate.value_namespace = name_space
                    self.diffservqminrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServQNext"):
                    self.diffservqnext = value
                    self.diffservqnext.value_namespace = name_space
                    self.diffservqnext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServQStatus"):
                    self.diffservqstatus = value
                    self.diffservqstatus.value_namespace = name_space
                    self.diffservqstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServQStorage"):
                    self.diffservqstorage = value
                    self.diffservqstorage.value_namespace = name_space
                    self.diffservqstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservqentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservqentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServQTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServQEntry"):
                for c in self.diffservqentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservqtable.Diffservqentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservqentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServQEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservschedulertable(Entity):
        """
        The Scheduler Table enumerates packet schedulers. Multiple
        scheduling algorithms can be used on a given data path, with each
        algorithm described by one diffServSchedulerEntry.
        
        .. attribute:: diffservschedulerentry
        
        	An entry in the Scheduler Table describing a single instance of a scheduling algorithm
        	**type**\: list of    :py:class:`Diffservschedulerentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservschedulertable.Diffservschedulerentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservschedulertable, self).__init__()

            self.yang_name = "diffServSchedulerTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservschedulerentry = YList(self)

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
                        super(DiffservMib.Diffservschedulertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservschedulertable, self).__setattr__(name, value)


        class Diffservschedulerentry(Entity):
            """
            An entry in the Scheduler Table describing a single instance of
            a scheduling algorithm.
            
            .. attribute:: diffservschedulerid  <key>
            
            	An index that enumerates the Scheduler entries.  Managers obtain new values for row creation in this table by reading diffServSchedulerNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservschedulermaxrate
            
            	This RowPointer indicates the entry in diffServMaxRateTable which indicates the maximum output rate from this scheduler. When more than one maximum rate applies (eg, when a multi\-rate shaper is in view), it points to the first of those rate entries. This attribute is used only when there is more than one level of scheduler.  When it has the value zeroDotZero, it indicates that no maximum rate is imposed.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulermethod
            
            	The scheduling algorithm used by this Scheduler. zeroDotZero indicates that this is unknown.  Standard values for generic algorithms\: diffServSchedulerPriority, diffServSchedulerWRR, and diffServSchedulerWFQ are specified in this MIB; additional values    may be further specified in other MIBs
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulerminrate
            
            	This RowPointer indicates the entry in diffServMinRateTable which indicates the priority or minimum output rate from this scheduler. This attribute is used only when there is more than one level of scheduler.  When it has the value zeroDotZero, it indicates that no minimum rate or priority is imposed.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulernext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This normally is null (zeroDotZero), or points to a diffServSchedulerEntry or a diffServQEntry.  However, this RowPointer may also point to an instance of\:   diffServClfrEntry,   diffServMeterEntry,   diffServActionEntry,   diffServAlgDropEntry.  It would point another diffServSchedulerEntry when implementing multiple scheduler methods for the same data path, such as having one set of queues scheduled by WRR and that group participating in a priority scheduling system in which other queues compete with it in that way.  It might also point to a second scheduler in a hierarchical scheduling system.  If the row pointed to is zeroDotZero, no further Differentiated Services treatment is performed on traffic of this data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulerstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservschedulerstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservschedulertable.Diffservschedulerentry, self).__init__()

                self.yang_name = "diffServSchedulerEntry"
                self.yang_parent_name = "diffServSchedulerTable"

                self.diffservschedulerid = YLeaf(YType.uint32, "diffServSchedulerId")

                self.diffservschedulermaxrate = YLeaf(YType.str, "diffServSchedulerMaxRate")

                self.diffservschedulermethod = YLeaf(YType.str, "diffServSchedulerMethod")

                self.diffservschedulerminrate = YLeaf(YType.str, "diffServSchedulerMinRate")

                self.diffservschedulernext = YLeaf(YType.str, "diffServSchedulerNext")

                self.diffservschedulerstatus = YLeaf(YType.enumeration, "diffServSchedulerStatus")

                self.diffservschedulerstorage = YLeaf(YType.enumeration, "diffServSchedulerStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservschedulerid",
                                "diffservschedulermaxrate",
                                "diffservschedulermethod",
                                "diffservschedulerminrate",
                                "diffservschedulernext",
                                "diffservschedulerstatus",
                                "diffservschedulerstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservschedulertable.Diffservschedulerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservschedulertable.Diffservschedulerentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservschedulerid.is_set or
                    self.diffservschedulermaxrate.is_set or
                    self.diffservschedulermethod.is_set or
                    self.diffservschedulerminrate.is_set or
                    self.diffservschedulernext.is_set or
                    self.diffservschedulerstatus.is_set or
                    self.diffservschedulerstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservschedulerid.yfilter != YFilter.not_set or
                    self.diffservschedulermaxrate.yfilter != YFilter.not_set or
                    self.diffservschedulermethod.yfilter != YFilter.not_set or
                    self.diffservschedulerminrate.yfilter != YFilter.not_set or
                    self.diffservschedulernext.yfilter != YFilter.not_set or
                    self.diffservschedulerstatus.yfilter != YFilter.not_set or
                    self.diffservschedulerstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServSchedulerEntry" + "[diffServSchedulerId='" + self.diffservschedulerid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServSchedulerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservschedulerid.is_set or self.diffservschedulerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulerid.get_name_leafdata())
                if (self.diffservschedulermaxrate.is_set or self.diffservschedulermaxrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulermaxrate.get_name_leafdata())
                if (self.diffservschedulermethod.is_set or self.diffservschedulermethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulermethod.get_name_leafdata())
                if (self.diffservschedulerminrate.is_set or self.diffservschedulerminrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulerminrate.get_name_leafdata())
                if (self.diffservschedulernext.is_set or self.diffservschedulernext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulernext.get_name_leafdata())
                if (self.diffservschedulerstatus.is_set or self.diffservschedulerstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulerstatus.get_name_leafdata())
                if (self.diffservschedulerstorage.is_set or self.diffservschedulerstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservschedulerstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServSchedulerId" or name == "diffServSchedulerMaxRate" or name == "diffServSchedulerMethod" or name == "diffServSchedulerMinRate" or name == "diffServSchedulerNext" or name == "diffServSchedulerStatus" or name == "diffServSchedulerStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServSchedulerId"):
                    self.diffservschedulerid = value
                    self.diffservschedulerid.value_namespace = name_space
                    self.diffservschedulerid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerMaxRate"):
                    self.diffservschedulermaxrate = value
                    self.diffservschedulermaxrate.value_namespace = name_space
                    self.diffservschedulermaxrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerMethod"):
                    self.diffservschedulermethod = value
                    self.diffservschedulermethod.value_namespace = name_space
                    self.diffservschedulermethod.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerMinRate"):
                    self.diffservschedulerminrate = value
                    self.diffservschedulerminrate.value_namespace = name_space
                    self.diffservschedulerminrate.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerNext"):
                    self.diffservschedulernext = value
                    self.diffservschedulernext.value_namespace = name_space
                    self.diffservschedulernext.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerStatus"):
                    self.diffservschedulerstatus = value
                    self.diffservschedulerstatus.value_namespace = name_space
                    self.diffservschedulerstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServSchedulerStorage"):
                    self.diffservschedulerstorage = value
                    self.diffservschedulerstorage.value_namespace = name_space
                    self.diffservschedulerstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservschedulerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservschedulerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServSchedulerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServSchedulerEntry"):
                for c in self.diffservschedulerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservschedulertable.Diffservschedulerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservschedulerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServSchedulerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservminratetable(Entity):
        """
        The Minimum Rate Parameters Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservminrateentry
        
        	An entry in the Minimum Rate Parameters Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of    :py:class:`Diffservminrateentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservminratetable.Diffservminrateentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservminratetable, self).__init__()

            self.yang_name = "diffServMinRateTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservminrateentry = YList(self)

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
                        super(DiffservMib.Diffservminratetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservminratetable, self).__setattr__(name, value)


        class Diffservminrateentry(Entity):
            """
            An entry in the Minimum Rate Parameters Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservminrateid  <key>
            
            	An index that enumerates the Scheduler Parameter entries. Managers obtain new values for row creation in this table by reading diffServMinRateNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminrateabsolute
            
            	The minimum absolute rate, in kilobits/sec, that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservminratepriority
            
            	The priority of this input to the associated scheduler, relative    to the scheduler's other inputs. A queue or scheduler with a larger numeric value will be served before another with a smaller numeric value
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminraterelative
            
            	The minimum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:      diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservminratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservminratetable.Diffservminrateentry, self).__init__()

                self.yang_name = "diffServMinRateEntry"
                self.yang_parent_name = "diffServMinRateTable"

                self.diffservminrateid = YLeaf(YType.uint32, "diffServMinRateId")

                self.diffservminrateabsolute = YLeaf(YType.uint32, "diffServMinRateAbsolute")

                self.diffservminratepriority = YLeaf(YType.uint32, "diffServMinRatePriority")

                self.diffservminraterelative = YLeaf(YType.uint32, "diffServMinRateRelative")

                self.diffservminratestatus = YLeaf(YType.enumeration, "diffServMinRateStatus")

                self.diffservminratestorage = YLeaf(YType.enumeration, "diffServMinRateStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservminrateid",
                                "diffservminrateabsolute",
                                "diffservminratepriority",
                                "diffservminraterelative",
                                "diffservminratestatus",
                                "diffservminratestorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservminratetable.Diffservminrateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservminratetable.Diffservminrateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservminrateid.is_set or
                    self.diffservminrateabsolute.is_set or
                    self.diffservminratepriority.is_set or
                    self.diffservminraterelative.is_set or
                    self.diffservminratestatus.is_set or
                    self.diffservminratestorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservminrateid.yfilter != YFilter.not_set or
                    self.diffservminrateabsolute.yfilter != YFilter.not_set or
                    self.diffservminratepriority.yfilter != YFilter.not_set or
                    self.diffservminraterelative.yfilter != YFilter.not_set or
                    self.diffservminratestatus.yfilter != YFilter.not_set or
                    self.diffservminratestorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServMinRateEntry" + "[diffServMinRateId='" + self.diffservminrateid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServMinRateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservminrateid.is_set or self.diffservminrateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminrateid.get_name_leafdata())
                if (self.diffservminrateabsolute.is_set or self.diffservminrateabsolute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminrateabsolute.get_name_leafdata())
                if (self.diffservminratepriority.is_set or self.diffservminratepriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminratepriority.get_name_leafdata())
                if (self.diffservminraterelative.is_set or self.diffservminraterelative.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminraterelative.get_name_leafdata())
                if (self.diffservminratestatus.is_set or self.diffservminratestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminratestatus.get_name_leafdata())
                if (self.diffservminratestorage.is_set or self.diffservminratestorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservminratestorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServMinRateId" or name == "diffServMinRateAbsolute" or name == "diffServMinRatePriority" or name == "diffServMinRateRelative" or name == "diffServMinRateStatus" or name == "diffServMinRateStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServMinRateId"):
                    self.diffservminrateid = value
                    self.diffservminrateid.value_namespace = name_space
                    self.diffservminrateid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMinRateAbsolute"):
                    self.diffservminrateabsolute = value
                    self.diffservminrateabsolute.value_namespace = name_space
                    self.diffservminrateabsolute.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMinRatePriority"):
                    self.diffservminratepriority = value
                    self.diffservminratepriority.value_namespace = name_space
                    self.diffservminratepriority.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMinRateRelative"):
                    self.diffservminraterelative = value
                    self.diffservminraterelative.value_namespace = name_space
                    self.diffservminraterelative.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMinRateStatus"):
                    self.diffservminratestatus = value
                    self.diffservminratestatus.value_namespace = name_space
                    self.diffservminratestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMinRateStorage"):
                    self.diffservminratestorage = value
                    self.diffservminratestorage.value_namespace = name_space
                    self.diffservminratestorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservminrateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservminrateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServMinRateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServMinRateEntry"):
                for c in self.diffservminrateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservminratetable.Diffservminrateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservminrateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMinRateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diffservmaxratetable(Entity):
        """
        The Maximum Rate Parameter Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservmaxrateentry
        
        	An entry in the Maximum Rate Parameter Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of    :py:class:`Diffservmaxrateentry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DiffservMib.Diffservmaxratetable.Diffservmaxrateentry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DiffservMib.Diffservmaxratetable, self).__init__()

            self.yang_name = "diffServMaxRateTable"
            self.yang_parent_name = "DIFFSERV-MIB"

            self.diffservmaxrateentry = YList(self)

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
                        super(DiffservMib.Diffservmaxratetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservMib.Diffservmaxratetable, self).__setattr__(name, value)


        class Diffservmaxrateentry(Entity):
            """
            An entry in the Maximum Rate Parameter Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservmaxrateid  <key>
            
            	An index that enumerates the Maximum Rate Parameter entries. Managers obtain new values for row creation in this table by reading diffServMaxRateNextFree
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratelevel  <key>
            
            	An index that indicates which level of a multi\-rate shaper is being given its parameters. A multi\-rate shaper has some number of rate levels. Frame Relay's dual rate specification refers to a 'committed' and an 'excess' rate; ATM's dual rate specification refers to a 'mean' and a 'peak' rate. This table is generalized to support an arbitrary number of rates. The committed or mean rate is level 1, the peak rate (if any) is the highest level rate configured, and if there are other rates they are distributed in monotonically increasing order between them
            	**type**\:  int
            
            	**range:** 1..32
            
            .. attribute:: diffservmaxrateabsolute
            
            	The maximum rate in kilobits/sec that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no maximum rate limit and that the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following    equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservmaxraterelative
            
            	The maximum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no maximum rate limit and the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: diffservmaxratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: diffservmaxratethreshold
            
            	The number of bytes of queue depth at which the rate of a    multi\-rate scheduler will increase to the next output rate. In the last conceptual row for such a shaper, this threshold is ignored and by convention is zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DiffservMib.Diffservmaxratetable.Diffservmaxrateentry, self).__init__()

                self.yang_name = "diffServMaxRateEntry"
                self.yang_parent_name = "diffServMaxRateTable"

                self.diffservmaxrateid = YLeaf(YType.uint32, "diffServMaxRateId")

                self.diffservmaxratelevel = YLeaf(YType.uint32, "diffServMaxRateLevel")

                self.diffservmaxrateabsolute = YLeaf(YType.uint32, "diffServMaxRateAbsolute")

                self.diffservmaxraterelative = YLeaf(YType.uint32, "diffServMaxRateRelative")

                self.diffservmaxratestatus = YLeaf(YType.enumeration, "diffServMaxRateStatus")

                self.diffservmaxratestorage = YLeaf(YType.enumeration, "diffServMaxRateStorage")

                self.diffservmaxratethreshold = YLeaf(YType.int32, "diffServMaxRateThreshold")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diffservmaxrateid",
                                "diffservmaxratelevel",
                                "diffservmaxrateabsolute",
                                "diffservmaxraterelative",
                                "diffservmaxratestatus",
                                "diffservmaxratestorage",
                                "diffservmaxratethreshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservMib.Diffservmaxratetable.Diffservmaxrateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservMib.Diffservmaxratetable.Diffservmaxrateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diffservmaxrateid.is_set or
                    self.diffservmaxratelevel.is_set or
                    self.diffservmaxrateabsolute.is_set or
                    self.diffservmaxraterelative.is_set or
                    self.diffservmaxratestatus.is_set or
                    self.diffservmaxratestorage.is_set or
                    self.diffservmaxratethreshold.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diffservmaxrateid.yfilter != YFilter.not_set or
                    self.diffservmaxratelevel.yfilter != YFilter.not_set or
                    self.diffservmaxrateabsolute.yfilter != YFilter.not_set or
                    self.diffservmaxraterelative.yfilter != YFilter.not_set or
                    self.diffservmaxratestatus.yfilter != YFilter.not_set or
                    self.diffservmaxratestorage.yfilter != YFilter.not_set or
                    self.diffservmaxratethreshold.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffServMaxRateEntry" + "[diffServMaxRateId='" + self.diffservmaxrateid.get() + "']" + "[diffServMaxRateLevel='" + self.diffservmaxratelevel.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/diffServMaxRateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diffservmaxrateid.is_set or self.diffservmaxrateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxrateid.get_name_leafdata())
                if (self.diffservmaxratelevel.is_set or self.diffservmaxratelevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxratelevel.get_name_leafdata())
                if (self.diffservmaxrateabsolute.is_set or self.diffservmaxrateabsolute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxrateabsolute.get_name_leafdata())
                if (self.diffservmaxraterelative.is_set or self.diffservmaxraterelative.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxraterelative.get_name_leafdata())
                if (self.diffservmaxratestatus.is_set or self.diffservmaxratestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxratestatus.get_name_leafdata())
                if (self.diffservmaxratestorage.is_set or self.diffservmaxratestorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxratestorage.get_name_leafdata())
                if (self.diffservmaxratethreshold.is_set or self.diffservmaxratethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diffservmaxratethreshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffServMaxRateId" or name == "diffServMaxRateLevel" or name == "diffServMaxRateAbsolute" or name == "diffServMaxRateRelative" or name == "diffServMaxRateStatus" or name == "diffServMaxRateStorage" or name == "diffServMaxRateThreshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diffServMaxRateId"):
                    self.diffservmaxrateid = value
                    self.diffservmaxrateid.value_namespace = name_space
                    self.diffservmaxrateid.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateLevel"):
                    self.diffservmaxratelevel = value
                    self.diffservmaxratelevel.value_namespace = name_space
                    self.diffservmaxratelevel.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateAbsolute"):
                    self.diffservmaxrateabsolute = value
                    self.diffservmaxrateabsolute.value_namespace = name_space
                    self.diffservmaxrateabsolute.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateRelative"):
                    self.diffservmaxraterelative = value
                    self.diffservmaxraterelative.value_namespace = name_space
                    self.diffservmaxraterelative.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateStatus"):
                    self.diffservmaxratestatus = value
                    self.diffservmaxratestatus.value_namespace = name_space
                    self.diffservmaxratestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateStorage"):
                    self.diffservmaxratestorage = value
                    self.diffservmaxratestorage.value_namespace = name_space
                    self.diffservmaxratestorage.value_namespace_prefix = name_space_prefix
                if(value_path == "diffServMaxRateThreshold"):
                    self.diffservmaxratethreshold = value
                    self.diffservmaxratethreshold.value_namespace = name_space
                    self.diffservmaxratethreshold.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffservmaxrateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.diffservmaxrateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffServMaxRateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffServMaxRateEntry"):
                for c in self.diffservmaxrateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservMib.Diffservmaxratetable.Diffservmaxrateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffservmaxrateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffServMaxRateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.diffservaction is not None and self.diffservaction.has_data()) or
            (self.diffservactiontable is not None and self.diffservactiontable.has_data()) or
            (self.diffservalgdrop is not None and self.diffservalgdrop.has_data()) or
            (self.diffservalgdroptable is not None and self.diffservalgdroptable.has_data()) or
            (self.diffservclassifier is not None and self.diffservclassifier.has_data()) or
            (self.diffservclfrelementtable is not None and self.diffservclfrelementtable.has_data()) or
            (self.diffservclfrtable is not None and self.diffservclfrtable.has_data()) or
            (self.diffservcountacttable is not None and self.diffservcountacttable.has_data()) or
            (self.diffservdatapathtable is not None and self.diffservdatapathtable.has_data()) or
            (self.diffservdscpmarkacttable is not None and self.diffservdscpmarkacttable.has_data()) or
            (self.diffservmaxratetable is not None and self.diffservmaxratetable.has_data()) or
            (self.diffservmeter is not None and self.diffservmeter.has_data()) or
            (self.diffservmetertable is not None and self.diffservmetertable.has_data()) or
            (self.diffservminratetable is not None and self.diffservminratetable.has_data()) or
            (self.diffservmultifieldclfrtable is not None and self.diffservmultifieldclfrtable.has_data()) or
            (self.diffservqtable is not None and self.diffservqtable.has_data()) or
            (self.diffservqueue is not None and self.diffservqueue.has_data()) or
            (self.diffservrandomdroptable is not None and self.diffservrandomdroptable.has_data()) or
            (self.diffservscheduler is not None and self.diffservscheduler.has_data()) or
            (self.diffservschedulertable is not None and self.diffservschedulertable.has_data()) or
            (self.diffservtbparam is not None and self.diffservtbparam.has_data()) or
            (self.diffservtbparamtable is not None and self.diffservtbparamtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.diffservaction is not None and self.diffservaction.has_operation()) or
            (self.diffservactiontable is not None and self.diffservactiontable.has_operation()) or
            (self.diffservalgdrop is not None and self.diffservalgdrop.has_operation()) or
            (self.diffservalgdroptable is not None and self.diffservalgdroptable.has_operation()) or
            (self.diffservclassifier is not None and self.diffservclassifier.has_operation()) or
            (self.diffservclfrelementtable is not None and self.diffservclfrelementtable.has_operation()) or
            (self.diffservclfrtable is not None and self.diffservclfrtable.has_operation()) or
            (self.diffservcountacttable is not None and self.diffservcountacttable.has_operation()) or
            (self.diffservdatapathtable is not None and self.diffservdatapathtable.has_operation()) or
            (self.diffservdscpmarkacttable is not None and self.diffservdscpmarkacttable.has_operation()) or
            (self.diffservmaxratetable is not None and self.diffservmaxratetable.has_operation()) or
            (self.diffservmeter is not None and self.diffservmeter.has_operation()) or
            (self.diffservmetertable is not None and self.diffservmetertable.has_operation()) or
            (self.diffservminratetable is not None and self.diffservminratetable.has_operation()) or
            (self.diffservmultifieldclfrtable is not None and self.diffservmultifieldclfrtable.has_operation()) or
            (self.diffservqtable is not None and self.diffservqtable.has_operation()) or
            (self.diffservqueue is not None and self.diffservqueue.has_operation()) or
            (self.diffservrandomdroptable is not None and self.diffservrandomdroptable.has_operation()) or
            (self.diffservscheduler is not None and self.diffservscheduler.has_operation()) or
            (self.diffservschedulertable is not None and self.diffservschedulertable.has_operation()) or
            (self.diffservtbparam is not None and self.diffservtbparam.has_operation()) or
            (self.diffservtbparamtable is not None and self.diffservtbparamtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DIFFSERV-MIB:DIFFSERV-MIB" + path_buffer

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

        if (child_yang_name == "diffServAction"):
            if (self.diffservaction is None):
                self.diffservaction = DiffservMib.Diffservaction()
                self.diffservaction.parent = self
                self._children_name_map["diffservaction"] = "diffServAction"
            return self.diffservaction

        if (child_yang_name == "diffServActionTable"):
            if (self.diffservactiontable is None):
                self.diffservactiontable = DiffservMib.Diffservactiontable()
                self.diffservactiontable.parent = self
                self._children_name_map["diffservactiontable"] = "diffServActionTable"
            return self.diffservactiontable

        if (child_yang_name == "diffServAlgDrop"):
            if (self.diffservalgdrop is None):
                self.diffservalgdrop = DiffservMib.Diffservalgdrop()
                self.diffservalgdrop.parent = self
                self._children_name_map["diffservalgdrop"] = "diffServAlgDrop"
            return self.diffservalgdrop

        if (child_yang_name == "diffServAlgDropTable"):
            if (self.diffservalgdroptable is None):
                self.diffservalgdroptable = DiffservMib.Diffservalgdroptable()
                self.diffservalgdroptable.parent = self
                self._children_name_map["diffservalgdroptable"] = "diffServAlgDropTable"
            return self.diffservalgdroptable

        if (child_yang_name == "diffServClassifier"):
            if (self.diffservclassifier is None):
                self.diffservclassifier = DiffservMib.Diffservclassifier()
                self.diffservclassifier.parent = self
                self._children_name_map["diffservclassifier"] = "diffServClassifier"
            return self.diffservclassifier

        if (child_yang_name == "diffServClfrElementTable"):
            if (self.diffservclfrelementtable is None):
                self.diffservclfrelementtable = DiffservMib.Diffservclfrelementtable()
                self.diffservclfrelementtable.parent = self
                self._children_name_map["diffservclfrelementtable"] = "diffServClfrElementTable"
            return self.diffservclfrelementtable

        if (child_yang_name == "diffServClfrTable"):
            if (self.diffservclfrtable is None):
                self.diffservclfrtable = DiffservMib.Diffservclfrtable()
                self.diffservclfrtable.parent = self
                self._children_name_map["diffservclfrtable"] = "diffServClfrTable"
            return self.diffservclfrtable

        if (child_yang_name == "diffServCountActTable"):
            if (self.diffservcountacttable is None):
                self.diffservcountacttable = DiffservMib.Diffservcountacttable()
                self.diffservcountacttable.parent = self
                self._children_name_map["diffservcountacttable"] = "diffServCountActTable"
            return self.diffservcountacttable

        if (child_yang_name == "diffServDataPathTable"):
            if (self.diffservdatapathtable is None):
                self.diffservdatapathtable = DiffservMib.Diffservdatapathtable()
                self.diffservdatapathtable.parent = self
                self._children_name_map["diffservdatapathtable"] = "diffServDataPathTable"
            return self.diffservdatapathtable

        if (child_yang_name == "diffServDscpMarkActTable"):
            if (self.diffservdscpmarkacttable is None):
                self.diffservdscpmarkacttable = DiffservMib.Diffservdscpmarkacttable()
                self.diffservdscpmarkacttable.parent = self
                self._children_name_map["diffservdscpmarkacttable"] = "diffServDscpMarkActTable"
            return self.diffservdscpmarkacttable

        if (child_yang_name == "diffServMaxRateTable"):
            if (self.diffservmaxratetable is None):
                self.diffservmaxratetable = DiffservMib.Diffservmaxratetable()
                self.diffservmaxratetable.parent = self
                self._children_name_map["diffservmaxratetable"] = "diffServMaxRateTable"
            return self.diffservmaxratetable

        if (child_yang_name == "diffServMeter"):
            if (self.diffservmeter is None):
                self.diffservmeter = DiffservMib.Diffservmeter()
                self.diffservmeter.parent = self
                self._children_name_map["diffservmeter"] = "diffServMeter"
            return self.diffservmeter

        if (child_yang_name == "diffServMeterTable"):
            if (self.diffservmetertable is None):
                self.diffservmetertable = DiffservMib.Diffservmetertable()
                self.diffservmetertable.parent = self
                self._children_name_map["diffservmetertable"] = "diffServMeterTable"
            return self.diffservmetertable

        if (child_yang_name == "diffServMinRateTable"):
            if (self.diffservminratetable is None):
                self.diffservminratetable = DiffservMib.Diffservminratetable()
                self.diffservminratetable.parent = self
                self._children_name_map["diffservminratetable"] = "diffServMinRateTable"
            return self.diffservminratetable

        if (child_yang_name == "diffServMultiFieldClfrTable"):
            if (self.diffservmultifieldclfrtable is None):
                self.diffservmultifieldclfrtable = DiffservMib.Diffservmultifieldclfrtable()
                self.diffservmultifieldclfrtable.parent = self
                self._children_name_map["diffservmultifieldclfrtable"] = "diffServMultiFieldClfrTable"
            return self.diffservmultifieldclfrtable

        if (child_yang_name == "diffServQTable"):
            if (self.diffservqtable is None):
                self.diffservqtable = DiffservMib.Diffservqtable()
                self.diffservqtable.parent = self
                self._children_name_map["diffservqtable"] = "diffServQTable"
            return self.diffservqtable

        if (child_yang_name == "diffServQueue"):
            if (self.diffservqueue is None):
                self.diffservqueue = DiffservMib.Diffservqueue()
                self.diffservqueue.parent = self
                self._children_name_map["diffservqueue"] = "diffServQueue"
            return self.diffservqueue

        if (child_yang_name == "diffServRandomDropTable"):
            if (self.diffservrandomdroptable is None):
                self.diffservrandomdroptable = DiffservMib.Diffservrandomdroptable()
                self.diffservrandomdroptable.parent = self
                self._children_name_map["diffservrandomdroptable"] = "diffServRandomDropTable"
            return self.diffservrandomdroptable

        if (child_yang_name == "diffServScheduler"):
            if (self.diffservscheduler is None):
                self.diffservscheduler = DiffservMib.Diffservscheduler()
                self.diffservscheduler.parent = self
                self._children_name_map["diffservscheduler"] = "diffServScheduler"
            return self.diffservscheduler

        if (child_yang_name == "diffServSchedulerTable"):
            if (self.diffservschedulertable is None):
                self.diffservschedulertable = DiffservMib.Diffservschedulertable()
                self.diffservschedulertable.parent = self
                self._children_name_map["diffservschedulertable"] = "diffServSchedulerTable"
            return self.diffservschedulertable

        if (child_yang_name == "diffServTBParam"):
            if (self.diffservtbparam is None):
                self.diffservtbparam = DiffservMib.Diffservtbparam()
                self.diffservtbparam.parent = self
                self._children_name_map["diffservtbparam"] = "diffServTBParam"
            return self.diffservtbparam

        if (child_yang_name == "diffServTBParamTable"):
            if (self.diffservtbparamtable is None):
                self.diffservtbparamtable = DiffservMib.Diffservtbparamtable()
                self.diffservtbparamtable.parent = self
                self._children_name_map["diffservtbparamtable"] = "diffServTBParamTable"
            return self.diffservtbparamtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "diffServAction" or name == "diffServActionTable" or name == "diffServAlgDrop" or name == "diffServAlgDropTable" or name == "diffServClassifier" or name == "diffServClfrElementTable" or name == "diffServClfrTable" or name == "diffServCountActTable" or name == "diffServDataPathTable" or name == "diffServDscpMarkActTable" or name == "diffServMaxRateTable" or name == "diffServMeter" or name == "diffServMeterTable" or name == "diffServMinRateTable" or name == "diffServMultiFieldClfrTable" or name == "diffServQTable" or name == "diffServQueue" or name == "diffServRandomDropTable" or name == "diffServScheduler" or name == "diffServSchedulerTable" or name == "diffServTBParam" or name == "diffServTBParamTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DiffservMib()
        return self._top_entity

