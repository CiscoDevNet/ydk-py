""" RMON_MIB 

Remote network monitoring devices, often called
monitors or probes, are instruments that exist for
the purpose of managing a network. This MIB defines
objects for managing remote network monitoring devices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Entrystatus(Enum):
    """
    Entrystatus

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


class RmonMib(Entity):
    """
    
    
    .. attribute:: alarmtable
    
    	A list of alarm entries
    	**type**\:   :py:class:`Alarmtable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Alarmtable>`
    
    .. attribute:: buffercontroltable
    
    	A list of buffers control entries
    	**type**\:   :py:class:`Buffercontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Buffercontroltable>`
    
    .. attribute:: capturebuffertable
    
    	A list of packets captured off of a channel
    	**type**\:   :py:class:`Capturebuffertable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Capturebuffertable>`
    
    .. attribute:: channeltable
    
    	A list of packet channel entries
    	**type**\:   :py:class:`Channeltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Channeltable>`
    
    .. attribute:: etherhistorytable
    
    	A list of Ethernet history entries
    	**type**\:   :py:class:`Etherhistorytable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Etherhistorytable>`
    
    .. attribute:: etherstatstable
    
    	A list of Ethernet statistics entries
    	**type**\:   :py:class:`Etherstatstable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Etherstatstable>`
    
    .. attribute:: eventtable
    
    	A list of events to be generated
    	**type**\:   :py:class:`Eventtable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Eventtable>`
    
    .. attribute:: filtertable
    
    	A list of packet filter entries
    	**type**\:   :py:class:`Filtertable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Filtertable>`
    
    .. attribute:: historycontroltable
    
    	A list of history control entries
    	**type**\:   :py:class:`Historycontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Historycontroltable>`
    
    .. attribute:: hostcontroltable
    
    	A list of host table control entries
    	**type**\:   :py:class:`Hostcontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hostcontroltable>`
    
    .. attribute:: hosttable
    
    	A list of host entries
    	**type**\:   :py:class:`Hosttable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttable>`
    
    .. attribute:: hosttimetable
    
    	A list of time\-ordered host table entries
    	**type**\:   :py:class:`Hosttimetable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttimetable>`
    
    .. attribute:: hosttopncontroltable
    
    	A list of top N host control entries
    	**type**\:   :py:class:`Hosttopncontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttopncontroltable>`
    
    .. attribute:: hosttopntable
    
    	A list of top N host entries
    	**type**\:   :py:class:`Hosttopntable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttopntable>`
    
    .. attribute:: logtable
    
    	A list of events that have been logged
    	**type**\:   :py:class:`Logtable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Logtable>`
    
    .. attribute:: matrixcontroltable
    
    	A list of information entries for the traffic matrix on each interface
    	**type**\:   :py:class:`Matrixcontroltable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixcontroltable>`
    
    .. attribute:: matrixdstable
    
    	A list of traffic matrix entries indexed by destination and source MAC address
    	**type**\:   :py:class:`Matrixdstable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixdstable>`
    
    .. attribute:: matrixsdtable
    
    	A list of traffic matrix entries indexed by source and destination MAC address
    	**type**\:   :py:class:`Matrixsdtable <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixsdtable>`
    
    

    """

    _prefix = 'RMON-MIB'
    _revision = '2000-05-11'

    def __init__(self):
        super(RmonMib, self).__init__()
        self._top_entity = None

        self.yang_name = "RMON-MIB"
        self.yang_parent_name = "RMON-MIB"

        self.alarmtable = RmonMib.Alarmtable()
        self.alarmtable.parent = self
        self._children_name_map["alarmtable"] = "alarmTable"
        self._children_yang_names.add("alarmTable")

        self.buffercontroltable = RmonMib.Buffercontroltable()
        self.buffercontroltable.parent = self
        self._children_name_map["buffercontroltable"] = "bufferControlTable"
        self._children_yang_names.add("bufferControlTable")

        self.capturebuffertable = RmonMib.Capturebuffertable()
        self.capturebuffertable.parent = self
        self._children_name_map["capturebuffertable"] = "captureBufferTable"
        self._children_yang_names.add("captureBufferTable")

        self.channeltable = RmonMib.Channeltable()
        self.channeltable.parent = self
        self._children_name_map["channeltable"] = "channelTable"
        self._children_yang_names.add("channelTable")

        self.etherhistorytable = RmonMib.Etherhistorytable()
        self.etherhistorytable.parent = self
        self._children_name_map["etherhistorytable"] = "etherHistoryTable"
        self._children_yang_names.add("etherHistoryTable")

        self.etherstatstable = RmonMib.Etherstatstable()
        self.etherstatstable.parent = self
        self._children_name_map["etherstatstable"] = "etherStatsTable"
        self._children_yang_names.add("etherStatsTable")

        self.eventtable = RmonMib.Eventtable()
        self.eventtable.parent = self
        self._children_name_map["eventtable"] = "eventTable"
        self._children_yang_names.add("eventTable")

        self.filtertable = RmonMib.Filtertable()
        self.filtertable.parent = self
        self._children_name_map["filtertable"] = "filterTable"
        self._children_yang_names.add("filterTable")

        self.historycontroltable = RmonMib.Historycontroltable()
        self.historycontroltable.parent = self
        self._children_name_map["historycontroltable"] = "historyControlTable"
        self._children_yang_names.add("historyControlTable")

        self.hostcontroltable = RmonMib.Hostcontroltable()
        self.hostcontroltable.parent = self
        self._children_name_map["hostcontroltable"] = "hostControlTable"
        self._children_yang_names.add("hostControlTable")

        self.hosttable = RmonMib.Hosttable()
        self.hosttable.parent = self
        self._children_name_map["hosttable"] = "hostTable"
        self._children_yang_names.add("hostTable")

        self.hosttimetable = RmonMib.Hosttimetable()
        self.hosttimetable.parent = self
        self._children_name_map["hosttimetable"] = "hostTimeTable"
        self._children_yang_names.add("hostTimeTable")

        self.hosttopncontroltable = RmonMib.Hosttopncontroltable()
        self.hosttopncontroltable.parent = self
        self._children_name_map["hosttopncontroltable"] = "hostTopNControlTable"
        self._children_yang_names.add("hostTopNControlTable")

        self.hosttopntable = RmonMib.Hosttopntable()
        self.hosttopntable.parent = self
        self._children_name_map["hosttopntable"] = "hostTopNTable"
        self._children_yang_names.add("hostTopNTable")

        self.logtable = RmonMib.Logtable()
        self.logtable.parent = self
        self._children_name_map["logtable"] = "logTable"
        self._children_yang_names.add("logTable")

        self.matrixcontroltable = RmonMib.Matrixcontroltable()
        self.matrixcontroltable.parent = self
        self._children_name_map["matrixcontroltable"] = "matrixControlTable"
        self._children_yang_names.add("matrixControlTable")

        self.matrixdstable = RmonMib.Matrixdstable()
        self.matrixdstable.parent = self
        self._children_name_map["matrixdstable"] = "matrixDSTable"
        self._children_yang_names.add("matrixDSTable")

        self.matrixsdtable = RmonMib.Matrixsdtable()
        self.matrixsdtable.parent = self
        self._children_name_map["matrixsdtable"] = "matrixSDTable"
        self._children_yang_names.add("matrixSDTable")


    class Etherstatstable(Entity):
        """
        A list of Ethernet statistics entries.
        
        .. attribute:: etherstatsentry
        
        	A collection of statistics kept for a particular Ethernet interface.  As an example, an instance of the etherStatsPkts object might be named etherStatsPkts.1
        	**type**\: list of    :py:class:`Etherstatsentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Etherstatstable.Etherstatsentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Etherstatstable, self).__init__()

            self.yang_name = "etherStatsTable"
            self.yang_parent_name = "RMON-MIB"

            self.etherstatsentry = YList(self)

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
                        super(RmonMib.Etherstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Etherstatstable, self).__setattr__(name, value)


        class Etherstatsentry(Entity):
            """
            A collection of statistics kept for a particular
            Ethernet interface.  As an example, an instance of the
            etherStatsPkts object might be named etherStatsPkts.1
            
            .. attribute:: etherstatsindex  <key>
            
            	The value of this object uniquely identifies this etherStats entry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: etherstatsbroadcastpkts
            
            	The total number of good packets received that were directed to the broadcast address.  Note that this does not include multicast packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatscollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Collisions
            
            .. attribute:: etherstatscrcalignerrors
            
            	The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsdatasource
            
            	This object identifies the source of the data that this etherStats entry is configured to analyze.  This source can be any ethernet interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated etherStatsStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: etherstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsfragments
            
            	The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherStatsFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsjabbers
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsmulticastpkts
            
            	The total number of good packets received that were directed to a multicast address.  Note that this number does not include packets directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets). This object can be used as a reasonable estimate of 10\-Megabit ethernet utilization.  If greater precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval.  The differences in the sampled values are Pkts and Octets, respectively, and the number of seconds in the interval is Interval.  These values are used to calculate the Utilization as follows\:                   Pkts \* (9.6 + 6.4) + (Octets \* .8)  Utilization = \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-                          Interval \* 10,000  The result of this equation is the value Utilization which is the percent utilization of the ethernet segment on a scale of 0 to 100 percent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: etherstatsoversizepkts
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: etherstatspkts
            
            	The total number of packets (including bad packets, broadcast packets, and multicast packets) received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts1024to1518octets
            
            	The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts128to255octets
            
            	The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts256to511octets
            
            	The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts512to1023octets
            
            	The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts64octets
            
            	The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatspkts65to127octets
            
            	The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherstatsstatus
            
            	The status of this etherStats entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: etherstatsundersizepkts
            
            	The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Etherstatstable.Etherstatsentry, self).__init__()

                self.yang_name = "etherStatsEntry"
                self.yang_parent_name = "etherStatsTable"

                self.etherstatsindex = YLeaf(YType.int32, "etherStatsIndex")

                self.etherstatsbroadcastpkts = YLeaf(YType.uint32, "etherStatsBroadcastPkts")

                self.etherstatscollisions = YLeaf(YType.uint32, "etherStatsCollisions")

                self.etherstatscrcalignerrors = YLeaf(YType.uint32, "etherStatsCRCAlignErrors")

                self.etherstatscreatetime = YLeaf(YType.uint32, "RMON2-MIB:etherStatsCreateTime")

                self.etherstatsdatasource = YLeaf(YType.str, "etherStatsDataSource")

                self.etherstatsdropevents = YLeaf(YType.uint32, "etherStatsDropEvents")

                self.etherstatsdroppedframes = YLeaf(YType.uint32, "RMON2-MIB:etherStatsDroppedFrames")

                self.etherstatsfragments = YLeaf(YType.uint32, "etherStatsFragments")

                self.etherstatsjabbers = YLeaf(YType.uint32, "etherStatsJabbers")

                self.etherstatsmulticastpkts = YLeaf(YType.uint32, "etherStatsMulticastPkts")

                self.etherstatsoctets = YLeaf(YType.uint32, "etherStatsOctets")

                self.etherstatsoversizepkts = YLeaf(YType.uint32, "etherStatsOversizePkts")

                self.etherstatsowner = YLeaf(YType.str, "etherStatsOwner")

                self.etherstatspkts = YLeaf(YType.uint32, "etherStatsPkts")

                self.etherstatspkts1024to1518octets = YLeaf(YType.uint32, "etherStatsPkts1024to1518Octets")

                self.etherstatspkts128to255octets = YLeaf(YType.uint32, "etherStatsPkts128to255Octets")

                self.etherstatspkts256to511octets = YLeaf(YType.uint32, "etherStatsPkts256to511Octets")

                self.etherstatspkts512to1023octets = YLeaf(YType.uint32, "etherStatsPkts512to1023Octets")

                self.etherstatspkts64octets = YLeaf(YType.uint32, "etherStatsPkts64Octets")

                self.etherstatspkts65to127octets = YLeaf(YType.uint32, "etherStatsPkts65to127Octets")

                self.etherstatsstatus = YLeaf(YType.enumeration, "etherStatsStatus")

                self.etherstatsundersizepkts = YLeaf(YType.uint32, "etherStatsUndersizePkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("etherstatsindex",
                                "etherstatsbroadcastpkts",
                                "etherstatscollisions",
                                "etherstatscrcalignerrors",
                                "etherstatscreatetime",
                                "etherstatsdatasource",
                                "etherstatsdropevents",
                                "etherstatsdroppedframes",
                                "etherstatsfragments",
                                "etherstatsjabbers",
                                "etherstatsmulticastpkts",
                                "etherstatsoctets",
                                "etherstatsoversizepkts",
                                "etherstatsowner",
                                "etherstatspkts",
                                "etherstatspkts1024to1518octets",
                                "etherstatspkts128to255octets",
                                "etherstatspkts256to511octets",
                                "etherstatspkts512to1023octets",
                                "etherstatspkts64octets",
                                "etherstatspkts65to127octets",
                                "etherstatsstatus",
                                "etherstatsundersizepkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Etherstatstable.Etherstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Etherstatstable.Etherstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.etherstatsindex.is_set or
                    self.etherstatsbroadcastpkts.is_set or
                    self.etherstatscollisions.is_set or
                    self.etherstatscrcalignerrors.is_set or
                    self.etherstatscreatetime.is_set or
                    self.etherstatsdatasource.is_set or
                    self.etherstatsdropevents.is_set or
                    self.etherstatsdroppedframes.is_set or
                    self.etherstatsfragments.is_set or
                    self.etherstatsjabbers.is_set or
                    self.etherstatsmulticastpkts.is_set or
                    self.etherstatsoctets.is_set or
                    self.etherstatsoversizepkts.is_set or
                    self.etherstatsowner.is_set or
                    self.etherstatspkts.is_set or
                    self.etherstatspkts1024to1518octets.is_set or
                    self.etherstatspkts128to255octets.is_set or
                    self.etherstatspkts256to511octets.is_set or
                    self.etherstatspkts512to1023octets.is_set or
                    self.etherstatspkts64octets.is_set or
                    self.etherstatspkts65to127octets.is_set or
                    self.etherstatsstatus.is_set or
                    self.etherstatsundersizepkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.etherstatsindex.yfilter != YFilter.not_set or
                    self.etherstatsbroadcastpkts.yfilter != YFilter.not_set or
                    self.etherstatscollisions.yfilter != YFilter.not_set or
                    self.etherstatscrcalignerrors.yfilter != YFilter.not_set or
                    self.etherstatscreatetime.yfilter != YFilter.not_set or
                    self.etherstatsdatasource.yfilter != YFilter.not_set or
                    self.etherstatsdropevents.yfilter != YFilter.not_set or
                    self.etherstatsdroppedframes.yfilter != YFilter.not_set or
                    self.etherstatsfragments.yfilter != YFilter.not_set or
                    self.etherstatsjabbers.yfilter != YFilter.not_set or
                    self.etherstatsmulticastpkts.yfilter != YFilter.not_set or
                    self.etherstatsoctets.yfilter != YFilter.not_set or
                    self.etherstatsoversizepkts.yfilter != YFilter.not_set or
                    self.etherstatsowner.yfilter != YFilter.not_set or
                    self.etherstatspkts.yfilter != YFilter.not_set or
                    self.etherstatspkts1024to1518octets.yfilter != YFilter.not_set or
                    self.etherstatspkts128to255octets.yfilter != YFilter.not_set or
                    self.etherstatspkts256to511octets.yfilter != YFilter.not_set or
                    self.etherstatspkts512to1023octets.yfilter != YFilter.not_set or
                    self.etherstatspkts64octets.yfilter != YFilter.not_set or
                    self.etherstatspkts65to127octets.yfilter != YFilter.not_set or
                    self.etherstatsstatus.yfilter != YFilter.not_set or
                    self.etherstatsundersizepkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherStatsEntry" + "[etherStatsIndex='" + self.etherstatsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/etherStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.etherstatsindex.is_set or self.etherstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsindex.get_name_leafdata())
                if (self.etherstatsbroadcastpkts.is_set or self.etherstatsbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsbroadcastpkts.get_name_leafdata())
                if (self.etherstatscollisions.is_set or self.etherstatscollisions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatscollisions.get_name_leafdata())
                if (self.etherstatscrcalignerrors.is_set or self.etherstatscrcalignerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatscrcalignerrors.get_name_leafdata())
                if (self.etherstatscreatetime.is_set or self.etherstatscreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatscreatetime.get_name_leafdata())
                if (self.etherstatsdatasource.is_set or self.etherstatsdatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsdatasource.get_name_leafdata())
                if (self.etherstatsdropevents.is_set or self.etherstatsdropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsdropevents.get_name_leafdata())
                if (self.etherstatsdroppedframes.is_set or self.etherstatsdroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsdroppedframes.get_name_leafdata())
                if (self.etherstatsfragments.is_set or self.etherstatsfragments.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsfragments.get_name_leafdata())
                if (self.etherstatsjabbers.is_set or self.etherstatsjabbers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsjabbers.get_name_leafdata())
                if (self.etherstatsmulticastpkts.is_set or self.etherstatsmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsmulticastpkts.get_name_leafdata())
                if (self.etherstatsoctets.is_set or self.etherstatsoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsoctets.get_name_leafdata())
                if (self.etherstatsoversizepkts.is_set or self.etherstatsoversizepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsoversizepkts.get_name_leafdata())
                if (self.etherstatsowner.is_set or self.etherstatsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsowner.get_name_leafdata())
                if (self.etherstatspkts.is_set or self.etherstatspkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts.get_name_leafdata())
                if (self.etherstatspkts1024to1518octets.is_set or self.etherstatspkts1024to1518octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts1024to1518octets.get_name_leafdata())
                if (self.etherstatspkts128to255octets.is_set or self.etherstatspkts128to255octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts128to255octets.get_name_leafdata())
                if (self.etherstatspkts256to511octets.is_set or self.etherstatspkts256to511octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts256to511octets.get_name_leafdata())
                if (self.etherstatspkts512to1023octets.is_set or self.etherstatspkts512to1023octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts512to1023octets.get_name_leafdata())
                if (self.etherstatspkts64octets.is_set or self.etherstatspkts64octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts64octets.get_name_leafdata())
                if (self.etherstatspkts65to127octets.is_set or self.etherstatspkts65to127octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatspkts65to127octets.get_name_leafdata())
                if (self.etherstatsstatus.is_set or self.etherstatsstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsstatus.get_name_leafdata())
                if (self.etherstatsundersizepkts.is_set or self.etherstatsundersizepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherstatsundersizepkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "etherStatsIndex" or name == "etherStatsBroadcastPkts" or name == "etherStatsCollisions" or name == "etherStatsCRCAlignErrors" or name == "etherStatsCreateTime" or name == "etherStatsDataSource" or name == "etherStatsDropEvents" or name == "etherStatsDroppedFrames" or name == "etherStatsFragments" or name == "etherStatsJabbers" or name == "etherStatsMulticastPkts" or name == "etherStatsOctets" or name == "etherStatsOversizePkts" or name == "etherStatsOwner" or name == "etherStatsPkts" or name == "etherStatsPkts1024to1518Octets" or name == "etherStatsPkts128to255Octets" or name == "etherStatsPkts256to511Octets" or name == "etherStatsPkts512to1023Octets" or name == "etherStatsPkts64Octets" or name == "etherStatsPkts65to127Octets" or name == "etherStatsStatus" or name == "etherStatsUndersizePkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "etherStatsIndex"):
                    self.etherstatsindex = value
                    self.etherstatsindex.value_namespace = name_space
                    self.etherstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsBroadcastPkts"):
                    self.etherstatsbroadcastpkts = value
                    self.etherstatsbroadcastpkts.value_namespace = name_space
                    self.etherstatsbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsCollisions"):
                    self.etherstatscollisions = value
                    self.etherstatscollisions.value_namespace = name_space
                    self.etherstatscollisions.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsCRCAlignErrors"):
                    self.etherstatscrcalignerrors = value
                    self.etherstatscrcalignerrors.value_namespace = name_space
                    self.etherstatscrcalignerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsCreateTime"):
                    self.etherstatscreatetime = value
                    self.etherstatscreatetime.value_namespace = name_space
                    self.etherstatscreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsDataSource"):
                    self.etherstatsdatasource = value
                    self.etherstatsdatasource.value_namespace = name_space
                    self.etherstatsdatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsDropEvents"):
                    self.etherstatsdropevents = value
                    self.etherstatsdropevents.value_namespace = name_space
                    self.etherstatsdropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsDroppedFrames"):
                    self.etherstatsdroppedframes = value
                    self.etherstatsdroppedframes.value_namespace = name_space
                    self.etherstatsdroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsFragments"):
                    self.etherstatsfragments = value
                    self.etherstatsfragments.value_namespace = name_space
                    self.etherstatsfragments.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsJabbers"):
                    self.etherstatsjabbers = value
                    self.etherstatsjabbers.value_namespace = name_space
                    self.etherstatsjabbers.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsMulticastPkts"):
                    self.etherstatsmulticastpkts = value
                    self.etherstatsmulticastpkts.value_namespace = name_space
                    self.etherstatsmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsOctets"):
                    self.etherstatsoctets = value
                    self.etherstatsoctets.value_namespace = name_space
                    self.etherstatsoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsOversizePkts"):
                    self.etherstatsoversizepkts = value
                    self.etherstatsoversizepkts.value_namespace = name_space
                    self.etherstatsoversizepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsOwner"):
                    self.etherstatsowner = value
                    self.etherstatsowner.value_namespace = name_space
                    self.etherstatsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts"):
                    self.etherstatspkts = value
                    self.etherstatspkts.value_namespace = name_space
                    self.etherstatspkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts1024to1518Octets"):
                    self.etherstatspkts1024to1518octets = value
                    self.etherstatspkts1024to1518octets.value_namespace = name_space
                    self.etherstatspkts1024to1518octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts128to255Octets"):
                    self.etherstatspkts128to255octets = value
                    self.etherstatspkts128to255octets.value_namespace = name_space
                    self.etherstatspkts128to255octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts256to511Octets"):
                    self.etherstatspkts256to511octets = value
                    self.etherstatspkts256to511octets.value_namespace = name_space
                    self.etherstatspkts256to511octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts512to1023Octets"):
                    self.etherstatspkts512to1023octets = value
                    self.etherstatspkts512to1023octets.value_namespace = name_space
                    self.etherstatspkts512to1023octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts64Octets"):
                    self.etherstatspkts64octets = value
                    self.etherstatspkts64octets.value_namespace = name_space
                    self.etherstatspkts64octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsPkts65to127Octets"):
                    self.etherstatspkts65to127octets = value
                    self.etherstatspkts65to127octets.value_namespace = name_space
                    self.etherstatspkts65to127octets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsStatus"):
                    self.etherstatsstatus = value
                    self.etherstatsstatus.value_namespace = name_space
                    self.etherstatsstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "etherStatsUndersizePkts"):
                    self.etherstatsundersizepkts = value
                    self.etherstatsundersizepkts.value_namespace = name_space
                    self.etherstatsundersizepkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.etherstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherStatsEntry"):
                for c in self.etherstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Etherstatstable.Etherstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Historycontroltable(Entity):
        """
        A list of history control entries.
        
        .. attribute:: historycontrolentry
        
        	A list of parameters that set up a periodic sampling of statistics.  As an example, an instance of the historyControlInterval object might be named historyControlInterval.2
        	**type**\: list of    :py:class:`Historycontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Historycontroltable.Historycontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Historycontroltable, self).__init__()

            self.yang_name = "historyControlTable"
            self.yang_parent_name = "RMON-MIB"

            self.historycontrolentry = YList(self)

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
                        super(RmonMib.Historycontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Historycontroltable, self).__setattr__(name, value)


        class Historycontrolentry(Entity):
            """
            A list of parameters that set up a periodic sampling of
            statistics.  As an example, an instance of the
            historyControlInterval object might be named
            historyControlInterval.2
            
            .. attribute:: historycontrolindex  <key>
            
            	An index that uniquely identifies an entry in the historyControl table.  Each such entry defines a set of samples at a particular interval for an interface on the device
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the media\-specific table associated with this historyControlEntry. When the associated historyControlBucketsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated historyControlBucketsRequested object.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the media\-specific table.  When the number of buckets reaches the value of this object and a new bucket is to be added to the media\-specific table, the oldest bucket associated with this historyControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the media\-specific table associated with this historyControlEntry.  Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated media\- specific entries may be allowed to grow
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the media\-specific table associated with this historyControlEntry.  When this object is created or modified, the probe should set historyControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: historycontroldatasource
            
            	This object identifies the source of the data for which historical data was collected and placed in a media\-specific table on behalf of this historyControlEntry.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in  RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: historycontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this      collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: historycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the media\-specific table associated with this historyControlEntry.  This interval can be set to any number of seconds between 1 and 3600 (1 hour).  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of the associated counters.  It is important to consider the minimum time in which any counter could overflow on a particular media type and set the historyControlInterval object to a value less than this interval.  This is typically most important for the 'octets' counter in any media\-specific table.  For example, on an Ethernet network, the etherHistoryOctets counter could overflow in about one hour at the Ethernet's maximum utilization.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: Seconds
            
            .. attribute:: historycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: historycontrolstatus
            
            	The status of this historyControl entry.  Each instance of the media\-specific table associated with this historyControlEntry will be deleted by the agent if this historyControlEntry is not equal to valid(1)
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Historycontroltable.Historycontrolentry, self).__init__()

                self.yang_name = "historyControlEntry"
                self.yang_parent_name = "historyControlTable"

                self.historycontrolindex = YLeaf(YType.int32, "historyControlIndex")

                self.historycontrolbucketsgranted = YLeaf(YType.int32, "historyControlBucketsGranted")

                self.historycontrolbucketsrequested = YLeaf(YType.int32, "historyControlBucketsRequested")

                self.historycontroldatasource = YLeaf(YType.str, "historyControlDataSource")

                self.historycontroldroppedframes = YLeaf(YType.uint32, "RMON2-MIB:historyControlDroppedFrames")

                self.historycontrolinterval = YLeaf(YType.int32, "historyControlInterval")

                self.historycontrolowner = YLeaf(YType.str, "historyControlOwner")

                self.historycontrolstatus = YLeaf(YType.enumeration, "historyControlStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("historycontrolindex",
                                "historycontrolbucketsgranted",
                                "historycontrolbucketsrequested",
                                "historycontroldatasource",
                                "historycontroldroppedframes",
                                "historycontrolinterval",
                                "historycontrolowner",
                                "historycontrolstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Historycontroltable.Historycontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Historycontroltable.Historycontrolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.historycontrolindex.is_set or
                    self.historycontrolbucketsgranted.is_set or
                    self.historycontrolbucketsrequested.is_set or
                    self.historycontroldatasource.is_set or
                    self.historycontroldroppedframes.is_set or
                    self.historycontrolinterval.is_set or
                    self.historycontrolowner.is_set or
                    self.historycontrolstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.historycontrolindex.yfilter != YFilter.not_set or
                    self.historycontrolbucketsgranted.yfilter != YFilter.not_set or
                    self.historycontrolbucketsrequested.yfilter != YFilter.not_set or
                    self.historycontroldatasource.yfilter != YFilter.not_set or
                    self.historycontroldroppedframes.yfilter != YFilter.not_set or
                    self.historycontrolinterval.yfilter != YFilter.not_set or
                    self.historycontrolowner.yfilter != YFilter.not_set or
                    self.historycontrolstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "historyControlEntry" + "[historyControlIndex='" + self.historycontrolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/historyControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.historycontrolindex.is_set or self.historycontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolindex.get_name_leafdata())
                if (self.historycontrolbucketsgranted.is_set or self.historycontrolbucketsgranted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolbucketsgranted.get_name_leafdata())
                if (self.historycontrolbucketsrequested.is_set or self.historycontrolbucketsrequested.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolbucketsrequested.get_name_leafdata())
                if (self.historycontroldatasource.is_set or self.historycontroldatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontroldatasource.get_name_leafdata())
                if (self.historycontroldroppedframes.is_set or self.historycontroldroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontroldroppedframes.get_name_leafdata())
                if (self.historycontrolinterval.is_set or self.historycontrolinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolinterval.get_name_leafdata())
                if (self.historycontrolowner.is_set or self.historycontrolowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolowner.get_name_leafdata())
                if (self.historycontrolstatus.is_set or self.historycontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.historycontrolstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "historyControlIndex" or name == "historyControlBucketsGranted" or name == "historyControlBucketsRequested" or name == "historyControlDataSource" or name == "historyControlDroppedFrames" or name == "historyControlInterval" or name == "historyControlOwner" or name == "historyControlStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "historyControlIndex"):
                    self.historycontrolindex = value
                    self.historycontrolindex.value_namespace = name_space
                    self.historycontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlBucketsGranted"):
                    self.historycontrolbucketsgranted = value
                    self.historycontrolbucketsgranted.value_namespace = name_space
                    self.historycontrolbucketsgranted.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlBucketsRequested"):
                    self.historycontrolbucketsrequested = value
                    self.historycontrolbucketsrequested.value_namespace = name_space
                    self.historycontrolbucketsrequested.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlDataSource"):
                    self.historycontroldatasource = value
                    self.historycontroldatasource.value_namespace = name_space
                    self.historycontroldatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlDroppedFrames"):
                    self.historycontroldroppedframes = value
                    self.historycontroldroppedframes.value_namespace = name_space
                    self.historycontroldroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlInterval"):
                    self.historycontrolinterval = value
                    self.historycontrolinterval.value_namespace = name_space
                    self.historycontrolinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlOwner"):
                    self.historycontrolowner = value
                    self.historycontrolowner.value_namespace = name_space
                    self.historycontrolowner.value_namespace_prefix = name_space_prefix
                if(value_path == "historyControlStatus"):
                    self.historycontrolstatus = value
                    self.historycontrolstatus.value_namespace = name_space
                    self.historycontrolstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.historycontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.historycontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "historyControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "historyControlEntry"):
                for c in self.historycontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Historycontroltable.Historycontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.historycontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "historyControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Etherhistorytable(Entity):
        """
        A list of Ethernet history entries.
        
        .. attribute:: etherhistoryentry
        
        	An historical sample of Ethernet statistics on a particular Ethernet interface.  This sample is associated with the historyControlEntry which set up the parameters for a regular collection of these samples.  As an example, an instance of the etherHistoryPkts object might be named etherHistoryPkts.2.89
        	**type**\: list of    :py:class:`Etherhistoryentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Etherhistorytable.Etherhistoryentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Etherhistorytable, self).__init__()

            self.yang_name = "etherHistoryTable"
            self.yang_parent_name = "RMON-MIB"

            self.etherhistoryentry = YList(self)

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
                        super(RmonMib.Etherhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Etherhistorytable, self).__setattr__(name, value)


        class Etherhistoryentry(Entity):
            """
            An historical sample of Ethernet statistics on a particular
            Ethernet interface.  This sample is associated with the
            historyControlEntry which set up the parameters for
            a regular collection of these samples.  As an example, an
            instance of the etherHistoryPkts object might be named
            etherHistoryPkts.2.89
            
            .. attribute:: etherhistoryindex  <key>
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: etherhistorysampleindex  <key>
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherhistorybroadcastpkts
            
            	The number of good packets received during this sampling interval that were directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorycollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment during this sampling interval.  The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE\-5) and section 10.3.1.3 (10BASE\-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously.  A repeater port must detect a collision when two or more stations are transmitting simultaneously.  Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would.  Probe location plays a much smaller role when considering 10BASE\-T.  14.2.1.4 (10BASE\-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time).  A 10BASE\-T station can only detect collisions when it is transmitting.  Thus probes placed on a station and a repeater, should report the same number of collisions.  Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Collisions
            
            .. attribute:: etherhistorycrcalignerrors
            
            	The number of packets received during this sampling interval that had a length (excluding framing bits but including FCS octets) between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryfragments
            
            	The total number of packets received during this sampling interval that were less than 64 octets in length (excluding framing bits but including FCS octets) had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that it is entirely normal for etherHistoryFragments to increment.  This is because it counts both runts (which are normal occurrences due to collisions) and noise hits
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryjabbers
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets), and  had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non\-integral number of octets (Alignment Error).  Note that this definition of jabber is different than the definition in IEEE\-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2).  These documents define jabber as the condition where any packet exceeds 20 ms.  The allowed range to detect jabber is between 20 ms and 150 ms
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorymulticastpkts
            
            	The number of good packets received during this sampling interval that were directed to a multicast address.  Note that this number does not include packets addressed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: etherhistoryoversizepkts
            
            	The number of packets received during this sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets) but were otherwise well formed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistorypkts
            
            	The number of packets (including bad packets) received during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryundersizepkts
            
            	The number of packets received during this sampling interval that were less than 64 octets long (excluding framing bits but including FCS octets) and were otherwise well formed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: etherhistoryutilization
            
            	The best estimate of the mean physical layer network utilization on this interface during this sampling interval, in hundredths of a percent
            	**type**\:  int
            
            	**range:** 0..10000
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Etherhistorytable.Etherhistoryentry, self).__init__()

                self.yang_name = "etherHistoryEntry"
                self.yang_parent_name = "etherHistoryTable"

                self.etherhistoryindex = YLeaf(YType.int32, "etherHistoryIndex")

                self.etherhistorysampleindex = YLeaf(YType.int32, "etherHistorySampleIndex")

                self.etherhistorybroadcastpkts = YLeaf(YType.uint32, "etherHistoryBroadcastPkts")

                self.etherhistorycollisions = YLeaf(YType.uint32, "etherHistoryCollisions")

                self.etherhistorycrcalignerrors = YLeaf(YType.uint32, "etherHistoryCRCAlignErrors")

                self.etherhistorydropevents = YLeaf(YType.uint32, "etherHistoryDropEvents")

                self.etherhistoryfragments = YLeaf(YType.uint32, "etherHistoryFragments")

                self.etherhistoryintervalstart = YLeaf(YType.uint32, "etherHistoryIntervalStart")

                self.etherhistoryjabbers = YLeaf(YType.uint32, "etherHistoryJabbers")

                self.etherhistorymulticastpkts = YLeaf(YType.uint32, "etherHistoryMulticastPkts")

                self.etherhistoryoctets = YLeaf(YType.uint32, "etherHistoryOctets")

                self.etherhistoryoversizepkts = YLeaf(YType.uint32, "etherHistoryOversizePkts")

                self.etherhistorypkts = YLeaf(YType.uint32, "etherHistoryPkts")

                self.etherhistoryundersizepkts = YLeaf(YType.uint32, "etherHistoryUndersizePkts")

                self.etherhistoryutilization = YLeaf(YType.int32, "etherHistoryUtilization")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("etherhistoryindex",
                                "etherhistorysampleindex",
                                "etherhistorybroadcastpkts",
                                "etherhistorycollisions",
                                "etherhistorycrcalignerrors",
                                "etherhistorydropevents",
                                "etherhistoryfragments",
                                "etherhistoryintervalstart",
                                "etherhistoryjabbers",
                                "etherhistorymulticastpkts",
                                "etherhistoryoctets",
                                "etherhistoryoversizepkts",
                                "etherhistorypkts",
                                "etherhistoryundersizepkts",
                                "etherhistoryutilization") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Etherhistorytable.Etherhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Etherhistorytable.Etherhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.etherhistoryindex.is_set or
                    self.etherhistorysampleindex.is_set or
                    self.etherhistorybroadcastpkts.is_set or
                    self.etherhistorycollisions.is_set or
                    self.etherhistorycrcalignerrors.is_set or
                    self.etherhistorydropevents.is_set or
                    self.etherhistoryfragments.is_set or
                    self.etherhistoryintervalstart.is_set or
                    self.etherhistoryjabbers.is_set or
                    self.etherhistorymulticastpkts.is_set or
                    self.etherhistoryoctets.is_set or
                    self.etherhistoryoversizepkts.is_set or
                    self.etherhistorypkts.is_set or
                    self.etherhistoryundersizepkts.is_set or
                    self.etherhistoryutilization.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.etherhistoryindex.yfilter != YFilter.not_set or
                    self.etherhistorysampleindex.yfilter != YFilter.not_set or
                    self.etherhistorybroadcastpkts.yfilter != YFilter.not_set or
                    self.etherhistorycollisions.yfilter != YFilter.not_set or
                    self.etherhistorycrcalignerrors.yfilter != YFilter.not_set or
                    self.etherhistorydropevents.yfilter != YFilter.not_set or
                    self.etherhistoryfragments.yfilter != YFilter.not_set or
                    self.etherhistoryintervalstart.yfilter != YFilter.not_set or
                    self.etherhistoryjabbers.yfilter != YFilter.not_set or
                    self.etherhistorymulticastpkts.yfilter != YFilter.not_set or
                    self.etherhistoryoctets.yfilter != YFilter.not_set or
                    self.etherhistoryoversizepkts.yfilter != YFilter.not_set or
                    self.etherhistorypkts.yfilter != YFilter.not_set or
                    self.etherhistoryundersizepkts.yfilter != YFilter.not_set or
                    self.etherhistoryutilization.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherHistoryEntry" + "[etherHistoryIndex='" + self.etherhistoryindex.get() + "']" + "[etherHistorySampleIndex='" + self.etherhistorysampleindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/etherHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.etherhistoryindex.is_set or self.etherhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryindex.get_name_leafdata())
                if (self.etherhistorysampleindex.is_set or self.etherhistorysampleindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorysampleindex.get_name_leafdata())
                if (self.etherhistorybroadcastpkts.is_set or self.etherhistorybroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorybroadcastpkts.get_name_leafdata())
                if (self.etherhistorycollisions.is_set or self.etherhistorycollisions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorycollisions.get_name_leafdata())
                if (self.etherhistorycrcalignerrors.is_set or self.etherhistorycrcalignerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorycrcalignerrors.get_name_leafdata())
                if (self.etherhistorydropevents.is_set or self.etherhistorydropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorydropevents.get_name_leafdata())
                if (self.etherhistoryfragments.is_set or self.etherhistoryfragments.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryfragments.get_name_leafdata())
                if (self.etherhistoryintervalstart.is_set or self.etherhistoryintervalstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryintervalstart.get_name_leafdata())
                if (self.etherhistoryjabbers.is_set or self.etherhistoryjabbers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryjabbers.get_name_leafdata())
                if (self.etherhistorymulticastpkts.is_set or self.etherhistorymulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorymulticastpkts.get_name_leafdata())
                if (self.etherhistoryoctets.is_set or self.etherhistoryoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryoctets.get_name_leafdata())
                if (self.etherhistoryoversizepkts.is_set or self.etherhistoryoversizepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryoversizepkts.get_name_leafdata())
                if (self.etherhistorypkts.is_set or self.etherhistorypkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistorypkts.get_name_leafdata())
                if (self.etherhistoryundersizepkts.is_set or self.etherhistoryundersizepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryundersizepkts.get_name_leafdata())
                if (self.etherhistoryutilization.is_set or self.etherhistoryutilization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherhistoryutilization.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "etherHistoryIndex" or name == "etherHistorySampleIndex" or name == "etherHistoryBroadcastPkts" or name == "etherHistoryCollisions" or name == "etherHistoryCRCAlignErrors" or name == "etherHistoryDropEvents" or name == "etherHistoryFragments" or name == "etherHistoryIntervalStart" or name == "etherHistoryJabbers" or name == "etherHistoryMulticastPkts" or name == "etherHistoryOctets" or name == "etherHistoryOversizePkts" or name == "etherHistoryPkts" or name == "etherHistoryUndersizePkts" or name == "etherHistoryUtilization"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "etherHistoryIndex"):
                    self.etherhistoryindex = value
                    self.etherhistoryindex.value_namespace = name_space
                    self.etherhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistorySampleIndex"):
                    self.etherhistorysampleindex = value
                    self.etherhistorysampleindex.value_namespace = name_space
                    self.etherhistorysampleindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryBroadcastPkts"):
                    self.etherhistorybroadcastpkts = value
                    self.etherhistorybroadcastpkts.value_namespace = name_space
                    self.etherhistorybroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryCollisions"):
                    self.etherhistorycollisions = value
                    self.etherhistorycollisions.value_namespace = name_space
                    self.etherhistorycollisions.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryCRCAlignErrors"):
                    self.etherhistorycrcalignerrors = value
                    self.etherhistorycrcalignerrors.value_namespace = name_space
                    self.etherhistorycrcalignerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryDropEvents"):
                    self.etherhistorydropevents = value
                    self.etherhistorydropevents.value_namespace = name_space
                    self.etherhistorydropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryFragments"):
                    self.etherhistoryfragments = value
                    self.etherhistoryfragments.value_namespace = name_space
                    self.etherhistoryfragments.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryIntervalStart"):
                    self.etherhistoryintervalstart = value
                    self.etherhistoryintervalstart.value_namespace = name_space
                    self.etherhistoryintervalstart.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryJabbers"):
                    self.etherhistoryjabbers = value
                    self.etherhistoryjabbers.value_namespace = name_space
                    self.etherhistoryjabbers.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryMulticastPkts"):
                    self.etherhistorymulticastpkts = value
                    self.etherhistorymulticastpkts.value_namespace = name_space
                    self.etherhistorymulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryOctets"):
                    self.etherhistoryoctets = value
                    self.etherhistoryoctets.value_namespace = name_space
                    self.etherhistoryoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryOversizePkts"):
                    self.etherhistoryoversizepkts = value
                    self.etherhistoryoversizepkts.value_namespace = name_space
                    self.etherhistoryoversizepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryPkts"):
                    self.etherhistorypkts = value
                    self.etherhistorypkts.value_namespace = name_space
                    self.etherhistorypkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryUndersizePkts"):
                    self.etherhistoryundersizepkts = value
                    self.etherhistoryundersizepkts.value_namespace = name_space
                    self.etherhistoryundersizepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "etherHistoryUtilization"):
                    self.etherhistoryutilization = value
                    self.etherhistoryutilization.value_namespace = name_space
                    self.etherhistoryutilization.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.etherhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherHistoryEntry"):
                for c in self.etherhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Etherhistorytable.Etherhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Alarmtable(Entity):
        """
        A list of alarm entries.
        
        .. attribute:: alarmentry
        
        	A list of parameters that set up a periodic checking for alarm conditions.  For example, an instance of the alarmValue object might be named alarmValue.8
        	**type**\: list of    :py:class:`Alarmentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Alarmtable.Alarmentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Alarmtable, self).__init__()

            self.yang_name = "alarmTable"
            self.yang_parent_name = "RMON-MIB"

            self.alarmentry = YList(self)

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
                        super(RmonMib.Alarmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Alarmtable, self).__setattr__(name, value)


        class Alarmentry(Entity):
            """
            A list of parameters that set up a periodic checking
            for alarm conditions.  For example, an instance of the
            alarmValue object might be named alarmValue.8
            
            .. attribute:: alarmindex  <key>
            
            	An index that uniquely identifies an entry in the alarm table.  Each such entry defines a diagnostic sample at a particular interval for an object on the device
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: alarmfallingeventindex
            
            	The index of the eventEntry that is used when a falling threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: alarmfallingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is less than or equal to this threshold and the associated alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3).  After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the alarmRisingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarminterval
            
            	The interval in seconds over which the data is sampled and compared with the rising and falling thresholds.  When setting this variable, care should be taken in the case of deltaValue sampling \- the interval should be set short enough that the sampled variable is very unlikely to increase or decrease by more than 2^31 \- 1 during a single sampling interval.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: alarmowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: alarmrisingeventindex
            
            	The index of the eventEntry that is used when a rising threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: alarmrisingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is greater than or equal to this threshold and the associated alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3).  After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the alarmFallingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmsampletype
            
            	The method of sampling the selected variable and calculating the value to be compared against the thresholds.  If the value of this object is absoluteValue(1), the value of the selected variable will be compared directly with the thresholds at the end of the sampling interval.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference compared with the thresholds.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:   :py:class:`Alarmsampletype <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Alarmtable.Alarmentry.Alarmsampletype>`
            
            .. attribute:: alarmstartupalarm
            
            	The alarm that may be sent when this entry is first set to valid.  If the first sample after this entry becomes valid is greater than or equal to the risingThreshold and alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single rising alarm will be generated.  If the first sample after this entry becomes valid is less than or equal to the fallingThreshold and alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single falling alarm will be generated.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:   :py:class:`Alarmstartupalarm <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Alarmtable.Alarmentry.Alarmstartupalarm>`
            
            .. attribute:: alarmstatus
            
            	The status of this alarm entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: alarmvalue
            
            	The value of the statistic during the last sampling period.  For example, if the sample type is deltaValue, this value will be the difference between the samples at the beginning and end of the period.  If the sample type is absoluteValue, this value will be the sampled value at the end of the period. This is the value that is compared with the rising and falling thresholds.  The value during the current sampling period is not made available until the period is completed and will remain available until the next period completes
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view.  Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  If at any time the variable name of an established alarmEntry is no longer available in the selected MIB view, the probe must change the status of this alarmEntry to invalid(4).  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Alarmtable.Alarmentry, self).__init__()

                self.yang_name = "alarmEntry"
                self.yang_parent_name = "alarmTable"

                self.alarmindex = YLeaf(YType.int32, "alarmIndex")

                self.alarmfallingeventindex = YLeaf(YType.int32, "alarmFallingEventIndex")

                self.alarmfallingthreshold = YLeaf(YType.int32, "alarmFallingThreshold")

                self.alarminterval = YLeaf(YType.int32, "alarmInterval")

                self.alarmowner = YLeaf(YType.str, "alarmOwner")

                self.alarmrisingeventindex = YLeaf(YType.int32, "alarmRisingEventIndex")

                self.alarmrisingthreshold = YLeaf(YType.int32, "alarmRisingThreshold")

                self.alarmsampletype = YLeaf(YType.enumeration, "alarmSampleType")

                self.alarmstartupalarm = YLeaf(YType.enumeration, "alarmStartupAlarm")

                self.alarmstatus = YLeaf(YType.enumeration, "alarmStatus")

                self.alarmvalue = YLeaf(YType.int32, "alarmValue")

                self.alarmvariable = YLeaf(YType.str, "alarmVariable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("alarmindex",
                                "alarmfallingeventindex",
                                "alarmfallingthreshold",
                                "alarminterval",
                                "alarmowner",
                                "alarmrisingeventindex",
                                "alarmrisingthreshold",
                                "alarmsampletype",
                                "alarmstartupalarm",
                                "alarmstatus",
                                "alarmvalue",
                                "alarmvariable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Alarmtable.Alarmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Alarmtable.Alarmentry, self).__setattr__(name, value)

            class Alarmsampletype(Enum):
                """
                Alarmsampletype

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
                Alarmstartupalarm

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


            def has_data(self):
                return (
                    self.alarmindex.is_set or
                    self.alarmfallingeventindex.is_set or
                    self.alarmfallingthreshold.is_set or
                    self.alarminterval.is_set or
                    self.alarmowner.is_set or
                    self.alarmrisingeventindex.is_set or
                    self.alarmrisingthreshold.is_set or
                    self.alarmsampletype.is_set or
                    self.alarmstartupalarm.is_set or
                    self.alarmstatus.is_set or
                    self.alarmvalue.is_set or
                    self.alarmvariable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.alarmindex.yfilter != YFilter.not_set or
                    self.alarmfallingeventindex.yfilter != YFilter.not_set or
                    self.alarmfallingthreshold.yfilter != YFilter.not_set or
                    self.alarminterval.yfilter != YFilter.not_set or
                    self.alarmowner.yfilter != YFilter.not_set or
                    self.alarmrisingeventindex.yfilter != YFilter.not_set or
                    self.alarmrisingthreshold.yfilter != YFilter.not_set or
                    self.alarmsampletype.yfilter != YFilter.not_set or
                    self.alarmstartupalarm.yfilter != YFilter.not_set or
                    self.alarmstatus.yfilter != YFilter.not_set or
                    self.alarmvalue.yfilter != YFilter.not_set or
                    self.alarmvariable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "alarmEntry" + "[alarmIndex='" + self.alarmindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/alarmTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.alarmindex.is_set or self.alarmindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmindex.get_name_leafdata())
                if (self.alarmfallingeventindex.is_set or self.alarmfallingeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmfallingeventindex.get_name_leafdata())
                if (self.alarmfallingthreshold.is_set or self.alarmfallingthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmfallingthreshold.get_name_leafdata())
                if (self.alarminterval.is_set or self.alarminterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarminterval.get_name_leafdata())
                if (self.alarmowner.is_set or self.alarmowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmowner.get_name_leafdata())
                if (self.alarmrisingeventindex.is_set or self.alarmrisingeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmrisingeventindex.get_name_leafdata())
                if (self.alarmrisingthreshold.is_set or self.alarmrisingthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmrisingthreshold.get_name_leafdata())
                if (self.alarmsampletype.is_set or self.alarmsampletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmsampletype.get_name_leafdata())
                if (self.alarmstartupalarm.is_set or self.alarmstartupalarm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmstartupalarm.get_name_leafdata())
                if (self.alarmstatus.is_set or self.alarmstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmstatus.get_name_leafdata())
                if (self.alarmvalue.is_set or self.alarmvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmvalue.get_name_leafdata())
                if (self.alarmvariable.is_set or self.alarmvariable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarmvariable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "alarmIndex" or name == "alarmFallingEventIndex" or name == "alarmFallingThreshold" or name == "alarmInterval" or name == "alarmOwner" or name == "alarmRisingEventIndex" or name == "alarmRisingThreshold" or name == "alarmSampleType" or name == "alarmStartupAlarm" or name == "alarmStatus" or name == "alarmValue" or name == "alarmVariable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "alarmIndex"):
                    self.alarmindex = value
                    self.alarmindex.value_namespace = name_space
                    self.alarmindex.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmFallingEventIndex"):
                    self.alarmfallingeventindex = value
                    self.alarmfallingeventindex.value_namespace = name_space
                    self.alarmfallingeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmFallingThreshold"):
                    self.alarmfallingthreshold = value
                    self.alarmfallingthreshold.value_namespace = name_space
                    self.alarmfallingthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmInterval"):
                    self.alarminterval = value
                    self.alarminterval.value_namespace = name_space
                    self.alarminterval.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmOwner"):
                    self.alarmowner = value
                    self.alarmowner.value_namespace = name_space
                    self.alarmowner.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmRisingEventIndex"):
                    self.alarmrisingeventindex = value
                    self.alarmrisingeventindex.value_namespace = name_space
                    self.alarmrisingeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmRisingThreshold"):
                    self.alarmrisingthreshold = value
                    self.alarmrisingthreshold.value_namespace = name_space
                    self.alarmrisingthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmSampleType"):
                    self.alarmsampletype = value
                    self.alarmsampletype.value_namespace = name_space
                    self.alarmsampletype.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmStartupAlarm"):
                    self.alarmstartupalarm = value
                    self.alarmstartupalarm.value_namespace = name_space
                    self.alarmstartupalarm.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmStatus"):
                    self.alarmstatus = value
                    self.alarmstatus.value_namespace = name_space
                    self.alarmstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmValue"):
                    self.alarmvalue = value
                    self.alarmvalue.value_namespace = name_space
                    self.alarmvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "alarmVariable"):
                    self.alarmvariable = value
                    self.alarmvariable.value_namespace = name_space
                    self.alarmvariable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.alarmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.alarmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "alarmTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "alarmEntry"):
                for c in self.alarmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Alarmtable.Alarmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.alarmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "alarmEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Hostcontroltable(Entity):
        """
        A list of host table control entries.
        
        .. attribute:: hostcontrolentry
        
        	A list of parameters that set up the discovery of hosts on a particular interface and the collection of statistics about these hosts.  For example, an instance of the hostControlTableSize object might be named hostControlTableSize.1
        	**type**\: list of    :py:class:`Hostcontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hostcontroltable.Hostcontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Hostcontroltable, self).__init__()

            self.yang_name = "hostControlTable"
            self.yang_parent_name = "RMON-MIB"

            self.hostcontrolentry = YList(self)

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
                        super(RmonMib.Hostcontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Hostcontroltable, self).__setattr__(name, value)


        class Hostcontrolentry(Entity):
            """
            A list of parameters that set up the discovery of hosts
            on a particular interface and the collection of statistics
            about these hosts.  For example, an instance of the
            hostControlTableSize object might be named
            hostControlTableSize.1
            
            .. attribute:: hostcontrolindex  <key>
            
            	An index that uniquely identifies an entry in the hostControl table.  Each such entry defines a function that discovers hosts on a particular interface and places statistics about them in the hostTable and the hostTimeTable on behalf of this hostControlEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hostcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontroldatasource
            
            	This object identifies the source of the data for this instance of the host function.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated hostControlStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hostcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the hostTable associated with this hostControlEntry.  If no deletions have occurred, this value shall be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: hostcontrolstatus
            
            	The status of this hostControl entry.  If this object is not equal to valid(1), all associated entries in the hostTable, hostTimeTable, and the hostTopNTable shall be deleted by the agent
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: hostcontroltablesize
            
            	The number of hostEntries in the hostTable and the hostTimeTable associated with this hostControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Hostcontroltable.Hostcontrolentry, self).__init__()

                self.yang_name = "hostControlEntry"
                self.yang_parent_name = "hostControlTable"

                self.hostcontrolindex = YLeaf(YType.int32, "hostControlIndex")

                self.hostcontrolcreatetime = YLeaf(YType.uint32, "RMON2-MIB:hostControlCreateTime")

                self.hostcontroldatasource = YLeaf(YType.str, "hostControlDataSource")

                self.hostcontroldroppedframes = YLeaf(YType.uint32, "RMON2-MIB:hostControlDroppedFrames")

                self.hostcontrollastdeletetime = YLeaf(YType.uint32, "hostControlLastDeleteTime")

                self.hostcontrolowner = YLeaf(YType.str, "hostControlOwner")

                self.hostcontrolstatus = YLeaf(YType.enumeration, "hostControlStatus")

                self.hostcontroltablesize = YLeaf(YType.int32, "hostControlTableSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hostcontrolindex",
                                "hostcontrolcreatetime",
                                "hostcontroldatasource",
                                "hostcontroldroppedframes",
                                "hostcontrollastdeletetime",
                                "hostcontrolowner",
                                "hostcontrolstatus",
                                "hostcontroltablesize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Hostcontroltable.Hostcontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Hostcontroltable.Hostcontrolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hostcontrolindex.is_set or
                    self.hostcontrolcreatetime.is_set or
                    self.hostcontroldatasource.is_set or
                    self.hostcontroldroppedframes.is_set or
                    self.hostcontrollastdeletetime.is_set or
                    self.hostcontrolowner.is_set or
                    self.hostcontrolstatus.is_set or
                    self.hostcontroltablesize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hostcontrolindex.yfilter != YFilter.not_set or
                    self.hostcontrolcreatetime.yfilter != YFilter.not_set or
                    self.hostcontroldatasource.yfilter != YFilter.not_set or
                    self.hostcontroldroppedframes.yfilter != YFilter.not_set or
                    self.hostcontrollastdeletetime.yfilter != YFilter.not_set or
                    self.hostcontrolowner.yfilter != YFilter.not_set or
                    self.hostcontrolstatus.yfilter != YFilter.not_set or
                    self.hostcontroltablesize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hostControlEntry" + "[hostControlIndex='" + self.hostcontrolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/hostControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hostcontrolindex.is_set or self.hostcontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontrolindex.get_name_leafdata())
                if (self.hostcontrolcreatetime.is_set or self.hostcontrolcreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontrolcreatetime.get_name_leafdata())
                if (self.hostcontroldatasource.is_set or self.hostcontroldatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontroldatasource.get_name_leafdata())
                if (self.hostcontroldroppedframes.is_set or self.hostcontroldroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontroldroppedframes.get_name_leafdata())
                if (self.hostcontrollastdeletetime.is_set or self.hostcontrollastdeletetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontrollastdeletetime.get_name_leafdata())
                if (self.hostcontrolowner.is_set or self.hostcontrolowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontrolowner.get_name_leafdata())
                if (self.hostcontrolstatus.is_set or self.hostcontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontrolstatus.get_name_leafdata())
                if (self.hostcontroltablesize.is_set or self.hostcontroltablesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcontroltablesize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hostControlIndex" or name == "hostControlCreateTime" or name == "hostControlDataSource" or name == "hostControlDroppedFrames" or name == "hostControlLastDeleteTime" or name == "hostControlOwner" or name == "hostControlStatus" or name == "hostControlTableSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hostControlIndex"):
                    self.hostcontrolindex = value
                    self.hostcontrolindex.value_namespace = name_space
                    self.hostcontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlCreateTime"):
                    self.hostcontrolcreatetime = value
                    self.hostcontrolcreatetime.value_namespace = name_space
                    self.hostcontrolcreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlDataSource"):
                    self.hostcontroldatasource = value
                    self.hostcontroldatasource.value_namespace = name_space
                    self.hostcontroldatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlDroppedFrames"):
                    self.hostcontroldroppedframes = value
                    self.hostcontroldroppedframes.value_namespace = name_space
                    self.hostcontroldroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlLastDeleteTime"):
                    self.hostcontrollastdeletetime = value
                    self.hostcontrollastdeletetime.value_namespace = name_space
                    self.hostcontrollastdeletetime.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlOwner"):
                    self.hostcontrolowner = value
                    self.hostcontrolowner.value_namespace = name_space
                    self.hostcontrolowner.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlStatus"):
                    self.hostcontrolstatus = value
                    self.hostcontrolstatus.value_namespace = name_space
                    self.hostcontrolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "hostControlTableSize"):
                    self.hostcontroltablesize = value
                    self.hostcontroltablesize.value_namespace = name_space
                    self.hostcontroltablesize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.hostcontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.hostcontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hostControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hostControlEntry"):
                for c in self.hostcontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Hostcontroltable.Hostcontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.hostcontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hostControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Hosttable(Entity):
        """
        A list of host entries.
        
        .. attribute:: hostentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  For example, an instance of the hostOutBroadcastPkts object might be named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
        	**type**\: list of    :py:class:`Hostentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttable.Hostentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Hosttable, self).__init__()

            self.yang_name = "hostTable"
            self.yang_parent_name = "RMON-MIB"

            self.hostentry = YList(self)

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
                        super(RmonMib.Hosttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Hosttable, self).__setattr__(name, value)


        class Hostentry(Entity):
            """
            A collection of statistics for a particular host that has
            been discovered on an interface of this device.  For example,
            an instance of the hostOutBroadcastPkts object might be
            named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
            
            .. attribute:: hostindex  <key>
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hostaddress  <key>
            
            	The physical address of this host
            	**type**\:  str
            
            .. attribute:: hostcreationorder
            
            	An index that defines the relative ordering of the creation time of hosts captured for a particular hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later.  It is important to note that the order for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTable.  By observing this variable, the management station may detect the circumstances where a previous association between a value of hostCreationOrder and a hostEntry may no longer hold
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hostinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hostinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTable. Note that this number does not include packets directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hostoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hostoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Hosttable.Hostentry, self).__init__()

                self.yang_name = "hostEntry"
                self.yang_parent_name = "hostTable"

                self.hostindex = YLeaf(YType.int32, "hostIndex")

                self.hostaddress = YLeaf(YType.str, "hostAddress")

                self.hostcreationorder = YLeaf(YType.int32, "hostCreationOrder")

                self.hostinoctets = YLeaf(YType.uint32, "hostInOctets")

                self.hostinpkts = YLeaf(YType.uint32, "hostInPkts")

                self.hostoutbroadcastpkts = YLeaf(YType.uint32, "hostOutBroadcastPkts")

                self.hostouterrors = YLeaf(YType.uint32, "hostOutErrors")

                self.hostoutmulticastpkts = YLeaf(YType.uint32, "hostOutMulticastPkts")

                self.hostoutoctets = YLeaf(YType.uint32, "hostOutOctets")

                self.hostoutpkts = YLeaf(YType.uint32, "hostOutPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hostindex",
                                "hostaddress",
                                "hostcreationorder",
                                "hostinoctets",
                                "hostinpkts",
                                "hostoutbroadcastpkts",
                                "hostouterrors",
                                "hostoutmulticastpkts",
                                "hostoutoctets",
                                "hostoutpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Hosttable.Hostentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Hosttable.Hostentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hostindex.is_set or
                    self.hostaddress.is_set or
                    self.hostcreationorder.is_set or
                    self.hostinoctets.is_set or
                    self.hostinpkts.is_set or
                    self.hostoutbroadcastpkts.is_set or
                    self.hostouterrors.is_set or
                    self.hostoutmulticastpkts.is_set or
                    self.hostoutoctets.is_set or
                    self.hostoutpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hostindex.yfilter != YFilter.not_set or
                    self.hostaddress.yfilter != YFilter.not_set or
                    self.hostcreationorder.yfilter != YFilter.not_set or
                    self.hostinoctets.yfilter != YFilter.not_set or
                    self.hostinpkts.yfilter != YFilter.not_set or
                    self.hostoutbroadcastpkts.yfilter != YFilter.not_set or
                    self.hostouterrors.yfilter != YFilter.not_set or
                    self.hostoutmulticastpkts.yfilter != YFilter.not_set or
                    self.hostoutoctets.yfilter != YFilter.not_set or
                    self.hostoutpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hostEntry" + "[hostIndex='" + self.hostindex.get() + "']" + "[hostAddress='" + self.hostaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/hostTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hostindex.is_set or self.hostindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostindex.get_name_leafdata())
                if (self.hostaddress.is_set or self.hostaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostaddress.get_name_leafdata())
                if (self.hostcreationorder.is_set or self.hostcreationorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostcreationorder.get_name_leafdata())
                if (self.hostinoctets.is_set or self.hostinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostinoctets.get_name_leafdata())
                if (self.hostinpkts.is_set or self.hostinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostinpkts.get_name_leafdata())
                if (self.hostoutbroadcastpkts.is_set or self.hostoutbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostoutbroadcastpkts.get_name_leafdata())
                if (self.hostouterrors.is_set or self.hostouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostouterrors.get_name_leafdata())
                if (self.hostoutmulticastpkts.is_set or self.hostoutmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostoutmulticastpkts.get_name_leafdata())
                if (self.hostoutoctets.is_set or self.hostoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostoutoctets.get_name_leafdata())
                if (self.hostoutpkts.is_set or self.hostoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hostoutpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hostIndex" or name == "hostAddress" or name == "hostCreationOrder" or name == "hostInOctets" or name == "hostInPkts" or name == "hostOutBroadcastPkts" or name == "hostOutErrors" or name == "hostOutMulticastPkts" or name == "hostOutOctets" or name == "hostOutPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hostIndex"):
                    self.hostindex = value
                    self.hostindex.value_namespace = name_space
                    self.hostindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostAddress"):
                    self.hostaddress = value
                    self.hostaddress.value_namespace = name_space
                    self.hostaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "hostCreationOrder"):
                    self.hostcreationorder = value
                    self.hostcreationorder.value_namespace = name_space
                    self.hostcreationorder.value_namespace_prefix = name_space_prefix
                if(value_path == "hostInOctets"):
                    self.hostinoctets = value
                    self.hostinoctets.value_namespace = name_space
                    self.hostinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "hostInPkts"):
                    self.hostinpkts = value
                    self.hostinpkts.value_namespace = name_space
                    self.hostinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostOutBroadcastPkts"):
                    self.hostoutbroadcastpkts = value
                    self.hostoutbroadcastpkts.value_namespace = name_space
                    self.hostoutbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostOutErrors"):
                    self.hostouterrors = value
                    self.hostouterrors.value_namespace = name_space
                    self.hostouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "hostOutMulticastPkts"):
                    self.hostoutmulticastpkts = value
                    self.hostoutmulticastpkts.value_namespace = name_space
                    self.hostoutmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostOutOctets"):
                    self.hostoutoctets = value
                    self.hostoutoctets.value_namespace = name_space
                    self.hostoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "hostOutPkts"):
                    self.hostoutpkts = value
                    self.hostoutpkts.value_namespace = name_space
                    self.hostoutpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.hostentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.hostentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hostTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hostEntry"):
                for c in self.hostentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Hosttable.Hostentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.hostentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hostEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Hosttimetable(Entity):
        """
        A list of time\-ordered host table entries.
        
        .. attribute:: hosttimeentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  This collection includes the relative ordering of the creation time of this object.  For example, an instance of the hostTimeOutBroadcastPkts object might be named hostTimeOutBroadcastPkts.1.687
        	**type**\: list of    :py:class:`Hosttimeentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttimetable.Hosttimeentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Hosttimetable, self).__init__()

            self.yang_name = "hostTimeTable"
            self.yang_parent_name = "RMON-MIB"

            self.hosttimeentry = YList(self)

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
                        super(RmonMib.Hosttimetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Hosttimetable, self).__setattr__(name, value)


        class Hosttimeentry(Entity):
            """
            A collection of statistics for a particular host that has
            been discovered on an interface of this device.  This
            collection includes the relative ordering of the creation
            time of this object.  For example, an instance of the
            hostTimeOutBroadcastPkts object might be named
            hostTimeOutBroadcastPkts.1.687
            
            .. attribute:: hosttimeindex  <key>
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttimecreationorder  <key>
            
            	An index that uniquely identifies an entry in the hostTime table among those entries associated with the same hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later. Thus the management station has the ability to learn of new entries added to this table without downloading the entire table.  It is important to note that the index for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTimeTable.  By observing this variable, the management station may detect the circumstances where a download of the table may have missed entries, and where a previous association between a value of hostTimeCreationOrder and a hostTimeEntry may no longer hold
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttimeaddress
            
            	The physical address of this host
            	**type**\:  str
            
            .. attribute:: hosttimeinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), except for those octets in bad packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hosttimeinpkts
            
            	The number of good packets transmitted to this address since it was added to the hostTimeTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTimeTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeouterrors
            
            	The number of bad packets transmitted by this address since this host was added to the hostTimeTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTimeTable. Note that this number does not include packets directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: hosttimeoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), including those octets in bad packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: hosttimeoutpkts
            
            	The number of packets, including bad packets, transmitted by this address since it was added to the hostTimeTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Hosttimetable.Hosttimeentry, self).__init__()

                self.yang_name = "hostTimeEntry"
                self.yang_parent_name = "hostTimeTable"

                self.hosttimeindex = YLeaf(YType.int32, "hostTimeIndex")

                self.hosttimecreationorder = YLeaf(YType.int32, "hostTimeCreationOrder")

                self.hosttimeaddress = YLeaf(YType.str, "hostTimeAddress")

                self.hosttimeinoctets = YLeaf(YType.uint32, "hostTimeInOctets")

                self.hosttimeinpkts = YLeaf(YType.uint32, "hostTimeInPkts")

                self.hosttimeoutbroadcastpkts = YLeaf(YType.uint32, "hostTimeOutBroadcastPkts")

                self.hosttimeouterrors = YLeaf(YType.uint32, "hostTimeOutErrors")

                self.hosttimeoutmulticastpkts = YLeaf(YType.uint32, "hostTimeOutMulticastPkts")

                self.hosttimeoutoctets = YLeaf(YType.uint32, "hostTimeOutOctets")

                self.hosttimeoutpkts = YLeaf(YType.uint32, "hostTimeOutPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hosttimeindex",
                                "hosttimecreationorder",
                                "hosttimeaddress",
                                "hosttimeinoctets",
                                "hosttimeinpkts",
                                "hosttimeoutbroadcastpkts",
                                "hosttimeouterrors",
                                "hosttimeoutmulticastpkts",
                                "hosttimeoutoctets",
                                "hosttimeoutpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Hosttimetable.Hosttimeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Hosttimetable.Hosttimeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hosttimeindex.is_set or
                    self.hosttimecreationorder.is_set or
                    self.hosttimeaddress.is_set or
                    self.hosttimeinoctets.is_set or
                    self.hosttimeinpkts.is_set or
                    self.hosttimeoutbroadcastpkts.is_set or
                    self.hosttimeouterrors.is_set or
                    self.hosttimeoutmulticastpkts.is_set or
                    self.hosttimeoutoctets.is_set or
                    self.hosttimeoutpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hosttimeindex.yfilter != YFilter.not_set or
                    self.hosttimecreationorder.yfilter != YFilter.not_set or
                    self.hosttimeaddress.yfilter != YFilter.not_set or
                    self.hosttimeinoctets.yfilter != YFilter.not_set or
                    self.hosttimeinpkts.yfilter != YFilter.not_set or
                    self.hosttimeoutbroadcastpkts.yfilter != YFilter.not_set or
                    self.hosttimeouterrors.yfilter != YFilter.not_set or
                    self.hosttimeoutmulticastpkts.yfilter != YFilter.not_set or
                    self.hosttimeoutoctets.yfilter != YFilter.not_set or
                    self.hosttimeoutpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hostTimeEntry" + "[hostTimeIndex='" + self.hosttimeindex.get() + "']" + "[hostTimeCreationOrder='" + self.hosttimecreationorder.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/hostTimeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hosttimeindex.is_set or self.hosttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeindex.get_name_leafdata())
                if (self.hosttimecreationorder.is_set or self.hosttimecreationorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimecreationorder.get_name_leafdata())
                if (self.hosttimeaddress.is_set or self.hosttimeaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeaddress.get_name_leafdata())
                if (self.hosttimeinoctets.is_set or self.hosttimeinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeinoctets.get_name_leafdata())
                if (self.hosttimeinpkts.is_set or self.hosttimeinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeinpkts.get_name_leafdata())
                if (self.hosttimeoutbroadcastpkts.is_set or self.hosttimeoutbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeoutbroadcastpkts.get_name_leafdata())
                if (self.hosttimeouterrors.is_set or self.hosttimeouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeouterrors.get_name_leafdata())
                if (self.hosttimeoutmulticastpkts.is_set or self.hosttimeoutmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeoutmulticastpkts.get_name_leafdata())
                if (self.hosttimeoutoctets.is_set or self.hosttimeoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeoutoctets.get_name_leafdata())
                if (self.hosttimeoutpkts.is_set or self.hosttimeoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttimeoutpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hostTimeIndex" or name == "hostTimeCreationOrder" or name == "hostTimeAddress" or name == "hostTimeInOctets" or name == "hostTimeInPkts" or name == "hostTimeOutBroadcastPkts" or name == "hostTimeOutErrors" or name == "hostTimeOutMulticastPkts" or name == "hostTimeOutOctets" or name == "hostTimeOutPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hostTimeIndex"):
                    self.hosttimeindex = value
                    self.hosttimeindex.value_namespace = name_space
                    self.hosttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeCreationOrder"):
                    self.hosttimecreationorder = value
                    self.hosttimecreationorder.value_namespace = name_space
                    self.hosttimecreationorder.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeAddress"):
                    self.hosttimeaddress = value
                    self.hosttimeaddress.value_namespace = name_space
                    self.hosttimeaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeInOctets"):
                    self.hosttimeinoctets = value
                    self.hosttimeinoctets.value_namespace = name_space
                    self.hosttimeinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeInPkts"):
                    self.hosttimeinpkts = value
                    self.hosttimeinpkts.value_namespace = name_space
                    self.hosttimeinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeOutBroadcastPkts"):
                    self.hosttimeoutbroadcastpkts = value
                    self.hosttimeoutbroadcastpkts.value_namespace = name_space
                    self.hosttimeoutbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeOutErrors"):
                    self.hosttimeouterrors = value
                    self.hosttimeouterrors.value_namespace = name_space
                    self.hosttimeouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeOutMulticastPkts"):
                    self.hosttimeoutmulticastpkts = value
                    self.hosttimeoutmulticastpkts.value_namespace = name_space
                    self.hosttimeoutmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeOutOctets"):
                    self.hosttimeoutoctets = value
                    self.hosttimeoutoctets.value_namespace = name_space
                    self.hosttimeoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTimeOutPkts"):
                    self.hosttimeoutpkts = value
                    self.hosttimeoutpkts.value_namespace = name_space
                    self.hosttimeoutpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.hosttimeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.hosttimeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hostTimeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hostTimeEntry"):
                for c in self.hosttimeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Hosttimetable.Hosttimeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.hosttimeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hostTimeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Hosttopncontroltable(Entity):
        """
        A list of top N host control entries.
        
        .. attribute:: hosttopncontrolentry
        
        	A set of parameters that control the creation of a report of the top N hosts according to several metrics.  For example, an instance of the hostTopNDuration object might be named hostTopNDuration.3
        	**type**\: list of    :py:class:`Hosttopncontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttopncontroltable.Hosttopncontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Hosttopncontroltable, self).__init__()

            self.yang_name = "hostTopNControlTable"
            self.yang_parent_name = "RMON-MIB"

            self.hosttopncontrolentry = YList(self)

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
                        super(RmonMib.Hosttopncontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Hosttopncontroltable, self).__setattr__(name, value)


        class Hosttopncontrolentry(Entity):
            """
            A set of parameters that control the creation of a report
            of the top N hosts according to several metrics.  For
            example, an instance of the hostTopNDuration object might
            be named hostTopNDuration.3
            
            .. attribute:: hosttopncontrolindex  <key>
            
            	An index that uniquely identifies an entry in the hostTopNControl table.  Each such entry defines one top N report prepared for one interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnduration
            
            	The number of seconds that this report has collected during the last sampling interval, or if this report is currently being collected, the number of seconds that this report is being collected during this sampling interval.  When the associated hostTopNTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the hostTopNTimeRemaining is set.  This value shall be zero if no reports have been requested for this hostTopNControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: hosttopngrantedsize
            
            	The maximum number of hosts in the top N table.  When the associated hostTopNRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated hostTopNRequestedSize object.  Hosts with the highest value of hostTopNRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more hosts
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopnhostindex
            
            	The host table for which a top N report will be prepared on behalf of this entry.  The host table identified by a particular value of this index is associated with the same host table as identified by the same value of hostIndex.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: hosttopnratebase
            
            	The variable for each host that the hostTopNRate variable is based upon.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\:   :py:class:`Hosttopnratebase <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttopncontroltable.Hosttopncontrolentry.Hosttopnratebase>`
            
            .. attribute:: hosttopnrequestedsize
            
            	The maximum number of hosts requested for the top N table.  When this object is created or modified, the probe should set hostTopNGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopnstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated hostTopNTimeRemaining object was modified to start the requested report
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttopnstatus
            
            	The status of this hostTopNControl entry.  If this object is not equal to valid(1), all associated hostTopNEntries shall be deleted by the agent
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: hosttopntimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, which is loaded into the associated hostTopNDuration object.  When this object is set to a non\-zero value, any associated hostTopNEntries shall be made inaccessible by the monitor.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  During this time, all associated hostTopNEntries shall remain inaccessible.  At the time that this object decrements to zero, the report is made accessible in the hostTopNTable.  Thus, the hostTopN table needs to be created only at the end of the collection interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Seconds
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Hosttopncontroltable.Hosttopncontrolentry, self).__init__()

                self.yang_name = "hostTopNControlEntry"
                self.yang_parent_name = "hostTopNControlTable"

                self.hosttopncontrolindex = YLeaf(YType.int32, "hostTopNControlIndex")

                self.hosttopnduration = YLeaf(YType.int32, "hostTopNDuration")

                self.hosttopngrantedsize = YLeaf(YType.int32, "hostTopNGrantedSize")

                self.hosttopnhostindex = YLeaf(YType.int32, "hostTopNHostIndex")

                self.hosttopnowner = YLeaf(YType.str, "hostTopNOwner")

                self.hosttopnratebase = YLeaf(YType.enumeration, "hostTopNRateBase")

                self.hosttopnrequestedsize = YLeaf(YType.int32, "hostTopNRequestedSize")

                self.hosttopnstarttime = YLeaf(YType.uint32, "hostTopNStartTime")

                self.hosttopnstatus = YLeaf(YType.enumeration, "hostTopNStatus")

                self.hosttopntimeremaining = YLeaf(YType.int32, "hostTopNTimeRemaining")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hosttopncontrolindex",
                                "hosttopnduration",
                                "hosttopngrantedsize",
                                "hosttopnhostindex",
                                "hosttopnowner",
                                "hosttopnratebase",
                                "hosttopnrequestedsize",
                                "hosttopnstarttime",
                                "hosttopnstatus",
                                "hosttopntimeremaining") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Hosttopncontroltable.Hosttopncontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Hosttopncontroltable.Hosttopncontrolentry, self).__setattr__(name, value)

            class Hosttopnratebase(Enum):
                """
                Hosttopnratebase

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


            def has_data(self):
                return (
                    self.hosttopncontrolindex.is_set or
                    self.hosttopnduration.is_set or
                    self.hosttopngrantedsize.is_set or
                    self.hosttopnhostindex.is_set or
                    self.hosttopnowner.is_set or
                    self.hosttopnratebase.is_set or
                    self.hosttopnrequestedsize.is_set or
                    self.hosttopnstarttime.is_set or
                    self.hosttopnstatus.is_set or
                    self.hosttopntimeremaining.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hosttopncontrolindex.yfilter != YFilter.not_set or
                    self.hosttopnduration.yfilter != YFilter.not_set or
                    self.hosttopngrantedsize.yfilter != YFilter.not_set or
                    self.hosttopnhostindex.yfilter != YFilter.not_set or
                    self.hosttopnowner.yfilter != YFilter.not_set or
                    self.hosttopnratebase.yfilter != YFilter.not_set or
                    self.hosttopnrequestedsize.yfilter != YFilter.not_set or
                    self.hosttopnstarttime.yfilter != YFilter.not_set or
                    self.hosttopnstatus.yfilter != YFilter.not_set or
                    self.hosttopntimeremaining.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hostTopNControlEntry" + "[hostTopNControlIndex='" + self.hosttopncontrolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/hostTopNControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hosttopncontrolindex.is_set or self.hosttopncontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopncontrolindex.get_name_leafdata())
                if (self.hosttopnduration.is_set or self.hosttopnduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnduration.get_name_leafdata())
                if (self.hosttopngrantedsize.is_set or self.hosttopngrantedsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopngrantedsize.get_name_leafdata())
                if (self.hosttopnhostindex.is_set or self.hosttopnhostindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnhostindex.get_name_leafdata())
                if (self.hosttopnowner.is_set or self.hosttopnowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnowner.get_name_leafdata())
                if (self.hosttopnratebase.is_set or self.hosttopnratebase.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnratebase.get_name_leafdata())
                if (self.hosttopnrequestedsize.is_set or self.hosttopnrequestedsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnrequestedsize.get_name_leafdata())
                if (self.hosttopnstarttime.is_set or self.hosttopnstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnstarttime.get_name_leafdata())
                if (self.hosttopnstatus.is_set or self.hosttopnstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnstatus.get_name_leafdata())
                if (self.hosttopntimeremaining.is_set or self.hosttopntimeremaining.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopntimeremaining.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hostTopNControlIndex" or name == "hostTopNDuration" or name == "hostTopNGrantedSize" or name == "hostTopNHostIndex" or name == "hostTopNOwner" or name == "hostTopNRateBase" or name == "hostTopNRequestedSize" or name == "hostTopNStartTime" or name == "hostTopNStatus" or name == "hostTopNTimeRemaining"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hostTopNControlIndex"):
                    self.hosttopncontrolindex = value
                    self.hosttopncontrolindex.value_namespace = name_space
                    self.hosttopncontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNDuration"):
                    self.hosttopnduration = value
                    self.hosttopnduration.value_namespace = name_space
                    self.hosttopnduration.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNGrantedSize"):
                    self.hosttopngrantedsize = value
                    self.hosttopngrantedsize.value_namespace = name_space
                    self.hosttopngrantedsize.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNHostIndex"):
                    self.hosttopnhostindex = value
                    self.hosttopnhostindex.value_namespace = name_space
                    self.hosttopnhostindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNOwner"):
                    self.hosttopnowner = value
                    self.hosttopnowner.value_namespace = name_space
                    self.hosttopnowner.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNRateBase"):
                    self.hosttopnratebase = value
                    self.hosttopnratebase.value_namespace = name_space
                    self.hosttopnratebase.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNRequestedSize"):
                    self.hosttopnrequestedsize = value
                    self.hosttopnrequestedsize.value_namespace = name_space
                    self.hosttopnrequestedsize.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNStartTime"):
                    self.hosttopnstarttime = value
                    self.hosttopnstarttime.value_namespace = name_space
                    self.hosttopnstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNStatus"):
                    self.hosttopnstatus = value
                    self.hosttopnstatus.value_namespace = name_space
                    self.hosttopnstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNTimeRemaining"):
                    self.hosttopntimeremaining = value
                    self.hosttopntimeremaining.value_namespace = name_space
                    self.hosttopntimeremaining.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.hosttopncontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.hosttopncontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hostTopNControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hostTopNControlEntry"):
                for c in self.hosttopncontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Hosttopncontroltable.Hosttopncontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.hosttopncontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hostTopNControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Hosttopntable(Entity):
        """
        A list of top N host entries.
        
        .. attribute:: hosttopnentry
        
        	A set of statistics for a host that is part of a top N report.  For example, an instance of the hostTopNRate object might be named hostTopNRate.3.10
        	**type**\: list of    :py:class:`Hosttopnentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Hosttopntable.Hosttopnentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Hosttopntable, self).__init__()

            self.yang_name = "hostTopNTable"
            self.yang_parent_name = "RMON-MIB"

            self.hosttopnentry = YList(self)

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
                        super(RmonMib.Hosttopntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Hosttopntable, self).__setattr__(name, value)


        class Hosttopnentry(Entity):
            """
            A set of statistics for a host that is part of a top N
            report.  For example, an instance of the hostTopNRate
            object might be named hostTopNRate.3.10
            
            .. attribute:: hosttopnreport  <key>
            
            	This object identifies the top N report of which this entry is a part.  The set of hosts identified by a particular value of this object is part of the same report as identified by the same value of the hostTopNControlIndex object
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnindex  <key>
            
            	An index that uniquely identifies an entry in the hostTopN table among those in the same report. This index is between 1 and N, where N is the number of entries in this table.  Increasing values of hostTopNIndex shall be assigned to entries with decreasing values of hostTopNRate until index N is assigned to the entry with the lowest value of hostTopNRate or there are no more hostTopNEntries
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnaddress
            
            	The physical address of this host
            	**type**\:  str
            
            .. attribute:: hosttopnrate
            
            	The amount of change in the selected variable during this sampling interval.  The selected variable is this host's instance of the object selected by hostTopNRateBase
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Hosttopntable.Hosttopnentry, self).__init__()

                self.yang_name = "hostTopNEntry"
                self.yang_parent_name = "hostTopNTable"

                self.hosttopnreport = YLeaf(YType.int32, "hostTopNReport")

                self.hosttopnindex = YLeaf(YType.int32, "hostTopNIndex")

                self.hosttopnaddress = YLeaf(YType.str, "hostTopNAddress")

                self.hosttopnrate = YLeaf(YType.int32, "hostTopNRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hosttopnreport",
                                "hosttopnindex",
                                "hosttopnaddress",
                                "hosttopnrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Hosttopntable.Hosttopnentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Hosttopntable.Hosttopnentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hosttopnreport.is_set or
                    self.hosttopnindex.is_set or
                    self.hosttopnaddress.is_set or
                    self.hosttopnrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hosttopnreport.yfilter != YFilter.not_set or
                    self.hosttopnindex.yfilter != YFilter.not_set or
                    self.hosttopnaddress.yfilter != YFilter.not_set or
                    self.hosttopnrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hostTopNEntry" + "[hostTopNReport='" + self.hosttopnreport.get() + "']" + "[hostTopNIndex='" + self.hosttopnindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/hostTopNTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hosttopnreport.is_set or self.hosttopnreport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnreport.get_name_leafdata())
                if (self.hosttopnindex.is_set or self.hosttopnindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnindex.get_name_leafdata())
                if (self.hosttopnaddress.is_set or self.hosttopnaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnaddress.get_name_leafdata())
                if (self.hosttopnrate.is_set or self.hosttopnrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hosttopnrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hostTopNReport" or name == "hostTopNIndex" or name == "hostTopNAddress" or name == "hostTopNRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hostTopNReport"):
                    self.hosttopnreport = value
                    self.hosttopnreport.value_namespace = name_space
                    self.hosttopnreport.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNIndex"):
                    self.hosttopnindex = value
                    self.hosttopnindex.value_namespace = name_space
                    self.hosttopnindex.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNAddress"):
                    self.hosttopnaddress = value
                    self.hosttopnaddress.value_namespace = name_space
                    self.hosttopnaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "hostTopNRate"):
                    self.hosttopnrate = value
                    self.hosttopnrate.value_namespace = name_space
                    self.hosttopnrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.hosttopnentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.hosttopnentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hostTopNTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hostTopNEntry"):
                for c in self.hosttopnentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Hosttopntable.Hosttopnentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.hosttopnentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hostTopNEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Matrixcontroltable(Entity):
        """
        A list of information entries for the
        traffic matrix on each interface.
        
        .. attribute:: matrixcontrolentry
        
        	Information about a traffic matrix on a particular interface.  For example, an instance of the matrixControlLastDeleteTime object might be named matrixControlLastDeleteTime.1
        	**type**\: list of    :py:class:`Matrixcontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixcontroltable.Matrixcontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Matrixcontroltable, self).__init__()

            self.yang_name = "matrixControlTable"
            self.yang_parent_name = "RMON-MIB"

            self.matrixcontrolentry = YList(self)

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
                        super(RmonMib.Matrixcontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Matrixcontroltable, self).__setattr__(name, value)


        class Matrixcontrolentry(Entity):
            """
            Information about a traffic matrix on a particular
            interface.  For example, an instance of the
            matrixControlLastDeleteTime object might be named
            matrixControlLastDeleteTime.1
            
            .. attribute:: matrixcontrolindex  <key>
            
            	An index that uniquely identifies an entry in the matrixControl table.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the matrixSDTable and the matrixDSTable on behalf of this matrixControlEntry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: matrixcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontroldatasource
            
            	This object identifies the source of the data from which this entry creates a traffic matrix. This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2233 [17], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated matrixControlStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: matrixcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted      because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the matrixSDTable or matrixDSTable associated with this matrixControlEntry. If no deletions have occurred, this value shall be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: matrixcontrolstatus
            
            	The status of this matrixControl entry. If this object is not equal to valid(1), all associated entries in the matrixSDTable and the matrixDSTable shall be deleted by the agent
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: matrixcontroltablesize
            
            	The number of matrixSDEntries in the matrixSDTable for this interface.  This must also be the value of the number of entries in the matrixDSTable for this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Matrixcontroltable.Matrixcontrolentry, self).__init__()

                self.yang_name = "matrixControlEntry"
                self.yang_parent_name = "matrixControlTable"

                self.matrixcontrolindex = YLeaf(YType.int32, "matrixControlIndex")

                self.matrixcontrolcreatetime = YLeaf(YType.uint32, "RMON2-MIB:matrixControlCreateTime")

                self.matrixcontroldatasource = YLeaf(YType.str, "matrixControlDataSource")

                self.matrixcontroldroppedframes = YLeaf(YType.uint32, "RMON2-MIB:matrixControlDroppedFrames")

                self.matrixcontrollastdeletetime = YLeaf(YType.uint32, "matrixControlLastDeleteTime")

                self.matrixcontrolowner = YLeaf(YType.str, "matrixControlOwner")

                self.matrixcontrolstatus = YLeaf(YType.enumeration, "matrixControlStatus")

                self.matrixcontroltablesize = YLeaf(YType.int32, "matrixControlTableSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("matrixcontrolindex",
                                "matrixcontrolcreatetime",
                                "matrixcontroldatasource",
                                "matrixcontroldroppedframes",
                                "matrixcontrollastdeletetime",
                                "matrixcontrolowner",
                                "matrixcontrolstatus",
                                "matrixcontroltablesize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Matrixcontroltable.Matrixcontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Matrixcontroltable.Matrixcontrolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.matrixcontrolindex.is_set or
                    self.matrixcontrolcreatetime.is_set or
                    self.matrixcontroldatasource.is_set or
                    self.matrixcontroldroppedframes.is_set or
                    self.matrixcontrollastdeletetime.is_set or
                    self.matrixcontrolowner.is_set or
                    self.matrixcontrolstatus.is_set or
                    self.matrixcontroltablesize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.matrixcontrolindex.yfilter != YFilter.not_set or
                    self.matrixcontrolcreatetime.yfilter != YFilter.not_set or
                    self.matrixcontroldatasource.yfilter != YFilter.not_set or
                    self.matrixcontroldroppedframes.yfilter != YFilter.not_set or
                    self.matrixcontrollastdeletetime.yfilter != YFilter.not_set or
                    self.matrixcontrolowner.yfilter != YFilter.not_set or
                    self.matrixcontrolstatus.yfilter != YFilter.not_set or
                    self.matrixcontroltablesize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "matrixControlEntry" + "[matrixControlIndex='" + self.matrixcontrolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/matrixControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.matrixcontrolindex.is_set or self.matrixcontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontrolindex.get_name_leafdata())
                if (self.matrixcontrolcreatetime.is_set or self.matrixcontrolcreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontrolcreatetime.get_name_leafdata())
                if (self.matrixcontroldatasource.is_set or self.matrixcontroldatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontroldatasource.get_name_leafdata())
                if (self.matrixcontroldroppedframes.is_set or self.matrixcontroldroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontroldroppedframes.get_name_leafdata())
                if (self.matrixcontrollastdeletetime.is_set or self.matrixcontrollastdeletetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontrollastdeletetime.get_name_leafdata())
                if (self.matrixcontrolowner.is_set or self.matrixcontrolowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontrolowner.get_name_leafdata())
                if (self.matrixcontrolstatus.is_set or self.matrixcontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontrolstatus.get_name_leafdata())
                if (self.matrixcontroltablesize.is_set or self.matrixcontroltablesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixcontroltablesize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "matrixControlIndex" or name == "matrixControlCreateTime" or name == "matrixControlDataSource" or name == "matrixControlDroppedFrames" or name == "matrixControlLastDeleteTime" or name == "matrixControlOwner" or name == "matrixControlStatus" or name == "matrixControlTableSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "matrixControlIndex"):
                    self.matrixcontrolindex = value
                    self.matrixcontrolindex.value_namespace = name_space
                    self.matrixcontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlCreateTime"):
                    self.matrixcontrolcreatetime = value
                    self.matrixcontrolcreatetime.value_namespace = name_space
                    self.matrixcontrolcreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlDataSource"):
                    self.matrixcontroldatasource = value
                    self.matrixcontroldatasource.value_namespace = name_space
                    self.matrixcontroldatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlDroppedFrames"):
                    self.matrixcontroldroppedframes = value
                    self.matrixcontroldroppedframes.value_namespace = name_space
                    self.matrixcontroldroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlLastDeleteTime"):
                    self.matrixcontrollastdeletetime = value
                    self.matrixcontrollastdeletetime.value_namespace = name_space
                    self.matrixcontrollastdeletetime.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlOwner"):
                    self.matrixcontrolowner = value
                    self.matrixcontrolowner.value_namespace = name_space
                    self.matrixcontrolowner.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlStatus"):
                    self.matrixcontrolstatus = value
                    self.matrixcontrolstatus.value_namespace = name_space
                    self.matrixcontrolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixControlTableSize"):
                    self.matrixcontroltablesize = value
                    self.matrixcontroltablesize.value_namespace = name_space
                    self.matrixcontroltablesize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.matrixcontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.matrixcontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "matrixControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "matrixControlEntry"):
                for c in self.matrixcontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Matrixcontroltable.Matrixcontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.matrixcontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "matrixControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Matrixsdtable(Entity):
        """
        A list of traffic matrix entries indexed by
        source and destination MAC address.
        
        .. attribute:: matrixsdentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
        	**type**\: list of    :py:class:`Matrixsdentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixsdtable.Matrixsdentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Matrixsdtable, self).__init__()

            self.yang_name = "matrixSDTable"
            self.yang_parent_name = "RMON-MIB"

            self.matrixsdentry = YList(self)

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
                        super(RmonMib.Matrixsdtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Matrixsdtable, self).__setattr__(name, value)


        class Matrixsdentry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
            
            .. attribute:: matrixsdindex  <key>
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: matrixsdsourceaddress  <key>
            
            	The source physical address
            	**type**\:  str
            
            .. attribute:: matrixsddestaddress  <key>
            
            	The destination physical address
            	**type**\:  str
            
            .. attribute:: matrixsderrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: matrixsdoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: matrixsdpkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Matrixsdtable.Matrixsdentry, self).__init__()

                self.yang_name = "matrixSDEntry"
                self.yang_parent_name = "matrixSDTable"

                self.matrixsdindex = YLeaf(YType.int32, "matrixSDIndex")

                self.matrixsdsourceaddress = YLeaf(YType.str, "matrixSDSourceAddress")

                self.matrixsddestaddress = YLeaf(YType.str, "matrixSDDestAddress")

                self.matrixsderrors = YLeaf(YType.uint32, "matrixSDErrors")

                self.matrixsdoctets = YLeaf(YType.uint32, "matrixSDOctets")

                self.matrixsdpkts = YLeaf(YType.uint32, "matrixSDPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("matrixsdindex",
                                "matrixsdsourceaddress",
                                "matrixsddestaddress",
                                "matrixsderrors",
                                "matrixsdoctets",
                                "matrixsdpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Matrixsdtable.Matrixsdentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Matrixsdtable.Matrixsdentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.matrixsdindex.is_set or
                    self.matrixsdsourceaddress.is_set or
                    self.matrixsddestaddress.is_set or
                    self.matrixsderrors.is_set or
                    self.matrixsdoctets.is_set or
                    self.matrixsdpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.matrixsdindex.yfilter != YFilter.not_set or
                    self.matrixsdsourceaddress.yfilter != YFilter.not_set or
                    self.matrixsddestaddress.yfilter != YFilter.not_set or
                    self.matrixsderrors.yfilter != YFilter.not_set or
                    self.matrixsdoctets.yfilter != YFilter.not_set or
                    self.matrixsdpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "matrixSDEntry" + "[matrixSDIndex='" + self.matrixsdindex.get() + "']" + "[matrixSDSourceAddress='" + self.matrixsdsourceaddress.get() + "']" + "[matrixSDDestAddress='" + self.matrixsddestaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/matrixSDTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.matrixsdindex.is_set or self.matrixsdindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsdindex.get_name_leafdata())
                if (self.matrixsdsourceaddress.is_set or self.matrixsdsourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsdsourceaddress.get_name_leafdata())
                if (self.matrixsddestaddress.is_set or self.matrixsddestaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsddestaddress.get_name_leafdata())
                if (self.matrixsderrors.is_set or self.matrixsderrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsderrors.get_name_leafdata())
                if (self.matrixsdoctets.is_set or self.matrixsdoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsdoctets.get_name_leafdata())
                if (self.matrixsdpkts.is_set or self.matrixsdpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixsdpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "matrixSDIndex" or name == "matrixSDSourceAddress" or name == "matrixSDDestAddress" or name == "matrixSDErrors" or name == "matrixSDOctets" or name == "matrixSDPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "matrixSDIndex"):
                    self.matrixsdindex = value
                    self.matrixsdindex.value_namespace = name_space
                    self.matrixsdindex.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixSDSourceAddress"):
                    self.matrixsdsourceaddress = value
                    self.matrixsdsourceaddress.value_namespace = name_space
                    self.matrixsdsourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixSDDestAddress"):
                    self.matrixsddestaddress = value
                    self.matrixsddestaddress.value_namespace = name_space
                    self.matrixsddestaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixSDErrors"):
                    self.matrixsderrors = value
                    self.matrixsderrors.value_namespace = name_space
                    self.matrixsderrors.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixSDOctets"):
                    self.matrixsdoctets = value
                    self.matrixsdoctets.value_namespace = name_space
                    self.matrixsdoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixSDPkts"):
                    self.matrixsdpkts = value
                    self.matrixsdpkts.value_namespace = name_space
                    self.matrixsdpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.matrixsdentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.matrixsdentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "matrixSDTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "matrixSDEntry"):
                for c in self.matrixsdentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Matrixsdtable.Matrixsdentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.matrixsdentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "matrixSDEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Matrixdstable(Entity):
        """
        A list of traffic matrix entries indexed by
        destination and source MAC address.
        
        .. attribute:: matrixdsentry
        
        	A collection of statistics for communications between two addresses on a particular interface.  For example, an instance of the matrixSDPkts object might be named matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
        	**type**\: list of    :py:class:`Matrixdsentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Matrixdstable.Matrixdsentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Matrixdstable, self).__init__()

            self.yang_name = "matrixDSTable"
            self.yang_parent_name = "RMON-MIB"

            self.matrixdsentry = YList(self)

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
                        super(RmonMib.Matrixdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Matrixdstable, self).__setattr__(name, value)


        class Matrixdsentry(Entity):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.  For example,
            an instance of the matrixSDPkts object might be named
            matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
            
            .. attribute:: matrixdsindex  <key>
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: matrixdsdestaddress  <key>
            
            	The destination physical address
            	**type**\:  str
            
            .. attribute:: matrixdssourceaddress  <key>
            
            	The source physical address
            	**type**\:  str
            
            .. attribute:: matrixdserrors
            
            	The number of bad packets transmitted from the source address to the destination address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: matrixdsoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: matrixdspkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes bad packets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Matrixdstable.Matrixdsentry, self).__init__()

                self.yang_name = "matrixDSEntry"
                self.yang_parent_name = "matrixDSTable"

                self.matrixdsindex = YLeaf(YType.int32, "matrixDSIndex")

                self.matrixdsdestaddress = YLeaf(YType.str, "matrixDSDestAddress")

                self.matrixdssourceaddress = YLeaf(YType.str, "matrixDSSourceAddress")

                self.matrixdserrors = YLeaf(YType.uint32, "matrixDSErrors")

                self.matrixdsoctets = YLeaf(YType.uint32, "matrixDSOctets")

                self.matrixdspkts = YLeaf(YType.uint32, "matrixDSPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("matrixdsindex",
                                "matrixdsdestaddress",
                                "matrixdssourceaddress",
                                "matrixdserrors",
                                "matrixdsoctets",
                                "matrixdspkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Matrixdstable.Matrixdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Matrixdstable.Matrixdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.matrixdsindex.is_set or
                    self.matrixdsdestaddress.is_set or
                    self.matrixdssourceaddress.is_set or
                    self.matrixdserrors.is_set or
                    self.matrixdsoctets.is_set or
                    self.matrixdspkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.matrixdsindex.yfilter != YFilter.not_set or
                    self.matrixdsdestaddress.yfilter != YFilter.not_set or
                    self.matrixdssourceaddress.yfilter != YFilter.not_set or
                    self.matrixdserrors.yfilter != YFilter.not_set or
                    self.matrixdsoctets.yfilter != YFilter.not_set or
                    self.matrixdspkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "matrixDSEntry" + "[matrixDSIndex='" + self.matrixdsindex.get() + "']" + "[matrixDSDestAddress='" + self.matrixdsdestaddress.get() + "']" + "[matrixDSSourceAddress='" + self.matrixdssourceaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/matrixDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.matrixdsindex.is_set or self.matrixdsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdsindex.get_name_leafdata())
                if (self.matrixdsdestaddress.is_set or self.matrixdsdestaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdsdestaddress.get_name_leafdata())
                if (self.matrixdssourceaddress.is_set or self.matrixdssourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdssourceaddress.get_name_leafdata())
                if (self.matrixdserrors.is_set or self.matrixdserrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdserrors.get_name_leafdata())
                if (self.matrixdsoctets.is_set or self.matrixdsoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdsoctets.get_name_leafdata())
                if (self.matrixdspkts.is_set or self.matrixdspkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.matrixdspkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "matrixDSIndex" or name == "matrixDSDestAddress" or name == "matrixDSSourceAddress" or name == "matrixDSErrors" or name == "matrixDSOctets" or name == "matrixDSPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "matrixDSIndex"):
                    self.matrixdsindex = value
                    self.matrixdsindex.value_namespace = name_space
                    self.matrixdsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixDSDestAddress"):
                    self.matrixdsdestaddress = value
                    self.matrixdsdestaddress.value_namespace = name_space
                    self.matrixdsdestaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixDSSourceAddress"):
                    self.matrixdssourceaddress = value
                    self.matrixdssourceaddress.value_namespace = name_space
                    self.matrixdssourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixDSErrors"):
                    self.matrixdserrors = value
                    self.matrixdserrors.value_namespace = name_space
                    self.matrixdserrors.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixDSOctets"):
                    self.matrixdsoctets = value
                    self.matrixdsoctets.value_namespace = name_space
                    self.matrixdsoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "matrixDSPkts"):
                    self.matrixdspkts = value
                    self.matrixdspkts.value_namespace = name_space
                    self.matrixdspkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.matrixdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.matrixdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "matrixDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "matrixDSEntry"):
                for c in self.matrixdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Matrixdstable.Matrixdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.matrixdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "matrixDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Filtertable(Entity):
        """
        A list of packet filter entries.
        
        .. attribute:: filterentry
        
        	A set of parameters for a packet filter applied on a particular interface.  As an example, an instance of the filterPktData object might be named filterPktData.12
        	**type**\: list of    :py:class:`Filterentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Filtertable.Filterentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Filtertable, self).__init__()

            self.yang_name = "filterTable"
            self.yang_parent_name = "RMON-MIB"

            self.filterentry = YList(self)

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
                        super(RmonMib.Filtertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Filtertable, self).__setattr__(name, value)


        class Filterentry(Entity):
            """
            A set of parameters for a packet filter applied on a
            particular interface.  As an example, an instance of the
            filterPktData object might be named filterPktData.12
            
            .. attribute:: filterindex  <key>
            
            	An index that uniquely identifies an entry in the filter table.  Each such entry defines one filter that is to be applied to every packet received on an interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: filterchannelindex
            
            	This object identifies the channel of which this filter is a part.  The filters identified by a particular value of this object are associated with the same channel as identified by the same value of the channelIndex object
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: filterowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: filterpktdata
            
            	The data that is to be matched with the input packet. For each packet received, this filter and the accompanying filterPktDataMask and filterPktDataNotMask will be adjusted for the offset.  The only bits relevant to this match algorithm are those that have the corresponding filterPktDataMask bit equal to one.  The following three rules are then applied to every packet\:  (1) If the packet is too short and does not have data     corresponding to part of the filterPktData, the packet     will fail this data match.  (2) For each relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to zero, if     the bit from the packet is not equal to the corresponding     bit from the filterPktData, then the packet will fail     this data match.  (3) If for every relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to one, the     bit from the packet is equal to the corresponding bit     from the filterPktData, then the packet will fail this     data match.  Any packets that have not failed any of the three matches above have passed this data match.  In particular, a zero length filter will match any packet.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  str
            
            .. attribute:: filterpktdatamask
            
            	The mask that is applied to the match process. After adjusting this mask for the offset, only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the match algorithm.  The offset is applied to filterPktDataMask in the same way it is applied to the filter.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  str
            
            .. attribute:: filterpktdatanotmask
            
            	The inversion mask that is applied to the match process.  After adjusting this mask for the offset, those relevant bits in the received packet that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktData object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet that correspond to bits set in this mask must be different to its corresponding bit in the filterPktData object.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  str
            
            .. attribute:: filterpktdataoffset
            
            	The offset from the beginning of each packet where a match of packet data will be attempted.  This offset is measured from the point in the physical layer packet after the framing bits, if any.  For example, in an Ethernet frame, this point is at the beginning of the destination MAC address.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: filterpktstatus
            
            	The status that is to be matched with the input packet. The only bits relevant to this match algorithm are those that have the corresponding filterPktStatusMask bit equal to one. The following two rules are then applied to every packet\:  (1) For each relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to zero, if     the bit from the packet status is not equal to the     corresponding bit from the filterPktStatus, then the     packet will fail this status match.  (2) If for every relevant bit from the packet status with the     corresponding filterPktStatusNotMask bit set to one, the     bit from the packet status is equal to the corresponding     bit from the filterPktStatus, then the packet will fail     this status match.  Any packets that have not failed either of the two matches above have passed this status match.  In particular, a zero length status filter will match any packet's status.  The value of the packet status is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum. The errors and the bits that represent them are dependent on the media type of the interface that this channel is receiving packets from.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined.  For the purposes of this status matching algorithm, if the packet status is longer than this filterPktStatus object, this object is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusmask
            
            	The mask that is applied to the status match process. Only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the status match algorithm.  For the purposes of the matching algorithm, if the associated filterPktStatus object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the size of the filterPktStatus.  In addition, if a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusnotmask
            
            	The inversion mask that is applied to the status match process.  Those relevant bits in the received packet status that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktStatus object for the packet to be accepted.  In addition, at least one of those relevant bits in the received packet status that correspond to bits set in this mask must be different to its corresponding bit in the filterPktStatus object for the packet to be accepted.  For the purposes of the matching algorithm, if the associated filterPktStatus object or a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the longer of the lengths of the filterPktStatus object and the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterprotocoldirdatalocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with performs the following operations on every packet\:  1) \- If the packet doesn't match the protocol directory entry      identified by this object, discard the packet and exit      (i.e., discard the packet if it is not of the identified      protocol). 2) \- If the associated filterProtocolDirLocalIndex is non\-zero      and the packet doesn't match the protocol directory      entry identified by that object, discard the packet and      exit 3) \- If the packet matches, perform the regular filter      algorithm as if the beginning of this named protocol is      the beginning of the packet, potentially applying the      filterOffset value to move further into the packet
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: filterprotocoldirlocalindex
            
            	When this object is set to a non\-zero value, the filter that it is associated with will discard the packet if the packet doesn't match this protocol directory entry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: filterstatus
            
            	The status of this filter entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Filtertable.Filterentry, self).__init__()

                self.yang_name = "filterEntry"
                self.yang_parent_name = "filterTable"

                self.filterindex = YLeaf(YType.int32, "filterIndex")

                self.filterchannelindex = YLeaf(YType.int32, "filterChannelIndex")

                self.filterowner = YLeaf(YType.str, "filterOwner")

                self.filterpktdata = YLeaf(YType.str, "filterPktData")

                self.filterpktdatamask = YLeaf(YType.str, "filterPktDataMask")

                self.filterpktdatanotmask = YLeaf(YType.str, "filterPktDataNotMask")

                self.filterpktdataoffset = YLeaf(YType.int32, "filterPktDataOffset")

                self.filterpktstatus = YLeaf(YType.int32, "filterPktStatus")

                self.filterpktstatusmask = YLeaf(YType.int32, "filterPktStatusMask")

                self.filterpktstatusnotmask = YLeaf(YType.int32, "filterPktStatusNotMask")

                self.filterprotocoldirdatalocalindex = YLeaf(YType.int32, "RMON2-MIB:filterProtocolDirDataLocalIndex")

                self.filterprotocoldirlocalindex = YLeaf(YType.int32, "RMON2-MIB:filterProtocolDirLocalIndex")

                self.filterstatus = YLeaf(YType.enumeration, "filterStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("filterindex",
                                "filterchannelindex",
                                "filterowner",
                                "filterpktdata",
                                "filterpktdatamask",
                                "filterpktdatanotmask",
                                "filterpktdataoffset",
                                "filterpktstatus",
                                "filterpktstatusmask",
                                "filterpktstatusnotmask",
                                "filterprotocoldirdatalocalindex",
                                "filterprotocoldirlocalindex",
                                "filterstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Filtertable.Filterentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Filtertable.Filterentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.filterindex.is_set or
                    self.filterchannelindex.is_set or
                    self.filterowner.is_set or
                    self.filterpktdata.is_set or
                    self.filterpktdatamask.is_set or
                    self.filterpktdatanotmask.is_set or
                    self.filterpktdataoffset.is_set or
                    self.filterpktstatus.is_set or
                    self.filterpktstatusmask.is_set or
                    self.filterpktstatusnotmask.is_set or
                    self.filterprotocoldirdatalocalindex.is_set or
                    self.filterprotocoldirlocalindex.is_set or
                    self.filterstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.filterindex.yfilter != YFilter.not_set or
                    self.filterchannelindex.yfilter != YFilter.not_set or
                    self.filterowner.yfilter != YFilter.not_set or
                    self.filterpktdata.yfilter != YFilter.not_set or
                    self.filterpktdatamask.yfilter != YFilter.not_set or
                    self.filterpktdatanotmask.yfilter != YFilter.not_set or
                    self.filterpktdataoffset.yfilter != YFilter.not_set or
                    self.filterpktstatus.yfilter != YFilter.not_set or
                    self.filterpktstatusmask.yfilter != YFilter.not_set or
                    self.filterpktstatusnotmask.yfilter != YFilter.not_set or
                    self.filterprotocoldirdatalocalindex.yfilter != YFilter.not_set or
                    self.filterprotocoldirlocalindex.yfilter != YFilter.not_set or
                    self.filterstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "filterEntry" + "[filterIndex='" + self.filterindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/filterTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.filterindex.is_set or self.filterindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterindex.get_name_leafdata())
                if (self.filterchannelindex.is_set or self.filterchannelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterchannelindex.get_name_leafdata())
                if (self.filterowner.is_set or self.filterowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterowner.get_name_leafdata())
                if (self.filterpktdata.is_set or self.filterpktdata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktdata.get_name_leafdata())
                if (self.filterpktdatamask.is_set or self.filterpktdatamask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktdatamask.get_name_leafdata())
                if (self.filterpktdatanotmask.is_set or self.filterpktdatanotmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktdatanotmask.get_name_leafdata())
                if (self.filterpktdataoffset.is_set or self.filterpktdataoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktdataoffset.get_name_leafdata())
                if (self.filterpktstatus.is_set or self.filterpktstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktstatus.get_name_leafdata())
                if (self.filterpktstatusmask.is_set or self.filterpktstatusmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktstatusmask.get_name_leafdata())
                if (self.filterpktstatusnotmask.is_set or self.filterpktstatusnotmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterpktstatusnotmask.get_name_leafdata())
                if (self.filterprotocoldirdatalocalindex.is_set or self.filterprotocoldirdatalocalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterprotocoldirdatalocalindex.get_name_leafdata())
                if (self.filterprotocoldirlocalindex.is_set or self.filterprotocoldirlocalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterprotocoldirlocalindex.get_name_leafdata())
                if (self.filterstatus.is_set or self.filterstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filterstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "filterIndex" or name == "filterChannelIndex" or name == "filterOwner" or name == "filterPktData" or name == "filterPktDataMask" or name == "filterPktDataNotMask" or name == "filterPktDataOffset" or name == "filterPktStatus" or name == "filterPktStatusMask" or name == "filterPktStatusNotMask" or name == "filterProtocolDirDataLocalIndex" or name == "filterProtocolDirLocalIndex" or name == "filterStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "filterIndex"):
                    self.filterindex = value
                    self.filterindex.value_namespace = name_space
                    self.filterindex.value_namespace_prefix = name_space_prefix
                if(value_path == "filterChannelIndex"):
                    self.filterchannelindex = value
                    self.filterchannelindex.value_namespace = name_space
                    self.filterchannelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "filterOwner"):
                    self.filterowner = value
                    self.filterowner.value_namespace = name_space
                    self.filterowner.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktData"):
                    self.filterpktdata = value
                    self.filterpktdata.value_namespace = name_space
                    self.filterpktdata.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktDataMask"):
                    self.filterpktdatamask = value
                    self.filterpktdatamask.value_namespace = name_space
                    self.filterpktdatamask.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktDataNotMask"):
                    self.filterpktdatanotmask = value
                    self.filterpktdatanotmask.value_namespace = name_space
                    self.filterpktdatanotmask.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktDataOffset"):
                    self.filterpktdataoffset = value
                    self.filterpktdataoffset.value_namespace = name_space
                    self.filterpktdataoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktStatus"):
                    self.filterpktstatus = value
                    self.filterpktstatus.value_namespace = name_space
                    self.filterpktstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktStatusMask"):
                    self.filterpktstatusmask = value
                    self.filterpktstatusmask.value_namespace = name_space
                    self.filterpktstatusmask.value_namespace_prefix = name_space_prefix
                if(value_path == "filterPktStatusNotMask"):
                    self.filterpktstatusnotmask = value
                    self.filterpktstatusnotmask.value_namespace = name_space
                    self.filterpktstatusnotmask.value_namespace_prefix = name_space_prefix
                if(value_path == "filterProtocolDirDataLocalIndex"):
                    self.filterprotocoldirdatalocalindex = value
                    self.filterprotocoldirdatalocalindex.value_namespace = name_space
                    self.filterprotocoldirdatalocalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "filterProtocolDirLocalIndex"):
                    self.filterprotocoldirlocalindex = value
                    self.filterprotocoldirlocalindex.value_namespace = name_space
                    self.filterprotocoldirlocalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "filterStatus"):
                    self.filterstatus = value
                    self.filterstatus.value_namespace = name_space
                    self.filterstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.filterentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.filterentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "filterTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "filterEntry"):
                for c in self.filterentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Filtertable.Filterentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.filterentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "filterEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Channeltable(Entity):
        """
        A list of packet channel entries.
        
        .. attribute:: channelentry
        
        	A set of parameters for a packet channel applied on a particular interface.  As an example, an instance of the channelMatches object might be named channelMatches.3
        	**type**\: list of    :py:class:`Channelentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Channeltable.Channelentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Channeltable, self).__init__()

            self.yang_name = "channelTable"
            self.yang_parent_name = "RMON-MIB"

            self.channelentry = YList(self)

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
                        super(RmonMib.Channeltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Channeltable, self).__setattr__(name, value)


        class Channelentry(Entity):
            """
            A set of parameters for a packet channel applied on a
            particular interface.  As an example, an instance of the
            channelMatches object might be named channelMatches.3
            
            .. attribute:: channelindex  <key>
            
            	An index that uniquely identifies an entry in the channel table.  Each such entry defines one channel, a logical data and event stream.  It is suggested that before creating a channel, an application should scan all instances of the filterChannelIndex object to make sure that there are no pre\-existing filters that would be inadvertently be linked to the channel
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: channelaccepttype
            
            	This object controls the action of the filters associated with this channel.  If this object is equal to acceptMatched(1), packets will be accepted to this channel if they are accepted by both the packet data and packet status matches of an associated filter.  If this object is equal to acceptFailed(2), packets will be accepted to this channel only if they fail either the packet data match or the packet status match of each of the associated filters.  In particular, a channel with no associated filters will match no packets if set to acceptMatched(1) case and will match all packets in the acceptFailed(2) case.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:   :py:class:`Channelaccepttype <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Channeltable.Channelentry.Channelaccepttype>`
            
            .. attribute:: channelcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: channeldatacontrol
            
            	This object controls the flow of data through this channel. If this object is on(1), data, status and events flow through this channel.  If this object is off(2), data, status and events will not flow through this channel
            	**type**\:   :py:class:`Channeldatacontrol <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Channeltable.Channelentry.Channeldatacontrol>`
            
            .. attribute:: channeldescription
            
            	A comment describing this channel
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: channeldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe      is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: channeleventindex
            
            	The value of this object identifies the event that is configured to be generated when the associated channelDataControl is on and a packet is matched.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: channeleventstatus
            
            	The event status of this channel.  If this channel is configured to generate events when packets are matched, a means of controlling the flow of those events is often needed.  When this object is equal to eventReady(1), a single event may be generated, after which this object will be set by the probe to eventFired(2).  While in the eventFired(2) state, no events will be generated until the object is modified to eventReady(1) (or eventAlwaysReady(3)).  The management station can thus easily respond to a notification of an event by re\-enabling this object.  If the management station wishes to disable this flow control and allow events to be generated at will, this object may be set to eventAlwaysReady(3).  Disabling the flow control is discouraged as it can result in high network traffic or other performance problems
            	**type**\:   :py:class:`Channeleventstatus <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Channeltable.Channelentry.Channeleventstatus>`
            
            .. attribute:: channelifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device to which the associated filters are applied to allow data into this channel.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in RFC 2233 [17].  The filters in this group are applied to all packets on the local network segment attached to the identified interface.  An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry.  For example, a hot\-pluggable ethernet card could be pulled out and replaced by a token\-ring card.  In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: channelmatches
            
            	The number of times this channel has matched a packet. Note that this object is updated even when channelDataControl is set to off
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: channelowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: channelstatus
            
            	The status of this channel entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: channelturnoffeventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from on to off when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOffEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: channelturnoneventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from off to on when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOnEventIndex must be set to zero, a non\-existent event index. This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Channeltable.Channelentry, self).__init__()

                self.yang_name = "channelEntry"
                self.yang_parent_name = "channelTable"

                self.channelindex = YLeaf(YType.int32, "channelIndex")

                self.channelaccepttype = YLeaf(YType.enumeration, "channelAcceptType")

                self.channelcreatetime = YLeaf(YType.uint32, "RMON2-MIB:channelCreateTime")

                self.channeldatacontrol = YLeaf(YType.enumeration, "channelDataControl")

                self.channeldescription = YLeaf(YType.str, "channelDescription")

                self.channeldroppedframes = YLeaf(YType.uint32, "RMON2-MIB:channelDroppedFrames")

                self.channeleventindex = YLeaf(YType.int32, "channelEventIndex")

                self.channeleventstatus = YLeaf(YType.enumeration, "channelEventStatus")

                self.channelifindex = YLeaf(YType.int32, "channelIfIndex")

                self.channelmatches = YLeaf(YType.uint32, "channelMatches")

                self.channelowner = YLeaf(YType.str, "channelOwner")

                self.channelstatus = YLeaf(YType.enumeration, "channelStatus")

                self.channelturnoffeventindex = YLeaf(YType.int32, "channelTurnOffEventIndex")

                self.channelturnoneventindex = YLeaf(YType.int32, "channelTurnOnEventIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("channelindex",
                                "channelaccepttype",
                                "channelcreatetime",
                                "channeldatacontrol",
                                "channeldescription",
                                "channeldroppedframes",
                                "channeleventindex",
                                "channeleventstatus",
                                "channelifindex",
                                "channelmatches",
                                "channelowner",
                                "channelstatus",
                                "channelturnoffeventindex",
                                "channelturnoneventindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Channeltable.Channelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Channeltable.Channelentry, self).__setattr__(name, value)

            class Channelaccepttype(Enum):
                """
                Channelaccepttype

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
                Channeldatacontrol

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
                Channeleventstatus

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


            def has_data(self):
                return (
                    self.channelindex.is_set or
                    self.channelaccepttype.is_set or
                    self.channelcreatetime.is_set or
                    self.channeldatacontrol.is_set or
                    self.channeldescription.is_set or
                    self.channeldroppedframes.is_set or
                    self.channeleventindex.is_set or
                    self.channeleventstatus.is_set or
                    self.channelifindex.is_set or
                    self.channelmatches.is_set or
                    self.channelowner.is_set or
                    self.channelstatus.is_set or
                    self.channelturnoffeventindex.is_set or
                    self.channelturnoneventindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.channelindex.yfilter != YFilter.not_set or
                    self.channelaccepttype.yfilter != YFilter.not_set or
                    self.channelcreatetime.yfilter != YFilter.not_set or
                    self.channeldatacontrol.yfilter != YFilter.not_set or
                    self.channeldescription.yfilter != YFilter.not_set or
                    self.channeldroppedframes.yfilter != YFilter.not_set or
                    self.channeleventindex.yfilter != YFilter.not_set or
                    self.channeleventstatus.yfilter != YFilter.not_set or
                    self.channelifindex.yfilter != YFilter.not_set or
                    self.channelmatches.yfilter != YFilter.not_set or
                    self.channelowner.yfilter != YFilter.not_set or
                    self.channelstatus.yfilter != YFilter.not_set or
                    self.channelturnoffeventindex.yfilter != YFilter.not_set or
                    self.channelturnoneventindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "channelEntry" + "[channelIndex='" + self.channelindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/channelTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.channelindex.is_set or self.channelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelindex.get_name_leafdata())
                if (self.channelaccepttype.is_set or self.channelaccepttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelaccepttype.get_name_leafdata())
                if (self.channelcreatetime.is_set or self.channelcreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelcreatetime.get_name_leafdata())
                if (self.channeldatacontrol.is_set or self.channeldatacontrol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channeldatacontrol.get_name_leafdata())
                if (self.channeldescription.is_set or self.channeldescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channeldescription.get_name_leafdata())
                if (self.channeldroppedframes.is_set or self.channeldroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channeldroppedframes.get_name_leafdata())
                if (self.channeleventindex.is_set or self.channeleventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channeleventindex.get_name_leafdata())
                if (self.channeleventstatus.is_set or self.channeleventstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channeleventstatus.get_name_leafdata())
                if (self.channelifindex.is_set or self.channelifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelifindex.get_name_leafdata())
                if (self.channelmatches.is_set or self.channelmatches.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelmatches.get_name_leafdata())
                if (self.channelowner.is_set or self.channelowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelowner.get_name_leafdata())
                if (self.channelstatus.is_set or self.channelstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelstatus.get_name_leafdata())
                if (self.channelturnoffeventindex.is_set or self.channelturnoffeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelturnoffeventindex.get_name_leafdata())
                if (self.channelturnoneventindex.is_set or self.channelturnoneventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.channelturnoneventindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "channelIndex" or name == "channelAcceptType" or name == "channelCreateTime" or name == "channelDataControl" or name == "channelDescription" or name == "channelDroppedFrames" or name == "channelEventIndex" or name == "channelEventStatus" or name == "channelIfIndex" or name == "channelMatches" or name == "channelOwner" or name == "channelStatus" or name == "channelTurnOffEventIndex" or name == "channelTurnOnEventIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "channelIndex"):
                    self.channelindex = value
                    self.channelindex.value_namespace = name_space
                    self.channelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "channelAcceptType"):
                    self.channelaccepttype = value
                    self.channelaccepttype.value_namespace = name_space
                    self.channelaccepttype.value_namespace_prefix = name_space_prefix
                if(value_path == "channelCreateTime"):
                    self.channelcreatetime = value
                    self.channelcreatetime.value_namespace = name_space
                    self.channelcreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "channelDataControl"):
                    self.channeldatacontrol = value
                    self.channeldatacontrol.value_namespace = name_space
                    self.channeldatacontrol.value_namespace_prefix = name_space_prefix
                if(value_path == "channelDescription"):
                    self.channeldescription = value
                    self.channeldescription.value_namespace = name_space
                    self.channeldescription.value_namespace_prefix = name_space_prefix
                if(value_path == "channelDroppedFrames"):
                    self.channeldroppedframes = value
                    self.channeldroppedframes.value_namespace = name_space
                    self.channeldroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "channelEventIndex"):
                    self.channeleventindex = value
                    self.channeleventindex.value_namespace = name_space
                    self.channeleventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "channelEventStatus"):
                    self.channeleventstatus = value
                    self.channeleventstatus.value_namespace = name_space
                    self.channeleventstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "channelIfIndex"):
                    self.channelifindex = value
                    self.channelifindex.value_namespace = name_space
                    self.channelifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "channelMatches"):
                    self.channelmatches = value
                    self.channelmatches.value_namespace = name_space
                    self.channelmatches.value_namespace_prefix = name_space_prefix
                if(value_path == "channelOwner"):
                    self.channelowner = value
                    self.channelowner.value_namespace = name_space
                    self.channelowner.value_namespace_prefix = name_space_prefix
                if(value_path == "channelStatus"):
                    self.channelstatus = value
                    self.channelstatus.value_namespace = name_space
                    self.channelstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "channelTurnOffEventIndex"):
                    self.channelturnoffeventindex = value
                    self.channelturnoffeventindex.value_namespace = name_space
                    self.channelturnoffeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "channelTurnOnEventIndex"):
                    self.channelturnoneventindex = value
                    self.channelturnoneventindex.value_namespace = name_space
                    self.channelturnoneventindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.channelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.channelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "channelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "channelEntry"):
                for c in self.channelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Channeltable.Channelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.channelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "channelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Buffercontroltable(Entity):
        """
        A list of buffers control entries.
        
        .. attribute:: buffercontrolentry
        
        	A set of parameters that control the collection of a stream of packets that have matched filters.  As an example, an instance of the bufferControlCaptureSliceSize object might be named bufferControlCaptureSliceSize.3
        	**type**\: list of    :py:class:`Buffercontrolentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Buffercontroltable.Buffercontrolentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Buffercontroltable, self).__init__()

            self.yang_name = "bufferControlTable"
            self.yang_parent_name = "RMON-MIB"

            self.buffercontrolentry = YList(self)

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
                        super(RmonMib.Buffercontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Buffercontroltable, self).__setattr__(name, value)


        class Buffercontrolentry(Entity):
            """
            A set of parameters that control the collection of a stream
            of packets that have matched filters.  As an example, an
            instance of the bufferControlCaptureSliceSize object might
            be named bufferControlCaptureSliceSize.3
            
            .. attribute:: buffercontrolindex  <key>
            
            	An index that uniquely identifies an entry in the bufferControl table.  The value of this index shall never be zero.  Each such entry defines one set of packets that is captured and controlled by one or more filters
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontrolcapturedpackets
            
            	The number of packets currently in this captureBuffer
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Packets
            
            .. attribute:: buffercontrolcaptureslicesize
            
            	The maximum number of octets of each packet that will be saved in this capture buffer. For example, if a 1500 octet packet is received by the probe and this object is set to 500, then only 500 octets of the packet will be stored in the associated capture buffer.  If this variable is set to 0, the capture buffer will save as many octets as is possible.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolchannelindex
            
            	An index that identifies the channel that is the source of packets for this bufferControl table. The channel identified by a particular value of this index is the same as identified by the same value of the channelIndex object.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontroldownloadoffset
            
            	The offset of the first octet of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer and this object is set to 100, then the captureBufferPacket object that contains the packet will contain bytes starting 100 octets into the packet
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontroldownloadslicesize
            
            	The maximum number of octets of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer, the associated bufferControlDownloadOffset is 0, and this object is set to 100, then the captureBufferPacket object that contains the packet will contain only the first 100 octets of the packet.  A prudent manager will take into account possible interoperability or fragmentation problems that may occur if the download slice size is set too large. In particular, conformant SNMP implementations are not required to accept messages whose length exceeds 484 octets, although they are encouraged to support larger datagrams whenever feasible
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolfullaction
            
            	Controls the action of the buffer when it reaches the full status.  When in the lockWhenFull(1) state and a packet is added to the buffer that fills the buffer, the bufferControlFullStatus will be set to full(2) and this buffer will stop capturing packets
            	**type**\:   :py:class:`Buffercontrolfullaction <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Buffercontroltable.Buffercontrolentry.Buffercontrolfullaction>`
            
            .. attribute:: buffercontrolfullstatus
            
            	This object shows whether the buffer has room to accept new packets or if it is full.  If the status is spaceAvailable(1), the buffer is accepting new packets normally.  If the status is full(2) and the associated bufferControlFullAction object is wrapWhenFull, the buffer is accepting new packets by deleting enough of the oldest packets to make room for new ones as they arrive.  Otherwise, if the status is full(2) and the bufferControlFullAction object is lockWhenFull, then the buffer has stopped collecting packets.  When this object is set to full(2) the probe must not later set it to spaceAvailable(1) except in the case of a significant gain in resources such as an increase of bufferControlOctetsGranted.  In particular, the wrap\-mode action of deleting old packets to make room for newly arrived packets must not affect the value of this object
            	**type**\:   :py:class:`Buffercontrolfullstatus <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Buffercontroltable.Buffercontrolentry.Buffercontrolfullstatus>`
            
            .. attribute:: buffercontrolmaxoctetsgranted
            
            	The maximum number of octets that can be saved in this captureBuffer, including overhead. If this variable is \-1, the capture buffer will save as many octets as possible.  When the bufferControlMaxOctetsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources. However, if the request object has the special value of \-1, the probe must set this object to \-1.  The probe must not lower this value except as a result of a modification to the associated bufferControlMaxOctetsRequested object.  When this maximum number of octets is reached and a new packet is to be added to this capture buffer and the corresponding bufferControlFullAction is set to wrapWhenFull(2), enough of the oldest packets associated with this capture buffer shall be deleted by the agent so that the new packet can be added.  If the corresponding bufferControlFullAction is set to lockWhenFull(1), the new packet shall be discarded.  In either case, the probe must set bufferControlFullStatus to full(2).  When the value of this object changes to a value less than the current value, entries are deleted from the captureBufferTable associated with this bufferControlEntry.  Enough of the oldest of these captureBufferEntries shall be deleted by the agent so that the number of octets used remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated captureBufferEntries may be allowed to grow
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolmaxoctetsrequested
            
            	The requested maximum number of octets to be saved in this captureBuffer, including any implementation\-specific overhead. If this variable is set to \-1, the capture buffer will save as many octets as is possible.  When this object is created or modified, the probe should set bufferControlMaxOctetsGranted as closely to this object as is possible for the particular probe implementation and available resources.  However, if the object has the special value of \-1, the probe must set bufferControlMaxOctetsGranted to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: buffercontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: buffercontrolstatus
            
            	The status of this buffer Control Entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: buffercontrolturnontime
            
            	The value of sysUpTime when this capture buffer was first turned on
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Buffercontroltable.Buffercontrolentry, self).__init__()

                self.yang_name = "bufferControlEntry"
                self.yang_parent_name = "bufferControlTable"

                self.buffercontrolindex = YLeaf(YType.int32, "bufferControlIndex")

                self.buffercontrolcapturedpackets = YLeaf(YType.int32, "bufferControlCapturedPackets")

                self.buffercontrolcaptureslicesize = YLeaf(YType.int32, "bufferControlCaptureSliceSize")

                self.buffercontrolchannelindex = YLeaf(YType.int32, "bufferControlChannelIndex")

                self.buffercontroldownloadoffset = YLeaf(YType.int32, "bufferControlDownloadOffset")

                self.buffercontroldownloadslicesize = YLeaf(YType.int32, "bufferControlDownloadSliceSize")

                self.buffercontrolfullaction = YLeaf(YType.enumeration, "bufferControlFullAction")

                self.buffercontrolfullstatus = YLeaf(YType.enumeration, "bufferControlFullStatus")

                self.buffercontrolmaxoctetsgranted = YLeaf(YType.int32, "bufferControlMaxOctetsGranted")

                self.buffercontrolmaxoctetsrequested = YLeaf(YType.int32, "bufferControlMaxOctetsRequested")

                self.buffercontrolowner = YLeaf(YType.str, "bufferControlOwner")

                self.buffercontrolstatus = YLeaf(YType.enumeration, "bufferControlStatus")

                self.buffercontrolturnontime = YLeaf(YType.uint32, "bufferControlTurnOnTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("buffercontrolindex",
                                "buffercontrolcapturedpackets",
                                "buffercontrolcaptureslicesize",
                                "buffercontrolchannelindex",
                                "buffercontroldownloadoffset",
                                "buffercontroldownloadslicesize",
                                "buffercontrolfullaction",
                                "buffercontrolfullstatus",
                                "buffercontrolmaxoctetsgranted",
                                "buffercontrolmaxoctetsrequested",
                                "buffercontrolowner",
                                "buffercontrolstatus",
                                "buffercontrolturnontime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Buffercontroltable.Buffercontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Buffercontroltable.Buffercontrolentry, self).__setattr__(name, value)

            class Buffercontrolfullaction(Enum):
                """
                Buffercontrolfullaction

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
                Buffercontrolfullstatus

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


            def has_data(self):
                return (
                    self.buffercontrolindex.is_set or
                    self.buffercontrolcapturedpackets.is_set or
                    self.buffercontrolcaptureslicesize.is_set or
                    self.buffercontrolchannelindex.is_set or
                    self.buffercontroldownloadoffset.is_set or
                    self.buffercontroldownloadslicesize.is_set or
                    self.buffercontrolfullaction.is_set or
                    self.buffercontrolfullstatus.is_set or
                    self.buffercontrolmaxoctetsgranted.is_set or
                    self.buffercontrolmaxoctetsrequested.is_set or
                    self.buffercontrolowner.is_set or
                    self.buffercontrolstatus.is_set or
                    self.buffercontrolturnontime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.buffercontrolindex.yfilter != YFilter.not_set or
                    self.buffercontrolcapturedpackets.yfilter != YFilter.not_set or
                    self.buffercontrolcaptureslicesize.yfilter != YFilter.not_set or
                    self.buffercontrolchannelindex.yfilter != YFilter.not_set or
                    self.buffercontroldownloadoffset.yfilter != YFilter.not_set or
                    self.buffercontroldownloadslicesize.yfilter != YFilter.not_set or
                    self.buffercontrolfullaction.yfilter != YFilter.not_set or
                    self.buffercontrolfullstatus.yfilter != YFilter.not_set or
                    self.buffercontrolmaxoctetsgranted.yfilter != YFilter.not_set or
                    self.buffercontrolmaxoctetsrequested.yfilter != YFilter.not_set or
                    self.buffercontrolowner.yfilter != YFilter.not_set or
                    self.buffercontrolstatus.yfilter != YFilter.not_set or
                    self.buffercontrolturnontime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bufferControlEntry" + "[bufferControlIndex='" + self.buffercontrolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/bufferControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.buffercontrolindex.is_set or self.buffercontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolindex.get_name_leafdata())
                if (self.buffercontrolcapturedpackets.is_set or self.buffercontrolcapturedpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolcapturedpackets.get_name_leafdata())
                if (self.buffercontrolcaptureslicesize.is_set or self.buffercontrolcaptureslicesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolcaptureslicesize.get_name_leafdata())
                if (self.buffercontrolchannelindex.is_set or self.buffercontrolchannelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolchannelindex.get_name_leafdata())
                if (self.buffercontroldownloadoffset.is_set or self.buffercontroldownloadoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontroldownloadoffset.get_name_leafdata())
                if (self.buffercontroldownloadslicesize.is_set or self.buffercontroldownloadslicesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontroldownloadslicesize.get_name_leafdata())
                if (self.buffercontrolfullaction.is_set or self.buffercontrolfullaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolfullaction.get_name_leafdata())
                if (self.buffercontrolfullstatus.is_set or self.buffercontrolfullstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolfullstatus.get_name_leafdata())
                if (self.buffercontrolmaxoctetsgranted.is_set or self.buffercontrolmaxoctetsgranted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolmaxoctetsgranted.get_name_leafdata())
                if (self.buffercontrolmaxoctetsrequested.is_set or self.buffercontrolmaxoctetsrequested.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolmaxoctetsrequested.get_name_leafdata())
                if (self.buffercontrolowner.is_set or self.buffercontrolowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolowner.get_name_leafdata())
                if (self.buffercontrolstatus.is_set or self.buffercontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolstatus.get_name_leafdata())
                if (self.buffercontrolturnontime.is_set or self.buffercontrolturnontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffercontrolturnontime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bufferControlIndex" or name == "bufferControlCapturedPackets" or name == "bufferControlCaptureSliceSize" or name == "bufferControlChannelIndex" or name == "bufferControlDownloadOffset" or name == "bufferControlDownloadSliceSize" or name == "bufferControlFullAction" or name == "bufferControlFullStatus" or name == "bufferControlMaxOctetsGranted" or name == "bufferControlMaxOctetsRequested" or name == "bufferControlOwner" or name == "bufferControlStatus" or name == "bufferControlTurnOnTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bufferControlIndex"):
                    self.buffercontrolindex = value
                    self.buffercontrolindex.value_namespace = name_space
                    self.buffercontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlCapturedPackets"):
                    self.buffercontrolcapturedpackets = value
                    self.buffercontrolcapturedpackets.value_namespace = name_space
                    self.buffercontrolcapturedpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlCaptureSliceSize"):
                    self.buffercontrolcaptureslicesize = value
                    self.buffercontrolcaptureslicesize.value_namespace = name_space
                    self.buffercontrolcaptureslicesize.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlChannelIndex"):
                    self.buffercontrolchannelindex = value
                    self.buffercontrolchannelindex.value_namespace = name_space
                    self.buffercontrolchannelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlDownloadOffset"):
                    self.buffercontroldownloadoffset = value
                    self.buffercontroldownloadoffset.value_namespace = name_space
                    self.buffercontroldownloadoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlDownloadSliceSize"):
                    self.buffercontroldownloadslicesize = value
                    self.buffercontroldownloadslicesize.value_namespace = name_space
                    self.buffercontroldownloadslicesize.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlFullAction"):
                    self.buffercontrolfullaction = value
                    self.buffercontrolfullaction.value_namespace = name_space
                    self.buffercontrolfullaction.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlFullStatus"):
                    self.buffercontrolfullstatus = value
                    self.buffercontrolfullstatus.value_namespace = name_space
                    self.buffercontrolfullstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlMaxOctetsGranted"):
                    self.buffercontrolmaxoctetsgranted = value
                    self.buffercontrolmaxoctetsgranted.value_namespace = name_space
                    self.buffercontrolmaxoctetsgranted.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlMaxOctetsRequested"):
                    self.buffercontrolmaxoctetsrequested = value
                    self.buffercontrolmaxoctetsrequested.value_namespace = name_space
                    self.buffercontrolmaxoctetsrequested.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlOwner"):
                    self.buffercontrolowner = value
                    self.buffercontrolowner.value_namespace = name_space
                    self.buffercontrolowner.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlStatus"):
                    self.buffercontrolstatus = value
                    self.buffercontrolstatus.value_namespace = name_space
                    self.buffercontrolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "bufferControlTurnOnTime"):
                    self.buffercontrolturnontime = value
                    self.buffercontrolturnontime.value_namespace = name_space
                    self.buffercontrolturnontime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.buffercontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.buffercontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bufferControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bufferControlEntry"):
                for c in self.buffercontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Buffercontroltable.Buffercontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.buffercontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bufferControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Capturebuffertable(Entity):
        """
        A list of packets captured off of a channel.
        
        .. attribute:: capturebufferentry
        
        	A packet captured off of an attached network.  As an example, an instance of the captureBufferPacketData object might be named captureBufferPacketData.3.1783
        	**type**\: list of    :py:class:`Capturebufferentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Capturebuffertable.Capturebufferentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Capturebuffertable, self).__init__()

            self.yang_name = "captureBufferTable"
            self.yang_parent_name = "RMON-MIB"

            self.capturebufferentry = YList(self)

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
                        super(RmonMib.Capturebuffertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Capturebuffertable, self).__setattr__(name, value)


        class Capturebufferentry(Entity):
            """
            A packet captured off of an attached network.  As an
            example, an instance of the captureBufferPacketData
            object might be named captureBufferPacketData.3.1783
            
            .. attribute:: capturebuffercontrolindex  <key>
            
            	The index of the bufferControlEntry with which this packet is associated
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: capturebufferindex  <key>
            
            	An index that uniquely identifies an entry in the captureBuffer table associated with a particular bufferControlEntry.  This index will start at 1 and increase by one for each new packet added with the same captureBufferControlIndex.  Should this value reach 2147483647, the next packet added with the same captureBufferControlIndex shall cause this value to wrap around to 1
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: capturebufferpacketdata
            
            	The data inside the packet, starting at the beginning of the packet plus any offset specified in the associated bufferControlDownloadOffset, including any link level headers.  The length of the data in this object is the minimum of the length of the captured packet minus the offset, the length of the associated bufferControlCaptureSliceSize minus the offset, and the associated bufferControlDownloadSliceSize.  If this minimum is less than zero, this object shall have a length of zero
            	**type**\:  str
            
            .. attribute:: capturebufferpacketid
            
            	An index that describes the order of packets that are received on a particular interface. The packetID of a packet captured on an interface is defined to be greater than the packetID's of all packets captured previously on the same interface.  As the captureBufferPacketID object has a maximum positive value of 2^31 \- 1, any captureBufferPacketID object shall have the value of the associated packet's packetID mod 2^31
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpacketlength
            
            	The actual length (off the wire) of the packet stored in this entry, including FCS octets
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Octets
            
            .. attribute:: capturebufferpacketstatus
            
            	A value which indicates the error status of this packet.  The value of this object is defined in the same way as filterPktStatus.  The value is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment error         3    First packet in this capture buffer after              it was detected that some packets were              not processed correctly.         4    Packet's order in buffer is only approximate              (May only be set for packets sent from              the probe)  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpackettime
            
            	The number of milliseconds that had passed since this capture buffer was first turned on when this packet was captured
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: Milliseconds
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Capturebuffertable.Capturebufferentry, self).__init__()

                self.yang_name = "captureBufferEntry"
                self.yang_parent_name = "captureBufferTable"

                self.capturebuffercontrolindex = YLeaf(YType.int32, "captureBufferControlIndex")

                self.capturebufferindex = YLeaf(YType.int32, "captureBufferIndex")

                self.capturebufferpacketdata = YLeaf(YType.str, "captureBufferPacketData")

                self.capturebufferpacketid = YLeaf(YType.int32, "captureBufferPacketID")

                self.capturebufferpacketlength = YLeaf(YType.int32, "captureBufferPacketLength")

                self.capturebufferpacketstatus = YLeaf(YType.int32, "captureBufferPacketStatus")

                self.capturebufferpackettime = YLeaf(YType.int32, "captureBufferPacketTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("capturebuffercontrolindex",
                                "capturebufferindex",
                                "capturebufferpacketdata",
                                "capturebufferpacketid",
                                "capturebufferpacketlength",
                                "capturebufferpacketstatus",
                                "capturebufferpackettime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Capturebuffertable.Capturebufferentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Capturebuffertable.Capturebufferentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.capturebuffercontrolindex.is_set or
                    self.capturebufferindex.is_set or
                    self.capturebufferpacketdata.is_set or
                    self.capturebufferpacketid.is_set or
                    self.capturebufferpacketlength.is_set or
                    self.capturebufferpacketstatus.is_set or
                    self.capturebufferpackettime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.capturebuffercontrolindex.yfilter != YFilter.not_set or
                    self.capturebufferindex.yfilter != YFilter.not_set or
                    self.capturebufferpacketdata.yfilter != YFilter.not_set or
                    self.capturebufferpacketid.yfilter != YFilter.not_set or
                    self.capturebufferpacketlength.yfilter != YFilter.not_set or
                    self.capturebufferpacketstatus.yfilter != YFilter.not_set or
                    self.capturebufferpackettime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "captureBufferEntry" + "[captureBufferControlIndex='" + self.capturebuffercontrolindex.get() + "']" + "[captureBufferIndex='" + self.capturebufferindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/captureBufferTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.capturebuffercontrolindex.is_set or self.capturebuffercontrolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebuffercontrolindex.get_name_leafdata())
                if (self.capturebufferindex.is_set or self.capturebufferindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferindex.get_name_leafdata())
                if (self.capturebufferpacketdata.is_set or self.capturebufferpacketdata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferpacketdata.get_name_leafdata())
                if (self.capturebufferpacketid.is_set or self.capturebufferpacketid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferpacketid.get_name_leafdata())
                if (self.capturebufferpacketlength.is_set or self.capturebufferpacketlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferpacketlength.get_name_leafdata())
                if (self.capturebufferpacketstatus.is_set or self.capturebufferpacketstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferpacketstatus.get_name_leafdata())
                if (self.capturebufferpackettime.is_set or self.capturebufferpackettime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capturebufferpackettime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "captureBufferControlIndex" or name == "captureBufferIndex" or name == "captureBufferPacketData" or name == "captureBufferPacketID" or name == "captureBufferPacketLength" or name == "captureBufferPacketStatus" or name == "captureBufferPacketTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "captureBufferControlIndex"):
                    self.capturebuffercontrolindex = value
                    self.capturebuffercontrolindex.value_namespace = name_space
                    self.capturebuffercontrolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferIndex"):
                    self.capturebufferindex = value
                    self.capturebufferindex.value_namespace = name_space
                    self.capturebufferindex.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferPacketData"):
                    self.capturebufferpacketdata = value
                    self.capturebufferpacketdata.value_namespace = name_space
                    self.capturebufferpacketdata.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferPacketID"):
                    self.capturebufferpacketid = value
                    self.capturebufferpacketid.value_namespace = name_space
                    self.capturebufferpacketid.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferPacketLength"):
                    self.capturebufferpacketlength = value
                    self.capturebufferpacketlength.value_namespace = name_space
                    self.capturebufferpacketlength.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferPacketStatus"):
                    self.capturebufferpacketstatus = value
                    self.capturebufferpacketstatus.value_namespace = name_space
                    self.capturebufferpacketstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "captureBufferPacketTime"):
                    self.capturebufferpackettime = value
                    self.capturebufferpackettime.value_namespace = name_space
                    self.capturebufferpackettime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.capturebufferentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.capturebufferentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "captureBufferTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "captureBufferEntry"):
                for c in self.capturebufferentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Capturebuffertable.Capturebufferentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.capturebufferentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "captureBufferEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Eventtable(Entity):
        """
        A list of events to be generated.
        
        .. attribute:: evententry
        
        	A set of parameters that describe an event to be generated when certain conditions are met.  As an example, an instance of the eventLastTimeSent object might be named eventLastTimeSent.6
        	**type**\: list of    :py:class:`Evententry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Eventtable.Evententry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Eventtable, self).__init__()

            self.yang_name = "eventTable"
            self.yang_parent_name = "RMON-MIB"

            self.evententry = YList(self)

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
                        super(RmonMib.Eventtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Eventtable, self).__setattr__(name, value)


        class Evententry(Entity):
            """
            A set of parameters that describe an event to be generated
            when certain conditions are met.  As an example, an instance
            of the eventLastTimeSent object might be named
            eventLastTimeSent.6
            
            .. attribute:: eventindex  <key>
            
            	An index that uniquely identifies an entry in the event table.  Each such entry defines one event that is to be generated when the appropriate conditions occur
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: eventcommunity
            
            	If an SNMP trap is to be sent, it will be sent to the SNMP community specified by this octet string
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: eventdescription
            
            	A comment describing this event entry
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: eventlasttimesent
            
            	The value of sysUpTime at the time this event entry last generated an event.  If this entry has not generated any events, this value will be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: eventowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it.  If this object contains a string starting with 'monitor' and has associated entries in the log table, all connected management stations should retrieve those log entries, as they may have significance to all management stations connected to this device
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: eventstatus
            
            	The status of this event entry.  If this object is not equal to valid(1), all associated log entries shall be deleted by the agent
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.RMON_MIB.Entrystatus>`
            
            .. attribute:: eventtype
            
            	The type of notification that the probe will make about this event.  In the case of log, an entry is made in the log table for each event.  In the case of snmp\-trap, an SNMP trap is sent to one or more management stations
            	**type**\:   :py:class:`Eventtype <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Eventtable.Evententry.Eventtype>`
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Eventtable.Evententry, self).__init__()

                self.yang_name = "eventEntry"
                self.yang_parent_name = "eventTable"

                self.eventindex = YLeaf(YType.int32, "eventIndex")

                self.eventcommunity = YLeaf(YType.str, "eventCommunity")

                self.eventdescription = YLeaf(YType.str, "eventDescription")

                self.eventlasttimesent = YLeaf(YType.uint32, "eventLastTimeSent")

                self.eventowner = YLeaf(YType.str, "eventOwner")

                self.eventstatus = YLeaf(YType.enumeration, "eventStatus")

                self.eventtype = YLeaf(YType.enumeration, "eventType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("eventindex",
                                "eventcommunity",
                                "eventdescription",
                                "eventlasttimesent",
                                "eventowner",
                                "eventstatus",
                                "eventtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Eventtable.Evententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Eventtable.Evententry, self).__setattr__(name, value)

            class Eventtype(Enum):
                """
                Eventtype

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


            def has_data(self):
                return (
                    self.eventindex.is_set or
                    self.eventcommunity.is_set or
                    self.eventdescription.is_set or
                    self.eventlasttimesent.is_set or
                    self.eventowner.is_set or
                    self.eventstatus.is_set or
                    self.eventtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.eventindex.yfilter != YFilter.not_set or
                    self.eventcommunity.yfilter != YFilter.not_set or
                    self.eventdescription.yfilter != YFilter.not_set or
                    self.eventlasttimesent.yfilter != YFilter.not_set or
                    self.eventowner.yfilter != YFilter.not_set or
                    self.eventstatus.yfilter != YFilter.not_set or
                    self.eventtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "eventEntry" + "[eventIndex='" + self.eventindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/eventTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.eventindex.is_set or self.eventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventindex.get_name_leafdata())
                if (self.eventcommunity.is_set or self.eventcommunity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventcommunity.get_name_leafdata())
                if (self.eventdescription.is_set or self.eventdescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventdescription.get_name_leafdata())
                if (self.eventlasttimesent.is_set or self.eventlasttimesent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventlasttimesent.get_name_leafdata())
                if (self.eventowner.is_set or self.eventowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventowner.get_name_leafdata())
                if (self.eventstatus.is_set or self.eventstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventstatus.get_name_leafdata())
                if (self.eventtype.is_set or self.eventtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eventtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "eventIndex" or name == "eventCommunity" or name == "eventDescription" or name == "eventLastTimeSent" or name == "eventOwner" or name == "eventStatus" or name == "eventType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "eventIndex"):
                    self.eventindex = value
                    self.eventindex.value_namespace = name_space
                    self.eventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "eventCommunity"):
                    self.eventcommunity = value
                    self.eventcommunity.value_namespace = name_space
                    self.eventcommunity.value_namespace_prefix = name_space_prefix
                if(value_path == "eventDescription"):
                    self.eventdescription = value
                    self.eventdescription.value_namespace = name_space
                    self.eventdescription.value_namespace_prefix = name_space_prefix
                if(value_path == "eventLastTimeSent"):
                    self.eventlasttimesent = value
                    self.eventlasttimesent.value_namespace = name_space
                    self.eventlasttimesent.value_namespace_prefix = name_space_prefix
                if(value_path == "eventOwner"):
                    self.eventowner = value
                    self.eventowner.value_namespace = name_space
                    self.eventowner.value_namespace_prefix = name_space_prefix
                if(value_path == "eventStatus"):
                    self.eventstatus = value
                    self.eventstatus.value_namespace = name_space
                    self.eventstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "eventType"):
                    self.eventtype = value
                    self.eventtype.value_namespace = name_space
                    self.eventtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.evententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.evententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "eventTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "eventEntry"):
                for c in self.evententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Eventtable.Evententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.evententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "eventEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Logtable(Entity):
        """
        A list of events that have been logged.
        
        .. attribute:: logentry
        
        	A set of data describing an event that has been logged.  For example, an instance of the logDescription object might be named logDescription.6.47
        	**type**\: list of    :py:class:`Logentry <ydk.models.cisco_ios_xe.RMON_MIB.RmonMib.Logtable.Logentry>`
        
        

        """

        _prefix = 'RMON-MIB'
        _revision = '2000-05-11'

        def __init__(self):
            super(RmonMib.Logtable, self).__init__()

            self.yang_name = "logTable"
            self.yang_parent_name = "RMON-MIB"

            self.logentry = YList(self)

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
                        super(RmonMib.Logtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RmonMib.Logtable, self).__setattr__(name, value)


        class Logentry(Entity):
            """
            A set of data describing an event that has been
            logged.  For example, an instance of the logDescription
            object might be named logDescription.6.47
            
            .. attribute:: logeventindex  <key>
            
            	The event entry that generated this log entry.  The log identified by a particular value of this index is associated with the same eventEntry as identified by the same value of eventIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: logindex  <key>
            
            	An index that uniquely identifies an entry in the log table amongst those generated by the same eventEntries.  These indexes are assigned beginning with 1 and increase by one with each new log entry.  The association between values of logIndex and logEntries is fixed for the lifetime of each logEntry. The agent may choose to delete the oldest instances of logEntry as required because of lack of memory.  It is an implementation\-specific matter as to when this deletion may occur
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: logdescription
            
            	An implementation dependent description of the event that activated this log entry
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: logtime
            
            	The value of sysUpTime when this log entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RMON-MIB'
            _revision = '2000-05-11'

            def __init__(self):
                super(RmonMib.Logtable.Logentry, self).__init__()

                self.yang_name = "logEntry"
                self.yang_parent_name = "logTable"

                self.logeventindex = YLeaf(YType.int32, "logEventIndex")

                self.logindex = YLeaf(YType.int32, "logIndex")

                self.logdescription = YLeaf(YType.str, "logDescription")

                self.logtime = YLeaf(YType.uint32, "logTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("logeventindex",
                                "logindex",
                                "logdescription",
                                "logtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RmonMib.Logtable.Logentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RmonMib.Logtable.Logentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.logeventindex.is_set or
                    self.logindex.is_set or
                    self.logdescription.is_set or
                    self.logtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.logeventindex.yfilter != YFilter.not_set or
                    self.logindex.yfilter != YFilter.not_set or
                    self.logdescription.yfilter != YFilter.not_set or
                    self.logtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "logEntry" + "[logEventIndex='" + self.logeventindex.get() + "']" + "[logIndex='" + self.logindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RMON-MIB:RMON-MIB/logTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.logeventindex.is_set or self.logeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.logeventindex.get_name_leafdata())
                if (self.logindex.is_set or self.logindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.logindex.get_name_leafdata())
                if (self.logdescription.is_set or self.logdescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.logdescription.get_name_leafdata())
                if (self.logtime.is_set or self.logtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.logtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "logEventIndex" or name == "logIndex" or name == "logDescription" or name == "logTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "logEventIndex"):
                    self.logeventindex = value
                    self.logeventindex.value_namespace = name_space
                    self.logeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "logIndex"):
                    self.logindex = value
                    self.logindex.value_namespace = name_space
                    self.logindex.value_namespace_prefix = name_space_prefix
                if(value_path == "logDescription"):
                    self.logdescription = value
                    self.logdescription.value_namespace = name_space
                    self.logdescription.value_namespace_prefix = name_space_prefix
                if(value_path == "logTime"):
                    self.logtime = value
                    self.logtime.value_namespace = name_space
                    self.logtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.logentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.logentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RMON-MIB:RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "logEntry"):
                for c in self.logentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RmonMib.Logtable.Logentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.logentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "logEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.alarmtable is not None and self.alarmtable.has_data()) or
            (self.buffercontroltable is not None and self.buffercontroltable.has_data()) or
            (self.capturebuffertable is not None and self.capturebuffertable.has_data()) or
            (self.channeltable is not None and self.channeltable.has_data()) or
            (self.etherhistorytable is not None and self.etherhistorytable.has_data()) or
            (self.etherstatstable is not None and self.etherstatstable.has_data()) or
            (self.eventtable is not None and self.eventtable.has_data()) or
            (self.filtertable is not None and self.filtertable.has_data()) or
            (self.historycontroltable is not None and self.historycontroltable.has_data()) or
            (self.hostcontroltable is not None and self.hostcontroltable.has_data()) or
            (self.hosttable is not None and self.hosttable.has_data()) or
            (self.hosttimetable is not None and self.hosttimetable.has_data()) or
            (self.hosttopncontroltable is not None and self.hosttopncontroltable.has_data()) or
            (self.hosttopntable is not None and self.hosttopntable.has_data()) or
            (self.logtable is not None and self.logtable.has_data()) or
            (self.matrixcontroltable is not None and self.matrixcontroltable.has_data()) or
            (self.matrixdstable is not None and self.matrixdstable.has_data()) or
            (self.matrixsdtable is not None and self.matrixsdtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.alarmtable is not None and self.alarmtable.has_operation()) or
            (self.buffercontroltable is not None and self.buffercontroltable.has_operation()) or
            (self.capturebuffertable is not None and self.capturebuffertable.has_operation()) or
            (self.channeltable is not None and self.channeltable.has_operation()) or
            (self.etherhistorytable is not None and self.etherhistorytable.has_operation()) or
            (self.etherstatstable is not None and self.etherstatstable.has_operation()) or
            (self.eventtable is not None and self.eventtable.has_operation()) or
            (self.filtertable is not None and self.filtertable.has_operation()) or
            (self.historycontroltable is not None and self.historycontroltable.has_operation()) or
            (self.hostcontroltable is not None and self.hostcontroltable.has_operation()) or
            (self.hosttable is not None and self.hosttable.has_operation()) or
            (self.hosttimetable is not None and self.hosttimetable.has_operation()) or
            (self.hosttopncontroltable is not None and self.hosttopncontroltable.has_operation()) or
            (self.hosttopntable is not None and self.hosttopntable.has_operation()) or
            (self.logtable is not None and self.logtable.has_operation()) or
            (self.matrixcontroltable is not None and self.matrixcontroltable.has_operation()) or
            (self.matrixdstable is not None and self.matrixdstable.has_operation()) or
            (self.matrixsdtable is not None and self.matrixsdtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "RMON-MIB:RMON-MIB" + path_buffer

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

        if (child_yang_name == "alarmTable"):
            if (self.alarmtable is None):
                self.alarmtable = RmonMib.Alarmtable()
                self.alarmtable.parent = self
                self._children_name_map["alarmtable"] = "alarmTable"
            return self.alarmtable

        if (child_yang_name == "bufferControlTable"):
            if (self.buffercontroltable is None):
                self.buffercontroltable = RmonMib.Buffercontroltable()
                self.buffercontroltable.parent = self
                self._children_name_map["buffercontroltable"] = "bufferControlTable"
            return self.buffercontroltable

        if (child_yang_name == "captureBufferTable"):
            if (self.capturebuffertable is None):
                self.capturebuffertable = RmonMib.Capturebuffertable()
                self.capturebuffertable.parent = self
                self._children_name_map["capturebuffertable"] = "captureBufferTable"
            return self.capturebuffertable

        if (child_yang_name == "channelTable"):
            if (self.channeltable is None):
                self.channeltable = RmonMib.Channeltable()
                self.channeltable.parent = self
                self._children_name_map["channeltable"] = "channelTable"
            return self.channeltable

        if (child_yang_name == "etherHistoryTable"):
            if (self.etherhistorytable is None):
                self.etherhistorytable = RmonMib.Etherhistorytable()
                self.etherhistorytable.parent = self
                self._children_name_map["etherhistorytable"] = "etherHistoryTable"
            return self.etherhistorytable

        if (child_yang_name == "etherStatsTable"):
            if (self.etherstatstable is None):
                self.etherstatstable = RmonMib.Etherstatstable()
                self.etherstatstable.parent = self
                self._children_name_map["etherstatstable"] = "etherStatsTable"
            return self.etherstatstable

        if (child_yang_name == "eventTable"):
            if (self.eventtable is None):
                self.eventtable = RmonMib.Eventtable()
                self.eventtable.parent = self
                self._children_name_map["eventtable"] = "eventTable"
            return self.eventtable

        if (child_yang_name == "filterTable"):
            if (self.filtertable is None):
                self.filtertable = RmonMib.Filtertable()
                self.filtertable.parent = self
                self._children_name_map["filtertable"] = "filterTable"
            return self.filtertable

        if (child_yang_name == "historyControlTable"):
            if (self.historycontroltable is None):
                self.historycontroltable = RmonMib.Historycontroltable()
                self.historycontroltable.parent = self
                self._children_name_map["historycontroltable"] = "historyControlTable"
            return self.historycontroltable

        if (child_yang_name == "hostControlTable"):
            if (self.hostcontroltable is None):
                self.hostcontroltable = RmonMib.Hostcontroltable()
                self.hostcontroltable.parent = self
                self._children_name_map["hostcontroltable"] = "hostControlTable"
            return self.hostcontroltable

        if (child_yang_name == "hostTable"):
            if (self.hosttable is None):
                self.hosttable = RmonMib.Hosttable()
                self.hosttable.parent = self
                self._children_name_map["hosttable"] = "hostTable"
            return self.hosttable

        if (child_yang_name == "hostTimeTable"):
            if (self.hosttimetable is None):
                self.hosttimetable = RmonMib.Hosttimetable()
                self.hosttimetable.parent = self
                self._children_name_map["hosttimetable"] = "hostTimeTable"
            return self.hosttimetable

        if (child_yang_name == "hostTopNControlTable"):
            if (self.hosttopncontroltable is None):
                self.hosttopncontroltable = RmonMib.Hosttopncontroltable()
                self.hosttopncontroltable.parent = self
                self._children_name_map["hosttopncontroltable"] = "hostTopNControlTable"
            return self.hosttopncontroltable

        if (child_yang_name == "hostTopNTable"):
            if (self.hosttopntable is None):
                self.hosttopntable = RmonMib.Hosttopntable()
                self.hosttopntable.parent = self
                self._children_name_map["hosttopntable"] = "hostTopNTable"
            return self.hosttopntable

        if (child_yang_name == "logTable"):
            if (self.logtable is None):
                self.logtable = RmonMib.Logtable()
                self.logtable.parent = self
                self._children_name_map["logtable"] = "logTable"
            return self.logtable

        if (child_yang_name == "matrixControlTable"):
            if (self.matrixcontroltable is None):
                self.matrixcontroltable = RmonMib.Matrixcontroltable()
                self.matrixcontroltable.parent = self
                self._children_name_map["matrixcontroltable"] = "matrixControlTable"
            return self.matrixcontroltable

        if (child_yang_name == "matrixDSTable"):
            if (self.matrixdstable is None):
                self.matrixdstable = RmonMib.Matrixdstable()
                self.matrixdstable.parent = self
                self._children_name_map["matrixdstable"] = "matrixDSTable"
            return self.matrixdstable

        if (child_yang_name == "matrixSDTable"):
            if (self.matrixsdtable is None):
                self.matrixsdtable = RmonMib.Matrixsdtable()
                self.matrixsdtable.parent = self
                self._children_name_map["matrixsdtable"] = "matrixSDTable"
            return self.matrixsdtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "alarmTable" or name == "bufferControlTable" or name == "captureBufferTable" or name == "channelTable" or name == "etherHistoryTable" or name == "etherStatsTable" or name == "eventTable" or name == "filterTable" or name == "historyControlTable" or name == "hostControlTable" or name == "hostTable" or name == "hostTimeTable" or name == "hostTopNControlTable" or name == "hostTopNTable" or name == "logTable" or name == "matrixControlTable" or name == "matrixDSTable" or name == "matrixSDTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RmonMib()
        return self._top_entity

