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



class Rmoneventsv2(Identity):
    """
    Definition point for RMON notifications.
    
    

    """

    _prefix = 'RMON-MIB'
    _revision = '2000-05-11'

    def __init__(self):
        super(Rmoneventsv2, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:RMON-MIB", "RMON-MIB", "RMON-MIB:rmonEventsV2")


class RMONMIB(Entity):
    """
    
    
    .. attribute:: etherstatstable
    
    	A list of Ethernet statistics entries
    	**type**\:  :py:class:`Etherstatstable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Etherstatstable>`
    
    .. attribute:: historycontroltable
    
    	A list of history control entries
    	**type**\:  :py:class:`Historycontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Historycontroltable>`
    
    .. attribute:: etherhistorytable
    
    	A list of Ethernet history entries
    	**type**\:  :py:class:`Etherhistorytable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Etherhistorytable>`
    
    .. attribute:: alarmtable
    
    	A list of alarm entries
    	**type**\:  :py:class:`Alarmtable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Alarmtable>`
    
    .. attribute:: hostcontroltable
    
    	A list of host table control entries
    	**type**\:  :py:class:`Hostcontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hostcontroltable>`
    
    .. attribute:: hosttable
    
    	A list of host entries
    	**type**\:  :py:class:`Hosttable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttable>`
    
    .. attribute:: hosttimetable
    
    	A list of time\-ordered host table entries
    	**type**\:  :py:class:`Hosttimetable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttimetable>`
    
    .. attribute:: hosttopncontroltable
    
    	A list of top N host control entries
    	**type**\:  :py:class:`Hosttopncontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttopncontroltable>`
    
    .. attribute:: hosttopntable
    
    	A list of top N host entries
    	**type**\:  :py:class:`Hosttopntable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttopntable>`
    
    .. attribute:: matrixcontroltable
    
    	A list of information entries for the traffic matrix on each interface
    	**type**\:  :py:class:`Matrixcontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixcontroltable>`
    
    .. attribute:: matrixsdtable
    
    	A list of traffic matrix entries indexed by source and destination MAC address
    	**type**\:  :py:class:`Matrixsdtable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixsdtable>`
    
    .. attribute:: matrixdstable
    
    	A list of traffic matrix entries indexed by destination and source MAC address
    	**type**\:  :py:class:`Matrixdstable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixdstable>`
    
    .. attribute:: filtertable
    
    	A list of packet filter entries
    	**type**\:  :py:class:`Filtertable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Filtertable>`
    
    .. attribute:: channeltable
    
    	A list of packet channel entries
    	**type**\:  :py:class:`Channeltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Channeltable>`
    
    .. attribute:: buffercontroltable
    
    	A list of buffers control entries
    	**type**\:  :py:class:`Buffercontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Buffercontroltable>`
    
    .. attribute:: capturebuffertable
    
    	A list of packets captured off of a channel
    	**type**\:  :py:class:`Capturebuffertable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Capturebuffertable>`
    
    .. attribute:: eventtable
    
    	A list of events to be generated
    	**type**\:  :py:class:`Eventtable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Eventtable>`
    
    .. attribute:: logtable
    
    	A list of events that have been logged
    	**type**\:  :py:class:`Logtable <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Logtable>`
    
    

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
        self._child_container_classes = OrderedDict([("etherStatsTable", ("etherstatstable", RMONMIB.Etherstatstable)), ("historyControlTable", ("historycontroltable", RMONMIB.Historycontroltable)), ("etherHistoryTable", ("etherhistorytable", RMONMIB.Etherhistorytable)), ("alarmTable", ("alarmtable", RMONMIB.Alarmtable)), ("hostControlTable", ("hostcontroltable", RMONMIB.Hostcontroltable)), ("hostTable", ("hosttable", RMONMIB.Hosttable)), ("hostTimeTable", ("hosttimetable", RMONMIB.Hosttimetable)), ("hostTopNControlTable", ("hosttopncontroltable", RMONMIB.Hosttopncontroltable)), ("hostTopNTable", ("hosttopntable", RMONMIB.Hosttopntable)), ("matrixControlTable", ("matrixcontroltable", RMONMIB.Matrixcontroltable)), ("matrixSDTable", ("matrixsdtable", RMONMIB.Matrixsdtable)), ("matrixDSTable", ("matrixdstable", RMONMIB.Matrixdstable)), ("filterTable", ("filtertable", RMONMIB.Filtertable)), ("channelTable", ("channeltable", RMONMIB.Channeltable)), ("bufferControlTable", ("buffercontroltable", RMONMIB.Buffercontroltable)), ("captureBufferTable", ("capturebuffertable", RMONMIB.Capturebuffertable)), ("eventTable", ("eventtable", RMONMIB.Eventtable)), ("logTable", ("logtable", RMONMIB.Logtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.etherstatstable = RMONMIB.Etherstatstable()
        self.etherstatstable.parent = self
        self._children_name_map["etherstatstable"] = "etherStatsTable"
        self._children_yang_names.add("etherStatsTable")

        self.historycontroltable = RMONMIB.Historycontroltable()
        self.historycontroltable.parent = self
        self._children_name_map["historycontroltable"] = "historyControlTable"
        self._children_yang_names.add("historyControlTable")

        self.etherhistorytable = RMONMIB.Etherhistorytable()
        self.etherhistorytable.parent = self
        self._children_name_map["etherhistorytable"] = "etherHistoryTable"
        self._children_yang_names.add("etherHistoryTable")

        self.alarmtable = RMONMIB.Alarmtable()
        self.alarmtable.parent = self
        self._children_name_map["alarmtable"] = "alarmTable"
        self._children_yang_names.add("alarmTable")

        self.hostcontroltable = RMONMIB.Hostcontroltable()
        self.hostcontroltable.parent = self
        self._children_name_map["hostcontroltable"] = "hostControlTable"
        self._children_yang_names.add("hostControlTable")

        self.hosttable = RMONMIB.Hosttable()
        self.hosttable.parent = self
        self._children_name_map["hosttable"] = "hostTable"
        self._children_yang_names.add("hostTable")

        self.hosttimetable = RMONMIB.Hosttimetable()
        self.hosttimetable.parent = self
        self._children_name_map["hosttimetable"] = "hostTimeTable"
        self._children_yang_names.add("hostTimeTable")

        self.hosttopncontroltable = RMONMIB.Hosttopncontroltable()
        self.hosttopncontroltable.parent = self
        self._children_name_map["hosttopncontroltable"] = "hostTopNControlTable"
        self._children_yang_names.add("hostTopNControlTable")

        self.hosttopntable = RMONMIB.Hosttopntable()
        self.hosttopntable.parent = self
        self._children_name_map["hosttopntable"] = "hostTopNTable"
        self._children_yang_names.add("hostTopNTable")

        self.matrixcontroltable = RMONMIB.Matrixcontroltable()
        self.matrixcontroltable.parent = self
        self._children_name_map["matrixcontroltable"] = "matrixControlTable"
        self._children_yang_names.add("matrixControlTable")

        self.matrixsdtable = RMONMIB.Matrixsdtable()
        self.matrixsdtable.parent = self
        self._children_name_map["matrixsdtable"] = "matrixSDTable"
        self._children_yang_names.add("matrixSDTable")

        self.matrixdstable = RMONMIB.Matrixdstable()
        self.matrixdstable.parent = self
        self._children_name_map["matrixdstable"] = "matrixDSTable"
        self._children_yang_names.add("matrixDSTable")

        self.filtertable = RMONMIB.Filtertable()
        self.filtertable.parent = self
        self._children_name_map["filtertable"] = "filterTable"
        self._children_yang_names.add("filterTable")

        self.channeltable = RMONMIB.Channeltable()
        self.channeltable.parent = self
        self._children_name_map["channeltable"] = "channelTable"
        self._children_yang_names.add("channelTable")

        self.buffercontroltable = RMONMIB.Buffercontroltable()
        self.buffercontroltable.parent = self
        self._children_name_map["buffercontroltable"] = "bufferControlTable"
        self._children_yang_names.add("bufferControlTable")

        self.capturebuffertable = RMONMIB.Capturebuffertable()
        self.capturebuffertable.parent = self
        self._children_name_map["capturebuffertable"] = "captureBufferTable"
        self._children_yang_names.add("captureBufferTable")

        self.eventtable = RMONMIB.Eventtable()
        self.eventtable.parent = self
        self._children_name_map["eventtable"] = "eventTable"
        self._children_yang_names.add("eventTable")

        self.logtable = RMONMIB.Logtable()
        self.logtable.parent = self
        self._children_name_map["logtable"] = "logTable"
        self._children_yang_names.add("logTable")
        self._segment_path = lambda: "RMON-MIB:RMON-MIB"


    class Etherstatstable(Entity):
        """
        A list of Ethernet statistics entries.
        
        .. attribute:: etherstatsentry
        
        	A collection of statistics kept for a particular Ethernet interface.  As an example, an instance of the etherStatsPkts object might be named etherStatsPkts.1
        	**type**\: list of  		 :py:class:`Etherstatsentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Etherstatstable.Etherstatsentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Etherstatstable, self).__init__()

            self.yang_name = "etherStatsTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("etherStatsEntry", ("etherstatsentry", RMONMIB.Etherstatstable.Etherstatsentry))])
            self._leafs = OrderedDict()

            self.etherstatsentry = YList(self)
            self._segment_path = lambda: "etherStatsTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Etherstatstable, [], name, value)


        class Etherstatsentry(Entity):
            """
            A collection of statistics kept for a particular
            Ethernet interface.  As an example, an instance of the
            etherStatsPkts object might be named etherStatsPkts.1
            
            .. attribute:: etherstatsindex  (key)
            
            	The value of this object uniquely identifies this etherStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: etherstatsdatasource
            
            	This object identifies the source of the data that this etherStats entry is configured to analyze.  This source can be any ethernet interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated etherStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: etherstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets). This object can be used as a reasonable estimate of 10\-Megabit ethernet utilization.  If greater precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval.  The differences in the sampled values are Pkts and Octets, respectively, and the number of seconds in the interval is Interval.  These values are used to calculate the Utilization as follows\:                   Pkts \* (9.6 + 6.4) + (Octets \* .8)  Utilization = \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-                          Interval \* 10,000  The result of this equation is the value Utilization which is the percent utilization of the ethernet segment on a scale of 0 to 100 percent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: etherstatspkts
            
            	The total number of packets (including bad packets, broadcast packets, and multicast packets) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsbroadcastpkts
            
            	The total number of good packets received that were directed to the broadcast address.  Note that this does not include multicast packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsmulticastpkts
            
            	The total number of good packets received that were directed to a multicast address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatscrcalignerrors
            
            	The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsundersizepkts
            
            	The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsoversizepkts
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsfragments
            
            	The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherStatsFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsjabbers
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatscollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Collisions
            
            .. attribute:: etherstatspkts64octets
            
            	The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts65to127octets
            
            	The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts128to255octets
            
            	The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts256to511octets
            
            	The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts512to1023octets
            
            	The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts1024to1518octets
            
            	The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: etherstatsstatus
            
            	The status of this etherStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: etherstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Etherstatstable.Etherstatsentry, self).__init__()

                self.yang_name = "etherStatsEntry"
                self.yang_parent_name = "etherStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['etherstatsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('etherstatsindex', YLeaf(YType.int32, 'etherStatsIndex')),
                    ('etherstatsdatasource', YLeaf(YType.str, 'etherStatsDataSource')),
                    ('etherstatsdropevents', YLeaf(YType.uint32, 'etherStatsDropEvents')),
                    ('etherstatsoctets', YLeaf(YType.uint32, 'etherStatsOctets')),
                    ('etherstatspkts', YLeaf(YType.uint32, 'etherStatsPkts')),
                    ('etherstatsbroadcastpkts', YLeaf(YType.uint32, 'etherStatsBroadcastPkts')),
                    ('etherstatsmulticastpkts', YLeaf(YType.uint32, 'etherStatsMulticastPkts')),
                    ('etherstatscrcalignerrors', YLeaf(YType.uint32, 'etherStatsCRCAlignErrors')),
                    ('etherstatsundersizepkts', YLeaf(YType.uint32, 'etherStatsUndersizePkts')),
                    ('etherstatsoversizepkts', YLeaf(YType.uint32, 'etherStatsOversizePkts')),
                    ('etherstatsfragments', YLeaf(YType.uint32, 'etherStatsFragments')),
                    ('etherstatsjabbers', YLeaf(YType.uint32, 'etherStatsJabbers')),
                    ('etherstatscollisions', YLeaf(YType.uint32, 'etherStatsCollisions')),
                    ('etherstatspkts64octets', YLeaf(YType.uint32, 'etherStatsPkts64Octets')),
                    ('etherstatspkts65to127octets', YLeaf(YType.uint32, 'etherStatsPkts65to127Octets')),
                    ('etherstatspkts128to255octets', YLeaf(YType.uint32, 'etherStatsPkts128to255Octets')),
                    ('etherstatspkts256to511octets', YLeaf(YType.uint32, 'etherStatsPkts256to511Octets')),
                    ('etherstatspkts512to1023octets', YLeaf(YType.uint32, 'etherStatsPkts512to1023Octets')),
                    ('etherstatspkts1024to1518octets', YLeaf(YType.uint32, 'etherStatsPkts1024to1518Octets')),
                    ('etherstatsowner', YLeaf(YType.str, 'etherStatsOwner')),
                    ('etherstatsstatus', YLeaf(YType.enumeration, 'etherStatsStatus')),
                    ('etherstatsdroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:etherStatsDroppedFrames')),
                    ('etherstatscreatetime', YLeaf(YType.uint32, 'RMON2-MIB:etherStatsCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Etherstatstable.Etherstatsentry, ['etherstatsindex', 'etherstatsdatasource', 'etherstatsdropevents', 'etherstatsoctets', 'etherstatspkts', 'etherstatsbroadcastpkts', 'etherstatsmulticastpkts', 'etherstatscrcalignerrors', 'etherstatsundersizepkts', 'etherstatsoversizepkts', 'etherstatsfragments', 'etherstatsjabbers', 'etherstatscollisions', 'etherstatspkts64octets', 'etherstatspkts65to127octets', 'etherstatspkts128to255octets', 'etherstatspkts256to511octets', 'etherstatspkts512to1023octets', 'etherstatspkts1024to1518octets', 'etherstatsowner', 'etherstatsstatus', 'etherstatsdroppedframes', 'etherstatscreatetime'], name, value)


    class Historycontroltable(Entity):
        """
        A list of history control entries.
        
        .. attribute:: historycontrolentry
        
        	A list of parameters that set up a periodic sampling of statistics.  As an example, an instance of the historyControlInterval object might be named historyControlInterval.2
        	**type**\: list of  		 :py:class:`Historycontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Historycontroltable.Historycontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Historycontroltable, self).__init__()

            self.yang_name = "historyControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("historyControlEntry", ("historycontrolentry", RMONMIB.Historycontroltable.Historycontrolentry))])
            self._leafs = OrderedDict()

            self.historycontrolentry = YList(self)
            self._segment_path = lambda: "historyControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Historycontroltable, [], name, value)


        class Historycontrolentry(Entity):
            """
            A list of parameters that set up a periodic sampling of
            statistics.  As an example, an instance of the
            historyControlInterval object might be named
            historyControlInterval.2
            
            .. attribute:: historycontrolindex  (key)
            
            	An index that uniquely identifies an entry in the historyControl table.  Each such entry defines a set of samples at a particular interval for an interface on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontroldatasource
            
            	This object identifies the source of the data for which historical data was collected and placed in a media\-specific table on behalf of this historyControlEntry.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in  RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: historycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the media\-specific table associated with this historyControlEntry.  When this object is created or modified, the probe should set historyControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the media\-specific table associated with this historyControlEntry. When the associated historyControlBucketsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated historyControlBucketsRequested object.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the media\-specific table.  When the number of buckets reaches the value of this object and a new bucket is to be added to the media\-specific table, the oldest bucket associated with this historyControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the media\-specific table associated with this historyControlEntry.  Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated media\- specific entries may be allowed to grow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the media\-specific table associated with this historyControlEntry.  This interval can be set to any number of seconds between 1 and 3600 (1 hour).  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of the associated counters.  It is important to consider the minimum time in which any counter could overflow on a particular media type and set the historyControlInterval object to a value less than this interval.  This is typically most important for the 'octets' counter in any media\-specific table.  For example, on an Ethernet network, the etherHistoryOctets counter could overflow in about one hour at the Ethernet's maximum utilization.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..3600
            
            	**units**\: Seconds
            
            .. attribute:: historycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: historycontrolstatus
            
            	The status of this historyControl entry.  Each instance of the media\-specific table associated with this historyControlEntry will be deleted by the agent if this historyControlEntry is not equal to valid(1)
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: historycontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this      collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Historycontroltable.Historycontrolentry, self).__init__()

                self.yang_name = "historyControlEntry"
                self.yang_parent_name = "historyControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['historycontrolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('historycontrolindex', YLeaf(YType.int32, 'historyControlIndex')),
                    ('historycontroldatasource', YLeaf(YType.str, 'historyControlDataSource')),
                    ('historycontrolbucketsrequested', YLeaf(YType.int32, 'historyControlBucketsRequested')),
                    ('historycontrolbucketsgranted', YLeaf(YType.int32, 'historyControlBucketsGranted')),
                    ('historycontrolinterval', YLeaf(YType.int32, 'historyControlInterval')),
                    ('historycontrolowner', YLeaf(YType.str, 'historyControlOwner')),
                    ('historycontrolstatus', YLeaf(YType.enumeration, 'historyControlStatus')),
                    ('historycontroldroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:historyControlDroppedFrames')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Historycontroltable.Historycontrolentry, ['historycontrolindex', 'historycontroldatasource', 'historycontrolbucketsrequested', 'historycontrolbucketsgranted', 'historycontrolinterval', 'historycontrolowner', 'historycontrolstatus', 'historycontroldroppedframes'], name, value)


    class Etherhistorytable(Entity):
        """
        A list of Ethernet history entries.
        
        .. attribute:: etherhistoryentry
        
        	An historical sample of Ethernet statistics on a particular Ethernet interface.  This sample is associated with the historyControlEntry which set up the parameters for a regular collection of these samples.  As an example, an instance of the etherHistoryPkts object might be named etherHistoryPkts.2.89
        	**type**\: list of  		 :py:class:`Etherhistoryentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Etherhistorytable.Etherhistoryentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Etherhistorytable, self).__init__()

            self.yang_name = "etherHistoryTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("etherHistoryEntry", ("etherhistoryentry", RMONMIB.Etherhistorytable.Etherhistoryentry))])
            self._leafs = OrderedDict()

            self.etherhistoryentry = YList(self)
            self._segment_path = lambda: "etherHistoryTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Etherhistorytable, [], name, value)


        class Etherhistoryentry(Entity):
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
            
            .. attribute:: etherhistorysampleindex  (key)
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: etherhistorypkts
            
            	The number of packets (including bad packets) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorybroadcastpkts
            
            	The number of good packets received during this sampling interval that were directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorymulticastpkts
            
            	The number of good packets received during this sampling interval that were directed to a multicast address.  Note that this number does not include packets addressed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorycrcalignerrors
            
            	The number of packets received during this sampling interval that had a length (excluding framing bits but including FCS octets) between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryundersizepkts
            
            	The number of packets received during this sampling interval that were less than 64 octets long (excluding framing bits but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryoversizepkts
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets) but were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryfragments
            
            	The total number of packets received during this sampling interval that were less than 64 octets in length (excluding framing bits but including FCS octets) had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherHistoryFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryjabbers
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets), and  had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorycollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment during this sampling interval.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Collisions
            
            .. attribute:: etherhistoryutilization
            
            	The best estimate of the mean physical layer network utilization on this interface during this sampling interval, in hundredths of a percent
            	**type**\: int
            
            	**range:** 0..10000
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Etherhistorytable.Etherhistoryentry, self).__init__()

                self.yang_name = "etherHistoryEntry"
                self.yang_parent_name = "etherHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['etherhistoryindex','etherhistorysampleindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('etherhistoryindex', YLeaf(YType.int32, 'etherHistoryIndex')),
                    ('etherhistorysampleindex', YLeaf(YType.int32, 'etherHistorySampleIndex')),
                    ('etherhistoryintervalstart', YLeaf(YType.uint32, 'etherHistoryIntervalStart')),
                    ('etherhistorydropevents', YLeaf(YType.uint32, 'etherHistoryDropEvents')),
                    ('etherhistoryoctets', YLeaf(YType.uint32, 'etherHistoryOctets')),
                    ('etherhistorypkts', YLeaf(YType.uint32, 'etherHistoryPkts')),
                    ('etherhistorybroadcastpkts', YLeaf(YType.uint32, 'etherHistoryBroadcastPkts')),
                    ('etherhistorymulticastpkts', YLeaf(YType.uint32, 'etherHistoryMulticastPkts')),
                    ('etherhistorycrcalignerrors', YLeaf(YType.uint32, 'etherHistoryCRCAlignErrors')),
                    ('etherhistoryundersizepkts', YLeaf(YType.uint32, 'etherHistoryUndersizePkts')),
                    ('etherhistoryoversizepkts', YLeaf(YType.uint32, 'etherHistoryOversizePkts')),
                    ('etherhistoryfragments', YLeaf(YType.uint32, 'etherHistoryFragments')),
                    ('etherhistoryjabbers', YLeaf(YType.uint32, 'etherHistoryJabbers')),
                    ('etherhistorycollisions', YLeaf(YType.uint32, 'etherHistoryCollisions')),
                    ('etherhistoryutilization', YLeaf(YType.int32, 'etherHistoryUtilization')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Etherhistorytable.Etherhistoryentry, ['etherhistoryindex', 'etherhistorysampleindex', 'etherhistoryintervalstart', 'etherhistorydropevents', 'etherhistoryoctets', 'etherhistorypkts', 'etherhistorybroadcastpkts', 'etherhistorymulticastpkts', 'etherhistorycrcalignerrors', 'etherhistoryundersizepkts', 'etherhistoryoversizepkts', 'etherhistoryfragments', 'etherhistoryjabbers', 'etherhistorycollisions', 'etherhistoryutilization'], name, value)


    class Alarmtable(Entity):
        """
        A list of alarm entries.
        
        .. attribute:: alarmentry
        
        	A list of parameters that set up a periodic checking for alarm conditions.  For example, an instance of the alarmValue object might be named alarmValue.8
        	**type**\: list of  		 :py:class:`Alarmentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Alarmtable.Alarmentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Alarmtable, self).__init__()

            self.yang_name = "alarmTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("alarmEntry", ("alarmentry", RMONMIB.Alarmtable.Alarmentry))])
            self._leafs = OrderedDict()

            self.alarmentry = YList(self)
            self._segment_path = lambda: "alarmTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Alarmtable, [], name, value)


        class Alarmentry(Entity):
            """
            A list of parameters that set up a periodic checking
            for alarm conditions.  For example, an instance of the
            alarmValue object might be named alarmValue.8
            
            .. attribute:: alarmindex  (key)
            
            	An index that uniquely identifies an entry in the alarm table.  Each such entry defines a diagnostic sample at a particular interval for an object on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: alarminterval
            
            	The interval in seconds over which the data is sampled and compared with the rising and falling thresholds.  When setting this variable, care should be taken in the case of deltaValue sampling \- the interval should be set short enough that the sampled variable is very unlikely to increase or decrease by more than 2^31 \- 1 during a single sampling interval.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: alarmvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view.  Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  If at any time the variable name of an established alarmEntry is no longer available in the selected MIB view, the probe must change the status of this alarmEntry to invalid(4).  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: alarmsampletype
            
            	The method of sampling the selected variable and calculating the value to be compared against the thresholds.  If the value of this object is absoluteValue(1), the value of the selected variable will be compared directly with the thresholds at the end of the sampling interval.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference compared with the thresholds.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  :py:class:`Alarmsampletype <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Alarmtable.Alarmentry.Alarmsampletype>`
            
            .. attribute:: alarmvalue
            
            	The value of the statistic during the last sampling period.  For example, if the sample type is deltaValue, this value will be the difference between the samples at the beginning and end of the period.  If the sample type is absoluteValue, this value will be the sampled value at the end of the period. This is the value that is compared with the rising and falling thresholds.  The value during the current sampling period is not made available until the period is completed and will remain available until the next period completes
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmstartupalarm
            
            	The alarm that may be sent when this entry is first set to valid.  If the first sample after this entry becomes valid is greater than or equal to the risingThreshold and alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single rising alarm will be generated.  If the first sample after this entry becomes valid is less than or equal to the fallingThreshold and alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single falling alarm will be generated.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  :py:class:`Alarmstartupalarm <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Alarmtable.Alarmentry.Alarmstartupalarm>`
            
            .. attribute:: alarmrisingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is greater than or equal to this threshold and the associated alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3).  After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the alarmFallingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmfallingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is less than or equal to this threshold and the associated alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3).  After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the alarmRisingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmrisingeventindex
            
            	The index of the eventEntry that is used when a rising threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: alarmfallingeventindex
            
            	The index of the eventEntry that is used when a falling threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: alarmowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: alarmstatus
            
            	The status of this alarm entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Alarmtable.Alarmentry, self).__init__()

                self.yang_name = "alarmEntry"
                self.yang_parent_name = "alarmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['alarmindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('alarmindex', YLeaf(YType.int32, 'alarmIndex')),
                    ('alarminterval', YLeaf(YType.int32, 'alarmInterval')),
                    ('alarmvariable', YLeaf(YType.str, 'alarmVariable')),
                    ('alarmsampletype', YLeaf(YType.enumeration, 'alarmSampleType')),
                    ('alarmvalue', YLeaf(YType.int32, 'alarmValue')),
                    ('alarmstartupalarm', YLeaf(YType.enumeration, 'alarmStartupAlarm')),
                    ('alarmrisingthreshold', YLeaf(YType.int32, 'alarmRisingThreshold')),
                    ('alarmfallingthreshold', YLeaf(YType.int32, 'alarmFallingThreshold')),
                    ('alarmrisingeventindex', YLeaf(YType.int32, 'alarmRisingEventIndex')),
                    ('alarmfallingeventindex', YLeaf(YType.int32, 'alarmFallingEventIndex')),
                    ('alarmowner', YLeaf(YType.str, 'alarmOwner')),
                    ('alarmstatus', YLeaf(YType.enumeration, 'alarmStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Alarmtable.Alarmentry, ['alarmindex', 'alarminterval', 'alarmvariable', 'alarmsampletype', 'alarmvalue', 'alarmstartupalarm', 'alarmrisingthreshold', 'alarmfallingthreshold', 'alarmrisingeventindex', 'alarmfallingeventindex', 'alarmowner', 'alarmstatus'], name, value)

            class Alarmsampletype(Enum):
                """
                Alarmsampletype (Enum Class)

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


            class Alarmstartupalarm(Enum):
                """
                Alarmstartupalarm (Enum Class)

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



    class Hostcontroltable(Entity):
        """
        A list of host table control entries.
        
        .. attribute:: hostcontrolentry
        
        	A list of parameters that set up the discovery of hosts on a particular interface and the collection of statistics about these hosts.  For example, an instance of the hostControlTableSize object might be named hostControlTableSize.1
        	**type**\: list of  		 :py:class:`Hostcontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hostcontroltable.Hostcontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Hostcontroltable, self).__init__()

            self.yang_name = "hostControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("hostControlEntry", ("hostcontrolentry", RMONMIB.Hostcontroltable.Hostcontrolentry))])
            self._leafs = OrderedDict()

            self.hostcontrolentry = YList(self)
            self._segment_path = lambda: "hostControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Hostcontroltable, [], name, value)


        class Hostcontrolentry(Entity):
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
            
            .. attribute:: hostcontroldatasource
            
            	This object identifies the source of the data for this instance of the host function.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated hostControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hostcontroltablesize
            
            	The number of hostEntries in the hostTable and the hostTimeTable associated with this hostControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hostcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the hostTable associated with this hostControlEntry.  If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: hostcontrolstatus
            
            	The status of this hostControl entry.  If this object is not equal to valid(1), all associated entries in the hostTable, hostTimeTable, and the hostTopNTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: hostcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Hostcontroltable.Hostcontrolentry, self).__init__()

                self.yang_name = "hostControlEntry"
                self.yang_parent_name = "hostControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hostcontrolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hostcontrolindex', YLeaf(YType.int32, 'hostControlIndex')),
                    ('hostcontroldatasource', YLeaf(YType.str, 'hostControlDataSource')),
                    ('hostcontroltablesize', YLeaf(YType.int32, 'hostControlTableSize')),
                    ('hostcontrollastdeletetime', YLeaf(YType.uint32, 'hostControlLastDeleteTime')),
                    ('hostcontrolowner', YLeaf(YType.str, 'hostControlOwner')),
                    ('hostcontrolstatus', YLeaf(YType.enumeration, 'hostControlStatus')),
                    ('hostcontroldroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:hostControlDroppedFrames')),
                    ('hostcontrolcreatetime', YLeaf(YType.uint32, 'RMON2-MIB:hostControlCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Hostcontroltable.Hostcontrolentry, ['hostcontrolindex', 'hostcontroldatasource', 'hostcontroltablesize', 'hostcontrollastdeletetime', 'hostcontrolowner', 'hostcontrolstatus', 'hostcontroldroppedframes', 'hostcontrolcreatetime'], name, value)


    class Hosttable(Entity):
        """
        A list of host entries.
        
        .. attribute:: hostentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  For example, an instance of the hostOutBroadcastPkts object might be named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
        	**type**\: list of  		 :py:class:`Hostentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttable.Hostentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Hosttable, self).__init__()

            self.yang_name = "hostTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("hostEntry", ("hostentry", RMONMIB.Hosttable.Hostentry))])
            self._leafs = OrderedDict()

            self.hostentry = YList(self)
            self._segment_path = lambda: "hostTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Hosttable, [], name, value)


        class Hostentry(Entity):
            """
            A collection of statistics for a particular host that has
            been discovered on an interface of this device.  For example,
            an instance of the hostOutBroadcastPkts object might be
            named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
            
            .. attribute:: hostindex  (key)
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hostaddress  (key)
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hostcreationorder
            
            	An index that defines the relative ordering of the creation time of hosts captured for a particular hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later.  It is important to note that the order for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTable.  By observing this variable, the management station may detect the circumstances where a previous association between a value of hostCreationOrder and a hostEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hostinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hostoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hostouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Hosttable.Hostentry, self).__init__()

                self.yang_name = "hostEntry"
                self.yang_parent_name = "hostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hostindex','hostaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hostindex', YLeaf(YType.int32, 'hostIndex')),
                    ('hostaddress', YLeaf(YType.str, 'hostAddress')),
                    ('hostcreationorder', YLeaf(YType.int32, 'hostCreationOrder')),
                    ('hostinpkts', YLeaf(YType.uint32, 'hostInPkts')),
                    ('hostoutpkts', YLeaf(YType.uint32, 'hostOutPkts')),
                    ('hostinoctets', YLeaf(YType.uint32, 'hostInOctets')),
                    ('hostoutoctets', YLeaf(YType.uint32, 'hostOutOctets')),
                    ('hostouterrors', YLeaf(YType.uint32, 'hostOutErrors')),
                    ('hostoutbroadcastpkts', YLeaf(YType.uint32, 'hostOutBroadcastPkts')),
                    ('hostoutmulticastpkts', YLeaf(YType.uint32, 'hostOutMulticastPkts')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Hosttable.Hostentry, ['hostindex', 'hostaddress', 'hostcreationorder', 'hostinpkts', 'hostoutpkts', 'hostinoctets', 'hostoutoctets', 'hostouterrors', 'hostoutbroadcastpkts', 'hostoutmulticastpkts'], name, value)


    class Hosttimetable(Entity):
        """
        A list of time\-ordered host table entries.
        
        .. attribute:: hosttimeentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  This collection includes the relative ordering of the creation time of this object.  For example, an instance of the hostTimeOutBroadcastPkts object might be named hostTimeOutBroadcastPkts.1.687
        	**type**\: list of  		 :py:class:`Hosttimeentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttimetable.Hosttimeentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Hosttimetable, self).__init__()

            self.yang_name = "hostTimeTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("hostTimeEntry", ("hosttimeentry", RMONMIB.Hosttimetable.Hosttimeentry))])
            self._leafs = OrderedDict()

            self.hosttimeentry = YList(self)
            self._segment_path = lambda: "hostTimeTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Hosttimetable, [], name, value)


        class Hosttimeentry(Entity):
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
            
            .. attribute:: hosttimecreationorder  (key)
            
            	An index that uniquely identifies an entry in the hostTime table among those entries associated with the same hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later. Thus the management station has the ability to learn of new entries added to this table without downloading the entire table.  It is important to note that the index for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTimeTable.  By observing this variable, the management station may detect the circumstances where a download of the table may have missed entries, and where a previous association between a value of hostTimeCreationOrder and a hostTimeEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttimeaddress
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hosttimeinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hosttimeoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hosttimeouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTimeTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Hosttimetable.Hosttimeentry, self).__init__()

                self.yang_name = "hostTimeEntry"
                self.yang_parent_name = "hostTimeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttimeindex','hosttimecreationorder']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttimeindex', YLeaf(YType.int32, 'hostTimeIndex')),
                    ('hosttimecreationorder', YLeaf(YType.int32, 'hostTimeCreationOrder')),
                    ('hosttimeaddress', YLeaf(YType.str, 'hostTimeAddress')),
                    ('hosttimeinpkts', YLeaf(YType.uint32, 'hostTimeInPkts')),
                    ('hosttimeoutpkts', YLeaf(YType.uint32, 'hostTimeOutPkts')),
                    ('hosttimeinoctets', YLeaf(YType.uint32, 'hostTimeInOctets')),
                    ('hosttimeoutoctets', YLeaf(YType.uint32, 'hostTimeOutOctets')),
                    ('hosttimeouterrors', YLeaf(YType.uint32, 'hostTimeOutErrors')),
                    ('hosttimeoutbroadcastpkts', YLeaf(YType.uint32, 'hostTimeOutBroadcastPkts')),
                    ('hosttimeoutmulticastpkts', YLeaf(YType.uint32, 'hostTimeOutMulticastPkts')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Hosttimetable.Hosttimeentry, ['hosttimeindex', 'hosttimecreationorder', 'hosttimeaddress', 'hosttimeinpkts', 'hosttimeoutpkts', 'hosttimeinoctets', 'hosttimeoutoctets', 'hosttimeouterrors', 'hosttimeoutbroadcastpkts', 'hosttimeoutmulticastpkts'], name, value)


    class Hosttopncontroltable(Entity):
        """
        A list of top N host control entries.
        
        .. attribute:: hosttopncontrolentry
        
        	A set of parameters that control the creation of a report of the top N hosts according to several metrics.  For example, an instance of the hostTopNDuration object might be named hostTopNDuration.3
        	**type**\: list of  		 :py:class:`Hosttopncontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttopncontroltable.Hosttopncontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Hosttopncontroltable, self).__init__()

            self.yang_name = "hostTopNControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("hostTopNControlEntry", ("hosttopncontrolentry", RMONMIB.Hosttopncontroltable.Hosttopncontrolentry))])
            self._leafs = OrderedDict()

            self.hosttopncontrolentry = YList(self)
            self._segment_path = lambda: "hostTopNControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Hosttopncontroltable, [], name, value)


        class Hosttopncontrolentry(Entity):
            """
            A set of parameters that control the creation of a report
            of the top N hosts according to several metrics.  For
            example, an instance of the hostTopNDuration object might
            be named hostTopNDuration.3
            
            .. attribute:: hosttopncontrolindex  (key)
            
            	An index that uniquely identifies an entry in the hostTopNControl table.  Each such entry defines one top N report prepared for one interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnhostindex
            
            	The host table for which a top N report will be prepared on behalf of this entry.  The host table identified by a particular value of this index is associated with the same host table as identified by the same value of hostIndex.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnratebase
            
            	The variable for each host that the hostTopNRate variable is based upon.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\:  :py:class:`Hosttopnratebase <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttopncontroltable.Hosttopncontrolentry.Hosttopnratebase>`
            
            .. attribute:: hosttopntimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, which is loaded into the associated hostTopNDuration object.  When this object is set to a non\-zero value, any associated hostTopNEntries shall be made inaccessible by the monitor.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  During this time, all associated hostTopNEntries shall remain inaccessible.  At the time that this object decrements to zero, the report is made accessible in the hostTopNTable.  Thus, the hostTopN table needs to be created only at the end of the collection interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: hosttopnduration
            
            	The number of seconds that this report has collected during the last sampling interval, or if this report is currently being collected, the number of seconds that this report is being collected during this sampling interval.  When the associated hostTopNTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the hostTopNTimeRemaining is set.  This value shall be zero if no reports have been requested for this hostTopNControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: hosttopnrequestedsize
            
            	The maximum number of hosts requested for the top N table.  When this object is created or modified, the probe should set hostTopNGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopngrantedsize
            
            	The maximum number of hosts in the top N table.  When the associated hostTopNRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated hostTopNRequestedSize object.  Hosts with the highest value of hostTopNRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more hosts
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopnstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated hostTopNTimeRemaining object was modified to start the requested report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttopnowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: hosttopnstatus
            
            	The status of this hostTopNControl entry.  If this object is not equal to valid(1), all associated hostTopNEntries shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Hosttopncontroltable.Hosttopncontrolentry, self).__init__()

                self.yang_name = "hostTopNControlEntry"
                self.yang_parent_name = "hostTopNControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttopncontrolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttopncontrolindex', YLeaf(YType.int32, 'hostTopNControlIndex')),
                    ('hosttopnhostindex', YLeaf(YType.int32, 'hostTopNHostIndex')),
                    ('hosttopnratebase', YLeaf(YType.enumeration, 'hostTopNRateBase')),
                    ('hosttopntimeremaining', YLeaf(YType.int32, 'hostTopNTimeRemaining')),
                    ('hosttopnduration', YLeaf(YType.int32, 'hostTopNDuration')),
                    ('hosttopnrequestedsize', YLeaf(YType.int32, 'hostTopNRequestedSize')),
                    ('hosttopngrantedsize', YLeaf(YType.int32, 'hostTopNGrantedSize')),
                    ('hosttopnstarttime', YLeaf(YType.uint32, 'hostTopNStartTime')),
                    ('hosttopnowner', YLeaf(YType.str, 'hostTopNOwner')),
                    ('hosttopnstatus', YLeaf(YType.enumeration, 'hostTopNStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Hosttopncontroltable.Hosttopncontrolentry, ['hosttopncontrolindex', 'hosttopnhostindex', 'hosttopnratebase', 'hosttopntimeremaining', 'hosttopnduration', 'hosttopnrequestedsize', 'hosttopngrantedsize', 'hosttopnstarttime', 'hosttopnowner', 'hosttopnstatus'], name, value)

            class Hosttopnratebase(Enum):
                """
                Hosttopnratebase (Enum Class)

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



    class Hosttopntable(Entity):
        """
        A list of top N host entries.
        
        .. attribute:: hosttopnentry
        
        	A set of statistics for a host that is part of a top N report.  For example, an instance of the hostTopNRate object might be named hostTopNRate.3.10
        	**type**\: list of  		 :py:class:`Hosttopnentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Hosttopntable.Hosttopnentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Hosttopntable, self).__init__()

            self.yang_name = "hostTopNTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("hostTopNEntry", ("hosttopnentry", RMONMIB.Hosttopntable.Hosttopnentry))])
            self._leafs = OrderedDict()

            self.hosttopnentry = YList(self)
            self._segment_path = lambda: "hostTopNTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Hosttopntable, [], name, value)


        class Hosttopnentry(Entity):
            """
            A set of statistics for a host that is part of a top N
            report.  For example, an instance of the hostTopNRate
            object might be named hostTopNRate.3.10
            
            .. attribute:: hosttopnreport  (key)
            
            	This object identifies the top N report of which this entry is a part.  The set of hosts identified by a particular value of this object is part of the same report as identified by the same value of the hostTopNControlIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnindex  (key)
            
            	An index that uniquely identifies an entry in the hostTopN table among those in the same report. This index is between 1 and N, where N is the number of entries in this table.  Increasing values of hostTopNIndex shall be assigned to entries with decreasing values of hostTopNRate until index N is assigned to the entry with the lowest value of hostTopNRate or there are no more hostTopNEntries
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnaddress
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hosttopnrate
            
            	The amount of change in the selected variable during this sampling interval.  The selected variable is this host's instance of the object selected by hostTopNRateBase
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Hosttopntable.Hosttopnentry, self).__init__()

                self.yang_name = "hostTopNEntry"
                self.yang_parent_name = "hostTopNTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hosttopnreport','hosttopnindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hosttopnreport', YLeaf(YType.int32, 'hostTopNReport')),
                    ('hosttopnindex', YLeaf(YType.int32, 'hostTopNIndex')),
                    ('hosttopnaddress', YLeaf(YType.str, 'hostTopNAddress')),
                    ('hosttopnrate', YLeaf(YType.int32, 'hostTopNRate')),
                ])
                self.hosttopnreport = None
                self.hosttopnindex = None
                self.hosttopnaddress = None
                self.hosttopnrate = None
                self._segment_path = lambda: "hostTopNEntry" + "[hostTopNReport='" + str(self.hosttopnreport) + "']" + "[hostTopNIndex='" + str(self.hosttopnindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/hostTopNTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Hosttopntable.Hosttopnentry, ['hosttopnreport', 'hosttopnindex', 'hosttopnaddress', 'hosttopnrate'], name, value)


    class Matrixcontroltable(Entity):
        """
        A list of information entries for the
        traffic matrix on each interface.
        
        .. attribute:: matrixcontrolentry
        
        	Information about a traffic matrix on a particular interface.  For example, an instance of the matrixControlLastDeleteTime object might be named matrixControlLastDeleteTime.1
        	**type**\: list of  		 :py:class:`Matrixcontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixcontroltable.Matrixcontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Matrixcontroltable, self).__init__()

            self.yang_name = "matrixControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("matrixControlEntry", ("matrixcontrolentry", RMONMIB.Matrixcontroltable.Matrixcontrolentry))])
            self._leafs = OrderedDict()

            self.matrixcontrolentry = YList(self)
            self._segment_path = lambda: "matrixControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Matrixcontroltable, [], name, value)


        class Matrixcontrolentry(Entity):
            """
            Information about a traffic matrix on a particular
            interface.  For example, an instance of the
            matrixControlLastDeleteTime object might be named
            matrixControlLastDeleteTime.1
            
            .. attribute:: matrixcontrolindex  (key)
            
            	An index that uniquely identifies an entry in the matrixControl table.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the matrixSDTable and the matrixDSTable on behalf of this matrixControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixcontroldatasource
            
            	This object identifies the source of the data from which this entry creates a traffic matrix. This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated matrixControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: matrixcontroltablesize
            
            	The number of matrixSDEntries in the matrixSDTable for this interface.  This must also be the value of the number of entries in the matrixDSTable for this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: matrixcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the matrixSDTable or matrixDSTable associated with this matrixControlEntry. If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: matrixcontrolstatus
            
            	The status of this matrixControl entry. If this object is not equal to valid(1), all associated entries in the matrixSDTable and the matrixDSTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: matrixcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Matrixcontroltable.Matrixcontrolentry, self).__init__()

                self.yang_name = "matrixControlEntry"
                self.yang_parent_name = "matrixControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixcontrolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixcontrolindex', YLeaf(YType.int32, 'matrixControlIndex')),
                    ('matrixcontroldatasource', YLeaf(YType.str, 'matrixControlDataSource')),
                    ('matrixcontroltablesize', YLeaf(YType.int32, 'matrixControlTableSize')),
                    ('matrixcontrollastdeletetime', YLeaf(YType.uint32, 'matrixControlLastDeleteTime')),
                    ('matrixcontrolowner', YLeaf(YType.str, 'matrixControlOwner')),
                    ('matrixcontrolstatus', YLeaf(YType.enumeration, 'matrixControlStatus')),
                    ('matrixcontroldroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:matrixControlDroppedFrames')),
                    ('matrixcontrolcreatetime', YLeaf(YType.uint32, 'RMON2-MIB:matrixControlCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Matrixcontroltable.Matrixcontrolentry, ['matrixcontrolindex', 'matrixcontroldatasource', 'matrixcontroltablesize', 'matrixcontrollastdeletetime', 'matrixcontrolowner', 'matrixcontrolstatus', 'matrixcontroldroppedframes', 'matrixcontrolcreatetime'], name, value)


    class Matrixsdtable(Entity):
        """
        A list of traffic matrix entries indexed by
        source and destination MAC address.
        
        .. attribute:: matrixsdentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
        	**type**\: list of  		 :py:class:`Matrixsdentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixsdtable.Matrixsdentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Matrixsdtable, self).__init__()

            self.yang_name = "matrixSDTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("matrixSDEntry", ("matrixsdentry", RMONMIB.Matrixsdtable.Matrixsdentry))])
            self._leafs = OrderedDict()

            self.matrixsdentry = YList(self)
            self._segment_path = lambda: "matrixSDTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Matrixsdtable, [], name, value)


        class Matrixsdentry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
            
            .. attribute:: matrixsdindex  (key)
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixsdsourceaddress  (key)
            
            	The source physical address
            	**type**\: str
            
            .. attribute:: matrixsddestaddress  (key)
            
            	The destination physical address
            	**type**\: str
            
            .. attribute:: matrixsdpkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: matrixsdoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: matrixsderrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Matrixsdtable.Matrixsdentry, self).__init__()

                self.yang_name = "matrixSDEntry"
                self.yang_parent_name = "matrixSDTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixsdindex','matrixsdsourceaddress','matrixsddestaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixsdindex', YLeaf(YType.int32, 'matrixSDIndex')),
                    ('matrixsdsourceaddress', YLeaf(YType.str, 'matrixSDSourceAddress')),
                    ('matrixsddestaddress', YLeaf(YType.str, 'matrixSDDestAddress')),
                    ('matrixsdpkts', YLeaf(YType.uint32, 'matrixSDPkts')),
                    ('matrixsdoctets', YLeaf(YType.uint32, 'matrixSDOctets')),
                    ('matrixsderrors', YLeaf(YType.uint32, 'matrixSDErrors')),
                ])
                self.matrixsdindex = None
                self.matrixsdsourceaddress = None
                self.matrixsddestaddress = None
                self.matrixsdpkts = None
                self.matrixsdoctets = None
                self.matrixsderrors = None
                self._segment_path = lambda: "matrixSDEntry" + "[matrixSDIndex='" + str(self.matrixsdindex) + "']" + "[matrixSDSourceAddress='" + str(self.matrixsdsourceaddress) + "']" + "[matrixSDDestAddress='" + str(self.matrixsddestaddress) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/matrixSDTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Matrixsdtable.Matrixsdentry, ['matrixsdindex', 'matrixsdsourceaddress', 'matrixsddestaddress', 'matrixsdpkts', 'matrixsdoctets', 'matrixsderrors'], name, value)


    class Matrixdstable(Entity):
        """
        A list of traffic matrix entries indexed by
        destination and source MAC address.
        
        .. attribute:: matrixdsentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
        	**type**\: list of  		 :py:class:`Matrixdsentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Matrixdstable.Matrixdsentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Matrixdstable, self).__init__()

            self.yang_name = "matrixDSTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("matrixDSEntry", ("matrixdsentry", RMONMIB.Matrixdstable.Matrixdsentry))])
            self._leafs = OrderedDict()

            self.matrixdsentry = YList(self)
            self._segment_path = lambda: "matrixDSTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Matrixdstable, [], name, value)


        class Matrixdsentry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
            
            .. attribute:: matrixdsindex  (key)
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixdsdestaddress  (key)
            
            	The destination physical address
            	**type**\: str
            
            .. attribute:: matrixdssourceaddress  (key)
            
            	The source physical address
            	**type**\: str
            
            .. attribute:: matrixdspkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: matrixdsoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: matrixdserrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Matrixdstable.Matrixdsentry, self).__init__()

                self.yang_name = "matrixDSEntry"
                self.yang_parent_name = "matrixDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['matrixdsindex','matrixdsdestaddress','matrixdssourceaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('matrixdsindex', YLeaf(YType.int32, 'matrixDSIndex')),
                    ('matrixdsdestaddress', YLeaf(YType.str, 'matrixDSDestAddress')),
                    ('matrixdssourceaddress', YLeaf(YType.str, 'matrixDSSourceAddress')),
                    ('matrixdspkts', YLeaf(YType.uint32, 'matrixDSPkts')),
                    ('matrixdsoctets', YLeaf(YType.uint32, 'matrixDSOctets')),
                    ('matrixdserrors', YLeaf(YType.uint32, 'matrixDSErrors')),
                ])
                self.matrixdsindex = None
                self.matrixdsdestaddress = None
                self.matrixdssourceaddress = None
                self.matrixdspkts = None
                self.matrixdsoctets = None
                self.matrixdserrors = None
                self._segment_path = lambda: "matrixDSEntry" + "[matrixDSIndex='" + str(self.matrixdsindex) + "']" + "[matrixDSDestAddress='" + str(self.matrixdsdestaddress) + "']" + "[matrixDSSourceAddress='" + str(self.matrixdssourceaddress) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/matrixDSTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Matrixdstable.Matrixdsentry, ['matrixdsindex', 'matrixdsdestaddress', 'matrixdssourceaddress', 'matrixdspkts', 'matrixdsoctets', 'matrixdserrors'], name, value)


    class Filtertable(Entity):
        """
        A list of packet filter entries.
        
        .. attribute:: filterentry
        
        	A set of parameters for a packet filter applied on a particular interface.  As an example, an instance of the filterPktData object might be named filterPktData.12
        	**type**\: list of  		 :py:class:`Filterentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Filtertable.Filterentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Filtertable, self).__init__()

            self.yang_name = "filterTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("filterEntry", ("filterentry", RMONMIB.Filtertable.Filterentry))])
            self._leafs = OrderedDict()

            self.filterentry = YList(self)
            self._segment_path = lambda: "filterTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Filtertable, [], name, value)


        class Filterentry(Entity):
            """
            A set of parameters for a packet filter applied on a
            particular interface.  As an example, an instance of the
            filterPktData object might be named filterPktData.12
            
            .. attribute:: filterindex  (key)
            
            	An index that uniquely identifies an entry in the filter table.  Each such entry defines one filter that is to be applied to every packet received on an interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: filterchannelindex
            
            	This object identifies the channel of which this filter is a part.  The filters identified by a particular value of this object are associated with the same channel as identified by the same value of the channelIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: filterpktdataoffset
            
            	The offset from the beginning of each packet where a match of packet data will be attempted.  This offset is measured from the point in the physical layer packet after the framing bits, if any.  For example, in an Ethernet frame, this point is at the beginning of the destination MAC address.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: filterpktdata
            
            	The data that is to be matched with the input packet. For each packet received, this filter and the accompanying filterPktDataMask and filterPktDataNotMask will be adjusted for the offset.  The only bits relevant to this match algorithm are those that have the corresponding filterPktDataMask bit equal to one.  The following three rules are then applied to every packet\:  (1) If the packet is too short and does not have data     corresponding to part of the filterPktData, the packet     will fail this data match.  (2) For each relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to zero, if     the bit from the packet is not equal to the corresponding     bit from the filterPktData, then the packet will fail     this data match.  (3) If for every relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to one, the     bit from the packet is equal to the corresponding bit     from the filterPktData, then the packet will fail this     data match.  Any packets that have not failed any of the three matches above have passed this data match.  In particular, a zero length filter will match any packet.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktdatamask
            
            	The mask that is applied to the match process. After adjusting this mask for the offset, only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the match algorithm.  The offset is applied to filterPktDataMask in the same way it is applied to the filter.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktdatanotmask
            
            	The inversion mask that is applied to the match process.  After adjusting this mask for the offset, those relevant bits in the received packet that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktData object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet that correspond to bits set in this mask must be different to its corresponding bit in the filterPktData object.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktstatus
            
            	The status that is to be matched with the input packet. The only bits relevant to this match algorithm are those that have the corresponding filterPktStatusMask bit equal to one. The following two rules are then applied to every packet\:  (1) For each relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to zero, if     the bit from the packet status is not equal to the     corresponding bit from the filterPktStatus, then the     packet will fail this status match.  (2) If for every relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to one, the     bit from the packet status is equal to the corresponding     bit from the filterPktStatus, then the packet will fail     this status match.  Any packets that have not failed either of the two matches above have passed this status match.  In particular, a zero length status filter will match any packet's status.  The value of the packet status is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum. The errors and the bits that represent them are dependent on the media type of the interface that this channel is receiving packets from.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined.  For the purposes of this status matching algorithm, if the packet status is longer than this filterPktStatus object, this object is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusmask
            
            	The mask that is applied to the status match process. Only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the status match algorithm.  For the purposes of the matching algorithm, if the associated filterPktStatus object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the size of the filterPktStatus.  In addition, if a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusnotmask
            
            	The inversion mask that is applied to the status match process.  Those relevant bits in the received packet status that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktStatus object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet status that correspond to bits set in this mask must be different to its corresponding bit in the filterPktStatus object for the packet to be accepted.  For the purposes of the matching algorithm, if the associated filterPktStatus object or a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the longer of the lengths of the filterPktStatus object and the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: filterstatus
            
            	The status of this filter entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: filterprotocoldirdatalocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with performs the following operations on every packet\:  1) \- If the packet doesn't match the protocol directory entry      identified by this object, discard the packet and exit      (i.e., discard the packet if it is not of the identified      protocol). 2) \- If the associated filterProtocolDirLocalIndex is non\-zero      and the packet doesn't match the protocol directory      entry identified by that object, discard the packet and      exit 3) \- If the packet matches, perform the regular filter      algorithm as if the beginning of this named protocol is      the beginning of the packet, potentially applying the      filterOffset value to move further into the packet
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: filterprotocoldirlocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with will discard the packet if the packet doesn't match this protocol directory entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Filtertable.Filterentry, self).__init__()

                self.yang_name = "filterEntry"
                self.yang_parent_name = "filterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['filterindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('filterindex', YLeaf(YType.int32, 'filterIndex')),
                    ('filterchannelindex', YLeaf(YType.int32, 'filterChannelIndex')),
                    ('filterpktdataoffset', YLeaf(YType.int32, 'filterPktDataOffset')),
                    ('filterpktdata', YLeaf(YType.str, 'filterPktData')),
                    ('filterpktdatamask', YLeaf(YType.str, 'filterPktDataMask')),
                    ('filterpktdatanotmask', YLeaf(YType.str, 'filterPktDataNotMask')),
                    ('filterpktstatus', YLeaf(YType.int32, 'filterPktStatus')),
                    ('filterpktstatusmask', YLeaf(YType.int32, 'filterPktStatusMask')),
                    ('filterpktstatusnotmask', YLeaf(YType.int32, 'filterPktStatusNotMask')),
                    ('filterowner', YLeaf(YType.str, 'filterOwner')),
                    ('filterstatus', YLeaf(YType.enumeration, 'filterStatus')),
                    ('filterprotocoldirdatalocalindex', YLeaf(YType.int32, 'RMON2-MIB:filterProtocolDirDataLocalIndex')),
                    ('filterprotocoldirlocalindex', YLeaf(YType.int32, 'RMON2-MIB:filterProtocolDirLocalIndex')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Filtertable.Filterentry, ['filterindex', 'filterchannelindex', 'filterpktdataoffset', 'filterpktdata', 'filterpktdatamask', 'filterpktdatanotmask', 'filterpktstatus', 'filterpktstatusmask', 'filterpktstatusnotmask', 'filterowner', 'filterstatus', 'filterprotocoldirdatalocalindex', 'filterprotocoldirlocalindex'], name, value)


    class Channeltable(Entity):
        """
        A list of packet channel entries.
        
        .. attribute:: channelentry
        
        	A set of parameters for a packet channel applied on a particular interface.  As an example, an instance of the channelMatches object might be named channelMatches.3
        	**type**\: list of  		 :py:class:`Channelentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Channeltable.Channelentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Channeltable, self).__init__()

            self.yang_name = "channelTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("channelEntry", ("channelentry", RMONMIB.Channeltable.Channelentry))])
            self._leafs = OrderedDict()

            self.channelentry = YList(self)
            self._segment_path = lambda: "channelTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Channeltable, [], name, value)


        class Channelentry(Entity):
            """
            A set of parameters for a packet channel applied on a
            particular interface.  As an example, an instance of the
            channelMatches object might be named channelMatches.3
            
            .. attribute:: channelindex  (key)
            
            	An index that uniquely identifies an entry in the channel table.  Each such entry defines one channel, a logical data and event stream.  It is suggested that before creating a channel, an application should scan all instances of the filterChannelIndex object to make sure that there are no pre\-existing filters that would be inadvertently be linked to the channel
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: channelifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device to which the associated filters are applied to allow data into this channel.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in RFC 2233 [17].  The filters in this group are applied to all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: channelaccepttype
            
            	This object controls the action of the filters associated with this channel.  If this object is equal to acceptMatched(1), packets will be accepted to this channel if they are accepted by both the packet data and packet status matches of an associated filter.  If this object is equal to acceptFailed(2), packets will be accepted to this channel only if they fail either the packet data match or the packet status match of each of the associated filters.  In particular, a channel with no associated filters will match no packets if set to acceptMatched(1) case and will match all packets in the acceptFailed(2) case.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  :py:class:`Channelaccepttype <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Channeltable.Channelentry.Channelaccepttype>`
            
            .. attribute:: channeldatacontrol
            
            	This object controls the flow of data through this channel. If this object is on(1), data, status and events flow through this channel.  If this object is off(2), data, status and events will not flow through this channel
            	**type**\:  :py:class:`Channeldatacontrol <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Channeltable.Channelentry.Channeldatacontrol>`
            
            .. attribute:: channelturnoneventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from off to on when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOnEventIndex must be set to zero, a non\-existent event index. This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: channelturnoffeventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from on to off when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOffEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: channeleventindex
            
            	The value of this object identifies the event that is configured to be generated when the associated channelDataControl is on and a packet is matched.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: channeleventstatus
            
            	The event status of this channel.  If this channel is configured to generate events when packets are matched, a means of controlling the flow of those events is often needed.  When this object is equal to eventReady(1), a single event may be generated, after which this object will be set by the probe to eventFired(2).  While in the eventFired(2) state, no events will be generated until the object is modified to eventReady(1) (or eventAlwaysReady(3)).  The management station can thus easily respond to a notification of an event by re\-enabling this object.  If the management station wishes to disable this flow control and allow events to be generated at will, this object may be set to eventAlwaysReady(3).  Disabling the flow control is discouraged as it can result in high network traffic or other performance problems
            	**type**\:  :py:class:`Channeleventstatus <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Channeltable.Channelentry.Channeleventstatus>`
            
            .. attribute:: channelmatches
            
            	The number of times this channel has matched a packet. Note that this object is updated even when channelDataControl is set to off
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: channeldescription
            
            	A comment describing this channel
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: channelowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: channelstatus
            
            	The status of this channel entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            .. attribute:: channeldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe      is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: channelcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Channeltable.Channelentry, self).__init__()

                self.yang_name = "channelEntry"
                self.yang_parent_name = "channelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['channelindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('channelindex', YLeaf(YType.int32, 'channelIndex')),
                    ('channelifindex', YLeaf(YType.int32, 'channelIfIndex')),
                    ('channelaccepttype', YLeaf(YType.enumeration, 'channelAcceptType')),
                    ('channeldatacontrol', YLeaf(YType.enumeration, 'channelDataControl')),
                    ('channelturnoneventindex', YLeaf(YType.int32, 'channelTurnOnEventIndex')),
                    ('channelturnoffeventindex', YLeaf(YType.int32, 'channelTurnOffEventIndex')),
                    ('channeleventindex', YLeaf(YType.int32, 'channelEventIndex')),
                    ('channeleventstatus', YLeaf(YType.enumeration, 'channelEventStatus')),
                    ('channelmatches', YLeaf(YType.uint32, 'channelMatches')),
                    ('channeldescription', YLeaf(YType.str, 'channelDescription')),
                    ('channelowner', YLeaf(YType.str, 'channelOwner')),
                    ('channelstatus', YLeaf(YType.enumeration, 'channelStatus')),
                    ('channeldroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:channelDroppedFrames')),
                    ('channelcreatetime', YLeaf(YType.uint32, 'RMON2-MIB:channelCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Channeltable.Channelentry, ['channelindex', 'channelifindex', 'channelaccepttype', 'channeldatacontrol', 'channelturnoneventindex', 'channelturnoffeventindex', 'channeleventindex', 'channeleventstatus', 'channelmatches', 'channeldescription', 'channelowner', 'channelstatus', 'channeldroppedframes', 'channelcreatetime'], name, value)

            class Channelaccepttype(Enum):
                """
                Channelaccepttype (Enum Class)

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


            class Channeldatacontrol(Enum):
                """
                Channeldatacontrol (Enum Class)

                This object controls the flow of data through this channel.

                If this object is on(1), data, status and events flow

                through this channel.  If this object is off(2), data,

                status and events will not flow through this channel.

                .. data:: on = 1

                .. data:: off = 2

                """

                on = Enum.YLeaf(1, "on")

                off = Enum.YLeaf(2, "off")


            class Channeleventstatus(Enum):
                """
                Channeleventstatus (Enum Class)

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



    class Buffercontroltable(Entity):
        """
        A list of buffers control entries.
        
        .. attribute:: buffercontrolentry
        
        	A set of parameters that control the collection of a stream of packets that have matched filters.  As an example, an instance of the bufferControlCaptureSliceSize object might be named bufferControlCaptureSliceSize.3
        	**type**\: list of  		 :py:class:`Buffercontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Buffercontroltable.Buffercontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Buffercontroltable, self).__init__()

            self.yang_name = "bufferControlTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bufferControlEntry", ("buffercontrolentry", RMONMIB.Buffercontroltable.Buffercontrolentry))])
            self._leafs = OrderedDict()

            self.buffercontrolentry = YList(self)
            self._segment_path = lambda: "bufferControlTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Buffercontroltable, [], name, value)


        class Buffercontrolentry(Entity):
            """
            A set of parameters that control the collection of a stream
            of packets that have matched filters.  As an example, an
            instance of the bufferControlCaptureSliceSize object might
            be named bufferControlCaptureSliceSize.3
            
            .. attribute:: buffercontrolindex  (key)
            
            	An index that uniquely identifies an entry in the bufferControl table.  The value of this index shall never be zero.  Each such entry defines one set of packets that is captured and controlled by one or more filters
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontrolchannelindex
            
            	An index that identifies the channel that is the source of packets for this bufferControl table. The channel identified by a particular value of this index is the same as identified by the same value of the channelIndex object.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontrolfullstatus
            
            	This object shows whether the buffer has room to accept new packets or if it is full.  If the status is spaceAvailable(1), the buffer is accepting new packets normally.  If the status is full(2) and the associated bufferControlFullAction object is wrapWhenFull, the buffer is accepting new packets by deleting enough of the oldest packets to make room for new ones as they arrive.  Otherwise, if the status is full(2) and the bufferControlFullAction object is lockWhenFull, then the buffer has stopped collecting packets.  When this object is set to full(2) the probe must not later set it to spaceAvailable(1) except in the case of a significant gain in resources such as an increase of bufferControlOctetsGranted.  In particular, the wrap\-mode action of deleting old packets to make room for newly arrived packets must not affect the value of this object
            	**type**\:  :py:class:`Buffercontrolfullstatus <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Buffercontroltable.Buffercontrolentry.Buffercontrolfullstatus>`
            
            .. attribute:: buffercontrolfullaction
            
            	Controls the action of the buffer when it reaches the full status.  When in the lockWhenFull(1) state and a packet is added to the buffer that fills the buffer, the bufferControlFullStatus will be set to full(2) and this buffer will stop capturing packets
            	**type**\:  :py:class:`Buffercontrolfullaction <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Buffercontroltable.Buffercontrolentry.Buffercontrolfullaction>`
            
            .. attribute:: buffercontrolcaptureslicesize
            
            	The maximum number of octets of each packet that will be saved in this capture buffer. For example, if a 1500 octet packet is received by the probe and this object is set to 500, then only 500 octets of the packet will be stored in the associated capture buffer.  If this variable is set to 0, the capture buffer will save as many octets as is possible.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontroldownloadslicesize
            
            	The maximum number of octets of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer, the associated bufferControlDownloadOffset is 0, and this object is set to 100, then the captureBufferPacket object that contains the packet will contain only the first 100 octets of the packet.  A prudent manager will take into account possible interoperability or fragmentation problems that may occur if the download slice size is set too large. In particular, conformant SNMP implementations are not required to accept messages whose length exceeds 484 octets, although they are encouraged to support larger datagrams whenever feasible
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontroldownloadoffset
            
            	The offset of the first octet of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer and this object is set to 100, then the captureBufferPacket object that contains the packet will contain bytes starting 100 octets into the packet
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolmaxoctetsrequested
            
            	The requested maximum number of octets to be saved in this captureBuffer, including any implementation\-specific overhead. If this variable is set to \-1, the capture buffer will save as many octets as is possible.  When this object is created or modified, the probe should set bufferControlMaxOctetsGranted as closely to this object as is possible for the particular probe implementation and available resources.  However, if the object has the special value of \-1, the probe must set bufferControlMaxOctetsGranted to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolmaxoctetsgranted
            
            	The maximum number of octets that can be saved in this captureBuffer, including overhead. If this variable is \-1, the capture buffer will save as many octets as possible.  When the bufferControlMaxOctetsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources. However, if the request object has the special value of \-1, the probe must set this object to \-1.  The probe must not lower this value except as a result of a modification to the associated bufferControlMaxOctetsRequested object.  When this maximum number of octets is reached and a new packet is to be added to this capture buffer and the corresponding bufferControlFullAction is set to wrapWhenFull(2), enough of the oldest packets associated with this capture buffer shall be deleted by the agent so that the new packet can be added.  If the corresponding bufferControlFullAction is set to lockWhenFull(1), the new packet shall be discarded.  In either case, the probe must set bufferControlFullStatus to full(2).  When the value of this object changes to a value less than the current value, entries are deleted from the captureBufferTable associated with this bufferControlEntry.  Enough of the oldest of these captureBufferEntries shall be deleted by the agent so that the number of octets used remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated captureBufferEntries may be allowed to grow
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolcapturedpackets
            
            	The number of packets currently in this captureBuffer
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Packets
            
            .. attribute:: buffercontrolturnontime
            
            	The value of sysUpTime when this capture buffer was first turned on
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffercontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: buffercontrolstatus
            
            	The status of this buffer Control Entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Buffercontroltable.Buffercontrolentry, self).__init__()

                self.yang_name = "bufferControlEntry"
                self.yang_parent_name = "bufferControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffercontrolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('buffercontrolindex', YLeaf(YType.int32, 'bufferControlIndex')),
                    ('buffercontrolchannelindex', YLeaf(YType.int32, 'bufferControlChannelIndex')),
                    ('buffercontrolfullstatus', YLeaf(YType.enumeration, 'bufferControlFullStatus')),
                    ('buffercontrolfullaction', YLeaf(YType.enumeration, 'bufferControlFullAction')),
                    ('buffercontrolcaptureslicesize', YLeaf(YType.int32, 'bufferControlCaptureSliceSize')),
                    ('buffercontroldownloadslicesize', YLeaf(YType.int32, 'bufferControlDownloadSliceSize')),
                    ('buffercontroldownloadoffset', YLeaf(YType.int32, 'bufferControlDownloadOffset')),
                    ('buffercontrolmaxoctetsrequested', YLeaf(YType.int32, 'bufferControlMaxOctetsRequested')),
                    ('buffercontrolmaxoctetsgranted', YLeaf(YType.int32, 'bufferControlMaxOctetsGranted')),
                    ('buffercontrolcapturedpackets', YLeaf(YType.int32, 'bufferControlCapturedPackets')),
                    ('buffercontrolturnontime', YLeaf(YType.uint32, 'bufferControlTurnOnTime')),
                    ('buffercontrolowner', YLeaf(YType.str, 'bufferControlOwner')),
                    ('buffercontrolstatus', YLeaf(YType.enumeration, 'bufferControlStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Buffercontroltable.Buffercontrolentry, ['buffercontrolindex', 'buffercontrolchannelindex', 'buffercontrolfullstatus', 'buffercontrolfullaction', 'buffercontrolcaptureslicesize', 'buffercontroldownloadslicesize', 'buffercontroldownloadoffset', 'buffercontrolmaxoctetsrequested', 'buffercontrolmaxoctetsgranted', 'buffercontrolcapturedpackets', 'buffercontrolturnontime', 'buffercontrolowner', 'buffercontrolstatus'], name, value)

            class Buffercontrolfullaction(Enum):
                """
                Buffercontrolfullaction (Enum Class)

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


            class Buffercontrolfullstatus(Enum):
                """
                Buffercontrolfullstatus (Enum Class)

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



    class Capturebuffertable(Entity):
        """
        A list of packets captured off of a channel.
        
        .. attribute:: capturebufferentry
        
        	A packet captured off of an attached network.  As an example, an instance of the captureBufferPacketData object might be named captureBufferPacketData.3.1783
        	**type**\: list of  		 :py:class:`Capturebufferentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Capturebuffertable.Capturebufferentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Capturebuffertable, self).__init__()

            self.yang_name = "captureBufferTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("captureBufferEntry", ("capturebufferentry", RMONMIB.Capturebuffertable.Capturebufferentry))])
            self._leafs = OrderedDict()

            self.capturebufferentry = YList(self)
            self._segment_path = lambda: "captureBufferTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Capturebuffertable, [], name, value)


        class Capturebufferentry(Entity):
            """
            A packet captured off of an attached network.  As an
            example, an instance of the captureBufferPacketData
            object might be named captureBufferPacketData.3.1783
            
            .. attribute:: capturebuffercontrolindex  (key)
            
            	The index of the bufferControlEntry with which this packet is associated
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: capturebufferindex  (key)
            
            	An index that uniquely identifies an entry in the captureBuffer table associated with a particular bufferControlEntry.  This index will start at 1 and increase by one for each new packet added with the same captureBufferControlIndex.  Should this value reach 2147483647, the next packet added with the same captureBufferControlIndex shall cause this value to wrap around to 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: capturebufferpacketid
            
            	An index that describes the order of packets that are received on a particular interface. The packetID of a packet captured on an interface is defined to be greater than the packetID's of all packets captured previously on the same interface.  As the captureBufferPacketID object has a maximum positive value of 2^31 \- 1, any captureBufferPacketID object shall have the value of the associated packet's packetID mod 2^31
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpacketdata
            
            	The data inside the packet, starting at the beginning of the packet plus any offset specified in the associated bufferControlDownloadOffset, including any link level headers.  The length of the data in this object is the minimum of the length of the captured packet minus the offset, the length of the associated bufferControlCaptureSliceSize minus the offset, and the associated bufferControlDownloadSliceSize.  If this minimum is less than zero, this object shall have a length of zero
            	**type**\: str
            
            .. attribute:: capturebufferpacketlength
            
            	The actual length (off the wire) of the packet stored in this entry, including FCS octets
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: capturebufferpackettime
            
            	The number of milliseconds that had passed since this capture buffer was first turned on when this packet was captured
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Milliseconds
            
            .. attribute:: capturebufferpacketstatus
            
            	A value which indicates the error status of this packet.  The value of this object is defined in the same way as filterPktStatus.  The value is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error         3    First packet in this capture buffer after              it was detected that some packets were              not processed correctly.         4    Packet's order in buffer is only approximate              (May only be set for packets sent from              the probe)  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Capturebuffertable.Capturebufferentry, self).__init__()

                self.yang_name = "captureBufferEntry"
                self.yang_parent_name = "captureBufferTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['capturebuffercontrolindex','capturebufferindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('capturebuffercontrolindex', YLeaf(YType.int32, 'captureBufferControlIndex')),
                    ('capturebufferindex', YLeaf(YType.int32, 'captureBufferIndex')),
                    ('capturebufferpacketid', YLeaf(YType.int32, 'captureBufferPacketID')),
                    ('capturebufferpacketdata', YLeaf(YType.str, 'captureBufferPacketData')),
                    ('capturebufferpacketlength', YLeaf(YType.int32, 'captureBufferPacketLength')),
                    ('capturebufferpackettime', YLeaf(YType.int32, 'captureBufferPacketTime')),
                    ('capturebufferpacketstatus', YLeaf(YType.int32, 'captureBufferPacketStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Capturebuffertable.Capturebufferentry, ['capturebuffercontrolindex', 'capturebufferindex', 'capturebufferpacketid', 'capturebufferpacketdata', 'capturebufferpacketlength', 'capturebufferpackettime', 'capturebufferpacketstatus'], name, value)


    class Eventtable(Entity):
        """
        A list of events to be generated.
        
        .. attribute:: evententry
        
        	A set of parameters that describe an event to be generated when certain conditions are met.  As an example, an instance of the eventLastTimeSent object might be named eventLastTimeSent.6
        	**type**\: list of  		 :py:class:`Evententry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Eventtable.Evententry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Eventtable, self).__init__()

            self.yang_name = "eventTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("eventEntry", ("evententry", RMONMIB.Eventtable.Evententry))])
            self._leafs = OrderedDict()

            self.evententry = YList(self)
            self._segment_path = lambda: "eventTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Eventtable, [], name, value)


        class Evententry(Entity):
            """
            A set of parameters that describe an event to be generated
            when certain conditions are met.  As an example, an instance
            of the eventLastTimeSent object might be named
            eventLastTimeSent.6
            
            .. attribute:: eventindex  (key)
            
            	An index that uniquely identifies an entry in the event table.  Each such entry defines one event that is to be generated when the appropriate conditions occur
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: eventdescription
            
            	A comment describing this event entry
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: eventtype
            
            	The type of notification that the probe will make about this event.  In the case of log, an entry is made in the log table for each event.  In the case of snmp\-trap, an SNMP trap is sent to one or more management stations
            	**type**\:  :py:class:`Eventtype <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Eventtable.Evententry.Eventtype>`
            
            .. attribute:: eventcommunity
            
            	If an SNMP trap is to be sent, it will be sent to the SNMP community specified by this octet string
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: eventlasttimesent
            
            	The value of sysUpTime at the time this event entry last generated an event.  If this entry has not generated any events, this value will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: eventowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it.  If this object contains a string starting with 'monitor' and has associated entries in the log table, all connected management stations should retrieve those log entries, as they may have significance to all management stations connected to this device
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: eventstatus
            
            	The status of this event entry.  If this object is not equal to valid(1), all associated log entries shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.RMON_MIB.EntryStatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Eventtable.Evententry, self).__init__()

                self.yang_name = "eventEntry"
                self.yang_parent_name = "eventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['eventindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('eventindex', YLeaf(YType.int32, 'eventIndex')),
                    ('eventdescription', YLeaf(YType.str, 'eventDescription')),
                    ('eventtype', YLeaf(YType.enumeration, 'eventType')),
                    ('eventcommunity', YLeaf(YType.str, 'eventCommunity')),
                    ('eventlasttimesent', YLeaf(YType.uint32, 'eventLastTimeSent')),
                    ('eventowner', YLeaf(YType.str, 'eventOwner')),
                    ('eventstatus', YLeaf(YType.enumeration, 'eventStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Eventtable.Evententry, ['eventindex', 'eventdescription', 'eventtype', 'eventcommunity', 'eventlasttimesent', 'eventowner', 'eventstatus'], name, value)

            class Eventtype(Enum):
                """
                Eventtype (Enum Class)

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



    class Logtable(Entity):
        """
        A list of events that have been logged.
        
        .. attribute:: logentry
        
        	A set of data describing an event that has been logged.  For example, an instance of the logDescription object might be named logDescription.6.47
        	**type**\: list of  		 :py:class:`Logentry <ydk.models.cisco_ios_xe.RMON_MIB.RMONMIB.Logtable.Logentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RMONMIB.Logtable, self).__init__()

            self.yang_name = "logTable"
            self.yang_parent_name = "RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("logEntry", ("logentry", RMONMIB.Logtable.Logentry))])
            self._leafs = OrderedDict()

            self.logentry = YList(self)
            self._segment_path = lambda: "logTable"
            self._absolute_path = lambda: "RMON-MIB:RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RMONMIB.Logtable, [], name, value)


        class Logentry(Entity):
            """
            A set of data describing an event that has been
            logged.  For example, an instance of the logDescription
            object might be named logDescription.6.47
            
            .. attribute:: logeventindex  (key)
            
            	The event entry that generated this log entry.  The log identified by a particular value of this index is associated with the same eventEntry as identified by the same value of eventIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: logindex  (key)
            
            	An index that uniquely identifies an entry in the log table amongst those generated by the same eventEntries.  These indexes are assigned beginning with 1 and increase by one with each new log entry.  The association between values of logIndex and logEntries is fixed for the lifetime of each logEntry. The agent may choose to delete the oldest instances of logEntry as required because of lack of memory.  It is an implementation\-specific matter as to when this deletion may occur
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: logtime
            
            	The value of sysUpTime when this log entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: logdescription
            
            	An implementation dependent description of the event that activated this log entry
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RMONMIB.Logtable.Logentry, self).__init__()

                self.yang_name = "logEntry"
                self.yang_parent_name = "logTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['logeventindex','logindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('logeventindex', YLeaf(YType.int32, 'logEventIndex')),
                    ('logindex', YLeaf(YType.int32, 'logIndex')),
                    ('logtime', YLeaf(YType.uint32, 'logTime')),
                    ('logdescription', YLeaf(YType.str, 'logDescription')),
                ])
                self.logeventindex = None
                self.logindex = None
                self.logtime = None
                self.logdescription = None
                self._segment_path = lambda: "logEntry" + "[logEventIndex='" + str(self.logeventindex) + "']" + "[logIndex='" + str(self.logindex) + "']"
                self._absolute_path = lambda: "RMON-MIB:RMON-MIB/logTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RMONMIB.Logtable.Logentry, ['logeventindex', 'logindex', 'logtime', 'logdescription'], name, value)

    def clone_ptr(self):
        self._top_entity = RMONMIB()
        return self._top_entity

