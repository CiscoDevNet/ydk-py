""" RMON_MIB 

Remote network monitoring devices, often called
monitors or probes, are instruments that exist for
the purpose of managing a network. This MIB defines
objects for managing remote network monitoring devices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity


class EntryStatus(Enum):
    """
    EntryStatus (Enum Class)

    The status of a table entry.

    Setting this object to the value invalid(4) has the

    effect of invalidating the corresponding entry.

    That is, it effectively disassociates the mapping

    identified with said entry.

    It is an implementation\-specific matter as to whether

    the agent removes an invalidated entry from the table.

    Accordingly, management stations must be prepared to

    receive tabular information from agents that corresponds

    to entries currently not in use.  Proper

    interpretation of such entries requires examination

    of the relevant EntryStatus object.

    An existing instance of this object cannot be set to

    createRequest(2).  This object may only be set to

    createRequest(2) when this instance is created.  When

    this object is created, the agent may wish to create

    supplemental object instances with default values

    to complete a conceptual row in this table.  Because the

    creation of these default objects is entirely at the option

    of the agent, the manager must not assume that any will be

    created, but may make use of any that are created.

    Immediately after completing the create operation, the agent

    must set this object to underCreation(3).

    When in the underCreation(3) state, an entry is allowed to

    exist in a possibly incomplete, possibly inconsistent state,

    usually to allow it to be modified in multiple PDUs.  When in

    this state, an entry is not fully active.

    Entries shall exist in the underCreation(3) state until

    the management station is finished configuring the entry

    and sets this object to valid(1) or aborts, setting this

    object to invalid(4).  If the agent determines that an

    entry has been in the underCreation(3) state for an

    abnormally long time, it may decide that the management

    station has crashed.  If the agent makes this decision,

    it may set this object to invalid(4) to reclaim the

    entry.  A prudent agent will understand that the

    management station may need to wait for human input

    and will allow for that possibility in its

    determination of this abnormally long period.

    An entry in the valid(1) state is fully configured and

    consistent and fully represents the configuration or

    operation such a row is intended to represent.  For

    example, it could be a statistical function that is

    configured and active, or a filter that is available

    in the list of filters processed by the packet capture

    process.

    A manager is restricted to changing the state of an entry in

    the following ways\:

         To\:       valid  createRequest  underCreation  invalid

    From\:

    valid             OK             NO             OK       OK

    createRequest    N/A            N/A            N/A      N/A

    underCreation     OK             NO             OK       OK

    invalid           NO             NO             NO       OK

    nonExistent       NO             OK             NO       OK

    In the table above, it is not applicable to move the state

    from the createRequest state to any other state because the

    manager will never find the variable in that state.  The

    nonExistent state is not a value of the enumeration, rather

    it means that the entryStatus variable does not exist at all.

    An agent may allow an entryStatus variable to change state in

    additional ways, so long as the semantics of the states are

    followed.  This allowance is made to ease the implementation of

    the agent and is made despite the fact that managers should

    never exercise these additional state transitions.

    .. data:: valid = 1

    .. data:: createRequest = 2

    .. data:: underCreation = 3

    .. data:: invalid = 4

    """

    valid = Enum.YLeaf(1, "valid")

    createRequest = Enum.YLeaf(2, "createRequest")

    underCreation = Enum.YLeaf(3, "underCreation")

    invalid = Enum.YLeaf(4, "invalid")



class RmonEventsV2(ObjectIdentity):
    """
    Definition point for RMON notifications.
    
    

    """

    _prefix = 'RMON-MIB'
    _revision = '2000-05-11'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:RMON-MIB", pref="RMON-MIB", tag="RMON-MIB:rmonEventsV2"):
        super(RmonEventsV2, self).__init__(ns, pref, tag)



class RMONMIB(Entity):
    """
    
    
    .. attribute:: etherstatstable
    
    	A list of Ethernet statistics entries
    	**type**\:  :py:class:`EtherStatsTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EtherStatsTable>`
    
    	**config**\: False
    
    .. attribute:: historycontroltable
    
    	A list of history control entries
    	**type**\:  :py:class:`HistoryControlTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HistoryControlTable>`
    
    	**config**\: False
    
    .. attribute:: etherhistorytable
    
    	A list of Ethernet history entries
    	**type**\:  :py:class:`EtherHistoryTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EtherHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: alarmtable
    
    	A list of alarm entries
    	**type**\:  :py:class:`AlarmTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.AlarmTable>`
    
    	**config**\: False
    
    .. attribute:: hostcontroltable
    
    	A list of host table control entries
    	**type**\:  :py:class:`HostControlTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostControlTable>`
    
    	**config**\: False
    
    .. attribute:: hosttable
    
    	A list of host entries
    	**type**\:  :py:class:`HostTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTable>`
    
    	**config**\: False
    
    .. attribute:: hosttimetable
    
    	A list of time\-ordered host table entries
    	**type**\:  :py:class:`HostTimeTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTimeTable>`
    
    	**config**\: False
    
    .. attribute:: hosttopncontroltable
    
    	A list of top N host control entries
    	**type**\:  :py:class:`HostTopNControlTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTopNControlTable>`
    
    	**config**\: False
    
    .. attribute:: hosttopntable
    
    	A list of top N host entries
    	**type**\:  :py:class:`HostTopNTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTopNTable>`
    
    	**config**\: False
    
    .. attribute:: matrixcontroltable
    
    	A list of information entries for the traffic matrix on each interface
    	**type**\:  :py:class:`MatrixControlTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixControlTable>`
    
    	**config**\: False
    
    .. attribute:: matrixsdtable
    
    	A list of traffic matrix entries indexed by source and destination MAC address
    	**type**\:  :py:class:`MatrixSDTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixSDTable>`
    
    	**config**\: False
    
    .. attribute:: matrixdstable
    
    	A list of traffic matrix entries indexed by destination and source MAC address
    	**type**\:  :py:class:`MatrixDSTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixDSTable>`
    
    	**config**\: False
    
    .. attribute:: filtertable
    
    	A list of packet filter entries
    	**type**\:  :py:class:`FilterTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.FilterTable>`
    
    	**config**\: False
    
    .. attribute:: channeltable
    
    	A list of packet channel entries
    	**type**\:  :py:class:`ChannelTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.ChannelTable>`
    
    	**config**\: False
    
    .. attribute:: buffercontroltable
    
    	A list of buffers control entries
    	**type**\:  :py:class:`BufferControlTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.BufferControlTable>`
    
    	**config**\: False
    
    .. attribute:: capturebuffertable
    
    	A list of packets captured off of a channel
    	**type**\:  :py:class:`CaptureBufferTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.CaptureBufferTable>`
    
    	**config**\: False
    
    .. attribute:: eventtable
    
    	A list of events to be generated
    	**type**\:  :py:class:`EventTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EventTable>`
    
    	**config**\: False
    
    .. attribute:: logtable
    
    	A list of events that have been logged
    	**type**\:  :py:class:`LogTable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.LogTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'RMON-MIB'
    _revision = '2000-05-11'

    def __init__(self):
        super(RMONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "RMON-MIB"
        self.yang_parent_name = "RMON-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("etherStatsTable", ("etherstatstable", RMONMIB.EtherStatsTable)), ("historyControlTable", ("historycontroltable", RMONMIB.HistoryControlTable)), ("etherHistoryTable", ("etherhistorytable", RMONMIB.EtherHistoryTable)), ("alarmTable", ("alarmtable", RMONMIB.AlarmTable)), ("hostControlTable", ("hostcontroltable", RMONMIB.HostControlTable)), ("hostTable", ("hosttable", RMONMIB.HostTable)), ("hostTimeTable", ("hosttimetable", RMONMIB.HostTimeTable)), ("hostTopNControlTable", ("hosttopncontroltable", RMONMIB.HostTopNControlTable)), ("hostTopNTable", ("hosttopntable", RMONMIB.HostTopNTable)), ("matrixControlTable", ("matrixcontroltable", RMONMIB.MatrixControlTable)), ("matrixSDTable", ("matrixsdtable", RMONMIB.MatrixSDTable)), ("matrixDSTable", ("matrixdstable", RMONMIB.MatrixDSTable)), ("filterTable", ("filtertable", RMONMIB.FilterTable)), ("channelTable", ("channeltable", RMONMIB.ChannelTable)), ("bufferControlTable", ("buffercontroltable", RMONMIB.BufferControlTable)), ("captureBufferTable", ("capturebuffertable", RMONMIB.CaptureBufferTable)), ("eventTable", ("eventtable", RMONMIB.EventTable)), ("logTable", ("logtable", RMONMIB.LogTable))])
        self._leafs = OrderedDict()

        self.etherstatstable = RMONMIB.EtherStatsTable()
        self.etherstatstable.parent = self
        self._children_name_map["etherstatstable"] = "etherStatsTable"

        self.historycontroltable = RMONMIB.HistoryControlTable()
        self.historycontroltable.parent = self
        self._children_name_map["historycontroltable"] = "historyControlTable"

        self.etherhistorytable = RMONMIB.EtherHistoryTable()
        self.etherhistorytable.parent = self
        self._children_name_map["etherhistorytable"] = "etherHistoryTable"

        self.alarmtable = RMONMIB.AlarmTable()
        self.alarmtable.parent = self
        self._children_name_map["alarmtable"] = "alarmTable"

        self.hostcontroltable = RMONMIB.HostControlTable()
        self.hostcontroltable.parent = self
        self._children_name_map["hostcontroltable"] = "hostControlTable"

        self.hosttable = RMONMIB.HostTable()
        self.hosttable.parent = self
        self._children_name_map["hosttable"] = "hostTable"

        self.hosttimetable = RMONMIB.HostTimeTable()
        self.hosttimetable.parent = self
        self._children_name_map["hosttimetable"] = "hostTimeTable"

        self.hosttopncontroltable = RMONMIB.HostTopNControlTable()
        self.hosttopncontroltable.parent = self
        self._children_name_map["hosttopncontroltable"] = "hostTopNControlTable"

        self.hosttopntable = RMONMIB.HostTopNTable()
        self.hosttopntable.parent = self
        self._children_name_map["hosttopntable"] = "hostTopNTable"

        self.matrixcontroltable = RMONMIB.MatrixControlTable()
        self.matrixcontroltable.parent = self
        self._children_name_map["matrixcontroltable"] = "matrixControlTable"

        self.matrixsdtable = RMONMIB.MatrixSDTable()
        self.matrixsdtable.parent = self
        self._children_name_map["matrixsdtable"] = "matrixSDTable"

        self.matrixdstable = RMONMIB.MatrixDSTable()
        self.matrixdstable.parent = self
        self._children_name_map["matrixdstable"] = "matrixDSTable"

        self.filtertable = RMONMIB.FilterTable()
        self.filtertable.parent = self
        self._children_name_map["filtertable"] = "filterTable"

        self.channeltable = RMONMIB.ChannelTable()
        self.channeltable.parent = self
        self._children_name_map["channeltable"] = "channelTable"

        self.buffercontroltable = RMONMIB.BufferControlTable()
        self.buffercontroltable.parent = self
        self._children_name_map["buffercontroltable"] = "bufferControlTable"

        self.capturebuffertable = RMONMIB.CaptureBufferTable()
        self.capturebuffertable.parent = self
        self._children_name_map["capturebuffertable"] = "captureBufferTable"

        self.eventtable = RMONMIB.EventTable()
        self.eventtable.parent = self
        self._children_name_map["eventtable"] = "eventTable"

        self.logtable = RMONMIB.LogTable()
        self.logtable.parent = self
        self._children_name_map["logtable"] = "logTable"
        self._segment_path = lambda: "RMON-MIB:RMON-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RMONMIB, [], name, value)


    class EtherStatsTable(Entity):
        """
        A list of Ethernet statistics entries.
        
        .. attribute:: etherstatsentry
        
        	A collection of statistics kept for a particular Ethernet interface.  As an example, an instance of the etherStatsPkts object might be named etherStatsPkts.1
        	**type**\: list of  		 :py:class:`EtherStatsEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EtherStatsTable.EtherStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.EtherStatsTable, self).__init__()

            self.yang_name = "etherStatsTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherStatsEntry", ("etherstatsentry", RMONMIB.EtherStatsTable.EtherStatsEntry))])
            self._leafs = OrderedDict()

            self.etherstatsentry = YList(self)
            self._segment_path = lambda: "etherStatsTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.EtherStatsTable, [], name, value)


        class EtherStatsEntry(Entity):
            """
            A collection of statistics kept for a particular
            Ethernet interface.  As an example, an instance of the
            etherStatsPkts object might be named etherStatsPkts.1
            
            .. attribute:: etherstatsindex  (key)
            
            	The value of this object uniquely identifies this etherStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: etherstatsdatasource
            
            	This object identifies the source of the data that this etherStats entry is configured to analyze.  This source can be any ethernet interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated etherStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: etherstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: etherstatsoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets). This object can be used as a reasonable estimate of 10\-Megabit ethernet utilization.  If greater precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval.  The differences in the sampled values are Pkts and Octets, respectively, and the number of seconds in the interval is Interval.  These values are used to calculate the Utilization as follows\:                   Pkts \* (9.6 + 6.4) + (Octets \* .8)  Utilization = \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-                          Interval \* 10,000  The result of this equation is the value Utilization which is the percent utilization of the ethernet segment on a scale of 0 to 100 percent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: etherstatspkts
            
            	The total number of packets (including bad packets, broadcast packets, and multicast packets) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsbroadcastpkts
            
            	The total number of good packets received that were directed to the broadcast address.  Note that this does not include multicast packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsmulticastpkts
            
            	The total number of good packets received that were directed to a multicast address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatscrcalignerrors
            
            	The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsundersizepkts
            
            	The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsoversizepkts
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsfragments
            
            	The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherStatsFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsjabbers
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatscollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Collisions
            
            .. attribute:: etherstatspkts64octets
            
            	The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts65to127octets
            
            	The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts128to255octets
            
            	The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts256to511octets
            
            	The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts512to1023octets
            
            	The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts1024to1518octets
            
            	The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: etherstatsstatus
            
            	The status of this etherStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: etherstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: etherstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.EtherStatsTable.EtherStatsEntry, self).__init__()

                self.yang_name = "etherStatsEntry"
                self.yang_parent_name = "etherStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['etherstatsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('etherstatsindex', (YLeaf(YType.int32, 'etherStatsIndex'), ['int'])),
                    ('etherstatsdatasource', (YLeaf(YType.str, 'etherStatsDataSource'), ['str'])),
                    ('etherstatsdropevents', (YLeaf(YType.uint32, 'etherStatsDropEvents'), ['int'])),
                    ('etherstatsoctets', (YLeaf(YType.uint32, 'etherStatsOctets'), ['int'])),
                    ('etherstatspkts', (YLeaf(YType.uint32, 'etherStatsPkts'), ['int'])),
                    ('etherstatsbroadcastpkts', (YLeaf(YType.uint32, 'etherStatsBroadcastPkts'), ['int'])),
                    ('etherstatsmulticastpkts', (YLeaf(YType.uint32, 'etherStatsMulticastPkts'), ['int'])),
                    ('etherstatscrcalignerrors', (YLeaf(YType.uint32, 'etherStatsCRCAlignErrors'), ['int'])),
                    ('etherstatsundersizepkts', (YLeaf(YType.uint32, 'etherStatsUndersizePkts'), ['int'])),
                    ('etherstatsoversizepkts', (YLeaf(YType.uint32, 'etherStatsOversizePkts'), ['int'])),
                    ('etherstatsfragments', (YLeaf(YType.uint32, 'etherStatsFragments'), ['int'])),
                    ('etherstatsjabbers', (YLeaf(YType.uint32, 'etherStatsJabbers'), ['int'])),
                    ('etherstatscollisions', (YLeaf(YType.uint32, 'etherStatsCollisions'), ['int'])),
                    ('etherstatspkts64octets', (YLeaf(YType.uint32, 'etherStatsPkts64Octets'), ['int'])),
                    ('etherstatspkts65to127octets', (YLeaf(YType.uint32, 'etherStatsPkts65to127Octets'), ['int'])),
                    ('etherstatspkts128to255octets', (YLeaf(YType.uint32, 'etherStatsPkts128to255Octets'), ['int'])),
                    ('etherstatspkts256to511octets', (YLeaf(YType.uint32, 'etherStatsPkts256to511Octets'), ['int'])),
                    ('etherstatspkts512to1023octets', (YLeaf(YType.uint32, 'etherStatsPkts512to1023Octets'), ['int'])),
                    ('etherstatspkts1024to1518octets', (YLeaf(YType.uint32, 'etherStatsPkts1024to1518Octets'), ['int'])),
                    ('etherstatsowner', (YLeaf(YType.str, 'etherStatsOwner'), ['str'])),
                    ('etherstatsstatus', (YLeaf(YType.enumeration, 'etherStatsStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('etherstatsdroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:etherStatsDroppedFrames'), ['int'])),
                    ('etherstatscreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:etherStatsCreateTime'), ['int'])),
                ])
                self.etherstatsindex = None
                self.etherstatsdatasource = None
                self.etherstatsdropevents = None
                self.etherstatsoctets = None
                self.etherstatspkts = None
                self.etherstatsbroadcastpkts = None
                self.etherstatsmulticastpkts = None
                self.etherstatscrcalignerrors = None
                self.etherstatsundersizepkts = None
                self.etherstatsoversizepkts = None
                self.etherstatsfragments = None
                self.etherstatsjabbers = None
                self.etherstatscollisions = None
                self.etherstatspkts64octets = None
                self.etherstatspkts65to127octets = None
                self.etherstatspkts128to255octets = None
                self.etherstatspkts256to511octets = None
                self.etherstatspkts512to1023octets = None
                self.etherstatspkts1024to1518octets = None
                self.etherstatsowner = None
                self.etherstatsstatus = None
                self.etherstatsdroppedframes = None
                self.etherstatscreatetime = None
                self._segment_path = lambda: "etherStatsEntry" + "[etherStatsIndex='" + str(self.etherstatsindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/etherStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.EtherStatsTable.EtherStatsEntry, [u'etherstatsindex', u'etherstatsdatasource', u'etherstatsdropevents', u'etherstatsoctets', u'etherstatspkts', u'etherstatsbroadcastpkts', u'etherstatsmulticastpkts', u'etherstatscrcalignerrors', u'etherstatsundersizepkts', u'etherstatsoversizepkts', u'etherstatsfragments', u'etherstatsjabbers', u'etherstatscollisions', u'etherstatspkts64octets', u'etherstatspkts65to127octets', u'etherstatspkts128to255octets', u'etherstatspkts256to511octets', u'etherstatspkts512to1023octets', u'etherstatspkts1024to1518octets', u'etherstatsowner', u'etherstatsstatus', 'etherstatsdroppedframes', 'etherstatscreatetime'], name, value)




    class HistoryControlTable(Entity):
        """
        A list of history control entries.
        
        .. attribute:: historycontrolentry
        
        	A list of parameters that set up a periodic sampling of statistics.  As an example, an instance of the historyControlInterval object might be named historyControlInterval.2
        	**type**\: list of  		 :py:class:`HistoryControlEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HistoryControlTable.HistoryControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HistoryControlTable, self).__init__()

            self.yang_name = "historyControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("historyControlEntry", ("historycontrolentry", RMONMIB.HistoryControlTable.HistoryControlEntry))])
            self._leafs = OrderedDict()

            self.historycontrolentry = YList(self)
            self._segment_path = lambda: "historyControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HistoryControlTable, [], name, value)


        class HistoryControlEntry(Entity):
            """
            A list of parameters that set up a periodic sampling of
            statistics.  As an example, an instance of the
            historyControlInterval object might be named
            historyControlInterval.2
            
            .. attribute:: historycontrolindex  (key)
            
            	An index that uniquely identifies an entry in the historyControl table.  Each such entry defines a set of samples at a particular interval for an interface on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: historycontroldatasource
            
            	This object identifies the source of the data for which historical data was collected and placed in a media\-specific table on behalf of this historyControlEntry.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in  RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: historycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the media\-specific table associated with this historyControlEntry.  When this object is created or modified, the probe should set historyControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: historycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the media\-specific table associated with this historyControlEntry. When the associated historyControlBucketsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated historyControlBucketsRequested object.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the media\-specific table.  When the number of buckets reaches the value of this object and a new bucket is to be added to the media\-specific table, the oldest bucket associated with this historyControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the media\-specific table associated with this historyControlEntry.  Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated media\- specific entries may be allowed to grow
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: historycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the media\-specific table associated with this historyControlEntry.  This interval can be set to any number of seconds between 1 and 3600 (1 hour).  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of the associated counters.  It is important to consider the minimum time in which any counter could overflow on a particular media type and set the historyControlInterval object to a value less than this interval.  This is typically most important for the 'octets' counter in any media\-specific table.  For example, on an Ethernet network, the etherHistoryOctets counter could overflow in about one hour at the Ethernet's maximum utilization.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..3600
            
            	**config**\: False
            
            	**units**\: Seconds
            
            .. attribute:: historycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: historycontrolstatus
            
            	The status of this historyControl entry.  Each instance of the media\-specific table associated with this historyControlEntry will be deleted by the agent if this historyControlEntry is not equal to valid(1)
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: historycontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this      collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HistoryControlTable.HistoryControlEntry, self).__init__()

                self.yang_name = "historyControlEntry"
                self.yang_parent_name = "historyControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['historycontrolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('historycontrolindex', (YLeaf(YType.int32, 'historyControlIndex'), ['int'])),
                    ('historycontroldatasource', (YLeaf(YType.str, 'historyControlDataSource'), ['str'])),
                    ('historycontrolbucketsrequested', (YLeaf(YType.int32, 'historyControlBucketsRequested'), ['int'])),
                    ('historycontrolbucketsgranted', (YLeaf(YType.int32, 'historyControlBucketsGranted'), ['int'])),
                    ('historycontrolinterval', (YLeaf(YType.int32, 'historyControlInterval'), ['int'])),
                    ('historycontrolowner', (YLeaf(YType.str, 'historyControlOwner'), ['str'])),
                    ('historycontrolstatus', (YLeaf(YType.enumeration, 'historyControlStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('historycontroldroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:historyControlDroppedFrames'), ['int'])),
                ])
                self.historycontrolindex = None
                self.historycontroldatasource = None
                self.historycontrolbucketsrequested = None
                self.historycontrolbucketsgranted = None
                self.historycontrolinterval = None
                self.historycontrolowner = None
                self.historycontrolstatus = None
                self.historycontroldroppedframes = None
                self._segment_path = lambda: "historyControlEntry" + "[historyControlIndex='" + str(self.historycontrolindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/historyControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HistoryControlTable.HistoryControlEntry, [u'historycontrolindex', u'historycontroldatasource', u'historycontrolbucketsrequested', u'historycontrolbucketsgranted', u'historycontrolinterval', u'historycontrolowner', u'historycontrolstatus', 'historycontroldroppedframes'], name, value)




    class EtherHistoryTable(Entity):
        """
        A list of Ethernet history entries.
        
        .. attribute:: etherhistoryentry
        
        	An historical sample of Ethernet statistics on a particular Ethernet interface.  This sample is associated with the historyControlEntry which set up the parameters for a regular collection of these samples.  As an example, an instance of the etherHistoryPkts object might be named etherHistoryPkts.2.89
        	**type**\: list of  		 :py:class:`EtherHistoryEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EtherHistoryTable.EtherHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.EtherHistoryTable, self).__init__()

            self.yang_name = "etherHistoryTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherHistoryEntry", ("etherhistoryentry", RMONMIB.EtherHistoryTable.EtherHistoryEntry))])
            self._leafs = OrderedDict()

            self.etherhistoryentry = YList(self)
            self._segment_path = lambda: "etherHistoryTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.EtherHistoryTable, [], name, value)


        class EtherHistoryEntry(Entity):
            """
            An historical sample of Ethernet statistics on a particular
            Ethernet interface.  This sample is associated with the
            historyControlEntry which set up the parameters for
            a regular collection of these samples.  As an example, an
            instance of the etherHistoryPkts object might be named
            etherHistoryPkts.2.89
            
            .. attribute:: etherhistoryindex  (key)
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: etherhistorysampleindex  (key)
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: etherhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: etherhistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: etherhistoryoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: etherhistorypkts
            
            	The number of packets (including bad packets) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistorybroadcastpkts
            
            	The number of good packets received during this sampling interval that were directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistorymulticastpkts
            
            	The number of good packets received during this sampling interval that were directed to a multicast address.  Note that this number does not include packets addressed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistorycrcalignerrors
            
            	The number of packets received during this sampling interval that had a length (excluding framing bits but including FCS octets) between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryundersizepkts
            
            	The number of packets received during this sampling interval that were less than 64 octets long (excluding framing bits but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryoversizepkts
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets) but were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryfragments
            
            	The total number of packets received during this sampling interval that were less than 64 octets in length (excluding framing bits but including FCS octets) had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherHistoryFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryjabbers
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets), and  had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: etherhistorycollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment during this sampling interval.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Collisions
            
            .. attribute:: etherhistoryutilization
            
            	The best estimate of the mean physical layer network utilization on this interface during this sampling interval, in hundredths of a percent
            	**type**\: int
            
            	**range:** 0..10000
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.EtherHistoryTable.EtherHistoryEntry, self).__init__()

                self.yang_name = "etherHistoryEntry"
                self.yang_parent_name = "etherHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['etherhistoryindex','etherhistorysampleindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('etherhistoryindex', (YLeaf(YType.int32, 'etherHistoryIndex'), ['int'])),
                    ('etherhistorysampleindex', (YLeaf(YType.int32, 'etherHistorySampleIndex'), ['int'])),
                    ('etherhistoryintervalstart', (YLeaf(YType.uint32, 'etherHistoryIntervalStart'), ['int'])),
                    ('etherhistorydropevents', (YLeaf(YType.uint32, 'etherHistoryDropEvents'), ['int'])),
                    ('etherhistoryoctets', (YLeaf(YType.uint32, 'etherHistoryOctets'), ['int'])),
                    ('etherhistorypkts', (YLeaf(YType.uint32, 'etherHistoryPkts'), ['int'])),
                    ('etherhistorybroadcastpkts', (YLeaf(YType.uint32, 'etherHistoryBroadcastPkts'), ['int'])),
                    ('etherhistorymulticastpkts', (YLeaf(YType.uint32, 'etherHistoryMulticastPkts'), ['int'])),
                    ('etherhistorycrcalignerrors', (YLeaf(YType.uint32, 'etherHistoryCRCAlignErrors'), ['int'])),
                    ('etherhistoryundersizepkts', (YLeaf(YType.uint32, 'etherHistoryUndersizePkts'), ['int'])),
                    ('etherhistoryoversizepkts', (YLeaf(YType.uint32, 'etherHistoryOversizePkts'), ['int'])),
                    ('etherhistoryfragments', (YLeaf(YType.uint32, 'etherHistoryFragments'), ['int'])),
                    ('etherhistoryjabbers', (YLeaf(YType.uint32, 'etherHistoryJabbers'), ['int'])),
                    ('etherhistorycollisions', (YLeaf(YType.uint32, 'etherHistoryCollisions'), ['int'])),
                    ('etherhistoryutilization', (YLeaf(YType.int32, 'etherHistoryUtilization'), ['int'])),
                ])
                self.etherhistoryindex = None
                self.etherhistorysampleindex = None
                self.etherhistoryintervalstart = None
                self.etherhistorydropevents = None
                self.etherhistoryoctets = None
                self.etherhistorypkts = None
                self.etherhistorybroadcastpkts = None
                self.etherhistorymulticastpkts = None
                self.etherhistorycrcalignerrors = None
                self.etherhistoryundersizepkts = None
                self.etherhistoryoversizepkts = None
                self.etherhistoryfragments = None
                self.etherhistoryjabbers = None
                self.etherhistorycollisions = None
                self.etherhistoryutilization = None
                self._segment_path = lambda: "etherHistoryEntry" + "[etherHistoryIndex='" + str(self.etherhistoryindex) + "']" + "[etherHistorySampleIndex='" + str(self.etherhistorysampleindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/etherHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.EtherHistoryTable.EtherHistoryEntry, [u'etherhistoryindex', u'etherhistorysampleindex', u'etherhistoryintervalstart', u'etherhistorydropevents', u'etherhistoryoctets', u'etherhistorypkts', u'etherhistorybroadcastpkts', u'etherhistorymulticastpkts', u'etherhistorycrcalignerrors', u'etherhistoryundersizepkts', u'etherhistoryoversizepkts', u'etherhistoryfragments', u'etherhistoryjabbers', u'etherhistorycollisions', u'etherhistoryutilization'], name, value)




    class AlarmTable(Entity):
        """
        A list of alarm entries.
        
        .. attribute:: alarmentry
        
        	A list of parameters that set up a periodic checking for alarm conditions.  For example, an instance of the alarmValue object might be named alarmValue.8
        	**type**\: list of  		 :py:class:`AlarmEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.AlarmTable.AlarmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.AlarmTable, self).__init__()

            self.yang_name = "alarmTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alarmEntry", ("alarmentry", RMONMIB.AlarmTable.AlarmEntry))])
            self._leafs = OrderedDict()

            self.alarmentry = YList(self)
            self._segment_path = lambda: "alarmTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.AlarmTable, [], name, value)


        class AlarmEntry(Entity):
            """
            A list of parameters that set up a periodic checking
            for alarm conditions.  For example, an instance of the
            alarmValue object might be named alarmValue.8
            
            .. attribute:: alarmindex  (key)
            
            	An index that uniquely identifies an entry in the alarm table.  Each such entry defines a diagnostic sample at a particular interval for an object on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: alarminterval
            
            	The interval in seconds over which the data is sampled and compared with the rising and falling thresholds.  When setting this variable, care should be taken in the case of deltaValue sampling \- the interval should be set short enough that the sampled variable is very unlikely to increase or decrease by more than 2^31 \- 1 during a single sampling interval.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Seconds
            
            .. attribute:: alarmvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view.  Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  If at any time the variable name of an established alarmEntry is no longer available in the selected MIB view, the probe must change the status of this alarmEntry to invalid(4).  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: alarmsampletype
            
            	The method of sampling the selected variable and calculating the value to be compared against the thresholds.  If the value of this object is absoluteValue(1), the value of the selected variable will be compared directly with the thresholds at the end of the sampling interval.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference compared with the thresholds.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  :py:class:`AlarmSampleType <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.AlarmTable.AlarmEntry.AlarmSampleType>`
            
            	**config**\: False
            
            .. attribute:: alarmvalue
            
            	The value of the statistic during the last sampling period.  For example, if the sample type is deltaValue, this value will be the difference between the samples at the beginning and end of the period.  If the sample type is absoluteValue, this value will be the sampled value at the end of the period. This is the value that is compared with the rising and falling thresholds.  The value during the current sampling period is not made available until the period is completed and will remain available until the next period completes
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: alarmstartupalarm
            
            	The alarm that may be sent when this entry is first set to valid.  If the first sample after this entry becomes valid is greater than or equal to the risingThreshold and alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single rising alarm will be generated.  If the first sample after this entry becomes valid is less than or equal to the fallingThreshold and alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single falling alarm will be generated.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  :py:class:`AlarmStartupAlarm <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.AlarmTable.AlarmEntry.AlarmStartupAlarm>`
            
            	**config**\: False
            
            .. attribute:: alarmrisingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is greater than or equal to this threshold and the associated alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3).  After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the alarmFallingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: alarmfallingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is less than or equal to this threshold and the associated alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3).  After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the alarmRisingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: alarmrisingeventindex
            
            	The index of the eventEntry that is used when a rising threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: alarmfallingeventindex
            
            	The index of the eventEntry that is used when a falling threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: alarmowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: alarmstatus
            
            	The status of this alarm entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.AlarmTable.AlarmEntry, self).__init__()

                self.yang_name = "alarmEntry"
                self.yang_parent_name = "alarmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['alarmindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('alarmindex', (YLeaf(YType.int32, 'alarmIndex'), ['int'])),
                    ('alarminterval', (YLeaf(YType.int32, 'alarmInterval'), ['int'])),
                    ('alarmvariable', (YLeaf(YType.str, 'alarmVariable'), ['str'])),
                    ('alarmsampletype', (YLeaf(YType.enumeration, 'alarmSampleType'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'AlarmTable.AlarmEntry.AlarmSampleType')])),
                    ('alarmvalue', (YLeaf(YType.int32, 'alarmValue'), ['int'])),
                    ('alarmstartupalarm', (YLeaf(YType.enumeration, 'alarmStartupAlarm'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'AlarmTable.AlarmEntry.AlarmStartupAlarm')])),
                    ('alarmrisingthreshold', (YLeaf(YType.int32, 'alarmRisingThreshold'), ['int'])),
                    ('alarmfallingthreshold', (YLeaf(YType.int32, 'alarmFallingThreshold'), ['int'])),
                    ('alarmrisingeventindex', (YLeaf(YType.int32, 'alarmRisingEventIndex'), ['int'])),
                    ('alarmfallingeventindex', (YLeaf(YType.int32, 'alarmFallingEventIndex'), ['int'])),
                    ('alarmowner', (YLeaf(YType.str, 'alarmOwner'), ['str'])),
                    ('alarmstatus', (YLeaf(YType.enumeration, 'alarmStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                ])
                self.alarmindex = None
                self.alarminterval = None
                self.alarmvariable = None
                self.alarmsampletype = None
                self.alarmvalue = None
                self.alarmstartupalarm = None
                self.alarmrisingthreshold = None
                self.alarmfallingthreshold = None
                self.alarmrisingeventindex = None
                self.alarmfallingeventindex = None
                self.alarmowner = None
                self.alarmstatus = None
                self._segment_path = lambda: "alarmEntry" + "[alarmIndex='" + str(self.alarmindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/alarmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.AlarmTable.AlarmEntry, [u'alarmindex', u'alarminterval', u'alarmvariable', u'alarmsampletype', u'alarmvalue', u'alarmstartupalarm', u'alarmrisingthreshold', u'alarmfallingthreshold', u'alarmrisingeventindex', u'alarmfallingeventindex', u'alarmowner', u'alarmstatus'], name, value)

            class AlarmSampleType(Enum):
                """
                AlarmSampleType (Enum Class)

                The method of sampling the selected variable and

                calculating the value to be compared against the

                thresholds.  If the value of this object is

                absoluteValue(1), the value of the selected variable

                will be compared directly with the thresholds at the

                end of the sampling interval.  If the value of this

                object is deltaValue(2), the value of the selected

                variable at the last sample will be subtracted from

                the current value, and the difference compared with

                the thresholds.

                This object may not be modified if the associated

                alarmStatus object is equal to valid(1).

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")


            class AlarmStartupAlarm(Enum):
                """
                AlarmStartupAlarm (Enum Class)

                The alarm that may be sent when this entry is first

                set to valid.  If the first sample after this entry

                becomes valid is greater than or equal to the

                risingThreshold and alarmStartupAlarm is equal to

                risingAlarm(1) or risingOrFallingAlarm(3), then a single

                rising alarm will be generated.  If the first sample

                after this entry becomes valid is less than or equal

                to the fallingThreshold and alarmStartupAlarm is equal

                to fallingAlarm(2) or risingOrFallingAlarm(3), then a

                single falling alarm will be generated.

                This object may not be modified if the associated

                alarmStatus object is equal to valid(1).

                .. data:: risingAlarm = 1

                .. data:: fallingAlarm = 2

                .. data:: risingOrFallingAlarm = 3

                """

                risingAlarm = Enum.YLeaf(1, "risingAlarm")

                fallingAlarm = Enum.YLeaf(2, "fallingAlarm")

                risingOrFallingAlarm = Enum.YLeaf(3, "risingOrFallingAlarm")





    class HostControlTable(Entity):
        """
        A list of host table control entries.
        
        .. attribute:: hostcontrolentry
        
        	A list of parameters that set up the discovery of hosts on a particular interface and the collection of statistics about these hosts.  For example, an instance of the hostControlTableSize object might be named hostControlTableSize.1
        	**type**\: list of  		 :py:class:`HostControlEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostControlTable.HostControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HostControlTable, self).__init__()

            self.yang_name = "hostControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hostControlEntry", ("hostcontrolentry", RMONMIB.HostControlTable.HostControlEntry))])
            self._leafs = OrderedDict()

            self.hostcontrolentry = YList(self)
            self._segment_path = lambda: "hostControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HostControlTable, [], name, value)


        class HostControlEntry(Entity):
            """
            A list of parameters that set up the discovery of hosts
            on a particular interface and the collection of statistics
            about these hosts.  For example, an instance of the
            hostControlTableSize object might be named
            hostControlTableSize.1
            
            .. attribute:: hostcontrolindex  (key)
            
            	An index that uniquely identifies an entry in the hostControl table.  Each such entry defines a function that discovers hosts on a particular interface and places statistics about them in the hostTable and the hostTimeTable on behalf of this hostControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hostcontroldatasource
            
            	This object identifies the source of the data for this instance of the host function.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated hostControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: hostcontroltablesize
            
            	The number of hostEntries in the hostTable and the hostTimeTable associated with this hostControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: hostcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the hostTable associated with this hostControlEntry.  If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: hostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: hostcontrolstatus
            
            	The status of this hostControl entry.  If this object is not equal to valid(1), all associated entries in the hostTable, hostTimeTable, and the hostTopNTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: hostcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: hostcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HostControlTable.HostControlEntry, self).__init__()

                self.yang_name = "hostControlEntry"
                self.yang_parent_name = "hostControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hostcontrolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hostcontrolindex', (YLeaf(YType.int32, 'hostControlIndex'), ['int'])),
                    ('hostcontroldatasource', (YLeaf(YType.str, 'hostControlDataSource'), ['str'])),
                    ('hostcontroltablesize', (YLeaf(YType.int32, 'hostControlTableSize'), ['int'])),
                    ('hostcontrollastdeletetime', (YLeaf(YType.uint32, 'hostControlLastDeleteTime'), ['int'])),
                    ('hostcontrolowner', (YLeaf(YType.str, 'hostControlOwner'), ['str'])),
                    ('hostcontrolstatus', (YLeaf(YType.enumeration, 'hostControlStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('hostcontroldroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:hostControlDroppedFrames'), ['int'])),
                    ('hostcontrolcreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:hostControlCreateTime'), ['int'])),
                ])
                self.hostcontrolindex = None
                self.hostcontroldatasource = None
                self.hostcontroltablesize = None
                self.hostcontrollastdeletetime = None
                self.hostcontrolowner = None
                self.hostcontrolstatus = None
                self.hostcontroldroppedframes = None
                self.hostcontrolcreatetime = None
                self._segment_path = lambda: "hostControlEntry" + "[hostControlIndex='" + str(self.hostcontrolindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HostControlTable.HostControlEntry, [u'hostcontrolindex', u'hostcontroldatasource', u'hostcontroltablesize', u'hostcontrollastdeletetime', u'hostcontrolowner', u'hostcontrolstatus', 'hostcontroldroppedframes', 'hostcontrolcreatetime'], name, value)




    class HostTable(Entity):
        """
        A list of host entries.
        
        .. attribute:: hostentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  For example, an instance of the hostOutBroadcastPkts object might be named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
        	**type**\: list of  		 :py:class:`HostEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTable.HostEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HostTable, self).__init__()

            self.yang_name = "hostTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hostEntry", ("hostentry", RMONMIB.HostTable.HostEntry))])
            self._leafs = OrderedDict()

            self.hostentry = YList(self)
            self._segment_path = lambda: "hostTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HostTable, [], name, value)


        class HostEntry(Entity):
            """
            A collection of statistics for a particular host that has
            been discovered on an interface of this device.  For example,
            an instance of the hostOutBroadcastPkts object might be
            named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
            
            .. attribute:: hostindex  (key)
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hostaddress  (key)
            
            	The physical address of this host
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: hostcreationorder
            
            	An index that defines the relative ordering of the creation time of hosts captured for a particular hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later.  It is important to note that the order for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTable.  By observing this variable, the management station may detect the circumstances where a previous association between a value of hostCreationOrder and a hostEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hostinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hostoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hostinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: hostoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: hostouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hostoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hostoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HostTable.HostEntry, self).__init__()

                self.yang_name = "hostEntry"
                self.yang_parent_name = "hostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hostindex','hostaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hostindex', (YLeaf(YType.int32, 'hostIndex'), ['int'])),
                    ('hostaddress', (YLeaf(YType.str, 'hostAddress'), ['str'])),
                    ('hostcreationorder', (YLeaf(YType.int32, 'hostCreationOrder'), ['int'])),
                    ('hostinpkts', (YLeaf(YType.uint32, 'hostInPkts'), ['int'])),
                    ('hostoutpkts', (YLeaf(YType.uint32, 'hostOutPkts'), ['int'])),
                    ('hostinoctets', (YLeaf(YType.uint32, 'hostInOctets'), ['int'])),
                    ('hostoutoctets', (YLeaf(YType.uint32, 'hostOutOctets'), ['int'])),
                    ('hostouterrors', (YLeaf(YType.uint32, 'hostOutErrors'), ['int'])),
                    ('hostoutbroadcastpkts', (YLeaf(YType.uint32, 'hostOutBroadcastPkts'), ['int'])),
                    ('hostoutmulticastpkts', (YLeaf(YType.uint32, 'hostOutMulticastPkts'), ['int'])),
                ])
                self.hostindex = None
                self.hostaddress = None
                self.hostcreationorder = None
                self.hostinpkts = None
                self.hostoutpkts = None
                self.hostinoctets = None
                self.hostoutoctets = None
                self.hostouterrors = None
                self.hostoutbroadcastpkts = None
                self.hostoutmulticastpkts = None
                self._segment_path = lambda: "hostEntry" + "[hostIndex='" + str(self.hostindex) + "']" + "[hostAddress='" + str(self.hostaddress) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HostTable.HostEntry, [u'hostindex', u'hostaddress', u'hostcreationorder', u'hostinpkts', u'hostoutpkts', u'hostinoctets', u'hostoutoctets', u'hostouterrors', u'hostoutbroadcastpkts', u'hostoutmulticastpkts'], name, value)




    class HostTimeTable(Entity):
        """
        A list of time\-ordered host table entries.
        
        .. attribute:: hosttimeentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  This collection includes the relative ordering of the creation time of this object.  For example, an instance of the hostTimeOutBroadcastPkts object might be named hostTimeOutBroadcastPkts.1.687
        	**type**\: list of  		 :py:class:`HostTimeEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTimeTable.HostTimeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HostTimeTable, self).__init__()

            self.yang_name = "hostTimeTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hostTimeEntry", ("hosttimeentry", RMONMIB.HostTimeTable.HostTimeEntry))])
            self._leafs = OrderedDict()

            self.hosttimeentry = YList(self)
            self._segment_path = lambda: "hostTimeTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HostTimeTable, [], name, value)


        class HostTimeEntry(Entity):
            """
            A collection of statistics for a particular host that has
            been discovered on an interface of this device.  This
            collection includes the relative ordering of the creation
            time of this object.  For example, an instance of the
            hostTimeOutBroadcastPkts object might be named
            hostTimeOutBroadcastPkts.1.687
            
            .. attribute:: hosttimeindex  (key)
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttimecreationorder  (key)
            
            	An index that uniquely identifies an entry in the hostTime table among those entries associated with the same hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later. Thus the management station has the ability to learn of new entries added to this table without downloading the entire table.  It is important to note that the index for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTimeTable.  By observing this variable, the management station may detect the circumstances where a download of the table may have missed entries, and where a previous association between a value of hostTimeCreationOrder and a hostTimeEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttimeaddress
            
            	The physical address of this host
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: hosttimeinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hosttimeinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: hosttimeoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: hosttimeouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTimeTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HostTimeTable.HostTimeEntry, self).__init__()

                self.yang_name = "hostTimeEntry"
                self.yang_parent_name = "hostTimeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttimeindex','hosttimecreationorder']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttimeindex', (YLeaf(YType.int32, 'hostTimeIndex'), ['int'])),
                    ('hosttimecreationorder', (YLeaf(YType.int32, 'hostTimeCreationOrder'), ['int'])),
                    ('hosttimeaddress', (YLeaf(YType.str, 'hostTimeAddress'), ['str'])),
                    ('hosttimeinpkts', (YLeaf(YType.uint32, 'hostTimeInPkts'), ['int'])),
                    ('hosttimeoutpkts', (YLeaf(YType.uint32, 'hostTimeOutPkts'), ['int'])),
                    ('hosttimeinoctets', (YLeaf(YType.uint32, 'hostTimeInOctets'), ['int'])),
                    ('hosttimeoutoctets', (YLeaf(YType.uint32, 'hostTimeOutOctets'), ['int'])),
                    ('hosttimeouterrors', (YLeaf(YType.uint32, 'hostTimeOutErrors'), ['int'])),
                    ('hosttimeoutbroadcastpkts', (YLeaf(YType.uint32, 'hostTimeOutBroadcastPkts'), ['int'])),
                    ('hosttimeoutmulticastpkts', (YLeaf(YType.uint32, 'hostTimeOutMulticastPkts'), ['int'])),
                ])
                self.hosttimeindex = None
                self.hosttimecreationorder = None
                self.hosttimeaddress = None
                self.hosttimeinpkts = None
                self.hosttimeoutpkts = None
                self.hosttimeinoctets = None
                self.hosttimeoutoctets = None
                self.hosttimeouterrors = None
                self.hosttimeoutbroadcastpkts = None
                self.hosttimeoutmulticastpkts = None
                self._segment_path = lambda: "hostTimeEntry" + "[hostTimeIndex='" + str(self.hosttimeindex) + "']" + "[hostTimeCreationOrder='" + str(self.hosttimecreationorder) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostTimeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HostTimeTable.HostTimeEntry, [u'hosttimeindex', u'hosttimecreationorder', u'hosttimeaddress', u'hosttimeinpkts', u'hosttimeoutpkts', u'hosttimeinoctets', u'hosttimeoutoctets', u'hosttimeouterrors', u'hosttimeoutbroadcastpkts', u'hosttimeoutmulticastpkts'], name, value)




    class HostTopNControlTable(Entity):
        """
        A list of top N host control entries.
        
        .. attribute:: hosttopncontrolentry
        
        	A set of parameters that control the creation of a report of the top N hosts according to several metrics.  For example, an instance of the hostTopNDuration object might be named hostTopNDuration.3
        	**type**\: list of  		 :py:class:`HostTopNControlEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTopNControlTable.HostTopNControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HostTopNControlTable, self).__init__()

            self.yang_name = "hostTopNControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hostTopNControlEntry", ("hosttopncontrolentry", RMONMIB.HostTopNControlTable.HostTopNControlEntry))])
            self._leafs = OrderedDict()

            self.hosttopncontrolentry = YList(self)
            self._segment_path = lambda: "hostTopNControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HostTopNControlTable, [], name, value)


        class HostTopNControlEntry(Entity):
            """
            A set of parameters that control the creation of a report
            of the top N hosts according to several metrics.  For
            example, an instance of the hostTopNDuration object might
            be named hostTopNDuration.3
            
            .. attribute:: hosttopncontrolindex  (key)
            
            	An index that uniquely identifies an entry in the hostTopNControl table.  Each such entry defines one top N report prepared for one interface
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttopnhostindex
            
            	The host table for which a top N report will be prepared on behalf of this entry.  The host table identified by a particular value of this index is associated with the same host table as identified by the same value of hostIndex.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttopnratebase
            
            	The variable for each host that the hostTopNRate variable is based upon.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\:  :py:class:`HostTopNRateBase <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase>`
            
            	**config**\: False
            
            .. attribute:: hosttopntimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, which is loaded into the associated hostTopNDuration object.  When this object is set to a non\-zero value, any associated hostTopNEntries shall be made inaccessible by the monitor.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  During this time, all associated hostTopNEntries shall remain inaccessible.  At the time that this object decrements to zero, the report is made accessible in the hostTopNTable.  Thus, the hostTopN table needs to be created only at the end of the collection interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Seconds
            
            .. attribute:: hosttopnduration
            
            	The number of seconds that this report has collected during the last sampling interval, or if this report is currently being collected, the number of seconds that this report is being collected during this sampling interval.  When the associated hostTopNTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the hostTopNTimeRemaining is set.  This value shall be zero if no reports have been requested for this hostTopNControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Seconds
            
            .. attribute:: hosttopnrequestedsize
            
            	The maximum number of hosts requested for the top N table.  When this object is created or modified, the probe should set hostTopNGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: hosttopngrantedsize
            
            	The maximum number of hosts in the top N table.  When the associated hostTopNRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated hostTopNRequestedSize object.  Hosts with the highest value of hostTopNRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more hosts
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: hosttopnstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated hostTopNTimeRemaining object was modified to start the requested report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: hosttopnowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: hosttopnstatus
            
            	The status of this hostTopNControl entry.  If this object is not equal to valid(1), all associated hostTopNEntries shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HostTopNControlTable.HostTopNControlEntry, self).__init__()

                self.yang_name = "hostTopNControlEntry"
                self.yang_parent_name = "hostTopNControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttopncontrolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttopncontrolindex', (YLeaf(YType.int32, 'hostTopNControlIndex'), ['int'])),
                    ('hosttopnhostindex', (YLeaf(YType.int32, 'hostTopNHostIndex'), ['int'])),
                    ('hosttopnratebase', (YLeaf(YType.enumeration, 'hostTopNRateBase'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase')])),
                    ('hosttopntimeremaining', (YLeaf(YType.int32, 'hostTopNTimeRemaining'), ['int'])),
                    ('hosttopnduration', (YLeaf(YType.int32, 'hostTopNDuration'), ['int'])),
                    ('hosttopnrequestedsize', (YLeaf(YType.int32, 'hostTopNRequestedSize'), ['int'])),
                    ('hosttopngrantedsize', (YLeaf(YType.int32, 'hostTopNGrantedSize'), ['int'])),
                    ('hosttopnstarttime', (YLeaf(YType.uint32, 'hostTopNStartTime'), ['int'])),
                    ('hosttopnowner', (YLeaf(YType.str, 'hostTopNOwner'), ['str'])),
                    ('hosttopnstatus', (YLeaf(YType.enumeration, 'hostTopNStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                ])
                self.hosttopncontrolindex = None
                self.hosttopnhostindex = None
                self.hosttopnratebase = None
                self.hosttopntimeremaining = None
                self.hosttopnduration = None
                self.hosttopnrequestedsize = None
                self.hosttopngrantedsize = None
                self.hosttopnstarttime = None
                self.hosttopnowner = None
                self.hosttopnstatus = None
                self._segment_path = lambda: "hostTopNControlEntry" + "[hostTopNControlIndex='" + str(self.hosttopncontrolindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostTopNControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HostTopNControlTable.HostTopNControlEntry, [u'hosttopncontrolindex', u'hosttopnhostindex', u'hosttopnratebase', u'hosttopntimeremaining', u'hosttopnduration', u'hosttopnrequestedsize', u'hosttopngrantedsize', u'hosttopnstarttime', u'hosttopnowner', u'hosttopnstatus'], name, value)

            class HostTopNRateBase(Enum):
                """
                HostTopNRateBase (Enum Class)

                The variable for each host that the hostTopNRate

                variable is based upon.

                This object may not be modified if the associated

                hostTopNStatus object is equal to valid(1).

                .. data:: hostTopNInPkts = 1

                .. data:: hostTopNOutPkts = 2

                .. data:: hostTopNInOctets = 3

                .. data:: hostTopNOutOctets = 4

                .. data:: hostTopNOutErrors = 5

                .. data:: hostTopNOutBroadcastPkts = 6

                .. data:: hostTopNOutMulticastPkts = 7

                """

                hostTopNInPkts = Enum.YLeaf(1, "hostTopNInPkts")

                hostTopNOutPkts = Enum.YLeaf(2, "hostTopNOutPkts")

                hostTopNInOctets = Enum.YLeaf(3, "hostTopNInOctets")

                hostTopNOutOctets = Enum.YLeaf(4, "hostTopNOutOctets")

                hostTopNOutErrors = Enum.YLeaf(5, "hostTopNOutErrors")

                hostTopNOutBroadcastPkts = Enum.YLeaf(6, "hostTopNOutBroadcastPkts")

                hostTopNOutMulticastPkts = Enum.YLeaf(7, "hostTopNOutMulticastPkts")





    class HostTopNTable(Entity):
        """
        A list of top N host entries.
        
        .. attribute:: hosttopnentry
        
        	A set of statistics for a host that is part of a top N report.  For example, an instance of the hostTopNRate object might be named hostTopNRate.3.10
        	**type**\: list of  		 :py:class:`HostTopNEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.HostTopNTable.HostTopNEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.HostTopNTable, self).__init__()

            self.yang_name = "hostTopNTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hostTopNEntry", ("hosttopnentry", RMONMIB.HostTopNTable.HostTopNEntry))])
            self._leafs = OrderedDict()

            self.hosttopnentry = YList(self)
            self._segment_path = lambda: "hostTopNTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.HostTopNTable, [], name, value)


        class HostTopNEntry(Entity):
            """
            A set of statistics for a host that is part of a top N
            report.  For example, an instance of the hostTopNRate
            object might be named hostTopNRate.3.10
            
            .. attribute:: hosttopnreport  (key)
            
            	This object identifies the top N report of which this entry is a part.  The set of hosts identified by a particular value of this object is part of the same report as identified by the same value of the hostTopNControlIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttopnindex  (key)
            
            	An index that uniquely identifies an entry in the hostTopN table among those in the same report. This index is between 1 and N, where N is the number of entries in this table.  Increasing values of hostTopNIndex shall be assigned to entries with decreasing values of hostTopNRate until index N is assigned to the entry with the lowest value of hostTopNRate or there are no more hostTopNEntries
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: hosttopnaddress
            
            	The physical address of this host
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: hosttopnrate
            
            	The amount of change in the selected variable during this sampling interval.  The selected variable is this host's instance of the object selected by hostTopNRateBase
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.HostTopNTable.HostTopNEntry, self).__init__()

                self.yang_name = "hostTopNEntry"
                self.yang_parent_name = "hostTopNTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttopnreport','hosttopnindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttopnreport', (YLeaf(YType.int32, 'hostTopNReport'), ['int'])),
                    ('hosttopnindex', (YLeaf(YType.int32, 'hostTopNIndex'), ['int'])),
                    ('hosttopnaddress', (YLeaf(YType.str, 'hostTopNAddress'), ['str'])),
                    ('hosttopnrate', (YLeaf(YType.int32, 'hostTopNRate'), ['int'])),
                ])
                self.hosttopnreport = None
                self.hosttopnindex = None
                self.hosttopnaddress = None
                self.hosttopnrate = None
                self._segment_path = lambda: "hostTopNEntry" + "[hostTopNReport='" + str(self.hosttopnreport) + "']" + "[hostTopNIndex='" + str(self.hosttopnindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostTopNTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.HostTopNTable.HostTopNEntry, [u'hosttopnreport', u'hosttopnindex', u'hosttopnaddress', u'hosttopnrate'], name, value)




    class MatrixControlTable(Entity):
        """
        A list of information entries for the
        traffic matrix on each interface.
        
        .. attribute:: matrixcontrolentry
        
        	Information about a traffic matrix on a particular interface.  For example, an instance of the matrixControlLastDeleteTime object might be named matrixControlLastDeleteTime.1
        	**type**\: list of  		 :py:class:`MatrixControlEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixControlTable.MatrixControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.MatrixControlTable, self).__init__()

            self.yang_name = "matrixControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("matrixControlEntry", ("matrixcontrolentry", RMONMIB.MatrixControlTable.MatrixControlEntry))])
            self._leafs = OrderedDict()

            self.matrixcontrolentry = YList(self)
            self._segment_path = lambda: "matrixControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.MatrixControlTable, [], name, value)


        class MatrixControlEntry(Entity):
            """
            Information about a traffic matrix on a particular
            interface.  For example, an instance of the
            matrixControlLastDeleteTime object might be named
            matrixControlLastDeleteTime.1
            
            .. attribute:: matrixcontrolindex  (key)
            
            	An index that uniquely identifies an entry in the matrixControl table.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the matrixSDTable and the matrixDSTable on behalf of this matrixControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: matrixcontroldatasource
            
            	This object identifies the source of the data from which this entry creates a traffic matrix. This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated matrixControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: matrixcontroltablesize
            
            	The number of matrixSDEntries in the matrixSDTable for this interface.  This must also be the value of the number of entries in the matrixDSTable for this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: matrixcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the matrixSDTable or matrixDSTable associated with this matrixControlEntry. If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: matrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: matrixcontrolstatus
            
            	The status of this matrixControl entry. If this object is not equal to valid(1), all associated entries in the matrixSDTable and the matrixDSTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: matrixcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: matrixcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.MatrixControlTable.MatrixControlEntry, self).__init__()

                self.yang_name = "matrixControlEntry"
                self.yang_parent_name = "matrixControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixcontrolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixcontrolindex', (YLeaf(YType.int32, 'matrixControlIndex'), ['int'])),
                    ('matrixcontroldatasource', (YLeaf(YType.str, 'matrixControlDataSource'), ['str'])),
                    ('matrixcontroltablesize', (YLeaf(YType.int32, 'matrixControlTableSize'), ['int'])),
                    ('matrixcontrollastdeletetime', (YLeaf(YType.uint32, 'matrixControlLastDeleteTime'), ['int'])),
                    ('matrixcontrolowner', (YLeaf(YType.str, 'matrixControlOwner'), ['str'])),
                    ('matrixcontrolstatus', (YLeaf(YType.enumeration, 'matrixControlStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('matrixcontroldroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:matrixControlDroppedFrames'), ['int'])),
                    ('matrixcontrolcreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:matrixControlCreateTime'), ['int'])),
                ])
                self.matrixcontrolindex = None
                self.matrixcontroldatasource = None
                self.matrixcontroltablesize = None
                self.matrixcontrollastdeletetime = None
                self.matrixcontrolowner = None
                self.matrixcontrolstatus = None
                self.matrixcontroldroppedframes = None
                self.matrixcontrolcreatetime = None
                self._segment_path = lambda: "matrixControlEntry" + "[matrixControlIndex='" + str(self.matrixcontrolindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/matrixControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.MatrixControlTable.MatrixControlEntry, [u'matrixcontrolindex', u'matrixcontroldatasource', u'matrixcontroltablesize', u'matrixcontrollastdeletetime', u'matrixcontrolowner', u'matrixcontrolstatus', 'matrixcontroldroppedframes', 'matrixcontrolcreatetime'], name, value)




    class MatrixSDTable(Entity):
        """
        A list of traffic matrix entries indexed by
        source and destination MAC address.
        
        .. attribute:: matrixsdentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
        	**type**\: list of  		 :py:class:`MatrixSDEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixSDTable.MatrixSDEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.MatrixSDTable, self).__init__()

            self.yang_name = "matrixSDTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("matrixSDEntry", ("matrixsdentry", RMONMIB.MatrixSDTable.MatrixSDEntry))])
            self._leafs = OrderedDict()

            self.matrixsdentry = YList(self)
            self._segment_path = lambda: "matrixSDTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.MatrixSDTable, [], name, value)


        class MatrixSDEntry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
            
            .. attribute:: matrixsdindex  (key)
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: matrixsdsourceaddress  (key)
            
            	The source physical address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: matrixsddestaddress  (key)
            
            	The destination physical address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: matrixsdpkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: matrixsdoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: matrixsderrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.MatrixSDTable.MatrixSDEntry, self).__init__()

                self.yang_name = "matrixSDEntry"
                self.yang_parent_name = "matrixSDTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixsdindex','matrixsdsourceaddress','matrixsddestaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixsdindex', (YLeaf(YType.int32, 'matrixSDIndex'), ['int'])),
                    ('matrixsdsourceaddress', (YLeaf(YType.str, 'matrixSDSourceAddress'), ['str'])),
                    ('matrixsddestaddress', (YLeaf(YType.str, 'matrixSDDestAddress'), ['str'])),
                    ('matrixsdpkts', (YLeaf(YType.uint32, 'matrixSDPkts'), ['int'])),
                    ('matrixsdoctets', (YLeaf(YType.uint32, 'matrixSDOctets'), ['int'])),
                    ('matrixsderrors', (YLeaf(YType.uint32, 'matrixSDErrors'), ['int'])),
                ])
                self.matrixsdindex = None
                self.matrixsdsourceaddress = None
                self.matrixsddestaddress = None
                self.matrixsdpkts = None
                self.matrixsdoctets = None
                self.matrixsderrors = None
                self._segment_path = lambda: "matrixSDEntry" + "[matrixSDIndex='" + str(self.matrixsdindex) + "']" + "[matrixSDSourceAddress='" + str(self.matrixsdsourceaddress) + "']" + "[matrixSDDestAddress='" + str(self.matrixsddestaddress) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/matrixSDTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.MatrixSDTable.MatrixSDEntry, [u'matrixsdindex', u'matrixsdsourceaddress', u'matrixsddestaddress', u'matrixsdpkts', u'matrixsdoctets', u'matrixsderrors'], name, value)




    class MatrixDSTable(Entity):
        """
        A list of traffic matrix entries indexed by
        destination and source MAC address.
        
        .. attribute:: matrixdsentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
        	**type**\: list of  		 :py:class:`MatrixDSEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.MatrixDSTable.MatrixDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.MatrixDSTable, self).__init__()

            self.yang_name = "matrixDSTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("matrixDSEntry", ("matrixdsentry", RMONMIB.MatrixDSTable.MatrixDSEntry))])
            self._leafs = OrderedDict()

            self.matrixdsentry = YList(self)
            self._segment_path = lambda: "matrixDSTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.MatrixDSTable, [], name, value)


        class MatrixDSEntry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
            
            .. attribute:: matrixdsindex  (key)
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: matrixdsdestaddress  (key)
            
            	The destination physical address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: matrixdssourceaddress  (key)
            
            	The source physical address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: matrixdspkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: matrixdsoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: matrixdserrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.MatrixDSTable.MatrixDSEntry, self).__init__()

                self.yang_name = "matrixDSEntry"
                self.yang_parent_name = "matrixDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixdsindex','matrixdsdestaddress','matrixdssourceaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixdsindex', (YLeaf(YType.int32, 'matrixDSIndex'), ['int'])),
                    ('matrixdsdestaddress', (YLeaf(YType.str, 'matrixDSDestAddress'), ['str'])),
                    ('matrixdssourceaddress', (YLeaf(YType.str, 'matrixDSSourceAddress'), ['str'])),
                    ('matrixdspkts', (YLeaf(YType.uint32, 'matrixDSPkts'), ['int'])),
                    ('matrixdsoctets', (YLeaf(YType.uint32, 'matrixDSOctets'), ['int'])),
                    ('matrixdserrors', (YLeaf(YType.uint32, 'matrixDSErrors'), ['int'])),
                ])
                self.matrixdsindex = None
                self.matrixdsdestaddress = None
                self.matrixdssourceaddress = None
                self.matrixdspkts = None
                self.matrixdsoctets = None
                self.matrixdserrors = None
                self._segment_path = lambda: "matrixDSEntry" + "[matrixDSIndex='" + str(self.matrixdsindex) + "']" + "[matrixDSDestAddress='" + str(self.matrixdsdestaddress) + "']" + "[matrixDSSourceAddress='" + str(self.matrixdssourceaddress) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/matrixDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.MatrixDSTable.MatrixDSEntry, [u'matrixdsindex', u'matrixdsdestaddress', u'matrixdssourceaddress', u'matrixdspkts', u'matrixdsoctets', u'matrixdserrors'], name, value)




    class FilterTable(Entity):
        """
        A list of packet filter entries.
        
        .. attribute:: filterentry
        
        	A set of parameters for a packet filter applied on a particular interface.  As an example, an instance of the filterPktData object might be named filterPktData.12
        	**type**\: list of  		 :py:class:`FilterEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.FilterTable.FilterEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.FilterTable, self).__init__()

            self.yang_name = "filterTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("filterEntry", ("filterentry", RMONMIB.FilterTable.FilterEntry))])
            self._leafs = OrderedDict()

            self.filterentry = YList(self)
            self._segment_path = lambda: "filterTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.FilterTable, [], name, value)


        class FilterEntry(Entity):
            """
            A set of parameters for a packet filter applied on a
            particular interface.  As an example, an instance of the
            filterPktData object might be named filterPktData.12
            
            .. attribute:: filterindex  (key)
            
            	An index that uniquely identifies an entry in the filter table.  Each such entry defines one filter that is to be applied to every packet received on an interface
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: filterchannelindex
            
            	This object identifies the channel of which this filter is a part.  The filters identified by a particular value of this object are associated with the same channel as identified by the same value of the channelIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: filterpktdataoffset
            
            	The offset from the beginning of each packet where a match of packet data will be attempted.  This offset is measured from the point in the physical layer packet after the framing bits, if any.  For example, in an Ethernet frame, this point is at the beginning of the destination MAC address.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: filterpktdata
            
            	The data that is to be matched with the input packet. For each packet received, this filter and the accompanying filterPktDataMask and filterPktDataNotMask will be adjusted for the offset.  The only bits relevant to this match algorithm are those that have the corresponding filterPktDataMask bit equal to one.  The following three rules are then applied to every packet\:  (1) If the packet is too short and does not have data     corresponding to part of the filterPktData, the packet     will fail this data match.  (2) For each relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to zero, if     the bit from the packet is not equal to the corresponding     bit from the filterPktData, then the packet will fail     this data match.  (3) If for every relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to one, the     bit from the packet is equal to the corresponding bit     from the filterPktData, then the packet will fail this     data match.  Any packets that have not failed any of the three matches above have passed this data match.  In particular, a zero length filter will match any packet.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: filterpktdatamask
            
            	The mask that is applied to the match process. After adjusting this mask for the offset, only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the match algorithm.  The offset is applied to filterPktDataMask in the same way it is applied to the filter.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: filterpktdatanotmask
            
            	The inversion mask that is applied to the match process.  After adjusting this mask for the offset, those relevant bits in the received packet that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktData object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet that correspond to bits set in this mask must be different to its corresponding bit in the filterPktData object.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: filterpktstatus
            
            	The status that is to be matched with the input packet. The only bits relevant to this match algorithm are those that have the corresponding filterPktStatusMask bit equal to one. The following two rules are then applied to every packet\:  (1) For each relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to zero, if     the bit from the packet status is not equal to the     corresponding bit from the filterPktStatus, then the     packet will fail this status match.  (2) If for every relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to one, the     bit from the packet status is equal to the corresponding     bit from the filterPktStatus, then the packet will fail     this status match.  Any packets that have not failed either of the two matches above have passed this status match.  In particular, a zero length status filter will match any packet's status.  The value of the packet status is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum. The errors and the bits that represent them are dependent on the media type of the interface that this channel is receiving packets from.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined.  For the purposes of this status matching algorithm, if the packet status is longer than this filterPktStatus object, this object is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: filterpktstatusmask
            
            	The mask that is applied to the status match process. Only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the status match algorithm.  For the purposes of the matching algorithm, if the associated filterPktStatus object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the size of the filterPktStatus.  In addition, if a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: filterpktstatusnotmask
            
            	The inversion mask that is applied to the status match process.  Those relevant bits in the received packet status that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktStatus object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet status that correspond to bits set in this mask must be different to its corresponding bit in the filterPktStatus object for the packet to be accepted.  For the purposes of the matching algorithm, if the associated filterPktStatus object or a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the longer of the lengths of the filterPktStatus object and the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: filterowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: filterstatus
            
            	The status of this filter entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: filterprotocoldirdatalocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with performs the following operations on every packet\:  1) \- If the packet doesn't match the protocol directory entry      identified by this object, discard the packet and exit      (i.e., discard the packet if it is not of the identified      protocol). 2) \- If the associated filterProtocolDirLocalIndex is non\-zero      and the packet doesn't match the protocol directory      entry identified by that object, discard the packet and      exit 3) \- If the packet matches, perform the regular filter      algorithm as if the beginning of this named protocol is      the beginning of the packet, potentially applying the      filterOffset value to move further into the packet
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: filterprotocoldirlocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with will discard the packet if the packet doesn't match this protocol directory entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.FilterTable.FilterEntry, self).__init__()

                self.yang_name = "filterEntry"
                self.yang_parent_name = "filterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['filterindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('filterindex', (YLeaf(YType.int32, 'filterIndex'), ['int'])),
                    ('filterchannelindex', (YLeaf(YType.int32, 'filterChannelIndex'), ['int'])),
                    ('filterpktdataoffset', (YLeaf(YType.int32, 'filterPktDataOffset'), ['int'])),
                    ('filterpktdata', (YLeaf(YType.str, 'filterPktData'), ['str'])),
                    ('filterpktdatamask', (YLeaf(YType.str, 'filterPktDataMask'), ['str'])),
                    ('filterpktdatanotmask', (YLeaf(YType.str, 'filterPktDataNotMask'), ['str'])),
                    ('filterpktstatus', (YLeaf(YType.int32, 'filterPktStatus'), ['int'])),
                    ('filterpktstatusmask', (YLeaf(YType.int32, 'filterPktStatusMask'), ['int'])),
                    ('filterpktstatusnotmask', (YLeaf(YType.int32, 'filterPktStatusNotMask'), ['int'])),
                    ('filterowner', (YLeaf(YType.str, 'filterOwner'), ['str'])),
                    ('filterstatus', (YLeaf(YType.enumeration, 'filterStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('filterprotocoldirdatalocalindex', (YLeaf(YType.int32, 'RMON2-MIB:filterProtocolDirDataLocalIndex'), ['int'])),
                    ('filterprotocoldirlocalindex', (YLeaf(YType.int32, 'RMON2-MIB:filterProtocolDirLocalIndex'), ['int'])),
                ])
                self.filterindex = None
                self.filterchannelindex = None
                self.filterpktdataoffset = None
                self.filterpktdata = None
                self.filterpktdatamask = None
                self.filterpktdatanotmask = None
                self.filterpktstatus = None
                self.filterpktstatusmask = None
                self.filterpktstatusnotmask = None
                self.filterowner = None
                self.filterstatus = None
                self.filterprotocoldirdatalocalindex = None
                self.filterprotocoldirlocalindex = None
                self._segment_path = lambda: "filterEntry" + "[filterIndex='" + str(self.filterindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/filterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.FilterTable.FilterEntry, [u'filterindex', u'filterchannelindex', u'filterpktdataoffset', u'filterpktdata', u'filterpktdatamask', u'filterpktdatanotmask', u'filterpktstatus', u'filterpktstatusmask', u'filterpktstatusnotmask', u'filterowner', u'filterstatus', 'filterprotocoldirdatalocalindex', 'filterprotocoldirlocalindex'], name, value)




    class ChannelTable(Entity):
        """
        A list of packet channel entries.
        
        .. attribute:: channelentry
        
        	A set of parameters for a packet channel applied on a particular interface.  As an example, an instance of the channelMatches object might be named channelMatches.3
        	**type**\: list of  		 :py:class:`ChannelEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.ChannelTable.ChannelEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.ChannelTable, self).__init__()

            self.yang_name = "channelTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("channelEntry", ("channelentry", RMONMIB.ChannelTable.ChannelEntry))])
            self._leafs = OrderedDict()

            self.channelentry = YList(self)
            self._segment_path = lambda: "channelTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.ChannelTable, [], name, value)


        class ChannelEntry(Entity):
            """
            A set of parameters for a packet channel applied on a
            particular interface.  As an example, an instance of the
            channelMatches object might be named channelMatches.3
            
            .. attribute:: channelindex  (key)
            
            	An index that uniquely identifies an entry in the channel table.  Each such entry defines one channel, a logical data and event stream.  It is suggested that before creating a channel, an application should scan all instances of the filterChannelIndex object to make sure that there are no pre\-existing filters that would be inadvertently be linked to the channel
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: channelifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device to which the associated filters are applied to allow data into this channel.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in RFC 2233 [17].  The filters in this group are applied to all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: channelaccepttype
            
            	This object controls the action of the filters associated with this channel.  If this object is equal to acceptMatched(1), packets will be accepted to this channel if they are accepted by both the packet data and packet status matches of an associated filter.  If this object is equal to acceptFailed(2), packets will be accepted to this channel only if they fail either the packet data match or the packet status match of each of the associated filters.  In particular, a channel with no associated filters will match no packets if set to acceptMatched(1) case and will match all packets in the acceptFailed(2) case.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  :py:class:`ChannelAcceptType <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.ChannelTable.ChannelEntry.ChannelAcceptType>`
            
            	**config**\: False
            
            .. attribute:: channeldatacontrol
            
            	This object controls the flow of data through this channel. If this object is on(1), data, status and events flow through this channel.  If this object is off(2), data, status and events will not flow through this channel
            	**type**\:  :py:class:`ChannelDataControl <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.ChannelTable.ChannelEntry.ChannelDataControl>`
            
            	**config**\: False
            
            .. attribute:: channelturnoneventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from off to on when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOnEventIndex must be set to zero, a non\-existent event index. This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: channelturnoffeventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from on to off when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOffEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: channeleventindex
            
            	The value of this object identifies the event that is configured to be generated when the associated channelDataControl is on and a packet is matched.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: channeleventstatus
            
            	The event status of this channel.  If this channel is configured to generate events when packets are matched, a means of controlling the flow of those events is often needed.  When this object is equal to eventReady(1), a single event may be generated, after which this object will be set by the probe to eventFired(2).  While in the eventFired(2) state, no events will be generated until the object is modified to eventReady(1) (or eventAlwaysReady(3)).  The management station can thus easily respond to a notification of an event by re\-enabling this object.  If the management station wishes to disable this flow control and allow events to be generated at will, this object may be set to eventAlwaysReady(3).  Disabling the flow control is discouraged as it can result in high network traffic or other performance problems
            	**type**\:  :py:class:`ChannelEventStatus <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.ChannelTable.ChannelEntry.ChannelEventStatus>`
            
            	**config**\: False
            
            .. attribute:: channelmatches
            
            	The number of times this channel has matched a packet. Note that this object is updated even when channelDataControl is set to off
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: channeldescription
            
            	A comment describing this channel
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: channelowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: channelstatus
            
            	The status of this channel entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: channeldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe      is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: channelcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.ChannelTable.ChannelEntry, self).__init__()

                self.yang_name = "channelEntry"
                self.yang_parent_name = "channelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['channelindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('channelindex', (YLeaf(YType.int32, 'channelIndex'), ['int'])),
                    ('channelifindex', (YLeaf(YType.int32, 'channelIfIndex'), ['int'])),
                    ('channelaccepttype', (YLeaf(YType.enumeration, 'channelAcceptType'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'ChannelTable.ChannelEntry.ChannelAcceptType')])),
                    ('channeldatacontrol', (YLeaf(YType.enumeration, 'channelDataControl'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'ChannelTable.ChannelEntry.ChannelDataControl')])),
                    ('channelturnoneventindex', (YLeaf(YType.int32, 'channelTurnOnEventIndex'), ['int'])),
                    ('channelturnoffeventindex', (YLeaf(YType.int32, 'channelTurnOffEventIndex'), ['int'])),
                    ('channeleventindex', (YLeaf(YType.int32, 'channelEventIndex'), ['int'])),
                    ('channeleventstatus', (YLeaf(YType.enumeration, 'channelEventStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'ChannelTable.ChannelEntry.ChannelEventStatus')])),
                    ('channelmatches', (YLeaf(YType.uint32, 'channelMatches'), ['int'])),
                    ('channeldescription', (YLeaf(YType.str, 'channelDescription'), ['str'])),
                    ('channelowner', (YLeaf(YType.str, 'channelOwner'), ['str'])),
                    ('channelstatus', (YLeaf(YType.enumeration, 'channelStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                    ('channeldroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:channelDroppedFrames'), ['int'])),
                    ('channelcreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:channelCreateTime'), ['int'])),
                ])
                self.channelindex = None
                self.channelifindex = None
                self.channelaccepttype = None
                self.channeldatacontrol = None
                self.channelturnoneventindex = None
                self.channelturnoffeventindex = None
                self.channeleventindex = None
                self.channeleventstatus = None
                self.channelmatches = None
                self.channeldescription = None
                self.channelowner = None
                self.channelstatus = None
                self.channeldroppedframes = None
                self.channelcreatetime = None
                self._segment_path = lambda: "channelEntry" + "[channelIndex='" + str(self.channelindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/channelTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.ChannelTable.ChannelEntry, [u'channelindex', u'channelifindex', u'channelaccepttype', u'channeldatacontrol', u'channelturnoneventindex', u'channelturnoffeventindex', u'channeleventindex', u'channeleventstatus', u'channelmatches', u'channeldescription', u'channelowner', u'channelstatus', 'channeldroppedframes', 'channelcreatetime'], name, value)

            class ChannelAcceptType(Enum):
                """
                ChannelAcceptType (Enum Class)

                This object controls the action of the filters

                associated with this channel.  If this object is equal

                to acceptMatched(1), packets will be accepted to this

                channel if they are accepted by both the packet data and

                packet status matches of an associated filter.  If

                this object is equal to acceptFailed(2), packets will

                be accepted to this channel only if they fail either

                the packet data match or the packet status match of

                each of the associated filters.

                In particular, a channel with no associated filters will

                match no packets if set to acceptMatched(1) case and will

                match all packets in the acceptFailed(2) case.

                This object may not be modified if the associated

                channelStatus object is equal to valid(1).

                .. data:: acceptMatched = 1

                .. data:: acceptFailed = 2

                """

                acceptMatched = Enum.YLeaf(1, "acceptMatched")

                acceptFailed = Enum.YLeaf(2, "acceptFailed")


            class ChannelDataControl(Enum):
                """
                ChannelDataControl (Enum Class)

                This object controls the flow of data through this channel.

                If this object is on(1), data, status and events flow

                through this channel.  If this object is off(2), data,

                status and events will not flow through this channel.

                .. data:: on = 1

                .. data:: off = 2

                """

                on = Enum.YLeaf(1, "on")

                off = Enum.YLeaf(2, "off")


            class ChannelEventStatus(Enum):
                """
                ChannelEventStatus (Enum Class)

                The event status of this channel.

                If this channel is configured to generate events

                when packets are matched, a means of controlling

                the flow of those events is often needed.  When

                this object is equal to eventReady(1), a single

                event may be generated, after which this object

                will be set by the probe to eventFired(2).  While

                in the eventFired(2) state, no events will be

                generated until the object is modified to

                eventReady(1) (or eventAlwaysReady(3)).  The

                management station can thus easily respond to a

                notification of an event by re\-enabling this object.

                If the management station wishes to disable this

                flow control and allow events to be generated

                at will, this object may be set to

                eventAlwaysReady(3).  Disabling the flow control

                is discouraged as it can result in high network

                traffic or other performance problems.

                .. data:: eventReady = 1

                .. data:: eventFired = 2

                .. data:: eventAlwaysReady = 3

                """

                eventReady = Enum.YLeaf(1, "eventReady")

                eventFired = Enum.YLeaf(2, "eventFired")

                eventAlwaysReady = Enum.YLeaf(3, "eventAlwaysReady")





    class BufferControlTable(Entity):
        """
        A list of buffers control entries.
        
        .. attribute:: buffercontrolentry
        
        	A set of parameters that control the collection of a stream of packets that have matched filters.  As an example, an instance of the bufferControlCaptureSliceSize object might be named bufferControlCaptureSliceSize.3
        	**type**\: list of  		 :py:class:`BufferControlEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.BufferControlTable.BufferControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.BufferControlTable, self).__init__()

            self.yang_name = "bufferControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("bufferControlEntry", ("buffercontrolentry", RMONMIB.BufferControlTable.BufferControlEntry))])
            self._leafs = OrderedDict()

            self.buffercontrolentry = YList(self)
            self._segment_path = lambda: "bufferControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.BufferControlTable, [], name, value)


        class BufferControlEntry(Entity):
            """
            A set of parameters that control the collection of a stream
            of packets that have matched filters.  As an example, an
            instance of the bufferControlCaptureSliceSize object might
            be named bufferControlCaptureSliceSize.3
            
            .. attribute:: buffercontrolindex  (key)
            
            	An index that uniquely identifies an entry in the bufferControl table.  The value of this index shall never be zero.  Each such entry defines one set of packets that is captured and controlled by one or more filters
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: buffercontrolchannelindex
            
            	An index that identifies the channel that is the source of packets for this bufferControl table. The channel identified by a particular value of this index is the same as identified by the same value of the channelIndex object.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: buffercontrolfullstatus
            
            	This object shows whether the buffer has room to accept new packets or if it is full.  If the status is spaceAvailable(1), the buffer is accepting new packets normally.  If the status is full(2) and the associated bufferControlFullAction object is wrapWhenFull, the buffer is accepting new packets by deleting enough of the oldest packets to make room for new ones as they arrive.  Otherwise, if the status is full(2) and the bufferControlFullAction object is lockWhenFull, then the buffer has stopped collecting packets.  When this object is set to full(2) the probe must not later set it to spaceAvailable(1) except in the case of a significant gain in resources such as an increase of bufferControlOctetsGranted.  In particular, the wrap\-mode action of deleting old packets to make room for newly arrived packets must not affect the value of this object
            	**type**\:  :py:class:`BufferControlFullStatus <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.BufferControlTable.BufferControlEntry.BufferControlFullStatus>`
            
            	**config**\: False
            
            .. attribute:: buffercontrolfullaction
            
            	Controls the action of the buffer when it reaches the full status.  When in the lockWhenFull(1) state and a packet is added to the buffer that fills the buffer, the bufferControlFullStatus will be set to full(2) and this buffer will stop capturing packets
            	**type**\:  :py:class:`BufferControlFullAction <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.BufferControlTable.BufferControlEntry.BufferControlFullAction>`
            
            	**config**\: False
            
            .. attribute:: buffercontrolcaptureslicesize
            
            	The maximum number of octets of each packet that will be saved in this capture buffer. For example, if a 1500 octet packet is received by the probe and this object is set to 500, then only 500 octets of the packet will be stored in the associated capture buffer.  If this variable is set to 0, the capture buffer will save as many octets as is possible.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: buffercontroldownloadslicesize
            
            	The maximum number of octets of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer, the associated bufferControlDownloadOffset is 0, and this object is set to 100, then the captureBufferPacket object that contains the packet will contain only the first 100 octets of the packet.  A prudent manager will take into account possible interoperability or fragmentation problems that may occur if the download slice size is set too large. In particular, conformant SNMP implementations are not required to accept messages whose length exceeds 484 octets, although they are encouraged to support larger datagrams whenever feasible
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: buffercontroldownloadoffset
            
            	The offset of the first octet of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer and this object is set to 100, then the captureBufferPacket object that contains the packet will contain bytes starting 100 octets into the packet
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolmaxoctetsrequested
            
            	The requested maximum number of octets to be saved in this captureBuffer, including any implementation\-specific overhead. If this variable is set to \-1, the capture buffer will save as many octets as is possible.  When this object is created or modified, the probe should set bufferControlMaxOctetsGranted as closely to this object as is possible for the particular probe implementation and available resources.  However, if the object has the special value of \-1, the probe must set bufferControlMaxOctetsGranted to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolmaxoctetsgranted
            
            	The maximum number of octets that can be saved in this captureBuffer, including overhead. If this variable is \-1, the capture buffer will save as many octets as possible.  When the bufferControlMaxOctetsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources. However, if the request object has the special value of \-1, the probe must set this object to \-1.  The probe must not lower this value except as a result of a modification to the associated bufferControlMaxOctetsRequested object.  When this maximum number of octets is reached and a new packet is to be added to this capture buffer and the corresponding bufferControlFullAction is set to wrapWhenFull(2), enough of the oldest packets associated with this capture buffer shall be deleted by the agent so that the new packet can be added.  If the corresponding bufferControlFullAction is set to lockWhenFull(1), the new packet shall be discarded.  In either case, the probe must set bufferControlFullStatus to full(2).  When the value of this object changes to a value less than the current value, entries are deleted from the captureBufferTable associated with this bufferControlEntry.  Enough of the oldest of these captureBufferEntries shall be deleted by the agent so that the number of octets used remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated captureBufferEntries may be allowed to grow
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolcapturedpackets
            
            	The number of packets currently in this captureBuffer
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: buffercontrolturnontime
            
            	The value of sysUpTime when this capture buffer was first turned on
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: buffercontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: buffercontrolstatus
            
            	The status of this buffer Control Entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.BufferControlTable.BufferControlEntry, self).__init__()

                self.yang_name = "bufferControlEntry"
                self.yang_parent_name = "bufferControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffercontrolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('buffercontrolindex', (YLeaf(YType.int32, 'bufferControlIndex'), ['int'])),
                    ('buffercontrolchannelindex', (YLeaf(YType.int32, 'bufferControlChannelIndex'), ['int'])),
                    ('buffercontrolfullstatus', (YLeaf(YType.enumeration, 'bufferControlFullStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'BufferControlTable.BufferControlEntry.BufferControlFullStatus')])),
                    ('buffercontrolfullaction', (YLeaf(YType.enumeration, 'bufferControlFullAction'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'BufferControlTable.BufferControlEntry.BufferControlFullAction')])),
                    ('buffercontrolcaptureslicesize', (YLeaf(YType.int32, 'bufferControlCaptureSliceSize'), ['int'])),
                    ('buffercontroldownloadslicesize', (YLeaf(YType.int32, 'bufferControlDownloadSliceSize'), ['int'])),
                    ('buffercontroldownloadoffset', (YLeaf(YType.int32, 'bufferControlDownloadOffset'), ['int'])),
                    ('buffercontrolmaxoctetsrequested', (YLeaf(YType.int32, 'bufferControlMaxOctetsRequested'), ['int'])),
                    ('buffercontrolmaxoctetsgranted', (YLeaf(YType.int32, 'bufferControlMaxOctetsGranted'), ['int'])),
                    ('buffercontrolcapturedpackets', (YLeaf(YType.int32, 'bufferControlCapturedPackets'), ['int'])),
                    ('buffercontrolturnontime', (YLeaf(YType.uint32, 'bufferControlTurnOnTime'), ['int'])),
                    ('buffercontrolowner', (YLeaf(YType.str, 'bufferControlOwner'), ['str'])),
                    ('buffercontrolstatus', (YLeaf(YType.enumeration, 'bufferControlStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                ])
                self.buffercontrolindex = None
                self.buffercontrolchannelindex = None
                self.buffercontrolfullstatus = None
                self.buffercontrolfullaction = None
                self.buffercontrolcaptureslicesize = None
                self.buffercontroldownloadslicesize = None
                self.buffercontroldownloadoffset = None
                self.buffercontrolmaxoctetsrequested = None
                self.buffercontrolmaxoctetsgranted = None
                self.buffercontrolcapturedpackets = None
                self.buffercontrolturnontime = None
                self.buffercontrolowner = None
                self.buffercontrolstatus = None
                self._segment_path = lambda: "bufferControlEntry" + "[bufferControlIndex='" + str(self.buffercontrolindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/bufferControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.BufferControlTable.BufferControlEntry, [u'buffercontrolindex', u'buffercontrolchannelindex', u'buffercontrolfullstatus', u'buffercontrolfullaction', u'buffercontrolcaptureslicesize', u'buffercontroldownloadslicesize', u'buffercontroldownloadoffset', u'buffercontrolmaxoctetsrequested', u'buffercontrolmaxoctetsgranted', u'buffercontrolcapturedpackets', u'buffercontrolturnontime', u'buffercontrolowner', u'buffercontrolstatus'], name, value)

            class BufferControlFullAction(Enum):
                """
                BufferControlFullAction (Enum Class)

                Controls the action of the buffer when it

                reaches the full status.  When in the lockWhenFull(1)

                state and a packet is added to the buffer that

                fills the buffer, the bufferControlFullStatus will

                be set to full(2) and this buffer will stop capturing

                packets.

                .. data:: lockWhenFull = 1

                .. data:: wrapWhenFull = 2

                """

                lockWhenFull = Enum.YLeaf(1, "lockWhenFull")

                wrapWhenFull = Enum.YLeaf(2, "wrapWhenFull")


            class BufferControlFullStatus(Enum):
                """
                BufferControlFullStatus (Enum Class)

                This object shows whether the buffer has room to

                accept new packets or if it is full.

                If the status is spaceAvailable(1), the buffer is

                accepting new packets normally.  If the status is

                full(2) and the associated bufferControlFullAction

                object is wrapWhenFull, the buffer is accepting new

                packets by deleting enough of the oldest packets

                to make room for new ones as they arrive.  Otherwise,

                if the status is full(2) and the

                bufferControlFullAction object is lockWhenFull,

                then the buffer has stopped collecting packets.

                When this object is set to full(2) the probe must

                not later set it to spaceAvailable(1) except in the

                case of a significant gain in resources such as

                an increase of bufferControlOctetsGranted.  In

                particular, the wrap\-mode action of deleting old

                packets to make room for newly arrived packets

                must not affect the value of this object.

                .. data:: spaceAvailable = 1

                .. data:: full = 2

                """

                spaceAvailable = Enum.YLeaf(1, "spaceAvailable")

                full = Enum.YLeaf(2, "full")





    class CaptureBufferTable(Entity):
        """
        A list of packets captured off of a channel.
        
        .. attribute:: capturebufferentry
        
        	A packet captured off of an attached network.  As an example, an instance of the captureBufferPacketData object might be named captureBufferPacketData.3.1783
        	**type**\: list of  		 :py:class:`CaptureBufferEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.CaptureBufferTable.CaptureBufferEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.CaptureBufferTable, self).__init__()

            self.yang_name = "captureBufferTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("captureBufferEntry", ("capturebufferentry", RMONMIB.CaptureBufferTable.CaptureBufferEntry))])
            self._leafs = OrderedDict()

            self.capturebufferentry = YList(self)
            self._segment_path = lambda: "captureBufferTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.CaptureBufferTable, [], name, value)


        class CaptureBufferEntry(Entity):
            """
            A packet captured off of an attached network.  As an
            example, an instance of the captureBufferPacketData
            object might be named captureBufferPacketData.3.1783
            
            .. attribute:: capturebuffercontrolindex  (key)
            
            	The index of the bufferControlEntry with which this packet is associated
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: capturebufferindex  (key)
            
            	An index that uniquely identifies an entry in the captureBuffer table associated with a particular bufferControlEntry.  This index will start at 1 and increase by one for each new packet added with the same captureBufferControlIndex.  Should this value reach 2147483647, the next packet added with the same captureBufferControlIndex shall cause this value to wrap around to 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: capturebufferpacketid
            
            	An index that describes the order of packets that are received on a particular interface. The packetID of a packet captured on an interface is defined to be greater than the packetID's of all packets captured previously on the same interface.  As the captureBufferPacketID object has a maximum positive value of 2^31 \- 1, any captureBufferPacketID object shall have the value of the associated packet's packetID mod 2^31
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: capturebufferpacketdata
            
            	The data inside the packet, starting at the beginning of the packet plus any offset specified in the associated bufferControlDownloadOffset, including any link level headers.  The length of the data in this object is the minimum of the length of the captured packet minus the offset, the length of the associated bufferControlCaptureSliceSize minus the offset, and the associated bufferControlDownloadSliceSize.  If this minimum is less than zero, this object shall have a length of zero
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: capturebufferpacketlength
            
            	The actual length (off the wire) of the packet stored in this entry, including FCS octets
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Octets
            
            .. attribute:: capturebufferpackettime
            
            	The number of milliseconds that had passed since this capture buffer was first turned on when this packet was captured
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: Milliseconds
            
            .. attribute:: capturebufferpacketstatus
            
            	A value which indicates the error status of this packet.  The value of this object is defined in the same way as filterPktStatus.  The value is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error         3    First packet in this capture buffer after              it was detected that some packets were              not processed correctly.         4    Packet's order in buffer is only approximate              (May only be set for packets sent from              the probe)  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.CaptureBufferTable.CaptureBufferEntry, self).__init__()

                self.yang_name = "captureBufferEntry"
                self.yang_parent_name = "captureBufferTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['capturebuffercontrolindex','capturebufferindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('capturebuffercontrolindex', (YLeaf(YType.int32, 'captureBufferControlIndex'), ['int'])),
                    ('capturebufferindex', (YLeaf(YType.int32, 'captureBufferIndex'), ['int'])),
                    ('capturebufferpacketid', (YLeaf(YType.int32, 'captureBufferPacketID'), ['int'])),
                    ('capturebufferpacketdata', (YLeaf(YType.str, 'captureBufferPacketData'), ['str'])),
                    ('capturebufferpacketlength', (YLeaf(YType.int32, 'captureBufferPacketLength'), ['int'])),
                    ('capturebufferpackettime', (YLeaf(YType.int32, 'captureBufferPacketTime'), ['int'])),
                    ('capturebufferpacketstatus', (YLeaf(YType.int32, 'captureBufferPacketStatus'), ['int'])),
                ])
                self.capturebuffercontrolindex = None
                self.capturebufferindex = None
                self.capturebufferpacketid = None
                self.capturebufferpacketdata = None
                self.capturebufferpacketlength = None
                self.capturebufferpackettime = None
                self.capturebufferpacketstatus = None
                self._segment_path = lambda: "captureBufferEntry" + "[captureBufferControlIndex='" + str(self.capturebuffercontrolindex) + "']" + "[captureBufferIndex='" + str(self.capturebufferindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/captureBufferTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.CaptureBufferTable.CaptureBufferEntry, [u'capturebuffercontrolindex', u'capturebufferindex', u'capturebufferpacketid', u'capturebufferpacketdata', u'capturebufferpacketlength', u'capturebufferpackettime', u'capturebufferpacketstatus'], name, value)




    class EventTable(Entity):
        """
        A list of events to be generated.
        
        .. attribute:: evententry
        
        	A set of parameters that describe an event to be generated when certain conditions are met.  As an example, an instance of the eventLastTimeSent object might be named eventLastTimeSent.6
        	**type**\: list of  		 :py:class:`EventEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EventTable.EventEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.EventTable, self).__init__()

            self.yang_name = "eventTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("eventEntry", ("evententry", RMONMIB.EventTable.EventEntry))])
            self._leafs = OrderedDict()

            self.evententry = YList(self)
            self._segment_path = lambda: "eventTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.EventTable, [], name, value)


        class EventEntry(Entity):
            """
            A set of parameters that describe an event to be generated
            when certain conditions are met.  As an example, an instance
            of the eventLastTimeSent object might be named
            eventLastTimeSent.6
            
            .. attribute:: eventindex  (key)
            
            	An index that uniquely identifies an entry in the event table.  Each such entry defines one event that is to be generated when the appropriate conditions occur
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: eventdescription
            
            	A comment describing this event entry
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: eventtype
            
            	The type of notification that the probe will make about this event.  In the case of log, an entry is made in the log table for each event.  In the case of snmp\-trap, an SNMP trap is sent to one or more management stations
            	**type**\:  :py:class:`EventType <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.EventTable.EventEntry.EventType>`
            
            	**config**\: False
            
            .. attribute:: eventcommunity
            
            	If an SNMP trap is to be sent, it will be sent to the SNMP community specified by this octet string
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: eventlasttimesent
            
            	The value of sysUpTime at the time this event entry last generated an event.  If this entry has not generated any events, this value will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: eventowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it.  If this object contains a string starting with 'monitor' and has associated entries in the log table, all connected management stations should retrieve those log entries, as they may have significance to all management stations connected to this device
            	**type**\: str
            
            	**length:** 0..127
            
            	**config**\: False
            
            .. attribute:: eventstatus
            
            	The status of this event entry.  If this object is not equal to valid(1), all associated log entries shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.EventTable.EventEntry, self).__init__()

                self.yang_name = "eventEntry"
                self.yang_parent_name = "eventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['eventindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('eventindex', (YLeaf(YType.int32, 'eventIndex'), ['int'])),
                    ('eventdescription', (YLeaf(YType.str, 'eventDescription'), ['str'])),
                    ('eventtype', (YLeaf(YType.enumeration, 'eventType'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'RMONMIB', 'EventTable.EventEntry.EventType')])),
                    ('eventcommunity', (YLeaf(YType.str, 'eventCommunity'), ['str'])),
                    ('eventlasttimesent', (YLeaf(YType.uint32, 'eventLastTimeSent'), ['int'])),
                    ('eventowner', (YLeaf(YType.str, 'eventOwner'), ['str'])),
                    ('eventstatus', (YLeaf(YType.enumeration, 'eventStatus'), [('ydk.models.cisco_ios_xe.RMON_MIB', 'EntryStatus', '')])),
                ])
                self.eventindex = None
                self.eventdescription = None
                self.eventtype = None
                self.eventcommunity = None
                self.eventlasttimesent = None
                self.eventowner = None
                self.eventstatus = None
                self._segment_path = lambda: "eventEntry" + "[eventIndex='" + str(self.eventindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/eventTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.EventTable.EventEntry, [u'eventindex', u'eventdescription', u'eventtype', u'eventcommunity', u'eventlasttimesent', u'eventowner', u'eventstatus'], name, value)

            class EventType(Enum):
                """
                EventType (Enum Class)

                The type of notification that the probe will make

                about this event.  In the case of log, an entry is

                made in the log table for each event.  In the case of

                snmp\-trap, an SNMP trap is sent to one or more

                management stations.

                .. data:: none = 1

                .. data:: log = 2

                .. data:: snmptrap = 3

                .. data:: logandtrap = 4

                """

                none = Enum.YLeaf(1, "none")

                log = Enum.YLeaf(2, "log")

                snmptrap = Enum.YLeaf(3, "snmptrap")

                logandtrap = Enum.YLeaf(4, "logandtrap")





    class LogTable(Entity):
        """
        A list of events that have been logged.
        
        .. attribute:: logentry
        
        	A set of data describing an event that has been logged.  For example, an instance of the logDescription object might be named logDescription.6.47
        	**type**\: list of  		 :py:class:`LogEntry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.LogTable.LogEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.LogTable, self).__init__()

            self.yang_name = "logTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("logEntry", ("logentry", RMONMIB.LogTable.LogEntry))])
            self._leafs = OrderedDict()

            self.logentry = YList(self)
            self._segment_path = lambda: "logTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.LogTable, [], name, value)


        class LogEntry(Entity):
            """
            A set of data describing an event that has been
            logged.  For example, an instance of the logDescription
            object might be named logDescription.6.47
            
            .. attribute:: logeventindex  (key)
            
            	The event entry that generated this log entry.  The log identified by a particular value of this index is associated with the same eventEntry as identified by the same value of eventIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: logindex  (key)
            
            	An index that uniquely identifies an entry in the log table amongst those generated by the same eventEntries.  These indexes are assigned beginning with 1 and increase by one with each new log entry.  The association between values of logIndex and logEntries is fixed for the lifetime of each logEntry. The agent may choose to delete the oldest instances of logEntry as required because of lack of memory.  It is an implementation\-specific matter as to when this deletion may occur
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: logtime
            
            	The value of sysUpTime when this log entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: logdescription
            
            	An implementation dependent description of the event that activated this log entry
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.LogTable.LogEntry, self).__init__()

                self.yang_name = "logEntry"
                self.yang_parent_name = "logTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['logeventindex','logindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('logeventindex', (YLeaf(YType.int32, 'logEventIndex'), ['int'])),
                    ('logindex', (YLeaf(YType.int32, 'logIndex'), ['int'])),
                    ('logtime', (YLeaf(YType.uint32, 'logTime'), ['int'])),
                    ('logdescription', (YLeaf(YType.str, 'logDescription'), ['str'])),
                ])
                self.logeventindex = None
                self.logindex = None
                self.logtime = None
                self.logdescription = None
                self._segment_path = lambda: "logEntry" + "[logEventIndex='" + str(self.logeventindex) + "']" + "[logIndex='" + str(self.logindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/logTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.LogTable.LogEntry, [u'logeventindex', u'logindex', u'logtime', u'logdescription'], name, value)



    def clone_ptr(self):
        self._top_entity = RMONMIB()
        return self._top_entity



