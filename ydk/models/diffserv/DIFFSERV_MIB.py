""" DIFFSERV_MIB 

This MIB defines the objects necessary to manage a device that
uses the Differentiated Services Architecture described in RFC
2475. The Conceptual Model of a Differentiated Services Router
provides supporting information on how such a router is modeled.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity_Identity
from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum

class IfDirection_Enum(Enum):
    """
    IfDirection_Enum

    IfDirection specifies a direction of data travel on an
    interface. 'inbound' traffic is operated on during reception from
    the interface, while 'outbound' traffic is operated on prior to
    transmission on the interface.

    """

    INBOUND = 1

    OUTBOUND = 2


    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['IfDirection_Enum']



class DIFFSERVMIB(object):
    """
    
    
    .. attribute:: diffservaction
    
    	
    	**type**\: :py:class:`DiffServAction <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServAction>`
    
    .. attribute:: diffservactiontable
    
    	The Action Table enumerates actions that can be performed to a stream of traffic. Multiple actions can be concatenated. For example, traffic exiting from a meter may be counted, marked, and potentially dropped before entering a queue.  Specific actions are indicated by diffServActionSpecific which points to an entry of a specific action type parameterizing the action in detail
    	**type**\: :py:class:`DiffServActionTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServActionTable>`
    
    .. attribute:: diffservalgdrop
    
    	
    	**type**\: :py:class:`DiffServAlgDrop <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDrop>`
    
    .. attribute:: diffservalgdroptable
    
    	The algorithmic drop table contains entries describing an element that drops packets according to some algorithm
    	**type**\: :py:class:`DiffServAlgDropTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable>`
    
    .. attribute:: diffservclassifier
    
    	
    	**type**\: :py:class:`DiffServClassifier <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServClassifier>`
    
    .. attribute:: diffservclfrelementtable
    
    	The classifier element table enumerates the relationship between classification patterns and subsequent downstream Differentiated Services Functional Data Path elements. diffServClfrElementSpecific points to a filter that specifies the classification parameters. A classifier may use filter tables of different types together.  One example of a filter table defined in this MIB is diffServMultiFieldClfrTable, for IP Multi\-Field Classifiers (MFCs). Such an entry might identify anything from a single micro\-flow (an identifiable sub\-session packet stream directed from one sending transport to the receiving transport or transports), or aggregates of those such as the traffic from a host, traffic for an application, or traffic between two hosts using an application and a given DSCP. The standard Behavior Aggregate used in the Differentiated Services Architecture is encoded as a degenerate case of such an aggregate \- the traffic using a particular DSCP value.  Filter tables for other filter types may be defined elsewhere
    	**type**\: :py:class:`DiffServClfrElementTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrElementTable>`
    
    .. attribute:: diffservclfrtable
    
    	This table enumerates all the diffserv classifier functional data path elements of this device.  The actual classification definitions are defined in diffServClfrElementTable entries belonging to each classifier.  An entry in this table, pointed to by a RowPointer specifying an instance of diffServClfrStatus, is frequently used as the name for a set of classifier elements, which all use the index diffServClfrId. Per the semantics of the classifier element table, these entries constitute one or more unordered sets of tests which may be simultaneously applied to a message to    classify it.  The primary function of this table is to ensure that the value of diffServClfrId is unique before attempting to use it in creating a diffServClfrElementEntry. Therefore, the diffServClfrEntry must be created on the same SET as the diffServClfrElementEntry, or before the diffServClfrElementEntry is created
    	**type**\: :py:class:`DiffServClfrTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrTable>`
    
    .. attribute:: diffservcountacttable
    
    	This table contains counters for all the traffic passing through an action element
    	**type**\: :py:class:`DiffServCountActTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServCountActTable>`
    
    .. attribute:: diffservdatapathtable
    
    	The data path table contains RowPointers indicating the start of the functional data path for each interface and traffic direction in this device. These may merge, or be separated into parallel data paths
    	**type**\: :py:class:`DiffServDataPathTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServDataPathTable>`
    
    .. attribute:: diffservdscpmarkacttable
    
    	This table enumerates specific DSCPs used for marking or remarking the DSCP field of IP packets. The entries of this table may be referenced by a diffServActionSpecific attribute
    	**type**\: :py:class:`DiffServDscpMarkActTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServDscpMarkActTable>`
    
    .. attribute:: diffservmaxratetable
    
    	The Maximum Rate Parameter Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\: :py:class:`DiffServMaxRateTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMaxRateTable>`
    
    .. attribute:: diffservmeter
    
    	
    	**type**\: :py:class:`DiffServMeter <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeter>`
    
    .. attribute:: diffservmetertable
    
    	This table enumerates specific meters that a system may use to police a stream of traffic. The traffic stream to be metered is determined by the Differentiated Services Functional Data Path Element(s) upstream of the meter i.e. by the object(s) that point to each entry in this table.  This may include all traffic on an interface.  Specific meter details are to be found in table entry referenced by diffServMeterSpecific
    	**type**\: :py:class:`DiffServMeterTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeterTable>`
    
    .. attribute:: diffservminratetable
    
    	The Minimum Rate Parameters Table enumerates individual sets of scheduling parameter that can be used/reused by Queues and Schedulers
    	**type**\: :py:class:`DiffServMinRateTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMinRateTable>`
    
    .. attribute:: diffservmultifieldclfrtable
    
    	A table of IP Multi\-field Classifier filter entries that a    system may use to identify IP traffic
    	**type**\: :py:class:`DiffServMultiFieldClfrTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMultiFieldClfrTable>`
    
    .. attribute:: diffservqtable
    
    	The Queue Table enumerates the individual queues.  Note that the MIB models queuing systems as composed of individual queues, one per class of traffic, even though they may in fact be structured as classes of traffic scheduled using a common calendar queue, or in other ways
    	**type**\: :py:class:`DiffServQTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServQTable>`
    
    .. attribute:: diffservqueue
    
    	
    	**type**\: :py:class:`DiffServQueue <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServQueue>`
    
    .. attribute:: diffservrandomdroptable
    
    	The random drop table contains entries describing a process that drops packets randomly. Entries in this table are pointed to by diffServAlgDropSpecific
    	**type**\: :py:class:`DiffServRandomDropTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServRandomDropTable>`
    
    .. attribute:: diffservscheduler
    
    	
    	**type**\: :py:class:`DiffServScheduler <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServScheduler>`
    
    .. attribute:: diffservschedulertable
    
    	The Scheduler Table enumerates packet schedulers. Multiple scheduling algorithms can be used on a given data path, with each algorithm described by one diffServSchedulerEntry
    	**type**\: :py:class:`DiffServSchedulerTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServSchedulerTable>`
    
    .. attribute:: diffservtbparam
    
    	
    	**type**\: :py:class:`DiffServTBParam <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParam>`
    
    .. attribute:: diffservtbparamtable
    
    	This table enumerates a single set of token bucket meter parameters that a system may use to police a stream of traffic. Such meters are modeled here as having a single rate and a single burst size. Multiple entries are used when multiple rates/burst sizes are needed
    	**type**\: :py:class:`DiffServTBParamTable <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParamTable>`
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        self.diffservaction = DIFFSERVMIB.DiffServAction()
        self.diffservaction.parent = self
        self.diffservactiontable = DIFFSERVMIB.DiffServActionTable()
        self.diffservactiontable.parent = self
        self.diffservalgdrop = DIFFSERVMIB.DiffServAlgDrop()
        self.diffservalgdrop.parent = self
        self.diffservalgdroptable = DIFFSERVMIB.DiffServAlgDropTable()
        self.diffservalgdroptable.parent = self
        self.diffservclassifier = DIFFSERVMIB.DiffServClassifier()
        self.diffservclassifier.parent = self
        self.diffservclfrelementtable = DIFFSERVMIB.DiffServClfrElementTable()
        self.diffservclfrelementtable.parent = self
        self.diffservclfrtable = DIFFSERVMIB.DiffServClfrTable()
        self.diffservclfrtable.parent = self
        self.diffservcountacttable = DIFFSERVMIB.DiffServCountActTable()
        self.diffservcountacttable.parent = self
        self.diffservdatapathtable = DIFFSERVMIB.DiffServDataPathTable()
        self.diffservdatapathtable.parent = self
        self.diffservdscpmarkacttable = DIFFSERVMIB.DiffServDscpMarkActTable()
        self.diffservdscpmarkacttable.parent = self
        self.diffservmaxratetable = DIFFSERVMIB.DiffServMaxRateTable()
        self.diffservmaxratetable.parent = self
        self.diffservmeter = DIFFSERVMIB.DiffServMeter()
        self.diffservmeter.parent = self
        self.diffservmetertable = DIFFSERVMIB.DiffServMeterTable()
        self.diffservmetertable.parent = self
        self.diffservminratetable = DIFFSERVMIB.DiffServMinRateTable()
        self.diffservminratetable.parent = self
        self.diffservmultifieldclfrtable = DIFFSERVMIB.DiffServMultiFieldClfrTable()
        self.diffservmultifieldclfrtable.parent = self
        self.diffservqtable = DIFFSERVMIB.DiffServQTable()
        self.diffservqtable.parent = self
        self.diffservqueue = DIFFSERVMIB.DiffServQueue()
        self.diffservqueue.parent = self
        self.diffservrandomdroptable = DIFFSERVMIB.DiffServRandomDropTable()
        self.diffservrandomdroptable.parent = self
        self.diffservscheduler = DIFFSERVMIB.DiffServScheduler()
        self.diffservscheduler.parent = self
        self.diffservschedulertable = DIFFSERVMIB.DiffServSchedulerTable()
        self.diffservschedulertable.parent = self
        self.diffservtbparam = DIFFSERVMIB.DiffServTBParam()
        self.diffservtbparam.parent = self
        self.diffservtbparamtable = DIFFSERVMIB.DiffServTBParamTable()
        self.diffservtbparamtable.parent = self


    class DiffServAction(object):
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

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservactionnextfree = None
            self.diffservcountactnextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServAction'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservactionnextfree is not None:
                return True

            if self.diffservcountactnextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServAction']['meta_info']


    class DiffServActionTable(object):
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
        	**type**\: list of :py:class:`DiffServActionEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServActionTable.DiffServActionEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservactionentry = YList()
            self.diffservactionentry.parent = self
            self.diffservactionentry.name = 'diffservactionentry'


        class DiffServActionEntry(object):
            """
            Each entry in the action table allows description of one
            specific action to be applied to traffic.
            
            .. attribute:: diffservactionid
            
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
            
            .. attribute:: diffservactionstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservactionstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservactionid = None
                self.diffservactioninterface = None
                self.diffservactionnext = None
                self.diffservactionspecific = None
                self.diffservactionstatus = None
                self.diffservactionstorage = None

            @property
            def _common_path(self):
                if self.diffservactionid is None:
                    raise YPYDataValidationError('Key property diffservactionid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServActionTable/DIFFSERV-MIB:diffServActionEntry[DIFFSERV-MIB:diffServActionId = ' + str(self.diffservactionid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservactionid is not None:
                    return True

                if self.diffservactioninterface is not None:
                    return True

                if self.diffservactionnext is not None:
                    return True

                if self.diffservactionspecific is not None:
                    return True

                if self.diffservactionstatus is not None:
                    return True

                if self.diffservactionstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServActionTable.DiffServActionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServActionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservactionentry is not None:
                for child_ref in self.diffservactionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServActionTable']['meta_info']


    class DiffServAlgDrop(object):
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

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservalgdropnextfree = None
            self.diffservrandomdropnextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServAlgDrop'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservalgdropnextfree is not None:
                return True

            if self.diffservrandomdropnextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServAlgDrop']['meta_info']


    class DiffServAlgDropTable(object):
        """
        The algorithmic drop table contains entries describing an
        element that drops packets according to some algorithm.
        
        .. attribute:: diffservalgdropentry
        
        	An entry describes a process that drops packets according to some algorithm. Further details of the algorithm type are to be found in diffServAlgDropType and with more detail parameter entry pointed to by diffServAlgDropSpecific when necessary
        	**type**\: list of :py:class:`DiffServAlgDropEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservalgdropentry = YList()
            self.diffservalgdropentry.parent = self
            self.diffservalgdropentry.name = 'diffservalgdropentry'


        class DiffServAlgDropEntry(object):
            """
            An entry describes a process that drops packets according to
            some algorithm. Further details of the algorithm type are to be
            found in diffServAlgDropType and with more detail parameter entry
            pointed to by diffServAlgDropSpecific when necessary.
            
            .. attribute:: diffservalgdropid
            
            	An index that enumerates the Algorithmic Dropper entries. Managers obtain new values for row creation in this table by reading diffServAlgDropNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservalgdropnext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  When diffServAlgDropType is alwaysDrop(5), this object is ignored.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
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
            
            .. attribute:: diffservalgdropqmeasure
            
            	Points to an entry in the diffServQTable to indicate the queue that a drop algorithm is to monitor when deciding whether to drop a packet. If the row pointed to does not exist, the algorithmic dropper element is considered inactive.    Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropqthreshold
            
            	A threshold on the depth in bytes of the queue being measured at which a trigger is generated to the dropping algorithm, unless diffServAlgDropType is alwaysDrop(5) where this object is ignored.  For the tailDrop(2) or headDrop(3) algorithms, this represents the depth of the queue, pointed to by diffServAlgDropQMeasure, at which the drop action will take place. Other algorithms will need to define their own semantics for this threshold
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservalgdropspecific
            
            	Points to a table entry that provides further detail regarding a drop algorithm.  Entries with diffServAlgDropType equal to other(1) may have this point to a table defined in another MIB module.  Entries with diffServAlgDropType equal to randomDrop(4) must have this point to an entry in diffServRandomDropTable.  For all other algorithms specified in this MIB, this should take the value zeroDotZero.  The diffServAlgDropType is authoritative for the type of the drop algorithm and the specific parameters for the drop algorithm needs to be evaluated based on the diffServAlgDropType.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservalgdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservalgdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: diffservalgdroptype
            
            	The type of algorithm used by this dropper. The value other(1) requires further specification in some other MIB module.  In the tailDrop(2) algorithm, diffServAlgDropQThreshold represents the maximum depth of the queue, pointed to by diffServAlgDropQMeasure, beyond which all newly arriving packets will be dropped.  In the headDrop(3) algorithm, if a packet arrives when the current depth of the queue, pointed to by diffServAlgDropQMeasure, is at diffServAlgDropQThreshold, packets currently at the head of the queue are dropped to make room for the new packet to be enqueued at the tail of the queue.  In the randomDrop(4) algorithm, on packet arrival, an Active Queue Management algorithm is executed which may randomly drop a packet. This algorithm may be proprietary, and it may drop either the arriving packet or another packet in the queue. diffServAlgDropSpecific points to a diffServRandomDropEntry that describes the algorithm. For this algorithm,    diffServAlgDropQThreshold is understood to be the absolute maximum size of the queue and additional parameters are described in diffServRandomDropTable.  The alwaysDrop(5) algorithm is as its name specifies; always drop. In this case, the other configuration values in this Entry are not meaningful; There is no useful 'next' processing step, there is no queue, and parameters describing the queue are not useful. Therefore, diffServAlgDropNext, diffServAlgDropMeasure, and diffServAlgDropSpecific are all zeroDotZero
            	**type**\: :py:class:`DiffServAlgDropType_Enum <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry.DiffServAlgDropType_Enum>`
            
            .. attribute:: diffservalgrandomdropoctets
            
            	The number of octets that have been randomly dropped by this drop process.  This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: diffservalgrandomdroppkts
            
            	The number of packets that have been randomly dropped by this drop process. This counter applies, therefore, only to random droppers.  Discontinuities in the value of this counter can occur at re\- initialization of the management system and at other times as indicated by the value of ifCounterDiscontinuityTime on the relevant interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservalgdropid = None
                self.diffservalgdropnext = None
                self.diffservalgdropoctets = None
                self.diffservalgdroppkts = None
                self.diffservalgdropqmeasure = None
                self.diffservalgdropqthreshold = None
                self.diffservalgdropspecific = None
                self.diffservalgdropstatus = None
                self.diffservalgdropstorage = None
                self.diffservalgdroptype = None
                self.diffservalgrandomdropoctets = None
                self.diffservalgrandomdroppkts = None

            class DiffServAlgDropType_Enum(Enum):
                """
                DiffServAlgDropType_Enum

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

                """

                OTHER = 1

                TAILDROP = 2

                HEADDROP = 3

                RANDOMDROP = 4

                ALWAYSDROP = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                    return meta._meta_table['DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry.DiffServAlgDropType_Enum']


            @property
            def _common_path(self):
                if self.diffservalgdropid is None:
                    raise YPYDataValidationError('Key property diffservalgdropid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServAlgDropTable/DIFFSERV-MIB:diffServAlgDropEntry[DIFFSERV-MIB:diffServAlgDropId = ' + str(self.diffservalgdropid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservalgdropid is not None:
                    return True

                if self.diffservalgdropnext is not None:
                    return True

                if self.diffservalgdropoctets is not None:
                    return True

                if self.diffservalgdroppkts is not None:
                    return True

                if self.diffservalgdropqmeasure is not None:
                    return True

                if self.diffservalgdropqthreshold is not None:
                    return True

                if self.diffservalgdropspecific is not None:
                    return True

                if self.diffservalgdropstatus is not None:
                    return True

                if self.diffservalgdropstorage is not None:
                    return True

                if self.diffservalgdroptype is not None:
                    return True

                if self.diffservalgrandomdropoctets is not None:
                    return True

                if self.diffservalgrandomdroppkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServAlgDropTable.DiffServAlgDropEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServAlgDropTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservalgdropentry is not None:
                for child_ref in self.diffservalgdropentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServAlgDropTable']['meta_info']


    class DiffServClassifier(object):
        """
        
        
        .. attribute:: diffservclfrelementnextfree
        
        	This object contains an unused value for diffServClfrElementId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservclfrnextfree
        
        	This object contains an unused value for diffServClfrId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservmultifieldclfrnextfree
        
        	This object contains an unused value for diffServMultiFieldClfrId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservclfrelementnextfree = None
            self.diffservclfrnextfree = None
            self.diffservmultifieldclfrnextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServClassifier'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservclfrelementnextfree is not None:
                return True

            if self.diffservclfrnextfree is not None:
                return True

            if self.diffservmultifieldclfrnextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServClassifier']['meta_info']


    class DiffServClfrElementTable(object):
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
        	**type**\: list of :py:class:`DiffServClfrElementEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservclfrelemententry = YList()
            self.diffservclfrelemententry.parent = self
            self.diffservclfrelemententry.name = 'diffservclfrelemententry'


        class DiffServClfrElementEntry(object):
            """
            An entry in the classifier element table describes a single
            element of the classifier.
            
            .. attribute:: diffservclfrelementid
            
            	An index that enumerates the Classifier Element entries. Managers obtain new values for row creation in this table by reading diffServClfrElementNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrid
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementnext
            
            	This attribute provides one branch of the fan\-out functionality of a classifier described in the Informal Differentiated Services Model section 4.1.  This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementprecedence
            
            	The relative order in which classifier elements are applied\: higher numbers represent classifier element with higher precedence.  Classifier elements with the same order must be unambiguous i.e. they must define non\-overlapping patterns, and are considered to be applied simultaneously to the traffic stream. Classifier elements with different order may overlap in their filters\:  the classifier element with the highest order that matches is taken.  On a given interface, there must be a complete classifier in place at all times in the ingress direction.  This means one or more filters must match any possible pattern. There is no such    requirement in the egress direction
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrelementspecific
            
            	A pointer to a valid entry in another table, filter table, that describes the applicable classification parameters, e.g. an entry in diffServMultiFieldClfrTable.  The value zeroDotZero is interpreted to match anything not matched by another classifier element \- only one such entry may exist for each classifier.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or    becomes inactive by other means, the element is ignored
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservclfrelementstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservclfrelementstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservclfrelementid = None
                self.diffservclfrid = None
                self.diffservclfrelementnext = None
                self.diffservclfrelementprecedence = None
                self.diffservclfrelementspecific = None
                self.diffservclfrelementstatus = None
                self.diffservclfrelementstorage = None

            @property
            def _common_path(self):
                if self.diffservclfrelementid is None:
                    raise YPYDataValidationError('Key property diffservclfrelementid is None')
                if self.diffservclfrid is None:
                    raise YPYDataValidationError('Key property diffservclfrid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServClfrElementTable/DIFFSERV-MIB:diffServClfrElementEntry[DIFFSERV-MIB:diffServClfrElementId = ' + str(self.diffservclfrelementid) + '][DIFFSERV-MIB:diffServClfrId = ' + str(self.diffservclfrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservclfrelementid is not None:
                    return True

                if self.diffservclfrid is not None:
                    return True

                if self.diffservclfrelementnext is not None:
                    return True

                if self.diffservclfrelementprecedence is not None:
                    return True

                if self.diffservclfrelementspecific is not None:
                    return True

                if self.diffservclfrelementstatus is not None:
                    return True

                if self.diffservclfrelementstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServClfrElementTable.DiffServClfrElementEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServClfrElementTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservclfrelemententry is not None:
                for child_ref in self.diffservclfrelemententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServClfrElementTable']['meta_info']


    class DiffServClfrTable(object):
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
        	**type**\: list of :py:class:`DiffServClfrEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservclfrentry = YList()
            self.diffservclfrentry.parent = self
            self.diffservclfrentry.name = 'diffservclfrentry'


        class DiffServClfrEntry(object):
            """
            An entry in the classifier table describes a single classifier.
            All classifier elements belonging to the same classifier use the
            classifier's diffServClfrId as part of their index.
            
            .. attribute:: diffservclfrid
            
            	An index that enumerates the classifier entries.  Managers should obtain new values for row creation in this table by reading diffServClfrNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservclfrid = None
                self.diffservclfrstatus = None
                self.diffservclfrstorage = None

            @property
            def _common_path(self):
                if self.diffservclfrid is None:
                    raise YPYDataValidationError('Key property diffservclfrid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServClfrTable/DIFFSERV-MIB:diffServClfrEntry[DIFFSERV-MIB:diffServClfrId = ' + str(self.diffservclfrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservclfrid is not None:
                    return True

                if self.diffservclfrstatus is not None:
                    return True

                if self.diffservclfrstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServClfrTable.DiffServClfrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServClfrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservclfrentry is not None:
                for child_ref in self.diffservclfrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServClfrTable']['meta_info']


    class DiffServCountActTable(object):
        """
        This table contains counters for all the traffic passing through
        an action element.
        
        .. attribute:: diffservcountactentry
        
        	An entry in the count action table describes a single set of traffic counters
        	**type**\: list of :py:class:`DiffServCountActEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservcountactentry = YList()
            self.diffservcountactentry.parent = self
            self.diffservcountactentry.name = 'diffservcountactentry'


        class DiffServCountActEntry(object):
            """
            An entry in the count action table describes a single set of
            traffic counters.
            
            .. attribute:: diffservcountactid
            
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
            
            .. attribute:: diffservcountactstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing    to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservcountactstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservcountactid = None
                self.diffservcountactoctets = None
                self.diffservcountactpkts = None
                self.diffservcountactstatus = None
                self.diffservcountactstorage = None

            @property
            def _common_path(self):
                if self.diffservcountactid is None:
                    raise YPYDataValidationError('Key property diffservcountactid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServCountActTable/DIFFSERV-MIB:diffServCountActEntry[DIFFSERV-MIB:diffServCountActId = ' + str(self.diffservcountactid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservcountactid is not None:
                    return True

                if self.diffservcountactoctets is not None:
                    return True

                if self.diffservcountactpkts is not None:
                    return True

                if self.diffservcountactstatus is not None:
                    return True

                if self.diffservcountactstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServCountActTable.DiffServCountActEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServCountActTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservcountactentry is not None:
                for child_ref in self.diffservcountactentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServCountActTable']['meta_info']


    class DiffServDataPathTable(object):
        """
        The data path table contains RowPointers indicating the start of
        the functional data path for each interface and traffic direction
        in this device. These may merge, or be separated into parallel
        data paths.
        
        .. attribute:: diffservdatapathentry
        
        	An entry in the data path table indicates the start of a single Differentiated Services Functional Data Path in this device.  These are associated with individual interfaces, logical or physical, and therefore are instantiated by ifIndex. Therefore, the interface index must have been assigned, according to the procedures applicable to that, before it can be meaningfully used. Generally, this means that the interface must exist.  When diffServDataPathStorage is of type nonVolatile, however, this may reflect the configuration for an interface whose ifIndex has been assigned but for which the supporting implementation is not currently present
        	**type**\: list of :py:class:`DiffServDataPathEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservdatapathentry = YList()
            self.diffservdatapathentry.parent = self
            self.diffservdatapathentry.name = 'diffservdatapathentry'


        class DiffServDataPathEntry(object):
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
            
            .. attribute:: diffservdatapathifdirection
            
            	IfDirection specifies whether the reception or transmission path for this interface is in view
            	**type**\: :py:class:`IfDirection_Enum <ydk.models.diffserv.DIFFSERV_MIB.IfDirection_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: diffservdatapathstart
            
            	This selects the first Differentiated Services Functional Data Path Element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no Differentiated Services treatment is performed on traffic of this data path. A pointer with the value zeroDotZero normally terminates a functional data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservdatapathstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservdatapathstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservdatapathifdirection = None
                self.ifindex = None
                self.diffservdatapathstart = None
                self.diffservdatapathstatus = None
                self.diffservdatapathstorage = None

            @property
            def _common_path(self):
                if self.diffservdatapathifdirection is None:
                    raise YPYDataValidationError('Key property diffservdatapathifdirection is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServDataPathTable/DIFFSERV-MIB:diffServDataPathEntry[DIFFSERV-MIB:diffServDataPathIfDirection = ' + str(self.diffservdatapathifdirection) + '][DIFFSERV-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservdatapathifdirection is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.diffservdatapathstart is not None:
                    return True

                if self.diffservdatapathstatus is not None:
                    return True

                if self.diffservdatapathstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServDataPathTable.DiffServDataPathEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServDataPathTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservdatapathentry is not None:
                for child_ref in self.diffservdatapathentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServDataPathTable']['meta_info']


    class DiffServDscpMarkActTable(object):
        """
        This table enumerates specific DSCPs used for marking or
        remarking the DSCP field of IP packets. The entries of this table
        may be referenced by a diffServActionSpecific attribute.
        
        .. attribute:: diffservdscpmarkactentry
        
        	An entry in the DSCP mark action table that describes a single DSCP used for marking
        	**type**\: list of :py:class:`DiffServDscpMarkActEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservdscpmarkactentry = YList()
            self.diffservdscpmarkactentry.parent = self
            self.diffservdscpmarkactentry.name = 'diffservdscpmarkactentry'


        class DiffServDscpMarkActEntry(object):
            """
            An entry in the DSCP mark action table that describes a single
            DSCP used for marking.
            
            .. attribute:: diffservdscpmarkactdscp
            
            	The DSCP that this Action will store into the DSCP field of the subject. It is quite possible that the only packets subject to this Action are already marked with this DSCP. Note also that Differentiated Services processing may result in packet being marked on both ingress to a network and on egress from it, and that ingress and egress can occur in the same router
            	**type**\: int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservdscpmarkactdscp = None

            @property
            def _common_path(self):
                if self.diffservdscpmarkactdscp is None:
                    raise YPYDataValidationError('Key property diffservdscpmarkactdscp is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServDscpMarkActTable/DIFFSERV-MIB:diffServDscpMarkActEntry[DIFFSERV-MIB:diffServDscpMarkActDscp = ' + str(self.diffservdscpmarkactdscp) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservdscpmarkactdscp is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServDscpMarkActTable.DiffServDscpMarkActEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServDscpMarkActTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservdscpmarkactentry is not None:
                for child_ref in self.diffservdscpmarkactentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServDscpMarkActTable']['meta_info']


    class DiffServMaxRateTable(object):
        """
        The Maximum Rate Parameter Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservmaxrateentry
        
        	An entry in the Maximum Rate Parameter Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of :py:class:`DiffServMaxRateEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservmaxrateentry = YList()
            self.diffservmaxrateentry.parent = self
            self.diffservmaxrateentry.name = 'diffservmaxrateentry'


        class DiffServMaxRateEntry(object):
            """
            An entry in the Maximum Rate Parameter Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservmaxrateid
            
            	An index that enumerates the Maximum Rate Parameter entries. Managers obtain new values for row creation in this table by reading diffServMaxRateNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratelevel
            
            	An index that indicates which level of a multi\-rate shaper is being given its parameters. A multi\-rate shaper has some number of rate levels. Frame Relay's dual rate specification refers to a 'committed' and an 'excess' rate; ATM's dual rate specification refers to a 'mean' and a 'peak' rate. This table is generalized to support an arbitrary number of rates. The committed or mean rate is level 1, the peak rate (if any) is the highest level rate configured, and if there are other rates they are distributed in monotonically increasing order between them
            	**type**\: int
            
            	**range:** 1..32
            
            .. attribute:: diffservmaxrateabsolute
            
            	The maximum rate in kilobits/sec that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no maximum rate limit and that the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following    equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxraterelative
            
            	The maximum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no maximum rate limit and the scheduler should attempt to be work conserving for this queue. If the value is non\-zero, the scheduler will limit the servicing of this queue to, at most, this rate in a non\-work\-conserving manner.  Note that this attribute value and that of diffServMaxRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMaxRateRelative =           (diffServMaxRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmaxratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservmaxratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: diffservmaxratethreshold
            
            	The number of bytes of queue depth at which the rate of a    multi\-rate scheduler will increase to the next output rate. In the last conceptual row for such a shaper, this threshold is ignored and by convention is zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservmaxrateid = None
                self.diffservmaxratelevel = None
                self.diffservmaxrateabsolute = None
                self.diffservmaxraterelative = None
                self.diffservmaxratestatus = None
                self.diffservmaxratestorage = None
                self.diffservmaxratethreshold = None

            @property
            def _common_path(self):
                if self.diffservmaxrateid is None:
                    raise YPYDataValidationError('Key property diffservmaxrateid is None')
                if self.diffservmaxratelevel is None:
                    raise YPYDataValidationError('Key property diffservmaxratelevel is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMaxRateTable/DIFFSERV-MIB:diffServMaxRateEntry[DIFFSERV-MIB:diffServMaxRateId = ' + str(self.diffservmaxrateid) + '][DIFFSERV-MIB:diffServMaxRateLevel = ' + str(self.diffservmaxratelevel) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservmaxrateid is not None:
                    return True

                if self.diffservmaxratelevel is not None:
                    return True

                if self.diffservmaxrateabsolute is not None:
                    return True

                if self.diffservmaxraterelative is not None:
                    return True

                if self.diffservmaxratestatus is not None:
                    return True

                if self.diffservmaxratestorage is not None:
                    return True

                if self.diffservmaxratethreshold is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServMaxRateTable.DiffServMaxRateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMaxRateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservmaxrateentry is not None:
                for child_ref in self.diffservmaxrateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServMaxRateTable']['meta_info']


    class DiffServMeter(object):
        """
        
        
        .. attribute:: diffservmeternextfree
        
        	This object contains an unused value for diffServMeterId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservmeternextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMeter'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservmeternextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServMeter']['meta_info']


    class DiffServMeterTable(object):
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
        	**type**\: list of :py:class:`DiffServMeterEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservmeterentry = YList()
            self.diffservmeterentry.parent = self
            self.diffservmeterentry.name = 'diffservmeterentry'


        class DiffServMeterEntry(object):
            """
            An entry in the meter table describes a single conformance level
            of a meter.
            
            .. attribute:: diffservmeterid
            
            	An index that enumerates the Meter entries.  Managers obtain new values for row creation in this table by reading diffServMeterNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmeterfailnext
            
            	If the traffic does not conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry      diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterspecific
            
            	This indicates the behavior of the meter by pointing to an entry containing detailed parameters. Note that entries in that specific table must be managed explicitly.  For example, diffServMeterSpecific may point to an entry in diffServTBParamTable, which contains an instance of a single set of Token Bucket parameters.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the meter always succeeds
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservmeterstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservmeterstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: diffservmetersucceednext
            
            	If the traffic does conform, this selects the next Differentiated Services Functional Data Path element to handle traffic for this data path. This RowPointer should point to an instance of one of\:   diffServClfrEntry   diffServMeterEntry   diffServActionEntry   diffServAlgDropEntry   diffServQEntry  A value of zeroDotZero in this attribute indicates that no further Differentiated Services treatment is performed on traffic of this data path. The use of zeroDotZero is the normal usage for the last functional data path element of the current data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservmeterid = None
                self.diffservmeterfailnext = None
                self.diffservmeterspecific = None
                self.diffservmeterstatus = None
                self.diffservmeterstorage = None
                self.diffservmetersucceednext = None

            @property
            def _common_path(self):
                if self.diffservmeterid is None:
                    raise YPYDataValidationError('Key property diffservmeterid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMeterTable/DIFFSERV-MIB:diffServMeterEntry[DIFFSERV-MIB:diffServMeterId = ' + str(self.diffservmeterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservmeterid is not None:
                    return True

                if self.diffservmeterfailnext is not None:
                    return True

                if self.diffservmeterspecific is not None:
                    return True

                if self.diffservmeterstatus is not None:
                    return True

                if self.diffservmeterstorage is not None:
                    return True

                if self.diffservmetersucceednext is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServMeterTable.DiffServMeterEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMeterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservmeterentry is not None:
                for child_ref in self.diffservmeterentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServMeterTable']['meta_info']


    class DiffServMinRateTable(object):
        """
        The Minimum Rate Parameters Table enumerates individual sets of
        scheduling parameter that can be used/reused by Queues and
        Schedulers.
        
        .. attribute:: diffservminrateentry
        
        	An entry in the Minimum Rate Parameters Table describes a single set of scheduling parameters for use by one or more queues or schedulers
        	**type**\: list of :py:class:`DiffServMinRateEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservminrateentry = YList()
            self.diffservminrateentry.parent = self
            self.diffservminrateentry.name = 'diffservminrateentry'


        class DiffServMinRateEntry(object):
            """
            An entry in the Minimum Rate Parameters Table describes a single
            set of scheduling parameters for use by one or more queues or
            schedulers.
            
            .. attribute:: diffservminrateid
            
            	An index that enumerates the Scheduler Parameter entries. Managers obtain new values for row creation in this table by reading diffServMinRateNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminrateabsolute
            
            	The minimum absolute rate, in kilobits/sec, that a downstream scheduler element should allocate to this queue. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateRelative are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:    diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminratepriority
            
            	The priority of this input to the associated scheduler, relative    to the scheduler's other inputs. A queue or scheduler with a larger numeric value will be served before another with a smaller numeric value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminraterelative
            
            	The minimum rate that a downstream scheduler element should allocate to this queue, relative to the maximum rate of the interface as reported by ifSpeed or ifHighSpeed, in units of 1/1000 of 1. If the value is zero, then there is effectively no minimum rate guarantee. If the value is non\-zero, the scheduler will assure the servicing of this queue to at least this rate.  Note that this attribute value and that of diffServMinRateAbsolute are coupled\: changes to one will affect the value of the other. They are linked by the following equation, in that setting one will change the other\:      diffServMinRateRelative =           (diffServMinRateAbsolute\*1000000)/ifSpeed  or, if appropriate\:    diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservminratestatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservminratestorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservminrateid = None
                self.diffservminrateabsolute = None
                self.diffservminratepriority = None
                self.diffservminraterelative = None
                self.diffservminratestatus = None
                self.diffservminratestorage = None

            @property
            def _common_path(self):
                if self.diffservminrateid is None:
                    raise YPYDataValidationError('Key property diffservminrateid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMinRateTable/DIFFSERV-MIB:diffServMinRateEntry[DIFFSERV-MIB:diffServMinRateId = ' + str(self.diffservminrateid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservminrateid is not None:
                    return True

                if self.diffservminrateabsolute is not None:
                    return True

                if self.diffservminratepriority is not None:
                    return True

                if self.diffservminraterelative is not None:
                    return True

                if self.diffservminratestatus is not None:
                    return True

                if self.diffservminratestorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServMinRateTable.DiffServMinRateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMinRateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservminrateentry is not None:
                for child_ref in self.diffservminrateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServMinRateTable']['meta_info']


    class DiffServMultiFieldClfrTable(object):
        """
        A table of IP Multi\-field Classifier filter entries that a
        
        
        
        system may use to identify IP traffic.
        
        .. attribute:: diffservmultifieldclfrentry
        
        	An IP Multi\-field Classifier entry describes a single filter
        	**type**\: list of :py:class:`DiffServMultiFieldClfrEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservmultifieldclfrentry = YList()
            self.diffservmultifieldclfrentry.parent = self
            self.diffservmultifieldclfrentry.name = 'diffservmultifieldclfrentry'


        class DiffServMultiFieldClfrEntry(object):
            """
            An IP Multi\-field Classifier entry describes a single filter.
            
            .. attribute:: diffservmultifieldclfrid
            
            	An index that enumerates the MultiField Classifier filter entries.  Managers obtain new values for row creation in this table by reading diffServMultiFieldClfrNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservmultifieldclfraddrtype
            
            	The type of IP address used by this classifier entry.  While other types of addresses are defined in the InetAddressType    textual convention, and DNS names, a classifier can only look at packets on the wire. Therefore, this object is limited to IPv4 and IPv6 addresses
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: diffservmultifieldclfrdscp
            
            	The value that the DSCP in the packet must have to match this entry. A value of \-1 indicates that a specific DSCP value has not been defined and thus all DSCP values are considered a match
            	**type**\: int
            
            	**range:** \-1..63
            
            .. attribute:: diffservmultifieldclfrdstaddr
            
            	The IP address to match against the packet's destination IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.  diffServMultiFieldClfrDstPrefixLength indicates the number of bits that are relevant
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: diffservmultifieldclfrdstl4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrDstL4PortMin
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrdstl4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrdstprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrDstAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: diffservmultifieldclfrflowid
            
            	The flow identifier in an IPv6 header
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: diffservmultifieldclfrprotocol
            
            	The IP protocol to match against the IPv4 protocol number or the IPv6 Next\- Header number in the packet. A value of 255 means match all.  Note the protocol number of 255 is reserved by IANA, and Next\-Header number of 0 is used in IPv6
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: diffservmultifieldclfrsrcaddr
            
            	The IP address to match against the packet's source IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix. diffServMultiFieldClfrSrcPrefixLength indicates the number of bits that are relevant
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: diffservmultifieldclfrsrcl4portmax
            
            	The maximum value that the layer\-4 source port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in diffServMultiFieldClfrSrcL4PortMin
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcl4portmin
            
            	The minimum value that the layer\-4 source port number in the packet must have in order to match this classifier entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: diffservmultifieldclfrsrcprefixlength
            
            	The length of the CIDR Prefix carried in diffServMultiFieldClfrSrcAddr. In IPv4 addresses, a length of 0 indicates a match of any address; a length of 32 indicates a match of a single host address, and a length between 0 and 32 indicates the use of a CIDR Prefix. IPv6 is similar, except that prefix lengths range from 0..128
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: diffservmultifieldclfrstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservmultifieldclfrstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservmultifieldclfrid = None
                self.diffservmultifieldclfraddrtype = None
                self.diffservmultifieldclfrdscp = None
                self.diffservmultifieldclfrdstaddr = None
                self.diffservmultifieldclfrdstl4portmax = None
                self.diffservmultifieldclfrdstl4portmin = None
                self.diffservmultifieldclfrdstprefixlength = None
                self.diffservmultifieldclfrflowid = None
                self.diffservmultifieldclfrprotocol = None
                self.diffservmultifieldclfrsrcaddr = None
                self.diffservmultifieldclfrsrcl4portmax = None
                self.diffservmultifieldclfrsrcl4portmin = None
                self.diffservmultifieldclfrsrcprefixlength = None
                self.diffservmultifieldclfrstatus = None
                self.diffservmultifieldclfrstorage = None

            @property
            def _common_path(self):
                if self.diffservmultifieldclfrid is None:
                    raise YPYDataValidationError('Key property diffservmultifieldclfrid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMultiFieldClfrTable/DIFFSERV-MIB:diffServMultiFieldClfrEntry[DIFFSERV-MIB:diffServMultiFieldClfrId = ' + str(self.diffservmultifieldclfrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservmultifieldclfrid is not None:
                    return True

                if self.diffservmultifieldclfraddrtype is not None:
                    return True

                if self.diffservmultifieldclfrdscp is not None:
                    return True

                if self.diffservmultifieldclfrdstaddr is not None:
                    return True

                if self.diffservmultifieldclfrdstl4portmax is not None:
                    return True

                if self.diffservmultifieldclfrdstl4portmin is not None:
                    return True

                if self.diffservmultifieldclfrdstprefixlength is not None:
                    return True

                if self.diffservmultifieldclfrflowid is not None:
                    return True

                if self.diffservmultifieldclfrprotocol is not None:
                    return True

                if self.diffservmultifieldclfrsrcaddr is not None:
                    return True

                if self.diffservmultifieldclfrsrcl4portmax is not None:
                    return True

                if self.diffservmultifieldclfrsrcl4portmin is not None:
                    return True

                if self.diffservmultifieldclfrsrcprefixlength is not None:
                    return True

                if self.diffservmultifieldclfrstatus is not None:
                    return True

                if self.diffservmultifieldclfrstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServMultiFieldClfrTable.DiffServMultiFieldClfrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServMultiFieldClfrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservmultifieldclfrentry is not None:
                for child_ref in self.diffservmultifieldclfrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServMultiFieldClfrTable']['meta_info']


    class DiffServQTable(object):
        """
        The Queue Table enumerates the individual queues.  Note that the
        MIB models queuing systems as composed of individual queues, one
        per class of traffic, even though they may in fact be structured
        as classes of traffic scheduled using a common calendar queue, or
        in other ways.
        
        .. attribute:: diffservqentry
        
        	An entry in the Queue Table describes a single queue or class of traffic
        	**type**\: list of :py:class:`DiffServQEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServQTable.DiffServQEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservqentry = YList()
            self.diffservqentry.parent = self
            self.diffservqentry.name = 'diffservqentry'


        class DiffServQEntry(object):
            """
            An entry in the Queue Table describes a single queue or class of
            traffic.
            
            .. attribute:: diffservqid
            
            	An index that enumerates the Queue entries.  Managers obtain new values for row creation in this table by reading diffServQNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservqmaxrate
            
            	This RowPointer indicates the diffServMaxRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the maximum rate is the line speed of the interface.     Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqminrate
            
            	This RowPointer indicates the diffServMinRateEntry that the scheduler, pointed to by diffServQNext, should use to service this queue.  If the row pointed to is zeroDotZero, the minimum rate and priority is unspecified.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqnext
            
            	This selects the next Differentiated Services Scheduler.  The RowPointer must point to a diffServSchedulerEntry.  A value of zeroDotZero in this attribute indicates an incomplete diffServQEntry instance. In such a case, the entry has no operational effect, since it has no parameters to give it meaning.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservqstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservqstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservqid = None
                self.diffservqmaxrate = None
                self.diffservqminrate = None
                self.diffservqnext = None
                self.diffservqstatus = None
                self.diffservqstorage = None

            @property
            def _common_path(self):
                if self.diffservqid is None:
                    raise YPYDataValidationError('Key property diffservqid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServQTable/DIFFSERV-MIB:diffServQEntry[DIFFSERV-MIB:diffServQId = ' + str(self.diffservqid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservqid is not None:
                    return True

                if self.diffservqmaxrate is not None:
                    return True

                if self.diffservqminrate is not None:
                    return True

                if self.diffservqnext is not None:
                    return True

                if self.diffservqstatus is not None:
                    return True

                if self.diffservqstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServQTable.DiffServQEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServQTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservqentry is not None:
                for child_ref in self.diffservqentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServQTable']['meta_info']


    class DiffServQueue(object):
        """
        
        
        .. attribute:: diffservqnextfree
        
        	This object contains an unused value for diffServQId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservqnextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServQueue'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservqnextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServQueue']['meta_info']


    class DiffServRandomDropTable(object):
        """
        The random drop table contains entries describing a process that
        drops packets randomly. Entries in this table are pointed to by
        diffServAlgDropSpecific.
        
        .. attribute:: diffservrandomdropentry
        
        	An entry describes a process that drops packets according to a random algorithm
        	**type**\: list of :py:class:`DiffServRandomDropEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservrandomdropentry = YList()
            self.diffservrandomdropentry.parent = self
            self.diffservrandomdropentry.name = 'diffservrandomdropentry'


        class DiffServRandomDropEntry(object):
            """
            An entry describes a process that drops packets according to a
            random algorithm.
            
            .. attribute:: diffservrandomdropid
            
            	An index that enumerates the Random Drop entries.  Managers obtain new values for row creation in this table by reading diffServRandomDropNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropmaxthreshbytes
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshPkts
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropmaxthreshpkts
            
            	The average queue depth beyond which traffic has a probability indicated by diffServRandomDropProbMax of being dropped or marked. Note that this differs from the physical queue limit, which is stored in diffServAlgDropQThreshold. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMaxThreshBytes
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropminthreshbytes
            
            	The average queue depth in bytes, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshPkts
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropminthreshpkts
            
            	The average queue depth in packets, beyond which traffic has a non\-zero probability of being dropped. Changes in this variable may or may not be reflected in the reported value of diffServRandomDropMinThreshBytes
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservrandomdropprobmax
            
            	The worst case random drop probability, expressed in drops per thousand packets.  For example, if in the worst case every arriving packet may be dropped (100%) for a period, this has the value 1000. Alternatively, if in the worst case only one percent (1%) of traffic may be dropped, it has the value 10
            	**type**\: int
            
            	**range:** 0..1000
            
            .. attribute:: diffservrandomdropsamplingrate
            
            	The number of times per second the queue is sampled for queue average calculation.  A value of zero is used to mean that the queue is sampled approximately each time a packet is enqueued (or dequeued)
            	**type**\: int
            
            	**range:** 0..1000000
            
            .. attribute:: diffservrandomdropstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservrandomdropstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: diffservrandomdropweight
            
            	The weighting of past history in affecting the Exponentially Weighted Moving Average function that calculates the current average queue depth.  The equation uses diffServRandomDropWeight/65536 as the coefficient for the new sample in the equation, and (65536 \- diffServRandomDropWeight)/65536 as the coefficient of the old value.  Implementations may limit the values of diffServRandomDropWeight to a subset of the possible range of values, such as powers of two. Doing this would facilitate implementation of the Exponentially Weighted Moving Average using shift instructions or registers
            	**type**\: int
            
            	**range:** 0..65536
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservrandomdropid = None
                self.diffservrandomdropmaxthreshbytes = None
                self.diffservrandomdropmaxthreshpkts = None
                self.diffservrandomdropminthreshbytes = None
                self.diffservrandomdropminthreshpkts = None
                self.diffservrandomdropprobmax = None
                self.diffservrandomdropsamplingrate = None
                self.diffservrandomdropstatus = None
                self.diffservrandomdropstorage = None
                self.diffservrandomdropweight = None

            @property
            def _common_path(self):
                if self.diffservrandomdropid is None:
                    raise YPYDataValidationError('Key property diffservrandomdropid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServRandomDropTable/DIFFSERV-MIB:diffServRandomDropEntry[DIFFSERV-MIB:diffServRandomDropId = ' + str(self.diffservrandomdropid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservrandomdropid is not None:
                    return True

                if self.diffservrandomdropmaxthreshbytes is not None:
                    return True

                if self.diffservrandomdropmaxthreshpkts is not None:
                    return True

                if self.diffservrandomdropminthreshbytes is not None:
                    return True

                if self.diffservrandomdropminthreshpkts is not None:
                    return True

                if self.diffservrandomdropprobmax is not None:
                    return True

                if self.diffservrandomdropsamplingrate is not None:
                    return True

                if self.diffservrandomdropstatus is not None:
                    return True

                if self.diffservrandomdropstorage is not None:
                    return True

                if self.diffservrandomdropweight is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServRandomDropTable.DiffServRandomDropEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServRandomDropTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservrandomdropentry is not None:
                for child_ref in self.diffservrandomdropentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServRandomDropTable']['meta_info']


    class DiffServScheduler(object):
        """
        
        
        .. attribute:: diffservmaxratenextfree
        
        	This object contains an unused value for diffServMaxRateId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservminratenextfree
        
        	This object contains an unused value for diffServMinRateId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: diffservschedulernextfree
        
        	This object contains an unused value for diffServSchedulerId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservmaxratenextfree = None
            self.diffservminratenextfree = None
            self.diffservschedulernextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServScheduler'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservmaxratenextfree is not None:
                return True

            if self.diffservminratenextfree is not None:
                return True

            if self.diffservschedulernextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServScheduler']['meta_info']


    class DiffServSchedulerTable(object):
        """
        The Scheduler Table enumerates packet schedulers. Multiple
        scheduling algorithms can be used on a given data path, with each
        algorithm described by one diffServSchedulerEntry.
        
        .. attribute:: diffservschedulerentry
        
        	An entry in the Scheduler Table describing a single instance of a scheduling algorithm
        	**type**\: list of :py:class:`DiffServSchedulerEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservschedulerentry = YList()
            self.diffservschedulerentry.parent = self
            self.diffservschedulerentry.name = 'diffservschedulerentry'


        class DiffServSchedulerEntry(object):
            """
            An entry in the Scheduler Table describing a single instance of
            a scheduling algorithm.
            
            .. attribute:: diffservschedulerid
            
            	An index that enumerates the Scheduler entries.  Managers obtain new values for row creation in this table by reading diffServSchedulerNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservschedulermaxrate
            
            	This RowPointer indicates the entry in diffServMaxRateTable which indicates the maximum output rate from this scheduler. When more than one maximum rate applies (eg, when a multi\-rate shaper is in view), it points to the first of those rate entries. This attribute is used only when there is more than one level of scheduler.  When it has the value zeroDotZero, it indicates that no maximum rate is imposed.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
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
            
            .. attribute:: diffservschedulernext
            
            	This selects the next Differentiated Services Functional Data Path Element to handle traffic for this data path. This normally is null (zeroDotZero), or points to a diffServSchedulerEntry or a diffServQEntry.  However, this RowPointer may also point to an instance of\:   diffServClfrEntry,   diffServMeterEntry,   diffServActionEntry,   diffServAlgDropEntry.  It would point another diffServSchedulerEntry when implementing multiple scheduler methods for the same data path, such as having one set of queues scheduled by WRR and that group participating in a priority scheduling system in which other queues compete with it in that way.  It might also point to a second scheduler in a hierarchical scheduling system.  If the row pointed to is zeroDotZero, no further Differentiated Services treatment is performed on traffic of this data path.  Setting this to point to a target that does not exist results in an inconsistentValue error.  If the row pointed to is removed or becomes inactive by other means, the treatment is as if this attribute contains a value of zeroDotZero
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: diffservschedulerstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservschedulerstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservschedulerid = None
                self.diffservschedulermaxrate = None
                self.diffservschedulermethod = None
                self.diffservschedulerminrate = None
                self.diffservschedulernext = None
                self.diffservschedulerstatus = None
                self.diffservschedulerstorage = None

            @property
            def _common_path(self):
                if self.diffservschedulerid is None:
                    raise YPYDataValidationError('Key property diffservschedulerid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServSchedulerTable/DIFFSERV-MIB:diffServSchedulerEntry[DIFFSERV-MIB:diffServSchedulerId = ' + str(self.diffservschedulerid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservschedulerid is not None:
                    return True

                if self.diffservschedulermaxrate is not None:
                    return True

                if self.diffservschedulermethod is not None:
                    return True

                if self.diffservschedulerminrate is not None:
                    return True

                if self.diffservschedulernext is not None:
                    return True

                if self.diffservschedulerstatus is not None:
                    return True

                if self.diffservschedulerstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServSchedulerTable.DiffServSchedulerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServSchedulerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservschedulerentry is not None:
                for child_ref in self.diffservschedulerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServSchedulerTable']['meta_info']


    class DiffServTBParam(object):
        """
        
        
        .. attribute:: diffservtbparamnextfree
        
        	This object contains an unused value for diffServTBParamId, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservtbparamnextfree = None

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServTBParam'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservtbparamnextfree is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServTBParam']['meta_info']


    class DiffServTBParamTable(object):
        """
        This table enumerates a single set of token bucket meter
        parameters that a system may use to police a stream of traffic.
        Such meters are modeled here as having a single rate and a single
        burst size. Multiple entries are used when multiple rates/burst
        sizes are needed.
        
        .. attribute:: diffservtbparamentry
        
        	An entry that describes a single set of token bucket parameters
        	**type**\: list of :py:class:`DiffServTBParamEntry <ydk.models.diffserv.DIFFSERV_MIB.DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry>`
        
        

        """

        _prefix = 'diffserv-mib'
        _revision = '2002-02-07'

        def __init__(self):
            self.parent = None
            self.diffservtbparamentry = YList()
            self.diffservtbparamentry.parent = self
            self.diffservtbparamentry.name = 'diffservtbparamentry'


        class DiffServTBParamEntry(object):
            """
            An entry that describes a single set of token bucket
            parameters.
            
            .. attribute:: diffservtbparamid
            
            	An index that enumerates the Token Bucket Parameter entries. Managers obtain new values for row creation in this table by reading diffServTBParamNextFree
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservtbparamburstsize
            
            	The maximum number of bytes in a single transmission burst. This attribute is used for\: 1. CBS and EBS in RFC 2697 for srTCM 2. CBS and PBS in RFC 2698 for trTCM 3. Burst Size in RFC 3290
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: diffservtbparaminterval
            
            	The time interval used with the token bucket.  For\: 1. Average Rate Meter, the Informal Differentiated Services Model    section 5.2.1, \- Delta. 2. Simple Token Bucket Meter, the Informal Differentiated    Services Model section 5.1, \- time interval t. 3. RFC 2859 TSWTCM, \- AVG\_INTERVAL. 4. RFC 2697 srTCM, RFC 2698 trTCM, \- token bucket update time    interval
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservtbparamrate
            
            	The token\-bucket rate, in kilobits per second (kbps). This attribute is used for\: 1. CIR in RFC 2697 for srTCM 2. CIR and PIR in RFC 2698 for trTCM 3. CTR and PTR in RFC 2859 for TSWTCM 4. AverageRate in RFC 3290
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: diffservtbparamstatus
            
            	The status of this conceptual row. All writable objects in this row may be modified at any time. Setting this variable to 'destroy' when the MIB contains one or more RowPointers pointing to it results in destruction being delayed until the row is no longer used
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: diffservtbparamstorage
            
            	The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: diffservtbparamtype
            
            	The Metering algorithm associated with the Token Bucket parameters.  zeroDotZero indicates this is unknown.  Standard values for generic algorithms\: diffServTBParamSimpleTokenBucket, diffServTBParamAvgRate, diffServTBParamSrTCMBlind, diffServTBParamSrTCMAware, diffServTBParamTrTCMBlind, diffServTBParamTrTCMAware, and diffServTBParamTswTCM are specified in this MIB as OBJECT\- IDENTITYs; additional values may be further specified in other MIBs
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'diffserv-mib'
            _revision = '2002-02-07'

            def __init__(self):
                self.parent = None
                self.diffservtbparamid = None
                self.diffservtbparamburstsize = None
                self.diffservtbparaminterval = None
                self.diffservtbparamrate = None
                self.diffservtbparamstatus = None
                self.diffservtbparamstorage = None
                self.diffservtbparamtype = None

            @property
            def _common_path(self):
                if self.diffservtbparamid is None:
                    raise YPYDataValidationError('Key property diffservtbparamid is None')

                return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServTBParamTable/DIFFSERV-MIB:diffServTBParamEntry[DIFFSERV-MIB:diffServTBParamId = ' + str(self.diffservtbparamid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.diffservtbparamid is not None:
                    return True

                if self.diffservtbparamburstsize is not None:
                    return True

                if self.diffservtbparaminterval is not None:
                    return True

                if self.diffservtbparamrate is not None:
                    return True

                if self.diffservtbparamstatus is not None:
                    return True

                if self.diffservtbparamstorage is not None:
                    return True

                if self.diffservtbparamtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
                return meta._meta_table['DIFFSERVMIB.DiffServTBParamTable.DiffServTBParamEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIFFSERV-MIB:DIFFSERV-MIB/DIFFSERV-MIB:diffServTBParamTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.diffservtbparamentry is not None:
                for child_ref in self.diffservtbparamentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
            return meta._meta_table['DIFFSERVMIB.DiffServTBParamTable']['meta_info']

    @property
    def _common_path(self):

        return '/DIFFSERV-MIB:DIFFSERV-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.diffservaction is not None and self.diffservaction._has_data():
            return True

        if self.diffservaction is not None and self.diffservaction.is_presence():
            return True

        if self.diffservactiontable is not None and self.diffservactiontable._has_data():
            return True

        if self.diffservactiontable is not None and self.diffservactiontable.is_presence():
            return True

        if self.diffservalgdrop is not None and self.diffservalgdrop._has_data():
            return True

        if self.diffservalgdrop is not None and self.diffservalgdrop.is_presence():
            return True

        if self.diffservalgdroptable is not None and self.diffservalgdroptable._has_data():
            return True

        if self.diffservalgdroptable is not None and self.diffservalgdroptable.is_presence():
            return True

        if self.diffservclassifier is not None and self.diffservclassifier._has_data():
            return True

        if self.diffservclassifier is not None and self.diffservclassifier.is_presence():
            return True

        if self.diffservclfrelementtable is not None and self.diffservclfrelementtable._has_data():
            return True

        if self.diffservclfrelementtable is not None and self.diffservclfrelementtable.is_presence():
            return True

        if self.diffservclfrtable is not None and self.diffservclfrtable._has_data():
            return True

        if self.diffservclfrtable is not None and self.diffservclfrtable.is_presence():
            return True

        if self.diffservcountacttable is not None and self.diffservcountacttable._has_data():
            return True

        if self.diffservcountacttable is not None and self.diffservcountacttable.is_presence():
            return True

        if self.diffservdatapathtable is not None and self.diffservdatapathtable._has_data():
            return True

        if self.diffservdatapathtable is not None and self.diffservdatapathtable.is_presence():
            return True

        if self.diffservdscpmarkacttable is not None and self.diffservdscpmarkacttable._has_data():
            return True

        if self.diffservdscpmarkacttable is not None and self.diffservdscpmarkacttable.is_presence():
            return True

        if self.diffservmaxratetable is not None and self.diffservmaxratetable._has_data():
            return True

        if self.diffservmaxratetable is not None and self.diffservmaxratetable.is_presence():
            return True

        if self.diffservmeter is not None and self.diffservmeter._has_data():
            return True

        if self.diffservmeter is not None and self.diffservmeter.is_presence():
            return True

        if self.diffservmetertable is not None and self.diffservmetertable._has_data():
            return True

        if self.diffservmetertable is not None and self.diffservmetertable.is_presence():
            return True

        if self.diffservminratetable is not None and self.diffservminratetable._has_data():
            return True

        if self.diffservminratetable is not None and self.diffservminratetable.is_presence():
            return True

        if self.diffservmultifieldclfrtable is not None and self.diffservmultifieldclfrtable._has_data():
            return True

        if self.diffservmultifieldclfrtable is not None and self.diffservmultifieldclfrtable.is_presence():
            return True

        if self.diffservqtable is not None and self.diffservqtable._has_data():
            return True

        if self.diffservqtable is not None and self.diffservqtable.is_presence():
            return True

        if self.diffservqueue is not None and self.diffservqueue._has_data():
            return True

        if self.diffservqueue is not None and self.diffservqueue.is_presence():
            return True

        if self.diffservrandomdroptable is not None and self.diffservrandomdroptable._has_data():
            return True

        if self.diffservrandomdroptable is not None and self.diffservrandomdroptable.is_presence():
            return True

        if self.diffservscheduler is not None and self.diffservscheduler._has_data():
            return True

        if self.diffservscheduler is not None and self.diffservscheduler.is_presence():
            return True

        if self.diffservschedulertable is not None and self.diffservschedulertable._has_data():
            return True

        if self.diffservschedulertable is not None and self.diffservschedulertable.is_presence():
            return True

        if self.diffservtbparam is not None and self.diffservtbparam._has_data():
            return True

        if self.diffservtbparam is not None and self.diffservtbparam.is_presence():
            return True

        if self.diffservtbparamtable is not None and self.diffservtbparamtable._has_data():
            return True

        if self.diffservtbparamtable is not None and self.diffservtbparamtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DIFFSERVMIB']['meta_info']


class DiffServSchedulerPriority_Identity(ObjectIdentity_Identity):
    """
    For use with diffServSchedulerMethod to indicate the Priority
    scheduling method.  This is defined as an algorithm in which the
    presence of data in a queue or set of queues absolutely precludes
    dequeue from another queue or set of queues of lower priority.
    Note that attributes from diffServMinRateEntry of the
    queues/schedulers feeding this scheduler are used when
    determining the next packet to schedule.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServSchedulerPriority_Identity']['meta_info']


class DiffServSchedulerWFQ_Identity(ObjectIdentity_Identity):
    """
    For use with diffServSchedulerMethod to indicate the Weighted
    Fair Queuing scheduling method, defined as any algorithm in which
    a set of queues are conceptually visited in some order, to
    implement an average output rate by class. Notice attributes from
    diffServMinRateEntry of the queues/schedulers feeding this
    scheduler are used when determining the next packet to schedule.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServSchedulerWFQ_Identity']['meta_info']


class DiffServSchedulerWRR_Identity(ObjectIdentity_Identity):
    """
    For use with diffServSchedulerMethod to indicate the Weighted
    Round Robin scheduling method, defined as any algorithm in which
    a set of queues are visited in a fixed order, and varying amounts
    of traffic are removed from each queue in turn to implement an
    average output rate by class. Notice attributes from
    diffServMinRateEntry of the queues/schedulers feeding this
    scheduler are used when determining the next packet to schedule.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServSchedulerWRR_Identity']['meta_info']


class DiffServTBParamAvgRate_Identity(ObjectIdentity_Identity):
    """
    Average Rate Meter as described in the Informal Differentiated
    Services Model section 5.2.1.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamAvgRate_Identity']['meta_info']


class DiffServTBParamSimpleTokenBucket_Identity(ObjectIdentity_Identity):
    """
    Two Parameter Token Bucket Meter as described in the Informal
    Differentiated Services Model section 5.2.3.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamSimpleTokenBucket_Identity']['meta_info']


class DiffServTBParamSrTCMAware_Identity(ObjectIdentity_Identity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamSrTCMAware_Identity']['meta_info']


class DiffServTBParamSrTCMBlind_Identity(ObjectIdentity_Identity):
    """
    Single Rate Three Color Marker Metering as defined by RFC 2697,
    in the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamSrTCMBlind_Identity']['meta_info']


class DiffServTBParamTrTCMAware_Identity(ObjectIdentity_Identity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Aware' mode as described by the RFC.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamTrTCMAware_Identity']['meta_info']


class DiffServTBParamTrTCMBlind_Identity(ObjectIdentity_Identity):
    """
    Two Rate Three Color Marker Metering as defined by RFC 2698, in
    the `Color Blind' mode as described by the RFC.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamTrTCMBlind_Identity']['meta_info']


class DiffServTBParamTswTCM_Identity(ObjectIdentity_Identity):
    """
    Time Sliding Window Three Color Marker Metering as defined by
    RFC 2859.
    
    

    """

    _prefix = 'diffserv-mib'
    _revision = '2002-02-07'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.diffserv._meta import _DIFFSERV_MIB as meta
        return meta._meta_table['DiffServTBParamTswTCM_Identity']['meta_info']


