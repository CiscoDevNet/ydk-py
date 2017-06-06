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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CiscosbcperiodicstatsintervalEnum(Enum):
    """
    CiscosbcperiodicstatsintervalEnum

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

    fiveMinute = 1

    fifteenMinute = 2

    oneHour = 3

    oneDay = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
        return meta._meta_table['CiscosbcperiodicstatsintervalEnum']



class CiscoSessBorderCtrlrCallStatsMib(object):
    """
    
    
    .. attribute:: csbcallstatsinstancetable
    
    	The call stats instance table contains the physical index for each of the physical entity (line card, primary, secondary cards). The index of the table is instance index which uniquely identifies the physical entity present on the box
    	**type**\:   :py:class:`Csbcallstatsinstancetable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable>`
    
    .. attribute:: csbcallstatstable
    
    	This table describes the global statistics information in the form of a table which contains call specific information like call rates, media flows, signaling flows etc. The index of the table is service index which corresponds to a particular  service configured on the SBC and all the rows of the table represents the global information regarding all the call flows related to that particular service. The other index of this table is csbCallStatsInstanceIndex which is defined in csbCallStatsInstanceTable
    	**type**\:   :py:class:`Csbcallstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable>`
    
    .. attribute:: csbcurrperiodicstatstable
    
    	This table is used to collect measurement over several different intervals as defined by the csbCurrPeriodicStatsInterval object. When a new interval starts the objects associated with the interval are reset and count up throughout the interval. The index of the table is the interval for which the stats information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour and one day. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable.  The gauge values are reported as \:\- 1.If the period being queried is current5mins, this is the value at the instant that the query is issued.  2.Otherwise, for the other intevals, this is an average value during the summary period sampled at 5 minute intervals
    	**type**\:   :py:class:`Csbcurrperiodicstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable>`
    
    .. attribute:: csbh248statsrev1table
    
    	This table describes the H.248 statistics for SBC. The index of the table is service index which corresponds to a particular  service configured on the SBC and the index assigned to a particular H.248 controller. The other index of this table is csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
    	**type**\:   :py:class:`Csbh248Statsrev1Table <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table>`
    
    .. attribute:: csbh248statstable
    
    	This table describes the H.248 statistics for SBC. The index of the table is service index which corresponds to a particular  service configured on the SBC and the index assigned to a particular H.248 controller. The other index of this table is csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable. This table is replaced by the csbH248StatsRev1Table
    	**type**\:   :py:class:`Csbh248Statstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable>`
    
    	**status**\: deprecated
    
    .. attribute:: csbhistorystatstable
    
    	This table provide historical measurement in various interval length defined by the csbHistoryStatsInterval object. Each interval may contain one or more entries to allow for detailed measurment to be collected. It is up to the platform to determine the number of intervals to be supported like  5 minutes, 15 minutes, 1 hour and 1 day. In addition, the number of historical entries is also determined by the platform resources.  The gauge values are reported as\: If the period being queried is previous5mins, this is the number of calls that were active at the end of the previous 5 minute period. Otherwise for the other intevals, this is an average value during the summary period, sampled at 5 minute intervals
    	**type**\:   :py:class:`Csbhistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable>`
    
    .. attribute:: csbperflowstatstable
    
    	This table describes statistics table for each call flow. The indices of the table are virtual media gateway id, gate id, falow pair id and side id (indices for side A or side B). The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:   :py:class:`Csbperflowstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable>`
    
    

    """

    _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
    _revision = '2010-09-03'

    def __init__(self):
        self.csbcallstatsinstancetable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable()
        self.csbcallstatsinstancetable.parent = self
        self.csbcallstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable()
        self.csbcallstatstable.parent = self
        self.csbcurrperiodicstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable()
        self.csbcurrperiodicstatstable.parent = self
        self.csbh248statsrev1table = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table()
        self.csbh248statsrev1table.parent = self
        self.csbh248statstable = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable()
        self.csbh248statstable.parent = self
        self.csbhistorystatstable = CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable()
        self.csbhistorystatstable.parent = self
        self.csbperflowstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable()
        self.csbperflowstatstable.parent = self


    class Csbcallstatsinstancetable(object):
        """
        The call stats instance table contains the physical index for
        each of the physical entity (line card, primary, secondary
        cards). The index of the table is instance index which uniquely
        identifies the physical entity present on the box.
        
        .. attribute:: csbcallstatsinstanceentry
        
        	A conceptual row in csbCallStatsInstanceTable. There is an entry in this table for each SBC instance, as identified by a  value of csbCallStatsInstanceIndex
        	**type**\: list of    :py:class:`Csbcallstatsinstanceentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbcallstatsinstanceentry = YList()
            self.csbcallstatsinstanceentry.parent = self
            self.csbcallstatsinstanceentry.name = 'csbcallstatsinstanceentry'


        class Csbcallstatsinstanceentry(object):
            """
            A conceptual row in csbCallStatsInstanceTable. There is an
            entry in this table for each SBC instance, as identified by a 
            value of csbCallStatsInstanceIndex.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	This object uniquely identifies the sequence number of an entity or slot that is configured per device. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsinstancephysicalindex
            
            	This object indicates the physical entity for which all the measurements are maintained. The exact type of this entity is described by its entPhysicalVendorType value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsinstancephysicalindex = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsinstancephysicalindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbcallstatsinstanceentry is not None:
                for child_ref in self.csbcallstatsinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable']['meta_info']


    class Csbcallstatstable(object):
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
        	**type**\: list of    :py:class:`Csbcallstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbcallstatsentry = YList()
            self.csbcallstatsentry.parent = self
            self.csbcallstatsentry.name = 'csbcallstatsentry'


        class Csbcallstatsentry(object):
            """
            An conceptual row in the csbCallStatsGlobalStatsTable. There is
            an entry in this table for the particular service configured on
            SBC identified by a value of csbCallStatsInstanceIndex. The
            other index of this table is csbCallStatsInstanceIndex which is
            defined in csbCallStatsInstanceTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	This object identifies the index of the name of the SBC service configured. This object also acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsactivetranscodeflows
            
            	This object indicates the current number of transcoded flows that are actively forwarding media traffic.  In this context, a flow is a media stream passing through the device. So a single voice call will be counted only once
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsavailableflows
            
            	This object indicates the number of media flows which are available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsavailablepktrate
            
            	This object indicates the remaining capacity that can be supported by SBC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets per second
            
            .. attribute:: csbcallstatsavailabletranscodeflows
            
            	This object indicates the number of additional transcoded flows that this media gateway manager (MGM) entity is currently able to configure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatscallshigh
            
            	This object indicates the maximum number of calls per second processed by the Session Border Controller in past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatscallslow
            
            	This object indicates the minimum calls per second in past 24 hours
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatsnomediacount
            
            	This object indicates the accumulated No media event count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: no media events
            
            .. attribute:: csbcallstatspeakflows
            
            	This object indicates the number of peak flows in SBC. This is the highest recorded value for the active flows since the box was booted/reseted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatspeaksigflows
            
            	This object indicates the peak signaling flow in SBC. This is the highest recorded value for the active signaling flows. This object is calculated using csbCallStatsUsedFlows
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            .. attribute:: csbcallstatspeaktranscodeflows
            
            	This object indicates the peak number of active transcoded flows since the statistics were last reset.  In this context, a flow is a media stream passing through the device, so a single voice call will be counted once
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsrate1sec
            
            	This object indicates the average calls per second processed by the Session Border Controller
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: csbcallstatsrouteerrors
            
            	This object indicates the accumulated route error event count. This counter is for the route error of media stream
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: route error events
            
            .. attribute:: csbcallstatsrtpoctetsdiscard
            
            	This object indicates the number of RTP octets discarded by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsrtpoctetsrcvd
            
            	This object indicates the number of RTP octets received by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsrtpoctetssent
            
            	This object indicates the number of RTP octets sent by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbcallstatsrtppktsdiscard
            
            	This object indicates the total number of RTP packets discarded
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtppktsrcvd
            
            	This object indicates the total number of RTP packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsrtppktssent
            
            	This object indicates the total number of RTP packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatssbcname
            
            	This object indicates the configured name of the SBC service. The length of this object is zero when value is not assigned to it
            	**type**\:  str
            
            .. attribute:: csbcallstatstotalflows
            
            	This object indicates the total number of media support by this instance of SBC. The total number of flows include the available flows and the active flows. This value is since box was booted/reseted. Total flows include the active flows and the flows allocated but not connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatstotalsigflows
            
            	This object indicates the maximum number of Signalling Flows that can be supported by this instance of SBC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            .. attribute:: csbcallstatstotaltranscodeflows
            
            	This object indicates the accumulated total number of transcoded flows.  This count contains both active flows and flows that were allocated but never connected.  In this context, a flow is a media stream passing through the device, so a single voice call will be counted once
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsunclassifiedpkts
            
            	This object indicates the number of unclassified packets processed by SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbcallstatsusedflows
            
            	This object indicates the number of media flows which are used. This is for the flow allocated and connected. The flow allocated but not connected is not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: flows
            
            .. attribute:: csbcallstatsusedsigflows
            
            	This object indicates the number of active signaling flows for signaling pinholes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: signal flows
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbcallstatsactivetranscodeflows = None
                self.csbcallstatsavailableflows = None
                self.csbcallstatsavailablepktrate = None
                self.csbcallstatsavailabletranscodeflows = None
                self.csbcallstatscallshigh = None
                self.csbcallstatscallslow = None
                self.csbcallstatsnomediacount = None
                self.csbcallstatspeakflows = None
                self.csbcallstatspeaksigflows = None
                self.csbcallstatspeaktranscodeflows = None
                self.csbcallstatsrate1sec = None
                self.csbcallstatsrouteerrors = None
                self.csbcallstatsrtpoctetsdiscard = None
                self.csbcallstatsrtpoctetsrcvd = None
                self.csbcallstatsrtpoctetssent = None
                self.csbcallstatsrtppktsdiscard = None
                self.csbcallstatsrtppktsrcvd = None
                self.csbcallstatsrtppktssent = None
                self.csbcallstatssbcname = None
                self.csbcallstatstotalflows = None
                self.csbcallstatstotalsigflows = None
                self.csbcallstatstotaltranscodeflows = None
                self.csbcallstatsunclassifiedpkts = None
                self.csbcallstatsusedflows = None
                self.csbcallstatsusedsigflows = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbcallstatsactivetranscodeflows is not None:
                    return True

                if self.csbcallstatsavailableflows is not None:
                    return True

                if self.csbcallstatsavailablepktrate is not None:
                    return True

                if self.csbcallstatsavailabletranscodeflows is not None:
                    return True

                if self.csbcallstatscallshigh is not None:
                    return True

                if self.csbcallstatscallslow is not None:
                    return True

                if self.csbcallstatsnomediacount is not None:
                    return True

                if self.csbcallstatspeakflows is not None:
                    return True

                if self.csbcallstatspeaksigflows is not None:
                    return True

                if self.csbcallstatspeaktranscodeflows is not None:
                    return True

                if self.csbcallstatsrate1sec is not None:
                    return True

                if self.csbcallstatsrouteerrors is not None:
                    return True

                if self.csbcallstatsrtpoctetsdiscard is not None:
                    return True

                if self.csbcallstatsrtpoctetsrcvd is not None:
                    return True

                if self.csbcallstatsrtpoctetssent is not None:
                    return True

                if self.csbcallstatsrtppktsdiscard is not None:
                    return True

                if self.csbcallstatsrtppktsrcvd is not None:
                    return True

                if self.csbcallstatsrtppktssent is not None:
                    return True

                if self.csbcallstatssbcname is not None:
                    return True

                if self.csbcallstatstotalflows is not None:
                    return True

                if self.csbcallstatstotalsigflows is not None:
                    return True

                if self.csbcallstatstotaltranscodeflows is not None:
                    return True

                if self.csbcallstatsunclassifiedpkts is not None:
                    return True

                if self.csbcallstatsusedflows is not None:
                    return True

                if self.csbcallstatsusedsigflows is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbcallstatsentry is not None:
                for child_ref in self.csbcallstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable']['meta_info']


    class Csbcurrperiodicstatstable(object):
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
        	**type**\: list of    :py:class:`Csbcurrperiodicstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbcurrperiodicstatsentry = YList()
            self.csbcurrperiodicstatsentry.parent = self
            self.csbcurrperiodicstatsentry.name = 'csbcurrperiodicstatsentry'


        class Csbcurrperiodicstatsentry(object):
            """
            An conceptual row in the csbCurrPeriodicStatsTable. There is
            an entry in this table for the particular controller by a value
            of csbH248StatsCtrlrIndex. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbcurrperiodicstatsinterval  <key>
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts as index for the table
            	**type**\:   :py:class:`CiscosbcperiodicstatsintervalEnum <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscosbcperiodicstatsintervalEnum>`
            
            .. attribute:: csbcurrperiodicipseccalls
            
            	The number of active calls on this adjacency or account which are to or from registered subscribers using IPSEC during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactivatingcalls
            
            	This object indicates the number of calls that have become activing during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactivecallfailure
            
            	This object indicates the number of active call failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatsactivecalls
            
            	This object indicates the number of calls that have become active during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactivee2emergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) and have used the e2 interface to obtain location information for the caller during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactiveemergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsactiveipv6calls
            
            	This Object indicates the number of calls through SBC that use IPv6 signaling.  This statistic totals all calls that traverse an IPv6 adjacency on either or both sides of SBC during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsaudiotranscodedcalls
            
            	The number of active audio transcoded calls through this adjacency or account during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatscallmediafailure
            
            	This object indicates the number of call setup failures due to media failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallresourcefailure
            
            	This object indicates the number of call setup failures due to resource failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallroutingfailure
            
            	This object indicates the number of call setup failures due to routing failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacbandwidthfailure
            
            	This object indicates the number of call setup failures due to CAC bandwidth limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcaccalllimitfailure
            
            	This object indicates the number of call setup failures due to CAC call limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacmedialimitfailure
            
            	This object indicates the number of call setup failures due to CAC media limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacmediaupdatefailure
            
            	This object indicates the number of call update failure due to policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacpolicyfailure
            
            	This object indicates the number of call setup failures due to CAC policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupcacratelimitfailure
            
            	This object indicates the number of call setup failures due to CAC call rate limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetupnapolicyfailure
            
            	This object indicates the number of call setup failures due to NA policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetuppolicyfailure
            
            	This object indicates the number of call setup failures due to policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsetuproutingpolicyfailure
            
            	This object indicates the number of call setup failures due to routing policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscallsigfailure
            
            	This object indicates the number of call setup failures due to signaling failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscongestionfailure
            
            	This object indicates the number of call setup failures due to congestion during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatscurrenttaps
            
            	This object indicates the Lawful intercept taps currently in place on calls within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: taps
            
            .. attribute:: csbcurrperiodicstatsdeactivatingcalls
            
            	This object indicates the number of calls that have become deactiving during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiw2833calls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via RFC 2833 during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiw2833inbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in media via RFC 2833 and DTMF in media via inband DTMF tones during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsdtmfiwinbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via  inband DTMF tones during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsfailedcallattempts
            
            	This object indicates the number of failed call attempts during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatsfaxtranscodedcalls
            
            	This object indicates the the number of active fax transcoded calls through this adjacency or account during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsimsrxactivecalls
            
            	This object indicates the total number of active calls which use IMS Rx, during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsimsrxcallrenegotiationattempts
            
            	This object indicates the total call renegotiation attempts using IMS Rx during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbcurrperiodicstatsimsrxcallrenegotiationfailures
            
            	This object indicates the total call renegotiation failures owing to IMS Rx failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatsimsrxcallsetupfaiures
            
            	This object indicates the total call Setup failures owing to IMS Rx failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatsnonsrtpcalls
            
            	This object indicates the number of active calls through this adjacency or account which do not use SRTP on any media channels during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatsrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to RTP being proposed when not permitted during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatssrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to SRTP being proposed when not permitted during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbcurrperiodicstatssrtpiwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that provide interworking between RTP and SRTP during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatssrtpnoniwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels which use SRTP. This count does not include media  channels that provide interworking between RTP and SRTP during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstimestamp
            
            	This object indicates the current time at the start of each interval
            	**type**\:  str
            
            	**length:** 0..80
            
            .. attribute:: csbcurrperiodicstatstotalcallattempts
            
            	This object indicates the number of total call attempts during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcurrperiodicstatstotalcallupdatefailure
            
            	This object indicates the total number of call update failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstotaltapsrequested
            
            	This object indicates the lawful intercept tap attempts requested within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbcurrperiodicstatstotaltapssucceeded
            
            	This object indicates the lawful intercept tap attempts that have been successfully implemented within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: success
            
            .. attribute:: csbcurrperiodicstatstranscodedcalls
            
            	The object indicates the number of transcoded calls that are active during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbcurrperiodicstatstransratedcalls
            
            	The object indicates the number of transrated calls that are active during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbcurrperiodicstatsinterval = None
                self.csbcurrperiodicipseccalls = None
                self.csbcurrperiodicstatsactivatingcalls = None
                self.csbcurrperiodicstatsactivecallfailure = None
                self.csbcurrperiodicstatsactivecalls = None
                self.csbcurrperiodicstatsactivee2emergencycalls = None
                self.csbcurrperiodicstatsactiveemergencycalls = None
                self.csbcurrperiodicstatsactiveipv6calls = None
                self.csbcurrperiodicstatsaudiotranscodedcalls = None
                self.csbcurrperiodicstatscallmediafailure = None
                self.csbcurrperiodicstatscallresourcefailure = None
                self.csbcurrperiodicstatscallroutingfailure = None
                self.csbcurrperiodicstatscallsetupcacbandwidthfailure = None
                self.csbcurrperiodicstatscallsetupcaccalllimitfailure = None
                self.csbcurrperiodicstatscallsetupcacmedialimitfailure = None
                self.csbcurrperiodicstatscallsetupcacmediaupdatefailure = None
                self.csbcurrperiodicstatscallsetupcacpolicyfailure = None
                self.csbcurrperiodicstatscallsetupcacratelimitfailure = None
                self.csbcurrperiodicstatscallsetupnapolicyfailure = None
                self.csbcurrperiodicstatscallsetuppolicyfailure = None
                self.csbcurrperiodicstatscallsetuproutingpolicyfailure = None
                self.csbcurrperiodicstatscallsigfailure = None
                self.csbcurrperiodicstatscongestionfailure = None
                self.csbcurrperiodicstatscurrenttaps = None
                self.csbcurrperiodicstatsdeactivatingcalls = None
                self.csbcurrperiodicstatsdtmfiw2833calls = None
                self.csbcurrperiodicstatsdtmfiw2833inbandcalls = None
                self.csbcurrperiodicstatsdtmfiwinbandcalls = None
                self.csbcurrperiodicstatsfailedcallattempts = None
                self.csbcurrperiodicstatsfaxtranscodedcalls = None
                self.csbcurrperiodicstatsimsrxactivecalls = None
                self.csbcurrperiodicstatsimsrxcallrenegotiationattempts = None
                self.csbcurrperiodicstatsimsrxcallrenegotiationfailures = None
                self.csbcurrperiodicstatsimsrxcallsetupfaiures = None
                self.csbcurrperiodicstatsnonsrtpcalls = None
                self.csbcurrperiodicstatsrtpdisallowedfailures = None
                self.csbcurrperiodicstatssrtpdisallowedfailures = None
                self.csbcurrperiodicstatssrtpiwcalls = None
                self.csbcurrperiodicstatssrtpnoniwcalls = None
                self.csbcurrperiodicstatstimestamp = None
                self.csbcurrperiodicstatstotalcallattempts = None
                self.csbcurrperiodicstatstotalcallupdatefailure = None
                self.csbcurrperiodicstatstotaltapsrequested = None
                self.csbcurrperiodicstatstotaltapssucceeded = None
                self.csbcurrperiodicstatstranscodedcalls = None
                self.csbcurrperiodicstatstransratedcalls = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')
                if self.csbcurrperiodicstatsinterval is None:
                    raise YPYModelError('Key property csbcurrperiodicstatsinterval is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCurrPeriodicStatsTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCurrPeriodicStatsEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCurrPeriodicStatsInterval = ' + str(self.csbcurrperiodicstatsinterval) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbcurrperiodicstatsinterval is not None:
                    return True

                if self.csbcurrperiodicipseccalls is not None:
                    return True

                if self.csbcurrperiodicstatsactivatingcalls is not None:
                    return True

                if self.csbcurrperiodicstatsactivecallfailure is not None:
                    return True

                if self.csbcurrperiodicstatsactivecalls is not None:
                    return True

                if self.csbcurrperiodicstatsactivee2emergencycalls is not None:
                    return True

                if self.csbcurrperiodicstatsactiveemergencycalls is not None:
                    return True

                if self.csbcurrperiodicstatsactiveipv6calls is not None:
                    return True

                if self.csbcurrperiodicstatsaudiotranscodedcalls is not None:
                    return True

                if self.csbcurrperiodicstatscallmediafailure is not None:
                    return True

                if self.csbcurrperiodicstatscallresourcefailure is not None:
                    return True

                if self.csbcurrperiodicstatscallroutingfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcacbandwidthfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcaccalllimitfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcacmedialimitfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcacmediaupdatefailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcacpolicyfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupcacratelimitfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetupnapolicyfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetuppolicyfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsetuproutingpolicyfailure is not None:
                    return True

                if self.csbcurrperiodicstatscallsigfailure is not None:
                    return True

                if self.csbcurrperiodicstatscongestionfailure is not None:
                    return True

                if self.csbcurrperiodicstatscurrenttaps is not None:
                    return True

                if self.csbcurrperiodicstatsdeactivatingcalls is not None:
                    return True

                if self.csbcurrperiodicstatsdtmfiw2833calls is not None:
                    return True

                if self.csbcurrperiodicstatsdtmfiw2833inbandcalls is not None:
                    return True

                if self.csbcurrperiodicstatsdtmfiwinbandcalls is not None:
                    return True

                if self.csbcurrperiodicstatsfailedcallattempts is not None:
                    return True

                if self.csbcurrperiodicstatsfaxtranscodedcalls is not None:
                    return True

                if self.csbcurrperiodicstatsimsrxactivecalls is not None:
                    return True

                if self.csbcurrperiodicstatsimsrxcallrenegotiationattempts is not None:
                    return True

                if self.csbcurrperiodicstatsimsrxcallrenegotiationfailures is not None:
                    return True

                if self.csbcurrperiodicstatsimsrxcallsetupfaiures is not None:
                    return True

                if self.csbcurrperiodicstatsnonsrtpcalls is not None:
                    return True

                if self.csbcurrperiodicstatsrtpdisallowedfailures is not None:
                    return True

                if self.csbcurrperiodicstatssrtpdisallowedfailures is not None:
                    return True

                if self.csbcurrperiodicstatssrtpiwcalls is not None:
                    return True

                if self.csbcurrperiodicstatssrtpnoniwcalls is not None:
                    return True

                if self.csbcurrperiodicstatstimestamp is not None:
                    return True

                if self.csbcurrperiodicstatstotalcallattempts is not None:
                    return True

                if self.csbcurrperiodicstatstotalcallupdatefailure is not None:
                    return True

                if self.csbcurrperiodicstatstotaltapsrequested is not None:
                    return True

                if self.csbcurrperiodicstatstotaltapssucceeded is not None:
                    return True

                if self.csbcurrperiodicstatstranscodedcalls is not None:
                    return True

                if self.csbcurrperiodicstatstransratedcalls is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCurrPeriodicStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbcurrperiodicstatsentry is not None:
                for child_ref in self.csbcurrperiodicstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable']['meta_info']


    class Csbhistorystatstable(object):
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
        	**type**\: list of    :py:class:`Csbhistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbhistorystatsentry = YList()
            self.csbhistorystatsentry.parent = self
            self.csbhistorystatsentry.name = 'csbhistorystatsentry'


        class Csbhistorystatsentry(object):
            """
            A conceptual row in the csbHistoryStatsTable. The entries in
            this table are updated as interval completes in the
            csbCurrPeriodicStatsTable table and the data is moved from that
            table to this one.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbhistorystatsinterval  <key>
            
            	This object identifies the interval for which the history statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 day. This object acts as index for the table
            	**type**\:   :py:class:`CiscosbcperiodicstatsintervalEnum <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscosbcperiodicstatsintervalEnum>`
            
            .. attribute:: csbhistorystatselements  <key>
            
            	The platform assigns a number starting with one and increments it each for each new row. When the maximum          number of row is reached the oldest rows are deleted. It is up to the platform to determine the number of entries for each interval. It is recommended that each platform support at least one entry for 5 min, 15 mins, 1 hour and 1 day intervals
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsactivecallfailure
            
            	This object indicates the number of active call failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsactivecalls
            
            	This object indicates the number of active calls history during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactivee2emergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis) and have used the e2 interface to obtain location information for the caller
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactiveemergencycalls
            
            	This object indicates the number of calls through SBC that have been identified as emergency calls (by Number Analysis)  during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsactiveipv6calls
            
            	This Object indicates the number of calls through SBC that use IPv6 signaling.  This statistic totals all calls that traverse an IPv6 adjacency on either or both sides of SBC during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsaudiotranscodedcalls
            
            	The number of active audio transcoded calls through this adjacency or account during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatscallmediafailure
            
            	This object indicates the number of call setup failures due to media failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallresourcefailure
            
            	This object indicates the number of call setup failures due to resource failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallroutingfailure
            
            	This object indicates the number of call setup failures due to routing failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacbandwidthfailure
            
            	This object indicates the number of call setup failures due to CAC bandwidth limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcaccalllimitfailure
            
            	This object indicates the number of call setup failures due to CAC call limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacmedialimitfailure
            
            	This object indicates the number of call setup failures due to CAC media limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacmediaupdatefailure
            
            	This object indicates the number of call update failure due to policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacpolicyfailure
            
            	This object indicates the number of call setup failures due to CAC policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupcacratelimitfailure
            
            	This object indicates the number of call setup failures due to CAC call rate limit during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetupnapolicyfailure
            
            	This object indicates the number of call setup failures due to NA policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetuppolicyfailure
            
            	This object indicates the number of call setup failures due to some policy violations during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscallsetuproutingpolicyfailure
            
            	This object indicates the number of call setup failures due to routing policy failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscongestionfailure
            
            	This object indicates the number of call setup failures due to congestion during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatscurrenttaps
            
            	This object indicates the Lawful intercept taps currently in place on calls within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: taps
            
            .. attribute:: csbhistorystatsdtmfiw2833calls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via RFC 2833 during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsdtmfiw2833inbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in media via RFC 2833 and DTMF in media via inband DTMF tones during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsdtmfiwinbandcalls
            
            	This object indicates the number of active calls through this adjacency or account for which DTMF interworking is enabled between DTMF in signaling and DTMF in media via inband DTMF tones during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsfailedcallattempts
            
            	This object indicates the number of failed call attempts during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsfailsigfailure
            
            	This object indicates the number of call setup failures due to signaling failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatsfaxtranscodedcalls
            
            	This object indicates the the number of active fax transcoded calls through this adjacency or account during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsimsrxactivecalls
            
            	This object indicates the total number of active calls which use IMS Rx, during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsimsrxcallrenegotiationattempts
            
            	This object indicates the total call renegotiation attempts using IMS Rx during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbhistorystatsimsrxcallrenegotiationfailures
            
            	This object indicates the total call renegotiation failures owing to IMS Rx failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatsimsrxcallsetupfailures
            
            	This object indicates the total call setup failures owing to IMS Rx failure during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatsipseccalls
            
            	The number of active calls on this adjacency or account which are to or from registered subscribers using IPSEC during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsnonsrtpcalls
            
            	This object indicates the number of active calls through this adjacency or account which do not use SRTP on any media channels during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatsrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to RTP being proposed when not permitted during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatssrtpdisallowedfailures
            
            	This object indicates the total call setup failures due to SRTP being proposed when not permitted during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: csbhistorystatssrtpiwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that provide interworking between RTP and SRTP during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatssrtpnoniwcalls
            
            	This object indicates the number of active calls through this adjacency or account that have one or more media channels that use SRTP but no media channels that provide interworking between RTP and SRTP during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatstimestamp
            
            	This object indicates the time at the start of the interval when measurements were first collected for this interval in the csbCurrPeriodicStatsTable
            	**type**\:  str
            
            	**length:** 0..80
            
            .. attribute:: csbhistorystatstotalcallattempts
            
            	This object indicates the number of total call attempts history during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbhistorystatstotalcallupdatefailure
            
            	This object indicates the total call update failures during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistorystatstotaltapsrequested
            
            	This object indicates the lawful intercept tap attempts requested within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: csbhistorystatstotaltapssucceeded
            
            	This object indicates the lawful intercept tap attempts that have been successfully implemented within the scope of this query during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: success
            
            .. attribute:: csbhistroystatstranscodedcalls
            
            	The object indicates the number of active transcoded calls during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: csbhistroystatstransratedcalls
            
            	The object indicates the number of active transrated calls during this interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbhistorystatsinterval = None
                self.csbhistorystatselements = None
                self.csbhistorystatsactivecallfailure = None
                self.csbhistorystatsactivecalls = None
                self.csbhistorystatsactivee2emergencycalls = None
                self.csbhistorystatsactiveemergencycalls = None
                self.csbhistorystatsactiveipv6calls = None
                self.csbhistorystatsaudiotranscodedcalls = None
                self.csbhistorystatscallmediafailure = None
                self.csbhistorystatscallresourcefailure = None
                self.csbhistorystatscallroutingfailure = None
                self.csbhistorystatscallsetupcacbandwidthfailure = None
                self.csbhistorystatscallsetupcaccalllimitfailure = None
                self.csbhistorystatscallsetupcacmedialimitfailure = None
                self.csbhistorystatscallsetupcacmediaupdatefailure = None
                self.csbhistorystatscallsetupcacpolicyfailure = None
                self.csbhistorystatscallsetupcacratelimitfailure = None
                self.csbhistorystatscallsetupnapolicyfailure = None
                self.csbhistorystatscallsetuppolicyfailure = None
                self.csbhistorystatscallsetuproutingpolicyfailure = None
                self.csbhistorystatscongestionfailure = None
                self.csbhistorystatscurrenttaps = None
                self.csbhistorystatsdtmfiw2833calls = None
                self.csbhistorystatsdtmfiw2833inbandcalls = None
                self.csbhistorystatsdtmfiwinbandcalls = None
                self.csbhistorystatsfailedcallattempts = None
                self.csbhistorystatsfailsigfailure = None
                self.csbhistorystatsfaxtranscodedcalls = None
                self.csbhistorystatsimsrxactivecalls = None
                self.csbhistorystatsimsrxcallrenegotiationattempts = None
                self.csbhistorystatsimsrxcallrenegotiationfailures = None
                self.csbhistorystatsimsrxcallsetupfailures = None
                self.csbhistorystatsipseccalls = None
                self.csbhistorystatsnonsrtpcalls = None
                self.csbhistorystatsrtpdisallowedfailures = None
                self.csbhistorystatssrtpdisallowedfailures = None
                self.csbhistorystatssrtpiwcalls = None
                self.csbhistorystatssrtpnoniwcalls = None
                self.csbhistorystatstimestamp = None
                self.csbhistorystatstotalcallattempts = None
                self.csbhistorystatstotalcallupdatefailure = None
                self.csbhistorystatstotaltapsrequested = None
                self.csbhistorystatstotaltapssucceeded = None
                self.csbhistroystatstranscodedcalls = None
                self.csbhistroystatstransratedcalls = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')
                if self.csbhistorystatsinterval is None:
                    raise YPYModelError('Key property csbhistorystatsinterval is None')
                if self.csbhistorystatselements is None:
                    raise YPYModelError('Key property csbhistorystatselements is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbHistoryStatsTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbHistoryStatsEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbHistoryStatsInterval = ' + str(self.csbhistorystatsinterval) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbHistoryStatsElements = ' + str(self.csbhistorystatselements) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbhistorystatsinterval is not None:
                    return True

                if self.csbhistorystatselements is not None:
                    return True

                if self.csbhistorystatsactivecallfailure is not None:
                    return True

                if self.csbhistorystatsactivecalls is not None:
                    return True

                if self.csbhistorystatsactivee2emergencycalls is not None:
                    return True

                if self.csbhistorystatsactiveemergencycalls is not None:
                    return True

                if self.csbhistorystatsactiveipv6calls is not None:
                    return True

                if self.csbhistorystatsaudiotranscodedcalls is not None:
                    return True

                if self.csbhistorystatscallmediafailure is not None:
                    return True

                if self.csbhistorystatscallresourcefailure is not None:
                    return True

                if self.csbhistorystatscallroutingfailure is not None:
                    return True

                if self.csbhistorystatscallsetupcacbandwidthfailure is not None:
                    return True

                if self.csbhistorystatscallsetupcaccalllimitfailure is not None:
                    return True

                if self.csbhistorystatscallsetupcacmedialimitfailure is not None:
                    return True

                if self.csbhistorystatscallsetupcacmediaupdatefailure is not None:
                    return True

                if self.csbhistorystatscallsetupcacpolicyfailure is not None:
                    return True

                if self.csbhistorystatscallsetupcacratelimitfailure is not None:
                    return True

                if self.csbhistorystatscallsetupnapolicyfailure is not None:
                    return True

                if self.csbhistorystatscallsetuppolicyfailure is not None:
                    return True

                if self.csbhistorystatscallsetuproutingpolicyfailure is not None:
                    return True

                if self.csbhistorystatscongestionfailure is not None:
                    return True

                if self.csbhistorystatscurrenttaps is not None:
                    return True

                if self.csbhistorystatsdtmfiw2833calls is not None:
                    return True

                if self.csbhistorystatsdtmfiw2833inbandcalls is not None:
                    return True

                if self.csbhistorystatsdtmfiwinbandcalls is not None:
                    return True

                if self.csbhistorystatsfailedcallattempts is not None:
                    return True

                if self.csbhistorystatsfailsigfailure is not None:
                    return True

                if self.csbhistorystatsfaxtranscodedcalls is not None:
                    return True

                if self.csbhistorystatsimsrxactivecalls is not None:
                    return True

                if self.csbhistorystatsimsrxcallrenegotiationattempts is not None:
                    return True

                if self.csbhistorystatsimsrxcallrenegotiationfailures is not None:
                    return True

                if self.csbhistorystatsimsrxcallsetupfailures is not None:
                    return True

                if self.csbhistorystatsipseccalls is not None:
                    return True

                if self.csbhistorystatsnonsrtpcalls is not None:
                    return True

                if self.csbhistorystatsrtpdisallowedfailures is not None:
                    return True

                if self.csbhistorystatssrtpdisallowedfailures is not None:
                    return True

                if self.csbhistorystatssrtpiwcalls is not None:
                    return True

                if self.csbhistorystatssrtpnoniwcalls is not None:
                    return True

                if self.csbhistorystatstimestamp is not None:
                    return True

                if self.csbhistorystatstotalcallattempts is not None:
                    return True

                if self.csbhistorystatstotalcallupdatefailure is not None:
                    return True

                if self.csbhistorystatstotaltapsrequested is not None:
                    return True

                if self.csbhistorystatstotaltapssucceeded is not None:
                    return True

                if self.csbhistroystatstranscodedcalls is not None:
                    return True

                if self.csbhistroystatstransratedcalls is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbHistoryStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbhistorystatsentry is not None:
                for child_ref in self.csbhistorystatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable']['meta_info']


    class Csbperflowstatstable(object):
        """
        This table describes statistics table for each call flow. The
        indices of the table are virtual media gateway id, gate id,
        falow pair id and side id (indices for side A or side B). The
        other indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        .. attribute:: csbperflowstatsentry
        
        	An conceptual row in the csbPerFlowStatsTable. There is an entry in this table for vdbe Id, gate id, flow pair id and side id. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbperflowstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbperflowstatsentry = YList()
            self.csbperflowstatsentry.parent = self
            self.csbperflowstatsentry.name = 'csbperflowstatsentry'


        class Csbperflowstatsentry(object):
            """
            An conceptual row in the csbPerFlowStatsTable. There is
            an entry in this table for vdbe Id, gate id, flow pair id and
            side id. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbperflowstatsvdbeid  <key>
            
            	This object identifies the virtual media gateway id. This object also acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: csbperflowstatsgateid  <key>
            
            	This object identifies the gate id. This object also acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: csbperflowstatsflowpairid  <key>
            
            	This object identifies the flow pair id. This object also acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: csbperflowstatssideid  <key>
            
            	This object identifies the index corresponding to side of flow pair either side A or side B. This object also acts as an index for the table
            	**type**\:   :py:class:`CsbperflowstatssideidEnum <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatssideidEnum>`
            
            .. attribute:: csbperflowstatsadrstatus
            
            	This object indicates whether the flow on the current FlowPair has subscribed for the NAT latch event
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: csbperflowstatsdscpsettings
            
            	This object indicates the mark packets sent for the current FlowPair with, or zero if none set. The DSCP is a 6\-bit value, which will be present in the top 6 bits of the lowest byte of this field
            	**type**\:  str
            
            .. attribute:: csbperflowstatsepjitter
            
            	This object indicates the End Point jitter per flow in the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: milliseconds
            
            .. attribute:: csbperflowstatsflowtype
            
            	This object indicates the type of the flow, like media flow, signaling flow etc
            	**type**\:   :py:class:`CsbperflowstatsflowtypeEnum <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatsflowtypeEnum>`
            
            .. attribute:: csbperflowstatsqasettings
            
            	This object indicates the flow on the current FlowPair has subscribed for the media loss event
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: csbperflowstatsrtcppktslost
            
            	The number of RTP packets reported as lost by the remote end point on this flow. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtcppktsrcvd
            
            	The number of RTP packets received by the remote end point from this MG on this flow. Comparing this with the local number of RTP packets sent from this MG to the remote endpoint gives an indication of how many outgoing packets were dropped on this leg of the call. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtcppktssent
            
            	The number of RTP packets sent by the remote end point to this MG on this flow. Comparing this with the local number of RTP packets received from the remote end point gives an indication of how many incoming  packets were dropped on this leg of the call. This information is from RTCP packet. Not all endpoints report this statistic, if it is not available it will be set to zero. This statistic will not be available for signaling flows
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtpoctetsdiscard
            
            	This object indicates the number of RTP octets discarded per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtpoctetsrcvd
            
            	This object indicates the number of RTP octets received per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtpoctetssent
            
            	This object indicates the number of RTP octets sent per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets
            
            .. attribute:: csbperflowstatsrtppktsdiscard
            
            	This object indicates the number of RTP packets discarded  per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtppktslost
            
            	This object indicates the number of RTP packets lost per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtppktsrcvd
            
            	This object indicates the number of RTP packets received per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatsrtppktssent
            
            	This object indicates the number of RTP packets sent per flow by the SBC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbperflowstatstmanpermbs
            
            	This object indicates the maximum burst size for the current FlowPair
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: csbperflowstatstmanpersdr
            
            	This object indicates the bandwidth reserved for flow in kilobytes/second
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobytes per second
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbperflowstatsvdbeid = None
                self.csbperflowstatsgateid = None
                self.csbperflowstatsflowpairid = None
                self.csbperflowstatssideid = None
                self.csbperflowstatsadrstatus = None
                self.csbperflowstatsdscpsettings = None
                self.csbperflowstatsepjitter = None
                self.csbperflowstatsflowtype = None
                self.csbperflowstatsqasettings = None
                self.csbperflowstatsrtcppktslost = None
                self.csbperflowstatsrtcppktsrcvd = None
                self.csbperflowstatsrtcppktssent = None
                self.csbperflowstatsrtpoctetsdiscard = None
                self.csbperflowstatsrtpoctetsrcvd = None
                self.csbperflowstatsrtpoctetssent = None
                self.csbperflowstatsrtppktsdiscard = None
                self.csbperflowstatsrtppktslost = None
                self.csbperflowstatsrtppktsrcvd = None
                self.csbperflowstatsrtppktssent = None
                self.csbperflowstatstmanpermbs = None
                self.csbperflowstatstmanpersdr = None

            class CsbperflowstatsflowtypeEnum(Enum):
                """
                CsbperflowstatsflowtypeEnum

                This object indicates the type of the flow, like media flow,

                signaling flow etc.

                .. data:: media = 1

                .. data:: signalling = 2

                """

                media = 1

                signalling = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                    return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatsflowtypeEnum']


            class CsbperflowstatssideidEnum(Enum):
                """
                CsbperflowstatssideidEnum

                This object identifies the index corresponding to side of flow

                pair either side A or side B. This object also acts as an index

                for the table.

                .. data:: sideA = 1

                .. data:: sideB = 2

                """

                sideA = 1

                sideB = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                    return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatssideidEnum']


            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')
                if self.csbperflowstatsvdbeid is None:
                    raise YPYModelError('Key property csbperflowstatsvdbeid is None')
                if self.csbperflowstatsgateid is None:
                    raise YPYModelError('Key property csbperflowstatsgateid is None')
                if self.csbperflowstatsflowpairid is None:
                    raise YPYModelError('Key property csbperflowstatsflowpairid is None')
                if self.csbperflowstatssideid is None:
                    raise YPYModelError('Key property csbperflowstatssideid is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsVdbeId = ' + str(self.csbperflowstatsvdbeid) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsGateId = ' + str(self.csbperflowstatsgateid) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsFlowPairId = ' + str(self.csbperflowstatsflowpairid) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsSideId = ' + str(self.csbperflowstatssideid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbperflowstatsvdbeid is not None:
                    return True

                if self.csbperflowstatsgateid is not None:
                    return True

                if self.csbperflowstatsflowpairid is not None:
                    return True

                if self.csbperflowstatssideid is not None:
                    return True

                if self.csbperflowstatsadrstatus is not None:
                    return True

                if self.csbperflowstatsdscpsettings is not None:
                    return True

                if self.csbperflowstatsepjitter is not None:
                    return True

                if self.csbperflowstatsflowtype is not None:
                    return True

                if self.csbperflowstatsqasettings is not None:
                    return True

                if self.csbperflowstatsrtcppktslost is not None:
                    return True

                if self.csbperflowstatsrtcppktsrcvd is not None:
                    return True

                if self.csbperflowstatsrtcppktssent is not None:
                    return True

                if self.csbperflowstatsrtpoctetsdiscard is not None:
                    return True

                if self.csbperflowstatsrtpoctetsrcvd is not None:
                    return True

                if self.csbperflowstatsrtpoctetssent is not None:
                    return True

                if self.csbperflowstatsrtppktsdiscard is not None:
                    return True

                if self.csbperflowstatsrtppktslost is not None:
                    return True

                if self.csbperflowstatsrtppktsrcvd is not None:
                    return True

                if self.csbperflowstatsrtppktssent is not None:
                    return True

                if self.csbperflowstatstmanpermbs is not None:
                    return True

                if self.csbperflowstatstmanpersdr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbPerFlowStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbperflowstatsentry is not None:
                for child_ref in self.csbperflowstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable']['meta_info']


    class Csbh248Statstable(object):
        """
        This table describes the H.248 statistics for SBC. The index of
        the table is service index which corresponds to a particular 
        service configured on the SBC and the index assigned to a
        particular H.248 controller. The other index of this table is
        csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
        This table is replaced by the csbH248StatsRev1Table.
        
        .. attribute:: csbh248statsentry
        
        	An conceptual row in the csbCallStath248Table. There is an entry in this table for the particular controller by a value of csbH248StatsCtrlrIndex. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbh248Statsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbh248statsentry = YList()
            self.csbh248statsentry.parent = self
            self.csbh248statsentry.name = 'csbh248statsentry'


        class Csbh248Statsentry(object):
            """
            An conceptual row in the csbCallStath248Table. There is
            an entry in this table for the particular controller by a value
            of csbH248StatsCtrlrIndex. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbh248statsctrlrindex  <key>
            
            	This object identifies the controller index of the H.248 server. This is also the index for the table
            	**type**\:  int
            
            	**range:** 1..50
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsestablishedtime
            
            	This object indicates the H.248 Controller established time (the time at which the association became established)
            	**type**\:  str
            
            	**length:** 0..80
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statslt
            
            	This object indicates the LT value calculated from RTT value and Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC plus the maximum round trip propagation delay in the network (in milliseconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliesrcvd
            
            	This object indicates the number of replies received from the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliesretried
            
            	This object indicates the number of replies retried through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrepliessent
            
            	This object indicates the number of replies sent through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsfailed
            
            	This object indicates the requests failed on session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsrcvd
            
            	This object indicates the requests received through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestsretried
            
            	This object indicates the requests retried through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrequestssent
            
            	This object indicates the requests sent through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statsrtt
            
            	This object indicates the calculated RTT value. This field specifies the maximum round trip propagation delay in the  network (in milliseconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statssegpktsrcvd
            
            	This object indicates the number of packets received from the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statssegpktssent
            
            	This object indicates the number of packets sent through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: csbh248statstmaxtimeoutval
            
            	This object indicates the T\-Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC before deciding that the request has failed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbh248statsctrlrindex = None
                self.csbh248statsestablishedtime = None
                self.csbh248statslt = None
                self.csbh248statsrepliesrcvd = None
                self.csbh248statsrepliesretried = None
                self.csbh248statsrepliessent = None
                self.csbh248statsrequestsfailed = None
                self.csbh248statsrequestsrcvd = None
                self.csbh248statsrequestsretried = None
                self.csbh248statsrequestssent = None
                self.csbh248statsrtt = None
                self.csbh248statssegpktsrcvd = None
                self.csbh248statssegpktssent = None
                self.csbh248statstmaxtimeoutval = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')
                if self.csbh248statsctrlrindex is None:
                    raise YPYModelError('Key property csbh248statsctrlrindex is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsTable/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsEntry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsCtrlrIndex = ' + str(self.csbh248statsctrlrindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbh248statsctrlrindex is not None:
                    return True

                if self.csbh248statsestablishedtime is not None:
                    return True

                if self.csbh248statslt is not None:
                    return True

                if self.csbh248statsrepliesrcvd is not None:
                    return True

                if self.csbh248statsrepliesretried is not None:
                    return True

                if self.csbh248statsrepliessent is not None:
                    return True

                if self.csbh248statsrequestsfailed is not None:
                    return True

                if self.csbh248statsrequestsrcvd is not None:
                    return True

                if self.csbh248statsrequestsretried is not None:
                    return True

                if self.csbh248statsrequestssent is not None:
                    return True

                if self.csbh248statsrtt is not None:
                    return True

                if self.csbh248statssegpktsrcvd is not None:
                    return True

                if self.csbh248statssegpktssent is not None:
                    return True

                if self.csbh248statstmaxtimeoutval is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbh248statsentry is not None:
                for child_ref in self.csbh248statsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable']['meta_info']


    class Csbh248Statsrev1Table(object):
        """
        This table describes the H.248 statistics for SBC. The index of
        the table is service index which corresponds to a particular 
        service configured on the SBC and the index assigned to a
        particular H.248 controller. The other index of this table is
        csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
        
        .. attribute:: csbh248statsrev1entry
        
        	An conceptual row in the csbCallStath248Table. There is an entry in this table for the particular Vdbe by a value of csbH248StatsVdbeId. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbh248Statsrev1Entry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            self.parent = None
            self.csbh248statsrev1entry = YList()
            self.csbh248statsrev1entry.parent = self
            self.csbh248statsrev1entry.name = 'csbh248statsrev1entry'


        class Csbh248Statsrev1Entry(object):
            """
            An conceptual row in the csbCallStath248Table. There is
            an entry in this table for the particular Vdbe by a value
            of csbH248StatsVdbeId. The other indices of this table are
            csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
            and csbCallStatsServiceIndex defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbh248statsvdbeid  <key>
            
            	This object identifies the virtual media gateway id. This is also the index for the table
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: csbh248statsestablishedtimerev1
            
            	This object indicates the H.248 Controller established time (the time at which the association became established)
            	**type**\:  str
            
            	**length:** 0..80
            
            .. attribute:: csbh248statsltrev1
            
            	This object indicates the LT value calculated from RTT value and Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC plus the maximum round trip propagation delay in the network (in milliseconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: csbh248statsrepliesrcvdrev1
            
            	This object indicates the number of replies received from the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrepliesretriedrev1
            
            	This object indicates the number of replies retried through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrepliessentrev1
            
            	This object indicates the number of replies sent through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsfailedrev1
            
            	This object indicates the requests failed on session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsrcvdrev1
            
            	This object indicates the requests received through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestsretriedrev1
            
            	This object indicates the requests retried through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrequestssentrev1
            
            	This object indicates the requests sent through the Session Controller Interface to an SBE or DBE
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statsrttrev1
            
            	This object indicates the calculated RTT value. This field specifies the maximum round trip propagation delay in the  network (in milliseconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: csbh248statssegpktsrcvdrev1
            
            	This object indicates the number of response segments received by DBE. This field will only be present if segmentation is enabled on this association
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statssegpktssentrev1
            
            	This object indicates the number of response segments sent by DBE. This field will only be present if segmentation is enabled on this association
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbh248statstmaxtimeoutvalrev1
            
            	This object indicates the T\-Max timeout value. This field specifies the maximum delay (in milliseconds) for a response from an MGC before deciding that the request has failed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
            _revision = '2010-09-03'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbh248statsvdbeid = None
                self.csbh248statsestablishedtimerev1 = None
                self.csbh248statsltrev1 = None
                self.csbh248statsrepliesrcvdrev1 = None
                self.csbh248statsrepliesretriedrev1 = None
                self.csbh248statsrepliessentrev1 = None
                self.csbh248statsrequestsfailedrev1 = None
                self.csbh248statsrequestsrcvdrev1 = None
                self.csbh248statsrequestsretriedrev1 = None
                self.csbh248statsrequestssentrev1 = None
                self.csbh248statsrttrev1 = None
                self.csbh248statssegpktsrcvdrev1 = None
                self.csbh248statssegpktssentrev1 = None
                self.csbh248statstmaxtimeoutvalrev1 = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYModelError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYModelError('Key property csbcallstatsserviceindex is None')
                if self.csbh248statsvdbeid is None:
                    raise YPYModelError('Key property csbh248statsvdbeid is None')

                return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsRev1Table/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsRev1Entry[CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsVdbeId = ' + str(self.csbh248statsvdbeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbh248statsvdbeid is not None:
                    return True

                if self.csbh248statsestablishedtimerev1 is not None:
                    return True

                if self.csbh248statsltrev1 is not None:
                    return True

                if self.csbh248statsrepliesrcvdrev1 is not None:
                    return True

                if self.csbh248statsrepliesretriedrev1 is not None:
                    return True

                if self.csbh248statsrepliessentrev1 is not None:
                    return True

                if self.csbh248statsrequestsfailedrev1 is not None:
                    return True

                if self.csbh248statsrequestsrcvdrev1 is not None:
                    return True

                if self.csbh248statsrequestsretriedrev1 is not None:
                    return True

                if self.csbh248statsrequestssentrev1 is not None:
                    return True

                if self.csbh248statsrttrev1 is not None:
                    return True

                if self.csbh248statssegpktsrcvdrev1 is not None:
                    return True

                if self.csbh248statssegpktssentrev1 is not None:
                    return True

                if self.csbh248statstmaxtimeoutvalrev1 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
                return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:csbH248StatsRev1Table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.csbh248statsrev1entry is not None:
                for child_ref in self.csbh248statsrev1entry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
            return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.csbcallstatsinstancetable is not None and self.csbcallstatsinstancetable._has_data():
            return True

        if self.csbcallstatstable is not None and self.csbcallstatstable._has_data():
            return True

        if self.csbcurrperiodicstatstable is not None and self.csbcurrperiodicstatstable._has_data():
            return True

        if self.csbh248statsrev1table is not None and self.csbh248statsrev1table._has_data():
            return True

        if self.csbh248statstable is not None and self.csbh248statstable._has_data():
            return True

        if self.csbhistorystatstable is not None and self.csbhistorystatstable._has_data():
            return True

        if self.csbperflowstatstable is not None and self.csbperflowstatstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB as meta
        return meta._meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']


