""" CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB 

The main purpose of this MIB is to define the statistics
information for Session Border Controller application. The 
statistics are mainly of two types \- Call statistics and 
Media statistics. The calls can further be categorized as SIP 
calls and H.248 calls.

This MIB categorizes the statistics information into following
four types\:
1. Global call statistics \- Represents the global call related
   statistics like call rates, media flows, signaling flows
   etc.

2. Periodic statistics \- Represents the SBC call statistics 
   information for a particular time interval like current 5 
   minutes, previous 5 minutes, current 15 minutes, previous 15
   minutes, current hour and previous hour.

3. Per flow statistics \- Represents the SBC media flow 
   statistics. These are media statistics for each of the
   current ongoing call flow.

4. H.248 statistics \- Represents the H.248 call related 
   statistics information when H.248 controller is associated
   with SBC.

The Session Border Controller (SBC) enables direct IP\-to\-IP
interconnect between multiple administrative domains for
session\-based services providing protocol inter\-working,
security, and admission control and management. The SBC is a
voice over IP (VoIP) device that sits on the border of a 
network and controls call admission to that network. 

The primary purpose of an SBC is to protect the interior of the
network from excessive call load and malicious traffic.
Additional functions provided by the SBC include media bridging
and billing services. 


GLOSSARY
SBC\: Session Border Controller

CSB\: CISCO Session Border Controller

CAC\: Call Admission Control \- protects voice traffic from the
negative effects of other voice traffic and to keep excess
voice traffic off the network. It is used to prevent congestion
in Voice traffic. It is used in the Call Setup phase.

RTP\: Real Time Transport Protocol \- defines a standardized
packet format for delivering audio and video over the Internet.

RTCP\: Real Time Control Protocol \- It is a sister protocol of
the Real\-time Transport Protocol (RTP). RTCP provides
out\-of\-band control information for an RTP flow. It partners
RTP in the delivery and packaging of multimedia data, but does
not transport any data itself. It is used periodically to
transmit control packets to participants in a streaming
multimedia session.

VMG\: Virtual Media Gateway \- introduced to bridge between
different transmission technologies and to add service to
end\-user connections. Its architecture separates control and
connectivity functions into physically separate network layers.

VPN\: Virtual Private Network \- It is a communications network
tunneled through another network, and dedicated for a specific
network.

Gate Id \- Context Identifiers assigned uniquely to a SIP/H.248
call flows.

Flow Pair Id\: Stream Identifiers assigned uniquely to a
SIP/H.248 call flows.

Adjacency\: An adjacency contains the system information to be
transmitted to next HOP.

REFERENCES
1. CISCO Session Border Controller Documents and FAQ
http\://zed.cisco.com/confluence/display/SBC/SBC

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoSbcPeriodicStatsInterval(Enum):
    """
    CiscoSbcPeriodicStatsInterval (Enum Class)

    This textual convention represents the interval values for

    which the periodic stats and history stats are to be displayed.

    fiveMinute \- Interval to display current/previous 5 minutes

    statistics information.

    fifteenMinute \- Interval to display current/previous 15 minutes

    statistics information.

    oneHour \- Interval to display current/previous one hour

    statistics information.

    oneDay \- Interval to display current/previous one day

    statistics information.

    .. data:: fiveMinute = 1

    .. data:: fifteenMinute = 2

    .. data:: oneHour = 3

    .. data:: oneDay = 4

    """

    fiveMinute = Enum.YLeaf(1, "fiveMinute")

    fifteenMinute = Enum.YLeaf(2, "fifteenMinute")

    oneHour = Enum.YLeaf(3, "oneHour")

    oneDay = Enum.YLeaf(4, "oneDay")



class CISCOSESSBORDERCTRLRCALLSTATSMIB(Entity):
    """
    
    
    .. attribute:: csbcallstatsinstancetable
    
    	The call stats instance table contains the physical index for each of the physical entity (line card, primary, secondary cards). The index of the table is instance index which uniquely identifies the physical entity present on the box
    	**type**\:  :py:class:`Csbcallstatsinstancetable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable>`
    
    .. attribute:: csbcallstatstable
    
    	This table describes the global statistics information in the form of a table which contains call specific information like call rates, media flows, signaling flows etc. The index of the table is service index which corresponds to a particular  service configured on the SBC and all the rows of the table represents the global information regarding all the call flows related to that particular service. The other index of this table is csbCallStatsInstanceIndex which is defined in csbCallStatsInstanceTable
    	**type**\:  :py:class:`Csbcallstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable>`
    
    .. attribute:: csbcurrperiodicstatstable
    
    	This table is used to collect measurement over several different intervals as defined by the csbCurrPeriodicStatsInterval object. When a new interval starts the objects associated with the interval are reset and count up throughout the interval. The index of the table is the interval for which the stats information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour and one day. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable.  The gauge values are reported as \:\- 1.If the period being queried is current5mins, this is the value at the instant that the query is issued.  2.Otherwise, for the other intevals, this is an average value during the summary period sampled at 5 minute intervals
    	**type**\:  :py:class:`Csbcurrperiodicstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable>`
    
    .. attribute:: csbhistorystatstable
    
    	This table provide historical measurement in various interval length defined by the csbHistoryStatsInterval object. Each interval may contain one or more entries to allow for detailed measurment to be collected. It is up to the platform to determine the number of intervals to be supported like  5 minutes, 15 minutes, 1 hour and 1 day. In addition, the number of historical entries is also determined by the platform resources.  The gauge values are reported as\: If the period being queried is previous5mins, this is the number of calls that were active at the end of the previous 5 minute period. Otherwise for the other intevals, this is an average value during the summary period, sampled at 5 minute intervals
    	**type**\:  :py:class:`Csbhistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable>`
    
    .. attribute:: csbperflowstatstable
    
    	This table describes statistics table for each call flow. The indices of the table are virtual media gateway id, gate id, falow pair id and side id (indices for side A or side B). The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:  :py:class:`Csbperflowstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable>`
    
    .. attribute:: csbh248statstable
    
    	This table describes the H.248 statistics for SBC. The index of the table is service index which corresponds to a particular  service configured on the SBC and the index assigned to a particular H.248 controller. The other index of this table is csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable. This table is replaced by the csbH248StatsRev1Table
    	**type**\:  :py:class:`Csbh248Statstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable>`
    
    	**status**\: deprecated
    
    .. attribute:: csbh248statsrev1table
    
    	This table describes the H.248 statistics for SBC. The index of the table is service index which corresponds to a particular  service configured on the SBC and the index assigned to a particular H.248 controller. The other index of this table is csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
    	**type**\:  :py:class:`Csbh248Statsrev1Table <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table>`
    
    

    """

    _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
    _revision = '2010-09-03'

    def __init__(self):
        super(CISCOSESSBORDERCTRLRCALLSTATSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
        self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("csbCallStatsInstanceTable", ("csbcallstatsinstancetable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable)), ("csbCallStatsTable", ("csbcallstatstable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable)), ("csbCurrPeriodicStatsTable", ("csbcurrperiodicstatstable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable)), ("csbHistoryStatsTable", ("csbhistorystatstable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable)), ("csbPerFlowStatsTable", ("csbperflowstatstable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable)), ("csbH248StatsTable", ("csbh248statstable", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable)), ("csbH248StatsRev1Table", ("csbh248statsrev1table", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.csbcallstatsinstancetable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable()
        self.csbcallstatsinstancetable.parent = self
        self._children_name_map["csbcallstatsinstancetable"] = "csbCallStatsInstanceTable"
        self._children_yang_names.add("csbCallStatsInstanceTable")

        self.csbcallstatstable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable()
        self.csbcallstatstable.parent = self
        self._children_name_map["csbcallstatstable"] = "csbCallStatsTable"
        self._children_yang_names.add("csbCallStatsTable")

        self.csbcurrperiodicstatstable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable()
        self.csbcurrperiodicstatstable.parent = self
        self._children_name_map["csbcurrperiodicstatstable"] = "csbCurrPeriodicStatsTable"
        self._children_yang_names.add("csbCurrPeriodicStatsTable")

        self.csbhistorystatstable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable()
        self.csbhistorystatstable.parent = self
        self._children_name_map["csbhistorystatstable"] = "csbHistoryStatsTable"
        self._children_yang_names.add("csbHistoryStatsTable")

        self.csbperflowstatstable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable()
        self.csbperflowstatstable.parent = self
        self._children_name_map["csbperflowstatstable"] = "csbPerFlowStatsTable"
        self._children_yang_names.add("csbPerFlowStatsTable")

        self.csbh248statstable = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable()
        self.csbh248statstable.parent = self
        self._children_name_map["csbh248statstable"] = "csbH248StatsTable"
        self._children_yang_names.add("csbH248StatsTable")

        self.csbh248statsrev1table = CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table()
        self.csbh248statsrev1table.parent = self
        self._children_name_map["csbh248statsrev1table"] = "csbH248StatsRev1Table"
        self._children_yang_names.add("csbH248StatsRev1Table")
        self._segment_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"


    class Csbcallstatsinstancetable(Entity):
        """
        The call stats instance table contains the physical index for
        each of the physical entity (line card, primary, secondary
        cards). The index of the table is instance index which uniquely
        identifies the physical entity present on the box.
        
        .. attribute:: csbcallstatsinstanceentry
        
        	A conceptual row in csbCallStatsInstanceTable. There is an entry in this table for each SBC instance, as identified by a  value of csbCallStatsInstanceIndex
        	**type**\: list of  		 :py:class:`Csbcallstatsinstanceentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable, self).__init__()

            self.yang_name = "csbCallStatsInstanceTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbCallStatsInstanceEntry", ("csbcallstatsinstanceentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry))])
            self._leafs = OrderedDict()

            self.csbcallstatsinstanceentry = YList(self)
            self._segment_path = lambda: "csbCallStatsInstanceTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable, [], name, value)


        class Csbcallstatsinstanceentry(Entity):
            """
            A conceptual row in csbCallStatsInstanceTable. There is an
            entry in this table for each SBC instance, as identified by a 
            value of csbCallStatsInstanceIndex.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	This object uniquely identifies the sequence number of an entity or slot that is configured per device. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsinstancephysicalindex
            
            	This object indicates the physical entity for which all the measurements are maintained. The exact type of this entity is described by its entPhysicalVendorType value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry, self).__init__()

                self.yang_name = "csbCallStatsInstanceEntry"
                self.yang_parent_name = "csbCallStatsInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.uint32, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsinstancephysicalindex', YLeaf(YType.int32, 'csbCallStatsInstancePhysicalIndex')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsinstancephysicalindex = None
                self._segment_path = lambda: "csbCallStatsInstanceEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCallStatsInstanceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry, ['csbcallstatsinstanceindex', 'csbcallstatsinstancephysicalindex'], name, value)


    class Csbcallstatstable(Entity):
        """
        This table describes the global statistics information in the
        form of a table which contains call specific information like
        call rates, media flows, signaling flows etc. The index of the
        table is service index which corresponds to a particular 
        service configured on the SBC and all the rows of the table
        represents the global information regarding all the call flows
        related to that particular service. The other index of this
        table is csbCallStatsInstanceIndex which is defined in
        csbCallStatsInstanceTable.
        
        .. attribute:: csbcallstatsentry
        
        	An conceptual row in the csbCallStatsGlobalStatsTable. There is an entry in this table for the particular service configured on SBC identified by a value of csbCallStatsInstanceIndex. The other index of this table is csbCallStatsInstanceIndex which is defined in csbCallStatsInstanceTable
        	**type**\: list of  		 :py:class:`Csbcallstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable, self).__init__()

            self.yang_name = "csbCallStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbCallStatsEntry", ("csbcallstatsentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry))])
            self._leafs = OrderedDict()

            self.csbcallstatsentry = YList(self)
            self._segment_path = lambda: "csbCallStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable, [], name, value)


        class Csbcallstatsentry(Entity):
            """
            An conceptual row in the csbCallStatsGlobalStatsTable. There is
            an entry in this table for the particular service configured on
            SBC identified by a value of csbCallStatsInstanceIndex. The
            other index of this table is csbCallStatsInstanceIndex which is
            defined in csbCallStatsInstanceTable.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	This object identifies the index of the name of the SBC service configured. This object also acts as an index for the table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatssbcname
            
            	This object indicates the configured name of the SBC service. The length of this object is zero when value is not assigned to it
            	**type**\: str
            
            .. attribute:: csbcallstatscallshigh
            
            	This object indicates the maximum number of calls per second processed by the Session Border Controller in past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatsrate1sec
            
            	This object indicates the average calls per second processed by the Session Border Controller
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatscallslow
            
            	This object indicates the minimum calls per second in past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatsavailableflows
            
            	This object indicates the number of media flows which are available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsusedflows
            
            	This object indicates the number of media flows which are used. This is for the flow allocated and connected. The flow allocated but not connected is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatspeakflows
            
            	This object indicates the number of peak flows in SBC. This is the highest recorded value for the active flows since the box was booted/reseted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatstotalflows
            
            	This object indicates the total number of media support by this instance of SBC. The total number of flows include the available flows and the active flows. This value is since box was booted/reseted. Total flows include the active flows and the flows allocated but not connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsusedsigflows
            
            	This object indicates the number of active signaling flows for signaling pinholes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            .. attribute:: csbcallstatspeaksigflows
            
            	This object indicates the peak signaling flow in SBC. This is the highest recorded value for the active signaling flows. This object is calculated using csbCallStatsUsedFlows
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            .. attribute:: csbcallstatstotalsigflows
            
            	This object indicates the maximum number of Signalling Flows that can be supported by this instance of SBC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            .. attribute:: csbcallstatsavailablepktrate
            
            	This object indicates the remaining capacity that can be supported by SBC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets per second
            
            .. attribute:: csbcallstatsunclassifiedpkts
            
            	This object indicates the number of unclassified packets processed by SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtppktssent
            
            	This object indicates the total number of RTP packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtppktsrcvd
            
            	This object indicates the total number of RTP packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtppktsdiscard
            
            	This object indicates the total number of RTP packets discarded
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtpoctetssent
            
            	This object indicates the number of RTP octets sent by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsrtpoctetsrcvd
            
            	This object indicates the number of RTP octets received by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsrtpoctetsdiscard
            
            	This object indicates the number of RTP octets discarded by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsnomediacount
            
            	This object indicates the accumulated No media event count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: no media events
            
            .. attribute:: csbcallstatsrouteerrors
            
            	This object indicates the accumulated route error event count. This counter is for the route error of media stream
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: route error events
            
            .. attribute:: csbcallstatsavailabletranscodeflows
            
            	This object indicates the number of additional transcoded flows that this media gateway manager (MGM) entity is currently able to configure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsactivetranscodeflows
            
            	This object indicates the current number of transcoded flows that are actively forwarding media traffic.  In this context, a flow is a media stream passing through the device. So a single voice call will be counted only once
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatspeaktranscodeflows
            
            	This object indicates the peak number of active transcoded flows since the statistics were last reset.  In this context, a flow is a media stream passing through the device, so a single voice call will be counted once
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatstotaltranscodeflows
            
            	This object indicates the accumulated total number of transcoded flows.  This count contains both active flows and flows that were allocated but never connected.  In this context, a flow is a media stream passing through the device, so a single voice call will be counted once
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry, self).__init__()

                self.yang_name = "csbCallStatsEntry"
                self.yang_parent_name = "csbCallStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.uint32, 'csbCallStatsServiceIndex')),
                    ('csbcallstatssbcname', YLeaf(YType.str, 'csbCallStatsSbcName')),
                    ('csbcallstatscallshigh', YLeaf(YType.uint32, 'csbCallStatsCallsHigh')),
                    ('csbcallstatsrate1sec', YLeaf(YType.uint32, 'csbCallStatsRate1Sec')),
                    ('csbcallstatscallslow', YLeaf(YType.uint32, 'csbCallStatsCallsLow')),
                    ('csbcallstatsavailableflows', YLeaf(YType.uint32, 'csbCallStatsAvailableFlows')),
                    ('csbcallstatsusedflows', YLeaf(YType.uint32, 'csbCallStatsUsedFlows')),
                    ('csbcallstatspeakflows', YLeaf(YType.uint32, 'csbCallStatsPeakFlows')),
                    ('csbcallstatstotalflows', YLeaf(YType.uint32, 'csbCallStatsTotalFlows')),
                    ('csbcallstatsusedsigflows', YLeaf(YType.uint32, 'csbCallStatsUsedSigFlows')),
                    ('csbcallstatspeaksigflows', YLeaf(YType.uint32, 'csbCallStatsPeakSigFlows')),
                    ('csbcallstatstotalsigflows', YLeaf(YType.uint32, 'csbCallStatsTotalSigFlows')),
                    ('csbcallstatsavailablepktrate', YLeaf(YType.uint32, 'csbCallStatsAvailablePktRate')),
                    ('csbcallstatsunclassifiedpkts', YLeaf(YType.uint64, 'csbCallStatsUnclassifiedPkts')),
                    ('csbcallstatsrtppktssent', YLeaf(YType.uint64, 'csbCallStatsRTPPktsSent')),
                    ('csbcallstatsrtppktsrcvd', YLeaf(YType.uint64, 'csbCallStatsRTPPktsRcvd')),
                    ('csbcallstatsrtppktsdiscard', YLeaf(YType.uint64, 'csbCallStatsRTPPktsDiscard')),
                    ('csbcallstatsrtpoctetssent', YLeaf(YType.uint64, 'csbCallStatsRTPOctetsSent')),
                    ('csbcallstatsrtpoctetsrcvd', YLeaf(YType.uint64, 'csbCallStatsRTPOctetsRcvd')),
                    ('csbcallstatsrtpoctetsdiscard', YLeaf(YType.uint64, 'csbCallStatsRTPOctetsDiscard')),
                    ('csbcallstatsnomediacount', YLeaf(YType.uint32, 'csbCallStatsNoMediaCount')),
                    ('csbcallstatsrouteerrors', YLeaf(YType.uint32, 'csbCallStatsRouteErrors')),
                    ('csbcallstatsavailabletranscodeflows', YLeaf(YType.uint32, 'csbCallStatsAvailableTranscodeFlows')),
                    ('csbcallstatsactivetranscodeflows', YLeaf(YType.uint32, 'csbCallStatsActiveTranscodeFlows')),
                    ('csbcallstatspeaktranscodeflows', YLeaf(YType.uint32, 'csbCallStatsPeakTranscodeFlows')),
                    ('csbcallstatstotaltranscodeflows', YLeaf(YType.uint32, 'csbCallStatsTotalTranscodeFlows')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbcallstatssbcname = None
                self.csbcallstatscallshigh = None
                self.csbcallstatsrate1sec = None
                self.csbcallstatscallslow = None
                self.csbcallstatsavailableflows = None
                self.csbcallstatsusedflows = None
                self.csbcallstatspeakflows = None
                self.csbcallstatstotalflows = None
                self.csbcallstatsusedsigflows = None
                self.csbcallstatspeaksigflows = None
                self.csbcallstatstotalsigflows = None
                self.csbcallstatsavailablepktrate = None
                self.csbcallstatsunclassifiedpkts = None
                self.csbcallstatsrtppktssent = None
                self.csbcallstatsrtppktsrcvd = None
                self.csbcallstatsrtppktsdiscard = None
                self.csbcallstatsrtpoctetssent = None
                self.csbcallstatsrtpoctetsrcvd = None
                self.csbcallstatsrtpoctetsdiscard = None
                self.csbcallstatsnomediacount = None
                self.csbcallstatsrouteerrors = None
                self.csbcallstatsavailabletranscodeflows = None
                self.csbcallstatsactivetranscodeflows = None
                self.csbcallstatspeaktranscodeflows = None
                self.csbcallstatstotaltranscodeflows = None
                self._segment_path = lambda: "csbCallStatsEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCallStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbcallstatssbcname', 'csbcallstatscallshigh', 'csbcallstatsrate1sec', 'csbcallstatscallslow', 'csbcallstatsavailableflows', 'csbcallstatsusedflows', 'csbcallstatspeakflows', 'csbcallstatstotalflows', 'csbcallstatsusedsigflows', 'csbcallstatspeaksigflows', 'csbcallstatstotalsigflows', 'csbcallstatsavailablepktrate', 'csbcallstatsunclassifiedpkts', 'csbcallstatsrtppktssent', 'csbcallstatsrtppktsrcvd', 'csbcallstatsrtppktsdiscard', 'csbcallstatsrtpoctetssent', 'csbcallstatsrtpoctetsrcvd', 'csbcallstatsrtpoctetsdiscard', 'csbcallstatsnomediacount', 'csbcallstatsrouteerrors', 'csbcallstatsavailabletranscodeflows', 'csbcallstatsactivetranscodeflows', 'csbcallstatspeaktranscodeflows', 'csbcallstatstotaltranscodeflows'], name, value)


    class Csbcurrperiodicstatstable(Entity):
        """
        This table is used to collect measurement over several
        different intervals as defined by the
        csbCurrPeriodicStatsInterval object. When a new interval starts
        the objects associated with the interval are reset and count up
        throughout the interval. The index of the table is the interval
        for which the stats information is to be displayed. The interval
        values can be 5 min, 15 mins, 1 hour and one day. The other
        indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        The gauge values are reported as \:\-
        1.If the period being queried is current5mins, this is the value
        at the instant that the query is issued. 
        2.Otherwise, for the other intevals, this is an average value
        during the summary period sampled at 5 minute intervals.
        
        .. attribute:: csbcurrperiodicstatsentry
        
        	An conceptual row in the csbCurrPeriodicStatsTable. There is an entry in this table for the particular controller by a value of csbH248StatsCtrlrIndex. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbcurrperiodicstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable, self).__init__()

            self.yang_name = "csbCurrPeriodicStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbCurrPeriodicStatsEntry", ("csbcurrperiodicstatsentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry))])
            self._leafs = OrderedDict()

            self.csbcurrperiodicstatsentry = YList(self)
            self._segment_path = lambda: "csbCurrPeriodicStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable, [], name, value)


        class Csbcurrperiodicstatsentry(Entity):
            """
            An conceptual row in the csbCurrPeriodicStatsTable. There is
            an entry in this table for the particular controller by a value
            of csbH248StatsCtrlrIndex. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbcurrperiodicstatsinterval  (key)
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts as index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbcurrperiodicstatsactivecalls
            
            	This object indicates the number of calls that have become active during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactivatingcalls
            
            	This object indicates the number of calls that have become activing during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdeactivatingcalls
            
            	This object indicates the number of calls that have become deactiving during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstotalcallattempts
            
            	This object indicates the number of total call attempts during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatsfailedcallattempts
            
            	This object indicates the number of failed call attempts during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallroutingfailure
            
            	This object indicates the number of call setup failures due to routing failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallresourcefailure
            
            	This object indicates the number of call setup failures due to resource failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallmediafailure
            
            	This object indicates the number of call setup failures due to media failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsigfailure
            
            	This object indicates the number of call setup failures due to signaling failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatsactivecallfailure
            
            	This object indicates the number of active call failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscongestionfailure
            
            	This object indicates the number of call setup failures due to congestion during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetuppolicyfailure
            
            	This object indicates the number of call setup failures due to policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupnapolicyfailure
            
            	This object indicates the number of call setup failures due to NA policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetuproutingpolicyfailure
            
            	This object indicates the number of call setup failures due to routing policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacpolicyfailure
            
            	This object indicates the number of call setup failures due to CAC policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcaccalllimitfailure
            
            	This object indicates the number of call setup failures due to CAC call limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacratelimitfailure
            
            	This object indicates the number of call setup failures due to CAC call rate limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacbandwidthfailure
            
            	This object indicates the number of call setup failures due to CAC bandwidth limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacmedialimitfailure
            
            	This object indicates the number of call setup failures due to CAC media limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacmediaupdatefailure
            
            	This object indicates the number of call update failure due to policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatstimestamp
            
            	This object indicates the current time at the start of each interval
            	**type**\: str
            
            	**length:** 0..80
            
            .. attribute:: csbcurrperiodicstatstranscodedcalls
            
            	The object indicates the number of transcoded calls that are active during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstransratedcalls
            
            	The object indicates the number of transrated calls that are active during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstotalcallupdatefailure
            
            	This object indicates the total number of call update failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactiveipv6calls
            
            	This Object indicates the number of calls through SBC that use IPv6 signaling.  This statistic totals all calls that traverse an IPv6 adjacency on either or both sides of SBC during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactiveemergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactivee2emergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) and have used the e2 interface to obtain location information for the caller during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsimsrxactivecalls
            
            	This object indicates the total number of active calls which use IMS Rx, during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsimsrxcallsetupfaiures
            
            	This object indicates the total call Setup failures owing to IMS Rx failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatsimsrxcallrenegotiationattempts
            
            	This object indicates the total call renegotiation attempts using IMS Rx during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbcurrperiodicstatsimsrxcallrenegotiationfailures
            
            	This object indicates the total call renegotiation failures owing to IMS Rx failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatsaudiotranscodedcalls
            
            	The number of active audio transcoded calls through this adjacency or account during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsfaxtranscodedcalls
            
            	This object indicates the the number of active fax transcoded calls through this adjacency or account during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to RTP being proposed when not permitted during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatssrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to SRTP being proposed when not permitted during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatsnonsrtpcalls
            
            	This object indicates the number of active calls through this adjacency or account which do not use SRTP on any media channels during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatssrtpnoniwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels which use SRTP. This count does not include media  channels that provide interworking between RTP and SRTP during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatssrtpiwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that provide interworking between RTP and SRTP during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiw2833calls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via RFC 2833 during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiwinbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via  inband DTMF tones during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiw2833inbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in media via RFC 2833 and DTMF in media via inband DTMF tones during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstotaltapsrequested
            
            	This object indicates the lawful intercept tap attempts requested within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbcurrperiodicstatstotaltapssucceeded
            
            	This object indicates the lawful intercept tap attempts that have been successfully implemented within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: success
            
            .. attribute:: csbcurrperiodicstatscurrenttaps
            
            	This object indicates the Lawful intercept taps currently in place on calls within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: taps
            
            .. attribute:: csbcurrperiodicipseccalls
            
            	The number of active calls on this adjacency or account which are to or from registered subscribers using IPSEC during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry, self).__init__()

                self.yang_name = "csbCurrPeriodicStatsEntry"
                self.yang_parent_name = "csbCurrPeriodicStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex','csbcurrperiodicstatsinterval']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.str, 'csbCallStatsServiceIndex')),
                    ('csbcurrperiodicstatsinterval', YLeaf(YType.enumeration, 'csbCurrPeriodicStatsInterval')),
                    ('csbcurrperiodicstatsactivecalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActiveCalls')),
                    ('csbcurrperiodicstatsactivatingcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActivatingCalls')),
                    ('csbcurrperiodicstatsdeactivatingcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsDeactivatingCalls')),
                    ('csbcurrperiodicstatstotalcallattempts', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTotalCallAttempts')),
                    ('csbcurrperiodicstatsfailedcallattempts', YLeaf(YType.uint32, 'csbCurrPeriodicStatsFailedCallAttempts')),
                    ('csbcurrperiodicstatscallroutingfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallRoutingFailure')),
                    ('csbcurrperiodicstatscallresourcefailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallResourceFailure')),
                    ('csbcurrperiodicstatscallmediafailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallMediaFailure')),
                    ('csbcurrperiodicstatscallsigfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSigFailure')),
                    ('csbcurrperiodicstatsactivecallfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActiveCallFailure')),
                    ('csbcurrperiodicstatscongestionfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCongestionFailure')),
                    ('csbcurrperiodicstatscallsetuppolicyfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupPolicyFailure')),
                    ('csbcurrperiodicstatscallsetupnapolicyfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupNAPolicyFailure')),
                    ('csbcurrperiodicstatscallsetuproutingpolicyfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupRoutingPolicyFailure')),
                    ('csbcurrperiodicstatscallsetupcacpolicyfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACPolicyFailure')),
                    ('csbcurrperiodicstatscallsetupcaccalllimitfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACCallLimitFailure')),
                    ('csbcurrperiodicstatscallsetupcacratelimitfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACRateLimitFailure')),
                    ('csbcurrperiodicstatscallsetupcacbandwidthfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACBandwidthFailure')),
                    ('csbcurrperiodicstatscallsetupcacmedialimitfailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACMediaLimitFailure')),
                    ('csbcurrperiodicstatscallsetupcacmediaupdatefailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure')),
                    ('csbcurrperiodicstatstimestamp', YLeaf(YType.str, 'csbCurrPeriodicStatsTimestamp')),
                    ('csbcurrperiodicstatstranscodedcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTranscodedCalls')),
                    ('csbcurrperiodicstatstransratedcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTransratedCalls')),
                    ('csbcurrperiodicstatstotalcallupdatefailure', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTotalCallUpdateFailure')),
                    ('csbcurrperiodicstatsactiveipv6calls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActiveIpv6Calls')),
                    ('csbcurrperiodicstatsactiveemergencycalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActiveEmergencyCalls')),
                    ('csbcurrperiodicstatsactivee2emergencycalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsActiveE2EmergencyCalls')),
                    ('csbcurrperiodicstatsimsrxactivecalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsImsRxActiveCalls')),
                    ('csbcurrperiodicstatsimsrxcallsetupfaiures', YLeaf(YType.uint32, 'csbCurrPeriodicStatsImsRxCallSetupFaiures')),
                    ('csbcurrperiodicstatsimsrxcallrenegotiationattempts', YLeaf(YType.uint32, 'csbCurrPeriodicStatsImsRxCallRenegotiationAttempts')),
                    ('csbcurrperiodicstatsimsrxcallrenegotiationfailures', YLeaf(YType.uint32, 'csbCurrPeriodicStatsImsRxCallRenegotiationFailures')),
                    ('csbcurrperiodicstatsaudiotranscodedcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsAudioTranscodedCalls')),
                    ('csbcurrperiodicstatsfaxtranscodedcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsFaxTranscodedCalls')),
                    ('csbcurrperiodicstatsrtpdisallowedfailures', YLeaf(YType.uint32, 'csbCurrPeriodicStatsRtpDisallowedFailures')),
                    ('csbcurrperiodicstatssrtpdisallowedfailures', YLeaf(YType.uint32, 'csbCurrPeriodicStatsSrtpDisallowedFailures')),
                    ('csbcurrperiodicstatsnonsrtpcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsNonSrtpCalls')),
                    ('csbcurrperiodicstatssrtpnoniwcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsSrtpNonIwCalls')),
                    ('csbcurrperiodicstatssrtpiwcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsSrtpIwCalls')),
                    ('csbcurrperiodicstatsdtmfiw2833calls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsDtmfIw2833Calls')),
                    ('csbcurrperiodicstatsdtmfiwinbandcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsDtmfIwInbandCalls')),
                    ('csbcurrperiodicstatsdtmfiw2833inbandcalls', YLeaf(YType.uint32, 'csbCurrPeriodicStatsDtmfIw2833InbandCalls')),
                    ('csbcurrperiodicstatstotaltapsrequested', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTotalTapsRequested')),
                    ('csbcurrperiodicstatstotaltapssucceeded', YLeaf(YType.uint32, 'csbCurrPeriodicStatsTotalTapsSucceeded')),
                    ('csbcurrperiodicstatscurrenttaps', YLeaf(YType.uint32, 'csbCurrPeriodicStatsCurrentTaps')),
                    ('csbcurrperiodicipseccalls', YLeaf(YType.uint32, 'csbCurrPeriodicIpsecCalls')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbcurrperiodicstatsinterval = None
                self.csbcurrperiodicstatsactivecalls = None
                self.csbcurrperiodicstatsactivatingcalls = None
                self.csbcurrperiodicstatsdeactivatingcalls = None
                self.csbcurrperiodicstatstotalcallattempts = None
                self.csbcurrperiodicstatsfailedcallattempts = None
                self.csbcurrperiodicstatscallroutingfailure = None
                self.csbcurrperiodicstatscallresourcefailure = None
                self.csbcurrperiodicstatscallmediafailure = None
                self.csbcurrperiodicstatscallsigfailure = None
                self.csbcurrperiodicstatsactivecallfailure = None
                self.csbcurrperiodicstatscongestionfailure = None
                self.csbcurrperiodicstatscallsetuppolicyfailure = None
                self.csbcurrperiodicstatscallsetupnapolicyfailure = None
                self.csbcurrperiodicstatscallsetuproutingpolicyfailure = None
                self.csbcurrperiodicstatscallsetupcacpolicyfailure = None
                self.csbcurrperiodicstatscallsetupcaccalllimitfailure = None
                self.csbcurrperiodicstatscallsetupcacratelimitfailure = None
                self.csbcurrperiodicstatscallsetupcacbandwidthfailure = None
                self.csbcurrperiodicstatscallsetupcacmedialimitfailure = None
                self.csbcurrperiodicstatscallsetupcacmediaupdatefailure = None
                self.csbcurrperiodicstatstimestamp = None
                self.csbcurrperiodicstatstranscodedcalls = None
                self.csbcurrperiodicstatstransratedcalls = None
                self.csbcurrperiodicstatstotalcallupdatefailure = None
                self.csbcurrperiodicstatsactiveipv6calls = None
                self.csbcurrperiodicstatsactiveemergencycalls = None
                self.csbcurrperiodicstatsactivee2emergencycalls = None
                self.csbcurrperiodicstatsimsrxactivecalls = None
                self.csbcurrperiodicstatsimsrxcallsetupfaiures = None
                self.csbcurrperiodicstatsimsrxcallrenegotiationattempts = None
                self.csbcurrperiodicstatsimsrxcallrenegotiationfailures = None
                self.csbcurrperiodicstatsaudiotranscodedcalls = None
                self.csbcurrperiodicstatsfaxtranscodedcalls = None
                self.csbcurrperiodicstatsrtpdisallowedfailures = None
                self.csbcurrperiodicstatssrtpdisallowedfailures = None
                self.csbcurrperiodicstatsnonsrtpcalls = None
                self.csbcurrperiodicstatssrtpnoniwcalls = None
                self.csbcurrperiodicstatssrtpiwcalls = None
                self.csbcurrperiodicstatsdtmfiw2833calls = None
                self.csbcurrperiodicstatsdtmfiwinbandcalls = None
                self.csbcurrperiodicstatsdtmfiw2833inbandcalls = None
                self.csbcurrperiodicstatstotaltapsrequested = None
                self.csbcurrperiodicstatstotaltapssucceeded = None
                self.csbcurrperiodicstatscurrenttaps = None
                self.csbcurrperiodicipseccalls = None
                self._segment_path = lambda: "csbCurrPeriodicStatsEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']" + "[csbCurrPeriodicStatsInterval='" + str(self.csbcurrperiodicstatsinterval) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCurrPeriodicStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbcurrperiodicstatsinterval', 'csbcurrperiodicstatsactivecalls', 'csbcurrperiodicstatsactivatingcalls', 'csbcurrperiodicstatsdeactivatingcalls', 'csbcurrperiodicstatstotalcallattempts', 'csbcurrperiodicstatsfailedcallattempts', 'csbcurrperiodicstatscallroutingfailure', 'csbcurrperiodicstatscallresourcefailure', 'csbcurrperiodicstatscallmediafailure', 'csbcurrperiodicstatscallsigfailure', 'csbcurrperiodicstatsactivecallfailure', 'csbcurrperiodicstatscongestionfailure', 'csbcurrperiodicstatscallsetuppolicyfailure', 'csbcurrperiodicstatscallsetupnapolicyfailure', 'csbcurrperiodicstatscallsetuproutingpolicyfailure', 'csbcurrperiodicstatscallsetupcacpolicyfailure', 'csbcurrperiodicstatscallsetupcaccalllimitfailure', 'csbcurrperiodicstatscallsetupcacratelimitfailure', 'csbcurrperiodicstatscallsetupcacbandwidthfailure', 'csbcurrperiodicstatscallsetupcacmedialimitfailure', 'csbcurrperiodicstatscallsetupcacmediaupdatefailure', 'csbcurrperiodicstatstimestamp', 'csbcurrperiodicstatstranscodedcalls', 'csbcurrperiodicstatstransratedcalls', 'csbcurrperiodicstatstotalcallupdatefailure', 'csbcurrperiodicstatsactiveipv6calls', 'csbcurrperiodicstatsactiveemergencycalls', 'csbcurrperiodicstatsactivee2emergencycalls', 'csbcurrperiodicstatsimsrxactivecalls', 'csbcurrperiodicstatsimsrxcallsetupfaiures', 'csbcurrperiodicstatsimsrxcallrenegotiationattempts', 'csbcurrperiodicstatsimsrxcallrenegotiationfailures', 'csbcurrperiodicstatsaudiotranscodedcalls', 'csbcurrperiodicstatsfaxtranscodedcalls', 'csbcurrperiodicstatsrtpdisallowedfailures', 'csbcurrperiodicstatssrtpdisallowedfailures', 'csbcurrperiodicstatsnonsrtpcalls', 'csbcurrperiodicstatssrtpnoniwcalls', 'csbcurrperiodicstatssrtpiwcalls', 'csbcurrperiodicstatsdtmfiw2833calls', 'csbcurrperiodicstatsdtmfiwinbandcalls', 'csbcurrperiodicstatsdtmfiw2833inbandcalls', 'csbcurrperiodicstatstotaltapsrequested', 'csbcurrperiodicstatstotaltapssucceeded', 'csbcurrperiodicstatscurrenttaps', 'csbcurrperiodicipseccalls'], name, value)


    class Csbhistorystatstable(Entity):
        """
        This table provide historical measurement in various interval
        length defined by the csbHistoryStatsInterval object. Each
        interval may contain one or more entries to allow for detailed
        measurment to be collected. It is up to the platform to
        determine the number of intervals to be supported like 
        5 minutes, 15 minutes, 1 hour and 1 day. In addition, the number
        of
        historical entries is also determined by the platform
        resources.
        
        The gauge values are reported as\:
        If the period being queried is previous5mins, this is the number
        of calls that were active at the end of the previous 5 minute
        period. Otherwise for the other intevals, this is an average
        value during the summary period, sampled at 5 minute intervals.
        
        .. attribute:: csbhistorystatsentry
        
        	A conceptual row in the csbHistoryStatsTable. The entries in this table are updated as interval completes in the csbCurrPeriodicStatsTable table and the data is moved from that table to this one
        	**type**\: list of  		 :py:class:`Csbhistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable.Csbhistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable, self).__init__()

            self.yang_name = "csbHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbHistoryStatsEntry", ("csbhistorystatsentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable.Csbhistorystatsentry))])
            self._leafs = OrderedDict()

            self.csbhistorystatsentry = YList(self)
            self._segment_path = lambda: "csbHistoryStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable, [], name, value)


        class Csbhistorystatsentry(Entity):
            """
            A conceptual row in the csbHistoryStatsTable. The entries in
            this table are updated as interval completes in the
            csbCurrPeriodicStatsTable table and the data is moved from that
            table to this one.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbhistorystatsinterval  (key)
            
            	This object identifies the interval for which the history statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 day. This object acts as index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbhistorystatselements  (key)
            
            	The platform assigns a number starting with one and increments it each for each new row. When the maximum          number of row is reached the oldest rows are deleted. It is up to the platform to determine the number of entries for each interval. It is recommended that each platform support at least one entry for 5 min, 15 mins, 1 hour and 1 day intervals
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsactivecalls
            
            	This object indicates the number of active calls history during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatstotalcallattempts
            
            	This object indicates the number of total call attempts history during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsfailedcallattempts
            
            	This object indicates the number of failed call attempts during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallroutingfailure
            
            	This object indicates the number of call setup failures due to routing failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallresourcefailure
            
            	This object indicates the number of call setup failures due to resource failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallmediafailure
            
            	This object indicates the number of call setup failures due to media failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsfailsigfailure
            
            	This object indicates the number of call setup failures due to signaling failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsactivecallfailure
            
            	This object indicates the number of active call failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscongestionfailure
            
            	This object indicates the number of call setup failures due to congestion during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetuppolicyfailure
            
            	This object indicates the number of call setup failures due to some policy violations during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupnapolicyfailure
            
            	This object indicates the number of call setup failures due to NA policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetuproutingpolicyfailure
            
            	This object indicates the number of call setup failures due to routing policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacpolicyfailure
            
            	This object indicates the number of call setup failures due to CAC policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcaccalllimitfailure
            
            	This object indicates the number of call setup failures due to CAC call limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacratelimitfailure
            
            	This object indicates the number of call setup failures due to CAC call rate limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacbandwidthfailure
            
            	This object indicates the number of call setup failures due to CAC bandwidth limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacmedialimitfailure
            
            	This object indicates the number of call setup failures due to CAC media limit during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacmediaupdatefailure
            
            	This object indicates the number of call update failure due to policy failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatstimestamp
            
            	This object indicates the time at the start of the interval when measurements were first collected for this interval in the csbCurrPeriodicStatsTable
            	**type**\: str
            
            	**length:** 0..80
            
            .. attribute:: csbhistroystatstranscodedcalls
            
            	The object indicates the number of active transcoded calls during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistroystatstransratedcalls
            
            	The object indicates the number of active transrated calls during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatstotalcallupdatefailure
            
            	This object indicates the total call update failures during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactiveipv6calls
            
            	This Object indicates the number of calls through SBC that use IPv6 signaling.  This statistic totals all calls that traverse an IPv6 adjacency on either or both sides of SBC during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactiveemergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis)  during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactivee2emergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) and have used the e2 interface to obtain location information for the caller
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsimsrxactivecalls
            
            	This object indicates the total number of active calls which use IMS Rx, during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsimsrxcallsetupfailures
            
            	This object indicates the total call setup failures owing to IMS Rx failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatsimsrxcallrenegotiationattempts
            
            	This object indicates the total call renegotiation attempts using IMS Rx during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbhistorystatsimsrxcallrenegotiationfailures
            
            	This object indicates the total call renegotiation failures owing to IMS Rx failure during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatsaudiotranscodedcalls
            
            	The number of active audio transcoded calls through this adjacency or account during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsfaxtranscodedcalls
            
            	This object indicates the the number of active fax transcoded calls through this adjacency or account during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to RTP being proposed when not permitted during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatssrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to SRTP being proposed when not permitted during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatsnonsrtpcalls
            
            	This object indicates the number of active calls through this adjacency or account which do not use SRTP on any media channels during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatssrtpnoniwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that use SRTP but no media channels that provide interworking between RTP and SRTP during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatssrtpiwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that provide interworking between RTP and SRTP during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsdtmfiw2833calls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via RFC 2833 during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsdtmfiwinbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via inband DTMF tones during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsdtmfiw2833inbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in media via RFC 2833 and DTMF in media via inband DTMF tones during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatstotaltapsrequested
            
            	This object indicates the lawful intercept tap attempts requested within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbhistorystatstotaltapssucceeded
            
            	This object indicates the lawful intercept tap attempts that have been successfully implemented within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: success
            
            .. attribute:: csbhistorystatscurrenttaps
            
            	This object indicates the Lawful intercept taps currently in place on calls within the scope of this query during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: taps
            
            .. attribute:: csbhistorystatsipseccalls
            
            	The number of active calls on this adjacency or account which are to or from registered subscribers using IPSEC during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable.Csbhistorystatsentry, self).__init__()

                self.yang_name = "csbHistoryStatsEntry"
                self.yang_parent_name = "csbHistoryStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex','csbhistorystatsinterval','csbhistorystatselements']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.str, 'csbCallStatsServiceIndex')),
                    ('csbhistorystatsinterval', YLeaf(YType.enumeration, 'csbHistoryStatsInterval')),
                    ('csbhistorystatselements', YLeaf(YType.uint32, 'csbHistoryStatsElements')),
                    ('csbhistorystatsactivecalls', YLeaf(YType.uint32, 'csbHistoryStatsActiveCalls')),
                    ('csbhistorystatstotalcallattempts', YLeaf(YType.uint32, 'csbHistoryStatsTotalCallAttempts')),
                    ('csbhistorystatsfailedcallattempts', YLeaf(YType.uint32, 'csbHistoryStatsFailedCallAttempts')),
                    ('csbhistorystatscallroutingfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallRoutingFailure')),
                    ('csbhistorystatscallresourcefailure', YLeaf(YType.uint32, 'csbHistoryStatsCallResourceFailure')),
                    ('csbhistorystatscallmediafailure', YLeaf(YType.uint32, 'csbHistoryStatsCallMediaFailure')),
                    ('csbhistorystatsfailsigfailure', YLeaf(YType.uint32, 'csbHistoryStatsFailSigFailure')),
                    ('csbhistorystatsactivecallfailure', YLeaf(YType.uint32, 'csbHistoryStatsActiveCallFailure')),
                    ('csbhistorystatscongestionfailure', YLeaf(YType.uint32, 'csbHistoryStatsCongestionFailure')),
                    ('csbhistorystatscallsetuppolicyfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupPolicyFailure')),
                    ('csbhistorystatscallsetupnapolicyfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupNAPolicyFailure')),
                    ('csbhistorystatscallsetuproutingpolicyfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupRoutingPolicyFailure')),
                    ('csbhistorystatscallsetupcacpolicyfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACPolicyFailure')),
                    ('csbhistorystatscallsetupcaccalllimitfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACCallLimitFailure')),
                    ('csbhistorystatscallsetupcacratelimitfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACRateLimitFailure')),
                    ('csbhistorystatscallsetupcacbandwidthfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACBandwidthFailure')),
                    ('csbhistorystatscallsetupcacmedialimitfailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACMediaLimitFailure')),
                    ('csbhistorystatscallsetupcacmediaupdatefailure', YLeaf(YType.uint32, 'csbHistoryStatsCallSetupCACMediaUpdateFailure')),
                    ('csbhistorystatstimestamp', YLeaf(YType.str, 'csbHistoryStatsTimestamp')),
                    ('csbhistroystatstranscodedcalls', YLeaf(YType.uint32, 'csbHistroyStatsTranscodedCalls')),
                    ('csbhistroystatstransratedcalls', YLeaf(YType.uint32, 'csbHistroyStatsTransratedCalls')),
                    ('csbhistorystatstotalcallupdatefailure', YLeaf(YType.uint32, 'csbHistoryStatsTotalCallUpdateFailure')),
                    ('csbhistorystatsactiveipv6calls', YLeaf(YType.uint32, 'csbHistoryStatsActiveIpv6Calls')),
                    ('csbhistorystatsactiveemergencycalls', YLeaf(YType.uint32, 'csbHistoryStatsActiveEmergencyCalls')),
                    ('csbhistorystatsactivee2emergencycalls', YLeaf(YType.uint32, 'csbHistoryStatsActiveE2EmergencyCalls')),
                    ('csbhistorystatsimsrxactivecalls', YLeaf(YType.uint32, 'csbHistoryStatsImsRxActiveCalls')),
                    ('csbhistorystatsimsrxcallsetupfailures', YLeaf(YType.uint32, 'csbHistoryStatsImsRxCallSetupFailures')),
                    ('csbhistorystatsimsrxcallrenegotiationattempts', YLeaf(YType.uint32, 'csbHistoryStatsImsRxCallRenegotiationAttempts')),
                    ('csbhistorystatsimsrxcallrenegotiationfailures', YLeaf(YType.uint32, 'csbHistoryStatsImsRxCallRenegotiationFailures')),
                    ('csbhistorystatsaudiotranscodedcalls', YLeaf(YType.uint32, 'csbHistoryStatsAudioTranscodedCalls')),
                    ('csbhistorystatsfaxtranscodedcalls', YLeaf(YType.uint32, 'csbHistoryStatsFaxTranscodedCalls')),
                    ('csbhistorystatsrtpdisallowedfailures', YLeaf(YType.uint32, 'csbHistoryStatsRtpDisallowedFailures')),
                    ('csbhistorystatssrtpdisallowedfailures', YLeaf(YType.uint32, 'csbHistoryStatsSrtpDisallowedFailures')),
                    ('csbhistorystatsnonsrtpcalls', YLeaf(YType.uint32, 'csbHistoryStatsNonSrtpCalls')),
                    ('csbhistorystatssrtpnoniwcalls', YLeaf(YType.uint32, 'csbHistoryStatsSrtpNonIwCalls')),
                    ('csbhistorystatssrtpiwcalls', YLeaf(YType.uint32, 'csbHistoryStatsSrtpIwCalls')),
                    ('csbhistorystatsdtmfiw2833calls', YLeaf(YType.uint32, 'csbHistoryStatsDtmfIw2833Calls')),
                    ('csbhistorystatsdtmfiwinbandcalls', YLeaf(YType.uint32, 'csbHistoryStatsDtmfIwInbandCalls')),
                    ('csbhistorystatsdtmfiw2833inbandcalls', YLeaf(YType.uint32, 'csbHistoryStatsDtmfIw2833InbandCalls')),
                    ('csbhistorystatstotaltapsrequested', YLeaf(YType.uint32, 'csbHistoryStatsTotalTapsRequested')),
                    ('csbhistorystatstotaltapssucceeded', YLeaf(YType.uint32, 'csbHistoryStatsTotalTapsSucceeded')),
                    ('csbhistorystatscurrenttaps', YLeaf(YType.uint32, 'csbHistoryStatsCurrentTaps')),
                    ('csbhistorystatsipseccalls', YLeaf(YType.uint32, 'csbHistoryStatsIpsecCalls')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbhistorystatsinterval = None
                self.csbhistorystatselements = None
                self.csbhistorystatsactivecalls = None
                self.csbhistorystatstotalcallattempts = None
                self.csbhistorystatsfailedcallattempts = None
                self.csbhistorystatscallroutingfailure = None
                self.csbhistorystatscallresourcefailure = None
                self.csbhistorystatscallmediafailure = None
                self.csbhistorystatsfailsigfailure = None
                self.csbhistorystatsactivecallfailure = None
                self.csbhistorystatscongestionfailure = None
                self.csbhistorystatscallsetuppolicyfailure = None
                self.csbhistorystatscallsetupnapolicyfailure = None
                self.csbhistorystatscallsetuproutingpolicyfailure = None
                self.csbhistorystatscallsetupcacpolicyfailure = None
                self.csbhistorystatscallsetupcaccalllimitfailure = None
                self.csbhistorystatscallsetupcacratelimitfailure = None
                self.csbhistorystatscallsetupcacbandwidthfailure = None
                self.csbhistorystatscallsetupcacmedialimitfailure = None
                self.csbhistorystatscallsetupcacmediaupdatefailure = None
                self.csbhistorystatstimestamp = None
                self.csbhistroystatstranscodedcalls = None
                self.csbhistroystatstransratedcalls = None
                self.csbhistorystatstotalcallupdatefailure = None
                self.csbhistorystatsactiveipv6calls = None
                self.csbhistorystatsactiveemergencycalls = None
                self.csbhistorystatsactivee2emergencycalls = None
                self.csbhistorystatsimsrxactivecalls = None
                self.csbhistorystatsimsrxcallsetupfailures = None
                self.csbhistorystatsimsrxcallrenegotiationattempts = None
                self.csbhistorystatsimsrxcallrenegotiationfailures = None
                self.csbhistorystatsaudiotranscodedcalls = None
                self.csbhistorystatsfaxtranscodedcalls = None
                self.csbhistorystatsrtpdisallowedfailures = None
                self.csbhistorystatssrtpdisallowedfailures = None
                self.csbhistorystatsnonsrtpcalls = None
                self.csbhistorystatssrtpnoniwcalls = None
                self.csbhistorystatssrtpiwcalls = None
                self.csbhistorystatsdtmfiw2833calls = None
                self.csbhistorystatsdtmfiwinbandcalls = None
                self.csbhistorystatsdtmfiw2833inbandcalls = None
                self.csbhistorystatstotaltapsrequested = None
                self.csbhistorystatstotaltapssucceeded = None
                self.csbhistorystatscurrenttaps = None
                self.csbhistorystatsipseccalls = None
                self._segment_path = lambda: "csbHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']" + "[csbHistoryStatsInterval='" + str(self.csbhistorystatsinterval) + "']" + "[csbHistoryStatsElements='" + str(self.csbhistorystatselements) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbHistoryStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbhistorystatstable.Csbhistorystatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbhistorystatsinterval', 'csbhistorystatselements', 'csbhistorystatsactivecalls', 'csbhistorystatstotalcallattempts', 'csbhistorystatsfailedcallattempts', 'csbhistorystatscallroutingfailure', 'csbhistorystatscallresourcefailure', 'csbhistorystatscallmediafailure', 'csbhistorystatsfailsigfailure', 'csbhistorystatsactivecallfailure', 'csbhistorystatscongestionfailure', 'csbhistorystatscallsetuppolicyfailure', 'csbhistorystatscallsetupnapolicyfailure', 'csbhistorystatscallsetuproutingpolicyfailure', 'csbhistorystatscallsetupcacpolicyfailure', 'csbhistorystatscallsetupcaccalllimitfailure', 'csbhistorystatscallsetupcacratelimitfailure', 'csbhistorystatscallsetupcacbandwidthfailure', 'csbhistorystatscallsetupcacmedialimitfailure', 'csbhistorystatscallsetupcacmediaupdatefailure', 'csbhistorystatstimestamp', 'csbhistroystatstranscodedcalls', 'csbhistroystatstransratedcalls', 'csbhistorystatstotalcallupdatefailure', 'csbhistorystatsactiveipv6calls', 'csbhistorystatsactiveemergencycalls', 'csbhistorystatsactivee2emergencycalls', 'csbhistorystatsimsrxactivecalls', 'csbhistorystatsimsrxcallsetupfailures', 'csbhistorystatsimsrxcallrenegotiationattempts', 'csbhistorystatsimsrxcallrenegotiationfailures', 'csbhistorystatsaudiotranscodedcalls', 'csbhistorystatsfaxtranscodedcalls', 'csbhistorystatsrtpdisallowedfailures', 'csbhistorystatssrtpdisallowedfailures', 'csbhistorystatsnonsrtpcalls', 'csbhistorystatssrtpnoniwcalls', 'csbhistorystatssrtpiwcalls', 'csbhistorystatsdtmfiw2833calls', 'csbhistorystatsdtmfiwinbandcalls', 'csbhistorystatsdtmfiw2833inbandcalls', 'csbhistorystatstotaltapsrequested', 'csbhistorystatstotaltapssucceeded', 'csbhistorystatscurrenttaps', 'csbhistorystatsipseccalls'], name, value)


    class Csbperflowstatstable(Entity):
        """
        This table describes statistics table for each call flow. The
        indices of the table are virtual media gateway id, gate id,
        falow pair id and side id (indices for side A or side B). The
        other indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        .. attribute:: csbperflowstatsentry
        
        	An conceptual row in the csbPerFlowStatsTable. There is an entry in this table for vdbe Id, gate id, flow pair id and side id. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbperflowstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable, self).__init__()

            self.yang_name = "csbPerFlowStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbPerFlowStatsEntry", ("csbperflowstatsentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry))])
            self._leafs = OrderedDict()

            self.csbperflowstatsentry = YList(self)
            self._segment_path = lambda: "csbPerFlowStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable, [], name, value)


        class Csbperflowstatsentry(Entity):
            """
            An conceptual row in the csbPerFlowStatsTable. There is
            an entry in this table for vdbe Id, gate id, flow pair id and
            side id. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbperflowstatsvdbeid  (key)
            
            	This object identifies the virtual media gateway id. This object also acts as an index for the table
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: csbperflowstatsgateid  (key)
            
            	This object identifies the gate id. This object also acts as an index for the table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: csbperflowstatsflowpairid  (key)
            
            	This object identifies the flow pair id. This object also acts as an index for the table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: csbperflowstatssideid  (key)
            
            	This object identifies the index corresponding to side of flow pair either side A or side B. This object also acts as an index for the table
            	**type**\:  :py:class:`Csbperflowstatssideid <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry.Csbperflowstatssideid>`
            
            .. attribute:: csbperflowstatsflowtype
            
            	This object indicates the type of the flow, like media flow, signaling flow etc
            	**type**\:  :py:class:`Csbperflowstatsflowtype <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry.Csbperflowstatsflowtype>`
            
            .. attribute:: csbperflowstatsrtppktssent
            
            	This object indicates the number of RTP packets sent per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtppktsrcvd
            
            	This object indicates the number of RTP packets received per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtppktsdiscard
            
            	This object indicates the number of RTP packets discarded  per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtpoctetssent
            
            	This object indicates the number of RTP octets sent per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtpoctetsrcvd
            
            	This object indicates the number of RTP octets received per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtpoctetsdiscard
            
            	This object indicates the number of RTP octets discarded per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtcppktssent
            
            	The number of RTP packets sent by the remote end point to this MG on this flow. Comparing this with the local number of RTP packets received from the remote end point gives an indication of how many incoming  packets were dropped on this leg of the call. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtcppktsrcvd
            
            	The number of RTP packets received by the remote end point from this MG on this flow. Comparing this with the local number of RTP packets sent from this MG to the remote endpoint gives an indication of how many outgoing packets were dropped on this leg of the call. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtcppktslost
            
            	The number of RTP packets reported as lost by the remote end point on this flow. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsepjitter
            
            	This object indicates the End Point jitter per flow in the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: milliseconds
            
            .. attribute:: csbperflowstatstmanpermbs
            
            	This object indicates the maximum burst size for the current FlowPair
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: csbperflowstatstmanpersdr
            
            	This object indicates the bandwidth reserved for flow in kilobytes/second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobytes per second
            
            .. attribute:: csbperflowstatsdscpsettings
            
            	This object indicates the mark packets sent for the current FlowPair with, or zero if none set. The DSCP is a 6\-bit value, which will be present in the top 6 bits of the lowest byte of this field
            	**type**\: str
            
            .. attribute:: csbperflowstatsadrstatus
            
            	This object indicates whether the flow on the current FlowPair has subscribed for the NAT latch event
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: csbperflowstatsqasettings
            
            	This object indicates the flow on the current FlowPair has subscribed for the media loss event
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: csbperflowstatsrtppktslost
            
            	This object indicates the number of RTP packets lost per flow by the SBC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry, self).__init__()

                self.yang_name = "csbPerFlowStatsEntry"
                self.yang_parent_name = "csbPerFlowStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex','csbperflowstatsvdbeid','csbperflowstatsgateid','csbperflowstatsflowpairid','csbperflowstatssideid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.str, 'csbCallStatsServiceIndex')),
                    ('csbperflowstatsvdbeid', YLeaf(YType.int32, 'csbPerFlowStatsVdbeId')),
                    ('csbperflowstatsgateid', YLeaf(YType.int32, 'csbPerFlowStatsGateId')),
                    ('csbperflowstatsflowpairid', YLeaf(YType.int32, 'csbPerFlowStatsFlowPairId')),
                    ('csbperflowstatssideid', YLeaf(YType.enumeration, 'csbPerFlowStatsSideId')),
                    ('csbperflowstatsflowtype', YLeaf(YType.enumeration, 'csbPerFlowStatsFlowType')),
                    ('csbperflowstatsrtppktssent', YLeaf(YType.uint64, 'csbPerFlowStatsRTPPktsSent')),
                    ('csbperflowstatsrtppktsrcvd', YLeaf(YType.uint64, 'csbPerFlowStatsRTPPktsRcvd')),
                    ('csbperflowstatsrtppktsdiscard', YLeaf(YType.uint64, 'csbPerFlowStatsRTPPktsDiscard')),
                    ('csbperflowstatsrtpoctetssent', YLeaf(YType.uint64, 'csbPerFlowStatsRTPOctetsSent')),
                    ('csbperflowstatsrtpoctetsrcvd', YLeaf(YType.uint64, 'csbPerFlowStatsRTPOctetsRcvd')),
                    ('csbperflowstatsrtpoctetsdiscard', YLeaf(YType.uint64, 'csbPerFlowStatsRTPOctetsDiscard')),
                    ('csbperflowstatsrtcppktssent', YLeaf(YType.uint64, 'csbPerFlowStatsRTCPPktsSent')),
                    ('csbperflowstatsrtcppktsrcvd', YLeaf(YType.uint64, 'csbPerFlowStatsRTCPPktsRcvd')),
                    ('csbperflowstatsrtcppktslost', YLeaf(YType.uint64, 'csbPerFlowStatsRTCPPktsLost')),
                    ('csbperflowstatsepjitter', YLeaf(YType.uint64, 'csbPerFlowStatsEPJitter')),
                    ('csbperflowstatstmanpermbs', YLeaf(YType.uint32, 'csbPerFlowStatsTmanPerMbs')),
                    ('csbperflowstatstmanpersdr', YLeaf(YType.uint32, 'csbPerFlowStatsTmanPerSdr')),
                    ('csbperflowstatsdscpsettings', YLeaf(YType.str, 'csbPerFlowStatsDscpSettings')),
                    ('csbperflowstatsadrstatus', YLeaf(YType.str, 'csbPerFlowStatsAdrStatus')),
                    ('csbperflowstatsqasettings', YLeaf(YType.str, 'csbPerFlowStatsQASettings')),
                    ('csbperflowstatsrtppktslost', YLeaf(YType.uint64, 'csbPerFlowStatsRTPPktsLost')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbperflowstatsvdbeid = None
                self.csbperflowstatsgateid = None
                self.csbperflowstatsflowpairid = None
                self.csbperflowstatssideid = None
                self.csbperflowstatsflowtype = None
                self.csbperflowstatsrtppktssent = None
                self.csbperflowstatsrtppktsrcvd = None
                self.csbperflowstatsrtppktsdiscard = None
                self.csbperflowstatsrtpoctetssent = None
                self.csbperflowstatsrtpoctetsrcvd = None
                self.csbperflowstatsrtpoctetsdiscard = None
                self.csbperflowstatsrtcppktssent = None
                self.csbperflowstatsrtcppktsrcvd = None
                self.csbperflowstatsrtcppktslost = None
                self.csbperflowstatsepjitter = None
                self.csbperflowstatstmanpermbs = None
                self.csbperflowstatstmanpersdr = None
                self.csbperflowstatsdscpsettings = None
                self.csbperflowstatsadrstatus = None
                self.csbperflowstatsqasettings = None
                self.csbperflowstatsrtppktslost = None
                self._segment_path = lambda: "csbPerFlowStatsEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']" + "[csbPerFlowStatsVdbeId='" + str(self.csbperflowstatsvdbeid) + "']" + "[csbPerFlowStatsGateId='" + str(self.csbperflowstatsgateid) + "']" + "[csbPerFlowStatsFlowPairId='" + str(self.csbperflowstatsflowpairid) + "']" + "[csbPerFlowStatsSideId='" + str(self.csbperflowstatssideid) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbPerFlowStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbperflowstatstable.Csbperflowstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbperflowstatsvdbeid', 'csbperflowstatsgateid', 'csbperflowstatsflowpairid', 'csbperflowstatssideid', 'csbperflowstatsflowtype', 'csbperflowstatsrtppktssent', 'csbperflowstatsrtppktsrcvd', 'csbperflowstatsrtppktsdiscard', 'csbperflowstatsrtpoctetssent', 'csbperflowstatsrtpoctetsrcvd', 'csbperflowstatsrtpoctetsdiscard', 'csbperflowstatsrtcppktssent', 'csbperflowstatsrtcppktsrcvd', 'csbperflowstatsrtcppktslost', 'csbperflowstatsepjitter', 'csbperflowstatstmanpermbs', 'csbperflowstatstmanpersdr', 'csbperflowstatsdscpsettings', 'csbperflowstatsadrstatus', 'csbperflowstatsqasettings', 'csbperflowstatsrtppktslost'], name, value)

            class Csbperflowstatsflowtype(Enum):
                """
                Csbperflowstatsflowtype (Enum Class)

                This object indicates the type of the flow, like media flow,

                signaling flow etc.

                .. data:: media = 1

                .. data:: signalling = 2

                """

                media = Enum.YLeaf(1, "media")

                signalling = Enum.YLeaf(2, "signalling")


            class Csbperflowstatssideid(Enum):
                """
                Csbperflowstatssideid (Enum Class)

                This object identifies the index corresponding to side of flow

                pair either side A or side B. This object also acts as an index

                for the table.

                .. data:: sideA = 1

                .. data:: sideB = 2

                """

                sideA = Enum.YLeaf(1, "sideA")

                sideB = Enum.YLeaf(2, "sideB")



    class Csbh248Statstable(Entity):
        """
        This table describes the H.248 statistics for SBC. The index of
        the table is service index which corresponds to a particular 
        service configured on the SBC and the index assigned to a
        particular H.248 controller. The other index of this table is
        csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
        This table is replaced by the csbH248StatsRev1Table.
        
        .. attribute:: csbh248statsentry
        
        	An conceptual row in the csbCallStath248Table. There is an entry in this table for the particular controller by a value of csbH248StatsCtrlrIndex. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbh248Statsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable.Csbh248Statsentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable, self).__init__()

            self.yang_name = "csbH248StatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbH248StatsEntry", ("csbh248statsentry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable.Csbh248Statsentry))])
            self._leafs = OrderedDict()

            self.csbh248statsentry = YList(self)
            self._segment_path = lambda: "csbH248StatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable, [], name, value)


        class Csbh248Statsentry(Entity):
            """
            An conceptual row in the csbCallStath248Table. There is
            an entry in this table for the particular controller by a value
            of csbH248StatsCtrlrIndex. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbh248statsctrlrindex  (key)
            
            	This object identifies the controller index of the H.248 server. This is also the index for the table
            	**type**\: int
            
            	**range:** 1..50
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestssent
            
            	This object indicates the requests sent through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsrcvd
            
            	This object indicates the requests received through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsfailed
            
            	This object indicates the requests failed on session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsretried
            
            	This object indicates the requests retried through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliessent
            
            	This object indicates the number of replies sent through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliesrcvd
            
            	This object indicates the number of replies received from the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliesretried
            
            	This object indicates the number of replies retried through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statssegpktssent
            
            	This object indicates the number of packets sent through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statssegpktsrcvd
            
            	This object indicates the number of packets received from the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsestablishedtime
            
            	This object indicates the H.248 Controller established time (the time at which the association became established)
            	**type**\: str
            
            	**length:** 0..80
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statstmaxtimeoutval
            
            	This object indicates the T\-Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC before deciding that the request has failed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrtt
            
            	This object indicates the calculated RTT value. This field specifies the maximum round trip propagation delay in the  network (in milliseconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statslt
            
            	This object indicates the LT value calculated from RTT value and Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC plus the maximum round trip propagation delay in the network (in milliseconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable.Csbh248Statsentry, self).__init__()

                self.yang_name = "csbH248StatsEntry"
                self.yang_parent_name = "csbH248StatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex','csbh248statsctrlrindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.str, 'csbCallStatsServiceIndex')),
                    ('csbh248statsctrlrindex', YLeaf(YType.int32, 'csbH248StatsCtrlrIndex')),
                    ('csbh248statsrequestssent', YLeaf(YType.uint32, 'csbH248StatsRequestsSent')),
                    ('csbh248statsrequestsrcvd', YLeaf(YType.uint32, 'csbH248StatsRequestsRcvd')),
                    ('csbh248statsrequestsfailed', YLeaf(YType.uint32, 'csbH248StatsRequestsFailed')),
                    ('csbh248statsrequestsretried', YLeaf(YType.uint32, 'csbH248StatsRequestsRetried')),
                    ('csbh248statsrepliessent', YLeaf(YType.uint32, 'csbH248StatsRepliesSent')),
                    ('csbh248statsrepliesrcvd', YLeaf(YType.uint32, 'csbH248StatsRepliesRcvd')),
                    ('csbh248statsrepliesretried', YLeaf(YType.uint32, 'csbH248StatsRepliesRetried')),
                    ('csbh248statssegpktssent', YLeaf(YType.uint32, 'csbH248StatsSegPktsSent')),
                    ('csbh248statssegpktsrcvd', YLeaf(YType.uint32, 'csbH248StatsSegPktsRcvd')),
                    ('csbh248statsestablishedtime', YLeaf(YType.str, 'csbH248StatsEstablishedTime')),
                    ('csbh248statstmaxtimeoutval', YLeaf(YType.int32, 'csbH248StatsTMaxTimeoutVal')),
                    ('csbh248statsrtt', YLeaf(YType.uint32, 'csbH248StatsRTT')),
                    ('csbh248statslt', YLeaf(YType.uint32, 'csbH248StatsLT')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbh248statsctrlrindex = None
                self.csbh248statsrequestssent = None
                self.csbh248statsrequestsrcvd = None
                self.csbh248statsrequestsfailed = None
                self.csbh248statsrequestsretried = None
                self.csbh248statsrepliessent = None
                self.csbh248statsrepliesrcvd = None
                self.csbh248statsrepliesretried = None
                self.csbh248statssegpktssent = None
                self.csbh248statssegpktsrcvd = None
                self.csbh248statsestablishedtime = None
                self.csbh248statstmaxtimeoutval = None
                self.csbh248statsrtt = None
                self.csbh248statslt = None
                self._segment_path = lambda: "csbH248StatsEntry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']" + "[csbH248StatsCtrlrIndex='" + str(self.csbh248statsctrlrindex) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbH248StatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statstable.Csbh248Statsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbh248statsctrlrindex', 'csbh248statsrequestssent', 'csbh248statsrequestsrcvd', 'csbh248statsrequestsfailed', 'csbh248statsrequestsretried', 'csbh248statsrepliessent', 'csbh248statsrepliesrcvd', 'csbh248statsrepliesretried', 'csbh248statssegpktssent', 'csbh248statssegpktsrcvd', 'csbh248statsestablishedtime', 'csbh248statstmaxtimeoutval', 'csbh248statsrtt', 'csbh248statslt'], name, value)


    class Csbh248Statsrev1Table(Entity):
        """
        This table describes the H.248 statistics for SBC. The index of
        the table is service index which corresponds to a particular 
        service configured on the SBC and the index assigned to a
        particular H.248 controller. The other index of this table is
        csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
        
        .. attribute:: csbh248statsrev1entry
        
        	An conceptual row in the csbCallStath248Table. There is an entry in this table for the particular Vdbe by a value of csbH248StatsVdbeId. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbh248Statsrev1Entry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table.Csbh248Statsrev1Entry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table, self).__init__()

            self.yang_name = "csbH248StatsRev1Table"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("csbH248StatsRev1Entry", ("csbh248statsrev1entry", CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table.Csbh248Statsrev1Entry))])
            self._leafs = OrderedDict()

            self.csbh248statsrev1entry = YList(self)
            self._segment_path = lambda: "csbH248StatsRev1Table"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table, [], name, value)


        class Csbh248Statsrev1Entry(Entity):
            """
            An conceptual row in the csbCallStath248Table. There is
            an entry in this table for the particular Vdbe by a value
            of csbH248StatsVdbeId. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbh248statsvdbeid  (key)
            
            	This object identifies the virtual media gateway id. This is also the index for the table
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: csbh248statsrequestssentrev1
            
            	This object indicates the requests sent through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsrcvdrev1
            
            	This object indicates the requests received through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsfailedrev1
            
            	This object indicates the requests failed on session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsretriedrev1
            
            	This object indicates the requests retried through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrepliessentrev1
            
            	This object indicates the number of replies sent through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrepliesrcvdrev1
            
            	This object indicates the number of replies received from the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrepliesretriedrev1
            
            	This object indicates the number of replies retried through the Session Controller Interface to an SBE or DBE
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statssegpktssentrev1
            
            	This object indicates the number of response segments sent by DBE. This field will only be present if segmentation is enabled on this association
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statssegpktsrcvdrev1
            
            	This object indicates the number of response segments received by DBE. This field will only be present if segmentation is enabled on this association
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsestablishedtimerev1
            
            	This object indicates the H.248 Controller established time (the time at which the association became established)
            	**type**\: str
            
            	**length:** 0..80
            
            .. attribute:: csbh248statstmaxtimeoutvalrev1
            
            	This object indicates the T\-Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC before deciding that the request has failed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: csbh248statsrttrev1
            
            	This object indicates the calculated RTT value. This field specifies the maximum round trip propagation delay in the  network (in milliseconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: csbh248statsltrev1
            
            	This object indicates the LT value calculated from RTT value and Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC plus the maximum round trip propagation delay in the network (in milliseconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table.Csbh248Statsrev1Entry, self).__init__()

                self.yang_name = "csbH248StatsRev1Entry"
                self.yang_parent_name = "csbH248StatsRev1Table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csbcallstatsinstanceindex','csbcallstatsserviceindex','csbh248statsvdbeid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csbcallstatsinstanceindex', YLeaf(YType.str, 'csbCallStatsInstanceIndex')),
                    ('csbcallstatsserviceindex', YLeaf(YType.str, 'csbCallStatsServiceIndex')),
                    ('csbh248statsvdbeid', YLeaf(YType.int32, 'csbH248StatsVdbeId')),
                    ('csbh248statsrequestssentrev1', YLeaf(YType.uint32, 'csbH248StatsRequestsSentRev1')),
                    ('csbh248statsrequestsrcvdrev1', YLeaf(YType.uint32, 'csbH248StatsRequestsRcvdRev1')),
                    ('csbh248statsrequestsfailedrev1', YLeaf(YType.uint32, 'csbH248StatsRequestsFailedRev1')),
                    ('csbh248statsrequestsretriedrev1', YLeaf(YType.uint32, 'csbH248StatsRequestsRetriedRev1')),
                    ('csbh248statsrepliessentrev1', YLeaf(YType.uint32, 'csbH248StatsRepliesSentRev1')),
                    ('csbh248statsrepliesrcvdrev1', YLeaf(YType.uint32, 'csbH248StatsRepliesRcvdRev1')),
                    ('csbh248statsrepliesretriedrev1', YLeaf(YType.uint32, 'csbH248StatsRepliesRetriedRev1')),
                    ('csbh248statssegpktssentrev1', YLeaf(YType.uint32, 'csbH248StatsSegPktsSentRev1')),
                    ('csbh248statssegpktsrcvdrev1', YLeaf(YType.uint32, 'csbH248StatsSegPktsRcvdRev1')),
                    ('csbh248statsestablishedtimerev1', YLeaf(YType.str, 'csbH248StatsEstablishedTimeRev1')),
                    ('csbh248statstmaxtimeoutvalrev1', YLeaf(YType.int32, 'csbH248StatsTMaxTimeoutValRev1')),
                    ('csbh248statsrttrev1', YLeaf(YType.uint32, 'csbH248StatsRTTRev1')),
                    ('csbh248statsltrev1', YLeaf(YType.uint32, 'csbH248StatsLTRev1')),
                ])
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbh248statsvdbeid = None
                self.csbh248statsrequestssentrev1 = None
                self.csbh248statsrequestsrcvdrev1 = None
                self.csbh248statsrequestsfailedrev1 = None
                self.csbh248statsrequestsretriedrev1 = None
                self.csbh248statsrepliessentrev1 = None
                self.csbh248statsrepliesrcvdrev1 = None
                self.csbh248statsrepliesretriedrev1 = None
                self.csbh248statssegpktssentrev1 = None
                self.csbh248statssegpktsrcvdrev1 = None
                self.csbh248statsestablishedtimerev1 = None
                self.csbh248statstmaxtimeoutvalrev1 = None
                self.csbh248statsrttrev1 = None
                self.csbh248statsltrev1 = None
                self._segment_path = lambda: "csbH248StatsRev1Entry" + "[csbCallStatsInstanceIndex='" + str(self.csbcallstatsinstanceindex) + "']" + "[csbCallStatsServiceIndex='" + str(self.csbcallstatsserviceindex) + "']" + "[csbH248StatsVdbeId='" + str(self.csbh248statsvdbeid) + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbH248StatsRev1Table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbh248Statsrev1Table.Csbh248Statsrev1Entry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbh248statsvdbeid', 'csbh248statsrequestssentrev1', 'csbh248statsrequestsrcvdrev1', 'csbh248statsrequestsfailedrev1', 'csbh248statsrequestsretriedrev1', 'csbh248statsrepliessentrev1', 'csbh248statsrepliesrcvdrev1', 'csbh248statsrepliesretriedrev1', 'csbh248statssegpktssentrev1', 'csbh248statssegpktsrcvdrev1', 'csbh248statsestablishedtimerev1', 'csbh248statstmaxtimeoutvalrev1', 'csbh248statsrttrev1', 'csbh248statsltrev1'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOSESSBORDERCTRLRCALLSTATSMIB()
        return self._top_entity

