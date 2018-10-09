""" DIFFSERV_MIB 

This MIB defines the objects necessary to manage a device that
uses the Differentiated Services Architecture described in RFC
2475. The Conceptual Model of a Differentiated Services Router
provides supporting information on how such a router is modeled.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity


class IfDirection(Enum):
    """
    IfDirection (Enum Class)

    IfDirection specifies a direction of data travel on an

    interface. 'inbound' traffic is operated on during reception from

    the interface, while 'outbound' traffic is operated on prior to

    transmission on the interface.

    .. data:: inbound = 1

    .. data:: outbound = 2

    """

    inbound = Enum.YLeaf(1, "inbound")

    outbound = Enum.YLeaf(2, "outbound")



class DiffServTBParamTrTCMBlind(ObjectIdentity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamTrTCMBlind"):
        super(DiffServTBParamTrTCMBlind, self).__init__(ns, pref, tag)


class DiffServSchedulerWFQ(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServSchedulerWFQ"):
        super(DiffServSchedulerWFQ, self).__init__(ns, pref, tag)


class DiffServTBParamTswTCM(ObjectIdentity):
    """
    Time Sliding Window Three Color Marker Metering as defined by
    RFC 2859.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamTswTCM"):
        super(DiffServTBParamTswTCM, self).__init__(ns, pref, tag)


class DiffServTBParamAvgRate(ObjectIdentity):
    """
    Average Rate Meter as described in the Informal Differentiated
    Services Model section 5.2.1.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamAvgRate"):
        super(DiffServTBParamAvgRate, self).__init__(ns, pref, tag)


class DiffServSchedulerWRR(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServSchedulerWRR"):
        super(DiffServSchedulerWRR, self).__init__(ns, pref, tag)


class DiffServTBParamSrTCMAware(ObjectIdentity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamSrTCMAware"):
        super(DiffServTBParamSrTCMAware, self).__init__(ns, pref, tag)


class DiffServTBParamSrTCMBlind(ObjectIdentity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamSrTCMBlind"):
        super(DiffServTBParamSrTCMBlind, self).__init__(ns, pref, tag)


class DiffServTBParamSimpleTokenBucket(ObjectIdentity):
    """
    Two Parameter Token Bucket Meter as described in the Informal
    Differentiated Services Model section 5.2.3.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamSimpleTokenBucket"):
        super(DiffServTBParamSimpleTokenBucket, self).__init__(ns, pref, tag)


