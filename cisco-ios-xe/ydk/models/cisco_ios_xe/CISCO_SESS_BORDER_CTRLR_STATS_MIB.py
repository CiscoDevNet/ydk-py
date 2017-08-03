""" CISCO_SESS_BORDER_CTRLR_STATS_MIB 

The main purpose of this MIB is to define the statistics
information for Session Border Controller application. This MIB
categorizes the statistics information into following types\:
1. RADIUS Messages Statistics \- Represents statistics of
   various RADIUS messages for RADIUS servers with which the
   client (SBC) shares a secret.

2. Rf Billing Statistics\- Represents Rf billing statistics 
   information which monitors the messages sent per\-realm over
   IMS Rx interface by Rf billing manager(SBC).

3. SIP Statistics \- Represents SIP requests and various SIP
   responses on a SIP adjacency in a given interval.

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

Periodic Statistics \- Represents the SBC call statistics 
information for a particular time interval. E.g. you can 
specify that you want to retrieve statistics for a summary 
period of the current or previous 5 minutes, 15 minutes, hour, 
or day. The statistics for 5 minutes are divided into five 
minute intervals past the hour \- that is, at 0 minutes, 5 
minutes, 10 minutes... past the hour.  When you retrieve 
statistics for the current five minute period, you will be 
given statistics from the start of the interval to the current
time. When you retrieve statistics for the previous five 
minutes, you will be given the statistics for the entirety of 
the previous interval. For example, if it is currently 12\:43
\-  the current 5 minute statistics cover 12\:40 \- 12\:43

\-  the previous 5 minute statistics cover 12\:35 \- 12\:40

The other intervals work similarly.  15 minute statistics are 
divided into 15 minute intervals past the hour (0 minutes, 15 
minutes, 30 minutes, 45 minutes).  Hourly statistics are divided
into intervals on the hour. Daily statistics are divided into
intervals at 0\:00 each day. Therefore, if you retrieve the 
statistics at 12\:43 for each of these intervals, the periods
covered are as follows.  
\-     current 15 minutes\: 12\:30 \- 12\:43

\-     previous 15 minutes\: 12\:15 \- 12\:30

\-     current hour\: 12\:00 \- 12\:43

\-     last hour\: 11\:00 \- 12\:00

\-     current day\: 00\:00 \- 12\:43

\-     last day\: 00\:00 (the day before) \- 00\:00.


GLOSSARY
SBC\: Session Border Controller

CSB\: CISCO Session Border Controller

Adjacency\: An adjacency contains the system information to be
transmitted to next HOP.

ACR\: Accounting Request

ACA\: Accounting Accept

AVP\: Attribute\-Value Pairs

REFERENCES
1. CISCO Session Border Controller Documents and FAQ
http\://zed.cisco.com/confluence/display/SBC/SBC

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscosbcradiusclienttype(Enum):
    """
    Ciscosbcradiusclienttype

    This textual convention represents the type of RADIUS client.

    .. data:: authentication = 1

    .. data:: accounting = 2

    """

    authentication = Enum.YLeaf(1, "authentication")

    accounting = Enum.YLeaf(2, "accounting")


class Ciscosbcsipmethod(Enum):
    """
    Ciscosbcsipmethod

    This textual convention represents the various SIP Methods.

    .. data:: unknown = 1

    .. data:: ack = 2

    .. data:: bye = 3

    .. data:: cancel = 4

    .. data:: info = 5

    .. data:: invite = 6

    .. data:: message = 7

    .. data:: notify = 8

    .. data:: options = 9

    .. data:: prack = 10

    .. data:: refer = 11

    .. data:: register = 12

    .. data:: subscribe = 13

    .. data:: update = 14

    """

    unknown = Enum.YLeaf(1, "unknown")

    ack = Enum.YLeaf(2, "ack")

    bye = Enum.YLeaf(3, "bye")

    cancel = Enum.YLeaf(4, "cancel")

    info = Enum.YLeaf(5, "info")

    invite = Enum.YLeaf(6, "invite")

    message = Enum.YLeaf(7, "message")

    notify = Enum.YLeaf(8, "notify")

    options = Enum.YLeaf(9, "options")

    prack = Enum.YLeaf(10, "prack")

    refer = Enum.YLeaf(11, "refer")

    register = Enum.YLeaf(12, "register")

    subscribe = Enum.YLeaf(13, "subscribe")

    update = Enum.YLeaf(14, "update")



class CiscoSessBorderCtrlrStatsMib(Entity):
    """
    
    
    .. attribute:: csbradiusstatstable
    
    	This table has the reporting statistics of various RADIUS messages for RADIUS servers with which the client (SBC) shares a secret. Each entry in this table is identified by a  value of csbRadiusStatsEntIndex. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:   :py:class:`Csbradiusstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable>`
    
    .. attribute:: csbrfbillrealmstatstable
    
    	This table describes the Rf billing statistics information which monitors the messages sent per\-realm by Rf billing  manager(SBC). SBC sends Rf billing data using Diameter as a transport protocol. Rf billing uses only ACR and ACA Diameter messages for the transport of billing data. The Accounting\-Record\-Type AVP on the ACR message labels the type  of the accounting request. The following types are used by Rf billing. 1.   For session\-based charging, the types Start (session begins), Interim (session is modified) and Stop (session ends) are used. 2.   For event\-based charging, the type Event is used when a chargeable event occurs outside the scope of a session.  Each row of this table is identified by a value of csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and  csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:   :py:class:`Csbrfbillrealmstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable>`
    
    .. attribute:: csbsipmthdcurrentstatstable
    
    	This table reports count of SIP request and various SIP responses  for each SIP method on a SIP adjacency in a given interval. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. To understand the meaning of  interval please refer <Periodic Statistics> section in  description of ciscoSbcStatsMIB.   This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:   :py:class:`Csbsipmthdcurrentstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable>`
    
    .. attribute:: csbsipmthdhistorystatstable
    
    	This table provide historical count of SIP request and various SIP responses for each SIP method on a SIP adjacency in various interval length defined by the csbSIPMthdHistoryStatsInterval object. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. The possible values of interval will be previous 5 minutes, previous 15 minutes, previous 1 hour and previous day. To understand the meaning of interval please refer <Periodic Statistics> description of ciscoSbcStatsMIB. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and  csbSIPMthdHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:   :py:class:`Csbsipmthdhistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable>`
    
    .. attribute:: csbsipmthdrccurrentstatstable
    
    	This table reports SIP method request and response code statistics for each method and response code combination on given SIP adjacency in a given interval. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows  for response codes which have not been received or sent
    	**type**\:   :py:class:`Csbsipmthdrccurrentstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable>`
    
    .. attribute:: csbsipmthdrchistorystatstable
    
    	This table reports historical data for SIP method request and response code statistics for each method and response code  combination in a given past interval. The possible values of  interval will be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous day. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows for response codes which have not been received or sent
    	**type**\:   :py:class:`Csbsipmthdrchistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable>`
    
    

    """

    _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
    _revision = '2010-09-15'

    def __init__(self):
        super(CiscoSessBorderCtrlrStatsMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
        self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

        self.csbradiusstatstable = CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable()
        self.csbradiusstatstable.parent = self
        self._children_name_map["csbradiusstatstable"] = "csbRadiusStatsTable"
        self._children_yang_names.add("csbRadiusStatsTable")

        self.csbrfbillrealmstatstable = CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable()
        self.csbrfbillrealmstatstable.parent = self
        self._children_name_map["csbrfbillrealmstatstable"] = "csbRfBillRealmStatsTable"
        self._children_yang_names.add("csbRfBillRealmStatsTable")

        self.csbsipmthdcurrentstatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable()
        self.csbsipmthdcurrentstatstable.parent = self
        self._children_name_map["csbsipmthdcurrentstatstable"] = "csbSIPMthdCurrentStatsTable"
        self._children_yang_names.add("csbSIPMthdCurrentStatsTable")

        self.csbsipmthdhistorystatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable()
        self.csbsipmthdhistorystatstable.parent = self
        self._children_name_map["csbsipmthdhistorystatstable"] = "csbSIPMthdHistoryStatsTable"
        self._children_yang_names.add("csbSIPMthdHistoryStatsTable")

        self.csbsipmthdrccurrentstatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable()
        self.csbsipmthdrccurrentstatstable.parent = self
        self._children_name_map["csbsipmthdrccurrentstatstable"] = "csbSIPMthdRCCurrentStatsTable"
        self._children_yang_names.add("csbSIPMthdRCCurrentStatsTable")

        self.csbsipmthdrchistorystatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable()
        self.csbsipmthdrchistorystatstable.parent = self
        self._children_name_map["csbsipmthdrchistorystatstable"] = "csbSIPMthdRCHistoryStatsTable"
        self._children_yang_names.add("csbSIPMthdRCHistoryStatsTable")


    class Csbradiusstatstable(Entity):
        """
        This table has the reporting statistics of various RADIUS
        messages for RADIUS servers with which the client (SBC) shares a
        secret. Each entry in this table is identified by a 
        value of csbRadiusStatsEntIndex. The other indices of this table
        are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbradiusstatsentry
        
        	A conceptual row in the csbRadiusStatsTable. There is an entry in this table for each RADIUS server, as identified by a  value of csbRadiusStatsEntIndex. The other indices of this  table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbradiusstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable, self).__init__()

            self.yang_name = "csbRadiusStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbradiusstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable, self).__setattr__(name, value)


        class Csbradiusstatsentry(Entity):
            """
            A conceptual row in the csbRadiusStatsTable. There is an
            entry in this table for each RADIUS server, as identified by a 
            value of csbRadiusStatsEntIndex. The other indices of this 
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbradiusstatsentindex  <key>
            
            	This object indicates the index of the RADIUS client entity that this server is configured on. This index is assigned  arbitrarily by the engine and is not saved over reboots
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbradiusstatsacsaccpts
            
            	This object indicates the number of RADIUS Access\-Accept packets (valid or invalid) received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacschalls
            
            	This object indicates the number of RADIUS Access\-Challenge packets (valid or invalid) received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacsrejects
            
            	This object indicates the number of RADIUS Access\-Reject packets (valid or invalid) received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacsreqs
            
            	This object indicates the number of RADIUS Access\-Request packets sent to this server.  This does not include retransmissions
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacsrtrns
            
            	This object indicates the number of RADIUS Access\-Request packets retransmitted to this RADIUS server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactreqs
            
            	This object indicates the number of RADIUS Accounting\-Request packets sent to this server. This does not include retransmissions
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactretrans
            
            	This object indicates the number of RADIUS Accounting\-Request packets retransmitted to this RADIUS server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactrsps
            
            	This object indicates the number of RADIUS Accounting\-Response packets (valid or invalid) received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsbadauths
            
            	This object indicates the number of RADIUS response packets containing invalid authenticators or Signature attributes received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsclientname
            
            	This object indicates the client name of the RADIUS client to which that these statistics apply
            	**type**\:  str
            
            .. attribute:: csbradiusstatsclienttype
            
            	This object indicates the type(authentication or accounting) of the RADIUS clients configured on SBC
            	**type**\:   :py:class:`Ciscosbcradiusclienttype <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.Ciscosbcradiusclienttype>`
            
            .. attribute:: csbradiusstatsdropped
            
            	This object indicates the number of RADIUS packets which were received from this server and dropped for some other reason
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsmalformedrsps
            
            	This object indicates the number of malformed RADIUS response packets received from this server.  Malformed packets include packets with an invalid length. Bad authenticators, Signature attributes and unknown types are not included as malformed access responses
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatspending
            
            	This object indicates the number of RADIUS request packets destined for this server that have not yet timed out or received a response. This variable is incremented when a request is sent and decremented on receipt of the response or on a timeout or retransmission
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatssrvrname
            
            	This object indicates the server name of the RADIUS server to which that these statistics apply
            	**type**\:  str
            
            .. attribute:: csbradiusstatstimeouts
            
            	This object indicates the number of RADIUS request timeouts to this server.  After a timeout the client may retry to a different server or give up. A retry to a different server is counted as a request as well as a timeout
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsunknowntype
            
            	This object indicates the number of RADIUS packets of unknown type which were received from this server
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry, self).__init__()

                self.yang_name = "csbRadiusStatsEntry"
                self.yang_parent_name = "csbRadiusStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbradiusstatsentindex = YLeaf(YType.uint32, "csbRadiusStatsEntIndex")

                self.csbradiusstatsacsaccpts = YLeaf(YType.uint64, "csbRadiusStatsAcsAccpts")

                self.csbradiusstatsacschalls = YLeaf(YType.uint64, "csbRadiusStatsAcsChalls")

                self.csbradiusstatsacsrejects = YLeaf(YType.uint64, "csbRadiusStatsAcsRejects")

                self.csbradiusstatsacsreqs = YLeaf(YType.uint64, "csbRadiusStatsAcsReqs")

                self.csbradiusstatsacsrtrns = YLeaf(YType.uint64, "csbRadiusStatsAcsRtrns")

                self.csbradiusstatsactreqs = YLeaf(YType.uint64, "csbRadiusStatsActReqs")

                self.csbradiusstatsactretrans = YLeaf(YType.uint64, "csbRadiusStatsActRetrans")

                self.csbradiusstatsactrsps = YLeaf(YType.uint64, "csbRadiusStatsActRsps")

                self.csbradiusstatsbadauths = YLeaf(YType.uint64, "csbRadiusStatsBadAuths")

                self.csbradiusstatsclientname = YLeaf(YType.str, "csbRadiusStatsClientName")

                self.csbradiusstatsclienttype = YLeaf(YType.enumeration, "csbRadiusStatsClientType")

                self.csbradiusstatsdropped = YLeaf(YType.uint64, "csbRadiusStatsDropped")

                self.csbradiusstatsmalformedrsps = YLeaf(YType.uint64, "csbRadiusStatsMalformedRsps")

                self.csbradiusstatspending = YLeaf(YType.uint32, "csbRadiusStatsPending")

                self.csbradiusstatssrvrname = YLeaf(YType.str, "csbRadiusStatsSrvrName")

                self.csbradiusstatstimeouts = YLeaf(YType.uint64, "csbRadiusStatsTimeouts")

                self.csbradiusstatsunknowntype = YLeaf(YType.uint64, "csbRadiusStatsUnknownType")

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
                                "csbradiusstatsentindex",
                                "csbradiusstatsacsaccpts",
                                "csbradiusstatsacschalls",
                                "csbradiusstatsacsrejects",
                                "csbradiusstatsacsreqs",
                                "csbradiusstatsacsrtrns",
                                "csbradiusstatsactreqs",
                                "csbradiusstatsactretrans",
                                "csbradiusstatsactrsps",
                                "csbradiusstatsbadauths",
                                "csbradiusstatsclientname",
                                "csbradiusstatsclienttype",
                                "csbradiusstatsdropped",
                                "csbradiusstatsmalformedrsps",
                                "csbradiusstatspending",
                                "csbradiusstatssrvrname",
                                "csbradiusstatstimeouts",
                                "csbradiusstatsunknowntype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbradiusstatsentindex.is_set or
                    self.csbradiusstatsacsaccpts.is_set or
                    self.csbradiusstatsacschalls.is_set or
                    self.csbradiusstatsacsrejects.is_set or
                    self.csbradiusstatsacsreqs.is_set or
                    self.csbradiusstatsacsrtrns.is_set or
                    self.csbradiusstatsactreqs.is_set or
                    self.csbradiusstatsactretrans.is_set or
                    self.csbradiusstatsactrsps.is_set or
                    self.csbradiusstatsbadauths.is_set or
                    self.csbradiusstatsclientname.is_set or
                    self.csbradiusstatsclienttype.is_set or
                    self.csbradiusstatsdropped.is_set or
                    self.csbradiusstatsmalformedrsps.is_set or
                    self.csbradiusstatspending.is_set or
                    self.csbradiusstatssrvrname.is_set or
                    self.csbradiusstatstimeouts.is_set or
                    self.csbradiusstatsunknowntype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbradiusstatsentindex.yfilter != YFilter.not_set or
                    self.csbradiusstatsacsaccpts.yfilter != YFilter.not_set or
                    self.csbradiusstatsacschalls.yfilter != YFilter.not_set or
                    self.csbradiusstatsacsrejects.yfilter != YFilter.not_set or
                    self.csbradiusstatsacsreqs.yfilter != YFilter.not_set or
                    self.csbradiusstatsacsrtrns.yfilter != YFilter.not_set or
                    self.csbradiusstatsactreqs.yfilter != YFilter.not_set or
                    self.csbradiusstatsactretrans.yfilter != YFilter.not_set or
                    self.csbradiusstatsactrsps.yfilter != YFilter.not_set or
                    self.csbradiusstatsbadauths.yfilter != YFilter.not_set or
                    self.csbradiusstatsclientname.yfilter != YFilter.not_set or
                    self.csbradiusstatsclienttype.yfilter != YFilter.not_set or
                    self.csbradiusstatsdropped.yfilter != YFilter.not_set or
                    self.csbradiusstatsmalformedrsps.yfilter != YFilter.not_set or
                    self.csbradiusstatspending.yfilter != YFilter.not_set or
                    self.csbradiusstatssrvrname.yfilter != YFilter.not_set or
                    self.csbradiusstatstimeouts.yfilter != YFilter.not_set or
                    self.csbradiusstatsunknowntype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbRadiusStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbRadiusStatsEntIndex='" + self.csbradiusstatsentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbRadiusStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbradiusstatsentindex.is_set or self.csbradiusstatsentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsentindex.get_name_leafdata())
                if (self.csbradiusstatsacsaccpts.is_set or self.csbradiusstatsacsaccpts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsacsaccpts.get_name_leafdata())
                if (self.csbradiusstatsacschalls.is_set or self.csbradiusstatsacschalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsacschalls.get_name_leafdata())
                if (self.csbradiusstatsacsrejects.is_set or self.csbradiusstatsacsrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsacsrejects.get_name_leafdata())
                if (self.csbradiusstatsacsreqs.is_set or self.csbradiusstatsacsreqs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsacsreqs.get_name_leafdata())
                if (self.csbradiusstatsacsrtrns.is_set or self.csbradiusstatsacsrtrns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsacsrtrns.get_name_leafdata())
                if (self.csbradiusstatsactreqs.is_set or self.csbradiusstatsactreqs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsactreqs.get_name_leafdata())
                if (self.csbradiusstatsactretrans.is_set or self.csbradiusstatsactretrans.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsactretrans.get_name_leafdata())
                if (self.csbradiusstatsactrsps.is_set or self.csbradiusstatsactrsps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsactrsps.get_name_leafdata())
                if (self.csbradiusstatsbadauths.is_set or self.csbradiusstatsbadauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsbadauths.get_name_leafdata())
                if (self.csbradiusstatsclientname.is_set or self.csbradiusstatsclientname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsclientname.get_name_leafdata())
                if (self.csbradiusstatsclienttype.is_set or self.csbradiusstatsclienttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsclienttype.get_name_leafdata())
                if (self.csbradiusstatsdropped.is_set or self.csbradiusstatsdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsdropped.get_name_leafdata())
                if (self.csbradiusstatsmalformedrsps.is_set or self.csbradiusstatsmalformedrsps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsmalformedrsps.get_name_leafdata())
                if (self.csbradiusstatspending.is_set or self.csbradiusstatspending.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatspending.get_name_leafdata())
                if (self.csbradiusstatssrvrname.is_set or self.csbradiusstatssrvrname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatssrvrname.get_name_leafdata())
                if (self.csbradiusstatstimeouts.is_set or self.csbradiusstatstimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatstimeouts.get_name_leafdata())
                if (self.csbradiusstatsunknowntype.is_set or self.csbradiusstatsunknowntype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbradiusstatsunknowntype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbRadiusStatsEntIndex" or name == "csbRadiusStatsAcsAccpts" or name == "csbRadiusStatsAcsChalls" or name == "csbRadiusStatsAcsRejects" or name == "csbRadiusStatsAcsReqs" or name == "csbRadiusStatsAcsRtrns" or name == "csbRadiusStatsActReqs" or name == "csbRadiusStatsActRetrans" or name == "csbRadiusStatsActRsps" or name == "csbRadiusStatsBadAuths" or name == "csbRadiusStatsClientName" or name == "csbRadiusStatsClientType" or name == "csbRadiusStatsDropped" or name == "csbRadiusStatsMalformedRsps" or name == "csbRadiusStatsPending" or name == "csbRadiusStatsSrvrName" or name == "csbRadiusStatsTimeouts" or name == "csbRadiusStatsUnknownType"):
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
                if(value_path == "csbRadiusStatsEntIndex"):
                    self.csbradiusstatsentindex = value
                    self.csbradiusstatsentindex.value_namespace = name_space
                    self.csbradiusstatsentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsAcsAccpts"):
                    self.csbradiusstatsacsaccpts = value
                    self.csbradiusstatsacsaccpts.value_namespace = name_space
                    self.csbradiusstatsacsaccpts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsAcsChalls"):
                    self.csbradiusstatsacschalls = value
                    self.csbradiusstatsacschalls.value_namespace = name_space
                    self.csbradiusstatsacschalls.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsAcsRejects"):
                    self.csbradiusstatsacsrejects = value
                    self.csbradiusstatsacsrejects.value_namespace = name_space
                    self.csbradiusstatsacsrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsAcsReqs"):
                    self.csbradiusstatsacsreqs = value
                    self.csbradiusstatsacsreqs.value_namespace = name_space
                    self.csbradiusstatsacsreqs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsAcsRtrns"):
                    self.csbradiusstatsacsrtrns = value
                    self.csbradiusstatsacsrtrns.value_namespace = name_space
                    self.csbradiusstatsacsrtrns.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsActReqs"):
                    self.csbradiusstatsactreqs = value
                    self.csbradiusstatsactreqs.value_namespace = name_space
                    self.csbradiusstatsactreqs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsActRetrans"):
                    self.csbradiusstatsactretrans = value
                    self.csbradiusstatsactretrans.value_namespace = name_space
                    self.csbradiusstatsactretrans.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsActRsps"):
                    self.csbradiusstatsactrsps = value
                    self.csbradiusstatsactrsps.value_namespace = name_space
                    self.csbradiusstatsactrsps.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsBadAuths"):
                    self.csbradiusstatsbadauths = value
                    self.csbradiusstatsbadauths.value_namespace = name_space
                    self.csbradiusstatsbadauths.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsClientName"):
                    self.csbradiusstatsclientname = value
                    self.csbradiusstatsclientname.value_namespace = name_space
                    self.csbradiusstatsclientname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsClientType"):
                    self.csbradiusstatsclienttype = value
                    self.csbradiusstatsclienttype.value_namespace = name_space
                    self.csbradiusstatsclienttype.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsDropped"):
                    self.csbradiusstatsdropped = value
                    self.csbradiusstatsdropped.value_namespace = name_space
                    self.csbradiusstatsdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsMalformedRsps"):
                    self.csbradiusstatsmalformedrsps = value
                    self.csbradiusstatsmalformedrsps.value_namespace = name_space
                    self.csbradiusstatsmalformedrsps.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsPending"):
                    self.csbradiusstatspending = value
                    self.csbradiusstatspending.value_namespace = name_space
                    self.csbradiusstatspending.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsSrvrName"):
                    self.csbradiusstatssrvrname = value
                    self.csbradiusstatssrvrname.value_namespace = name_space
                    self.csbradiusstatssrvrname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsTimeouts"):
                    self.csbradiusstatstimeouts = value
                    self.csbradiusstatstimeouts.value_namespace = name_space
                    self.csbradiusstatstimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRadiusStatsUnknownType"):
                    self.csbradiusstatsunknowntype = value
                    self.csbradiusstatsunknowntype.value_namespace = name_space
                    self.csbradiusstatsunknowntype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbradiusstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbradiusstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbRadiusStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbRadiusStatsEntry"):
                for c in self.csbradiusstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbradiusstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbRadiusStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbrfbillrealmstatstable(Entity):
        """
        This table describes the Rf billing statistics information
        which monitors the messages sent per\-realm by Rf billing 
        manager(SBC). SBC sends Rf billing data using Diameter as a
        transport protocol. Rf billing uses only ACR and ACA Diameter
        messages for the transport of billing data. The
        Accounting\-Record\-Type AVP on the ACR message labels the type 
        of the accounting request. The following types are used by Rf
        billing.
        1.   For session\-based charging, the types Start (session
        begins), Interim (session is modified) and Stop (session ends)
        are used.
        2.   For event\-based charging, the type Event is used when a
        chargeable event occurs outside the scope of a session.
        
        Each row of this table is identified by a value of
        csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName.
        The other indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and 
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        .. attribute:: csbrfbillrealmstatsentry
        
        	A conceptual row in the csbRfBillRealmStatsTable. There is an entry in this table for each realm, as identified by a  value of csbRfBillRealmStatsIndex and  csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbrfbillrealmstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable, self).__init__()

            self.yang_name = "csbRfBillRealmStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbrfbillrealmstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable, self).__setattr__(name, value)


        class Csbrfbillrealmstatsentry(Entity):
            """
            A conceptual row in the csbRfBillRealmStatsTable. There
            is an entry in this table for each realm, as identified by a 
            value of csbRfBillRealmStatsIndex and 
            csbRfBillRealmStatsRealmName. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbrfbillrealmstatsindex  <key>
            
            	This object indicates the billing method instance index. The range of valid values for this field is 0 \- 31
            	**type**\:  int
            
            	**range:** 0..31
            
            .. attribute:: csbrfbillrealmstatsrealmname  <key>
            
            	This object indicates the realm for which these statistics are collected. The length of this object is zero when value is not assigned to it
            	**type**\:  str
            
            .. attribute:: csbrfbillrealmstatsfaileventacrs
            
            	This object indicates the total number of failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailinterimacrs
            
            	This object indicates the total number of failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailstartacrs
            
            	This object indicates the total number of failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailstopacrs
            
            	This object indicates the total number of failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssucceventacrs
            
            	This object indicates the total number of successful Event ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccinterimacrs
            
            	This object indicates the total number of successful Interim ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccstartacrs
            
            	This object indicates the total number of successful Start ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccstopacrs
            
            	This object indicates the total number of successful Stop ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotaleventacrs
            
            	This object indicates the combined sum of successful and failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotalinterimacrs
            
            	This object indicates the combined sum of successful and failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotalstartacrs
            
            	This object indicates the combined sum of successful and failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotalstopacrs
            
            	This object indicates the combined sum of successful and failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry, self).__init__()

                self.yang_name = "csbRfBillRealmStatsEntry"
                self.yang_parent_name = "csbRfBillRealmStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbrfbillrealmstatsindex = YLeaf(YType.uint32, "csbRfBillRealmStatsIndex")

                self.csbrfbillrealmstatsrealmname = YLeaf(YType.str, "csbRfBillRealmStatsRealmName")

                self.csbrfbillrealmstatsfaileventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailEventAcrs")

                self.csbrfbillrealmstatsfailinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailInterimAcrs")

                self.csbrfbillrealmstatsfailstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailStartAcrs")

                self.csbrfbillrealmstatsfailstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailStopAcrs")

                self.csbrfbillrealmstatssucceventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccEventAcrs")

                self.csbrfbillrealmstatssuccinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccInterimAcrs")

                self.csbrfbillrealmstatssuccstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccStartAcrs")

                self.csbrfbillrealmstatssuccstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccStopAcrs")

                self.csbrfbillrealmstatstotaleventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalEventAcrs")

                self.csbrfbillrealmstatstotalinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalInterimAcrs")

                self.csbrfbillrealmstatstotalstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalStartAcrs")

                self.csbrfbillrealmstatstotalstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalStopAcrs")

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
                                "csbrfbillrealmstatsindex",
                                "csbrfbillrealmstatsrealmname",
                                "csbrfbillrealmstatsfaileventacrs",
                                "csbrfbillrealmstatsfailinterimacrs",
                                "csbrfbillrealmstatsfailstartacrs",
                                "csbrfbillrealmstatsfailstopacrs",
                                "csbrfbillrealmstatssucceventacrs",
                                "csbrfbillrealmstatssuccinterimacrs",
                                "csbrfbillrealmstatssuccstartacrs",
                                "csbrfbillrealmstatssuccstopacrs",
                                "csbrfbillrealmstatstotaleventacrs",
                                "csbrfbillrealmstatstotalinterimacrs",
                                "csbrfbillrealmstatstotalstartacrs",
                                "csbrfbillrealmstatstotalstopacrs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbrfbillrealmstatsindex.is_set or
                    self.csbrfbillrealmstatsrealmname.is_set or
                    self.csbrfbillrealmstatsfaileventacrs.is_set or
                    self.csbrfbillrealmstatsfailinterimacrs.is_set or
                    self.csbrfbillrealmstatsfailstartacrs.is_set or
                    self.csbrfbillrealmstatsfailstopacrs.is_set or
                    self.csbrfbillrealmstatssucceventacrs.is_set or
                    self.csbrfbillrealmstatssuccinterimacrs.is_set or
                    self.csbrfbillrealmstatssuccstartacrs.is_set or
                    self.csbrfbillrealmstatssuccstopacrs.is_set or
                    self.csbrfbillrealmstatstotaleventacrs.is_set or
                    self.csbrfbillrealmstatstotalinterimacrs.is_set or
                    self.csbrfbillrealmstatstotalstartacrs.is_set or
                    self.csbrfbillrealmstatstotalstopacrs.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsindex.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsrealmname.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsfaileventacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsfailinterimacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsfailstartacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatsfailstopacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatssucceventacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatssuccinterimacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatssuccstartacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatssuccstopacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatstotaleventacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatstotalinterimacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatstotalstartacrs.yfilter != YFilter.not_set or
                    self.csbrfbillrealmstatstotalstopacrs.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbRfBillRealmStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbRfBillRealmStatsIndex='" + self.csbrfbillrealmstatsindex.get() + "']" + "[csbRfBillRealmStatsRealmName='" + self.csbrfbillrealmstatsrealmname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbRfBillRealmStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbrfbillrealmstatsindex.is_set or self.csbrfbillrealmstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsindex.get_name_leafdata())
                if (self.csbrfbillrealmstatsrealmname.is_set or self.csbrfbillrealmstatsrealmname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsrealmname.get_name_leafdata())
                if (self.csbrfbillrealmstatsfaileventacrs.is_set or self.csbrfbillrealmstatsfaileventacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsfaileventacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatsfailinterimacrs.is_set or self.csbrfbillrealmstatsfailinterimacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsfailinterimacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatsfailstartacrs.is_set or self.csbrfbillrealmstatsfailstartacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsfailstartacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatsfailstopacrs.is_set or self.csbrfbillrealmstatsfailstopacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatsfailstopacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatssucceventacrs.is_set or self.csbrfbillrealmstatssucceventacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatssucceventacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatssuccinterimacrs.is_set or self.csbrfbillrealmstatssuccinterimacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatssuccinterimacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatssuccstartacrs.is_set or self.csbrfbillrealmstatssuccstartacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatssuccstartacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatssuccstopacrs.is_set or self.csbrfbillrealmstatssuccstopacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatssuccstopacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatstotaleventacrs.is_set or self.csbrfbillrealmstatstotaleventacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatstotaleventacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatstotalinterimacrs.is_set or self.csbrfbillrealmstatstotalinterimacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatstotalinterimacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatstotalstartacrs.is_set or self.csbrfbillrealmstatstotalstartacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatstotalstartacrs.get_name_leafdata())
                if (self.csbrfbillrealmstatstotalstopacrs.is_set or self.csbrfbillrealmstatstotalstopacrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbrfbillrealmstatstotalstopacrs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbRfBillRealmStatsIndex" or name == "csbRfBillRealmStatsRealmName" or name == "csbRfBillRealmStatsFailEventAcrs" or name == "csbRfBillRealmStatsFailInterimAcrs" or name == "csbRfBillRealmStatsFailStartAcrs" or name == "csbRfBillRealmStatsFailStopAcrs" or name == "csbRfBillRealmStatsSuccEventAcrs" or name == "csbRfBillRealmStatsSuccInterimAcrs" or name == "csbRfBillRealmStatsSuccStartAcrs" or name == "csbRfBillRealmStatsSuccStopAcrs" or name == "csbRfBillRealmStatsTotalEventAcrs" or name == "csbRfBillRealmStatsTotalInterimAcrs" or name == "csbRfBillRealmStatsTotalStartAcrs" or name == "csbRfBillRealmStatsTotalStopAcrs"):
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
                if(value_path == "csbRfBillRealmStatsIndex"):
                    self.csbrfbillrealmstatsindex = value
                    self.csbrfbillrealmstatsindex.value_namespace = name_space
                    self.csbrfbillrealmstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsRealmName"):
                    self.csbrfbillrealmstatsrealmname = value
                    self.csbrfbillrealmstatsrealmname.value_namespace = name_space
                    self.csbrfbillrealmstatsrealmname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsFailEventAcrs"):
                    self.csbrfbillrealmstatsfaileventacrs = value
                    self.csbrfbillrealmstatsfaileventacrs.value_namespace = name_space
                    self.csbrfbillrealmstatsfaileventacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsFailInterimAcrs"):
                    self.csbrfbillrealmstatsfailinterimacrs = value
                    self.csbrfbillrealmstatsfailinterimacrs.value_namespace = name_space
                    self.csbrfbillrealmstatsfailinterimacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsFailStartAcrs"):
                    self.csbrfbillrealmstatsfailstartacrs = value
                    self.csbrfbillrealmstatsfailstartacrs.value_namespace = name_space
                    self.csbrfbillrealmstatsfailstartacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsFailStopAcrs"):
                    self.csbrfbillrealmstatsfailstopacrs = value
                    self.csbrfbillrealmstatsfailstopacrs.value_namespace = name_space
                    self.csbrfbillrealmstatsfailstopacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsSuccEventAcrs"):
                    self.csbrfbillrealmstatssucceventacrs = value
                    self.csbrfbillrealmstatssucceventacrs.value_namespace = name_space
                    self.csbrfbillrealmstatssucceventacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsSuccInterimAcrs"):
                    self.csbrfbillrealmstatssuccinterimacrs = value
                    self.csbrfbillrealmstatssuccinterimacrs.value_namespace = name_space
                    self.csbrfbillrealmstatssuccinterimacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsSuccStartAcrs"):
                    self.csbrfbillrealmstatssuccstartacrs = value
                    self.csbrfbillrealmstatssuccstartacrs.value_namespace = name_space
                    self.csbrfbillrealmstatssuccstartacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsSuccStopAcrs"):
                    self.csbrfbillrealmstatssuccstopacrs = value
                    self.csbrfbillrealmstatssuccstopacrs.value_namespace = name_space
                    self.csbrfbillrealmstatssuccstopacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsTotalEventAcrs"):
                    self.csbrfbillrealmstatstotaleventacrs = value
                    self.csbrfbillrealmstatstotaleventacrs.value_namespace = name_space
                    self.csbrfbillrealmstatstotaleventacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsTotalInterimAcrs"):
                    self.csbrfbillrealmstatstotalinterimacrs = value
                    self.csbrfbillrealmstatstotalinterimacrs.value_namespace = name_space
                    self.csbrfbillrealmstatstotalinterimacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsTotalStartAcrs"):
                    self.csbrfbillrealmstatstotalstartacrs = value
                    self.csbrfbillrealmstatstotalstartacrs.value_namespace = name_space
                    self.csbrfbillrealmstatstotalstartacrs.value_namespace_prefix = name_space_prefix
                if(value_path == "csbRfBillRealmStatsTotalStopAcrs"):
                    self.csbrfbillrealmstatstotalstopacrs = value
                    self.csbrfbillrealmstatstotalstopacrs.value_namespace = name_space
                    self.csbrfbillrealmstatstotalstopacrs.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbrfbillrealmstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbrfbillrealmstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbRfBillRealmStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbRfBillRealmStatsEntry"):
                for c in self.csbrfbillrealmstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbrfbillrealmstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbRfBillRealmStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbsipmthdcurrentstatstable(Entity):
        """
        This table reports count of SIP request and various SIP
        responses  for each SIP method on a SIP adjacency in a given
        interval. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. To understand the meaning of 
        interval please refer <Periodic Statistics> section in 
        description of ciscoSbcStatsMIB.  
        This table is indexed on csbSIPMthdCurrentStatsAdjName,
        csbSIPMthdCurrentStatsMethod and 
        csbSIPMthdCurrentStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdcurrentstatsentry
        
        	A conceptual row in the csbSIPMthdCurrentStatsTable. Each row describes a SIP method and various responses count for this method on a given SIP adjacency and given interval. This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbsipmthdcurrentstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable, self).__init__()

            self.yang_name = "csbSIPMthdCurrentStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbsipmthdcurrentstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable, self).__setattr__(name, value)


        class Csbsipmthdcurrentstatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdCurrentStatsTable. Each row
            describes a SIP method and various responses count for this
            method on a given SIP adjacency and given interval. This table
            is indexed on csbSIPMthdCurrentStatsAdjName,
            csbSIPMthdCurrentStatsMethod and 
            csbSIPMthdCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdcurrentstatsadjname  <key>
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\:  str
            
            .. attribute:: csbsipmthdcurrentstatsmethod  <key>
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\:   :py:class:`Ciscosbcsipmethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.Ciscosbcsipmethod>`
            
            .. attribute:: csbsipmthdcurrentstatsinterval  <key>
            
            	This object indicates the interval for which the periodic statistics information is to be displayed. The interval values can be 5 minutes, 15 minutes, 1 hour , 1 Day. This  object acts as an index for the table
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
            .. attribute:: csbsipmthdcurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\:  str
            
            .. attribute:: csbsipmthdcurrentstatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdcurrentstatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry, self).__init__()

                self.yang_name = "csbSIPMthdCurrentStatsEntry"
                self.yang_parent_name = "csbSIPMthdCurrentStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdcurrentstatsadjname = YLeaf(YType.str, "csbSIPMthdCurrentStatsAdjName")

                self.csbsipmthdcurrentstatsmethod = YLeaf(YType.enumeration, "csbSIPMthdCurrentStatsMethod")

                self.csbsipmthdcurrentstatsinterval = YLeaf(YType.enumeration, "csbSIPMthdCurrentStatsInterval")

                self.csbsipmthdcurrentstatsmethodname = YLeaf(YType.str, "csbSIPMthdCurrentStatsMethodName")

                self.csbsipmthdcurrentstatsreqin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsReqIn")

                self.csbsipmthdcurrentstatsreqout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsReqOut")

                self.csbsipmthdcurrentstatsresp1xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp1xxIn")

                self.csbsipmthdcurrentstatsresp1xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp1xxOut")

                self.csbsipmthdcurrentstatsresp2xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp2xxIn")

                self.csbsipmthdcurrentstatsresp2xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp2xxOut")

                self.csbsipmthdcurrentstatsresp3xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp3xxIn")

                self.csbsipmthdcurrentstatsresp3xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp3xxOut")

                self.csbsipmthdcurrentstatsresp4xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp4xxIn")

                self.csbsipmthdcurrentstatsresp4xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp4xxOut")

                self.csbsipmthdcurrentstatsresp5xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp5xxIn")

                self.csbsipmthdcurrentstatsresp5xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp5xxOut")

                self.csbsipmthdcurrentstatsresp6xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp6xxIn")

                self.csbsipmthdcurrentstatsresp6xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp6xxOut")

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
                                "csbsipmthdcurrentstatsadjname",
                                "csbsipmthdcurrentstatsmethod",
                                "csbsipmthdcurrentstatsinterval",
                                "csbsipmthdcurrentstatsmethodname",
                                "csbsipmthdcurrentstatsreqin",
                                "csbsipmthdcurrentstatsreqout",
                                "csbsipmthdcurrentstatsresp1xxin",
                                "csbsipmthdcurrentstatsresp1xxout",
                                "csbsipmthdcurrentstatsresp2xxin",
                                "csbsipmthdcurrentstatsresp2xxout",
                                "csbsipmthdcurrentstatsresp3xxin",
                                "csbsipmthdcurrentstatsresp3xxout",
                                "csbsipmthdcurrentstatsresp4xxin",
                                "csbsipmthdcurrentstatsresp4xxout",
                                "csbsipmthdcurrentstatsresp5xxin",
                                "csbsipmthdcurrentstatsresp5xxout",
                                "csbsipmthdcurrentstatsresp6xxin",
                                "csbsipmthdcurrentstatsresp6xxout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbsipmthdcurrentstatsadjname.is_set or
                    self.csbsipmthdcurrentstatsmethod.is_set or
                    self.csbsipmthdcurrentstatsinterval.is_set or
                    self.csbsipmthdcurrentstatsmethodname.is_set or
                    self.csbsipmthdcurrentstatsreqin.is_set or
                    self.csbsipmthdcurrentstatsreqout.is_set or
                    self.csbsipmthdcurrentstatsresp1xxin.is_set or
                    self.csbsipmthdcurrentstatsresp1xxout.is_set or
                    self.csbsipmthdcurrentstatsresp2xxin.is_set or
                    self.csbsipmthdcurrentstatsresp2xxout.is_set or
                    self.csbsipmthdcurrentstatsresp3xxin.is_set or
                    self.csbsipmthdcurrentstatsresp3xxout.is_set or
                    self.csbsipmthdcurrentstatsresp4xxin.is_set or
                    self.csbsipmthdcurrentstatsresp4xxout.is_set or
                    self.csbsipmthdcurrentstatsresp5xxin.is_set or
                    self.csbsipmthdcurrentstatsresp5xxout.is_set or
                    self.csbsipmthdcurrentstatsresp6xxin.is_set or
                    self.csbsipmthdcurrentstatsresp6xxout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsadjname.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsmethod.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsinterval.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsmethodname.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsreqin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsreqout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp1xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp1xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp2xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp2xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp3xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp3xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp4xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp4xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp5xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp5xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp6xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdcurrentstatsresp6xxout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbSIPMthdCurrentStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdCurrentStatsAdjName='" + self.csbsipmthdcurrentstatsadjname.get() + "']" + "[csbSIPMthdCurrentStatsMethod='" + self.csbsipmthdcurrentstatsmethod.get() + "']" + "[csbSIPMthdCurrentStatsInterval='" + self.csbsipmthdcurrentstatsinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdCurrentStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsadjname.is_set or self.csbsipmthdcurrentstatsadjname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsadjname.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsmethod.is_set or self.csbsipmthdcurrentstatsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsmethod.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsinterval.is_set or self.csbsipmthdcurrentstatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsinterval.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsmethodname.is_set or self.csbsipmthdcurrentstatsmethodname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsmethodname.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsreqin.is_set or self.csbsipmthdcurrentstatsreqin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsreqin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsreqout.is_set or self.csbsipmthdcurrentstatsreqout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsreqout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp1xxin.is_set or self.csbsipmthdcurrentstatsresp1xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp1xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp1xxout.is_set or self.csbsipmthdcurrentstatsresp1xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp1xxout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp2xxin.is_set or self.csbsipmthdcurrentstatsresp2xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp2xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp2xxout.is_set or self.csbsipmthdcurrentstatsresp2xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp2xxout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp3xxin.is_set or self.csbsipmthdcurrentstatsresp3xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp3xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp3xxout.is_set or self.csbsipmthdcurrentstatsresp3xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp3xxout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp4xxin.is_set or self.csbsipmthdcurrentstatsresp4xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp4xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp4xxout.is_set or self.csbsipmthdcurrentstatsresp4xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp4xxout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp5xxin.is_set or self.csbsipmthdcurrentstatsresp5xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp5xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp5xxout.is_set or self.csbsipmthdcurrentstatsresp5xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp5xxout.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp6xxin.is_set or self.csbsipmthdcurrentstatsresp6xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp6xxin.get_name_leafdata())
                if (self.csbsipmthdcurrentstatsresp6xxout.is_set or self.csbsipmthdcurrentstatsresp6xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdcurrentstatsresp6xxout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbSIPMthdCurrentStatsAdjName" or name == "csbSIPMthdCurrentStatsMethod" or name == "csbSIPMthdCurrentStatsInterval" or name == "csbSIPMthdCurrentStatsMethodName" or name == "csbSIPMthdCurrentStatsReqIn" or name == "csbSIPMthdCurrentStatsReqOut" or name == "csbSIPMthdCurrentStatsResp1xxIn" or name == "csbSIPMthdCurrentStatsResp1xxOut" or name == "csbSIPMthdCurrentStatsResp2xxIn" or name == "csbSIPMthdCurrentStatsResp2xxOut" or name == "csbSIPMthdCurrentStatsResp3xxIn" or name == "csbSIPMthdCurrentStatsResp3xxOut" or name == "csbSIPMthdCurrentStatsResp4xxIn" or name == "csbSIPMthdCurrentStatsResp4xxOut" or name == "csbSIPMthdCurrentStatsResp5xxIn" or name == "csbSIPMthdCurrentStatsResp5xxOut" or name == "csbSIPMthdCurrentStatsResp6xxIn" or name == "csbSIPMthdCurrentStatsResp6xxOut"):
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
                if(value_path == "csbSIPMthdCurrentStatsAdjName"):
                    self.csbsipmthdcurrentstatsadjname = value
                    self.csbsipmthdcurrentstatsadjname.value_namespace = name_space
                    self.csbsipmthdcurrentstatsadjname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsMethod"):
                    self.csbsipmthdcurrentstatsmethod = value
                    self.csbsipmthdcurrentstatsmethod.value_namespace = name_space
                    self.csbsipmthdcurrentstatsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsInterval"):
                    self.csbsipmthdcurrentstatsinterval = value
                    self.csbsipmthdcurrentstatsinterval.value_namespace = name_space
                    self.csbsipmthdcurrentstatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsMethodName"):
                    self.csbsipmthdcurrentstatsmethodname = value
                    self.csbsipmthdcurrentstatsmethodname.value_namespace = name_space
                    self.csbsipmthdcurrentstatsmethodname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsReqIn"):
                    self.csbsipmthdcurrentstatsreqin = value
                    self.csbsipmthdcurrentstatsreqin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsreqin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsReqOut"):
                    self.csbsipmthdcurrentstatsreqout = value
                    self.csbsipmthdcurrentstatsreqout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsreqout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp1xxIn"):
                    self.csbsipmthdcurrentstatsresp1xxin = value
                    self.csbsipmthdcurrentstatsresp1xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp1xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp1xxOut"):
                    self.csbsipmthdcurrentstatsresp1xxout = value
                    self.csbsipmthdcurrentstatsresp1xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp1xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp2xxIn"):
                    self.csbsipmthdcurrentstatsresp2xxin = value
                    self.csbsipmthdcurrentstatsresp2xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp2xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp2xxOut"):
                    self.csbsipmthdcurrentstatsresp2xxout = value
                    self.csbsipmthdcurrentstatsresp2xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp2xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp3xxIn"):
                    self.csbsipmthdcurrentstatsresp3xxin = value
                    self.csbsipmthdcurrentstatsresp3xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp3xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp3xxOut"):
                    self.csbsipmthdcurrentstatsresp3xxout = value
                    self.csbsipmthdcurrentstatsresp3xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp3xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp4xxIn"):
                    self.csbsipmthdcurrentstatsresp4xxin = value
                    self.csbsipmthdcurrentstatsresp4xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp4xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp4xxOut"):
                    self.csbsipmthdcurrentstatsresp4xxout = value
                    self.csbsipmthdcurrentstatsresp4xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp4xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp5xxIn"):
                    self.csbsipmthdcurrentstatsresp5xxin = value
                    self.csbsipmthdcurrentstatsresp5xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp5xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp5xxOut"):
                    self.csbsipmthdcurrentstatsresp5xxout = value
                    self.csbsipmthdcurrentstatsresp5xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp5xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp6xxIn"):
                    self.csbsipmthdcurrentstatsresp6xxin = value
                    self.csbsipmthdcurrentstatsresp6xxin.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp6xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdCurrentStatsResp6xxOut"):
                    self.csbsipmthdcurrentstatsresp6xxout = value
                    self.csbsipmthdcurrentstatsresp6xxout.value_namespace = name_space
                    self.csbsipmthdcurrentstatsresp6xxout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbsipmthdcurrentstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbsipmthdcurrentstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbSIPMthdCurrentStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbSIPMthdCurrentStatsEntry"):
                for c in self.csbsipmthdcurrentstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbsipmthdcurrentstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbSIPMthdCurrentStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbsipmthdhistorystatstable(Entity):
        """
        This table provide historical count of SIP request and various
        SIP responses for each SIP method on a SIP adjacency in various
        interval length defined by the csbSIPMthdHistoryStatsInterval
        object. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. The possible values of interval
        will be previous 5 minutes, previous 15 minutes, previous 1 hour
        and previous day. To understand the meaning of interval please
        refer <Periodic Statistics> description of ciscoSbcStatsMIB.
        This table is indexed on csbSIPMthdHistoryStatsAdjName,
        csbSIPMthdHistoryStatsMethod and 
        csbSIPMthdHistoryStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdhistorystatsentry
        
        	A conceptual row in the csbSIPMthdHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdCurrentStatsTable table and the data is  moved from that table to this one. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and csbSIPMthdHistoryStatsInterval. The other indices of this  table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbsipmthdhistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable, self).__init__()

            self.yang_name = "csbSIPMthdHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbsipmthdhistorystatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable, self).__setattr__(name, value)


        class Csbsipmthdhistorystatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdCurrentStatsTable table and the data is 
            moved from that table to this one.
            This table is indexed on csbSIPMthdHistoryStatsAdjName,
            csbSIPMthdHistoryStatsMethod and
            csbSIPMthdHistoryStatsInterval. The other indices of this 
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex
            defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdhistorystatsadjname  <key>
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\:  str
            
            .. attribute:: csbsipmthdhistorystatsmethod  <key>
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\:   :py:class:`Ciscosbcsipmethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.Ciscosbcsipmethod>`
            
            .. attribute:: csbsipmthdhistorystatsinterval  <key>
            
            	This object indicates the interval for which the historical statistics information is to be displayed. The interval values can be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous 1 Day. This object acts as an  index for the table
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
            .. attribute:: csbsipmthdhistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\:  str
            
            .. attribute:: csbsipmthdhistorystatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdhistorystatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdhistorystatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry, self).__init__()

                self.yang_name = "csbSIPMthdHistoryStatsEntry"
                self.yang_parent_name = "csbSIPMthdHistoryStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdhistorystatsadjname = YLeaf(YType.str, "csbSIPMthdHistoryStatsAdjName")

                self.csbsipmthdhistorystatsmethod = YLeaf(YType.enumeration, "csbSIPMthdHistoryStatsMethod")

                self.csbsipmthdhistorystatsinterval = YLeaf(YType.enumeration, "csbSIPMthdHistoryStatsInterval")

                self.csbsipmthdhistorystatsmethodname = YLeaf(YType.str, "csbSIPMthdHistoryStatsMethodName")

                self.csbsipmthdhistorystatsreqin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsReqIn")

                self.csbsipmthdhistorystatsreqout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsReqOut")

                self.csbsipmthdhistorystatsresp1xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp1xxIn")

                self.csbsipmthdhistorystatsresp1xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp1xxOut")

                self.csbsipmthdhistorystatsresp2xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp2xxIn")

                self.csbsipmthdhistorystatsresp2xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp2xxOut")

                self.csbsipmthdhistorystatsresp3xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp3xxIn")

                self.csbsipmthdhistorystatsresp3xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp3xxOut")

                self.csbsipmthdhistorystatsresp4xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp4xxIn")

                self.csbsipmthdhistorystatsresp4xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp4xxOut")

                self.csbsipmthdhistorystatsresp5xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp5xxIn")

                self.csbsipmthdhistorystatsresp5xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp5xxOut")

                self.csbsipmthdhistorystatsresp6xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp6xxIn")

                self.csbsipmthdhistorystatsresp6xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp6xxOut")

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
                                "csbsipmthdhistorystatsadjname",
                                "csbsipmthdhistorystatsmethod",
                                "csbsipmthdhistorystatsinterval",
                                "csbsipmthdhistorystatsmethodname",
                                "csbsipmthdhistorystatsreqin",
                                "csbsipmthdhistorystatsreqout",
                                "csbsipmthdhistorystatsresp1xxin",
                                "csbsipmthdhistorystatsresp1xxout",
                                "csbsipmthdhistorystatsresp2xxin",
                                "csbsipmthdhistorystatsresp2xxout",
                                "csbsipmthdhistorystatsresp3xxin",
                                "csbsipmthdhistorystatsresp3xxout",
                                "csbsipmthdhistorystatsresp4xxin",
                                "csbsipmthdhistorystatsresp4xxout",
                                "csbsipmthdhistorystatsresp5xxin",
                                "csbsipmthdhistorystatsresp5xxout",
                                "csbsipmthdhistorystatsresp6xxin",
                                "csbsipmthdhistorystatsresp6xxout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbsipmthdhistorystatsadjname.is_set or
                    self.csbsipmthdhistorystatsmethod.is_set or
                    self.csbsipmthdhistorystatsinterval.is_set or
                    self.csbsipmthdhistorystatsmethodname.is_set or
                    self.csbsipmthdhistorystatsreqin.is_set or
                    self.csbsipmthdhistorystatsreqout.is_set or
                    self.csbsipmthdhistorystatsresp1xxin.is_set or
                    self.csbsipmthdhistorystatsresp1xxout.is_set or
                    self.csbsipmthdhistorystatsresp2xxin.is_set or
                    self.csbsipmthdhistorystatsresp2xxout.is_set or
                    self.csbsipmthdhistorystatsresp3xxin.is_set or
                    self.csbsipmthdhistorystatsresp3xxout.is_set or
                    self.csbsipmthdhistorystatsresp4xxin.is_set or
                    self.csbsipmthdhistorystatsresp4xxout.is_set or
                    self.csbsipmthdhistorystatsresp5xxin.is_set or
                    self.csbsipmthdhistorystatsresp5xxout.is_set or
                    self.csbsipmthdhistorystatsresp6xxin.is_set or
                    self.csbsipmthdhistorystatsresp6xxout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsadjname.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsmethod.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsinterval.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsmethodname.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsreqin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsreqout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp1xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp1xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp2xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp2xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp3xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp3xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp4xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp4xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp5xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp5xxout.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp6xxin.yfilter != YFilter.not_set or
                    self.csbsipmthdhistorystatsresp6xxout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbSIPMthdHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdHistoryStatsAdjName='" + self.csbsipmthdhistorystatsadjname.get() + "']" + "[csbSIPMthdHistoryStatsMethod='" + self.csbsipmthdhistorystatsmethod.get() + "']" + "[csbSIPMthdHistoryStatsInterval='" + self.csbsipmthdhistorystatsinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdHistoryStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbsipmthdhistorystatsadjname.is_set or self.csbsipmthdhistorystatsadjname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsadjname.get_name_leafdata())
                if (self.csbsipmthdhistorystatsmethod.is_set or self.csbsipmthdhistorystatsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsmethod.get_name_leafdata())
                if (self.csbsipmthdhistorystatsinterval.is_set or self.csbsipmthdhistorystatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsinterval.get_name_leafdata())
                if (self.csbsipmthdhistorystatsmethodname.is_set or self.csbsipmthdhistorystatsmethodname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsmethodname.get_name_leafdata())
                if (self.csbsipmthdhistorystatsreqin.is_set or self.csbsipmthdhistorystatsreqin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsreqin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsreqout.is_set or self.csbsipmthdhistorystatsreqout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsreqout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp1xxin.is_set or self.csbsipmthdhistorystatsresp1xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp1xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp1xxout.is_set or self.csbsipmthdhistorystatsresp1xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp1xxout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp2xxin.is_set or self.csbsipmthdhistorystatsresp2xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp2xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp2xxout.is_set or self.csbsipmthdhistorystatsresp2xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp2xxout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp3xxin.is_set or self.csbsipmthdhistorystatsresp3xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp3xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp3xxout.is_set or self.csbsipmthdhistorystatsresp3xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp3xxout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp4xxin.is_set or self.csbsipmthdhistorystatsresp4xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp4xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp4xxout.is_set or self.csbsipmthdhistorystatsresp4xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp4xxout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp5xxin.is_set or self.csbsipmthdhistorystatsresp5xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp5xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp5xxout.is_set or self.csbsipmthdhistorystatsresp5xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp5xxout.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp6xxin.is_set or self.csbsipmthdhistorystatsresp6xxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp6xxin.get_name_leafdata())
                if (self.csbsipmthdhistorystatsresp6xxout.is_set or self.csbsipmthdhistorystatsresp6xxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdhistorystatsresp6xxout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbSIPMthdHistoryStatsAdjName" or name == "csbSIPMthdHistoryStatsMethod" or name == "csbSIPMthdHistoryStatsInterval" or name == "csbSIPMthdHistoryStatsMethodName" or name == "csbSIPMthdHistoryStatsReqIn" or name == "csbSIPMthdHistoryStatsReqOut" or name == "csbSIPMthdHistoryStatsResp1xxIn" or name == "csbSIPMthdHistoryStatsResp1xxOut" or name == "csbSIPMthdHistoryStatsResp2xxIn" or name == "csbSIPMthdHistoryStatsResp2xxOut" or name == "csbSIPMthdHistoryStatsResp3xxIn" or name == "csbSIPMthdHistoryStatsResp3xxOut" or name == "csbSIPMthdHistoryStatsResp4xxIn" or name == "csbSIPMthdHistoryStatsResp4xxOut" or name == "csbSIPMthdHistoryStatsResp5xxIn" or name == "csbSIPMthdHistoryStatsResp5xxOut" or name == "csbSIPMthdHistoryStatsResp6xxIn" or name == "csbSIPMthdHistoryStatsResp6xxOut"):
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
                if(value_path == "csbSIPMthdHistoryStatsAdjName"):
                    self.csbsipmthdhistorystatsadjname = value
                    self.csbsipmthdhistorystatsadjname.value_namespace = name_space
                    self.csbsipmthdhistorystatsadjname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsMethod"):
                    self.csbsipmthdhistorystatsmethod = value
                    self.csbsipmthdhistorystatsmethod.value_namespace = name_space
                    self.csbsipmthdhistorystatsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsInterval"):
                    self.csbsipmthdhistorystatsinterval = value
                    self.csbsipmthdhistorystatsinterval.value_namespace = name_space
                    self.csbsipmthdhistorystatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsMethodName"):
                    self.csbsipmthdhistorystatsmethodname = value
                    self.csbsipmthdhistorystatsmethodname.value_namespace = name_space
                    self.csbsipmthdhistorystatsmethodname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsReqIn"):
                    self.csbsipmthdhistorystatsreqin = value
                    self.csbsipmthdhistorystatsreqin.value_namespace = name_space
                    self.csbsipmthdhistorystatsreqin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsReqOut"):
                    self.csbsipmthdhistorystatsreqout = value
                    self.csbsipmthdhistorystatsreqout.value_namespace = name_space
                    self.csbsipmthdhistorystatsreqout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp1xxIn"):
                    self.csbsipmthdhistorystatsresp1xxin = value
                    self.csbsipmthdhistorystatsresp1xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp1xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp1xxOut"):
                    self.csbsipmthdhistorystatsresp1xxout = value
                    self.csbsipmthdhistorystatsresp1xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp1xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp2xxIn"):
                    self.csbsipmthdhistorystatsresp2xxin = value
                    self.csbsipmthdhistorystatsresp2xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp2xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp2xxOut"):
                    self.csbsipmthdhistorystatsresp2xxout = value
                    self.csbsipmthdhistorystatsresp2xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp2xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp3xxIn"):
                    self.csbsipmthdhistorystatsresp3xxin = value
                    self.csbsipmthdhistorystatsresp3xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp3xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp3xxOut"):
                    self.csbsipmthdhistorystatsresp3xxout = value
                    self.csbsipmthdhistorystatsresp3xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp3xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp4xxIn"):
                    self.csbsipmthdhistorystatsresp4xxin = value
                    self.csbsipmthdhistorystatsresp4xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp4xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp4xxOut"):
                    self.csbsipmthdhistorystatsresp4xxout = value
                    self.csbsipmthdhistorystatsresp4xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp4xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp5xxIn"):
                    self.csbsipmthdhistorystatsresp5xxin = value
                    self.csbsipmthdhistorystatsresp5xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp5xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp5xxOut"):
                    self.csbsipmthdhistorystatsresp5xxout = value
                    self.csbsipmthdhistorystatsresp5xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp5xxout.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp6xxIn"):
                    self.csbsipmthdhistorystatsresp6xxin = value
                    self.csbsipmthdhistorystatsresp6xxin.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp6xxin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdHistoryStatsResp6xxOut"):
                    self.csbsipmthdhistorystatsresp6xxout = value
                    self.csbsipmthdhistorystatsresp6xxout.value_namespace = name_space
                    self.csbsipmthdhistorystatsresp6xxout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbsipmthdhistorystatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbsipmthdhistorystatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbSIPMthdHistoryStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbSIPMthdHistoryStatsEntry"):
                for c in self.csbsipmthdhistorystatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbsipmthdhistorystatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbSIPMthdHistoryStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbsipmthdrccurrentstatstable(Entity):
        """
        This table reports SIP method request and response code
        statistics for each method and response code combination on
        given SIP adjacency in a given interval. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows 
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrccurrentstatsentry
        
        	A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each entry in this table represents a method and response code combination. Each entry in this table is identified by a value of csbSIPMthdRCCurrentStatsAdjName, csbSIPMthdRCCurrentStatsMethod, csbSIPMthdRCCurrentStatsRespCode and csbSIPMthdRCCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbsipmthdrccurrentstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable, self).__init__()

            self.yang_name = "csbSIPMthdRCCurrentStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbsipmthdrccurrentstatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable, self).__setattr__(name, value)


        class Csbsipmthdrccurrentstatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each
            entry in this table represents a method and response code
            combination. Each entry in this table is identified by a value
            of csbSIPMthdRCCurrentStatsAdjName,
            csbSIPMthdRCCurrentStatsMethod,
            csbSIPMthdRCCurrentStatsRespCode and
            csbSIPMthdRCCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdrccurrentstatsadjname  <key>
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\:  str
            
            .. attribute:: csbsipmthdrccurrentstatsmethod  <key>
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\:   :py:class:`Ciscosbcsipmethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.Ciscosbcsipmethod>`
            
            .. attribute:: csbsipmthdrccurrentstatsrespcode  <key>
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrccurrentstatsinterval  <key>
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts as an index for the table
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
            .. attribute:: csbsipmthdrccurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\:  str
            
            .. attribute:: csbsipmthdrccurrentstatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdrccurrentstatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry, self).__init__()

                self.yang_name = "csbSIPMthdRCCurrentStatsEntry"
                self.yang_parent_name = "csbSIPMthdRCCurrentStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdrccurrentstatsadjname = YLeaf(YType.str, "csbSIPMthdRCCurrentStatsAdjName")

                self.csbsipmthdrccurrentstatsmethod = YLeaf(YType.enumeration, "csbSIPMthdRCCurrentStatsMethod")

                self.csbsipmthdrccurrentstatsrespcode = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespCode")

                self.csbsipmthdrccurrentstatsinterval = YLeaf(YType.enumeration, "csbSIPMthdRCCurrentStatsInterval")

                self.csbsipmthdrccurrentstatsmethodname = YLeaf(YType.str, "csbSIPMthdRCCurrentStatsMethodName")

                self.csbsipmthdrccurrentstatsrespin = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespIn")

                self.csbsipmthdrccurrentstatsrespout = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespOut")

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
                                "csbsipmthdrccurrentstatsadjname",
                                "csbsipmthdrccurrentstatsmethod",
                                "csbsipmthdrccurrentstatsrespcode",
                                "csbsipmthdrccurrentstatsinterval",
                                "csbsipmthdrccurrentstatsmethodname",
                                "csbsipmthdrccurrentstatsrespin",
                                "csbsipmthdrccurrentstatsrespout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbsipmthdrccurrentstatsadjname.is_set or
                    self.csbsipmthdrccurrentstatsmethod.is_set or
                    self.csbsipmthdrccurrentstatsrespcode.is_set or
                    self.csbsipmthdrccurrentstatsinterval.is_set or
                    self.csbsipmthdrccurrentstatsmethodname.is_set or
                    self.csbsipmthdrccurrentstatsrespin.is_set or
                    self.csbsipmthdrccurrentstatsrespout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsadjname.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsmethod.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsrespcode.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsinterval.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsmethodname.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsrespin.yfilter != YFilter.not_set or
                    self.csbsipmthdrccurrentstatsrespout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbSIPMthdRCCurrentStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdRCCurrentStatsAdjName='" + self.csbsipmthdrccurrentstatsadjname.get() + "']" + "[csbSIPMthdRCCurrentStatsMethod='" + self.csbsipmthdrccurrentstatsmethod.get() + "']" + "[csbSIPMthdRCCurrentStatsRespCode='" + self.csbsipmthdrccurrentstatsrespcode.get() + "']" + "[csbSIPMthdRCCurrentStatsInterval='" + self.csbsipmthdrccurrentstatsinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdRCCurrentStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsadjname.is_set or self.csbsipmthdrccurrentstatsadjname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsadjname.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsmethod.is_set or self.csbsipmthdrccurrentstatsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsmethod.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsrespcode.is_set or self.csbsipmthdrccurrentstatsrespcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsrespcode.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsinterval.is_set or self.csbsipmthdrccurrentstatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsinterval.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsmethodname.is_set or self.csbsipmthdrccurrentstatsmethodname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsmethodname.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsrespin.is_set or self.csbsipmthdrccurrentstatsrespin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsrespin.get_name_leafdata())
                if (self.csbsipmthdrccurrentstatsrespout.is_set or self.csbsipmthdrccurrentstatsrespout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrccurrentstatsrespout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbSIPMthdRCCurrentStatsAdjName" or name == "csbSIPMthdRCCurrentStatsMethod" or name == "csbSIPMthdRCCurrentStatsRespCode" or name == "csbSIPMthdRCCurrentStatsInterval" or name == "csbSIPMthdRCCurrentStatsMethodName" or name == "csbSIPMthdRCCurrentStatsRespIn" or name == "csbSIPMthdRCCurrentStatsRespOut"):
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
                if(value_path == "csbSIPMthdRCCurrentStatsAdjName"):
                    self.csbsipmthdrccurrentstatsadjname = value
                    self.csbsipmthdrccurrentstatsadjname.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsadjname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsMethod"):
                    self.csbsipmthdrccurrentstatsmethod = value
                    self.csbsipmthdrccurrentstatsmethod.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsRespCode"):
                    self.csbsipmthdrccurrentstatsrespcode = value
                    self.csbsipmthdrccurrentstatsrespcode.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsrespcode.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsInterval"):
                    self.csbsipmthdrccurrentstatsinterval = value
                    self.csbsipmthdrccurrentstatsinterval.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsMethodName"):
                    self.csbsipmthdrccurrentstatsmethodname = value
                    self.csbsipmthdrccurrentstatsmethodname.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsmethodname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsRespIn"):
                    self.csbsipmthdrccurrentstatsrespin = value
                    self.csbsipmthdrccurrentstatsrespin.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsrespin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCCurrentStatsRespOut"):
                    self.csbsipmthdrccurrentstatsrespout = value
                    self.csbsipmthdrccurrentstatsrespout.value_namespace = name_space
                    self.csbsipmthdrccurrentstatsrespout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbsipmthdrccurrentstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbsipmthdrccurrentstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbSIPMthdRCCurrentStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbSIPMthdRCCurrentStatsEntry"):
                for c in self.csbsipmthdrccurrentstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbsipmthdrccurrentstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbSIPMthdRCCurrentStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csbsipmthdrchistorystatstable(Entity):
        """
        This table reports historical data for SIP method request and
        response code statistics for each method and response code 
        combination in a given past interval. The possible values of 
        interval will be previous 5 minutes, previous 15 minutes, 
        previous 1 hour and previous day. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrchistorystatsentry
        
        	A conceptual row in the csbSIPMthdRCHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdRCCurrentStatsTable table and the data is  moved from that table to this one. Each entry in this table  is identified by a value of csbSIPMthdRCHistoryStatsAdjName,  csbSIPMthdRCHistoryStatsMethod, csbSIPMthdRCHistoryStatsRespCode and csbSIPMthdRCHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of    :py:class:`Csbsipmthdrchistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable, self).__init__()

            self.yang_name = "csbSIPMthdRCHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"

            self.csbsipmthdrchistorystatsentry = YList(self)

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
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable, self).__setattr__(name, value)


        class Csbsipmthdrchistorystatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdRCHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdRCCurrentStatsTable table and the data is 
            moved from that table to this one. Each entry in this table 
            is identified by a value of csbSIPMthdRCHistoryStatsAdjName, 
            csbSIPMthdRCHistoryStatsMethod,
            csbSIPMthdRCHistoryStatsRespCode and
            csbSIPMthdRCHistoryStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdrchistorystatsadjname  <key>
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\:  str
            
            .. attribute:: csbsipmthdrchistorystatsmethod  <key>
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\:   :py:class:`Ciscosbcsipmethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.Ciscosbcsipmethod>`
            
            .. attribute:: csbsipmthdrchistorystatsrespcode  <key>
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrchistorystatsinterval  <key>
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be previous 5 min, previous 15 mins, previous 1  hour , previous 1 Day. This object acts as an index for the table
            	**type**\:   :py:class:`Ciscosbcperiodicstatsinterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.Ciscosbcperiodicstatsinterval>`
            
            .. attribute:: csbsipmthdrchistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\:  str
            
            .. attribute:: csbsipmthdrchistorystatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdrchistorystatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry, self).__init__()

                self.yang_name = "csbSIPMthdRCHistoryStatsEntry"
                self.yang_parent_name = "csbSIPMthdRCHistoryStatsTable"

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdrchistorystatsadjname = YLeaf(YType.str, "csbSIPMthdRCHistoryStatsAdjName")

                self.csbsipmthdrchistorystatsmethod = YLeaf(YType.enumeration, "csbSIPMthdRCHistoryStatsMethod")

                self.csbsipmthdrchistorystatsrespcode = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespCode")

                self.csbsipmthdrchistorystatsinterval = YLeaf(YType.enumeration, "csbSIPMthdRCHistoryStatsInterval")

                self.csbsipmthdrchistorystatsmethodname = YLeaf(YType.str, "csbSIPMthdRCHistoryStatsMethodName")

                self.csbsipmthdrchistorystatsrespin = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespIn")

                self.csbsipmthdrchistorystatsrespout = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespOut")

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
                                "csbsipmthdrchistorystatsadjname",
                                "csbsipmthdrchistorystatsmethod",
                                "csbsipmthdrchistorystatsrespcode",
                                "csbsipmthdrchistorystatsinterval",
                                "csbsipmthdrchistorystatsmethodname",
                                "csbsipmthdrchistorystatsrespin",
                                "csbsipmthdrchistorystatsrespout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csbcallstatsinstanceindex.is_set or
                    self.csbcallstatsserviceindex.is_set or
                    self.csbsipmthdrchistorystatsadjname.is_set or
                    self.csbsipmthdrchistorystatsmethod.is_set or
                    self.csbsipmthdrchistorystatsrespcode.is_set or
                    self.csbsipmthdrchistorystatsinterval.is_set or
                    self.csbsipmthdrchistorystatsmethodname.is_set or
                    self.csbsipmthdrchistorystatsrespin.is_set or
                    self.csbsipmthdrchistorystatsrespout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csbcallstatsinstanceindex.yfilter != YFilter.not_set or
                    self.csbcallstatsserviceindex.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsadjname.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsmethod.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsrespcode.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsinterval.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsmethodname.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsrespin.yfilter != YFilter.not_set or
                    self.csbsipmthdrchistorystatsrespout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csbSIPMthdRCHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdRCHistoryStatsAdjName='" + self.csbsipmthdrchistorystatsadjname.get() + "']" + "[csbSIPMthdRCHistoryStatsMethod='" + self.csbsipmthdrchistorystatsmethod.get() + "']" + "[csbSIPMthdRCHistoryStatsRespCode='" + self.csbsipmthdrchistorystatsrespcode.get() + "']" + "[csbSIPMthdRCHistoryStatsInterval='" + self.csbsipmthdrchistorystatsinterval.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdRCHistoryStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csbcallstatsinstanceindex.is_set or self.csbcallstatsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsinstanceindex.get_name_leafdata())
                if (self.csbcallstatsserviceindex.is_set or self.csbcallstatsserviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbcallstatsserviceindex.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsadjname.is_set or self.csbsipmthdrchistorystatsadjname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsadjname.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsmethod.is_set or self.csbsipmthdrchistorystatsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsmethod.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsrespcode.is_set or self.csbsipmthdrchistorystatsrespcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsrespcode.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsinterval.is_set or self.csbsipmthdrchistorystatsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsinterval.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsmethodname.is_set or self.csbsipmthdrchistorystatsmethodname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsmethodname.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsrespin.is_set or self.csbsipmthdrchistorystatsrespin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsrespin.get_name_leafdata())
                if (self.csbsipmthdrchistorystatsrespout.is_set or self.csbsipmthdrchistorystatsrespout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csbsipmthdrchistorystatsrespout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csbCallStatsInstanceIndex" or name == "csbCallStatsServiceIndex" or name == "csbSIPMthdRCHistoryStatsAdjName" or name == "csbSIPMthdRCHistoryStatsMethod" or name == "csbSIPMthdRCHistoryStatsRespCode" or name == "csbSIPMthdRCHistoryStatsInterval" or name == "csbSIPMthdRCHistoryStatsMethodName" or name == "csbSIPMthdRCHistoryStatsRespIn" or name == "csbSIPMthdRCHistoryStatsRespOut"):
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
                if(value_path == "csbSIPMthdRCHistoryStatsAdjName"):
                    self.csbsipmthdrchistorystatsadjname = value
                    self.csbsipmthdrchistorystatsadjname.value_namespace = name_space
                    self.csbsipmthdrchistorystatsadjname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsMethod"):
                    self.csbsipmthdrchistorystatsmethod = value
                    self.csbsipmthdrchistorystatsmethod.value_namespace = name_space
                    self.csbsipmthdrchistorystatsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsRespCode"):
                    self.csbsipmthdrchistorystatsrespcode = value
                    self.csbsipmthdrchistorystatsrespcode.value_namespace = name_space
                    self.csbsipmthdrchistorystatsrespcode.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsInterval"):
                    self.csbsipmthdrchistorystatsinterval = value
                    self.csbsipmthdrchistorystatsinterval.value_namespace = name_space
                    self.csbsipmthdrchistorystatsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsMethodName"):
                    self.csbsipmthdrchistorystatsmethodname = value
                    self.csbsipmthdrchistorystatsmethodname.value_namespace = name_space
                    self.csbsipmthdrchistorystatsmethodname.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsRespIn"):
                    self.csbsipmthdrchistorystatsrespin = value
                    self.csbsipmthdrchistorystatsrespin.value_namespace = name_space
                    self.csbsipmthdrchistorystatsrespin.value_namespace_prefix = name_space_prefix
                if(value_path == "csbSIPMthdRCHistoryStatsRespOut"):
                    self.csbsipmthdrchistorystatsrespout = value
                    self.csbsipmthdrchistorystatsrespout.value_namespace = name_space
                    self.csbsipmthdrchistorystatsrespout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csbsipmthdrchistorystatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csbsipmthdrchistorystatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csbSIPMthdRCHistoryStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csbSIPMthdRCHistoryStatsEntry"):
                for c in self.csbsipmthdrchistorystatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csbsipmthdrchistorystatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csbSIPMthdRCHistoryStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.csbradiusstatstable is not None and self.csbradiusstatstable.has_data()) or
            (self.csbrfbillrealmstatstable is not None and self.csbrfbillrealmstatstable.has_data()) or
            (self.csbsipmthdcurrentstatstable is not None and self.csbsipmthdcurrentstatstable.has_data()) or
            (self.csbsipmthdhistorystatstable is not None and self.csbsipmthdhistorystatstable.has_data()) or
            (self.csbsipmthdrccurrentstatstable is not None and self.csbsipmthdrccurrentstatstable.has_data()) or
            (self.csbsipmthdrchistorystatstable is not None and self.csbsipmthdrchistorystatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.csbradiusstatstable is not None and self.csbradiusstatstable.has_operation()) or
            (self.csbrfbillrealmstatstable is not None and self.csbrfbillrealmstatstable.has_operation()) or
            (self.csbsipmthdcurrentstatstable is not None and self.csbsipmthdcurrentstatstable.has_operation()) or
            (self.csbsipmthdhistorystatstable is not None and self.csbsipmthdhistorystatstable.has_operation()) or
            (self.csbsipmthdrccurrentstatstable is not None and self.csbsipmthdrccurrentstatstable.has_operation()) or
            (self.csbsipmthdrchistorystatstable is not None and self.csbsipmthdrchistorystatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB" + path_buffer

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

        if (child_yang_name == "csbRadiusStatsTable"):
            if (self.csbradiusstatstable is None):
                self.csbradiusstatstable = CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable()
                self.csbradiusstatstable.parent = self
                self._children_name_map["csbradiusstatstable"] = "csbRadiusStatsTable"
            return self.csbradiusstatstable

        if (child_yang_name == "csbRfBillRealmStatsTable"):
            if (self.csbrfbillrealmstatstable is None):
                self.csbrfbillrealmstatstable = CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable()
                self.csbrfbillrealmstatstable.parent = self
                self._children_name_map["csbrfbillrealmstatstable"] = "csbRfBillRealmStatsTable"
            return self.csbrfbillrealmstatstable

        if (child_yang_name == "csbSIPMthdCurrentStatsTable"):
            if (self.csbsipmthdcurrentstatstable is None):
                self.csbsipmthdcurrentstatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable()
                self.csbsipmthdcurrentstatstable.parent = self
                self._children_name_map["csbsipmthdcurrentstatstable"] = "csbSIPMthdCurrentStatsTable"
            return self.csbsipmthdcurrentstatstable

        if (child_yang_name == "csbSIPMthdHistoryStatsTable"):
            if (self.csbsipmthdhistorystatstable is None):
                self.csbsipmthdhistorystatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable()
                self.csbsipmthdhistorystatstable.parent = self
                self._children_name_map["csbsipmthdhistorystatstable"] = "csbSIPMthdHistoryStatsTable"
            return self.csbsipmthdhistorystatstable

        if (child_yang_name == "csbSIPMthdRCCurrentStatsTable"):
            if (self.csbsipmthdrccurrentstatstable is None):
                self.csbsipmthdrccurrentstatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable()
                self.csbsipmthdrccurrentstatstable.parent = self
                self._children_name_map["csbsipmthdrccurrentstatstable"] = "csbSIPMthdRCCurrentStatsTable"
            return self.csbsipmthdrccurrentstatstable

        if (child_yang_name == "csbSIPMthdRCHistoryStatsTable"):
            if (self.csbsipmthdrchistorystatstable is None):
                self.csbsipmthdrchistorystatstable = CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable()
                self.csbsipmthdrchistorystatstable.parent = self
                self._children_name_map["csbsipmthdrchistorystatstable"] = "csbSIPMthdRCHistoryStatsTable"
            return self.csbsipmthdrchistorystatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "csbRadiusStatsTable" or name == "csbRfBillRealmStatsTable" or name == "csbSIPMthdCurrentStatsTable" or name == "csbSIPMthdHistoryStatsTable" or name == "csbSIPMthdRCCurrentStatsTable" or name == "csbSIPMthdRCHistoryStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoSessBorderCtrlrStatsMib()
        return self._top_entity

