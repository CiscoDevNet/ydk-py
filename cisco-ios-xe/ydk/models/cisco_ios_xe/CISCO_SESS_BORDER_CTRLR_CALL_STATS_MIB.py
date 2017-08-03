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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscosbcperiodicstatsinterval(Enum):
    """
    Ciscosbcperiodicstatsinterval

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



class CiscoSessBorderCtrlrCallStatsMib(Entity):
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
        super(CiscoSessBorderCtrlrCallStatsMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"
        self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

        self.csbcallstatsinstancetable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable()
        self.csbcallstatsinstancetable.parent = self
        self._children_name_map["csbcallstatsinstancetable"] = "csbCallStatsInstanceTable"
        self._children_yang_names.add("csbCallStatsInstanceTable")

        self.csbcallstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable()
        self.csbcallstatstable.parent = self
        self._children_name_map["csbcallstatstable"] = "csbCallStatsTable"
        self._children_yang_names.add("csbCallStatsTable")

        self.csbcurrperiodicstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable()
        self.csbcurrperiodicstatstable.parent = self
        self._children_name_map["csbcurrperiodicstatstable"] = "csbCurrPeriodicStatsTable"
        self._children_yang_names.add("csbCurrPeriodicStatsTable")

        self.csbh248statsrev1table = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table()
        self.csbh248statsrev1table.parent = self
        self._children_name_map["csbh248statsrev1table"] = "csbH248StatsRev1Table"
        self._children_yang_names.add("csbH248StatsRev1Table")

        self.csbh248statstable = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable()
        self.csbh248statstable.parent = self
        self._children_name_map["csbh248statstable"] = "csbH248StatsTable"
        self._children_yang_names.add("csbH248StatsTable")

        self.csbhistorystatstable = CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable()
        self.csbhistorystatstable.parent = self
        self._children_name_map["csbhistorystatstable"] = "csbHistoryStatsTable"
        self._children_yang_names.add("csbHistoryStatsTable")

        self.csbperflowstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable()
        self.csbperflowstatstable.parent = self
        self._children_name_map["csbperflowstatstable"] = "csbPerFlowStatsTable"
        self._children_yang_names.add("csbPerFlowStatsTable")


    class Csbcallstatsinstancetable(Entity):
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
            super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable, self).__init__()

            self.yang_name = "csbCallStatsInstanceTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbcallstatsinstanceentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable, self).__setattr__(name, value)


        class Csbcallstatsinstanceentry(Entity):
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry, self).__init__()

                self.yang_name = "csbCallStatsInstanceEntry"
                self.yang_parent_name = "csbCallStatsInstanceTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.uint32, "csbCallStatsInstanceIndex")

                self.csbcallstatsinstancephysicalindex = YLeaf(YType.int32, "csbCallStatsInstancePhysicalIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsinstancephysicalindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsinstancephysicalindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsinstancephysicalindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbCallStatsInstanceEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCallStatsInstanceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsinstancephysicalindex.is_set or self.csbcallstatsinstancephysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstancephysicalindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsInstancePhysicalIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsInstancePhysicalIndex"):
                    self.csbcallstatsinstancephysicalindex = value
                    self.csbcallstatsinstancephysicalindex.value_namespace = name_space
                    self.csbcallstatsinstancephysicalindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbcallstatsinstanceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbcallstatsinstanceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbCallStatsInstanceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbCallStatsInstanceEntry"):
                for c in self.csbcallstatsinstanceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbcallstatsinstanceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbCallStatsInstanceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csbcallstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable, self).__init__()

            self.yang_name = "csbCallStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbcallstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable, self).__setattr__(name, value)


        class Csbcallstatsentry(Entity):
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry, self).__init__()

                self.yang_name = "csbCallStatsEntry"
                self.yang_parent_name = "csbCallStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.uint32, "csbCallStatsServiceIndex")

                self.csbcallstatsactivetranscodeflows = YLeaf(YType.uint32, "csbCallStatsActiveTranscodeFlows")

                self.csbcallstatsavailableflows = YLeaf(YType.uint32, "csbCallStatsAvailableFlows")

                self.csbcallstatsavailablepktrate = YLeaf(YType.uint32, "csbCallStatsAvailablePktRate")

                self.csbcallstatsavailabletranscodeflows = YLeaf(YType.uint32, "csbCallStatsAvailableTranscodeFlows")

                self.csbcallstatscallshigh = YLeaf(YType.uint32, "csbCallStatsCallsHigh")

                self.csbcallstatscallslow = YLeaf(YType.uint32, "csbCallStatsCallsLow")

                self.csbcallstatsnomediacount = YLeaf(YType.uint32, "csbCallStatsNoMediaCount")

                self.csbcallstatspeakflows = YLeaf(YType.uint32, "csbCallStatsPeakFlows")

                self.csbcallstatspeaksigflows = YLeaf(YType.uint32, "csbCallStatsPeakSigFlows")

                self.csbcallstatspeaktranscodeflows = YLeaf(YType.uint32, "csbCallStatsPeakTranscodeFlows")

                self.csbcallstatsrate1sec = YLeaf(YType.uint32, "csbCallStatsRate1Sec")

                self.csbcallstatsrouteerrors = YLeaf(YType.uint32, "csbCallStatsRouteErrors")

                self.csbcallstatsrtpoctetsdiscard = YLeaf(YType.uint64, "csbCallStatsRTPOctetsDiscard")

                self.csbcallstatsrtpoctetsrcvd = YLeaf(YType.uint64, "csbCallStatsRTPOctetsRcvd")

                self.csbcallstatsrtpoctetssent = YLeaf(YType.uint64, "csbCallStatsRTPOctetsSent")

                self.csbcallstatsrtppktsdiscard = YLeaf(YType.uint64, "csbCallStatsRTPPktsDiscard")

                self.csbcallstatsrtppktsrcvd = YLeaf(YType.uint64, "csbCallStatsRTPPktsRcvd")

                self.csbcallstatsrtppktssent = YLeaf(YType.uint64, "csbCallStatsRTPPktsSent")

                self.csbcallstatssbcname = YLeaf(YType.str, "csbCallStatsSbcName")

                self.csbcallstatstotalflows = YLeaf(YType.uint32, "csbCallStatsTotalFlows")

                self.csbcallstatstotalsigflows = YLeaf(YType.uint32, "csbCallStatsTotalSigFlows")

                self.csbcallstatstotaltranscodeflows = YLeaf(YType.uint32, "csbCallStatsTotalTranscodeFlows")

                self.csbcallstatsunclassifiedpkts = YLeaf(YType.uint64, "csbCallStatsUnclassifiedPkts")

                self.csbcallstatsusedflows = YLeaf(YType.uint32, "csbCallStatsUsedFlows")

                self.csbcallstatsusedsigflows = YLeaf(YType.uint32, "csbCallStatsUsedSigFlows")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbcallstatsactivetranscodeflows",
                                "csbcallstatsavailableflows",
                                "csbcallstatsavailablepktrate",
                                "csbcallstatsavailabletranscodeflows",
                                "csbcallstatscallshigh",
                                "csbcallstatscallslow",
                                "csbcallstatsnomediacount",
                                "csbcallstatspeakflows",
                                "csbcallstatspeaksigflows",
                                "csbcallstatspeaktranscodeflows",
                                "csbcallstatsrate1sec",
                                "csbcallstatsrouteerrors",
                                "csbcallstatsrtpoctetsdiscard",
                                "csbcallstatsrtpoctetsrcvd",
                                "csbcallstatsrtpoctetssent",
                                "csbcallstatsrtppktsdiscard",
                                "csbcallstatsrtppktsrcvd",
                                "csbcallstatsrtppktssent",
                                "csbcallstatssbcname",
                                "csbcallstatstotalflows",
                                "csbcallstatstotalsigflows",
                                "csbcallstatstotaltranscodeflows",
                                "csbcallstatsunclassifiedpkts",
                                "csbcallstatsusedflows",
                                "csbcallstatsusedsigflows") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbcallstatsactivetranscodeflows.is_set or
                    self.csbcallstatsavailableflows.is_set or
                    self.csbcallstatsavailablepktrate.is_set or
                    self.csbcallstatsavailabletranscodeflows.is_set or
                    self.csbcallstatscallshigh.is_set or
                    self.csbcallstatscallslow.is_set or
                    self.csbcallstatsnomediacount.is_set or
                    self.csbcallstatspeakflows.is_set or
                    self.csbcallstatspeaksigflows.is_set or
                    self.csbcallstatspeaktranscodeflows.is_set or
                    self.csbcallstatsrate1sec.is_set or
                    self.csbcallstatsrouteerrors.is_set or
                    self.csbcallstatsrtpoctetsdiscard.is_set or
                    self.csbcallstatsrtpoctetsrcvd.is_set or
                    self.csbcallstatsrtpoctetssent.is_set or
                    self.csbcallstatsrtppktsdiscard.is_set or
                    self.csbcallstatsrtppktsrcvd.is_set or
                    self.csbcallstatsrtppktssent.is_set or
                    self.csbcallstatssbcname.is_set or
                    self.csbcallstatstotalflows.is_set or
                    self.csbcallstatstotalsigflows.is_set or
                    self.csbcallstatstotaltranscodeflows.is_set or
                    self.csbcallstatsunclassifiedpkts.is_set or
                    self.csbcallstatsusedflows.is_set or
                    self.csbcallstatsusedsigflows.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsactivetranscodeflows.yfilter != YFilter.not_set or
                    self.csbcallstatsavailableflows.yfilter != YFilter.not_set or
                    self.csbcallstatsavailablepktrate.yfilter != YFilter.not_set or
                    self.csbcallstatsavailabletranscodeflows.yfilter != YFilter.not_set or
                    self.csbcallstatscallshigh.yfilter != YFilter.not_set or
                    self.csbcallstatscallslow.yfilter != YFilter.not_set or
                    self.csbcallstatsnomediacount.yfilter != YFilter.not_set or
                    self.csbcallstatspeakflows.yfilter != YFilter.not_set or
                    self.csbcallstatspeaksigflows.yfilter != YFilter.not_set or
                    self.csbcallstatspeaktranscodeflows.yfilter != YFilter.not_set or
                    self.csbcallstatsrate1sec.yfilter != YFilter.not_set or
                    self.csbcallstatsrouteerrors.yfilter != YFilter.not_set or
                    self.csbcallstatsrtpoctetsdiscard.yfilter != YFilter.not_set or
                    self.csbcallstatsrtpoctetsrcvd.yfilter != YFilter.not_set or
                    self.csbcallstatsrtpoctetssent.yfilter != YFilter.not_set or
                    self.csbcallstatsrtppktsdiscard.yfilter != YFilter.not_set or
                    self.csbcallstatsrtppktsrcvd.yfilter != YFilter.not_set or
                    self.csbcallstatsrtppktssent.yfilter != YFilter.not_set or
                    self.csbcallstatssbcname.yfilter != YFilter.not_set or
                    self.csbcallstatstotalflows.yfilter != YFilter.not_set or
                    self.csbcallstatstotalsigflows.yfilter != YFilter.not_set or
                    self.csbcallstatstotaltranscodeflows.yfilter != YFilter.not_set or
                    self.csbcallstatsunclassifiedpkts.yfilter != YFilter.not_set or
                    self.csbcallstatsusedflows.yfilter != YFilter.not_set or
                    self.csbcallstatsusedsigflows.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbCallStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCallStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbcallstatsactivetranscodeflows.is_set or self.csbcallstatsactivetranscodeflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsactivetranscodeflows.get_name_leafdata())
                if (self.csbcallstatsavailableflows.is_set or self.csbcallstatsavailableflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsavailableflows.get_name_leafdata())
                if (self.csbcallstatsavailablepktrate.is_set or self.csbcallstatsavailablepktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsavailablepktrate.get_name_leafdata())
                if (self.csbcallstatsavailabletranscodeflows.is_set or self.csbcallstatsavailabletranscodeflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsavailabletranscodeflows.get_name_leafdata())
                if (self.csbcallstatscallshigh.is_set or self.csbcallstatscallshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatscallshigh.get_name_leafdata())
                if (self.csbcallstatscallslow.is_set or self.csbcallstatscallslow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatscallslow.get_name_leafdata())
                if (self.csbcallstatsnomediacount.is_set or self.csbcallstatsnomediacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsnomediacount.get_name_leafdata())
                if (self.csbcallstatspeakflows.is_set or self.csbcallstatspeakflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatspeakflows.get_name_leafdata())
                if (self.csbcallstatspeaksigflows.is_set or self.csbcallstatspeaksigflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatspeaksigflows.get_name_leafdata())
                if (self.csbcallstatspeaktranscodeflows.is_set or self.csbcallstatspeaktranscodeflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatspeaktranscodeflows.get_name_leafdata())
                if (self.csbcallstatsrate1sec.is_set or self.csbcallstatsrate1sec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrate1sec.get_name_leafdata())
                if (self.csbcallstatsrouteerrors.is_set or self.csbcallstatsrouteerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrouteerrors.get_name_leafdata())
                if (self.csbcallstatsrtpoctetsdiscard.is_set or self.csbcallstatsrtpoctetsdiscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtpoctetsdiscard.get_name_leafdata())
                if (self.csbcallstatsrtpoctetsrcvd.is_set or self.csbcallstatsrtpoctetsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtpoctetsrcvd.get_name_leafdata())
                if (self.csbcallstatsrtpoctetssent.is_set or self.csbcallstatsrtpoctetssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtpoctetssent.get_name_leafdata())
                if (self.csbcallstatsrtppktsdiscard.is_set or self.csbcallstatsrtppktsdiscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtppktsdiscard.get_name_leafdata())
                if (self.csbcallstatsrtppktsrcvd.is_set or self.csbcallstatsrtppktsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtppktsrcvd.get_name_leafdata())
                if (self.csbcallstatsrtppktssent.is_set or self.csbcallstatsrtppktssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsrtppktssent.get_name_leafdata())
                if (self.csbcallstatssbcname.is_set or self.csbcallstatssbcname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatssbcname.get_name_leafdata())
                if (self.csbcallstatstotalflows.is_set or self.csbcallstatstotalflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatstotalflows.get_name_leafdata())
                if (self.csbcallstatstotalsigflows.is_set or self.csbcallstatstotalsigflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatstotalsigflows.get_name_leafdata())
                if (self.csbcallstatstotaltranscodeflows.is_set or self.csbcallstatstotaltranscodeflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatstotaltranscodeflows.get_name_leafdata())
                if (self.csbcallstatsunclassifiedpkts.is_set or self.csbcallstatsunclassifiedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsunclassifiedpkts.get_name_leafdata())
                if (self.csbcallstatsusedflows.is_set or self.csbcallstatsusedflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsusedflows.get_name_leafdata())
                if (self.csbcallstatsusedsigflows.is_set or self.csbcallstatsusedsigflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsusedsigflows.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbCallStatsActiveTranscodeFlows" or name == "csbCallStatsAvailableFlows" or name == "csbCallStatsAvailablePktRate" or name == "csbCallStatsAvailableTranscodeFlows" or name == "csbCallStatsCallsHigh" or name == "csbCallStatsCallsLow" or name == "csbCallStatsNoMediaCount" or name == "csbCallStatsPeakFlows" or name == "csbCallStatsPeakSigFlows" or name == "csbCallStatsPeakTranscodeFlows" or name == "csbCallStatsRate1Sec" or name == "csbCallStatsRouteErrors" or name == "csbCallStatsRTPOctetsDiscard" or name == "csbCallStatsRTPOctetsRcvd" or name == "csbCallStatsRTPOctetsSent" or name == "csbCallStatsRTPPktsDiscard" or name == "csbCallStatsRTPPktsRcvd" or name == "csbCallStatsRTPPktsSent" or name == "csbCallStatsSbcName" or name == "csbCallStatsTotalFlows" or name == "csbCallStatsTotalSigFlows" or name == "csbCallStatsTotalTranscodeFlows" or name == "csbCallStatsUnclassifiedPkts" or name == "csbCallStatsUsedFlows" or name == "csbCallStatsUsedSigFlows"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsActiveTranscodeFlows"):
                    self.csbcallstatsactivetranscodeflows = value
                    self.csbcallstatsactivetranscodeflows.value_namespace = name_space
                    self.csbcallstatsactivetranscodeflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsAvailableFlows"):
                    self.csbcallstatsavailableflows = value
                    self.csbcallstatsavailableflows.value_namespace = name_space
                    self.csbcallstatsavailableflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsAvailablePktRate"):
                    self.csbcallstatsavailablepktrate = value
                    self.csbcallstatsavailablepktrate.value_namespace = name_space
                    self.csbcallstatsavailablepktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsAvailableTranscodeFlows"):
                    self.csbcallstatsavailabletranscodeflows = value
                    self.csbcallstatsavailabletranscodeflows.value_namespace = name_space
                    self.csbcallstatsavailabletranscodeflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsCallsHigh"):
                    self.csbcallstatscallshigh = value
                    self.csbcallstatscallshigh.value_namespace = name_space
                    self.csbcallstatscallshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsCallsLow"):
                    self.csbcallstatscallslow = value
                    self.csbcallstatscallslow.value_namespace = name_space
                    self.csbcallstatscallslow.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsNoMediaCount"):
                    self.csbcallstatsnomediacount = value
                    self.csbcallstatsnomediacount.value_namespace = name_space
                    self.csbcallstatsnomediacount.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsPeakFlows"):
                    self.csbcallstatspeakflows = value
                    self.csbcallstatspeakflows.value_namespace = name_space
                    self.csbcallstatspeakflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsPeakSigFlows"):
                    self.csbcallstatspeaksigflows = value
                    self.csbcallstatspeaksigflows.value_namespace = name_space
                    self.csbcallstatspeaksigflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsPeakTranscodeFlows"):
                    self.csbcallstatspeaktranscodeflows = value
                    self.csbcallstatspeaktranscodeflows.value_namespace = name_space
                    self.csbcallstatspeaktranscodeflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRate1Sec"):
                    self.csbcallstatsrate1sec = value
                    self.csbcallstatsrate1sec.value_namespace = name_space
                    self.csbcallstatsrate1sec.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRouteErrors"):
                    self.csbcallstatsrouteerrors = value
                    self.csbcallstatsrouteerrors.value_namespace = name_space
                    self.csbcallstatsrouteerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPOctetsDiscard"):
                    self.csbcallstatsrtpoctetsdiscard = value
                    self.csbcallstatsrtpoctetsdiscard.value_namespace = name_space
                    self.csbcallstatsrtpoctetsdiscard.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPOctetsRcvd"):
                    self.csbcallstatsrtpoctetsrcvd = value
                    self.csbcallstatsrtpoctetsrcvd.value_namespace = name_space
                    self.csbcallstatsrtpoctetsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPOctetsSent"):
                    self.csbcallstatsrtpoctetssent = value
                    self.csbcallstatsrtpoctetssent.value_namespace = name_space
                    self.csbcallstatsrtpoctetssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPPktsDiscard"):
                    self.csbcallstatsrtppktsdiscard = value
                    self.csbcallstatsrtppktsdiscard.value_namespace = name_space
                    self.csbcallstatsrtppktsdiscard.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPPktsRcvd"):
                    self.csbcallstatsrtppktsrcvd = value
                    self.csbcallstatsrtppktsrcvd.value_namespace = name_space
                    self.csbcallstatsrtppktsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsRTPPktsSent"):
                    self.csbcallstatsrtppktssent = value
                    self.csbcallstatsrtppktssent.value_namespace = name_space
                    self.csbcallstatsrtppktssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsSbcName"):
                    self.csbcallstatssbcname = value
                    self.csbcallstatssbcname.value_namespace = name_space
                    self.csbcallstatssbcname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsTotalFlows"):
                    self.csbcallstatstotalflows = value
                    self.csbcallstatstotalflows.value_namespace = name_space
                    self.csbcallstatstotalflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsTotalSigFlows"):
                    self.csbcallstatstotalsigflows = value
                    self.csbcallstatstotalsigflows.value_namespace = name_space
                    self.csbcallstatstotalsigflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsTotalTranscodeFlows"):
                    self.csbcallstatstotaltranscodeflows = value
                    self.csbcallstatstotaltranscodeflows.value_namespace = name_space
                    self.csbcallstatstotaltranscodeflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsUnclassifiedPkts"):
                    self.csbcallstatsunclassifiedpkts = value
                    self.csbcallstatsunclassifiedpkts.value_namespace = name_space
                    self.csbcallstatsunclassifiedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsUsedFlows"):
                    self.csbcallstatsusedflows = value
                    self.csbcallstatsusedflows.value_namespace = name_space
                    self.csbcallstatsusedflows.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsUsedSigFlows"):
                    self.csbcallstatsusedsigflows = value
                    self.csbcallstatsusedsigflows.value_namespace = name_space
                    self.csbcallstatsusedsigflows.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbcallstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbcallstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbCallStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbCallStatsEntry"):
                for c in self.csbcallstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbcallstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbCallStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csbcurrperiodicstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable, self).__init__()

            self.yang_name = "csbCurrPeriodicStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbcurrperiodicstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable, self).__setattr__(name, value)


        class Csbcurrperiodicstatsentry(Entity):
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
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry, self).__init__()

                self.yang_name = "csbCurrPeriodicStatsEntry"
                self.yang_parent_name = "csbCurrPeriodicStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbcurrperiodicstatsinterval = YLeaf(YType.enumeration, "csbCurrPeriodicStatsInterval")

                self.csbcurrperiodicipseccalls = YLeaf(YType.uint32, "csbCurrPeriodicIpsecCalls")

                self.csbcurrperiodicstatsactivatingcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsActivatingCalls")

                self.csbcurrperiodicstatsactivecallfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsActiveCallFailure")

                self.csbcurrperiodicstatsactivecalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsActiveCalls")

                self.csbcurrperiodicstatsactivee2emergencycalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsActiveE2EmergencyCalls")

                self.csbcurrperiodicstatsactiveemergencycalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsActiveEmergencyCalls")

                self.csbcurrperiodicstatsactiveipv6calls = YLeaf(YType.uint32, "csbCurrPeriodicStatsActiveIpv6Calls")

                self.csbcurrperiodicstatsaudiotranscodedcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsAudioTranscodedCalls")

                self.csbcurrperiodicstatscallmediafailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallMediaFailure")

                self.csbcurrperiodicstatscallresourcefailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallResourceFailure")

                self.csbcurrperiodicstatscallroutingfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallRoutingFailure")

                self.csbcurrperiodicstatscallsetupcacbandwidthfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACBandwidthFailure")

                self.csbcurrperiodicstatscallsetupcaccalllimitfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACCallLimitFailure")

                self.csbcurrperiodicstatscallsetupcacmedialimitfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACMediaLimitFailure")

                self.csbcurrperiodicstatscallsetupcacmediaupdatefailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure")

                self.csbcurrperiodicstatscallsetupcacpolicyfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACPolicyFailure")

                self.csbcurrperiodicstatscallsetupcacratelimitfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupCACRateLimitFailure")

                self.csbcurrperiodicstatscallsetupnapolicyfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupNAPolicyFailure")

                self.csbcurrperiodicstatscallsetuppolicyfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupPolicyFailure")

                self.csbcurrperiodicstatscallsetuproutingpolicyfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSetupRoutingPolicyFailure")

                self.csbcurrperiodicstatscallsigfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCallSigFailure")

                self.csbcurrperiodicstatscongestionfailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsCongestionFailure")

                self.csbcurrperiodicstatscurrenttaps = YLeaf(YType.uint32, "csbCurrPeriodicStatsCurrentTaps")

                self.csbcurrperiodicstatsdeactivatingcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsDeactivatingCalls")

                self.csbcurrperiodicstatsdtmfiw2833calls = YLeaf(YType.uint32, "csbCurrPeriodicStatsDtmfIw2833Calls")

                self.csbcurrperiodicstatsdtmfiw2833inbandcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsDtmfIw2833InbandCalls")

                self.csbcurrperiodicstatsdtmfiwinbandcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsDtmfIwInbandCalls")

                self.csbcurrperiodicstatsfailedcallattempts = YLeaf(YType.uint32, "csbCurrPeriodicStatsFailedCallAttempts")

                self.csbcurrperiodicstatsfaxtranscodedcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsFaxTranscodedCalls")

                self.csbcurrperiodicstatsimsrxactivecalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsImsRxActiveCalls")

                self.csbcurrperiodicstatsimsrxcallrenegotiationattempts = YLeaf(YType.uint32, "csbCurrPeriodicStatsImsRxCallRenegotiationAttempts")

                self.csbcurrperiodicstatsimsrxcallrenegotiationfailures = YLeaf(YType.uint32, "csbCurrPeriodicStatsImsRxCallRenegotiationFailures")

                self.csbcurrperiodicstatsimsrxcallsetupfaiures = YLeaf(YType.uint32, "csbCurrPeriodicStatsImsRxCallSetupFaiures")

                self.csbcurrperiodicstatsnonsrtpcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsNonSrtpCalls")

                self.csbcurrperiodicstatsrtpdisallowedfailures = YLeaf(YType.uint32, "csbCurrPeriodicStatsRtpDisallowedFailures")

                self.csbcurrperiodicstatssrtpdisallowedfailures = YLeaf(YType.uint32, "csbCurrPeriodicStatsSrtpDisallowedFailures")

                self.csbcurrperiodicstatssrtpiwcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsSrtpIwCalls")

                self.csbcurrperiodicstatssrtpnoniwcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsSrtpNonIwCalls")

                self.csbcurrperiodicstatstimestamp = YLeaf(YType.str, "csbCurrPeriodicStatsTimestamp")

                self.csbcurrperiodicstatstotalcallattempts = YLeaf(YType.uint32, "csbCurrPeriodicStatsTotalCallAttempts")

                self.csbcurrperiodicstatstotalcallupdatefailure = YLeaf(YType.uint32, "csbCurrPeriodicStatsTotalCallUpdateFailure")

                self.csbcurrperiodicstatstotaltapsrequested = YLeaf(YType.uint32, "csbCurrPeriodicStatsTotalTapsRequested")

                self.csbcurrperiodicstatstotaltapssucceeded = YLeaf(YType.uint32, "csbCurrPeriodicStatsTotalTapsSucceeded")

                self.csbcurrperiodicstatstranscodedcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsTranscodedCalls")

                self.csbcurrperiodicstatstransratedcalls = YLeaf(YType.uint32, "csbCurrPeriodicStatsTransratedCalls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbcurrperiodicstatsinterval",
                                "csbcurrperiodicipseccalls",
                                "csbcurrperiodicstatsactivatingcalls",
                                "csbcurrperiodicstatsactivecallfailure",
                                "csbcurrperiodicstatsactivecalls",
                                "csbcurrperiodicstatsactivee2emergencycalls",
                                "csbcurrperiodicstatsactiveemergencycalls",
                                "csbcurrperiodicstatsactiveipv6calls",
                                "csbcurrperiodicstatsaudiotranscodedcalls",
                                "csbcurrperiodicstatscallmediafailure",
                                "csbcurrperiodicstatscallresourcefailure",
                                "csbcurrperiodicstatscallroutingfailure",
                                "csbcurrperiodicstatscallsetupcacbandwidthfailure",
                                "csbcurrperiodicstatscallsetupcaccalllimitfailure",
                                "csbcurrperiodicstatscallsetupcacmedialimitfailure",
                                "csbcurrperiodicstatscallsetupcacmediaupdatefailure",
                                "csbcurrperiodicstatscallsetupcacpolicyfailure",
                                "csbcurrperiodicstatscallsetupcacratelimitfailure",
                                "csbcurrperiodicstatscallsetupnapolicyfailure",
                                "csbcurrperiodicstatscallsetuppolicyfailure",
                                "csbcurrperiodicstatscallsetuproutingpolicyfailure",
                                "csbcurrperiodicstatscallsigfailure",
                                "csbcurrperiodicstatscongestionfailure",
                                "csbcurrperiodicstatscurrenttaps",
                                "csbcurrperiodicstatsdeactivatingcalls",
                                "csbcurrperiodicstatsdtmfiw2833calls",
                                "csbcurrperiodicstatsdtmfiw2833inbandcalls",
                                "csbcurrperiodicstatsdtmfiwinbandcalls",
                                "csbcurrperiodicstatsfailedcallattempts",
                                "csbcurrperiodicstatsfaxtranscodedcalls",
                                "csbcurrperiodicstatsimsrxactivecalls",
                                "csbcurrperiodicstatsimsrxcallrenegotiationattempts",
                                "csbcurrperiodicstatsimsrxcallrenegotiationfailures",
                                "csbcurrperiodicstatsimsrxcallsetupfaiures",
                                "csbcurrperiodicstatsnonsrtpcalls",
                                "csbcurrperiodicstatsrtpdisallowedfailures",
                                "csbcurrperiodicstatssrtpdisallowedfailures",
                                "csbcurrperiodicstatssrtpiwcalls",
                                "csbcurrperiodicstatssrtpnoniwcalls",
                                "csbcurrperiodicstatstimestamp",
                                "csbcurrperiodicstatstotalcallattempts",
                                "csbcurrperiodicstatstotalcallupdatefailure",
                                "csbcurrperiodicstatstotaltapsrequested",
                                "csbcurrperiodicstatstotaltapssucceeded",
                                "csbcurrperiodicstatstranscodedcalls",
                                "csbcurrperiodicstatstransratedcalls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbcurrperiodicstatsinterval.is_set or
                    self.csbcurrperiodicipseccalls.is_set or
                    self.csbcurrperiodicstatsactivatingcalls.is_set or
                    self.csbcurrperiodicstatsactivecallfailure.is_set or
                    self.csbcurrperiodicstatsactivecalls.is_set or
                    self.csbcurrperiodicstatsactivee2emergencycalls.is_set or
                    self.csbcurrperiodicstatsactiveemergencycalls.is_set or
                    self.csbcurrperiodicstatsactiveipv6calls.is_set or
                    self.csbcurrperiodicstatsaudiotranscodedcalls.is_set or
                    self.csbcurrperiodicstatscallmediafailure.is_set or
                    self.csbcurrperiodicstatscallresourcefailure.is_set or
                    self.csbcurrperiodicstatscallroutingfailure.is_set or
                    self.csbcurrperiodicstatscallsetupcacbandwidthfailure.is_set or
                    self.csbcurrperiodicstatscallsetupcaccalllimitfailure.is_set or
                    self.csbcurrperiodicstatscallsetupcacmedialimitfailure.is_set or
                    self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.is_set or
                    self.csbcurrperiodicstatscallsetupcacpolicyfailure.is_set or
                    self.csbcurrperiodicstatscallsetupcacratelimitfailure.is_set or
                    self.csbcurrperiodicstatscallsetupnapolicyfailure.is_set or
                    self.csbcurrperiodicstatscallsetuppolicyfailure.is_set or
                    self.csbcurrperiodicstatscallsetuproutingpolicyfailure.is_set or
                    self.csbcurrperiodicstatscallsigfailure.is_set or
                    self.csbcurrperiodicstatscongestionfailure.is_set or
                    self.csbcurrperiodicstatscurrenttaps.is_set or
                    self.csbcurrperiodicstatsdeactivatingcalls.is_set or
                    self.csbcurrperiodicstatsdtmfiw2833calls.is_set or
                    self.csbcurrperiodicstatsdtmfiw2833inbandcalls.is_set or
                    self.csbcurrperiodicstatsdtmfiwinbandcalls.is_set or
                    self.csbcurrperiodicstatsfailedcallattempts.is_set or
                    self.csbcurrperiodicstatsfaxtranscodedcalls.is_set or
                    self.csbcurrperiodicstatsimsrxactivecalls.is_set or
                    self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.is_set or
                    self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.is_set or
                    self.csbcurrperiodicstatsimsrxcallsetupfaiures.is_set or
                    self.csbcurrperiodicstatsnonsrtpcalls.is_set or
                    self.csbcurrperiodicstatsrtpdisallowedfailures.is_set or
                    self.csbcurrperiodicstatssrtpdisallowedfailures.is_set or
                    self.csbcurrperiodicstatssrtpiwcalls.is_set or
                    self.csbcurrperiodicstatssrtpnoniwcalls.is_set or
                    self.csbcurrperiodicstatstimestamp.is_set or
                    self.csbcurrperiodicstatstotalcallattempts.is_set or
                    self.csbcurrperiodicstatstotalcallupdatefailure.is_set or
                    self.csbcurrperiodicstatstotaltapsrequested.is_set or
                    self.csbcurrperiodicstatstotaltapssucceeded.is_set or
                    self.csbcurrperiodicstatstranscodedcalls.is_set or
                    self.csbcurrperiodicstatstransratedcalls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsinterval.yfilter != YFilter.not_set or
                    self.csbcurrperiodicipseccalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactivatingcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactivecallfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactivecalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactivee2emergencycalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactiveemergencycalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsactiveipv6calls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsaudiotranscodedcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallmediafailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallresourcefailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallroutingfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcacbandwidthfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcaccalllimitfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcacmedialimitfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcacpolicyfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupcacratelimitfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetupnapolicyfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetuppolicyfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsetuproutingpolicyfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscallsigfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscongestionfailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatscurrenttaps.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsdeactivatingcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsdtmfiw2833calls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsdtmfiw2833inbandcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsdtmfiwinbandcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsfailedcallattempts.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsfaxtranscodedcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsimsrxactivecalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsimsrxcallsetupfaiures.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsnonsrtpcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatsrtpdisallowedfailures.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatssrtpdisallowedfailures.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatssrtpiwcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatssrtpnoniwcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstimestamp.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstotalcallattempts.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstotalcallupdatefailure.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstotaltapsrequested.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstotaltapssucceeded.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstranscodedcalls.yfilter != YFilter.not_set or
                    self.csbcurrperiodicstatstransratedcalls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbCurrPeriodicStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbCurrPeriodicStatsInterval='" + self.csbcurrperiodicstatsinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbCurrPeriodicStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbcurrperiodicstatsinterval.is_set or self.csbcurrperiodicstatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsinterval.get_name_leafdata())
                if (self.csbcurrperiodicipseccalls.is_set or self.csbcurrperiodicipseccalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicipseccalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsactivatingcalls.is_set or self.csbcurrperiodicstatsactivatingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactivatingcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsactivecallfailure.is_set or self.csbcurrperiodicstatsactivecallfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactivecallfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatsactivecalls.is_set or self.csbcurrperiodicstatsactivecalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactivecalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsactivee2emergencycalls.is_set or self.csbcurrperiodicstatsactivee2emergencycalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactivee2emergencycalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsactiveemergencycalls.is_set or self.csbcurrperiodicstatsactiveemergencycalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactiveemergencycalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsactiveipv6calls.is_set or self.csbcurrperiodicstatsactiveipv6calls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsactiveipv6calls.get_name_leafdata())
                if (self.csbcurrperiodicstatsaudiotranscodedcalls.is_set or self.csbcurrperiodicstatsaudiotranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsaudiotranscodedcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatscallmediafailure.is_set or self.csbcurrperiodicstatscallmediafailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallmediafailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallresourcefailure.is_set or self.csbcurrperiodicstatscallresourcefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallresourcefailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallroutingfailure.is_set or self.csbcurrperiodicstatscallroutingfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallroutingfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcacbandwidthfailure.is_set or self.csbcurrperiodicstatscallsetupcacbandwidthfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcacbandwidthfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcaccalllimitfailure.is_set or self.csbcurrperiodicstatscallsetupcaccalllimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcaccalllimitfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcacmedialimitfailure.is_set or self.csbcurrperiodicstatscallsetupcacmedialimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcacmedialimitfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.is_set or self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcacpolicyfailure.is_set or self.csbcurrperiodicstatscallsetupcacpolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcacpolicyfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupcacratelimitfailure.is_set or self.csbcurrperiodicstatscallsetupcacratelimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupcacratelimitfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetupnapolicyfailure.is_set or self.csbcurrperiodicstatscallsetupnapolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetupnapolicyfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetuppolicyfailure.is_set or self.csbcurrperiodicstatscallsetuppolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetuppolicyfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsetuproutingpolicyfailure.is_set or self.csbcurrperiodicstatscallsetuproutingpolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsetuproutingpolicyfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscallsigfailure.is_set or self.csbcurrperiodicstatscallsigfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscallsigfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscongestionfailure.is_set or self.csbcurrperiodicstatscongestionfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscongestionfailure.get_name_leafdata())
                if (self.csbcurrperiodicstatscurrenttaps.is_set or self.csbcurrperiodicstatscurrenttaps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatscurrenttaps.get_name_leafdata())
                if (self.csbcurrperiodicstatsdeactivatingcalls.is_set or self.csbcurrperiodicstatsdeactivatingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsdeactivatingcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsdtmfiw2833calls.is_set or self.csbcurrperiodicstatsdtmfiw2833calls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsdtmfiw2833calls.get_name_leafdata())
                if (self.csbcurrperiodicstatsdtmfiw2833inbandcalls.is_set or self.csbcurrperiodicstatsdtmfiw2833inbandcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsdtmfiw2833inbandcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsdtmfiwinbandcalls.is_set or self.csbcurrperiodicstatsdtmfiwinbandcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsdtmfiwinbandcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsfailedcallattempts.is_set or self.csbcurrperiodicstatsfailedcallattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsfailedcallattempts.get_name_leafdata())
                if (self.csbcurrperiodicstatsfaxtranscodedcalls.is_set or self.csbcurrperiodicstatsfaxtranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsfaxtranscodedcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsimsrxactivecalls.is_set or self.csbcurrperiodicstatsimsrxactivecalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsimsrxactivecalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.is_set or self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.get_name_leafdata())
                if (self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.is_set or self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.get_name_leafdata())
                if (self.csbcurrperiodicstatsimsrxcallsetupfaiures.is_set or self.csbcurrperiodicstatsimsrxcallsetupfaiures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsimsrxcallsetupfaiures.get_name_leafdata())
                if (self.csbcurrperiodicstatsnonsrtpcalls.is_set or self.csbcurrperiodicstatsnonsrtpcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsnonsrtpcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatsrtpdisallowedfailures.is_set or self.csbcurrperiodicstatsrtpdisallowedfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatsrtpdisallowedfailures.get_name_leafdata())
                if (self.csbcurrperiodicstatssrtpdisallowedfailures.is_set or self.csbcurrperiodicstatssrtpdisallowedfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatssrtpdisallowedfailures.get_name_leafdata())
                if (self.csbcurrperiodicstatssrtpiwcalls.is_set or self.csbcurrperiodicstatssrtpiwcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatssrtpiwcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatssrtpnoniwcalls.is_set or self.csbcurrperiodicstatssrtpnoniwcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatssrtpnoniwcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatstimestamp.is_set or self.csbcurrperiodicstatstimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstimestamp.get_name_leafdata())
                if (self.csbcurrperiodicstatstotalcallattempts.is_set or self.csbcurrperiodicstatstotalcallattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstotalcallattempts.get_name_leafdata())
                if (self.csbcurrperiodicstatstotalcallupdatefailure.is_set or self.csbcurrperiodicstatstotalcallupdatefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstotalcallupdatefailure.get_name_leafdata())
                if (self.csbcurrperiodicstatstotaltapsrequested.is_set or self.csbcurrperiodicstatstotaltapsrequested.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstotaltapsrequested.get_name_leafdata())
                if (self.csbcurrperiodicstatstotaltapssucceeded.is_set or self.csbcurrperiodicstatstotaltapssucceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstotaltapssucceeded.get_name_leafdata())
                if (self.csbcurrperiodicstatstranscodedcalls.is_set or self.csbcurrperiodicstatstranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstranscodedcalls.get_name_leafdata())
                if (self.csbcurrperiodicstatstransratedcalls.is_set or self.csbcurrperiodicstatstransratedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcurrperiodicstatstransratedcalls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbCurrPeriodicStatsInterval" or name == "csbCurrPeriodicIpsecCalls" or name == "csbCurrPeriodicStatsActivatingCalls" or name == "csbCurrPeriodicStatsActiveCallFailure" or name == "csbCurrPeriodicStatsActiveCalls" or name == "csbCurrPeriodicStatsActiveE2EmergencyCalls" or name == "csbCurrPeriodicStatsActiveEmergencyCalls" or name == "csbCurrPeriodicStatsActiveIpv6Calls" or name == "csbCurrPeriodicStatsAudioTranscodedCalls" or name == "csbCurrPeriodicStatsCallMediaFailure" or name == "csbCurrPeriodicStatsCallResourceFailure" or name == "csbCurrPeriodicStatsCallRoutingFailure" or name == "csbCurrPeriodicStatsCallSetupCACBandwidthFailure" or name == "csbCurrPeriodicStatsCallSetupCACCallLimitFailure" or name == "csbCurrPeriodicStatsCallSetupCACMediaLimitFailure" or name == "csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure" or name == "csbCurrPeriodicStatsCallSetupCACPolicyFailure" or name == "csbCurrPeriodicStatsCallSetupCACRateLimitFailure" or name == "csbCurrPeriodicStatsCallSetupNAPolicyFailure" or name == "csbCurrPeriodicStatsCallSetupPolicyFailure" or name == "csbCurrPeriodicStatsCallSetupRoutingPolicyFailure" or name == "csbCurrPeriodicStatsCallSigFailure" or name == "csbCurrPeriodicStatsCongestionFailure" or name == "csbCurrPeriodicStatsCurrentTaps" or name == "csbCurrPeriodicStatsDeactivatingCalls" or name == "csbCurrPeriodicStatsDtmfIw2833Calls" or name == "csbCurrPeriodicStatsDtmfIw2833InbandCalls" or name == "csbCurrPeriodicStatsDtmfIwInbandCalls" or name == "csbCurrPeriodicStatsFailedCallAttempts" or name == "csbCurrPeriodicStatsFaxTranscodedCalls" or name == "csbCurrPeriodicStatsImsRxActiveCalls" or name == "csbCurrPeriodicStatsImsRxCallRenegotiationAttempts" or name == "csbCurrPeriodicStatsImsRxCallRenegotiationFailures" or name == "csbCurrPeriodicStatsImsRxCallSetupFaiures" or name == "csbCurrPeriodicStatsNonSrtpCalls" or name == "csbCurrPeriodicStatsRtpDisallowedFailures" or name == "csbCurrPeriodicStatsSrtpDisallowedFailures" or name == "csbCurrPeriodicStatsSrtpIwCalls" or name == "csbCurrPeriodicStatsSrtpNonIwCalls" or name == "csbCurrPeriodicStatsTimestamp" or name == "csbCurrPeriodicStatsTotalCallAttempts" or name == "csbCurrPeriodicStatsTotalCallUpdateFailure" or name == "csbCurrPeriodicStatsTotalTapsRequested" or name == "csbCurrPeriodicStatsTotalTapsSucceeded" or name == "csbCurrPeriodicStatsTranscodedCalls" or name == "csbCurrPeriodicStatsTransratedCalls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsInterval"):
                    self.csbcurrperiodicstatsinterval = value
                    self.csbcurrperiodicstatsinterval.value_namespace = name_space
                    self.csbcurrperiodicstatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicIpsecCalls"):
                    self.csbcurrperiodicipseccalls = value
                    self.csbcurrperiodicipseccalls.value_namespace = name_space
                    self.csbcurrperiodicipseccalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActivatingCalls"):
                    self.csbcurrperiodicstatsactivatingcalls = value
                    self.csbcurrperiodicstatsactivatingcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsactivatingcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActiveCallFailure"):
                    self.csbcurrperiodicstatsactivecallfailure = value
                    self.csbcurrperiodicstatsactivecallfailure.value_namespace = name_space
                    self.csbcurrperiodicstatsactivecallfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActiveCalls"):
                    self.csbcurrperiodicstatsactivecalls = value
                    self.csbcurrperiodicstatsactivecalls.value_namespace = name_space
                    self.csbcurrperiodicstatsactivecalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActiveE2EmergencyCalls"):
                    self.csbcurrperiodicstatsactivee2emergencycalls = value
                    self.csbcurrperiodicstatsactivee2emergencycalls.value_namespace = name_space
                    self.csbcurrperiodicstatsactivee2emergencycalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActiveEmergencyCalls"):
                    self.csbcurrperiodicstatsactiveemergencycalls = value
                    self.csbcurrperiodicstatsactiveemergencycalls.value_namespace = name_space
                    self.csbcurrperiodicstatsactiveemergencycalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsActiveIpv6Calls"):
                    self.csbcurrperiodicstatsactiveipv6calls = value
                    self.csbcurrperiodicstatsactiveipv6calls.value_namespace = name_space
                    self.csbcurrperiodicstatsactiveipv6calls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsAudioTranscodedCalls"):
                    self.csbcurrperiodicstatsaudiotranscodedcalls = value
                    self.csbcurrperiodicstatsaudiotranscodedcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsaudiotranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallMediaFailure"):
                    self.csbcurrperiodicstatscallmediafailure = value
                    self.csbcurrperiodicstatscallmediafailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallmediafailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallResourceFailure"):
                    self.csbcurrperiodicstatscallresourcefailure = value
                    self.csbcurrperiodicstatscallresourcefailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallresourcefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallRoutingFailure"):
                    self.csbcurrperiodicstatscallroutingfailure = value
                    self.csbcurrperiodicstatscallroutingfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallroutingfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACBandwidthFailure"):
                    self.csbcurrperiodicstatscallsetupcacbandwidthfailure = value
                    self.csbcurrperiodicstatscallsetupcacbandwidthfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcacbandwidthfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACCallLimitFailure"):
                    self.csbcurrperiodicstatscallsetupcaccalllimitfailure = value
                    self.csbcurrperiodicstatscallsetupcaccalllimitfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcaccalllimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACMediaLimitFailure"):
                    self.csbcurrperiodicstatscallsetupcacmedialimitfailure = value
                    self.csbcurrperiodicstatscallsetupcacmedialimitfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcacmedialimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure"):
                    self.csbcurrperiodicstatscallsetupcacmediaupdatefailure = value
                    self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcacmediaupdatefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACPolicyFailure"):
                    self.csbcurrperiodicstatscallsetupcacpolicyfailure = value
                    self.csbcurrperiodicstatscallsetupcacpolicyfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcacpolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupCACRateLimitFailure"):
                    self.csbcurrperiodicstatscallsetupcacratelimitfailure = value
                    self.csbcurrperiodicstatscallsetupcacratelimitfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupcacratelimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupNAPolicyFailure"):
                    self.csbcurrperiodicstatscallsetupnapolicyfailure = value
                    self.csbcurrperiodicstatscallsetupnapolicyfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetupnapolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupPolicyFailure"):
                    self.csbcurrperiodicstatscallsetuppolicyfailure = value
                    self.csbcurrperiodicstatscallsetuppolicyfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetuppolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSetupRoutingPolicyFailure"):
                    self.csbcurrperiodicstatscallsetuproutingpolicyfailure = value
                    self.csbcurrperiodicstatscallsetuproutingpolicyfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsetuproutingpolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCallSigFailure"):
                    self.csbcurrperiodicstatscallsigfailure = value
                    self.csbcurrperiodicstatscallsigfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscallsigfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCongestionFailure"):
                    self.csbcurrperiodicstatscongestionfailure = value
                    self.csbcurrperiodicstatscongestionfailure.value_namespace = name_space
                    self.csbcurrperiodicstatscongestionfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsCurrentTaps"):
                    self.csbcurrperiodicstatscurrenttaps = value
                    self.csbcurrperiodicstatscurrenttaps.value_namespace = name_space
                    self.csbcurrperiodicstatscurrenttaps.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsDeactivatingCalls"):
                    self.csbcurrperiodicstatsdeactivatingcalls = value
                    self.csbcurrperiodicstatsdeactivatingcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsdeactivatingcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsDtmfIw2833Calls"):
                    self.csbcurrperiodicstatsdtmfiw2833calls = value
                    self.csbcurrperiodicstatsdtmfiw2833calls.value_namespace = name_space
                    self.csbcurrperiodicstatsdtmfiw2833calls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsDtmfIw2833InbandCalls"):
                    self.csbcurrperiodicstatsdtmfiw2833inbandcalls = value
                    self.csbcurrperiodicstatsdtmfiw2833inbandcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsdtmfiw2833inbandcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsDtmfIwInbandCalls"):
                    self.csbcurrperiodicstatsdtmfiwinbandcalls = value
                    self.csbcurrperiodicstatsdtmfiwinbandcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsdtmfiwinbandcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsFailedCallAttempts"):
                    self.csbcurrperiodicstatsfailedcallattempts = value
                    self.csbcurrperiodicstatsfailedcallattempts.value_namespace = name_space
                    self.csbcurrperiodicstatsfailedcallattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsFaxTranscodedCalls"):
                    self.csbcurrperiodicstatsfaxtranscodedcalls = value
                    self.csbcurrperiodicstatsfaxtranscodedcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsfaxtranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsImsRxActiveCalls"):
                    self.csbcurrperiodicstatsimsrxactivecalls = value
                    self.csbcurrperiodicstatsimsrxactivecalls.value_namespace = name_space
                    self.csbcurrperiodicstatsimsrxactivecalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsImsRxCallRenegotiationAttempts"):
                    self.csbcurrperiodicstatsimsrxcallrenegotiationattempts = value
                    self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.value_namespace = name_space
                    self.csbcurrperiodicstatsimsrxcallrenegotiationattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsImsRxCallRenegotiationFailures"):
                    self.csbcurrperiodicstatsimsrxcallrenegotiationfailures = value
                    self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.value_namespace = name_space
                    self.csbcurrperiodicstatsimsrxcallrenegotiationfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsImsRxCallSetupFaiures"):
                    self.csbcurrperiodicstatsimsrxcallsetupfaiures = value
                    self.csbcurrperiodicstatsimsrxcallsetupfaiures.value_namespace = name_space
                    self.csbcurrperiodicstatsimsrxcallsetupfaiures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsNonSrtpCalls"):
                    self.csbcurrperiodicstatsnonsrtpcalls = value
                    self.csbcurrperiodicstatsnonsrtpcalls.value_namespace = name_space
                    self.csbcurrperiodicstatsnonsrtpcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsRtpDisallowedFailures"):
                    self.csbcurrperiodicstatsrtpdisallowedfailures = value
                    self.csbcurrperiodicstatsrtpdisallowedfailures.value_namespace = name_space
                    self.csbcurrperiodicstatsrtpdisallowedfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsSrtpDisallowedFailures"):
                    self.csbcurrperiodicstatssrtpdisallowedfailures = value
                    self.csbcurrperiodicstatssrtpdisallowedfailures.value_namespace = name_space
                    self.csbcurrperiodicstatssrtpdisallowedfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsSrtpIwCalls"):
                    self.csbcurrperiodicstatssrtpiwcalls = value
                    self.csbcurrperiodicstatssrtpiwcalls.value_namespace = name_space
                    self.csbcurrperiodicstatssrtpiwcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsSrtpNonIwCalls"):
                    self.csbcurrperiodicstatssrtpnoniwcalls = value
                    self.csbcurrperiodicstatssrtpnoniwcalls.value_namespace = name_space
                    self.csbcurrperiodicstatssrtpnoniwcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTimestamp"):
                    self.csbcurrperiodicstatstimestamp = value
                    self.csbcurrperiodicstatstimestamp.value_namespace = name_space
                    self.csbcurrperiodicstatstimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTotalCallAttempts"):
                    self.csbcurrperiodicstatstotalcallattempts = value
                    self.csbcurrperiodicstatstotalcallattempts.value_namespace = name_space
                    self.csbcurrperiodicstatstotalcallattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTotalCallUpdateFailure"):
                    self.csbcurrperiodicstatstotalcallupdatefailure = value
                    self.csbcurrperiodicstatstotalcallupdatefailure.value_namespace = name_space
                    self.csbcurrperiodicstatstotalcallupdatefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTotalTapsRequested"):
                    self.csbcurrperiodicstatstotaltapsrequested = value
                    self.csbcurrperiodicstatstotaltapsrequested.value_namespace = name_space
                    self.csbcurrperiodicstatstotaltapsrequested.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTotalTapsSucceeded"):
                    self.csbcurrperiodicstatstotaltapssucceeded = value
                    self.csbcurrperiodicstatstotaltapssucceeded.value_namespace = name_space
                    self.csbcurrperiodicstatstotaltapssucceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTranscodedCalls"):
                    self.csbcurrperiodicstatstranscodedcalls = value
                    self.csbcurrperiodicstatstranscodedcalls.value_namespace = name_space
                    self.csbcurrperiodicstatstranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCurrPeriodicStatsTransratedCalls"):
                    self.csbcurrperiodicstatstransratedcalls = value
                    self.csbcurrperiodicstatstransratedcalls.value_namespace = name_space
                    self.csbcurrperiodicstatstransratedcalls.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbcurrperiodicstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbcurrperiodicstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbCurrPeriodicStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbCurrPeriodicStatsEntry"):
                for c in self.csbcurrperiodicstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbcurrperiodicstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbCurrPeriodicStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csbhistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable, self).__init__()

            self.yang_name = "csbHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbhistorystatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable, self).__setattr__(name, value)


        class Csbhistorystatsentry(Entity):
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
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry, self).__init__()

                self.yang_name = "csbHistoryStatsEntry"
                self.yang_parent_name = "csbHistoryStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbhistorystatsinterval = YLeaf(YType.enumeration, "csbHistoryStatsInterval")

                self.csbhistorystatselements = YLeaf(YType.uint32, "csbHistoryStatsElements")

                self.csbhistorystatsactivecallfailure = YLeaf(YType.uint32, "csbHistoryStatsActiveCallFailure")

                self.csbhistorystatsactivecalls = YLeaf(YType.uint32, "csbHistoryStatsActiveCalls")

                self.csbhistorystatsactivee2emergencycalls = YLeaf(YType.uint32, "csbHistoryStatsActiveE2EmergencyCalls")

                self.csbhistorystatsactiveemergencycalls = YLeaf(YType.uint32, "csbHistoryStatsActiveEmergencyCalls")

                self.csbhistorystatsactiveipv6calls = YLeaf(YType.uint32, "csbHistoryStatsActiveIpv6Calls")

                self.csbhistorystatsaudiotranscodedcalls = YLeaf(YType.uint32, "csbHistoryStatsAudioTranscodedCalls")

                self.csbhistorystatscallmediafailure = YLeaf(YType.uint32, "csbHistoryStatsCallMediaFailure")

                self.csbhistorystatscallresourcefailure = YLeaf(YType.uint32, "csbHistoryStatsCallResourceFailure")

                self.csbhistorystatscallroutingfailure = YLeaf(YType.uint32, "csbHistoryStatsCallRoutingFailure")

                self.csbhistorystatscallsetupcacbandwidthfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACBandwidthFailure")

                self.csbhistorystatscallsetupcaccalllimitfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACCallLimitFailure")

                self.csbhistorystatscallsetupcacmedialimitfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACMediaLimitFailure")

                self.csbhistorystatscallsetupcacmediaupdatefailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACMediaUpdateFailure")

                self.csbhistorystatscallsetupcacpolicyfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACPolicyFailure")

                self.csbhistorystatscallsetupcacratelimitfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupCACRateLimitFailure")

                self.csbhistorystatscallsetupnapolicyfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupNAPolicyFailure")

                self.csbhistorystatscallsetuppolicyfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupPolicyFailure")

                self.csbhistorystatscallsetuproutingpolicyfailure = YLeaf(YType.uint32, "csbHistoryStatsCallSetupRoutingPolicyFailure")

                self.csbhistorystatscongestionfailure = YLeaf(YType.uint32, "csbHistoryStatsCongestionFailure")

                self.csbhistorystatscurrenttaps = YLeaf(YType.uint32, "csbHistoryStatsCurrentTaps")

                self.csbhistorystatsdtmfiw2833calls = YLeaf(YType.uint32, "csbHistoryStatsDtmfIw2833Calls")

                self.csbhistorystatsdtmfiw2833inbandcalls = YLeaf(YType.uint32, "csbHistoryStatsDtmfIw2833InbandCalls")

                self.csbhistorystatsdtmfiwinbandcalls = YLeaf(YType.uint32, "csbHistoryStatsDtmfIwInbandCalls")

                self.csbhistorystatsfailedcallattempts = YLeaf(YType.uint32, "csbHistoryStatsFailedCallAttempts")

                self.csbhistorystatsfailsigfailure = YLeaf(YType.uint32, "csbHistoryStatsFailSigFailure")

                self.csbhistorystatsfaxtranscodedcalls = YLeaf(YType.uint32, "csbHistoryStatsFaxTranscodedCalls")

                self.csbhistorystatsimsrxactivecalls = YLeaf(YType.uint32, "csbHistoryStatsImsRxActiveCalls")

                self.csbhistorystatsimsrxcallrenegotiationattempts = YLeaf(YType.uint32, "csbHistoryStatsImsRxCallRenegotiationAttempts")

                self.csbhistorystatsimsrxcallrenegotiationfailures = YLeaf(YType.uint32, "csbHistoryStatsImsRxCallRenegotiationFailures")

                self.csbhistorystatsimsrxcallsetupfailures = YLeaf(YType.uint32, "csbHistoryStatsImsRxCallSetupFailures")

                self.csbhistorystatsipseccalls = YLeaf(YType.uint32, "csbHistoryStatsIpsecCalls")

                self.csbhistorystatsnonsrtpcalls = YLeaf(YType.uint32, "csbHistoryStatsNonSrtpCalls")

                self.csbhistorystatsrtpdisallowedfailures = YLeaf(YType.uint32, "csbHistoryStatsRtpDisallowedFailures")

                self.csbhistorystatssrtpdisallowedfailures = YLeaf(YType.uint32, "csbHistoryStatsSrtpDisallowedFailures")

                self.csbhistorystatssrtpiwcalls = YLeaf(YType.uint32, "csbHistoryStatsSrtpIwCalls")

                self.csbhistorystatssrtpnoniwcalls = YLeaf(YType.uint32, "csbHistoryStatsSrtpNonIwCalls")

                self.csbhistorystatstimestamp = YLeaf(YType.str, "csbHistoryStatsTimestamp")

                self.csbhistorystatstotalcallattempts = YLeaf(YType.uint32, "csbHistoryStatsTotalCallAttempts")

                self.csbhistorystatstotalcallupdatefailure = YLeaf(YType.uint32, "csbHistoryStatsTotalCallUpdateFailure")

                self.csbhistorystatstotaltapsrequested = YLeaf(YType.uint32, "csbHistoryStatsTotalTapsRequested")

                self.csbhistorystatstotaltapssucceeded = YLeaf(YType.uint32, "csbHistoryStatsTotalTapsSucceeded")

                self.csbhistroystatstranscodedcalls = YLeaf(YType.uint32, "csbHistroyStatsTranscodedCalls")

                self.csbhistroystatstransratedcalls = YLeaf(YType.uint32, "csbHistroyStatsTransratedCalls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbhistorystatsinterval",
                                "csbhistorystatselements",
                                "csbhistorystatsactivecallfailure",
                                "csbhistorystatsactivecalls",
                                "csbhistorystatsactivee2emergencycalls",
                                "csbhistorystatsactiveemergencycalls",
                                "csbhistorystatsactiveipv6calls",
                                "csbhistorystatsaudiotranscodedcalls",
                                "csbhistorystatscallmediafailure",
                                "csbhistorystatscallresourcefailure",
                                "csbhistorystatscallroutingfailure",
                                "csbhistorystatscallsetupcacbandwidthfailure",
                                "csbhistorystatscallsetupcaccalllimitfailure",
                                "csbhistorystatscallsetupcacmedialimitfailure",
                                "csbhistorystatscallsetupcacmediaupdatefailure",
                                "csbhistorystatscallsetupcacpolicyfailure",
                                "csbhistorystatscallsetupcacratelimitfailure",
                                "csbhistorystatscallsetupnapolicyfailure",
                                "csbhistorystatscallsetuppolicyfailure",
                                "csbhistorystatscallsetuproutingpolicyfailure",
                                "csbhistorystatscongestionfailure",
                                "csbhistorystatscurrenttaps",
                                "csbhistorystatsdtmfiw2833calls",
                                "csbhistorystatsdtmfiw2833inbandcalls",
                                "csbhistorystatsdtmfiwinbandcalls",
                                "csbhistorystatsfailedcallattempts",
                                "csbhistorystatsfailsigfailure",
                                "csbhistorystatsfaxtranscodedcalls",
                                "csbhistorystatsimsrxactivecalls",
                                "csbhistorystatsimsrxcallrenegotiationattempts",
                                "csbhistorystatsimsrxcallrenegotiationfailures",
                                "csbhistorystatsimsrxcallsetupfailures",
                                "csbhistorystatsipseccalls",
                                "csbhistorystatsnonsrtpcalls",
                                "csbhistorystatsrtpdisallowedfailures",
                                "csbhistorystatssrtpdisallowedfailures",
                                "csbhistorystatssrtpiwcalls",
                                "csbhistorystatssrtpnoniwcalls",
                                "csbhistorystatstimestamp",
                                "csbhistorystatstotalcallattempts",
                                "csbhistorystatstotalcallupdatefailure",
                                "csbhistorystatstotaltapsrequested",
                                "csbhistorystatstotaltapssucceeded",
                                "csbhistroystatstranscodedcalls",
                                "csbhistroystatstransratedcalls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbhistorystatsinterval.is_set or
                    self.csbhistorystatselements.is_set or
                    self.csbhistorystatsactivecallfailure.is_set or
                    self.csbhistorystatsactivecalls.is_set or
                    self.csbhistorystatsactivee2emergencycalls.is_set or
                    self.csbhistorystatsactiveemergencycalls.is_set or
                    self.csbhistorystatsactiveipv6calls.is_set or
                    self.csbhistorystatsaudiotranscodedcalls.is_set or
                    self.csbhistorystatscallmediafailure.is_set or
                    self.csbhistorystatscallresourcefailure.is_set or
                    self.csbhistorystatscallroutingfailure.is_set or
                    self.csbhistorystatscallsetupcacbandwidthfailure.is_set or
                    self.csbhistorystatscallsetupcaccalllimitfailure.is_set or
                    self.csbhistorystatscallsetupcacmedialimitfailure.is_set or
                    self.csbhistorystatscallsetupcacmediaupdatefailure.is_set or
                    self.csbhistorystatscallsetupcacpolicyfailure.is_set or
                    self.csbhistorystatscallsetupcacratelimitfailure.is_set or
                    self.csbhistorystatscallsetupnapolicyfailure.is_set or
                    self.csbhistorystatscallsetuppolicyfailure.is_set or
                    self.csbhistorystatscallsetuproutingpolicyfailure.is_set or
                    self.csbhistorystatscongestionfailure.is_set or
                    self.csbhistorystatscurrenttaps.is_set or
                    self.csbhistorystatsdtmfiw2833calls.is_set or
                    self.csbhistorystatsdtmfiw2833inbandcalls.is_set or
                    self.csbhistorystatsdtmfiwinbandcalls.is_set or
                    self.csbhistorystatsfailedcallattempts.is_set or
                    self.csbhistorystatsfailsigfailure.is_set or
                    self.csbhistorystatsfaxtranscodedcalls.is_set or
                    self.csbhistorystatsimsrxactivecalls.is_set or
                    self.csbhistorystatsimsrxcallrenegotiationattempts.is_set or
                    self.csbhistorystatsimsrxcallrenegotiationfailures.is_set or
                    self.csbhistorystatsimsrxcallsetupfailures.is_set or
                    self.csbhistorystatsipseccalls.is_set or
                    self.csbhistorystatsnonsrtpcalls.is_set or
                    self.csbhistorystatsrtpdisallowedfailures.is_set or
                    self.csbhistorystatssrtpdisallowedfailures.is_set or
                    self.csbhistorystatssrtpiwcalls.is_set or
                    self.csbhistorystatssrtpnoniwcalls.is_set or
                    self.csbhistorystatstimestamp.is_set or
                    self.csbhistorystatstotalcallattempts.is_set or
                    self.csbhistorystatstotalcallupdatefailure.is_set or
                    self.csbhistorystatstotaltapsrequested.is_set or
                    self.csbhistorystatstotaltapssucceeded.is_set or
                    self.csbhistroystatstranscodedcalls.is_set or
                    self.csbhistroystatstransratedcalls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbhistorystatsinterval.yfilter != YFilter.not_set or
                    self.csbhistorystatselements.yfilter != YFilter.not_set or
                    self.csbhistorystatsactivecallfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatsactivecalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsactivee2emergencycalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsactiveemergencycalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsactiveipv6calls.yfilter != YFilter.not_set or
                    self.csbhistorystatsaudiotranscodedcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatscallmediafailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallresourcefailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallroutingfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcacbandwidthfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcaccalllimitfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcacmedialimitfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcacmediaupdatefailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcacpolicyfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupcacratelimitfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetupnapolicyfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetuppolicyfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscallsetuproutingpolicyfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscongestionfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatscurrenttaps.yfilter != YFilter.not_set or
                    self.csbhistorystatsdtmfiw2833calls.yfilter != YFilter.not_set or
                    self.csbhistorystatsdtmfiw2833inbandcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsdtmfiwinbandcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsfailedcallattempts.yfilter != YFilter.not_set or
                    self.csbhistorystatsfailsigfailure.yfilter != YFilter.not_set or
                    self.csbhistorystatsfaxtranscodedcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsimsrxactivecalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsimsrxcallrenegotiationattempts.yfilter != YFilter.not_set or
                    self.csbhistorystatsimsrxcallrenegotiationfailures.yfilter != YFilter.not_set or
                    self.csbhistorystatsimsrxcallsetupfailures.yfilter != YFilter.not_set or
                    self.csbhistorystatsipseccalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsnonsrtpcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatsrtpdisallowedfailures.yfilter != YFilter.not_set or
                    self.csbhistorystatssrtpdisallowedfailures.yfilter != YFilter.not_set or
                    self.csbhistorystatssrtpiwcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatssrtpnoniwcalls.yfilter != YFilter.not_set or
                    self.csbhistorystatstimestamp.yfilter != YFilter.not_set or
                    self.csbhistorystatstotalcallattempts.yfilter != YFilter.not_set or
                    self.csbhistorystatstotalcallupdatefailure.yfilter != YFilter.not_set or
                    self.csbhistorystatstotaltapsrequested.yfilter != YFilter.not_set or
                    self.csbhistorystatstotaltapssucceeded.yfilter != YFilter.not_set or
                    self.csbhistroystatstranscodedcalls.yfilter != YFilter.not_set or
                    self.csbhistroystatstransratedcalls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbHistoryStatsInterval='" + self.csbhistorystatsinterval.get() + "']" + "[csbHistoryStatsElements='" + self.csbhistorystatselements.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbHistoryStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbhistorystatsinterval.is_set or self.csbhistorystatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsinterval.get_name_leafdata())
                if (self.csbhistorystatselements.is_set or self.csbhistorystatselements.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatselements.get_name_leafdata())
                if (self.csbhistorystatsactivecallfailure.is_set or self.csbhistorystatsactivecallfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsactivecallfailure.get_name_leafdata())
                if (self.csbhistorystatsactivecalls.is_set or self.csbhistorystatsactivecalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsactivecalls.get_name_leafdata())
                if (self.csbhistorystatsactivee2emergencycalls.is_set or self.csbhistorystatsactivee2emergencycalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsactivee2emergencycalls.get_name_leafdata())
                if (self.csbhistorystatsactiveemergencycalls.is_set or self.csbhistorystatsactiveemergencycalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsactiveemergencycalls.get_name_leafdata())
                if (self.csbhistorystatsactiveipv6calls.is_set or self.csbhistorystatsactiveipv6calls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsactiveipv6calls.get_name_leafdata())
                if (self.csbhistorystatsaudiotranscodedcalls.is_set or self.csbhistorystatsaudiotranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsaudiotranscodedcalls.get_name_leafdata())
                if (self.csbhistorystatscallmediafailure.is_set or self.csbhistorystatscallmediafailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallmediafailure.get_name_leafdata())
                if (self.csbhistorystatscallresourcefailure.is_set or self.csbhistorystatscallresourcefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallresourcefailure.get_name_leafdata())
                if (self.csbhistorystatscallroutingfailure.is_set or self.csbhistorystatscallroutingfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallroutingfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcacbandwidthfailure.is_set or self.csbhistorystatscallsetupcacbandwidthfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcacbandwidthfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcaccalllimitfailure.is_set or self.csbhistorystatscallsetupcaccalllimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcaccalllimitfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcacmedialimitfailure.is_set or self.csbhistorystatscallsetupcacmedialimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcacmedialimitfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcacmediaupdatefailure.is_set or self.csbhistorystatscallsetupcacmediaupdatefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcacmediaupdatefailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcacpolicyfailure.is_set or self.csbhistorystatscallsetupcacpolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcacpolicyfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupcacratelimitfailure.is_set or self.csbhistorystatscallsetupcacratelimitfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupcacratelimitfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetupnapolicyfailure.is_set or self.csbhistorystatscallsetupnapolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetupnapolicyfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetuppolicyfailure.is_set or self.csbhistorystatscallsetuppolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetuppolicyfailure.get_name_leafdata())
                if (self.csbhistorystatscallsetuproutingpolicyfailure.is_set or self.csbhistorystatscallsetuproutingpolicyfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscallsetuproutingpolicyfailure.get_name_leafdata())
                if (self.csbhistorystatscongestionfailure.is_set or self.csbhistorystatscongestionfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscongestionfailure.get_name_leafdata())
                if (self.csbhistorystatscurrenttaps.is_set or self.csbhistorystatscurrenttaps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatscurrenttaps.get_name_leafdata())
                if (self.csbhistorystatsdtmfiw2833calls.is_set or self.csbhistorystatsdtmfiw2833calls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsdtmfiw2833calls.get_name_leafdata())
                if (self.csbhistorystatsdtmfiw2833inbandcalls.is_set or self.csbhistorystatsdtmfiw2833inbandcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsdtmfiw2833inbandcalls.get_name_leafdata())
                if (self.csbhistorystatsdtmfiwinbandcalls.is_set or self.csbhistorystatsdtmfiwinbandcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsdtmfiwinbandcalls.get_name_leafdata())
                if (self.csbhistorystatsfailedcallattempts.is_set or self.csbhistorystatsfailedcallattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsfailedcallattempts.get_name_leafdata())
                if (self.csbhistorystatsfailsigfailure.is_set or self.csbhistorystatsfailsigfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsfailsigfailure.get_name_leafdata())
                if (self.csbhistorystatsfaxtranscodedcalls.is_set or self.csbhistorystatsfaxtranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsfaxtranscodedcalls.get_name_leafdata())
                if (self.csbhistorystatsimsrxactivecalls.is_set or self.csbhistorystatsimsrxactivecalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsimsrxactivecalls.get_name_leafdata())
                if (self.csbhistorystatsimsrxcallrenegotiationattempts.is_set or self.csbhistorystatsimsrxcallrenegotiationattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsimsrxcallrenegotiationattempts.get_name_leafdata())
                if (self.csbhistorystatsimsrxcallrenegotiationfailures.is_set or self.csbhistorystatsimsrxcallrenegotiationfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsimsrxcallrenegotiationfailures.get_name_leafdata())
                if (self.csbhistorystatsimsrxcallsetupfailures.is_set or self.csbhistorystatsimsrxcallsetupfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsimsrxcallsetupfailures.get_name_leafdata())
                if (self.csbhistorystatsipseccalls.is_set or self.csbhistorystatsipseccalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsipseccalls.get_name_leafdata())
                if (self.csbhistorystatsnonsrtpcalls.is_set or self.csbhistorystatsnonsrtpcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsnonsrtpcalls.get_name_leafdata())
                if (self.csbhistorystatsrtpdisallowedfailures.is_set or self.csbhistorystatsrtpdisallowedfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatsrtpdisallowedfailures.get_name_leafdata())
                if (self.csbhistorystatssrtpdisallowedfailures.is_set or self.csbhistorystatssrtpdisallowedfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatssrtpdisallowedfailures.get_name_leafdata())
                if (self.csbhistorystatssrtpiwcalls.is_set or self.csbhistorystatssrtpiwcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatssrtpiwcalls.get_name_leafdata())
                if (self.csbhistorystatssrtpnoniwcalls.is_set or self.csbhistorystatssrtpnoniwcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatssrtpnoniwcalls.get_name_leafdata())
                if (self.csbhistorystatstimestamp.is_set or self.csbhistorystatstimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatstimestamp.get_name_leafdata())
                if (self.csbhistorystatstotalcallattempts.is_set or self.csbhistorystatstotalcallattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatstotalcallattempts.get_name_leafdata())
                if (self.csbhistorystatstotalcallupdatefailure.is_set or self.csbhistorystatstotalcallupdatefailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatstotalcallupdatefailure.get_name_leafdata())
                if (self.csbhistorystatstotaltapsrequested.is_set or self.csbhistorystatstotaltapsrequested.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatstotaltapsrequested.get_name_leafdata())
                if (self.csbhistorystatstotaltapssucceeded.is_set or self.csbhistorystatstotaltapssucceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistorystatstotaltapssucceeded.get_name_leafdata())
                if (self.csbhistroystatstranscodedcalls.is_set or self.csbhistroystatstranscodedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistroystatstranscodedcalls.get_name_leafdata())
                if (self.csbhistroystatstransratedcalls.is_set or self.csbhistroystatstransratedcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbhistroystatstransratedcalls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbHistoryStatsInterval" or name == "csbHistoryStatsElements" or name == "csbHistoryStatsActiveCallFailure" or name == "csbHistoryStatsActiveCalls" or name == "csbHistoryStatsActiveE2EmergencyCalls" or name == "csbHistoryStatsActiveEmergencyCalls" or name == "csbHistoryStatsActiveIpv6Calls" or name == "csbHistoryStatsAudioTranscodedCalls" or name == "csbHistoryStatsCallMediaFailure" or name == "csbHistoryStatsCallResourceFailure" or name == "csbHistoryStatsCallRoutingFailure" or name == "csbHistoryStatsCallSetupCACBandwidthFailure" or name == "csbHistoryStatsCallSetupCACCallLimitFailure" or name == "csbHistoryStatsCallSetupCACMediaLimitFailure" or name == "csbHistoryStatsCallSetupCACMediaUpdateFailure" or name == "csbHistoryStatsCallSetupCACPolicyFailure" or name == "csbHistoryStatsCallSetupCACRateLimitFailure" or name == "csbHistoryStatsCallSetupNAPolicyFailure" or name == "csbHistoryStatsCallSetupPolicyFailure" or name == "csbHistoryStatsCallSetupRoutingPolicyFailure" or name == "csbHistoryStatsCongestionFailure" or name == "csbHistoryStatsCurrentTaps" or name == "csbHistoryStatsDtmfIw2833Calls" or name == "csbHistoryStatsDtmfIw2833InbandCalls" or name == "csbHistoryStatsDtmfIwInbandCalls" or name == "csbHistoryStatsFailedCallAttempts" or name == "csbHistoryStatsFailSigFailure" or name == "csbHistoryStatsFaxTranscodedCalls" or name == "csbHistoryStatsImsRxActiveCalls" or name == "csbHistoryStatsImsRxCallRenegotiationAttempts" or name == "csbHistoryStatsImsRxCallRenegotiationFailures" or name == "csbHistoryStatsImsRxCallSetupFailures" or name == "csbHistoryStatsIpsecCalls" or name == "csbHistoryStatsNonSrtpCalls" or name == "csbHistoryStatsRtpDisallowedFailures" or name == "csbHistoryStatsSrtpDisallowedFailures" or name == "csbHistoryStatsSrtpIwCalls" or name == "csbHistoryStatsSrtpNonIwCalls" or name == "csbHistoryStatsTimestamp" or name == "csbHistoryStatsTotalCallAttempts" or name == "csbHistoryStatsTotalCallUpdateFailure" or name == "csbHistoryStatsTotalTapsRequested" or name == "csbHistoryStatsTotalTapsSucceeded" or name == "csbHistroyStatsTranscodedCalls" or name == "csbHistroyStatsTransratedCalls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsInterval"):
                    self.csbhistorystatsinterval = value
                    self.csbhistorystatsinterval.value_namespace = name_space
                    self.csbhistorystatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsElements"):
                    self.csbhistorystatselements = value
                    self.csbhistorystatselements.value_namespace = name_space
                    self.csbhistorystatselements.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsActiveCallFailure"):
                    self.csbhistorystatsactivecallfailure = value
                    self.csbhistorystatsactivecallfailure.value_namespace = name_space
                    self.csbhistorystatsactivecallfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsActiveCalls"):
                    self.csbhistorystatsactivecalls = value
                    self.csbhistorystatsactivecalls.value_namespace = name_space
                    self.csbhistorystatsactivecalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsActiveE2EmergencyCalls"):
                    self.csbhistorystatsactivee2emergencycalls = value
                    self.csbhistorystatsactivee2emergencycalls.value_namespace = name_space
                    self.csbhistorystatsactivee2emergencycalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsActiveEmergencyCalls"):
                    self.csbhistorystatsactiveemergencycalls = value
                    self.csbhistorystatsactiveemergencycalls.value_namespace = name_space
                    self.csbhistorystatsactiveemergencycalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsActiveIpv6Calls"):
                    self.csbhistorystatsactiveipv6calls = value
                    self.csbhistorystatsactiveipv6calls.value_namespace = name_space
                    self.csbhistorystatsactiveipv6calls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsAudioTranscodedCalls"):
                    self.csbhistorystatsaudiotranscodedcalls = value
                    self.csbhistorystatsaudiotranscodedcalls.value_namespace = name_space
                    self.csbhistorystatsaudiotranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallMediaFailure"):
                    self.csbhistorystatscallmediafailure = value
                    self.csbhistorystatscallmediafailure.value_namespace = name_space
                    self.csbhistorystatscallmediafailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallResourceFailure"):
                    self.csbhistorystatscallresourcefailure = value
                    self.csbhistorystatscallresourcefailure.value_namespace = name_space
                    self.csbhistorystatscallresourcefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallRoutingFailure"):
                    self.csbhistorystatscallroutingfailure = value
                    self.csbhistorystatscallroutingfailure.value_namespace = name_space
                    self.csbhistorystatscallroutingfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACBandwidthFailure"):
                    self.csbhistorystatscallsetupcacbandwidthfailure = value
                    self.csbhistorystatscallsetupcacbandwidthfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcacbandwidthfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACCallLimitFailure"):
                    self.csbhistorystatscallsetupcaccalllimitfailure = value
                    self.csbhistorystatscallsetupcaccalllimitfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcaccalllimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACMediaLimitFailure"):
                    self.csbhistorystatscallsetupcacmedialimitfailure = value
                    self.csbhistorystatscallsetupcacmedialimitfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcacmedialimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACMediaUpdateFailure"):
                    self.csbhistorystatscallsetupcacmediaupdatefailure = value
                    self.csbhistorystatscallsetupcacmediaupdatefailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcacmediaupdatefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACPolicyFailure"):
                    self.csbhistorystatscallsetupcacpolicyfailure = value
                    self.csbhistorystatscallsetupcacpolicyfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcacpolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupCACRateLimitFailure"):
                    self.csbhistorystatscallsetupcacratelimitfailure = value
                    self.csbhistorystatscallsetupcacratelimitfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupcacratelimitfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupNAPolicyFailure"):
                    self.csbhistorystatscallsetupnapolicyfailure = value
                    self.csbhistorystatscallsetupnapolicyfailure.value_namespace = name_space
                    self.csbhistorystatscallsetupnapolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupPolicyFailure"):
                    self.csbhistorystatscallsetuppolicyfailure = value
                    self.csbhistorystatscallsetuppolicyfailure.value_namespace = name_space
                    self.csbhistorystatscallsetuppolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCallSetupRoutingPolicyFailure"):
                    self.csbhistorystatscallsetuproutingpolicyfailure = value
                    self.csbhistorystatscallsetuproutingpolicyfailure.value_namespace = name_space
                    self.csbhistorystatscallsetuproutingpolicyfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCongestionFailure"):
                    self.csbhistorystatscongestionfailure = value
                    self.csbhistorystatscongestionfailure.value_namespace = name_space
                    self.csbhistorystatscongestionfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsCurrentTaps"):
                    self.csbhistorystatscurrenttaps = value
                    self.csbhistorystatscurrenttaps.value_namespace = name_space
                    self.csbhistorystatscurrenttaps.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsDtmfIw2833Calls"):
                    self.csbhistorystatsdtmfiw2833calls = value
                    self.csbhistorystatsdtmfiw2833calls.value_namespace = name_space
                    self.csbhistorystatsdtmfiw2833calls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsDtmfIw2833InbandCalls"):
                    self.csbhistorystatsdtmfiw2833inbandcalls = value
                    self.csbhistorystatsdtmfiw2833inbandcalls.value_namespace = name_space
                    self.csbhistorystatsdtmfiw2833inbandcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsDtmfIwInbandCalls"):
                    self.csbhistorystatsdtmfiwinbandcalls = value
                    self.csbhistorystatsdtmfiwinbandcalls.value_namespace = name_space
                    self.csbhistorystatsdtmfiwinbandcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsFailedCallAttempts"):
                    self.csbhistorystatsfailedcallattempts = value
                    self.csbhistorystatsfailedcallattempts.value_namespace = name_space
                    self.csbhistorystatsfailedcallattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsFailSigFailure"):
                    self.csbhistorystatsfailsigfailure = value
                    self.csbhistorystatsfailsigfailure.value_namespace = name_space
                    self.csbhistorystatsfailsigfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsFaxTranscodedCalls"):
                    self.csbhistorystatsfaxtranscodedcalls = value
                    self.csbhistorystatsfaxtranscodedcalls.value_namespace = name_space
                    self.csbhistorystatsfaxtranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsImsRxActiveCalls"):
                    self.csbhistorystatsimsrxactivecalls = value
                    self.csbhistorystatsimsrxactivecalls.value_namespace = name_space
                    self.csbhistorystatsimsrxactivecalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsImsRxCallRenegotiationAttempts"):
                    self.csbhistorystatsimsrxcallrenegotiationattempts = value
                    self.csbhistorystatsimsrxcallrenegotiationattempts.value_namespace = name_space
                    self.csbhistorystatsimsrxcallrenegotiationattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsImsRxCallRenegotiationFailures"):
                    self.csbhistorystatsimsrxcallrenegotiationfailures = value
                    self.csbhistorystatsimsrxcallrenegotiationfailures.value_namespace = name_space
                    self.csbhistorystatsimsrxcallrenegotiationfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsImsRxCallSetupFailures"):
                    self.csbhistorystatsimsrxcallsetupfailures = value
                    self.csbhistorystatsimsrxcallsetupfailures.value_namespace = name_space
                    self.csbhistorystatsimsrxcallsetupfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsIpsecCalls"):
                    self.csbhistorystatsipseccalls = value
                    self.csbhistorystatsipseccalls.value_namespace = name_space
                    self.csbhistorystatsipseccalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsNonSrtpCalls"):
                    self.csbhistorystatsnonsrtpcalls = value
                    self.csbhistorystatsnonsrtpcalls.value_namespace = name_space
                    self.csbhistorystatsnonsrtpcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsRtpDisallowedFailures"):
                    self.csbhistorystatsrtpdisallowedfailures = value
                    self.csbhistorystatsrtpdisallowedfailures.value_namespace = name_space
                    self.csbhistorystatsrtpdisallowedfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsSrtpDisallowedFailures"):
                    self.csbhistorystatssrtpdisallowedfailures = value
                    self.csbhistorystatssrtpdisallowedfailures.value_namespace = name_space
                    self.csbhistorystatssrtpdisallowedfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsSrtpIwCalls"):
                    self.csbhistorystatssrtpiwcalls = value
                    self.csbhistorystatssrtpiwcalls.value_namespace = name_space
                    self.csbhistorystatssrtpiwcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsSrtpNonIwCalls"):
                    self.csbhistorystatssrtpnoniwcalls = value
                    self.csbhistorystatssrtpnoniwcalls.value_namespace = name_space
                    self.csbhistorystatssrtpnoniwcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsTimestamp"):
                    self.csbhistorystatstimestamp = value
                    self.csbhistorystatstimestamp.value_namespace = name_space
                    self.csbhistorystatstimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsTotalCallAttempts"):
                    self.csbhistorystatstotalcallattempts = value
                    self.csbhistorystatstotalcallattempts.value_namespace = name_space
                    self.csbhistorystatstotalcallattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsTotalCallUpdateFailure"):
                    self.csbhistorystatstotalcallupdatefailure = value
                    self.csbhistorystatstotalcallupdatefailure.value_namespace = name_space
                    self.csbhistorystatstotalcallupdatefailure.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsTotalTapsRequested"):
                    self.csbhistorystatstotaltapsrequested = value
                    self.csbhistorystatstotaltapsrequested.value_namespace = name_space
                    self.csbhistorystatstotaltapsrequested.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistoryStatsTotalTapsSucceeded"):
                    self.csbhistorystatstotaltapssucceeded = value
                    self.csbhistorystatstotaltapssucceeded.value_namespace = name_space
                    self.csbhistorystatstotaltapssucceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistroyStatsTranscodedCalls"):
                    self.csbhistroystatstranscodedcalls = value
                    self.csbhistroystatstranscodedcalls.value_namespace = name_space
                    self.csbhistroystatstranscodedcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbHistroyStatsTransratedCalls"):
                    self.csbhistroystatstransratedcalls = value
                    self.csbhistroystatstransratedcalls.value_namespace = name_space
                    self.csbhistroystatstransratedcalls.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbhistorystatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbhistorystatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbHistoryStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbHistoryStatsEntry"):
                for c in self.csbhistorystatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbhistorystatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbHistoryStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csbperflowstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable, self).__init__()

            self.yang_name = "csbPerFlowStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbperflowstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable, self).__setattr__(name, value)


        class Csbperflowstatsentry(Entity):
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
            	**type**\:   :py:class:`Csbperflowstatssideid <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.Csbperflowstatssideid>`
            
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
            	**type**\:   :py:class:`Csbperflowstatsflowtype <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.Csbperflowstatsflowtype>`
            
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry, self).__init__()

                self.yang_name = "csbPerFlowStatsEntry"
                self.yang_parent_name = "csbPerFlowStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbperflowstatsvdbeid = YLeaf(YType.int32, "csbPerFlowStatsVdbeId")

                self.csbperflowstatsgateid = YLeaf(YType.int32, "csbPerFlowStatsGateId")

                self.csbperflowstatsflowpairid = YLeaf(YType.int32, "csbPerFlowStatsFlowPairId")

                self.csbperflowstatssideid = YLeaf(YType.enumeration, "csbPerFlowStatsSideId")

                self.csbperflowstatsadrstatus = YLeaf(YType.str, "csbPerFlowStatsAdrStatus")

                self.csbperflowstatsdscpsettings = YLeaf(YType.str, "csbPerFlowStatsDscpSettings")

                self.csbperflowstatsepjitter = YLeaf(YType.uint64, "csbPerFlowStatsEPJitter")

                self.csbperflowstatsflowtype = YLeaf(YType.enumeration, "csbPerFlowStatsFlowType")

                self.csbperflowstatsqasettings = YLeaf(YType.str, "csbPerFlowStatsQASettings")

                self.csbperflowstatsrtcppktslost = YLeaf(YType.uint64, "csbPerFlowStatsRTCPPktsLost")

                self.csbperflowstatsrtcppktsrcvd = YLeaf(YType.uint64, "csbPerFlowStatsRTCPPktsRcvd")

                self.csbperflowstatsrtcppktssent = YLeaf(YType.uint64, "csbPerFlowStatsRTCPPktsSent")

                self.csbperflowstatsrtpoctetsdiscard = YLeaf(YType.uint64, "csbPerFlowStatsRTPOctetsDiscard")

                self.csbperflowstatsrtpoctetsrcvd = YLeaf(YType.uint64, "csbPerFlowStatsRTPOctetsRcvd")

                self.csbperflowstatsrtpoctetssent = YLeaf(YType.uint64, "csbPerFlowStatsRTPOctetsSent")

                self.csbperflowstatsrtppktsdiscard = YLeaf(YType.uint64, "csbPerFlowStatsRTPPktsDiscard")

                self.csbperflowstatsrtppktslost = YLeaf(YType.uint64, "csbPerFlowStatsRTPPktsLost")

                self.csbperflowstatsrtppktsrcvd = YLeaf(YType.uint64, "csbPerFlowStatsRTPPktsRcvd")

                self.csbperflowstatsrtppktssent = YLeaf(YType.uint64, "csbPerFlowStatsRTPPktsSent")

                self.csbperflowstatstmanpermbs = YLeaf(YType.uint32, "csbPerFlowStatsTmanPerMbs")

                self.csbperflowstatstmanpersdr = YLeaf(YType.uint32, "csbPerFlowStatsTmanPerSdr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbperflowstatsvdbeid",
                                "csbperflowstatsgateid",
                                "csbperflowstatsflowpairid",
                                "csbperflowstatssideid",
                                "csbperflowstatsadrstatus",
                                "csbperflowstatsdscpsettings",
                                "csbperflowstatsepjitter",
                                "csbperflowstatsflowtype",
                                "csbperflowstatsqasettings",
                                "csbperflowstatsrtcppktslost",
                                "csbperflowstatsrtcppktsrcvd",
                                "csbperflowstatsrtcppktssent",
                                "csbperflowstatsrtpoctetsdiscard",
                                "csbperflowstatsrtpoctetsrcvd",
                                "csbperflowstatsrtpoctetssent",
                                "csbperflowstatsrtppktsdiscard",
                                "csbperflowstatsrtppktslost",
                                "csbperflowstatsrtppktsrcvd",
                                "csbperflowstatsrtppktssent",
                                "csbperflowstatstmanpermbs",
                                "csbperflowstatstmanpersdr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry, self).__setattr__(name, value)

            class Csbperflowstatsflowtype(Enum):
                """
                Csbperflowstatsflowtype

                This object indicates the type of the flow, like media flow,

                signaling flow etc.

                .. data:: media = 1

                .. data:: signalling = 2

                """

                media = Enum.YLeaf(1, "media")

                signalling = Enum.YLeaf(2, "signalling")


            class Csbperflowstatssideid(Enum):
                """
                Csbperflowstatssideid

                This object identifies the index corresponding to side of flow

                pair either side A or side B. This object also acts as an index

                for the table.

                .. data:: sideA = 1

                .. data:: sideB = 2

                """

                sideA = Enum.YLeaf(1, "sideA")

                sideB = Enum.YLeaf(2, "sideB")


            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbperflowstatsvdbeid.is_set or
                    self.csbperflowstatsgateid.is_set or
                    self.csbperflowstatsflowpairid.is_set or
                    self.csbperflowstatssideid.is_set or
                    self.csbperflowstatsadrstatus.is_set or
                    self.csbperflowstatsdscpsettings.is_set or
                    self.csbperflowstatsepjitter.is_set or
                    self.csbperflowstatsflowtype.is_set or
                    self.csbperflowstatsqasettings.is_set or
                    self.csbperflowstatsrtcppktslost.is_set or
                    self.csbperflowstatsrtcppktsrcvd.is_set or
                    self.csbperflowstatsrtcppktssent.is_set or
                    self.csbperflowstatsrtpoctetsdiscard.is_set or
                    self.csbperflowstatsrtpoctetsrcvd.is_set or
                    self.csbperflowstatsrtpoctetssent.is_set or
                    self.csbperflowstatsrtppktsdiscard.is_set or
                    self.csbperflowstatsrtppktslost.is_set or
                    self.csbperflowstatsrtppktsrcvd.is_set or
                    self.csbperflowstatsrtppktssent.is_set or
                    self.csbperflowstatstmanpermbs.is_set or
                    self.csbperflowstatstmanpersdr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbperflowstatsvdbeid.yfilter != YFilter.not_set or
                    self.csbperflowstatsgateid.yfilter != YFilter.not_set or
                    self.csbperflowstatsflowpairid.yfilter != YFilter.not_set or
                    self.csbperflowstatssideid.yfilter != YFilter.not_set or
                    self.csbperflowstatsadrstatus.yfilter != YFilter.not_set or
                    self.csbperflowstatsdscpsettings.yfilter != YFilter.not_set or
                    self.csbperflowstatsepjitter.yfilter != YFilter.not_set or
                    self.csbperflowstatsflowtype.yfilter != YFilter.not_set or
                    self.csbperflowstatsqasettings.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtcppktslost.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtcppktsrcvd.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtcppktssent.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtpoctetsdiscard.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtpoctetsrcvd.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtpoctetssent.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtppktsdiscard.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtppktslost.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtppktsrcvd.yfilter != YFilter.not_set or
                    self.csbperflowstatsrtppktssent.yfilter != YFilter.not_set or
                    self.csbperflowstatstmanpermbs.yfilter != YFilter.not_set or
                    self.csbperflowstatstmanpersdr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbPerFlowStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbPerFlowStatsVdbeId='" + self.csbperflowstatsvdbeid.get() + "']" + "[csbPerFlowStatsGateId='" + self.csbperflowstatsgateid.get() + "']" + "[csbPerFlowStatsFlowPairId='" + self.csbperflowstatsflowpairid.get() + "']" + "[csbPerFlowStatsSideId='" + self.csbperflowstatssideid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbPerFlowStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbperflowstatsvdbeid.is_set or self.csbperflowstatsvdbeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsvdbeid.get_name_leafdata())
                if (self.csbperflowstatsgateid.is_set or self.csbperflowstatsgateid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsgateid.get_name_leafdata())
                if (self.csbperflowstatsflowpairid.is_set or self.csbperflowstatsflowpairid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsflowpairid.get_name_leafdata())
                if (self.csbperflowstatssideid.is_set or self.csbperflowstatssideid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatssideid.get_name_leafdata())
                if (self.csbperflowstatsadrstatus.is_set or self.csbperflowstatsadrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsadrstatus.get_name_leafdata())
                if (self.csbperflowstatsdscpsettings.is_set or self.csbperflowstatsdscpsettings.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsdscpsettings.get_name_leafdata())
                if (self.csbperflowstatsepjitter.is_set or self.csbperflowstatsepjitter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsepjitter.get_name_leafdata())
                if (self.csbperflowstatsflowtype.is_set or self.csbperflowstatsflowtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsflowtype.get_name_leafdata())
                if (self.csbperflowstatsqasettings.is_set or self.csbperflowstatsqasettings.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsqasettings.get_name_leafdata())
                if (self.csbperflowstatsrtcppktslost.is_set or self.csbperflowstatsrtcppktslost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtcppktslost.get_name_leafdata())
                if (self.csbperflowstatsrtcppktsrcvd.is_set or self.csbperflowstatsrtcppktsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtcppktsrcvd.get_name_leafdata())
                if (self.csbperflowstatsrtcppktssent.is_set or self.csbperflowstatsrtcppktssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtcppktssent.get_name_leafdata())
                if (self.csbperflowstatsrtpoctetsdiscard.is_set or self.csbperflowstatsrtpoctetsdiscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtpoctetsdiscard.get_name_leafdata())
                if (self.csbperflowstatsrtpoctetsrcvd.is_set or self.csbperflowstatsrtpoctetsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtpoctetsrcvd.get_name_leafdata())
                if (self.csbperflowstatsrtpoctetssent.is_set or self.csbperflowstatsrtpoctetssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtpoctetssent.get_name_leafdata())
                if (self.csbperflowstatsrtppktsdiscard.is_set or self.csbperflowstatsrtppktsdiscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtppktsdiscard.get_name_leafdata())
                if (self.csbperflowstatsrtppktslost.is_set or self.csbperflowstatsrtppktslost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtppktslost.get_name_leafdata())
                if (self.csbperflowstatsrtppktsrcvd.is_set or self.csbperflowstatsrtppktsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtppktsrcvd.get_name_leafdata())
                if (self.csbperflowstatsrtppktssent.is_set or self.csbperflowstatsrtppktssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatsrtppktssent.get_name_leafdata())
                if (self.csbperflowstatstmanpermbs.is_set or self.csbperflowstatstmanpermbs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatstmanpermbs.get_name_leafdata())
                if (self.csbperflowstatstmanpersdr.is_set or self.csbperflowstatstmanpersdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbperflowstatstmanpersdr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbPerFlowStatsVdbeId" or name == "csbPerFlowStatsGateId" or name == "csbPerFlowStatsFlowPairId" or name == "csbPerFlowStatsSideId" or name == "csbPerFlowStatsAdrStatus" or name == "csbPerFlowStatsDscpSettings" or name == "csbPerFlowStatsEPJitter" or name == "csbPerFlowStatsFlowType" or name == "csbPerFlowStatsQASettings" or name == "csbPerFlowStatsRTCPPktsLost" or name == "csbPerFlowStatsRTCPPktsRcvd" or name == "csbPerFlowStatsRTCPPktsSent" or name == "csbPerFlowStatsRTPOctetsDiscard" or name == "csbPerFlowStatsRTPOctetsRcvd" or name == "csbPerFlowStatsRTPOctetsSent" or name == "csbPerFlowStatsRTPPktsDiscard" or name == "csbPerFlowStatsRTPPktsLost" or name == "csbPerFlowStatsRTPPktsRcvd" or name == "csbPerFlowStatsRTPPktsSent" or name == "csbPerFlowStatsTmanPerMbs" or name == "csbPerFlowStatsTmanPerSdr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsVdbeId"):
                    self.csbperflowstatsvdbeid = value
                    self.csbperflowstatsvdbeid.value_namespace = name_space
                    self.csbperflowstatsvdbeid.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsGateId"):
                    self.csbperflowstatsgateid = value
                    self.csbperflowstatsgateid.value_namespace = name_space
                    self.csbperflowstatsgateid.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsFlowPairId"):
                    self.csbperflowstatsflowpairid = value
                    self.csbperflowstatsflowpairid.value_namespace = name_space
                    self.csbperflowstatsflowpairid.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsSideId"):
                    self.csbperflowstatssideid = value
                    self.csbperflowstatssideid.value_namespace = name_space
                    self.csbperflowstatssideid.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsAdrStatus"):
                    self.csbperflowstatsadrstatus = value
                    self.csbperflowstatsadrstatus.value_namespace = name_space
                    self.csbperflowstatsadrstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsDscpSettings"):
                    self.csbperflowstatsdscpsettings = value
                    self.csbperflowstatsdscpsettings.value_namespace = name_space
                    self.csbperflowstatsdscpsettings.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsEPJitter"):
                    self.csbperflowstatsepjitter = value
                    self.csbperflowstatsepjitter.value_namespace = name_space
                    self.csbperflowstatsepjitter.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsFlowType"):
                    self.csbperflowstatsflowtype = value
                    self.csbperflowstatsflowtype.value_namespace = name_space
                    self.csbperflowstatsflowtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsQASettings"):
                    self.csbperflowstatsqasettings = value
                    self.csbperflowstatsqasettings.value_namespace = name_space
                    self.csbperflowstatsqasettings.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTCPPktsLost"):
                    self.csbperflowstatsrtcppktslost = value
                    self.csbperflowstatsrtcppktslost.value_namespace = name_space
                    self.csbperflowstatsrtcppktslost.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTCPPktsRcvd"):
                    self.csbperflowstatsrtcppktsrcvd = value
                    self.csbperflowstatsrtcppktsrcvd.value_namespace = name_space
                    self.csbperflowstatsrtcppktsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTCPPktsSent"):
                    self.csbperflowstatsrtcppktssent = value
                    self.csbperflowstatsrtcppktssent.value_namespace = name_space
                    self.csbperflowstatsrtcppktssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPOctetsDiscard"):
                    self.csbperflowstatsrtpoctetsdiscard = value
                    self.csbperflowstatsrtpoctetsdiscard.value_namespace = name_space
                    self.csbperflowstatsrtpoctetsdiscard.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPOctetsRcvd"):
                    self.csbperflowstatsrtpoctetsrcvd = value
                    self.csbperflowstatsrtpoctetsrcvd.value_namespace = name_space
                    self.csbperflowstatsrtpoctetsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPOctetsSent"):
                    self.csbperflowstatsrtpoctetssent = value
                    self.csbperflowstatsrtpoctetssent.value_namespace = name_space
                    self.csbperflowstatsrtpoctetssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPPktsDiscard"):
                    self.csbperflowstatsrtppktsdiscard = value
                    self.csbperflowstatsrtppktsdiscard.value_namespace = name_space
                    self.csbperflowstatsrtppktsdiscard.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPPktsLost"):
                    self.csbperflowstatsrtppktslost = value
                    self.csbperflowstatsrtppktslost.value_namespace = name_space
                    self.csbperflowstatsrtppktslost.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPPktsRcvd"):
                    self.csbperflowstatsrtppktsrcvd = value
                    self.csbperflowstatsrtppktsrcvd.value_namespace = name_space
                    self.csbperflowstatsrtppktsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsRTPPktsSent"):
                    self.csbperflowstatsrtppktssent = value
                    self.csbperflowstatsrtppktssent.value_namespace = name_space
                    self.csbperflowstatsrtppktssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsTmanPerMbs"):
                    self.csbperflowstatstmanpermbs = value
                    self.csbperflowstatstmanpermbs.value_namespace = name_space
                    self.csbperflowstatstmanpermbs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbPerFlowStatsTmanPerSdr"):
                    self.csbperflowstatstmanpersdr = value
                    self.csbperflowstatstmanpersdr.value_namespace = name_space
                    self.csbperflowstatstmanpersdr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbperflowstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbperflowstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbPerFlowStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbPerFlowStatsEntry"):
                for c in self.csbperflowstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbperflowstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbPerFlowStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csbh248Statsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'
        _revision = '2010-09-03'

        def __init__(self):
            super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable, self).__init__()

            self.yang_name = "csbH248StatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbh248statsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable, self).__setattr__(name, value)


        class Csbh248Statsentry(Entity):
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry, self).__init__()

                self.yang_name = "csbH248StatsEntry"
                self.yang_parent_name = "csbH248StatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbh248statsctrlrindex = YLeaf(YType.int32, "csbH248StatsCtrlrIndex")

                self.csbh248statsestablishedtime = YLeaf(YType.str, "csbH248StatsEstablishedTime")

                self.csbh248statslt = YLeaf(YType.uint32, "csbH248StatsLT")

                self.csbh248statsrepliesrcvd = YLeaf(YType.uint32, "csbH248StatsRepliesRcvd")

                self.csbh248statsrepliesretried = YLeaf(YType.uint32, "csbH248StatsRepliesRetried")

                self.csbh248statsrepliessent = YLeaf(YType.uint32, "csbH248StatsRepliesSent")

                self.csbh248statsrequestsfailed = YLeaf(YType.uint32, "csbH248StatsRequestsFailed")

                self.csbh248statsrequestsrcvd = YLeaf(YType.uint32, "csbH248StatsRequestsRcvd")

                self.csbh248statsrequestsretried = YLeaf(YType.uint32, "csbH248StatsRequestsRetried")

                self.csbh248statsrequestssent = YLeaf(YType.uint32, "csbH248StatsRequestsSent")

                self.csbh248statsrtt = YLeaf(YType.uint32, "csbH248StatsRTT")

                self.csbh248statssegpktsrcvd = YLeaf(YType.uint32, "csbH248StatsSegPktsRcvd")

                self.csbh248statssegpktssent = YLeaf(YType.uint32, "csbH248StatsSegPktsSent")

                self.csbh248statstmaxtimeoutval = YLeaf(YType.int32, "csbH248StatsTMaxTimeoutVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbh248statsctrlrindex",
                                "csbh248statsestablishedtime",
                                "csbh248statslt",
                                "csbh248statsrepliesrcvd",
                                "csbh248statsrepliesretried",
                                "csbh248statsrepliessent",
                                "csbh248statsrequestsfailed",
                                "csbh248statsrequestsrcvd",
                                "csbh248statsrequestsretried",
                                "csbh248statsrequestssent",
                                "csbh248statsrtt",
                                "csbh248statssegpktsrcvd",
                                "csbh248statssegpktssent",
                                "csbh248statstmaxtimeoutval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbh248statsctrlrindex.is_set or
                    self.csbh248statsestablishedtime.is_set or
                    self.csbh248statslt.is_set or
                    self.csbh248statsrepliesrcvd.is_set or
                    self.csbh248statsrepliesretried.is_set or
                    self.csbh248statsrepliessent.is_set or
                    self.csbh248statsrequestsfailed.is_set or
                    self.csbh248statsrequestsrcvd.is_set or
                    self.csbh248statsrequestsretried.is_set or
                    self.csbh248statsrequestssent.is_set or
                    self.csbh248statsrtt.is_set or
                    self.csbh248statssegpktsrcvd.is_set or
                    self.csbh248statssegpktssent.is_set or
                    self.csbh248statstmaxtimeoutval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbh248statsctrlrindex.yfilter != YFilter.not_set or
                    self.csbh248statsestablishedtime.yfilter != YFilter.not_set or
                    self.csbh248statslt.yfilter != YFilter.not_set or
                    self.csbh248statsrepliesrcvd.yfilter != YFilter.not_set or
                    self.csbh248statsrepliesretried.yfilter != YFilter.not_set or
                    self.csbh248statsrepliessent.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsfailed.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsrcvd.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsretried.yfilter != YFilter.not_set or
                    self.csbh248statsrequestssent.yfilter != YFilter.not_set or
                    self.csbh248statsrtt.yfilter != YFilter.not_set or
                    self.csbh248statssegpktsrcvd.yfilter != YFilter.not_set or
                    self.csbh248statssegpktssent.yfilter != YFilter.not_set or
                    self.csbh248statstmaxtimeoutval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbH248StatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbH248StatsCtrlrIndex='" + self.csbh248statsctrlrindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbH248StatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbh248statsctrlrindex.is_set or self.csbh248statsctrlrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsctrlrindex.get_name_leafdata())
                if (self.csbh248statsestablishedtime.is_set or self.csbh248statsestablishedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsestablishedtime.get_name_leafdata())
                if (self.csbh248statslt.is_set or self.csbh248statslt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statslt.get_name_leafdata())
                if (self.csbh248statsrepliesrcvd.is_set or self.csbh248statsrepliesrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliesrcvd.get_name_leafdata())
                if (self.csbh248statsrepliesretried.is_set or self.csbh248statsrepliesretried.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliesretried.get_name_leafdata())
                if (self.csbh248statsrepliessent.is_set or self.csbh248statsrepliessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliessent.get_name_leafdata())
                if (self.csbh248statsrequestsfailed.is_set or self.csbh248statsrequestsfailed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsfailed.get_name_leafdata())
                if (self.csbh248statsrequestsrcvd.is_set or self.csbh248statsrequestsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsrcvd.get_name_leafdata())
                if (self.csbh248statsrequestsretried.is_set or self.csbh248statsrequestsretried.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsretried.get_name_leafdata())
                if (self.csbh248statsrequestssent.is_set or self.csbh248statsrequestssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestssent.get_name_leafdata())
                if (self.csbh248statsrtt.is_set or self.csbh248statsrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrtt.get_name_leafdata())
                if (self.csbh248statssegpktsrcvd.is_set or self.csbh248statssegpktsrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statssegpktsrcvd.get_name_leafdata())
                if (self.csbh248statssegpktssent.is_set or self.csbh248statssegpktssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statssegpktssent.get_name_leafdata())
                if (self.csbh248statstmaxtimeoutval.is_set or self.csbh248statstmaxtimeoutval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statstmaxtimeoutval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbH248StatsCtrlrIndex" or name == "csbH248StatsEstablishedTime" or name == "csbH248StatsLT" or name == "csbH248StatsRepliesRcvd" or name == "csbH248StatsRepliesRetried" or name == "csbH248StatsRepliesSent" or name == "csbH248StatsRequestsFailed" or name == "csbH248StatsRequestsRcvd" or name == "csbH248StatsRequestsRetried" or name == "csbH248StatsRequestsSent" or name == "csbH248StatsRTT" or name == "csbH248StatsSegPktsRcvd" or name == "csbH248StatsSegPktsSent" or name == "csbH248StatsTMaxTimeoutVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsCtrlrIndex"):
                    self.csbh248statsctrlrindex = value
                    self.csbh248statsctrlrindex.value_namespace = name_space
                    self.csbh248statsctrlrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsEstablishedTime"):
                    self.csbh248statsestablishedtime = value
                    self.csbh248statsestablishedtime.value_namespace = name_space
                    self.csbh248statsestablishedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsLT"):
                    self.csbh248statslt = value
                    self.csbh248statslt.value_namespace = name_space
                    self.csbh248statslt.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesRcvd"):
                    self.csbh248statsrepliesrcvd = value
                    self.csbh248statsrepliesrcvd.value_namespace = name_space
                    self.csbh248statsrepliesrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesRetried"):
                    self.csbh248statsrepliesretried = value
                    self.csbh248statsrepliesretried.value_namespace = name_space
                    self.csbh248statsrepliesretried.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesSent"):
                    self.csbh248statsrepliessent = value
                    self.csbh248statsrepliessent.value_namespace = name_space
                    self.csbh248statsrepliessent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsFailed"):
                    self.csbh248statsrequestsfailed = value
                    self.csbh248statsrequestsfailed.value_namespace = name_space
                    self.csbh248statsrequestsfailed.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsRcvd"):
                    self.csbh248statsrequestsrcvd = value
                    self.csbh248statsrequestsrcvd.value_namespace = name_space
                    self.csbh248statsrequestsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsRetried"):
                    self.csbh248statsrequestsretried = value
                    self.csbh248statsrequestsretried.value_namespace = name_space
                    self.csbh248statsrequestsretried.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsSent"):
                    self.csbh248statsrequestssent = value
                    self.csbh248statsrequestssent.value_namespace = name_space
                    self.csbh248statsrequestssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRTT"):
                    self.csbh248statsrtt = value
                    self.csbh248statsrtt.value_namespace = name_space
                    self.csbh248statsrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsSegPktsRcvd"):
                    self.csbh248statssegpktsrcvd = value
                    self.csbh248statssegpktsrcvd.value_namespace = name_space
                    self.csbh248statssegpktsrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsSegPktsSent"):
                    self.csbh248statssegpktssent = value
                    self.csbh248statssegpktssent.value_namespace = name_space
                    self.csbh248statssegpktssent.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsTMaxTimeoutVal"):
                    self.csbh248statstmaxtimeoutval = value
                    self.csbh248statstmaxtimeoutval.value_namespace = name_space
                    self.csbh248statstmaxtimeoutval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbh248statsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbh248statsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbH248StatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbH248StatsEntry"):
                for c in self.csbh248statsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbh248statsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbH248StatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbh248Statsrev1Table(Entity):
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
            super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table, self).__init__()

            self.yang_name = "csbH248StatsRev1Table"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB"

            self.csbh248statsrev1entry = YList(self)

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
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table, self).__setattr__(name, value)


        class Csbh248Statsrev1Entry(Entity):
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
                super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry, self).__init__()

                self.yang_name = "csbH248StatsRev1Entry"
                self.yang_parent_name = "csbH248StatsRev1Table"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbh248statsvdbeid = YLeaf(YType.int32, "csbH248StatsVdbeId")

                self.csbh248statsestablishedtimerev1 = YLeaf(YType.str, "csbH248StatsEstablishedTimeRev1")

                self.csbh248statsltrev1 = YLeaf(YType.uint32, "csbH248StatsLTRev1")

                self.csbh248statsrepliesrcvdrev1 = YLeaf(YType.uint32, "csbH248StatsRepliesRcvdRev1")

                self.csbh248statsrepliesretriedrev1 = YLeaf(YType.uint32, "csbH248StatsRepliesRetriedRev1")

                self.csbh248statsrepliessentrev1 = YLeaf(YType.uint32, "csbH248StatsRepliesSentRev1")

                self.csbh248statsrequestsfailedrev1 = YLeaf(YType.uint32, "csbH248StatsRequestsFailedRev1")

                self.csbh248statsrequestsrcvdrev1 = YLeaf(YType.uint32, "csbH248StatsRequestsRcvdRev1")

                self.csbh248statsrequestsretriedrev1 = YLeaf(YType.uint32, "csbH248StatsRequestsRetriedRev1")

                self.csbh248statsrequestssentrev1 = YLeaf(YType.uint32, "csbH248StatsRequestsSentRev1")

                self.csbh248statsrttrev1 = YLeaf(YType.uint32, "csbH248StatsRTTRev1")

                self.csbh248statssegpktsrcvdrev1 = YLeaf(YType.uint32, "csbH248StatsSegPktsRcvdRev1")

                self.csbh248statssegpktssentrev1 = YLeaf(YType.uint32, "csbH248StatsSegPktsSentRev1")

                self.csbh248statstmaxtimeoutvalrev1 = YLeaf(YType.int32, "csbH248StatsTMaxTimeoutValRev1")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csbcallstatsinstanceindex",
                                "csbcallstatsserviceindex",
                                "csbh248statsvdbeid",
                                "csbh248statsestablishedtimerev1",
                                "csbh248statsltrev1",
                                "csbh248statsrepliesrcvdrev1",
                                "csbh248statsrepliesretriedrev1",
                                "csbh248statsrepliessentrev1",
                                "csbh248statsrequestsfailedrev1",
                                "csbh248statsrequestsrcvdrev1",
                                "csbh248statsrequestsretriedrev1",
                                "csbh248statsrequestssentrev1",
                                "csbh248statsrttrev1",
                                "csbh248statssegpktsrcvdrev1",
                                "csbh248statssegpktssentrev1",
                                "csbh248statstmaxtimeoutvalrev1") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbh248statsvdbeid.is_set or
                    self.csbh248statsestablishedtimerev1.is_set or
                    self.csbh248statsltrev1.is_set or
                    self.csbh248statsrepliesrcvdrev1.is_set or
                    self.csbh248statsrepliesretriedrev1.is_set or
                    self.csbh248statsrepliessentrev1.is_set or
                    self.csbh248statsrequestsfailedrev1.is_set or
                    self.csbh248statsrequestsrcvdrev1.is_set or
                    self.csbh248statsrequestsretriedrev1.is_set or
                    self.csbh248statsrequestssentrev1.is_set or
                    self.csbh248statsrttrev1.is_set or
                    self.csbh248statssegpktsrcvdrev1.is_set or
                    self.csbh248statssegpktssentrev1.is_set or
                    self.csbh248statstmaxtimeoutvalrev1.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbh248statsvdbeid.yfilter != YFilter.not_set or
                    self.csbh248statsestablishedtimerev1.yfilter != YFilter.not_set or
                    self.csbh248statsltrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrepliesrcvdrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrepliesretriedrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrepliessentrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsfailedrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsrcvdrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrequestsretriedrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrequestssentrev1.yfilter != YFilter.not_set or
                    self.csbh248statsrttrev1.yfilter != YFilter.not_set or
                    self.csbh248statssegpktsrcvdrev1.yfilter != YFilter.not_set or
                    self.csbh248statssegpktssentrev1.yfilter != YFilter.not_set or
                    self.csbh248statstmaxtimeoutvalrev1.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbH248StatsRev1Entry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbH248StatsVdbeId='" + self.csbh248statsvdbeid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/csbH248StatsRev1Table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbh248statsvdbeid.is_set or self.csbh248statsvdbeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsvdbeid.get_name_leafdata())
                if (self.csbh248statsestablishedtimerev1.is_set or self.csbh248statsestablishedtimerev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsestablishedtimerev1.get_name_leafdata())
                if (self.csbh248statsltrev1.is_set or self.csbh248statsltrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsltrev1.get_name_leafdata())
                if (self.csbh248statsrepliesrcvdrev1.is_set or self.csbh248statsrepliesrcvdrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliesrcvdrev1.get_name_leafdata())
                if (self.csbh248statsrepliesretriedrev1.is_set or self.csbh248statsrepliesretriedrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliesretriedrev1.get_name_leafdata())
                if (self.csbh248statsrepliessentrev1.is_set or self.csbh248statsrepliessentrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrepliessentrev1.get_name_leafdata())
                if (self.csbh248statsrequestsfailedrev1.is_set or self.csbh248statsrequestsfailedrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsfailedrev1.get_name_leafdata())
                if (self.csbh248statsrequestsrcvdrev1.is_set or self.csbh248statsrequestsrcvdrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsrcvdrev1.get_name_leafdata())
                if (self.csbh248statsrequestsretriedrev1.is_set or self.csbh248statsrequestsretriedrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestsretriedrev1.get_name_leafdata())
                if (self.csbh248statsrequestssentrev1.is_set or self.csbh248statsrequestssentrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrequestssentrev1.get_name_leafdata())
                if (self.csbh248statsrttrev1.is_set or self.csbh248statsrttrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statsrttrev1.get_name_leafdata())
                if (self.csbh248statssegpktsrcvdrev1.is_set or self.csbh248statssegpktsrcvdrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statssegpktsrcvdrev1.get_name_leafdata())
                if (self.csbh248statssegpktssentrev1.is_set or self.csbh248statssegpktssentrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statssegpktssentrev1.get_name_leafdata())
                if (self.csbh248statstmaxtimeoutvalrev1.is_set or self.csbh248statstmaxtimeoutvalrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbh248statstmaxtimeoutvalrev1.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbH248StatsVdbeId" or name == "csbH248StatsEstablishedTimeRev1" or name == "csbH248StatsLTRev1" or name == "csbH248StatsRepliesRcvdRev1" or name == "csbH248StatsRepliesRetriedRev1" or name == "csbH248StatsRepliesSentRev1" or name == "csbH248StatsRequestsFailedRev1" or name == "csbH248StatsRequestsRcvdRev1" or name == "csbH248StatsRequestsRetriedRev1" or name == "csbH248StatsRequestsSentRev1" or name == "csbH248StatsRTTRev1" or name == "csbH248StatsSegPktsRcvdRev1" or name == "csbH248StatsSegPktsSentRev1" or name == "csbH248StatsTMaxTimeoutValRev1"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csbCallStatsInstanceIndex"):
                    self.csbcallstatsinstanceindex = value
                    self.csbcallstatsinstanceindex.value_namespace = name_space
                    self.csbcallstatsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbCallStatsServiceIndex"):
                    self.csbcallstatsserviceindex = value
                    self.csbcallstatsserviceindex.value_namespace = name_space
                    self.csbcallstatsserviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsVdbeId"):
                    self.csbh248statsvdbeid = value
                    self.csbh248statsvdbeid.value_namespace = name_space
                    self.csbh248statsvdbeid.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsEstablishedTimeRev1"):
                    self.csbh248statsestablishedtimerev1 = value
                    self.csbh248statsestablishedtimerev1.value_namespace = name_space
                    self.csbh248statsestablishedtimerev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsLTRev1"):
                    self.csbh248statsltrev1 = value
                    self.csbh248statsltrev1.value_namespace = name_space
                    self.csbh248statsltrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesRcvdRev1"):
                    self.csbh248statsrepliesrcvdrev1 = value
                    self.csbh248statsrepliesrcvdrev1.value_namespace = name_space
                    self.csbh248statsrepliesrcvdrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesRetriedRev1"):
                    self.csbh248statsrepliesretriedrev1 = value
                    self.csbh248statsrepliesretriedrev1.value_namespace = name_space
                    self.csbh248statsrepliesretriedrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRepliesSentRev1"):
                    self.csbh248statsrepliessentrev1 = value
                    self.csbh248statsrepliessentrev1.value_namespace = name_space
                    self.csbh248statsrepliessentrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsFailedRev1"):
                    self.csbh248statsrequestsfailedrev1 = value
                    self.csbh248statsrequestsfailedrev1.value_namespace = name_space
                    self.csbh248statsrequestsfailedrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsRcvdRev1"):
                    self.csbh248statsrequestsrcvdrev1 = value
                    self.csbh248statsrequestsrcvdrev1.value_namespace = name_space
                    self.csbh248statsrequestsrcvdrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsRetriedRev1"):
                    self.csbh248statsrequestsretriedrev1 = value
                    self.csbh248statsrequestsretriedrev1.value_namespace = name_space
                    self.csbh248statsrequestsretriedrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRequestsSentRev1"):
                    self.csbh248statsrequestssentrev1 = value
                    self.csbh248statsrequestssentrev1.value_namespace = name_space
                    self.csbh248statsrequestssentrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsRTTRev1"):
                    self.csbh248statsrttrev1 = value
                    self.csbh248statsrttrev1.value_namespace = name_space
                    self.csbh248statsrttrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsSegPktsRcvdRev1"):
                    self.csbh248statssegpktsrcvdrev1 = value
                    self.csbh248statssegpktsrcvdrev1.value_namespace = name_space
                    self.csbh248statssegpktsrcvdrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsSegPktsSentRev1"):
                    self.csbh248statssegpktssentrev1 = value
                    self.csbh248statssegpktssentrev1.value_namespace = name_space
                    self.csbh248statssegpktssentrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "csbH248StatsTMaxTimeoutValRev1"):
                    self.csbh248statstmaxtimeoutvalrev1 = value
                    self.csbh248statstmaxtimeoutvalrev1.value_namespace = name_space
                    self.csbh248statstmaxtimeoutvalrev1.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbh248statsrev1entry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbh248statsrev1entry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbH248StatsRev1Table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbH248StatsRev1Entry"):
                for c in self.csbh248statsrev1entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbh248statsrev1entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbH248StatsRev1Entry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.csbcallstatsinstancetable is not None and self.csbcallstatsinstancetable.has_data()) or
            (self.csbcallstatstable is not None and self.csbcallstatstable.has_data()) or
            (self.csbcurrperiodicstatstable is not None and self.csbcurrperiodicstatstable.has_data()) or
            (self.csbh248statsrev1table is not None and self.csbh248statsrev1table.has_data()) or
            (self.csbh248statstable is not None and self.csbh248statstable.has_data()) or
            (self.csbhistorystatstable is not None and self.csbhistorystatstable.has_data()) or
            (self.csbperflowstatstable is not None and self.csbperflowstatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.csbcallstatsinstancetable is not None and self.csbcallstatsinstancetable.has_operation()) or
            (self.csbcallstatstable is not None and self.csbcallstatstable.has_operation()) or
            (self.csbcurrperiodicstatstable is not None and self.csbcurrperiodicstatstable.has_operation()) or
            (self.csbh248statsrev1table is not None and self.csbh248statsrev1table.has_operation()) or
            (self.csbh248statstable is not None and self.csbh248statstable.has_operation()) or
            (self.csbhistorystatstable is not None and self.csbhistorystatstable.has_operation()) or
            (self.csbperflowstatstable is not None and self.csbperflowstatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB:CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB" + path_buffer

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

        if (child_yang_name == "csbCallStatsInstanceTable"):
            if (self.csbcallstatsinstancetable is None):
                self.csbcallstatsinstancetable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable()
                self.csbcallstatsinstancetable.parent = self
                self._children_name_map["csbcallstatsinstancetable"] = "csbCallStatsInstanceTable"
            return self.csbcallstatsinstancetable

        if (child_yang_name == "csbCallStatsTable"):
            if (self.csbcallstatstable is None):
                self.csbcallstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable()
                self.csbcallstatstable.parent = self
                self._children_name_map["csbcallstatstable"] = "csbCallStatsTable"
            return self.csbcallstatstable

        if (child_yang_name == "csbCurrPeriodicStatsTable"):
            if (self.csbcurrperiodicstatstable is None):
                self.csbcurrperiodicstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable()
                self.csbcurrperiodicstatstable.parent = self
                self._children_name_map["csbcurrperiodicstatstable"] = "csbCurrPeriodicStatsTable"
            return self.csbcurrperiodicstatstable

        if (child_yang_name == "csbH248StatsRev1Table"):
            if (self.csbh248statsrev1table is None):
                self.csbh248statsrev1table = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table()
                self.csbh248statsrev1table.parent = self
                self._children_name_map["csbh248statsrev1table"] = "csbH248StatsRev1Table"
            return self.csbh248statsrev1table

        if (child_yang_name == "csbH248StatsTable"):
            if (self.csbh248statstable is None):
                self.csbh248statstable = CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable()
                self.csbh248statstable.parent = self
                self._children_name_map["csbh248statstable"] = "csbH248StatsTable"
            return self.csbh248statstable

        if (child_yang_name == "csbHistoryStatsTable"):
            if (self.csbhistorystatstable is None):
                self.csbhistorystatstable = CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable()
                self.csbhistorystatstable.parent = self
                self._children_name_map["csbhistorystatstable"] = "csbHistoryStatsTable"
            return self.csbhistorystatstable

        if (child_yang_name == "csbPerFlowStatsTable"):
            if (self.csbperflowstatstable is None):
                self.csbperflowstatstable = CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable()
                self.csbperflowstatstable.parent = self
                self._children_name_map["csbperflowstatstable"] = "csbPerFlowStatsTable"
            return self.csbperflowstatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "csbCallStatsInstanceTable" or name == "csbCallStatsTable" or name == "csbCurrPeriodicStatsTable" or name == "csbH248StatsRev1Table" or name == "csbH248StatsTable" or name == "csbHistoryStatsTable" or name == "csbPerFlowStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoSessBorderCtrlrCallStatsMib()
        return self._top_entity