class DiffServSchedulerPriority(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServSchedulerPriority"):
        super(DiffServSchedulerPriority, self).__init__(ns, pref, tag)


class DiffServTBParamTrTCMAware(ObjectIdentity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:DIFFSERV-MIB", pref="DIFFSERV-MIB", tag="DIFFSERV-MIB:diffServTBParamTrTCMAware"):
        super(DiffServTBParamTrTCMAware, self).__init__(ns, pref, tag)


class DIFFSERVMIB(Entity):
    """
    
    
    .. attribute:: diffservclassifier
    
    	
    	**type**\:  :py:class:`DiffServClassifier <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClassifier>`
    
    .. attribute:: diffservmeter
    
    	
    	**type**\:  :py:class:`DiffServMeter <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeter>`
    
    .. attribute:: diffservtbparam
    
    	
    	**type**\:  :py:class:`DiffServTBParam <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParam>`
    
    .. attribute:: diffservaction
    
    	
    	**type**\:  :py:class:`DiffServAction <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServAction>`
    
    .. attribute:: diffservalgdrop
    
    	
    	**type**\:  :py:class:`DiffServAlgDrop <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDrop>`
    
    .. attribute:: diffservqueue
    
    	
    	**type**\:  :py:class:`DiffServQueue <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServQueue>`
    
    .. attribute:: diffservscheduler
    
    	
    	**type**\:  :py:class:`DiffServScheduler <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServScheduler>`
    
    .. attribute:: diffservdatapathtable
    
    	The data path table contains RowPointers indicating the start of the functional data path for each interface and traffic direction in this device. These may merge, or be separated into parallel data paths
    	**type**\:  :py:class:`DiffServDataPathTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServDataPathTable>`
    
    .. attribute:: diffservclfrtable
    
    	This table enumerates all the diffserv classifier functional data path elements of this device.  The actual classification definitions are defined in diffServClfrElementTable entries belonging to each classifier.  An entry in this table, pointed to by a RowPointer specifying an instance of diffServClfrStatus, is frequently used as the name for a set of classifier elements, which all use the index diffServClfrId. Per the semantics of the classifier element table, these entries constitute one or more unordered sets of tests which may be simultaneously applied to a message to    classify it.  The primary function of this table is to ensure that the value of diffServClfrId is unique before attempting to use it in creating a diffServClfrElementEntry. Therefore, the diffServClfrEntry must be created on the same SET as the diffServClfrElementEntry, or before the diffServClfrElementEntry is created
    	**type**\:  :py:class:`DiffServClfrTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrTable>`
    
    .. attribute:: diffservclfrelementtable
    
    	The classifier element table enumerates the relationship between classification patterns and subsequent downstream Differentiated Services Functional Data Path elements. diffServClfrElementSpecific points to a filter that specifies the classification parameters. A classifier may use filter tables of different types together.  One example of a filter table defined in this MIB is diffServMultiFieldClfrTable, for IP Multi\-Field Classifiers (MFCs). Such an entry might identify anything from a single micro\-flow (an identifiable sub\-session packet stream directed from one sending transport to the receiving transport or transports), or aggregates of those such as the traffic from a host, traffic for an application, or traffic between two hosts using an application and a given DSCP. The standard Behavior Aggregate used in the Differentiated Services Architecture is encoded as a degenerate case of such an aggregate \- the traffic using a particular DSCP value.  Filter tables for other filter types may be defined elsewhere
    	**type**\:  :py:class:`DiffServClfrElementTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrElementTable>`
    
    .. attribute:: diffservmultifieldclfrtable
    
    	A table of IP Multi\-field Classifier filter entries that a    system may use to identify IP traffic
    	**type**\:  :py:class:`DiffServMultiFieldClfrTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMultiFieldClfrTable>`
    
    .. attribute:: diffservmetertable
    
    	This table enumerates specific meters that a system may use to police a stream of traffic. The traffic stream to be metered is determined by the Differentiated Services Functional Data Path Element(s) upstream of the meter i.e. by the object(s) that point to each entry in this table.  This may include all traffic on an interface.  Specific meter details are to be found in table entry referenced by diffServMeterSpecific
    	**type**\:  :py:class:`DiffServMeterTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeterTable>`
    
    .. attribute:: diffservtbparamtable
    
    	This table enumerates a single set of token bucket meter parameters that a system may use to police a stream of traffic. Such meters are modeled here as having a single rate and a single burst size. Multiple entries are used when multiple rates/burst sizes are needed
    	**type**\:  :py:class:`DiffServTBParamTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParamTable>`
    
    .. attribute:: diffservactiontable
    
    	The Action Table enumerates actions that can be performed to a stream of traffic. Multiple actions can be concatenated. For example, traffic exiting from a meter may be counted, marked, and potentially dropped before entering a queue.  Specific actions are indicated by diffServActionSpecific which points to an entry of a specific action type parameterizing the action in detail
    	**type**\:  :py:class:`DiffServActionTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServActionTable>`
    
    .. attribute:: diffservdscpmarkacttable
    
    	This table enumerates specific DSCPs used for marking or remarking the DSCP field of IP packets. The entries of this table may be referenced by a diffServActionSpecific attribute
    	**type**\:  :py:class:`DiffServDscpMarkActTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServDscpMarkActTable>`
    
    .. attribute:: diffservcountacttable
    
    	This table contains counters for all the traffic passing through an action element
    	**type**\:  :py:class:`DiffServCountActTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServCountActTable>`
    
    .. attribute:: diffservalgdroptable
    
    	The algorithmic drop table contains entries describing an element that drops packets according to some algorithm
    	**type**\:  :py:class:`DiffServAlgDropTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable>`
    
    .. attribute:: diffservrandomdroptable
    
    	The random drop table contains entries describing a process that drops packets randomly. Entries in this table are pointed to by diffServAlgDropSpecific
    	**type**\:  :py:class:`DiffServRandomDropTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServRandomDropTable>`
    
    .. attribute:: diffservqtable
    
    	The Queue Table enumerates the individual queues.  Note that the MIB models queuing systems as composed of individual queues, one per class of traffic, even though they may in fact be structured as classes of traffic scheduled using a common calendar queue, or in other ways
    	**type**\:  :py:class:`DiffServQTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServQTable>`
    
    .. attribute:: diffservschedulertable
    
    	The Scheduler Table enumerates packet schedulers. Multiple scheduling algorithms can be used on a given data path, with each algorithm described by one diffServSchedulerEntry
    	**type**\:  :py:class:`DiffServSchedulerTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServSchedulerTable>`
    
    .. attribute:: diffservminratetable
    
    	The Minimum Rate Parameters Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\:  :py:class:`DiffServMinRateTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMinRateTable>`
    
    .. attribute:: diffservmaxratetable
    
    	The Maximum Rate Parameter Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\:  :py:class:`DiffServMaxRateTable <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMaxRateTable>`
    
    

    """

    _prefix = 'DIFFSERV-MIB'
    _revision = '2002-02-07'

    def __init__(self):
        super(DIFFSERVMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DIFFSERV-MIB"
        self.yang_parent_name = "DIFFSERV-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("diffServClassifier", ("diffservclassifier", DIFFSERVMIB.DiffServClassifier)), ("diffServMeter", ("diffservmeter", DIFFSERVMIB.DiffServMeter)), ("diffServTBParam", ("diffservtbparam", DIFFSERVMIB.DiffServTBParam)), ("diffServAction", ("diffservaction", DIFFSERVMIB.DiffServAction)), ("diffServAlgDrop", ("diffservalgdrop", DIFFSERVMIB.DiffServAlgDrop)), ("diffServQueue", ("diffservqueue", DIFFSERVMIB.DiffServQueue)), ("diffServScheduler", ("diffservscheduler", DIFFSERVMIB.DiffServScheduler)), ("diffServDataPathTable", ("diffservdatapathtable", DIFFSERVMIB.DiffServDataPathTable)), ("diffServClfrTable", ("diffservclfrtable", DIFFSERVMIB.DiffServClfrTable)), ("diffServClfrElementTable", ("diffservclfrelementtable", DIFFSERVMIB.DiffServClfrElementTable)), ("diffServMultiFieldClfrTable", ("diffservmultifieldclfrtable", DIFFSERVMIB.DiffServMultiFieldClfrTable)), ("diffServMeterTable", ("diffservmetertable", DIFFSERVMIB.DiffServMeterTable)), ("diffServTBParamTable", ("diffservtbparamtable", DIFFSERVMIB.DiffServTBParamTable)), ("diffServActionTable", ("diffservactiontable", DIFFSERVMIB.DiffServActionTable)), ("diffServDscpMarkActTable", ("diffservdscpmarkacttable", DIFFSERVMIB.DiffServDscpMarkActTable)), ("diffServCountActTable", ("diffservcountacttable", DIFFSERVMIB.DiffServCountActTable)), ("diffServAlgDropTable", ("diffservalgdroptable", DIFFSERVMIB.DiffServAlgDropTable)), ("diffServRandomDropTable", ("diffservrandomdroptable", DIFFSERVMIB.DiffServRandomDropTable)), ("diffServQTable", ("diffservqtable", DIFFSERVMIB.DiffServQTable)), ("diffServSchedulerTable", ("diffservschedulertable", DIFFSERVMIB.DiffServSchedulerTable)), ("diffServMinRateTable", ("diffservminratetable", DIFFSERVMIB.DiffServMinRateTable)), ("diffServMaxRateTable", ("diffservmaxratetable", DIFFSERVMIB.DiffServMaxRateTable))])
        self._leafs = OrderedDict()

        self.diffservclassifier = DIFFSERVMIB.DiffServClassifier()
        self.diffservclassifier.parent = self
        self._children_name_map["diffservclassifier"] = "diffServClassifier"

        self.diffservmeter = DIFFSERVMIB.DiffServMeter()
        self.diffservmeter.parent = self
        self._children_name_map["diffservmeter"] = "diffServMeter"

        self.diffservtbparam = DIFFSERVMIB.DiffServTBParam()
        self.diffservtbparam.parent = self
        self._children_name_map["diffservtbparam"] = "diffServTBParam"

        self.diffservaction = DIFFSERVMIB.DiffServAction()
        self.diffservaction.parent = self
        self._children_name_map["diffservaction"] = "diffServAction"

        self.diffservalgdrop = DIFFSERVMIB.DiffServAlgDrop()
        self.diffservalgdrop.parent = self
        self._children_name_map["diffservalgdrop"] = "diffServAlgDrop"

        self.diffservqueue = DIFFSERVMIB.DiffServQueue()
        self.diffservqueue.parent = self
        self._children_name_map["diffservqueue"] = "diffServQueue"

        self.diffservscheduler = DIFFSERVMIB.DiffServScheduler()
        self.diffservscheduler.parent = self
        self._children_name_map["diffservscheduler"] = "diffServScheduler"

        self.diffservdatapathtable = DIFFSERVMIB.DiffServDataPathTable()
        self.diffservdatapathtable.parent = self
        self._children_name_map["diffservdatapathtable"] = "diffServDataPathTable"

        self.diffservclfrtable = DIFFSERVMIB.DiffServClfrTable()
        self.diffservclfrtable.parent = self
        self._children_name_map["diffservclfrtable"] = "diffServClfrTable"

        self.diffservclfrelementtable = DIFFSERVMIB.DiffServClfrElementTable()
        self.diffservclfrelementtable.parent = self
        self._children_name_map["diffservclfrelementtable"] = "diffServClfrElementTable"

        self.diffservmultifieldclfrtable = DIFFSERVMIB.DiffServMultiFieldClfrTable()
        self.diffservmultifieldclfrtable.parent = self
        self._children_name_map["diffservmultifieldclfrtable"] = "diffServMultiFieldClfrTable"

        self.diffservmetertable = DIFFSERVMIB.DiffServMeterTable()
        self.diffservmetertable.parent = self
        self._children_name_map["diffservmetertable"] = "diffServMeterTable"

        self.diffservtbparamtable = DIFFSERVMIB.DiffServTBParamTable()
        self.diffservtbparamtable.parent = self
        self._children_name_map["diffservtbparamtable"] = "diffServTBParamTable"

        self.diffservactiontable = DIFFSERVMIB.DiffServActionTable()
        self.diffservactiontable.parent = self
        self._children_name_map["diffservactiontable"] = "diffServActionTable"

        self.diffservdscpmarkacttable = DIFFSERVMIB.DiffServDscpMarkActTable()
        self.diffservdscpmarkacttable.parent = self
        self._children_name_map["diffservdscpmarkacttable"] = "diffServDscpMarkActTable"

        self.diffservcountacttable = DIFFSERVMIB.DiffServCountActTable()
        self.diffservcountacttable.parent = self
        self._children_name_map["diffservcountacttable"] = "diffServCountActTable"

        self.diffservalgdroptable = DIFFSERVMIB.DiffServAlgDropTable()
        self.diffservalgdroptable.parent = self
        self._children_name_map["diffservalgdroptable"] = "diffServAlgDropTable"

        self.diffservrandomdroptable = DIFFSERVMIB.DiffServRandomDropTable()
        self.diffservrandomdroptable.parent = self
        self._children_name_map["diffservrandomdroptable"] = "diffServRandomDropTable"

        self.diffservqtable = DIFFSERVMIB.DiffServQTable()
        self.diffservqtable.parent = self
        self._children_name_map["diffservqtable"] = "diffServQTable"

        self.diffservschedulertable = DIFFSERVMIB.DiffServSchedulerTable()
        self.diffservschedulertable.parent = self
        self._children_name_map["diffservschedulertable"] = "diffServSchedulerTable"

        self.diffservminratetable = DIFFSERVMIB.DiffServMinRateTable()
        self.diffservminratetable.parent = self
        self._children_name_map["diffservminratetable"] = "diffServMinRateTable"

        self.diffservmaxratetable = DIFFSERVMIB.DiffServMaxRateTable()
        self.diffservmaxratetable.parent = self
        self._children_name_map["diffservmaxratetable"] = "diffServMaxRateTable"
        self._segment_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DIFFSERVMIB, [], name, value)


    class DiffServClassifier(Entity):
        """
        
        
        .. attribute:: diffservclfrnextfree
        
        	This object contains an unused value for diffServClfrId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservclfrelementnextfree
        
        	This object contains an unused value for diffServClfrElementId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservmultifieldclfrnextfree
        
        	This object contains an unused value for diffServMultiFieldClfrId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServClassifier, self).__init__()

            self.yang_name = "diffServClassifier"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservclfrnextfree', (YLeaf(YType.uint32, 'diffServClfrNextFree'), ['int'])),
                ('diffservclfrelementnextfree', (YLeaf(YType.uint32, 'diffServClfrElementNextFree'), ['int'])),
                ('diffservmultifieldclfrnextfree', (YLeaf(YType.uint32, 'diffServMultiFieldClfrNextFree'), ['int'])),
            ])
            self.diffservclfrnextfree = None
            self.diffservclfrelementnextfree = None
            self.diffservmultifieldclfrnextfree = None
            self._segment_path = lambda: "diffServClassifier"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServClassifier, [u'diffservclfrnextfree', u'diffservclfrelementnextfree', u'diffservmultifieldclfrnextfree'], name, value)


    class DiffServMeter(Entity):
        """
        
        
        .. attribute:: diffservmeternextfree
        
        	This object contains an unused value for diffServMeterId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServMeter, self).__init__()

            self.yang_name = "diffServMeter"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservmeternextfree', (YLeaf(YType.uint32, 'diffServMeterNextFree'), ['int'])),
            ])
            self.diffservmeternextfree = None
            self._segment_path = lambda: "diffServMeter"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServMeter, [u'diffservmeternextfree'], name, value)


    class DiffServTBParam(Entity):
        """
        
        
        .. attribute:: diffservtbparamnextfree
        
        	This object contains an unused value for diffServTBParamId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServTBParam, self).__init__()

            self.yang_name = "diffServTBParam"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservtbparamnextfree', (YLeaf(YType.uint32, 'diffServTBParamNextFree'), ['int'])),
            ])
            self.diffservtbparamnextfree = None
            self._segment_path = lambda: "diffServTBParam"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServTBParam, [u'diffservtbparamnextfree'], name, value)


    class DiffServAction(Entity):
        """
        
        
        .. attribute:: diffservactionnextfree
        
        	This object contains an unused value for diffServActionId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservcountactnextfree
        
        	This object contains an unused value for diffServCountActId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServAction, self).__init__()

            self.yang_name = "diffServAction"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservactionnextfree', (YLeaf(YType.uint32, 'diffServActionNextFree'), ['int'])),
                ('diffservcountactnextfree', (YLeaf(YType.uint32, 'diffServCountActNextFree'), ['int'])),
            ])
            self.diffservactionnextfree = None
            self.diffservcountactnextfree = None
            self._segment_path = lambda: "diffServAction"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServAction, [u'diffservactionnextfree', u'diffservcountactnextfree'], name, value)


    class DiffServAlgDrop(Entity):
        """
        
        
        .. attribute:: diffservalgdropnextfree
        
        	This object contains an unused value for diffServAlgDropId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservrandomdropnextfree
        
        	This object contains an unused value for diffServRandomDropId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServAlgDrop, self).__init__()

            self.yang_name = "diffServAlgDrop"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservalgdropnextfree', (YLeaf(YType.uint32, 'diffServAlgDropNextFree'), ['int'])),
                ('diffservrandomdropnextfree', (YLeaf(YType.uint32, 'diffServRandomDropNextFree'), ['int'])),
            ])
            self.diffservalgdropnextfree = None
            self.diffservrandomdropnextfree = None
            self._segment_path = lambda: "diffServAlgDrop"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServAlgDrop, [u'diffservalgdropnextfree', u'diffservrandomdropnextfree'], name, value)


    class DiffServQueue(Entity):
        """
        
        
        .. attribute:: diffservqnextfree
        
        	This object contains an unused value for diffServQId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServQueue, self).__init__()

            self.yang_name = "diffServQueue"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservqnextfree', (YLeaf(YType.uint32, 'diffServQNextFree'), ['int'])),
            ])
            self.diffservqnextfree = None
            self._segment_path = lambda: "diffServQueue"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServQueue, [u'diffservqnextfree'], name, value)


    class DiffServScheduler(Entity):
        """
        
        
        .. attribute:: diffservschedulernextfree
        
        	This object contains an unused value for diffServSchedulerId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservminratenextfree
        
        	This object contains an unused value for diffServMinRateId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservmaxratenextfree
        
        	This object contains an unused value for diffServMaxRateId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServScheduler, self).__init__()

            self.yang_name = "diffServScheduler"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('diffservschedulernextfree', (YLeaf(YType.uint32, 'diffServSchedulerNextFree'), ['int'])),
                ('diffservminratenextfree', (YLeaf(YType.uint32, 'diffServMinRateNextFree'), ['int'])),
                ('diffservmaxratenextfree', (YLeaf(YType.uint32, 'diffServMaxRateNextFree'), ['int'])),
            ])
            self.diffservschedulernextfree = None
            self.diffservminratenextfree = None
            self.diffservmaxratenextfree = None
            self._segment_path = lambda: "diffServScheduler"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServScheduler, [u'diffservschedulernextfree', u'diffservminratenextfree', u'diffservmaxratenextfree'], name, value)


    class DiffServDataPathTable(Entity):
        """
        The data path table contains RowPointers indicating the start of
        the functional data path for each interface and traffic direction
        in this device. These may merge, or be separated into parallel
        data paths.
        
        .. attribute:: diffservdatapathentry
        
        	An entry in the data path table indicates the start of a single Differentiated Services Functional Data Path in this device.  These are associated with individual interfaces, logical or physical, and therefore are instantiated by ifIndex. Therefore, the interface index must have been assigned, according to the procedures applicable to that, before it can be meaningfully used. Generally, this means that the interface must exist.  When diffServDataPathStorage is of type nonVolatile, however, this may reflect the configuration for an interface whose ifIndex has been assigned but for which the supporting implementation is not currently present
        	**type**\: list of  		 :py:class:`DiffServDataPathEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServDataPathTable, self).__init__()

            self.yang_name = "diffServDataPathTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServDataPathEntry", ("diffservdatapathentry", DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry))])
            self._leafs = OrderedDict()

            self.diffservdatapathentry = YList(self)
            self._segment_path = lambda: "diffServDataPathTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServDataPathTable, [], name, value)


        class DiffServDataPathEntry(Entity):
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
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: diffservdatapathifdirection  (key)
            
            	IfDirection specifies whether the reception or transmission path for this interface is in view
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DIFFSERV_MIB.IfDirection>`
            
            .. attribute:: diffservdatapathstart
            
            	This selects the first Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no Differentiated Services treatment is performed on traffic of this data path. A pointer with the value zeroDotZero normally terminates a functional data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservdatapathstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservdatapathstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry, self).__init__()

                self.yang_name = "diffServDataPathEntry"
                self.yang_parent_name = "diffServDataPathTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','diffservdatapathifdirection']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('diffservdatapathifdirection', (YLeaf(YType.enumeration, 'diffServDataPathIfDirection'), [('ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'IfDirection', '')])),
                    ('diffservdatapathstart', (YLeaf(YType.str, 'diffServDataPathStart'), ['str'])),
                    ('diffservdatapathstorage', (YLeaf(YType.enumeration, 'diffServDataPathStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservdatapathstatus', (YLeaf(YType.enumeration, 'diffServDataPathStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.diffservdatapathifdirection = None
                self.diffservdatapathstart = None
                self.diffservdatapathstorage = None
                self.diffservdatapathstatus = None
                self._segment_path = lambda: "diffServDataPathEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[diffServDataPathIfDirection='" + str(self.diffservdatapathifdirection) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServDataPathTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry, [u'ifindex', u'diffservdatapathifdirection', u'diffservdatapathstart', u'diffservdatapathstorage', u'diffservdatapathstatus'], name, value)


    class DiffServClfrTable(Entity):
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
        	**type**\: list of  		 :py:class:`DiffServClfrEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServClfrTable, self).__init__()

            self.yang_name = "diffServClfrTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServClfrEntry", ("diffservclfrentry", DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry))])
            self._leafs = OrderedDict()

            self.diffservclfrentry = YList(self)
            self._segment_path = lambda: "diffServClfrTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServClfrTable, [], name, value)


        class DiffServClfrEntry(Entity):
            """
            An entry in the classifier table describes a single classifier.
            All classifier elements belonging to the same classifier use the
            classifier's diffServClfrId as part of their index.
            
            .. attribute:: diffservclfrid  (key)
            
            	An index that enumerates the classifier entries.  Managers should obtain new values for row creation in this table by reading diffServClfrNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry, self).__init__()

                self.yang_name = "diffServClfrEntry"
                self.yang_parent_name = "diffServClfrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservclfrid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservclfrid', (YLeaf(YType.uint32, 'diffServClfrId'), ['int'])),
                    ('diffservclfrstorage', (YLeaf(YType.enumeration, 'diffServClfrStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservclfrstatus', (YLeaf(YType.enumeration, 'diffServClfrStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservclfrid = None
                self.diffservclfrstorage = None
                self.diffservclfrstatus = None
                self._segment_path = lambda: "diffServClfrEntry" + "[diffServClfrId='" + str(self.diffservclfrid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServClfrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry, [u'diffservclfrid', u'diffservclfrstorage', u'diffservclfrstatus'], name, value)


    class DiffServClfrElementTable(Entity):
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
        	**type**\: list of  		 :py:class:`DiffServClfrElementEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServClfrElementTable, self).__init__()

            self.yang_name = "diffServClfrElementTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServClfrElementEntry", ("diffservclfrelemententry", DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry))])
            self._leafs = OrderedDict()

            self.diffservclfrelemententry = YList(self)
            self._segment_path = lambda: "diffServClfrElementTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServClfrElementTable, [], name, value)


        class DiffServClfrElementEntry(Entity):
            """
            An entry in the classifier element table describes a single
            element of the classifier.
            
            .. attribute:: diffservclfrid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`diffservclfrid <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry>`
            
            .. attribute:: diffservclfrelementid  (key)
            
            	An index that enumerates the Classifier Element entries. Managers obtain new values for row creation in this table by reading diffServClfrElementNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementprecedence
            
            	The relative order in which classifier elements are applied\: higher numbers represent classifier element with higher precedence.  Classifier elements with the same order must be unambiguous i.e. they must define non\-overlapping patterns, and are considered to be applied simultaneously to the traffic stream. Classifier elements with different order may overlap in their filters\:  the classifier element with the highest order that matches is taken.  On a given interface, there must be a complete classifier in place at all times in the ingress direction.  This means one or more filters must match any possible pattern. There is no such    requirement in the egress direction
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementnext
            
            	This attribute provides one branch of the fan\-out functionality of a classifier described in the Informal Differentiated Services Model section 4.1.  This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementspecific
            
            	A pointer to a valid entry in another table, filter table, that describes the applicable classification parameters, e.g. an entry in diffServMultiFieldClfrTable.  The value zeroDotZero is interpreted to match anything not matched by another classifier element \- only one such entry may exist for each classifier.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or    becomes inactive by other means, the element is ignored
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservclfrelementstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry, self).__init__()

                self.yang_name = "diffServClfrElementEntry"
                self.yang_parent_name = "diffServClfrElementTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservclfrid','diffservclfrelementid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservclfrid', (YLeaf(YType.str, 'diffServClfrId'), ['int'])),
                    ('diffservclfrelementid', (YLeaf(YType.uint32, 'diffServClfrElementId'), ['int'])),
                    ('diffservclfrelementprecedence', (YLeaf(YType.uint32, 'diffServClfrElementPrecedence'), ['int'])),
                    ('diffservclfrelementnext', (YLeaf(YType.str, 'diffServClfrElementNext'), ['str'])),
                    ('diffservclfrelementspecific', (YLeaf(YType.str, 'diffServClfrElementSpecific'), ['str'])),
                    ('diffservclfrelementstorage', (YLeaf(YType.enumeration, 'diffServClfrElementStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservclfrelementstatus', (YLeaf(YType.enumeration, 'diffServClfrElementStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservclfrid = None
                self.diffservclfrelementid = None
                self.diffservclfrelementprecedence = None
                self.diffservclfrelementnext = None
                self.diffservclfrelementspecific = None
                self.diffservclfrelementstorage = None
                self.diffservclfrelementstatus = None
                self._segment_path = lambda: "diffServClfrElementEntry" + "[diffServClfrId='" + str(self.diffservclfrid) + "']" + "[diffServClfrElementId='" + str(self.diffservclfrelementid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServClfrElementTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry, [u'diffservclfrid', u'diffservclfrelementid', u'diffservclfrelementprecedence', u'diffservclfrelementnext', u'diffservclfrelementspecific', u'diffservclfrelementstorage', u'diffservclfrelementstatus'], name, value)


    class DiffServMultiFieldClfrTable(Entity):
        """
        A table of IP Multi\-field Classifier filter entries that a
        
        
        
        system may use to identify IP traffic.
        
        .. attribute:: diffservmultifieldclfrentry
        
        	An IP Multi\-field Classifier entry describes a single filter
        	**type**\: list of  		 :py:class:`DiffServMultiFieldClfrEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServMultiFieldClfrTable, self).__init__()

            self.yang_name = "diffServMultiFieldClfrTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServMultiFieldClfrEntry", ("diffservmultifieldclfrentry", DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry))])
            self._leafs = OrderedDict()

            self.diffservmultifieldclfrentry = YList(self)
            self._segment_path = lambda: "diffServMultiFieldClfrTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServMultiFieldClfrTable, [], name, value)


        class DiffServMultiFieldClfrEntry(Entity):
            """
            An IP Multi\-field Classifier entry describes a single filter.
            
            .. attribute:: diffservmultifieldclfrid  (key)
            
            	An index that enumerates the MultiField Classifier filter entries.  Managers obtain new values for row creation in this table by reading diffServMultiFieldClfrNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmultifieldclfraddrtype
            
            	The type of IP address used by this classifier entry.  While other types of addresses are defined in the InetAddressType    textual convention, and DNS names, a classifier can only look at packets on the wire. Therefore, this object is limited to IPv4 and IPv6 addresses
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: diffservmultifieldclfrdstaddr
            
            	The IP address to match against the packet's destination IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.  diffServMultiFieldClfrDstPrefixLength indicates the number of bits that are relevant
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: diffservmultifieldclfrdstprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrDstAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\: int
            
            	**range:** 0..2040
            
            	**units**\: bits
            
            .. attribute:: diffservmultifieldclfrsrcaddr
            
            	The IP address to match against the packet's source IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix. diffServMultiFieldClfrSrcPrefixLength indicates the number of bits that are relevant
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: diffservmultifieldclfrsrcprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrSrcAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\: int
            
            	**range:** 0..2040
            
            	**units**\: bits
            
            .. attribute:: diffservmultifieldclfrdscp
            
            	The value that the DSCP in the packet must have to match this entry. A value of \-1 indicates that a specific DSCP value has not been defined and thus all DSCP values are considered a match
            	**type**\: int
            
            	**range:** \-1..63
            
            .. attribute:: diffservmultifieldclfrflowid
            
            	The flow identifier in an IPv6 header
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: diffservmultifieldclfrprotocol
            
            	The IP protocol to match against the IPv4 protocol number or the IPv6 Next\- Header number in the packet. A value of 255 means match all.  Note the protocol number of 255 is reserved by IANA, and Next\-Header number of 0 is used in IPv6
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: diffservmultifieldclfrdstl4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrdstl4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrDstL4PortMin
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcl4portmin
            
            	The minimum value that the layer\-4 source port number in the packet must have in order to match this classifier entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcl4portmax
            
            	The maximum value that the layer\-4 source port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrSrcL4PortMin
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservmultifieldclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry, self).__init__()

                self.yang_name = "diffServMultiFieldClfrEntry"
                self.yang_parent_name = "diffServMultiFieldClfrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservmultifieldclfrid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservmultifieldclfrid', (YLeaf(YType.uint32, 'diffServMultiFieldClfrId'), ['int'])),
                    ('diffservmultifieldclfraddrtype', (YLeaf(YType.enumeration, 'diffServMultiFieldClfrAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('diffservmultifieldclfrdstaddr', (YLeaf(YType.str, 'diffServMultiFieldClfrDstAddr'), ['str'])),
                    ('diffservmultifieldclfrdstprefixlength', (YLeaf(YType.uint32, 'diffServMultiFieldClfrDstPrefixLength'), ['int'])),
                    ('diffservmultifieldclfrsrcaddr', (YLeaf(YType.str, 'diffServMultiFieldClfrSrcAddr'), ['str'])),
                    ('diffservmultifieldclfrsrcprefixlength', (YLeaf(YType.uint32, 'diffServMultiFieldClfrSrcPrefixLength'), ['int'])),
                    ('diffservmultifieldclfrdscp', (YLeaf(YType.int32, 'diffServMultiFieldClfrDscp'), ['int'])),
                    ('diffservmultifieldclfrflowid', (YLeaf(YType.uint32, 'diffServMultiFieldClfrFlowId'), ['int'])),
                    ('diffservmultifieldclfrprotocol', (YLeaf(YType.uint32, 'diffServMultiFieldClfrProtocol'), ['int'])),
                    ('diffservmultifieldclfrdstl4portmin', (YLeaf(YType.uint16, 'diffServMultiFieldClfrDstL4PortMin'), ['int'])),
                    ('diffservmultifieldclfrdstl4portmax', (YLeaf(YType.uint16, 'diffServMultiFieldClfrDstL4PortMax'), ['int'])),
                    ('diffservmultifieldclfrsrcl4portmin', (YLeaf(YType.uint16, 'diffServMultiFieldClfrSrcL4PortMin'), ['int'])),
                    ('diffservmultifieldclfrsrcl4portmax', (YLeaf(YType.uint16, 'diffServMultiFieldClfrSrcL4PortMax'), ['int'])),
                    ('diffservmultifieldclfrstorage', (YLeaf(YType.enumeration, 'diffServMultiFieldClfrStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservmultifieldclfrstatus', (YLeaf(YType.enumeration, 'diffServMultiFieldClfrStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservmultifieldclfrid = None
                self.diffservmultifieldclfraddrtype = None
                self.diffservmultifieldclfrdstaddr = None
                self.diffservmultifieldclfrdstprefixlength = None
                self.diffservmultifieldclfrsrcaddr = None
                self.diffservmultifieldclfrsrcprefixlength = None
                self.diffservmultifieldclfrdscp = None
                self.diffservmultifieldclfrflowid = None
                self.diffservmultifieldclfrprotocol = None
                self.diffservmultifieldclfrdstl4portmin = None
                self.diffservmultifieldclfrdstl4portmax = None
                self.diffservmultifieldclfrsrcl4portmin = None
                self.diffservmultifieldclfrsrcl4portmax = None
                self.diffservmultifieldclfrstorage = None
                self.diffservmultifieldclfrstatus = None
                self._segment_path = lambda: "diffServMultiFieldClfrEntry" + "[diffServMultiFieldClfrId='" + str(self.diffservmultifieldclfrid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServMultiFieldClfrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry, [u'diffservmultifieldclfrid', u'diffservmultifieldclfraddrtype', u'diffservmultifieldclfrdstaddr', u'diffservmultifieldclfrdstprefixlength', u'diffservmultifieldclfrsrcaddr', u'diffservmultifieldclfrsrcprefixlength', u'diffservmultifieldclfrdscp', u'diffservmultifieldclfrflowid', u'diffservmultifieldclfrprotocol', u'diffservmultifieldclfrdstl4portmin', u'diffservmultifieldclfrdstl4portmax', u'diffservmultifieldclfrsrcl4portmin', u'diffservmultifieldclfrsrcl4portmax', u'diffservmultifieldclfrstorage', u'diffservmultifieldclfrstatus'], name, value)


    class DiffServMeterTable(Entity):
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
        	**type**\: list of  		 :py:class:`DiffServMeterEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServMeterTable, self).__init__()

            self.yang_name = "diffServMeterTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServMeterEntry", ("diffservmeterentry", DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry))])
            self._leafs = OrderedDict()

            self.diffservmeterentry = YList(self)
            self._segment_path = lambda: "diffServMeterTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServMeterTable, [], name, value)


        class DiffServMeterEntry(Entity):
            """
            An entry in the meter table describes a single conformance level
            of a meter.
            
            .. attribute:: diffservmeterid  (key)
            
            	An index that enumerates the Meter entries.  Managers obtain new values for row creation in this table by reading diffServMeterNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmetersucceednext
            
            	If the traffic does conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterfailnext
            
            	If the traffic does not conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry      diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterspecific
            
            	This indicates the behavior of the meter by pointing to an entry containing detailed parameters. Note that entries in that specific table must be managed explicitly.  For example, diffServMeterSpecific may point to an entry in diffServTBParamTable, which contains an instance of a single set of Token Bucket parameters.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the meter always succeeds
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservmeterstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry, self).__init__()

                self.yang_name = "diffServMeterEntry"
                self.yang_parent_name = "diffServMeterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservmeterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservmeterid', (YLeaf(YType.uint32, 'diffServMeterId'), ['int'])),
                    ('diffservmetersucceednext', (YLeaf(YType.str, 'diffServMeterSucceedNext'), ['str'])),
                    ('diffservmeterfailnext', (YLeaf(YType.str, 'diffServMeterFailNext'), ['str'])),
                    ('diffservmeterspecific', (YLeaf(YType.str, 'diffServMeterSpecific'), ['str'])),
                    ('diffservmeterstorage', (YLeaf(YType.enumeration, 'diffServMeterStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservmeterstatus', (YLeaf(YType.enumeration, 'diffServMeterStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservmeterid = None
                self.diffservmetersucceednext = None
                self.diffservmeterfailnext = None
                self.diffservmeterspecific = None
                self.diffservmeterstorage = None
                self.diffservmeterstatus = None
                self._segment_path = lambda: "diffServMeterEntry" + "[diffServMeterId='" + str(self.diffservmeterid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServMeterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry, [u'diffservmeterid', u'diffservmetersucceednext', u'diffservmeterfailnext', u'diffservmeterspecific', u'diffservmeterstorage', u'diffservmeterstatus'], name, value)


    class DiffServTBParamTable(Entity):
        """
        This table enumerates a single set of token bucket meter
        parameters that a system may use to police a stream of traffic.
        Such meters are modeled here as having a single rate and a single
        burst size. Multiple entries are used when multiple rates/burst
        sizes are needed.
        
        .. attribute:: diffservtbparamentry
        
        	An entry that describes a single set of token bucket parameters
        	**type**\: list of  		 :py:class:`DiffServTBParamEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServTBParamTable, self).__init__()

            self.yang_name = "diffServTBParamTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServTBParamEntry", ("diffservtbparamentry", DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry))])
            self._leafs = OrderedDict()

            self.diffservtbparamentry = YList(self)
            self._segment_path = lambda: "diffServTBParamTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServTBParamTable, [], name, value)


        class DiffServTBParamEntry(Entity):
            """
            An entry that describes a single set of token bucket
            parameters.
            
            .. attribute:: diffservtbparamid  (key)
            
            	An index that enumerates the Token Bucket Parameter entries. Managers obtain new values for row creation in this table by reading diffServTBParamNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservtbparamtype
            
            	The Metering algorithm associated with the Token Bucket parameters.  zeroDotZero indicates this is unknown.  Standard values for generic algorithms\: diffServTBParamSimpleTokenBucket, diffServTBParamAvgRate, diffServTBParamSrTCMBlind, diffServTBParamSrTCMAware, diffServTBParamTrTCMBlind, diffServTBParamTrTCMAware, and diffServTBParamTswTCM are specified in this MIB as OBJECT\- IDENTITYs; additional values may be further specified in other MIBs
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservtbparamrate
            
            	The token\-bucket rate, in kilobits per second (kbps). This attribute is used for\: 1. CIR in RFC 2697 for srTCM 2. CIR and PIR in RFC 2698 for trTCM 3. CTR and PTR in RFC 2859 for TSWTCM 4. AverageRate in RFC 3290
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservtbparamburstsize
            
            	The maximum number of bytes in a single transmission burst. This attribute is used for\: 1. CBS and EBS in RFC 2697 for srTCM 2. CBS and PBS in RFC 2698 for trTCM 3. Burst Size in RFC 3290
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: diffservtbparaminterval
            
            	The time interval used with the token bucket.  For\: 1. Average Rate Meter, the Informal Differentiated Services Model    section 5.2.1, \- Delta. 2. Simple Token Bucket Meter, the Informal Differentiated    Services Model section 5.1, \- time interval t. 3. RFC 2859 TSWTCM, \- AVG\_INTERVAL. 4. RFC 2697 srTCM, RFC 2698 trTCM, \- token bucket update time    interval
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: diffservtbparamstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservtbparamstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry, self).__init__()

                self.yang_name = "diffServTBParamEntry"
                self.yang_parent_name = "diffServTBParamTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservtbparamid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservtbparamid', (YLeaf(YType.uint32, 'diffServTBParamId'), ['int'])),
                    ('diffservtbparamtype', (YLeaf(YType.str, 'diffServTBParamType'), ['str'])),
                    ('diffservtbparamrate', (YLeaf(YType.uint32, 'diffServTBParamRate'), ['int'])),
                    ('diffservtbparamburstsize', (YLeaf(YType.int32, 'diffServTBParamBurstSize'), ['int'])),
                    ('diffservtbparaminterval', (YLeaf(YType.uint32, 'diffServTBParamInterval'), ['int'])),
                    ('diffservtbparamstorage', (YLeaf(YType.enumeration, 'diffServTBParamStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservtbparamstatus', (YLeaf(YType.enumeration, 'diffServTBParamStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservtbparamid = None
                self.diffservtbparamtype = None
                self.diffservtbparamrate = None
                self.diffservtbparamburstsize = None
                self.diffservtbparaminterval = None
                self.diffservtbparamstorage = None
                self.diffservtbparamstatus = None
                self._segment_path = lambda: "diffServTBParamEntry" + "[diffServTBParamId='" + str(self.diffservtbparamid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServTBParamTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry, [u'diffservtbparamid', u'diffservtbparamtype', u'diffservtbparamrate', u'diffservtbparamburstsize', u'diffservtbparaminterval', u'diffservtbparamstorage', u'diffservtbparamstatus'], name, value)


    class DiffServActionTable(Entity):
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
        	**type**\: list of  		 :py:class:`DiffServActionEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServActionTable.DiffServActionEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServActionTable, self).__init__()

            self.yang_name = "diffServActionTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServActionEntry", ("diffservactionentry", DIFFSERVMIB.DiffServActionTable.DiffServActionEntry))])
            self._leafs = OrderedDict()

            self.diffservactionentry = YList(self)
            self._segment_path = lambda: "diffServActionTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServActionTable, [], name, value)


        class DiffServActionEntry(Entity):
            """
            Each entry in the action table allows description of one
            specific action to be applied to traffic.
            
            .. attribute:: diffservactionid  (key)
            
            	An index that enumerates the Action entries.  Managers obtain new values for row creation in this table by reading diffServActionNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservactioninterface
            
            	The interface index (value of ifIndex) that this action occurs on. This may be derived from the diffServDataPathStartEntry's index by extension through the various RowPointers. However, as this may be difficult for a network management station, it is placed here as well.  If this is indeterminate, the value is zero.  This is of especial relevance when reporting the counters which may apply to traffic crossing an interface\:    diffServCountActOctets,    diffServCountActPkts,    diffServAlgDropOctets,    diffServAlgDropPkts,    diffServAlgRandomDropOctets, and    diffServAlgRandomDropPkts.  It is also especially relevant to the queue and scheduler which may be subsequently applied
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: diffservactionnext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservactionspecific
            
            	A pointer to an object instance providing additional information for the type of action indicated by this action table entry.  For the standard actions defined by this MIB module, this should point to either a diffServDscpMarkActEntry or a diffServCountActEntry. For other actions, it may point to an object instance defined in some other MIB.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the Meter should be treated as if it were not present.  This may lead to incorrect policy behavior
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservactionstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservactionstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServActionTable.DiffServActionEntry, self).__init__()

                self.yang_name = "diffServActionEntry"
                self.yang_parent_name = "diffServActionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservactionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservactionid', (YLeaf(YType.uint32, 'diffServActionId'), ['int'])),
                    ('diffservactioninterface', (YLeaf(YType.int32, 'diffServActionInterface'), ['int'])),
                    ('diffservactionnext', (YLeaf(YType.str, 'diffServActionNext'), ['str'])),
                    ('diffservactionspecific', (YLeaf(YType.str, 'diffServActionSpecific'), ['str'])),
                    ('diffservactionstorage', (YLeaf(YType.enumeration, 'diffServActionStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservactionstatus', (YLeaf(YType.enumeration, 'diffServActionStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservactionid = None
                self.diffservactioninterface = None
                self.diffservactionnext = None
                self.diffservactionspecific = None
                self.diffservactionstorage = None
                self.diffservactionstatus = None
                self._segment_path = lambda: "diffServActionEntry" + "[diffServActionId='" + str(self.diffservactionid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServActionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServActionTable.DiffServActionEntry, [u'diffservactionid', u'diffservactioninterface', u'diffservactionnext', u'diffservactionspecific', u'diffservactionstorage', u'diffservactionstatus'], name, value)


    class DiffServDscpMarkActTable(Entity):
        """
        This table enumerates specific DSCPs used for marking or
        remarking the DSCP field of IP packets. The entries of this table
        may be referenced by a diffServActionSpecific attribute.
        
        .. attribute:: diffservdscpmarkactentry
        
        	An entry in the DSCP mark action table that describes a single DSCP used for marking
        	**type**\: list of  		 :py:class:`DiffServDscpMarkActEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServDscpMarkActTable, self).__init__()

            self.yang_name = "diffServDscpMarkActTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServDscpMarkActEntry", ("diffservdscpmarkactentry", DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry))])
            self._leafs = OrderedDict()

            self.diffservdscpmarkactentry = YList(self)
            self._segment_path = lambda: "diffServDscpMarkActTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServDscpMarkActTable, [], name, value)


        class DiffServDscpMarkActEntry(Entity):
            """
            An entry in the DSCP mark action table that describes a single
            DSCP used for marking.
            
            .. attribute:: diffservdscpmarkactdscp  (key)
            
            	The DSCP that this Action will store into the DSCP field of the subject. It is quite possible that the only packets subject to this Action are already marked with this DSCP. Note also that Differentiated Services processing may result in packet being marked on both ingress to a network and on egress from it, and that ingress and egress can occur in the same router
            	**type**\: int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry, self).__init__()

                self.yang_name = "diffServDscpMarkActEntry"
                self.yang_parent_name = "diffServDscpMarkActTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservdscpmarkactdscp']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservdscpmarkactdscp', (YLeaf(YType.uint8, 'diffServDscpMarkActDscp'), ['int'])),
                ])
                self.diffservdscpmarkactdscp = None
                self._segment_path = lambda: "diffServDscpMarkActEntry" + "[diffServDscpMarkActDscp='" + str(self.diffservdscpmarkactdscp) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServDscpMarkActTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry, [u'diffservdscpmarkactdscp'], name, value)


    class DiffServCountActTable(Entity):
        """
        This table contains counters for all the traffic passing through
        an action element.
        
        .. attribute:: diffservcountactentry
        
        	An entry in the count action table describes a single set of traffic counters
        	**type**\: list of  		 :py:class:`DiffServCountActEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServCountActTable, self).__init__()

            self.yang_name = "diffServCountActTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServCountActEntry", ("diffservcountactentry", DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry))])
            self._leafs = OrderedDict()

            self.diffservcountactentry = YList(self)
            self._segment_path = lambda: "diffServCountActTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServCountActTable, [], name, value)


        class DiffServCountActEntry(Entity):
            """
            An entry in the count action table describes a single set of
            traffic counters.
            
            .. attribute:: diffservcountactid  (key)
            
            	An index that enumerates the Count Action entries.  Managers obtain new values for row creation in this table by reading    diffServCountActNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservcountactoctets
            
            	The number of octets at the Action data path element.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservcountactpkts
            
            	The number of packets at the Action data path element.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservcountactstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservcountactstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing    to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry, self).__init__()

                self.yang_name = "diffServCountActEntry"
                self.yang_parent_name = "diffServCountActTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservcountactid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservcountactid', (YLeaf(YType.uint32, 'diffServCountActId'), ['int'])),
                    ('diffservcountactoctets', (YLeaf(YType.uint64, 'diffServCountActOctets'), ['int'])),
                    ('diffservcountactpkts', (YLeaf(YType.uint64, 'diffServCountActPkts'), ['int'])),
                    ('diffservcountactstorage', (YLeaf(YType.enumeration, 'diffServCountActStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservcountactstatus', (YLeaf(YType.enumeration, 'diffServCountActStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservcountactid = None
                self.diffservcountactoctets = None
                self.diffservcountactpkts = None
                self.diffservcountactstorage = None
                self.diffservcountactstatus = None
                self._segment_path = lambda: "diffServCountActEntry" + "[diffServCountActId='" + str(self.diffservcountactid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServCountActTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry, [u'diffservcountactid', u'diffservcountactoctets', u'diffservcountactpkts', u'diffservcountactstorage', u'diffservcountactstatus'], name, value)


    class DiffServAlgDropTable(Entity):
        """
        The algorithmic drop table contains entries describing an
        element that drops packets according to some algorithm.
        
        .. attribute:: diffservalgdropentry
        
        	An entry describes a process that drops packets according to some algorithm. Further details of the algorithm type are to be found in diffServAlgDropType and with more detail parameter entry pointed to by diffServAlgDropSpecific when necessary
        	**type**\: list of  		 :py:class:`DiffServAlgDropEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServAlgDropTable, self).__init__()

            self.yang_name = "diffServAlgDropTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServAlgDropEntry", ("diffservalgdropentry", DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry))])
            self._leafs = OrderedDict()

            self.diffservalgdropentry = YList(self)
            self._segment_path = lambda: "diffServAlgDropTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServAlgDropTable, [], name, value)


        class DiffServAlgDropEntry(Entity):
            """
            An entry describes a process that drops packets according to
            some algorithm. Further details of the algorithm type are to be
            found in diffServAlgDropType and with more detail parameter entry
            pointed to by diffServAlgDropSpecific when necessary.
            
            .. attribute:: diffservalgdropid  (key)
            
            	An index that enumerates the Algorithmic Dropper entries. Managers obtain new values for row creation in this table by reading diffServAlgDropNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservalgdroptype
            
            	The type of algorithm used by this dropper. The value other(1) requires further specification in some other MIB module.  In the tailDrop(2) algorithm, diffServAlgDropQThreshold represents the maximum depth of the queue, pointed to by diffServAlgDropQMeasure, beyond which all newly arriving packets will be dropped.  In the headDrop(3) algorithm, if a packet arrives when the current depth of the queue, pointed to by diffServAlgDropQMeasure, is at diffServAlgDropQThreshold, packets currently at the head of the queue are dropped to make room for the new packet to be enqueued at the tail of the queue.  In the randomDrop(4) algorithm, on packet arrival, an Active Queue Management algorithm is executed which may randomly drop a packet. This algorithm may be proprietary, and it may drop either the arriving packet or another packet in the queue. diffServAlgDropSpecific points to a diffServRandomDropEntry that describes the algorithm. For this algorithm,    diffServAlgDropQThreshold is understood to be the absolute maximum size of the queue and additional parameters are described in diffServRandomDropTable.  The alwaysDrop(5) algorithm is as its name specifies; always drop. In this case, the other configuration values in this Entry are not meaningful; There is no useful 'next' processing step, there is no queue, and parameters describing the queue are not useful. Therefore, diffServAlgDropNext, diffServAlgDropMeasure, and diffServAlgDropSpecific are all zeroDotZero
            	**type**\:  :py:class:`DiffServAlgDropType <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry.DiffServAlgDropType>`
            
            .. attribute:: diffservalgdropnext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  When diffServAlgDropType is alwaysDrop(5), this object is ignored.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropqmeasure
            
            	Points to an entry in the diffServQTable to indicate the queue that a drop algorithm is to monitor when deciding whether to drop a packet. If the row pointed to does not exist, the algorithmic dropper element is considered inactive.    Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropqthreshold
            
            	A threshold on the depth in bytes of the queue being measured at which a trigger is generated to the dropping algorithm, unless diffServAlgDropType is alwaysDrop(5) where this object is ignored.  For the tailDrop(2) or headDrop(3) algorithms, this represents the depth of the queue, pointed to by diffServAlgDropQMeasure, at which the drop action will take place. Other algorithms will need to define their own semantics for this threshold
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: Bytes
            
            .. attribute:: diffservalgdropspecific
            
            	Points to a table entry that provides further detail regarding a drop algorithm.  Entries with diffServAlgDropType equal to other(1) may have this point to a table defined in another MIB module.  Entries with diffServAlgDropType equal to randomDrop(4) must have this point to an entry in diffServRandomDropTable.  For all other algorithms specified in this MIB, this should take the value zeroDotZero.  The diffServAlgDropType is authoritative for the type of the drop algorithm and the specific parameters for the drop algorithm needs to be evaluated based on the diffServAlgDropType.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropoctets
            
            	The number of octets that have been deterministically dropped by this drop process.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgdroppkts
            
            	The number of packets that have been deterministically dropped by this drop process.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgrandomdropoctets
            
            	The number of octets that have been randomly dropped by this drop process.  This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgrandomdroppkts
            
            	The number of packets that have been randomly dropped by this drop process. This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservalgdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry, self).__init__()

                self.yang_name = "diffServAlgDropEntry"
                self.yang_parent_name = "diffServAlgDropTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservalgdropid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservalgdropid', (YLeaf(YType.uint32, 'diffServAlgDropId'), ['int'])),
                    ('diffservalgdroptype', (YLeaf(YType.enumeration, 'diffServAlgDropType'), [('ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DIFFSERVMIB', 'DiffServAlgDropTable.DiffServAlgDropEntry.DiffServAlgDropType')])),
                    ('diffservalgdropnext', (YLeaf(YType.str, 'diffServAlgDropNext'), ['str'])),
                    ('diffservalgdropqmeasure', (YLeaf(YType.str, 'diffServAlgDropQMeasure'), ['str'])),
                    ('diffservalgdropqthreshold', (YLeaf(YType.uint32, 'diffServAlgDropQThreshold'), ['int'])),
                    ('diffservalgdropspecific', (YLeaf(YType.str, 'diffServAlgDropSpecific'), ['str'])),
                    ('diffservalgdropoctets', (YLeaf(YType.uint64, 'diffServAlgDropOctets'), ['int'])),
                    ('diffservalgdroppkts', (YLeaf(YType.uint64, 'diffServAlgDropPkts'), ['int'])),
                    ('diffservalgrandomdropoctets', (YLeaf(YType.uint64, 'diffServAlgRandomDropOctets'), ['int'])),
                    ('diffservalgrandomdroppkts', (YLeaf(YType.uint64, 'diffServAlgRandomDropPkts'), ['int'])),
                    ('diffservalgdropstorage', (YLeaf(YType.enumeration, 'diffServAlgDropStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservalgdropstatus', (YLeaf(YType.enumeration, 'diffServAlgDropStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservalgdropid = None
                self.diffservalgdroptype = None
                self.diffservalgdropnext = None
                self.diffservalgdropqmeasure = None
                self.diffservalgdropqthreshold = None
                self.diffservalgdropspecific = None
                self.diffservalgdropoctets = None
                self.diffservalgdroppkts = None
                self.diffservalgrandomdropoctets = None
                self.diffservalgrandomdroppkts = None
                self.diffservalgdropstorage = None
                self.diffservalgdropstatus = None
                self._segment_path = lambda: "diffServAlgDropEntry" + "[diffServAlgDropId='" + str(self.diffservalgdropid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServAlgDropTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry, [u'diffservalgdropid', u'diffservalgdroptype', u'diffservalgdropnext', u'diffservalgdropqmeasure', u'diffservalgdropqthreshold', u'diffservalgdropspecific', u'diffservalgdropoctets', u'diffservalgdroppkts', u'diffservalgrandomdropoctets', u'diffservalgrandomdroppkts', u'diffservalgdropstorage', u'diffservalgdropstatus'], name, value)

            class DiffServAlgDropType(Enum):
                """
                DiffServAlgDropType (Enum Class)

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



    class DiffServRandomDropTable(Entity):
        """
        The random drop table contains entries describing a process that
        drops packets randomly. Entries in this table are pointed to by
        diffServAlgDropSpecific.
        
        .. attribute:: diffservrandomdropentry
        
        	An entry describes a process that drops packets according to a random algorithm
        	**type**\: list of  		 :py:class:`DiffServRandomDropEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServRandomDropTable, self).__init__()

            self.yang_name = "diffServRandomDropTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServRandomDropEntry", ("diffservrandomdropentry", DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry))])
            self._leafs = OrderedDict()

            self.diffservrandomdropentry = YList(self)
            self._segment_path = lambda: "diffServRandomDropTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServRandomDropTable, [], name, value)


        class DiffServRandomDropEntry(Entity):
            """
            An entry describes a process that drops packets according to a
            random algorithm.
            
            .. attribute:: diffservrandomdropid  (key)
            
            	An index that enumerates the Random Drop entries.  Managers obtain new values for row creation in this table by reading diffServRandomDropNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropminthreshbytes
            
            	The average queue depth in bytes, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshPkts
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: diffservrandomdropminthreshpkts
            
            	The average queue depth in packets, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshBytes
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: packets
            
            .. attribute:: diffservrandomdropmaxthreshbytes
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshPkts
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: diffservrandomdropmaxthreshpkts
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshBytes
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: packets
            
            .. attribute:: diffservrandomdropprobmax
            
            	The worst case random drop probability, expressed in drops per thousand packets.  For example, if in the worst case every arriving packet may be dropped (100%) for a period, this has the value 1000. Alternatively, if in the worst case only one percent (1%) of traffic may be dropped, it has the value 10
            	**type**\: int
            
            	**range:** 0..1000
            
            .. attribute:: diffservrandomdropweight
            
            	The weighting of past history in affecting the Exponentially Weighted Moving Average function that calculates the current average queue depth.  The equation uses diffServRandomDropWeight/65536 as the coefficient for the new sample in the equation, and (65536 \- diffServRandomDropWeight)/65536 as the coefficient of the old value.  Implementations may limit the values of diffServRandomDropWeight to a subset of the possible range of values, such as powers of two. Doing this would facilitate implementation of the Exponentially Weighted Moving Average using shift instructions or registers
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: diffservrandomdropsamplingrate
            
            	The number of times per second the queue is sampled for queue average calculation.  A value of zero is used to mean that the queue is sampled approximately each time a packet is enqueued (or dequeued)
            	**type**\: int
            
            	**range:** 0..1000000
            
            .. attribute:: diffservrandomdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservrandomdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry, self).__init__()

                self.yang_name = "diffServRandomDropEntry"
                self.yang_parent_name = "diffServRandomDropTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservrandomdropid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservrandomdropid', (YLeaf(YType.uint32, 'diffServRandomDropId'), ['int'])),
                    ('diffservrandomdropminthreshbytes', (YLeaf(YType.uint32, 'diffServRandomDropMinThreshBytes'), ['int'])),
                    ('diffservrandomdropminthreshpkts', (YLeaf(YType.uint32, 'diffServRandomDropMinThreshPkts'), ['int'])),
                    ('diffservrandomdropmaxthreshbytes', (YLeaf(YType.uint32, 'diffServRandomDropMaxThreshBytes'), ['int'])),
                    ('diffservrandomdropmaxthreshpkts', (YLeaf(YType.uint32, 'diffServRandomDropMaxThreshPkts'), ['int'])),
                    ('diffservrandomdropprobmax', (YLeaf(YType.uint32, 'diffServRandomDropProbMax'), ['int'])),
                    ('diffservrandomdropweight', (YLeaf(YType.uint32, 'diffServRandomDropWeight'), ['int'])),
                    ('diffservrandomdropsamplingrate', (YLeaf(YType.uint32, 'diffServRandomDropSamplingRate'), ['int'])),
                    ('diffservrandomdropstorage', (YLeaf(YType.enumeration, 'diffServRandomDropStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservrandomdropstatus', (YLeaf(YType.enumeration, 'diffServRandomDropStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservrandomdropid = None
                self.diffservrandomdropminthreshbytes = None
                self.diffservrandomdropminthreshpkts = None
                self.diffservrandomdropmaxthreshbytes = None
                self.diffservrandomdropmaxthreshpkts = None
                self.diffservrandomdropprobmax = None
                self.diffservrandomdropweight = None
                self.diffservrandomdropsamplingrate = None
                self.diffservrandomdropstorage = None
                self.diffservrandomdropstatus = None
                self._segment_path = lambda: "diffServRandomDropEntry" + "[diffServRandomDropId='" + str(self.diffservrandomdropid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServRandomDropTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry, [u'diffservrandomdropid', u'diffservrandomdropminthreshbytes', u'diffservrandomdropminthreshpkts', u'diffservrandomdropmaxthreshbytes', u'diffservrandomdropmaxthreshpkts', u'diffservrandomdropprobmax', u'diffservrandomdropweight', u'diffservrandomdropsamplingrate', u'diffservrandomdropstorage', u'diffservrandomdropstatus'], name, value)


    class DiffServQTable(Entity):
        """
        The Queue Table enumerates the individual queues.  Note that the
        MIB models queuing systems as composed of individual queues, one
        per class of traffic, even though they may in fact be structured
        as classes of traffic scheduled using a common calendar queue, or
        in other ways.
        
        .. attribute:: diffservqentry
        
        	An entry in the Queue Table describes a single queue or class of traffic
        	**type**\: list of  		 :py:class:`DiffServQEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServQTable.DiffServQEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServQTable, self).__init__()

            self.yang_name = "diffServQTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServQEntry", ("diffservqentry", DIFFSERVMIB.DiffServQTable.DiffServQEntry))])
            self._leafs = OrderedDict()

            self.diffservqentry = YList(self)
            self._segment_path = lambda: "diffServQTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServQTable, [], name, value)


        class DiffServQEntry(Entity):
            """
            An entry in the Queue Table describes a single queue or class of
            traffic.
            
            .. attribute:: diffservqid  (key)
            
            	An index that enumerates the Queue entries.  Managers obtain new values for row creation in this table by reading diffServQNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservqnext
            
            	This selects the next Differentiated Services Scheduler.  The RowPointer must point to a diffServSchedulerEntry.  A value of zeroDotZero in this attribute indicates an incomplete diffServQEntry instance. In such a case, the entry has no operational effect, since it has no parameters to give it meaning.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqminrate
            
            	This RowPointer indicates the diffServMinRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the minimum rate and priority is unspecified.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqmaxrate
            
            	This RowPointer indicates the diffServMaxRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the maximum rate is the line speed of the interface.     Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservqstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServQTable.DiffServQEntry, self).__init__()

                self.yang_name = "diffServQEntry"
                self.yang_parent_name = "diffServQTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservqid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservqid', (YLeaf(YType.uint32, 'diffServQId'), ['int'])),
                    ('diffservqnext', (YLeaf(YType.str, 'diffServQNext'), ['str'])),
                    ('diffservqminrate', (YLeaf(YType.str, 'diffServQMinRate'), ['str'])),
                    ('diffservqmaxrate', (YLeaf(YType.str, 'diffServQMaxRate'), ['str'])),
                    ('diffservqstorage', (YLeaf(YType.enumeration, 'diffServQStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservqstatus', (YLeaf(YType.enumeration, 'diffServQStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservqid = None
                self.diffservqnext = None
                self.diffservqminrate = None
                self.diffservqmaxrate = None
                self.diffservqstorage = None
                self.diffservqstatus = None
                self._segment_path = lambda: "diffServQEntry" + "[diffServQId='" + str(self.diffservqid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServQTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServQTable.DiffServQEntry, [u'diffservqid', u'diffservqnext', u'diffservqminrate', u'diffservqmaxrate', u'diffservqstorage', u'diffservqstatus'], name, value)


    class DiffServSchedulerTable(Entity):
        """
        The Scheduler Table enumerates packet schedulers. Multiple
        scheduling algorithms can be used on a given data path, with each
        algorithm described by one diffServSchedulerEntry.
        
        .. attribute:: diffservschedulerentry
        
        	An entry in the Scheduler Table describing a single instance of a scheduling algorithm
        	**type**\: list of  		 :py:class:`DiffServSchedulerEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServSchedulerTable, self).__init__()

            self.yang_name = "diffServSchedulerTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServSchedulerEntry", ("diffservschedulerentry", DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry))])
            self._leafs = OrderedDict()

            self.diffservschedulerentry = YList(self)
            self._segment_path = lambda: "diffServSchedulerTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServSchedulerTable, [], name, value)


        class DiffServSchedulerEntry(Entity):
            """
            An entry in the Scheduler Table describing a single instance of
            a scheduling algorithm.
            
            .. attribute:: diffservschedulerid  (key)
            
            	An index that enumerates the Scheduler entries.  Managers obtain new values for row creation in this table by reading diffServSchedulerNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservschedulernext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This normally is null (zeroDotZero), or points to a diffServSchedulerEntry or a diffServQEntry.  However, this RowPointer may also point to an instance of\:   diffServClfrEntry,   diffServMeterEntry,   diffServActionEntry,   diffServAlgDropEntry.  It would point another diffServSchedulerEntry when implementing multiple scheduler methods for the same data path, such as having one set of queues scheduled by WRR and that group participating in a priority scheduling system in which other queues compete with it in that way.  It might also point to a second scheduler in a hierarchical scheduling system.  If the row pointed to is zeroDotZero, no further Differentiated Services treatment is performed on traffic of this data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulermethod
            
            	The scheduling algorithm used by this Scheduler. zeroDotZero indicates that this is unknown.  Standard values for generic algorithms\: diffServSchedulerPriority, diffServSchedulerWRR, and diffServSchedulerWFQ are specified in this MIB; additional values    may be further specified in other MIBs
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulerminrate
            
            	This RowPointer indicates the entry in diffServMinRateTable which indicates the priority or minimum output rate from this scheduler. This attribute is used only when there is more than one level of scheduler.  When it has the value zeroDotZero, it indicates that no minimum rate or priority is imposed.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulermaxrate
            
            	This RowPointer indicates the entry in diffServMaxRateTable which indicates the maximum output rate from this scheduler. When more than one maximum rate applies (eg, when a multi\-rate shaper is in view), it points to the first of those rate entries. This attribute is used only when there is more than one level of scheduler.  When it has the value zeroDotZero, it indicates that no maximum rate is imposed.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulerstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservschedulerstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry, self).__init__()

                self.yang_name = "diffServSchedulerEntry"
                self.yang_parent_name = "diffServSchedulerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservschedulerid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservschedulerid', (YLeaf(YType.uint32, 'diffServSchedulerId'), ['int'])),
                    ('diffservschedulernext', (YLeaf(YType.str, 'diffServSchedulerNext'), ['str'])),
                    ('diffservschedulermethod', (YLeaf(YType.str, 'diffServSchedulerMethod'), ['str'])),
                    ('diffservschedulerminrate', (YLeaf(YType.str, 'diffServSchedulerMinRate'), ['str'])),
                    ('diffservschedulermaxrate', (YLeaf(YType.str, 'diffServSchedulerMaxRate'), ['str'])),
                    ('diffservschedulerstorage', (YLeaf(YType.enumeration, 'diffServSchedulerStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservschedulerstatus', (YLeaf(YType.enumeration, 'diffServSchedulerStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservschedulerid = None
                self.diffservschedulernext = None
                self.diffservschedulermethod = None
                self.diffservschedulerminrate = None
                self.diffservschedulermaxrate = None
                self.diffservschedulerstorage = None
                self.diffservschedulerstatus = None
                self._segment_path = lambda: "diffServSchedulerEntry" + "[diffServSchedulerId='" + str(self.diffservschedulerid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServSchedulerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry, [u'diffservschedulerid', u'diffservschedulernext', u'diffservschedulermethod', u'diffservschedulerminrate', u'diffservschedulermaxrate', u'diffservschedulerstorage', u'diffservschedulerstatus'], name, value)


    class DiffServMinRateTable(Entity):
        """
        The Minimum Rate Parameters Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservminrateentry
        
        	An entry in the Minimum Rate Parameters Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of  		 :py:class:`DiffServMinRateEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServMinRateTable, self).__init__()

            self.yang_name = "diffServMinRateTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServMinRateEntry", ("diffservminrateentry", DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry))])
            self._leafs = OrderedDict()

            self.diffservminrateentry = YList(self)
            self._segment_path = lambda: "diffServMinRateTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServMinRateTable, [], name, value)


        class DiffServMinRateEntry(Entity):
            """
            An entry in the Minimum Rate Parameters Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservminrateid  (key)
            
            	An index that enumerates the Scheduler Parameter entries. Managers obtain new values for row creation in this table by reading diffServMinRateNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminratepriority
            
            	The priority of this input to the associated scheduler, relative    to the scheduler's other inputs. A queue or scheduler with a larger numeric value will be served before another with a smaller numeric value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminrateabsolute
            
            	The minimum absolute rate, in kilobits/sec, that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservminraterelative
            
            	The minimum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:      diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservminratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry, self).__init__()

                self.yang_name = "diffServMinRateEntry"
                self.yang_parent_name = "diffServMinRateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservminrateid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservminrateid', (YLeaf(YType.uint32, 'diffServMinRateId'), ['int'])),
                    ('diffservminratepriority', (YLeaf(YType.uint32, 'diffServMinRatePriority'), ['int'])),
                    ('diffservminrateabsolute', (YLeaf(YType.uint32, 'diffServMinRateAbsolute'), ['int'])),
                    ('diffservminraterelative', (YLeaf(YType.uint32, 'diffServMinRateRelative'), ['int'])),
                    ('diffservminratestorage', (YLeaf(YType.enumeration, 'diffServMinRateStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservminratestatus', (YLeaf(YType.enumeration, 'diffServMinRateStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservminrateid = None
                self.diffservminratepriority = None
                self.diffservminrateabsolute = None
                self.diffservminraterelative = None
                self.diffservminratestorage = None
                self.diffservminratestatus = None
                self._segment_path = lambda: "diffServMinRateEntry" + "[diffServMinRateId='" + str(self.diffservminrateid) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServMinRateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry, [u'diffservminrateid', u'diffservminratepriority', u'diffservminrateabsolute', u'diffservminraterelative', u'diffservminratestorage', u'diffservminratestatus'], name, value)


    class DiffServMaxRateTable(Entity):
        """
        The Maximum Rate Parameter Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservmaxrateentry
        
        	An entry in the Maximum Rate Parameter Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of  		 :py:class:`DiffServMaxRateEntry <ydk.models.cisco_ios_xe.DIFFSERV_MIB.DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry>`
        
        

        """

        _prefix = 'DIFFSERV-MIB'
        _revision = '2002-02-07'

        def __init__(self):
            super(DIFFSERVMIB.DiffServMaxRateTable, self).__init__()

            self.yang_name = "diffServMaxRateTable"
            self.yang_parent_name = "DIFFSERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("diffServMaxRateEntry", ("diffservmaxrateentry", DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry))])
            self._leafs = OrderedDict()

            self.diffservmaxrateentry = YList(self)
            self._segment_path = lambda: "diffServMaxRateTable"
            self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DIFFSERVMIB.DiffServMaxRateTable, [], name, value)


        class DiffServMaxRateEntry(Entity):
            """
            An entry in the Maximum Rate Parameter Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservmaxrateid  (key)
            
            	An index that enumerates the Maximum Rate Parameter entries. Managers obtain new values for row creation in this table by reading diffServMaxRateNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratelevel  (key)
            
            	An index that indicates which level of a multi\-rate shaper is being given its parameters. A multi\-rate shaper has some number of rate levels. Frame Relay's dual rate specification refers to a 'committed' and an 'excess' rate; ATM's dual rate specification refers to a 'mean' and a 'peak' rate. This table is generalized to support an arbitrary number of rates. The committed or mean rate is level 1, the peak rate (if any) is the highest level rate configured, and if there are other rates they are distributed in monotonically increasing order between them
            	**type**\: int
            
            	**range:** 1..32
            
            .. attribute:: diffservmaxrateabsolute
            
            	The maximum rate in kilobits/sec that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no maximum rate limit and that the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following    equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: diffservmaxraterelative
            
            	The maximum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no maximum rate limit and the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratethreshold
            
            	The number of bytes of queue depth at which the rate of a    multi\-rate scheduler will increase to the next output rate. In the last conceptual row for such a shaper, this threshold is ignored and by convention is zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: diffservmaxratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: diffservmaxratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DIFFSERV-MIB'
            _revision = '2002-02-07'

            def __init__(self):
                super(DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry, self).__init__()

                self.yang_name = "diffServMaxRateEntry"
                self.yang_parent_name = "diffServMaxRateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['diffservmaxrateid','diffservmaxratelevel']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('diffservmaxrateid', (YLeaf(YType.uint32, 'diffServMaxRateId'), ['int'])),
                    ('diffservmaxratelevel', (YLeaf(YType.uint32, 'diffServMaxRateLevel'), ['int'])),
                    ('diffservmaxrateabsolute', (YLeaf(YType.uint32, 'diffServMaxRateAbsolute'), ['int'])),
                    ('diffservmaxraterelative', (YLeaf(YType.uint32, 'diffServMaxRateRelative'), ['int'])),
                    ('diffservmaxratethreshold', (YLeaf(YType.int32, 'diffServMaxRateThreshold'), ['int'])),
                    ('diffservmaxratestorage', (YLeaf(YType.enumeration, 'diffServMaxRateStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('diffservmaxratestatus', (YLeaf(YType.enumeration, 'diffServMaxRateStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.diffservmaxrateid = None
                self.diffservmaxratelevel = None
                self.diffservmaxrateabsolute = None
                self.diffservmaxraterelative = None
                self.diffservmaxratethreshold = None
                self.diffservmaxratestorage = None
                self.diffservmaxratestatus = None
                self._segment_path = lambda: "diffServMaxRateEntry" + "[diffServMaxRateId='" + str(self.diffservmaxrateid) + "']" + "[diffServMaxRateLevel='" + str(self.diffservmaxratelevel) + "']"
                self._absolute_path = lambda: "DIFFSERV-MIB:DIFFSERV-MIB/diffServMaxRateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry, [u'diffservmaxrateid', u'diffservmaxratelevel', u'diffservmaxrateabsolute', u'diffservmaxraterelative', u'diffservmaxratethreshold', u'diffservmaxratestorage', u'diffservmaxratestatus'], name, value)

    def clone_ptr(self):
        self._top_entity = DIFFSERVMIB()
        return self._top_entity

