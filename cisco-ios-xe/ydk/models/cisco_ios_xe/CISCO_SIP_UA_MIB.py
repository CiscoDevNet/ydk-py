""" CISCO_SIP_UA_MIB 

Cisco User Agent Session Initiation Protocol (SIP) 
MIB module.  SIP is an application\-layer signalling
protocol for creating, modifying and terminating
multimedia sessions with one or more participants.
These sessions include Internet multimedia conferences
and Internet telephone calls.  SIP is defined in 
RFC 2543 (March 1999).  

This MIB is defined for the management of SIP User 
Agents (UAs).  A User Agent is an application which 
contains both a User Agent Client (UAC) and a User 
Agent Server (UAS).   A UAC is an application that 
initiates a SIP request.  A UAS is an application that 
contacts the user when a SIP request is received and 
that returns a response on behalf of the user.  The 
response accepts, rejects, or redirects the request.

A SIP transaction occurs between a client and a server 
and comprises all messages from the first request sent
from the client to the server up to a final (non\-1xx) 
response sent from the server to the client.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ciscosipuamibnotificationprefix(Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(Ciscosipuamibnotificationprefix, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB:ciscoSipUaMIBNotificationPrefix")


class Ciscosipuamibnotifications(Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(Ciscosipuamibnotifications, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB:ciscoSipUaMIBNotifications")


class CISCOSIPUAMIB(Entity):
    """
    
    
    .. attribute:: csipcfgbase
    
    	
    	**type**\:  :py:class:`Csipcfgbase <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase>`
    
    .. attribute:: csipcfgtimer
    
    	
    	**type**\:  :py:class:`Csipcfgtimer <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgtimer>`
    
    .. attribute:: csipcfgretry
    
    	
    	**type**\:  :py:class:`Csipcfgretry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgretry>`
    
    .. attribute:: csipcfgpeer
    
    	
    	**type**\:  :py:class:`Csipcfgpeer <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeer>`
    
    .. attribute:: csipcfgaaa
    
    	
    	**type**\:  :py:class:`Csipcfgaaa <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgaaa>`
    
    .. attribute:: csipcfgvoiceservicevoip
    
    	
    	**type**\:  :py:class:`Csipcfgvoiceservicevoip <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgvoiceservicevoip>`
    
    .. attribute:: csipstatsinfo
    
    	
    	**type**\:  :py:class:`Csipstatsinfo <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsinfo>`
    
    .. attribute:: csipstatssuccess
    
    	
    	**type**\:  :py:class:`Csipstatssuccess <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatssuccess>`
    
    .. attribute:: csipstatsredirect
    
    	
    	**type**\:  :py:class:`Csipstatsredirect <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsredirect>`
    
    .. attribute:: csipstatserrclient
    
    	
    	**type**\:  :py:class:`Csipstatserrclient <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatserrclient>`
    
    .. attribute:: csipstatserrserver
    
    	
    	**type**\:  :py:class:`Csipstatserrserver <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatserrserver>`
    
    .. attribute:: csipstatsglobalfail
    
    	
    	**type**\:  :py:class:`Csipstatsglobalfail <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsglobalfail>`
    
    .. attribute:: csipstatstraffic
    
    	
    	**type**\:  :py:class:`Csipstatstraffic <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatstraffic>`
    
    .. attribute:: csipstatsretry
    
    	
    	**type**\:  :py:class:`Csipstatsretry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsretry>`
    
    .. attribute:: csipstatsmisc
    
    	
    	**type**\:  :py:class:`Csipstatsmisc <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsmisc>`
    
    .. attribute:: csipstatsconnection
    
    	
    	**type**\:  :py:class:`Csipstatsconnection <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatsconnection>`
    
    .. attribute:: csipcfgearlymediatable
    
    	This table contains configuration for Early Media Cut Through.  The configuration controls how the SIP user agent will process 1xx (Provisional) SIP response messages that contain  Session Definition Protocol (SDP) payloads
    	**type**\:  :py:class:`Csipcfgearlymediatable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgearlymediatable>`
    
    .. attribute:: csipcfgbindsourceaddrtable
    
    	This table contains configuration for binding the scope of packets to the particular ethernet interface. The scope for the packets can be specified as either 'signalling' or 'media' packets. The ethernet interface shall be specified by the interface index. The table shall be indexed based on the scope
    	**type**\:  :py:class:`Csipcfgbindsourceaddrtable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbindsourceaddrtable>`
    
    .. attribute:: csipcfgpeertable
    
    	This table contains per dial\-peer SIP related  configuration.     The table is a sparse table of dial\-peer information. This means, it only reflects dial\-peers being used  for SIP.  A dial\-peer is being used for SIP if the  value of cvVoIPPeerCfgSessionProtocol  (CISCO\-VOICE\-DIAL\-CONTROL\-MIB) is 'sip'.  Dial\-peers are not created or destroyed via this table.  Only SIP related configuration can be  performed via this table once the dial\-peer exists in the system and is visible in this table
    	**type**\:  :py:class:`Csipcfgpeertable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeertable>`
    
    .. attribute:: csipcfgstatuscausetable
    
    	This table contains SIP status code to PSTN cause code mapping configuration.  Inbound SIP response messages  that will result in outbound PSTN signalling messages will have the SIP status codes transposed into the PSTN cause codes as prescribed by the contents of this  table
    	**type**\:  :py:class:`Csipcfgstatuscausetable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgstatuscausetable>`
    
    .. attribute:: csipcfgcausestatustable
    
    	This table contains PSTN cause code to SIP status code mapping configuration.   Inbound PSTN signalling messages that will result in outbound SIP response messages  will have the PSTN cause codes transposed into the SIP status codes as prescribed by the contents of this  table
    	**type**\:  :py:class:`Csipcfgcausestatustable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgcausestatustable>`
    
    .. attribute:: csipstatssuccessoktable
    
    	This table contains statistics for sent and received 200 Ok response messages.  The  statistics are kept on per SIP method basis
    	**type**\:  :py:class:`Csipstatssuccessoktable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatssuccessoktable>`
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(CISCOSIPUAMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SIP-UA-MIB"
        self.yang_parent_name = "CISCO-SIP-UA-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cSipCfgBase", ("csipcfgbase", CISCOSIPUAMIB.Csipcfgbase)), ("cSipCfgTimer", ("csipcfgtimer", CISCOSIPUAMIB.Csipcfgtimer)), ("cSipCfgRetry", ("csipcfgretry", CISCOSIPUAMIB.Csipcfgretry)), ("cSipCfgPeer", ("csipcfgpeer", CISCOSIPUAMIB.Csipcfgpeer)), ("cSipCfgAaa", ("csipcfgaaa", CISCOSIPUAMIB.Csipcfgaaa)), ("cSipCfgVoiceServiceVoip", ("csipcfgvoiceservicevoip", CISCOSIPUAMIB.Csipcfgvoiceservicevoip)), ("cSipStatsInfo", ("csipstatsinfo", CISCOSIPUAMIB.Csipstatsinfo)), ("cSipStatsSuccess", ("csipstatssuccess", CISCOSIPUAMIB.Csipstatssuccess)), ("cSipStatsRedirect", ("csipstatsredirect", CISCOSIPUAMIB.Csipstatsredirect)), ("cSipStatsErrClient", ("csipstatserrclient", CISCOSIPUAMIB.Csipstatserrclient)), ("cSipStatsErrServer", ("csipstatserrserver", CISCOSIPUAMIB.Csipstatserrserver)), ("cSipStatsGlobalFail", ("csipstatsglobalfail", CISCOSIPUAMIB.Csipstatsglobalfail)), ("cSipStatsTraffic", ("csipstatstraffic", CISCOSIPUAMIB.Csipstatstraffic)), ("cSipStatsRetry", ("csipstatsretry", CISCOSIPUAMIB.Csipstatsretry)), ("cSipStatsMisc", ("csipstatsmisc", CISCOSIPUAMIB.Csipstatsmisc)), ("cSipStatsConnection", ("csipstatsconnection", CISCOSIPUAMIB.Csipstatsconnection)), ("cSipCfgEarlyMediaTable", ("csipcfgearlymediatable", CISCOSIPUAMIB.Csipcfgearlymediatable)), ("cSipCfgBindSourceAddrTable", ("csipcfgbindsourceaddrtable", CISCOSIPUAMIB.Csipcfgbindsourceaddrtable)), ("cSipCfgPeerTable", ("csipcfgpeertable", CISCOSIPUAMIB.Csipcfgpeertable)), ("cSipCfgStatusCauseTable", ("csipcfgstatuscausetable", CISCOSIPUAMIB.Csipcfgstatuscausetable)), ("cSipCfgCauseStatusTable", ("csipcfgcausestatustable", CISCOSIPUAMIB.Csipcfgcausestatustable)), ("cSipStatsSuccessOkTable", ("csipstatssuccessoktable", CISCOSIPUAMIB.Csipstatssuccessoktable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.csipcfgbase = CISCOSIPUAMIB.Csipcfgbase()
        self.csipcfgbase.parent = self
        self._children_name_map["csipcfgbase"] = "cSipCfgBase"
        self._children_yang_names.add("cSipCfgBase")

        self.csipcfgtimer = CISCOSIPUAMIB.Csipcfgtimer()
        self.csipcfgtimer.parent = self
        self._children_name_map["csipcfgtimer"] = "cSipCfgTimer"
        self._children_yang_names.add("cSipCfgTimer")

        self.csipcfgretry = CISCOSIPUAMIB.Csipcfgretry()
        self.csipcfgretry.parent = self
        self._children_name_map["csipcfgretry"] = "cSipCfgRetry"
        self._children_yang_names.add("cSipCfgRetry")

        self.csipcfgpeer = CISCOSIPUAMIB.Csipcfgpeer()
        self.csipcfgpeer.parent = self
        self._children_name_map["csipcfgpeer"] = "cSipCfgPeer"
        self._children_yang_names.add("cSipCfgPeer")

        self.csipcfgaaa = CISCOSIPUAMIB.Csipcfgaaa()
        self.csipcfgaaa.parent = self
        self._children_name_map["csipcfgaaa"] = "cSipCfgAaa"
        self._children_yang_names.add("cSipCfgAaa")

        self.csipcfgvoiceservicevoip = CISCOSIPUAMIB.Csipcfgvoiceservicevoip()
        self.csipcfgvoiceservicevoip.parent = self
        self._children_name_map["csipcfgvoiceservicevoip"] = "cSipCfgVoiceServiceVoip"
        self._children_yang_names.add("cSipCfgVoiceServiceVoip")

        self.csipstatsinfo = CISCOSIPUAMIB.Csipstatsinfo()
        self.csipstatsinfo.parent = self
        self._children_name_map["csipstatsinfo"] = "cSipStatsInfo"
        self._children_yang_names.add("cSipStatsInfo")

        self.csipstatssuccess = CISCOSIPUAMIB.Csipstatssuccess()
        self.csipstatssuccess.parent = self
        self._children_name_map["csipstatssuccess"] = "cSipStatsSuccess"
        self._children_yang_names.add("cSipStatsSuccess")

        self.csipstatsredirect = CISCOSIPUAMIB.Csipstatsredirect()
        self.csipstatsredirect.parent = self
        self._children_name_map["csipstatsredirect"] = "cSipStatsRedirect"
        self._children_yang_names.add("cSipStatsRedirect")

        self.csipstatserrclient = CISCOSIPUAMIB.Csipstatserrclient()
        self.csipstatserrclient.parent = self
        self._children_name_map["csipstatserrclient"] = "cSipStatsErrClient"
        self._children_yang_names.add("cSipStatsErrClient")

        self.csipstatserrserver = CISCOSIPUAMIB.Csipstatserrserver()
        self.csipstatserrserver.parent = self
        self._children_name_map["csipstatserrserver"] = "cSipStatsErrServer"
        self._children_yang_names.add("cSipStatsErrServer")

        self.csipstatsglobalfail = CISCOSIPUAMIB.Csipstatsglobalfail()
        self.csipstatsglobalfail.parent = self
        self._children_name_map["csipstatsglobalfail"] = "cSipStatsGlobalFail"
        self._children_yang_names.add("cSipStatsGlobalFail")

        self.csipstatstraffic = CISCOSIPUAMIB.Csipstatstraffic()
        self.csipstatstraffic.parent = self
        self._children_name_map["csipstatstraffic"] = "cSipStatsTraffic"
        self._children_yang_names.add("cSipStatsTraffic")

        self.csipstatsretry = CISCOSIPUAMIB.Csipstatsretry()
        self.csipstatsretry.parent = self
        self._children_name_map["csipstatsretry"] = "cSipStatsRetry"
        self._children_yang_names.add("cSipStatsRetry")

        self.csipstatsmisc = CISCOSIPUAMIB.Csipstatsmisc()
        self.csipstatsmisc.parent = self
        self._children_name_map["csipstatsmisc"] = "cSipStatsMisc"
        self._children_yang_names.add("cSipStatsMisc")

        self.csipstatsconnection = CISCOSIPUAMIB.Csipstatsconnection()
        self.csipstatsconnection.parent = self
        self._children_name_map["csipstatsconnection"] = "cSipStatsConnection"
        self._children_yang_names.add("cSipStatsConnection")

        self.csipcfgearlymediatable = CISCOSIPUAMIB.Csipcfgearlymediatable()
        self.csipcfgearlymediatable.parent = self
        self._children_name_map["csipcfgearlymediatable"] = "cSipCfgEarlyMediaTable"
        self._children_yang_names.add("cSipCfgEarlyMediaTable")

        self.csipcfgbindsourceaddrtable = CISCOSIPUAMIB.Csipcfgbindsourceaddrtable()
        self.csipcfgbindsourceaddrtable.parent = self
        self._children_name_map["csipcfgbindsourceaddrtable"] = "cSipCfgBindSourceAddrTable"
        self._children_yang_names.add("cSipCfgBindSourceAddrTable")

        self.csipcfgpeertable = CISCOSIPUAMIB.Csipcfgpeertable()
        self.csipcfgpeertable.parent = self
        self._children_name_map["csipcfgpeertable"] = "cSipCfgPeerTable"
        self._children_yang_names.add("cSipCfgPeerTable")

        self.csipcfgstatuscausetable = CISCOSIPUAMIB.Csipcfgstatuscausetable()
        self.csipcfgstatuscausetable.parent = self
        self._children_name_map["csipcfgstatuscausetable"] = "cSipCfgStatusCauseTable"
        self._children_yang_names.add("cSipCfgStatusCauseTable")

        self.csipcfgcausestatustable = CISCOSIPUAMIB.Csipcfgcausestatustable()
        self.csipcfgcausestatustable.parent = self
        self._children_name_map["csipcfgcausestatustable"] = "cSipCfgCauseStatusTable"
        self._children_yang_names.add("cSipCfgCauseStatusTable")

        self.csipstatssuccessoktable = CISCOSIPUAMIB.Csipstatssuccessoktable()
        self.csipstatssuccessoktable.parent = self
        self._children_name_map["csipstatssuccessoktable"] = "cSipStatsSuccessOkTable"
        self._children_yang_names.add("cSipStatsSuccessOkTable")
        self._segment_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB"


    class Csipcfgbase(Entity):
        """
        
        
        .. attribute:: csipcfgversion
        
        	This object will reflect the version of SIP supported by this  user agent.  It will follow the same format as SIP version  information contained in the SIP messages generated by this user agent.  For example, user agents supporting SIP version 2 will return 'SIP/2.0' as dictated by RFC 2543
        	**type**\: str
        
        .. attribute:: csipcfgtransport
        
        	This object specifies the transport protocol the SIP user  agent will use to receive SIP messages.  A value of 'disabled' indicates that the UA will not receive any SIP messages
        	**type**\:  :py:class:`Csipcfgtransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase.Csipcfgtransport>`
        
        .. attribute:: csipcfguserlocationserveraddr
        
        	This object specifies address of the User Location  Server (ULS) being used to resolve the location of end  points.  This could be a Domain Name Server (DNS) or a  SIP proxy/redirect server.  The format of the address follows the IETF service location  protocol. The syntax is as follows\:     mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching  dial string to a target server. The type\-specific\-syntax is  exactly that, something that the particular mapping scheme can understand.  For example,    Session target           Meaning    ipv4\:171.68.13.55\:1006   The session target is the IP                              version 4 address of 171.68.13.55                              and port 1006.    dns\:pots.cisco.com       The session target is the IP host                              with dns name pots.cisco.com.  The valid Mapping type definitions for the peer follow\:    ipv4  \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z     dns   \- Syntax\: dns\:host.domain
        	**type**\: str
        
        .. attribute:: csipcfgmaxforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\: int
        
        	**range:** 1..70
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgbindsrcaddrinterface
        
        	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that  there is no specific source address configured and  in this case the best local IP address will be chosen  by the system
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgbindsrcaddrscope
        
        	This object specifies the scope of packets to which the source IP address of the interface  designated by cSipCfgBindSrcAddrInterface will be bound.  A value of 'all' means the IP address  will be bound to both SIP signalling and media packets. A value of 'control' means the IP address will only be bound to SIP signalling packets.   If cSipCfgBindSrcAddrInterface is set to 0, the value of this object has no meaning
        	**type**\:  :py:class:`Csipcfgbindsrcaddrscope <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase.Csipcfgbindsrcaddrscope>`
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgdnssrvquerystringformat
        
        	This object specifies the format of the prefix used  by the system for DNS SRV queries.  v1  \:  RFC 2052 format \- 'protocol.transport.' v2  \:  RFC 2782 format \- '\_protocol.\_transport.'  This object allows backward compatibility with systems only supporting RFC 2052 format
        	**type**\:  :py:class:`Csipcfgdnssrvquerystringformat <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase.Csipcfgdnssrvquerystringformat>`
        
        .. attribute:: csipcfgredirectiondisabled
        
        	This object specifies how call redirection (3xx) is handled by the user agent.    If 'false', the user agent's treatment of incoming  3xx class response messages is as defined in RFC 2543.   That is, the user agent uses the Contact header(s) from the 3xx response to reinitiate another INVITE transaction to the user's new location.  The call  is redirected.  If 'true', the user agent treats incoming 3xx  response messages as 4xx (client error) class  response messages.  In this case, the call is not redirected, instead it is released with the  appropriate PSTN cause code.  The mapping of SIP 3xx response status codes to 4xx response status codes is as follows\:  300 Multiple Choices \-> 410 Gone  301 Moved Permanently \-> 410 Gone  302 Moved Temporarily \-> 480 Temporarily Unavailable  305 User Proxy        \-> 410 Gone  380 Alternative Service \-> 410 Gone  Any other 3xx \-> 410 Gone
        	**type**\: bool
        
        .. attribute:: csipcfgsymnatenabled
        
        	This object specifies whether remote media checks for Symmetric Network Address Translation (NAT)  is enabled or disabled.  If 'true', remote media checks are enabled.  The gateway will have the ability to open a Real Time  Transport Protocol (RTP) session with the remote end and then update (modify) the existing RTP session's remote address/port (raddr\:rport) with the source address and port of the actual media packet received.  This would be triggered for only those calls where the Session Description Protocol (SDP) received by the gateway has an indication to do so.  If 'false', remote media checks are disabled
        	**type**\: bool
        
        .. attribute:: csipcfgsymnatdirectionrole
        
        	This object specifies the value of the 'a=direction\:<role>' SDP attribute supported by  the user agent.  The direction attribute is used  to describe the role of the user agent (as an  endpoint for a connection\-oriented media stream)  in the connection setup procedure.  none    \:  No role is specified. passive \:  The user agent will advertise itself            as a 'passive' entity (inside the NAT)            in the SDP. active  \:  The user agent will advertise itself            as a 'active' entity (outside the NAT)            in the SDP
        	**type**\:  :py:class:`Csipcfgsymnatdirectionrole <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase.Csipcfgsymnatdirectionrole>`
        
        .. attribute:: csipcfgsuspendresumeenabled
        
        	This object specifies if support for handling  Suspend/Resume events from the switch is enabled or not.  If 'true', the user agent on getting a Suspend will notify the remote agent by sending it a re\-invite with a hold SDP. Similarly, when the Gateway receives a Resume, it will initiate a re\-invite with the original SDP and unhold the call.  If 'false', the user agent will not initiate any re\-invites on receiving Suspend/Resume events, basically it won't be putting the call on hold or off hold
        	**type**\: bool
        
        .. attribute:: csipcfgoffercallhold
        
        	This object specifies how the SIP gateway would initiate call hold requests.  directionAttr\: The user agent will use the direction                 attribute such as a=sendonly or a=inactive in                 the sdp to initiate call hold requests.                    connAddr\: The user agent will use 0.0.0.0 connection address            to specify Call Hold
        	**type**\:  :py:class:`Csipcfgoffercallhold <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbase.Csipcfgoffercallhold>`
        
        .. attribute:: csipcfgreasonheaderoveride
        
        	This object specifies that the Reason header overrides SIP  status code mapping table
        	**type**\: bool
        
        .. attribute:: csipcfgmaximumforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\: int
        
        	**range:** 1..70
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgbase, self).__init__()

            self.yang_name = "cSipCfgBase"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgversion', YLeaf(YType.str, 'cSipCfgVersion')),
                ('csipcfgtransport', YLeaf(YType.enumeration, 'cSipCfgTransport')),
                ('csipcfguserlocationserveraddr', YLeaf(YType.str, 'cSipCfgUserLocationServerAddr')),
                ('csipcfgmaxforwards', YLeaf(YType.int32, 'cSipCfgMaxForwards')),
                ('csipcfgbindsrcaddrinterface', YLeaf(YType.int32, 'cSipCfgBindSrcAddrInterface')),
                ('csipcfgbindsrcaddrscope', YLeaf(YType.enumeration, 'cSipCfgBindSrcAddrScope')),
                ('csipcfgdnssrvquerystringformat', YLeaf(YType.enumeration, 'cSipCfgDnsSrvQueryStringFormat')),
                ('csipcfgredirectiondisabled', YLeaf(YType.boolean, 'cSipCfgRedirectionDisabled')),
                ('csipcfgsymnatenabled', YLeaf(YType.boolean, 'cSipCfgSymNatEnabled')),
                ('csipcfgsymnatdirectionrole', YLeaf(YType.enumeration, 'cSipCfgSymNatDirectionRole')),
                ('csipcfgsuspendresumeenabled', YLeaf(YType.boolean, 'cSipCfgSuspendResumeEnabled')),
                ('csipcfgoffercallhold', YLeaf(YType.enumeration, 'cSipCfgOfferCallHold')),
                ('csipcfgreasonheaderoveride', YLeaf(YType.boolean, 'cSipCfgReasonHeaderOveride')),
                ('csipcfgmaximumforwards', YLeaf(YType.int32, 'cSipCfgMaximumForwards')),
            ])
            self.csipcfgversion = None
            self.csipcfgtransport = None
            self.csipcfguserlocationserveraddr = None
            self.csipcfgmaxforwards = None
            self.csipcfgbindsrcaddrinterface = None
            self.csipcfgbindsrcaddrscope = None
            self.csipcfgdnssrvquerystringformat = None
            self.csipcfgredirectiondisabled = None
            self.csipcfgsymnatenabled = None
            self.csipcfgsymnatdirectionrole = None
            self.csipcfgsuspendresumeenabled = None
            self.csipcfgoffercallhold = None
            self.csipcfgreasonheaderoveride = None
            self.csipcfgmaximumforwards = None
            self._segment_path = lambda: "cSipCfgBase"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgbase, ['csipcfgversion', 'csipcfgtransport', 'csipcfguserlocationserveraddr', 'csipcfgmaxforwards', 'csipcfgbindsrcaddrinterface', 'csipcfgbindsrcaddrscope', 'csipcfgdnssrvquerystringformat', 'csipcfgredirectiondisabled', 'csipcfgsymnatenabled', 'csipcfgsymnatdirectionrole', 'csipcfgsuspendresumeenabled', 'csipcfgoffercallhold', 'csipcfgreasonheaderoveride', 'csipcfgmaximumforwards'], name, value)

        class Csipcfgbindsrcaddrscope(Enum):
            """
            Csipcfgbindsrcaddrscope (Enum Class)

            This object specifies the scope of packets to

            which the source IP address of the interface 

            designated by cSipCfgBindSrcAddrInterface

            will be bound.  A value of 'all' means the IP address 

            will be bound to both SIP signalling and media packets.

            A value of 'control' means the IP address will only

            be bound to SIP signalling packets.  

            If cSipCfgBindSrcAddrInterface is set to 0,

            the value of this object has no meaning.

            .. data:: none = 0

            .. data:: all = 1

            .. data:: control = 2

            """

            none = Enum.YLeaf(0, "none")

            all = Enum.YLeaf(1, "all")

            control = Enum.YLeaf(2, "control")


        class Csipcfgdnssrvquerystringformat(Enum):
            """
            Csipcfgdnssrvquerystringformat (Enum Class)

            This object specifies the format of the prefix used 

            by the system for DNS SRV queries.

            v1  \:  RFC 2052 format \- 'protocol.transport.'

            v2  \:  RFC 2782 format \- '\_protocol.\_transport.'

            This object allows backward compatibility with systems

            only supporting RFC 2052 format.

            .. data:: v1 = 1

            .. data:: v2 = 2

            """

            v1 = Enum.YLeaf(1, "v1")

            v2 = Enum.YLeaf(2, "v2")


        class Csipcfgoffercallhold(Enum):
            """
            Csipcfgoffercallhold (Enum Class)

            This object specifies how the SIP gateway would initiate call

            hold requests.

            directionAttr\: The user agent will use the direction

                            attribute such as a=sendonly or a=inactive in

                            the sdp to initiate call hold requests.

            connAddr\: The user agent will use 0.0.0.0 connection address

                       to specify Call Hold.

            .. data:: directionAttr = 1

            .. data:: connAddr = 2

            """

            directionAttr = Enum.YLeaf(1, "directionAttr")

            connAddr = Enum.YLeaf(2, "connAddr")


        class Csipcfgsymnatdirectionrole(Enum):
            """
            Csipcfgsymnatdirectionrole (Enum Class)

            This object specifies the value of the

            'a=direction\:<role>' SDP attribute supported by 

            the user agent.  The direction attribute is used 

            to describe the role of the user agent (as an 

            endpoint for a connection\-oriented media stream) 

            in the connection setup procedure.

            none    \:  No role is specified.

            passive \:  The user agent will advertise itself

                       as a 'passive' entity (inside the NAT)

                       in the SDP.

            active  \:  The user agent will advertise itself

                       as a 'active' entity (outside the NAT)

                       in the SDP.

            .. data:: none = 1

            .. data:: passive = 2

            .. data:: active = 3

            """

            none = Enum.YLeaf(1, "none")

            passive = Enum.YLeaf(2, "passive")

            active = Enum.YLeaf(3, "active")


        class Csipcfgtransport(Enum):
            """
            Csipcfgtransport (Enum Class)

            This object specifies the transport protocol the SIP user 

            agent will use to receive SIP messages.  A value of 'disabled'

            indicates that the UA will not receive any SIP messages.

            .. data:: udp = 1

            .. data:: tcp = 2

            .. data:: udpAndTcp = 3

            .. data:: disabled = 4

            """

            udp = Enum.YLeaf(1, "udp")

            tcp = Enum.YLeaf(2, "tcp")

            udpAndTcp = Enum.YLeaf(3, "udpAndTcp")

            disabled = Enum.YLeaf(4, "disabled")



    class Csipcfgtimer(Entity):
        """
        
        
        .. attribute:: csipcfgtimertrying
        
        	This object specifies the time a user agent will wait to  receive a provisional response to a INVITE before resending  the INVITE
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerexpires
        
        	This object specifies the time a user agent will wait to  receive a final response to a INVITE before cancelling the  transaction
        	**type**\: int
        
        	**range:** 60000..300000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerconnect
        
        	This object specifies the time a user agent will wait to  receive an ACK confirmation a session is established
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerdisconnect
        
        	This object specifies the time a user agent will wait to  receive an BYE confirmation a session is disconnected
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerprack
        
        	This object specifies the time a user agent will wait for  a final response before retransmitting the PRACK (PRovisional ACKnowledgment)
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimercomet
        
        	This object specifies the time a user agent will wait  for a final response before retransmitting the COMET  (COndition MET)
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerreliablersp
        
        	This object specifies the amount of time to wait for a PRACK before retransmitting the reliable 1xx response
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimernotify
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Notify
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerrefer
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Refer
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimersessiontimer
        
        	This object specifies the value of the Min\-SE  header for INVITE messages originated by this  user agent and the minimum value of the  Session\-Expires headers for INVITE messages  received by this user agent.  Any Session\-Expires headers received with a  value below this object's value will be rejected with a 422 client error response message.  Setting this object to a value less than 600 is valid, but the possibly of excessive re\-INVITES  and the impact of those messages should be fully  understood and considered an acceptable risk
        	**type**\: int
        
        	**range:** 60..86400
        
        	**units**\: seconds
        
        .. attribute:: csipcfgtimerhold
        
        	This object specifies the amount of time to wait before  disconnecting a call already on hold. A value of 0 specifies that this functionality is disabled
        	**type**\: int
        
        	**range:** 0..None \| 15..2880
        
        	**units**\: minutes
        
        .. attribute:: csipcfgtimerinfo
        
        	This object specifies the amount of time to wait for a 200ok response before retransmitting the Info
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerconnectionaging
        
        	This object specifies the amount of time to wait before  aging out a TCP/UDP connection
        	**type**\: int
        
        	**range:** 5..30
        
        	**units**\: minutes
        
        .. attribute:: csipcfgtimerbufferinvite
        
        	This object specifies the amount of time to buffer the INVITE  while waiting for display name info in the Facility.  A value of 0 means that the INVITE wouldn't be buffered waiting for the display name info in the Facility
        	**type**\: int
        
        	**range:** 0..None \| 50..5000
        
        	**units**\: milliseconds
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgtimer, self).__init__()

            self.yang_name = "cSipCfgTimer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgtimertrying', YLeaf(YType.int32, 'cSipCfgTimerTrying')),
                ('csipcfgtimerexpires', YLeaf(YType.int32, 'cSipCfgTimerExpires')),
                ('csipcfgtimerconnect', YLeaf(YType.int32, 'cSipCfgTimerConnect')),
                ('csipcfgtimerdisconnect', YLeaf(YType.int32, 'cSipCfgTimerDisconnect')),
                ('csipcfgtimerprack', YLeaf(YType.int32, 'cSipCfgTimerPrack')),
                ('csipcfgtimercomet', YLeaf(YType.int32, 'cSipCfgTimerComet')),
                ('csipcfgtimerreliablersp', YLeaf(YType.int32, 'cSipCfgTimerReliableRsp')),
                ('csipcfgtimernotify', YLeaf(YType.int32, 'cSipCfgTimerNotify')),
                ('csipcfgtimerrefer', YLeaf(YType.int32, 'cSipCfgTimerRefer')),
                ('csipcfgtimersessiontimer', YLeaf(YType.int32, 'cSipCfgTimerSessionTimer')),
                ('csipcfgtimerhold', YLeaf(YType.int32, 'cSipCfgTimerHold')),
                ('csipcfgtimerinfo', YLeaf(YType.int32, 'cSipCfgTimerInfo')),
                ('csipcfgtimerconnectionaging', YLeaf(YType.int32, 'cSipCfgTimerConnectionAging')),
                ('csipcfgtimerbufferinvite', YLeaf(YType.int32, 'cSipCfgTimerBufferInvite')),
            ])
            self.csipcfgtimertrying = None
            self.csipcfgtimerexpires = None
            self.csipcfgtimerconnect = None
            self.csipcfgtimerdisconnect = None
            self.csipcfgtimerprack = None
            self.csipcfgtimercomet = None
            self.csipcfgtimerreliablersp = None
            self.csipcfgtimernotify = None
            self.csipcfgtimerrefer = None
            self.csipcfgtimersessiontimer = None
            self.csipcfgtimerhold = None
            self.csipcfgtimerinfo = None
            self.csipcfgtimerconnectionaging = None
            self.csipcfgtimerbufferinvite = None
            self._segment_path = lambda: "cSipCfgTimer"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgtimer, ['csipcfgtimertrying', 'csipcfgtimerexpires', 'csipcfgtimerconnect', 'csipcfgtimerdisconnect', 'csipcfgtimerprack', 'csipcfgtimercomet', 'csipcfgtimerreliablersp', 'csipcfgtimernotify', 'csipcfgtimerrefer', 'csipcfgtimersessiontimer', 'csipcfgtimerhold', 'csipcfgtimerinfo', 'csipcfgtimerconnectionaging', 'csipcfgtimerbufferinvite'], name, value)


    class Csipcfgretry(Entity):
        """
        
        
        .. attribute:: csipcfgretryinvite
        
        	This object specifies the number of times a user agent  will retry sending a INVITE request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrybye
        
        	This object specifies the number of times a user agent  will retry sending a BYE request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycancel
        
        	This object specifies the number of times a user agent  will retry sending a CANCEL request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryregister
        
        	This object specifies the number of times a user agent  will retry sending a REGISTER request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryresponse
        
        	This object specifies the number of times a user agent  will retry sending a Response and expecting a ACK
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryprack
        
        	This object specifies the number of times a user agent  will retry sending a PRACK (PRovisional ACKnowledgement)
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycomet
        
        	This object specifies the number of times a user agent  will retry sending a COMET (COndition MET)
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryreliablersp
        
        	This object specifies the number of times a user agent  will retry sending a reliable response
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrynotify
        
        	This object specifies the number of times a user agent  will retry sending a Notify request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryrefer
        
        	This object specifies the number of times a user agent  will retry sending a Refer request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryinfo
        
        	This object specifies the number of times a user agent will retry sending a Info request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrysubscribe
        
        	This object specifies the number of times a user agent will retry sending a Subscribe request
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgretry, self).__init__()

            self.yang_name = "cSipCfgRetry"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgretryinvite', YLeaf(YType.int32, 'cSipCfgRetryInvite')),
                ('csipcfgretrybye', YLeaf(YType.int32, 'cSipCfgRetryBye')),
                ('csipcfgretrycancel', YLeaf(YType.int32, 'cSipCfgRetryCancel')),
                ('csipcfgretryregister', YLeaf(YType.int32, 'cSipCfgRetryRegister')),
                ('csipcfgretryresponse', YLeaf(YType.int32, 'cSipCfgRetryResponse')),
                ('csipcfgretryprack', YLeaf(YType.int32, 'cSipCfgRetryPrack')),
                ('csipcfgretrycomet', YLeaf(YType.int32, 'cSipCfgRetryComet')),
                ('csipcfgretryreliablersp', YLeaf(YType.int32, 'cSipCfgRetryReliableRsp')),
                ('csipcfgretrynotify', YLeaf(YType.int32, 'cSipCfgRetryNotify')),
                ('csipcfgretryrefer', YLeaf(YType.int32, 'cSipCfgRetryRefer')),
                ('csipcfgretryinfo', YLeaf(YType.int32, 'cSipCfgRetryInfo')),
                ('csipcfgretrysubscribe', YLeaf(YType.int32, 'cSipCfgRetrySubscribe')),
            ])
            self.csipcfgretryinvite = None
            self.csipcfgretrybye = None
            self.csipcfgretrycancel = None
            self.csipcfgretryregister = None
            self.csipcfgretryresponse = None
            self.csipcfgretryprack = None
            self.csipcfgretrycomet = None
            self.csipcfgretryreliablersp = None
            self.csipcfgretrynotify = None
            self.csipcfgretryrefer = None
            self.csipcfgretryinfo = None
            self.csipcfgretrysubscribe = None
            self._segment_path = lambda: "cSipCfgRetry"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgretry, ['csipcfgretryinvite', 'csipcfgretrybye', 'csipcfgretrycancel', 'csipcfgretryregister', 'csipcfgretryresponse', 'csipcfgretryprack', 'csipcfgretrycomet', 'csipcfgretryreliablersp', 'csipcfgretrynotify', 'csipcfgretryrefer', 'csipcfgretryinfo', 'csipcfgretrysubscribe'], name, value)


    class Csipcfgpeer(Entity):
        """
        
        
        .. attribute:: csipcfgoutsessiontransport
        
        	This object specifies the session transport  protocol that will be used for outbound SIP  messages.  This configuration is applicable to all dial\-peers in the system having  cSipCfgPeerOutSessionTransport set to 'system'
        	**type**\:  :py:class:`Csipcfgoutsessiontransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeer.Csipcfgoutsessiontransport>`
        
        .. attribute:: csipcfgreliable1xxrspstr
        
        	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgReliable1xxRspHdr
        	**type**\: str
        
        .. attribute:: csipcfgreliable1xxrsphdr
        
        	This object specifies behavior with respect to Supported or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs
        	**type**\:  :py:class:`Csipcfgreliable1Xxrsphdr <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeer.Csipcfgreliable1Xxrsphdr>`
        
        .. attribute:: csipcfgurltype
        
        	This object specifies the URL type sent in outbound INVITES generated by this device
        	**type**\:  :py:class:`Csipcfgurltype <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeer.Csipcfgurltype>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgpeer, self).__init__()

            self.yang_name = "cSipCfgPeer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgoutsessiontransport', YLeaf(YType.enumeration, 'cSipCfgOutSessionTransport')),
                ('csipcfgreliable1xxrspstr', YLeaf(YType.str, 'cSipCfgReliable1xxRspStr')),
                ('csipcfgreliable1xxrsphdr', YLeaf(YType.enumeration, 'cSipCfgReliable1xxRspHdr')),
                ('csipcfgurltype', YLeaf(YType.enumeration, 'cSipCfgUrlType')),
            ])
            self.csipcfgoutsessiontransport = None
            self.csipcfgreliable1xxrspstr = None
            self.csipcfgreliable1xxrsphdr = None
            self.csipcfgurltype = None
            self._segment_path = lambda: "cSipCfgPeer"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeer, ['csipcfgoutsessiontransport', 'csipcfgreliable1xxrspstr', 'csipcfgreliable1xxrsphdr', 'csipcfgurltype'], name, value)

        class Csipcfgoutsessiontransport(Enum):
            """
            Csipcfgoutsessiontransport (Enum Class)

            This object specifies the session transport 

            protocol that will be used for outbound SIP 

            messages.  This configuration is applicable

            to all dial\-peers in the system having 

            cSipCfgPeerOutSessionTransport set to 'system'.

            .. data:: udp = 1

            .. data:: tcp = 2

            """

            udp = Enum.YLeaf(1, "udp")

            tcp = Enum.YLeaf(2, "tcp")


        class Csipcfgreliable1Xxrsphdr(Enum):
            """
            Csipcfgreliable1Xxrsphdr (Enum Class)

            This object specifies behavior with respect to

            Supported or Require headers in SIP messages sent

            and received via this dial\-peer.

            If the originating gateway is configured for 'require',

            the Require header is added to the outgoing INVITEs

            with the value of cSipCfgReliable1xxStr.  This

            requires the use of reliable provisional responses by

            the terminating gateway.  Sessions will be torn down

            if this use cannot be supported by that gateway.

            If the originating gateway is configured for 'supported',

            the Supported header is added to the outgoing INVITEs

            with the value of cSipCfgReliable1xxStr.  This 

            requires that an attempt to use reliable provisional

            responses be made, but sessions can continue without them.

            If the originating gateway is configured for 'disabled',

            the value of cSipCfgReliable1xxStr will NOT be added to

            either the Require or Supported headers of outgoing INVITEs.

            .. data:: supported = 1

            .. data:: require = 2

            .. data:: disabled = 3

            """

            supported = Enum.YLeaf(1, "supported")

            require = Enum.YLeaf(2, "require")

            disabled = Enum.YLeaf(3, "disabled")


        class Csipcfgurltype(Enum):
            """
            Csipcfgurltype (Enum Class)

            This object specifies the URL type sent in outbound

            INVITES generated by this device.

            .. data:: sip = 1

            .. data:: tel = 2

            """

            sip = Enum.YLeaf(1, "sip")

            tel = Enum.YLeaf(2, "tel")



    class Csipcfgaaa(Entity):
        """
        
        
        .. attribute:: csipcfgaaausername
        
        	This object specifies the source of the information used to populate the username attribute of AAA billing records
        	**type**\:  :py:class:`Csipcfgaaausername <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgaaa.Csipcfgaaausername>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgaaa, self).__init__()

            self.yang_name = "cSipCfgAaa"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgaaausername', YLeaf(YType.enumeration, 'cSipCfgAaaUsername')),
            ])
            self.csipcfgaaausername = None
            self._segment_path = lambda: "cSipCfgAaa"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgaaa, ['csipcfgaaausername'], name, value)

        class Csipcfgaaausername(Enum):
            """
            Csipcfgaaausername (Enum Class)

            This object specifies the source of the information used to

            populate the username attribute of AAA billing records.

            .. data:: callingNumber = 1

            .. data:: proxyAuth = 2

            """

            callingNumber = Enum.YLeaf(1, "callingNumber")

            proxyAuth = Enum.YLeaf(2, "proxyAuth")



    class Csipcfgvoiceservicevoip(Entity):
        """
        
        
        .. attribute:: csipcfgheaderpassingenabled
        
        	This object specifies if support for passing SIP headers from Invite, Subscribe, Notify Request to the application is enabled.  If 'true', the headers received in a message will be passed to the application.  If 'false', the headers received in a message will not be passed to the application
        	**type**\: bool
        
        .. attribute:: csipcfgmaxsubscriptionaccept
        
        	This object specifies the maximum number of concurrent SIP subscriptions a SIP Gateway can accept
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipcfgmaxsubscriptionoriginate
        
        	This object specifies the maximum number of concurrent SIP subscriptions that a SIP Gateway can originate. Default is Max Dialpeers on platform. Maximum is 2\*Max Dialpeers on Platform
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipcfgswitchtransportenabled
        
        	This object specifies if the functionality of switching between transports from udp to tcp if the message size of a Request is greater than 1300 bytes is enabled or not.  This configuration is at the global level, and will only be  considered if there exists no voip dial\-peer
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgvoiceservicevoip, self).__init__()

            self.yang_name = "cSipCfgVoiceServiceVoip"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipcfgheaderpassingenabled', YLeaf(YType.boolean, 'cSipCfgHeaderPassingEnabled')),
                ('csipcfgmaxsubscriptionaccept', YLeaf(YType.uint32, 'cSipCfgMaxSubscriptionAccept')),
                ('csipcfgmaxsubscriptionoriginate', YLeaf(YType.uint32, 'cSipCfgMaxSubscriptionOriginate')),
                ('csipcfgswitchtransportenabled', YLeaf(YType.boolean, 'cSipCfgSwitchTransportEnabled')),
            ])
            self.csipcfgheaderpassingenabled = None
            self.csipcfgmaxsubscriptionaccept = None
            self.csipcfgmaxsubscriptionoriginate = None
            self.csipcfgswitchtransportenabled = None
            self._segment_path = lambda: "cSipCfgVoiceServiceVoip"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgvoiceservicevoip, ['csipcfgheaderpassingenabled', 'csipcfgmaxsubscriptionaccept', 'csipcfgmaxsubscriptionoriginate', 'csipcfgswitchtransportenabled'], name, value)


    class Csipstatsinfo(Entity):
        """
        
        
        .. attribute:: csipstatsinfotryingins
        
        	This object reflects the total number of Trying (100) responses received by the user agent since system startup.   Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Inbound Trying responses indicate that outbound INVITE request  sent out by this system have been received and are processed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfotryingouts
        
        	This object reflects the total number of Trying (100) responses sent by the user agent since system startup. Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Outbound Trying responses indicate this system is successfully  receiving INVITE requests and processing them on  behalf of the system initiating the INVITE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinforingingins
        
        	This object reflects the total number of Ringing (180) responses received by the user agent since system startup. A inbound Ringing response indicates that the UAS processing a INVITE initiated by this system has  found a possible location where the desired end user  has registered recently and is trying to alert the user
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinforingingouts
        
        	This object reflects the total number of Ringing (180) responses sent by the user agent since system startup. A outbound Ringing response indicates that this system has processed an INVITE for a particular end user and found a possible location where that user has registered recently.  The system is trying to alert the end user and is conveying that status to the system that originated the INVITE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoforwardedins
        
        	This object reflects the total number of Call Is Being Forwarded (181) responses received by the user agent since system startup. A proxy server may use a Forwarded status code to indicate that the call is being forwarded to a different set of destinations.  Inbound Forwarded responses indicate  to this system that forwarding actions are taking place  with regard to calls initiated by this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoforwardedouts
        
        	This object reflects the total number of Call Is Being Forwarded (181) responses sent by the user agent since system startup. A proxy server may use a Forwarded status code to indicate that the call is being forwarded to a different set of destinations.  Outbound Forwarded responses indicate this system is taking some forwarding action for calls and conveying that status to the system that initiated the calls
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoqueuedins
        
        	This object reflects the total number of Queued (182) responses received by the user agent since system startup. Inbound Queued responses indicate that the users this system is attempting to call are temporarily unavailable but the SIP agents operating on behalf of those users wish to queue the calls rather than reject them.  When the called parties become available, this system can expect to receive the appropriate final status response.  The Reason\-Phrase from the Queued response messages Status\-Line may give further details about the status of the call.  Multiple  Queued responses to update this system about the status of the queued call my be received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoqueuedouts
        
        	This object reflects the total number of Queued (182) responses sent by the user agent since system startup. Outbound Queued responses indicate this system has determined that the called party is temporarily unavailable but the call is not rejected.  Rather  the call is queued until the called party becomes available.  Queued responses messages are sent to the system originating the call request to convey the current status of a queued call
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfosessionprogins
        
        	This object reflects the total number of Session Progress (183) responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfosessionprogouts
        
        	This object reflects the total number of Session Progress (183) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsinfo, self).__init__()

            self.yang_name = "cSipStatsInfo"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsinfotryingins', YLeaf(YType.uint32, 'cSipStatsInfoTryingIns')),
                ('csipstatsinfotryingouts', YLeaf(YType.uint32, 'cSipStatsInfoTryingOuts')),
                ('csipstatsinforingingins', YLeaf(YType.uint32, 'cSipStatsInfoRingingIns')),
                ('csipstatsinforingingouts', YLeaf(YType.uint32, 'cSipStatsInfoRingingOuts')),
                ('csipstatsinfoforwardedins', YLeaf(YType.uint32, 'cSipStatsInfoForwardedIns')),
                ('csipstatsinfoforwardedouts', YLeaf(YType.uint32, 'cSipStatsInfoForwardedOuts')),
                ('csipstatsinfoqueuedins', YLeaf(YType.uint32, 'cSipStatsInfoQueuedIns')),
                ('csipstatsinfoqueuedouts', YLeaf(YType.uint32, 'cSipStatsInfoQueuedOuts')),
                ('csipstatsinfosessionprogins', YLeaf(YType.uint32, 'cSipStatsInfoSessionProgIns')),
                ('csipstatsinfosessionprogouts', YLeaf(YType.uint32, 'cSipStatsInfoSessionProgOuts')),
            ])
            self.csipstatsinfotryingins = None
            self.csipstatsinfotryingouts = None
            self.csipstatsinforingingins = None
            self.csipstatsinforingingouts = None
            self.csipstatsinfoforwardedins = None
            self.csipstatsinfoforwardedouts = None
            self.csipstatsinfoqueuedins = None
            self.csipstatsinfoqueuedouts = None
            self.csipstatsinfosessionprogins = None
            self.csipstatsinfosessionprogouts = None
            self._segment_path = lambda: "cSipStatsInfo"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsinfo, ['csipstatsinfotryingins', 'csipstatsinfotryingouts', 'csipstatsinforingingins', 'csipstatsinforingingouts', 'csipstatsinfoforwardedins', 'csipstatsinfoforwardedouts', 'csipstatsinfoqueuedins', 'csipstatsinfoqueuedouts', 'csipstatsinfosessionprogins', 'csipstatsinfosessionprogouts'], name, value)


    class Csipstatssuccess(Entity):
        """
        
        
        .. attribute:: csipstatssuccessokins
        
        	This object reflects the total number of Ok (200) responses received by the user agent since system startup. The meaning of inbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: csipstatssuccessokouts
        
        	This object reflects the total number of Ok (200) responses sent by the user agent since system startup. The meaning of outbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: csipstatssuccessacceptedins
        
        	This object reflects the total number of Accepted (202) responses received by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessacceptedouts
        
        	This object reflects the total number of Accepted (202) responses sent by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatssuccess, self).__init__()

            self.yang_name = "cSipStatsSuccess"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatssuccessokins', YLeaf(YType.uint32, 'cSipStatsSuccessOkIns')),
                ('csipstatssuccessokouts', YLeaf(YType.uint32, 'cSipStatsSuccessOkOuts')),
                ('csipstatssuccessacceptedins', YLeaf(YType.uint32, 'cSipStatsSuccessAcceptedIns')),
                ('csipstatssuccessacceptedouts', YLeaf(YType.uint32, 'cSipStatsSuccessAcceptedOuts')),
            ])
            self.csipstatssuccessokins = None
            self.csipstatssuccessokouts = None
            self.csipstatssuccessacceptedins = None
            self.csipstatssuccessacceptedouts = None
            self._segment_path = lambda: "cSipStatsSuccess"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatssuccess, ['csipstatssuccessokins', 'csipstatssuccessokouts', 'csipstatssuccessacceptedins', 'csipstatssuccessacceptedouts'], name, value)


    class Csipstatsredirect(Entity):
        """
        
        
        .. attribute:: csipstatsredirmultiplechoices
        
        	This object reflects the total number of Multiple Choices (300) responses received by the user agent since system startup. Multiple Choices responses indicate that the called party can be reached at several different locations and the server cannot or prefers not to proxy the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedperms
        
        	This object reflects the total number of Moved  Permanently (301) responses received by the user agent since system startup. Moved Permanently responses indicate that the called party  can no longer be found at the address offered in the request  and the requesting UAC should retry at the new address given  by the Contact header field of the response
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtemps
        
        	This object reflects the total number of Moved  Temporarily (302) responses received by the user agent since system startup. Moved Temporarily responses indicate the UAC should retry the request directed at the new address(es) given by the Contact header field of the response. The duration of this redirection can be indicated through the Expires header.  If no explicit expiration time is given, the new address(es) are only valid for this call
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: csipstatsredirseeothers
        
        	This object reflects the total number of See Other  (303) responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsrediruseproxys
        
        	This object reflects the total number of Use Proxy  (305) responses received by the user agent since system startup. See Other responses indicate that requested resources must be accessed through the proxy given by the  Contact header field of the response.  The recipient of this response is expected to repeat this single request via the proxy
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsrediraltservices
        
        	This object reflects the total number of Alternative Service (380) responses received by the user agent since system startup. Alternative Service responses indicate that the call was not successful, but alternative services are possible.  Those alternative services are described in the message body of the response
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtempsins
        
        	This object reflects the total number of Moved Temporarily (302) responses received by the user agent since system startup.  Moved Temporarily responses indicate the UAC should retry the request directed at the new address(es)  given by the Contact header field of the response. The duration of this redirection can be indicated through the Expires header.  If no explicit expiration time is given, the new address(es) are only valid for this call
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtempsouts
        
        	This object reflects the total number of Moved Temporarily (302) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsredirect, self).__init__()

            self.yang_name = "cSipStatsRedirect"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsredirmultiplechoices', YLeaf(YType.uint32, 'cSipStatsRedirMultipleChoices')),
                ('csipstatsredirmovedperms', YLeaf(YType.uint32, 'cSipStatsRedirMovedPerms')),
                ('csipstatsredirmovedtemps', YLeaf(YType.uint32, 'cSipStatsRedirMovedTemps')),
                ('csipstatsredirseeothers', YLeaf(YType.uint32, 'cSipStatsRedirSeeOthers')),
                ('csipstatsrediruseproxys', YLeaf(YType.uint32, 'cSipStatsRedirUseProxys')),
                ('csipstatsrediraltservices', YLeaf(YType.uint32, 'cSipStatsRedirAltServices')),
                ('csipstatsredirmovedtempsins', YLeaf(YType.uint32, 'cSipStatsRedirMovedTempsIns')),
                ('csipstatsredirmovedtempsouts', YLeaf(YType.uint32, 'cSipStatsRedirMovedTempsOuts')),
            ])
            self.csipstatsredirmultiplechoices = None
            self.csipstatsredirmovedperms = None
            self.csipstatsredirmovedtemps = None
            self.csipstatsredirseeothers = None
            self.csipstatsrediruseproxys = None
            self.csipstatsrediraltservices = None
            self.csipstatsredirmovedtempsins = None
            self.csipstatsredirmovedtempsouts = None
            self._segment_path = lambda: "cSipStatsRedirect"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsredirect, ['csipstatsredirmultiplechoices', 'csipstatsredirmovedperms', 'csipstatsredirmovedtemps', 'csipstatsredirseeothers', 'csipstatsrediruseproxys', 'csipstatsrediraltservices', 'csipstatsredirmovedtempsins', 'csipstatsredirmovedtempsouts'], name, value)


    class Csipstatserrclient(Entity):
        """
        
        
        .. attribute:: csipstatsclientbadrequestins
        
        	This object reflects the total number of Bad Request (400)  responses received by the user agent since system startup. Inbound Bad Request responses indicate that requests issued  by this system could not be understood due to malformed  syntax
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadrequestouts
        
        	This object reflects the total number of Bad Request (400)  responses sent by the user agent since system startup. Outbound Bad Request responses indicate that requests  received by this system could not be understood due to  malformed syntax
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientunauthorizedins
        
        	This object reflects the total number of Unauthorized (401)  responses received by the user agent since system startup.   Inbound Unauthorized responses indicate that requests issued  by this system require user authentication
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientunauthorizedouts
        
        	This object reflects the total number of Unauthorized (401)  responses sent by the user agent since system startup. Outbound Unauthorized responses indicate that requests  received by this system require user authentication
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientpaymentreqdins
        
        	This object reflects the total number of Payment Required  (402) responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientpaymentreqdouts
        
        	This object reflects the total number of Payment Required  (402) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientforbiddenins
        
        	This object reflects the total number of Forbidden (403)  responses received by the user agent since system startup. Inbound Forbidden responses indicate that requests issued by this system are understood by the server but the server refuses to fulfill the request.  Authorization will not help and the requests should not be repeated
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientforbiddenouts
        
        	This object reflects the total number of Forbidden (403)  responses sent by the user agent since system startup. Outbound Forbidden responses indicate that requests received by this system are understood but this system is refusing to fulfill the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotfoundins
        
        	This object reflects the total number of Not Found (404)  responses received by the user agent since system startup. Inbound Not Found responses indicate that the called party  does not exist at the domain specified in the Request\-URI  or the domain is not handled by the recipient of the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotfoundouts
        
        	This object reflects the total number of Not Found (404)  responses sent by the user agent since system startup. Outbound Not Found responses indicate that this system knows that the called party does not exist at the domain specified in the Request\-URI or the domain is not handled by this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientmethnotallowedins
        
        	This object reflects the total number of Method Not Allowed  (405) received responses by the user agent. Inbound Method Not Allowed responses indicate that requests  issued by this system have specified a SIP method in the  Request\-Line that is not allowed for the address identified  by the Request\-URI
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientmethnotallowedouts
        
        	This object reflects the total number of Method Not Allowed  (405) received sent by the user agent since system startup. Outbound Method Not Allowed responses indicate that requests  received by this system have SIP methods specified in the  Request\-Line that are not allowed for the address identified  by the Request\-URI
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotacceptableins
        
        	This object reflects the total number of Not Acceptable  (406) responses received by the user agent since system startup. Inbound Not Acceptable responses indicate the resources  identified by requests issued by this system cannot generate  responses with content characteristics acceptable to this  system according to the accept headers sent in the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotacceptableouts
        
        	This object reflects the total number of Not Acceptable (406)  responses sent by the user agent since system startup. Outbound Not Acceptable responses indicate that the resources identified by requests received by this system cannot generate responses with content characteristics acceptable to the  system sending the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientproxyauthreqdins
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses received by the user agent since system startup. Inbound Proxy Authentication Required responses indicate that  this system must authenticate itself with the proxy before  gaining access to the requested resource
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientproxyauthreqdouts
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses sent by the user agent since system startup. Outbound Proxy Authentication Required responses indicate that the systems issuing requests being processed by this system  must authenticate themselves with this system before gaining  access to requested resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtimeoutins
        
        	This object reflects the total number of Request Timeout  (408) responses received by the user agent since system startup. Inbound Request Timeout responses indicate that requests  issued by this system are not being processed by the server  within the time indicated in the Expires header of the  request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtimeoutouts
        
        	This object reflects the total number of Request Timeout  (408) responses sent by the user agent since system startup. Outbound Request Timeout responses indicate that this  system is not able to produce an appropriate response within  the time indicated in the Expires header of the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientconflictins
        
        	This object reflects the total number of Conflict (409)  responses received by the user agent since system startup. Inbound Conflict responses indicate that requests issued by this system could not be completed due to a conflict with the current state of a requested resource
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientconflictouts
        
        	This object reflects the total number of Conflict (409)  responses sent by the user agent since system startup. Outbound Conflict responses indicate that requests received by this system could not be completed due to a conflict with the current state of a requested resource
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientgoneins
        
        	This object reflects the total number of Gone (410)  responses received by the user agent since system startup. Inbound Gone responses indicate that resources requested by this system are no longer available at the recipient server and no forwarding address is known
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientgoneouts
        
        	This object reflects the total number of Gone (410)  responses sent by the user agent since system startup. Outbound Gone responses indicate that the requested resources are no longer available at this system and no forwarding address is known
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientlengthrequiredins
        
        	This object reflects the total number of Length Required  (411) responses received by the user agent since system startup. Inbound Length Required responses indicate that requests  issued by this system are being refused by servers because  of no defined Content\-Length header field
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsclientlengthrequiredouts
        
        	This object reflects the total number of Length Required  (411) responses sent by the user agent since system startup. Outbound Length Required responses indicate that requests  received by this system are being refused because of no  defined Content\-Length header field
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsclientreqenttoolargeins
        
        	This object reflects the total number of Request Entity Too  Large (413) responses received by the user agent since system startup. Inbound Request Entity Too Large responses indicate that  requests issued by this system are being refused because  the request is larger than the server is willing or able to  process
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqenttoolargeouts
        
        	This object reflects the total number of Request Entity Too  Large (413) responses sent by the user agent since system startup. Outbound Request Entity Too Large responses indicate that  requests received by this system are larger than this system  is willing or able to process
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientrequritoolargeins
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses received by the user agent since system startup. Inbound Request\-URI Too Large responses indicate that  requests issued by this system are being refused because the  Request\-URI is longer than the server is willing or able to  interpret
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientrequritoolargeouts
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses sent by the user agent since system startup. Outbound Request\-URI Too Large responses indicate that  Request\-URIs received by this system are longer than this  system is willing or able to interpret
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnosupmediatypeins
        
        	This object reflects the total number of Unsupported Media  Type (415) responses received by the user agent since system startup. Inbound Unsupported Media Type responses indicate that  requests issued by this system are being refused because the  message body of the request is in a format not supported by  the requested resource for the requested method
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnosupmediatypeouts
        
        	This object reflects the total number of Unsupported Media  Type (415) responses sent by the user agent since system startup. Outbound Unsupported Media Type responses indicate that the  body of requests received by this system are in a format not  supported by the requested resource for the requested method
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadextensionins
        
        	This object reflects the total number of Bad Extension (420)  responses received by the user agent since system startup. Inbound Bad Extension responses indicate that the recipient  did not understand the protocol extension specified in a  Require header field
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadextensionouts
        
        	This object reflects the total number of Bad Extension (420)  responses sent by the user agent since system startup. Outbound Bad Extension responses indicate that this system did not understand the protocol extension specified in a Require header field of requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttempnotavailins
        
        	This object reflects the total number of Temporarily Not  Available (480) responses received by the user agent since system startup. Inbound Temporarily Not Available responses indicate that  the called party is currently unavailable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttempnotavailouts
        
        	This object reflects the total number of Temporarily Not  Available (480) responses sent by the user agent since system startup. Outbound Temporarily Not Available responses indicate that  the called party's end system was contacted successfully but  the called party is currently unavailable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientcalllegnoexistins
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses received by the user agent since system startup. Inbound Call Leg/Transaction Does Not Exist responses indicate that either BYE or CANCEL requests issued by this system were  received by a server and not matching call leg or transaction  existed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientcalllegnoexistouts
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses sent by the user agent since system startup. Outbound Call Leg/Transaction Does Not Exist responses  indicate that BYE or CANCEL requests have been received by  this system and not call leg or transaction matching that  request exists
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientloopdetectedins
        
        	This object reflects the total number of Loop Detected (482)  responses received by the user agent since system startup. Inbound Loop Detected responses indicate that requests issued by this system were received at servers and the server found  itself in the Via path more than once
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientloopdetectedouts
        
        	This object reflects the total number of Loop Detected (482)  responses sent by the user agent since system startup. Outbound Loop Detected responses indicate that requests  received by this system contain a Via path with this system  appearing more than once
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttoomanyhopsins
        
        	This object reflects the total number of Too Many Hops (483)  responses received by the user agent since system startup. Inbound Too Many Hops responses indicate that requests issued by this system contain more Via entries (hops) than allowed by the Max\-Forwards header field of the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttoomanyhopsouts
        
        	This object reflects the total number of Too Many Hops (483)  responses sent by the user agent since system startup. Outbound Too Many Hops responses indicate that requests received by this system contain more Via entries (hops) than are allowed by the Max\-Forwards header field of the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientaddrincompleteins
        
        	This object reflects the total number of Address Incomplete  (484) responses received by the user agent since system startup. Inbound Address Incomplete responses indicate that requests  issued by this system had To addresses or Request\-URIs that  were incomplete
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientaddrincompleteouts
        
        	This object reflects the total number of Address Incomplete  (484) responses sent by the user agent since system startup. Outbound Address Incomplete responses indicate that requests  received by this system had To addresses or Request\-URIs that  were incomplete
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientambiguousins
        
        	This object reflects the total number of Ambiguous (485)  responses received by the user agent since system startup. Inbound Ambiguous responses indicate that requests issued by this system provided ambiguous address information
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientambiguousouts
        
        	This object reflects the total number of Ambiguous (485)  responses sent by the user agent since system startup. Outbound Ambiguous responses indicate that requests received by this system contained ambiguous address information
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbusyhereins
        
        	This object reflects the total number of Busy Here (486)  responses received by the user agent since system startup. Inbound Busy Here responses indicate that the called party is currently not willing or not able to take additional calls
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbusyhereouts
        
        	This object reflects the total number of Busy Here (486)  responses sent by the user agent since system startup. Outbound Busy Here responses indicate that the called party's end system was contacted successfully but the called party is currently not willing or able to take  additional calls
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtermins
        
        	This object reflects the total number of Request Terminated  (487) responses received by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtermouts
        
        	This object reflects the total number of Request Terminated  (487) responses sent by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnoaccepthereins
        
        	This object reflects the total number of Not Acceptable Here (488) responses received by the user agent since system startup. The response has the same meaning as 606 (Not Acceptable),  but only applies to the specific entity addressed by the  Request\-URI and the request may succeed elsewhere
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnoaccepthereouts
        
        	This object reflects the total number of Not Acceptable Here (488) responses sent by the user agent since system startup. The response has the same meaning as 606 (Not Acceptable),  but only applies to the specific entity addressed by the  Request\-URI and the request may succeed elsewhere
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadeventins
        
        	This object reflects the total number of BadEvent (489)  responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadeventouts
        
        	This object reflects the total number of BadEvent (489)  responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientsttoosmallins
        
        	This object reflects the total number of SessionTimerTooSmall (422) responses received by the user agent since system  startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientsttoosmallouts
        
        	This object reflects the total number of SessionTimerTooSmall (422) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqpendingins
        
        	This object reflects the total number of RequestPending (491) responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqpendingouts
        
        	This object reflects the total number of RequestPending (491) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatserrclient, self).__init__()

            self.yang_name = "cSipStatsErrClient"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsclientbadrequestins', YLeaf(YType.uint32, 'cSipStatsClientBadRequestIns')),
                ('csipstatsclientbadrequestouts', YLeaf(YType.uint32, 'cSipStatsClientBadRequestOuts')),
                ('csipstatsclientunauthorizedins', YLeaf(YType.uint32, 'cSipStatsClientUnauthorizedIns')),
                ('csipstatsclientunauthorizedouts', YLeaf(YType.uint32, 'cSipStatsClientUnauthorizedOuts')),
                ('csipstatsclientpaymentreqdins', YLeaf(YType.uint32, 'cSipStatsClientPaymentReqdIns')),
                ('csipstatsclientpaymentreqdouts', YLeaf(YType.uint32, 'cSipStatsClientPaymentReqdOuts')),
                ('csipstatsclientforbiddenins', YLeaf(YType.uint32, 'cSipStatsClientForbiddenIns')),
                ('csipstatsclientforbiddenouts', YLeaf(YType.uint32, 'cSipStatsClientForbiddenOuts')),
                ('csipstatsclientnotfoundins', YLeaf(YType.uint32, 'cSipStatsClientNotFoundIns')),
                ('csipstatsclientnotfoundouts', YLeaf(YType.uint32, 'cSipStatsClientNotFoundOuts')),
                ('csipstatsclientmethnotallowedins', YLeaf(YType.uint32, 'cSipStatsClientMethNotAllowedIns')),
                ('csipstatsclientmethnotallowedouts', YLeaf(YType.uint32, 'cSipStatsClientMethNotAllowedOuts')),
                ('csipstatsclientnotacceptableins', YLeaf(YType.uint32, 'cSipStatsClientNotAcceptableIns')),
                ('csipstatsclientnotacceptableouts', YLeaf(YType.uint32, 'cSipStatsClientNotAcceptableOuts')),
                ('csipstatsclientproxyauthreqdins', YLeaf(YType.uint32, 'cSipStatsClientProxyAuthReqdIns')),
                ('csipstatsclientproxyauthreqdouts', YLeaf(YType.uint32, 'cSipStatsClientProxyAuthReqdOuts')),
                ('csipstatsclientreqtimeoutins', YLeaf(YType.uint32, 'cSipStatsClientReqTimeoutIns')),
                ('csipstatsclientreqtimeoutouts', YLeaf(YType.uint32, 'cSipStatsClientReqTimeoutOuts')),
                ('csipstatsclientconflictins', YLeaf(YType.uint32, 'cSipStatsClientConflictIns')),
                ('csipstatsclientconflictouts', YLeaf(YType.uint32, 'cSipStatsClientConflictOuts')),
                ('csipstatsclientgoneins', YLeaf(YType.uint32, 'cSipStatsClientGoneIns')),
                ('csipstatsclientgoneouts', YLeaf(YType.uint32, 'cSipStatsClientGoneOuts')),
                ('csipstatsclientlengthrequiredins', YLeaf(YType.uint32, 'cSipStatsClientLengthRequiredIns')),
                ('csipstatsclientlengthrequiredouts', YLeaf(YType.uint32, 'cSipStatsClientLengthRequiredOuts')),
                ('csipstatsclientreqenttoolargeins', YLeaf(YType.uint32, 'cSipStatsClientReqEntTooLargeIns')),
                ('csipstatsclientreqenttoolargeouts', YLeaf(YType.uint32, 'cSipStatsClientReqEntTooLargeOuts')),
                ('csipstatsclientrequritoolargeins', YLeaf(YType.uint32, 'cSipStatsClientReqURITooLargeIns')),
                ('csipstatsclientrequritoolargeouts', YLeaf(YType.uint32, 'cSipStatsClientReqURITooLargeOuts')),
                ('csipstatsclientnosupmediatypeins', YLeaf(YType.uint32, 'cSipStatsClientNoSupMediaTypeIns')),
                ('csipstatsclientnosupmediatypeouts', YLeaf(YType.uint32, 'cSipStatsClientNoSupMediaTypeOuts')),
                ('csipstatsclientbadextensionins', YLeaf(YType.uint32, 'cSipStatsClientBadExtensionIns')),
                ('csipstatsclientbadextensionouts', YLeaf(YType.uint32, 'cSipStatsClientBadExtensionOuts')),
                ('csipstatsclienttempnotavailins', YLeaf(YType.uint32, 'cSipStatsClientTempNotAvailIns')),
                ('csipstatsclienttempnotavailouts', YLeaf(YType.uint32, 'cSipStatsClientTempNotAvailOuts')),
                ('csipstatsclientcalllegnoexistins', YLeaf(YType.uint32, 'cSipStatsClientCallLegNoExistIns')),
                ('csipstatsclientcalllegnoexistouts', YLeaf(YType.uint32, 'cSipStatsClientCallLegNoExistOuts')),
                ('csipstatsclientloopdetectedins', YLeaf(YType.uint32, 'cSipStatsClientLoopDetectedIns')),
                ('csipstatsclientloopdetectedouts', YLeaf(YType.uint32, 'cSipStatsClientLoopDetectedOuts')),
                ('csipstatsclienttoomanyhopsins', YLeaf(YType.uint32, 'cSipStatsClientTooManyHopsIns')),
                ('csipstatsclienttoomanyhopsouts', YLeaf(YType.uint32, 'cSipStatsClientTooManyHopsOuts')),
                ('csipstatsclientaddrincompleteins', YLeaf(YType.uint32, 'cSipStatsClientAddrIncompleteIns')),
                ('csipstatsclientaddrincompleteouts', YLeaf(YType.uint32, 'cSipStatsClientAddrIncompleteOuts')),
                ('csipstatsclientambiguousins', YLeaf(YType.uint32, 'cSipStatsClientAmbiguousIns')),
                ('csipstatsclientambiguousouts', YLeaf(YType.uint32, 'cSipStatsClientAmbiguousOuts')),
                ('csipstatsclientbusyhereins', YLeaf(YType.uint32, 'cSipStatsClientBusyHereIns')),
                ('csipstatsclientbusyhereouts', YLeaf(YType.uint32, 'cSipStatsClientBusyHereOuts')),
                ('csipstatsclientreqtermins', YLeaf(YType.uint32, 'cSipStatsClientReqTermIns')),
                ('csipstatsclientreqtermouts', YLeaf(YType.uint32, 'cSipStatsClientReqTermOuts')),
                ('csipstatsclientnoaccepthereins', YLeaf(YType.uint32, 'cSipStatsClientNoAcceptHereIns')),
                ('csipstatsclientnoaccepthereouts', YLeaf(YType.uint32, 'cSipStatsClientNoAcceptHereOuts')),
                ('csipstatsclientbadeventins', YLeaf(YType.uint32, 'cSipStatsClientBadEventIns')),
                ('csipstatsclientbadeventouts', YLeaf(YType.uint32, 'cSipStatsClientBadEventOuts')),
                ('csipstatsclientsttoosmallins', YLeaf(YType.uint32, 'cSipStatsClientSTTooSmallIns')),
                ('csipstatsclientsttoosmallouts', YLeaf(YType.uint32, 'cSipStatsClientSTTooSmallOuts')),
                ('csipstatsclientreqpendingins', YLeaf(YType.uint32, 'cSipStatsClientReqPendingIns')),
                ('csipstatsclientreqpendingouts', YLeaf(YType.uint32, 'cSipStatsClientReqPendingOuts')),
            ])
            self.csipstatsclientbadrequestins = None
            self.csipstatsclientbadrequestouts = None
            self.csipstatsclientunauthorizedins = None
            self.csipstatsclientunauthorizedouts = None
            self.csipstatsclientpaymentreqdins = None
            self.csipstatsclientpaymentreqdouts = None
            self.csipstatsclientforbiddenins = None
            self.csipstatsclientforbiddenouts = None
            self.csipstatsclientnotfoundins = None
            self.csipstatsclientnotfoundouts = None
            self.csipstatsclientmethnotallowedins = None
            self.csipstatsclientmethnotallowedouts = None
            self.csipstatsclientnotacceptableins = None
            self.csipstatsclientnotacceptableouts = None
            self.csipstatsclientproxyauthreqdins = None
            self.csipstatsclientproxyauthreqdouts = None
            self.csipstatsclientreqtimeoutins = None
            self.csipstatsclientreqtimeoutouts = None
            self.csipstatsclientconflictins = None
            self.csipstatsclientconflictouts = None
            self.csipstatsclientgoneins = None
            self.csipstatsclientgoneouts = None
            self.csipstatsclientlengthrequiredins = None
            self.csipstatsclientlengthrequiredouts = None
            self.csipstatsclientreqenttoolargeins = None
            self.csipstatsclientreqenttoolargeouts = None
            self.csipstatsclientrequritoolargeins = None
            self.csipstatsclientrequritoolargeouts = None
            self.csipstatsclientnosupmediatypeins = None
            self.csipstatsclientnosupmediatypeouts = None
            self.csipstatsclientbadextensionins = None
            self.csipstatsclientbadextensionouts = None
            self.csipstatsclienttempnotavailins = None
            self.csipstatsclienttempnotavailouts = None
            self.csipstatsclientcalllegnoexistins = None
            self.csipstatsclientcalllegnoexistouts = None
            self.csipstatsclientloopdetectedins = None
            self.csipstatsclientloopdetectedouts = None
            self.csipstatsclienttoomanyhopsins = None
            self.csipstatsclienttoomanyhopsouts = None
            self.csipstatsclientaddrincompleteins = None
            self.csipstatsclientaddrincompleteouts = None
            self.csipstatsclientambiguousins = None
            self.csipstatsclientambiguousouts = None
            self.csipstatsclientbusyhereins = None
            self.csipstatsclientbusyhereouts = None
            self.csipstatsclientreqtermins = None
            self.csipstatsclientreqtermouts = None
            self.csipstatsclientnoaccepthereins = None
            self.csipstatsclientnoaccepthereouts = None
            self.csipstatsclientbadeventins = None
            self.csipstatsclientbadeventouts = None
            self.csipstatsclientsttoosmallins = None
            self.csipstatsclientsttoosmallouts = None
            self.csipstatsclientreqpendingins = None
            self.csipstatsclientreqpendingouts = None
            self._segment_path = lambda: "cSipStatsErrClient"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatserrclient, ['csipstatsclientbadrequestins', 'csipstatsclientbadrequestouts', 'csipstatsclientunauthorizedins', 'csipstatsclientunauthorizedouts', 'csipstatsclientpaymentreqdins', 'csipstatsclientpaymentreqdouts', 'csipstatsclientforbiddenins', 'csipstatsclientforbiddenouts', 'csipstatsclientnotfoundins', 'csipstatsclientnotfoundouts', 'csipstatsclientmethnotallowedins', 'csipstatsclientmethnotallowedouts', 'csipstatsclientnotacceptableins', 'csipstatsclientnotacceptableouts', 'csipstatsclientproxyauthreqdins', 'csipstatsclientproxyauthreqdouts', 'csipstatsclientreqtimeoutins', 'csipstatsclientreqtimeoutouts', 'csipstatsclientconflictins', 'csipstatsclientconflictouts', 'csipstatsclientgoneins', 'csipstatsclientgoneouts', 'csipstatsclientlengthrequiredins', 'csipstatsclientlengthrequiredouts', 'csipstatsclientreqenttoolargeins', 'csipstatsclientreqenttoolargeouts', 'csipstatsclientrequritoolargeins', 'csipstatsclientrequritoolargeouts', 'csipstatsclientnosupmediatypeins', 'csipstatsclientnosupmediatypeouts', 'csipstatsclientbadextensionins', 'csipstatsclientbadextensionouts', 'csipstatsclienttempnotavailins', 'csipstatsclienttempnotavailouts', 'csipstatsclientcalllegnoexistins', 'csipstatsclientcalllegnoexistouts', 'csipstatsclientloopdetectedins', 'csipstatsclientloopdetectedouts', 'csipstatsclienttoomanyhopsins', 'csipstatsclienttoomanyhopsouts', 'csipstatsclientaddrincompleteins', 'csipstatsclientaddrincompleteouts', 'csipstatsclientambiguousins', 'csipstatsclientambiguousouts', 'csipstatsclientbusyhereins', 'csipstatsclientbusyhereouts', 'csipstatsclientreqtermins', 'csipstatsclientreqtermouts', 'csipstatsclientnoaccepthereins', 'csipstatsclientnoaccepthereouts', 'csipstatsclientbadeventins', 'csipstatsclientbadeventouts', 'csipstatsclientsttoosmallins', 'csipstatsclientsttoosmallouts', 'csipstatsclientreqpendingins', 'csipstatsclientreqpendingouts'], name, value)


    class Csipstatserrserver(Entity):
        """
        
        
        .. attribute:: csipstatsserverinterrorins
        
        	This object reflects the total number of Internal Server Error (500) responses received by the user agent since system startup. Inbound Internal Server Error responses indicate that servers  to which this system is sending requests have encountered  unexpected conditions that prevent them from fulfilling the  requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverinterrorouts
        
        	This object reflects the total number of Internal Server Error (500) responses sent by the user agent since system startup. Outbound Internal Server Error responses indicate that this  system has encountered unexpected conditions that prevent it  from fulfilling received requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservernotimplementedins
        
        	This object reflects the total number of Not Implemented  (501) responses received by the user agent since system startup. Inbound Not Implemented responses indicate that servers to  which this system is sending requests do not support the  functionality required to fulfill the requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservernotimplementedouts
        
        	This object reflects the total number of Not Implemented  (501) responses sent by the user agent since system startup. Outbound Not Implemented responses indicate that this system does not support the functionality required to fulfill the  requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadgatewayins
        
        	This object reflects the total number of Bad Gateway (502)  responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadgatewayouts
        
        	This object reflects the total number of Bad Gateway (502)  responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverserviceunavailins
        
        	This object reflects the total number of Service Unavailable  (503) responses received by the user agent since system startup. Inbound Service Unavailable responses indicate that the server servicing this system's request is temporarily unavailable to handle the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverserviceunavailouts
        
        	This object reflects the total number of Service Unavailable  (503) responses sent by the user agent since system startup. Outbound Service Unavailable responses indicate that this system is temporarily unable to handle received requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservergatewaytimeoutins
        
        	This object reflects the total number of Gateway Time\-out  (504) responses received by the user agent since system startup. Inbound Gateway Time\-out responses indicate that the server attempting to complete this system's request did not receive a timely response from yet another system it was accessing to complete the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservergatewaytimeoutouts
        
        	This object reflects the total number of Gateway Time\-out  (504) responses sent by the user agent since system startup. Outbound Gateway Time\-out responses indicate that this system did not receive a timely response from the system it had accessed to assist in completing a received request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadsipversionins
        
        	This object reflects the total number of SIP Version Not  Supported (505) responses received by the user agent since system startup. Inbound SIP Version Not Supported responses indicate that  the server does not support, or refuses to support, the SIP  protocol version that was used in the request message
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadsipversionouts
        
        	This object reflects the total number of SIP Version Not  Supported (505) responses sent by the user agent since system startup. Outbound SIP Version Not Supported responses indicate that  this system does not support, or refuses to support, the SIP  protocol version used in received requests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverprecondfailureins
        
        	This object reflects the total number of Precondition  Failure (580) responses received by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverprecondfailureouts
        
        	This object reflects the total number of Precondition  Failure (580) responses sent by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatserrserver, self).__init__()

            self.yang_name = "cSipStatsErrServer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsserverinterrorins', YLeaf(YType.uint32, 'cSipStatsServerIntErrorIns')),
                ('csipstatsserverinterrorouts', YLeaf(YType.uint32, 'cSipStatsServerIntErrorOuts')),
                ('csipstatsservernotimplementedins', YLeaf(YType.uint32, 'cSipStatsServerNotImplementedIns')),
                ('csipstatsservernotimplementedouts', YLeaf(YType.uint32, 'cSipStatsServerNotImplementedOuts')),
                ('csipstatsserverbadgatewayins', YLeaf(YType.uint32, 'cSipStatsServerBadGatewayIns')),
                ('csipstatsserverbadgatewayouts', YLeaf(YType.uint32, 'cSipStatsServerBadGatewayOuts')),
                ('csipstatsserverserviceunavailins', YLeaf(YType.uint32, 'cSipStatsServerServiceUnavailIns')),
                ('csipstatsserverserviceunavailouts', YLeaf(YType.uint32, 'cSipStatsServerServiceUnavailOuts')),
                ('csipstatsservergatewaytimeoutins', YLeaf(YType.uint32, 'cSipStatsServerGatewayTimeoutIns')),
                ('csipstatsservergatewaytimeoutouts', YLeaf(YType.uint32, 'cSipStatsServerGatewayTimeoutOuts')),
                ('csipstatsserverbadsipversionins', YLeaf(YType.uint32, 'cSipStatsServerBadSipVersionIns')),
                ('csipstatsserverbadsipversionouts', YLeaf(YType.uint32, 'cSipStatsServerBadSipVersionOuts')),
                ('csipstatsserverprecondfailureins', YLeaf(YType.uint32, 'cSipStatsServerPrecondFailureIns')),
                ('csipstatsserverprecondfailureouts', YLeaf(YType.uint32, 'cSipStatsServerPrecondFailureOuts')),
            ])
            self.csipstatsserverinterrorins = None
            self.csipstatsserverinterrorouts = None
            self.csipstatsservernotimplementedins = None
            self.csipstatsservernotimplementedouts = None
            self.csipstatsserverbadgatewayins = None
            self.csipstatsserverbadgatewayouts = None
            self.csipstatsserverserviceunavailins = None
            self.csipstatsserverserviceunavailouts = None
            self.csipstatsservergatewaytimeoutins = None
            self.csipstatsservergatewaytimeoutouts = None
            self.csipstatsserverbadsipversionins = None
            self.csipstatsserverbadsipversionouts = None
            self.csipstatsserverprecondfailureins = None
            self.csipstatsserverprecondfailureouts = None
            self._segment_path = lambda: "cSipStatsErrServer"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatserrserver, ['csipstatsserverinterrorins', 'csipstatsserverinterrorouts', 'csipstatsservernotimplementedins', 'csipstatsservernotimplementedouts', 'csipstatsserverbadgatewayins', 'csipstatsserverbadgatewayouts', 'csipstatsserverserviceunavailins', 'csipstatsserverserviceunavailouts', 'csipstatsservergatewaytimeoutins', 'csipstatsservergatewaytimeoutouts', 'csipstatsserverbadsipversionins', 'csipstatsserverbadsipversionouts', 'csipstatsserverprecondfailureins', 'csipstatsserverprecondfailureouts'], name, value)


    class Csipstatsglobalfail(Entity):
        """
        
        
        .. attribute:: csipstatsglobalbusyeverywhereins
        
        	This object reflects the total number of Busy Everywhere (600) responses received by the user agent since system startup. Inbound Busy Everywhere responses indicate that the  called party's end system was contacted successfully but the called party is busy and does not wish to take the call at this time
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalbusyeverywhereouts
        
        	This object reflects the total number of Busy Everywhere (600) responses sent by the user agent since system startup. Outbound Busy Everywhere responses indicate that  this system has successfully contacted a called party's end system and the called party does not wish to take the call at this time
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobaldeclineins
        
        	This object reflects the total number of Decline (603) responses received by the user agent since system startup. Decline responses indicate that the called party's end  system was contacted successfully but the called party  explicitly does not wish to, or cannot, participate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobaldeclineouts
        
        	This object reflects the total number of Decline (603) responses sent by the user agent since system startup. Outbound Decline responses indicate that this system has successfully contacted a called party's end system and the called party explicitly does not wish to, or cannot, participate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotanywhereins
        
        	This object reflects the total number of Does Not Exist Anywhere (604) responses received by the user agent since system startup. Inbound Does Not Exist Anywhere responses indicate that the server handling this system's request has authoritative information that the called party indicated in the To request field does not exist anywhere
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotanywhereouts
        
        	This object reflects the total number of Does Not Exist Anywhere (604) responses sent by the user agent since system startup. Outbound Does Not Exist Anywhere responses indicate that this system has authoritative information that the called party in the To field of received requests does not exist anywhere
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotacceptableins
        
        	This object reflects the total number of Not Acceptable (606) responses received by the user agent since system startup. Inbound Not Acceptable responses indicate that the called party's end system was contacted successfully but some aspect of the session description is not acceptable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotacceptableouts
        
        	This object reflects the total number of Not Acceptable (606) responses sent by the user agent since system startup. Outbound Not Acceptable responses indicate that the called party wishes to communicate, but cannot adequately support the session described in the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsglobalfail, self).__init__()

            self.yang_name = "cSipStatsGlobalFail"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsglobalbusyeverywhereins', YLeaf(YType.uint32, 'cSipStatsGlobalBusyEverywhereIns')),
                ('csipstatsglobalbusyeverywhereouts', YLeaf(YType.uint32, 'cSipStatsGlobalBusyEverywhereOuts')),
                ('csipstatsglobaldeclineins', YLeaf(YType.uint32, 'cSipStatsGlobalDeclineIns')),
                ('csipstatsglobaldeclineouts', YLeaf(YType.uint32, 'cSipStatsGlobalDeclineOuts')),
                ('csipstatsglobalnotanywhereins', YLeaf(YType.uint32, 'cSipStatsGlobalNotAnywhereIns')),
                ('csipstatsglobalnotanywhereouts', YLeaf(YType.uint32, 'cSipStatsGlobalNotAnywhereOuts')),
                ('csipstatsglobalnotacceptableins', YLeaf(YType.uint32, 'cSipStatsGlobalNotAcceptableIns')),
                ('csipstatsglobalnotacceptableouts', YLeaf(YType.uint32, 'cSipStatsGlobalNotAcceptableOuts')),
            ])
            self.csipstatsglobalbusyeverywhereins = None
            self.csipstatsglobalbusyeverywhereouts = None
            self.csipstatsglobaldeclineins = None
            self.csipstatsglobaldeclineouts = None
            self.csipstatsglobalnotanywhereins = None
            self.csipstatsglobalnotanywhereouts = None
            self.csipstatsglobalnotacceptableins = None
            self.csipstatsglobalnotacceptableouts = None
            self._segment_path = lambda: "cSipStatsGlobalFail"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsglobalfail, ['csipstatsglobalbusyeverywhereins', 'csipstatsglobalbusyeverywhereouts', 'csipstatsglobaldeclineins', 'csipstatsglobaldeclineouts', 'csipstatsglobalnotanywhereins', 'csipstatsglobalnotanywhereouts', 'csipstatsglobalnotacceptableins', 'csipstatsglobalnotacceptableouts'], name, value)


    class Csipstatstraffic(Entity):
        """
        
        
        .. attribute:: csipstatstrafficinviteins
        
        	This object reflects the total number of INVITE requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinviteouts
        
        	This object reflects the total number of INVITE requests sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficackins
        
        	This object reflects the total number of ACK requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficackouts
        
        	This object reflects the total number of ACK requests sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficbyeins
        
        	This object reflects the total number of BYE requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficbyeouts
        
        	This object reflects the total number of BYE requests sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcancelins
        
        	This object reflects the total number of CANCEL requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcancelouts
        
        	This object reflects the total number of CANCEL requests sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficoptionsins
        
        	This object reflects the total number of OPTIONS requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficoptionsouts
        
        	This object reflects the total number of OPTIONS requests sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficregisterins
        
        	This object reflects the total number of REGISTER requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficregisterouts
        
        	This object reflects the total number of REGISTER requests  sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcometins
        
        	This object reflects the total number of COndition MET  requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcometouts
        
        	This object reflects the total number of COndition MET  requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficprackins
        
        	This object reflects the total number of PRovisonal  ACKnowledgement requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficprackouts
        
        	This object reflects the total number of PRovisonal  ACKnowledgement requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficreferins
        
        	This object reflects the total number of Refer requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficreferouts
        
        	This object reflects the total number of Refer requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficnotifyins
        
        	This object reflects the total number of Notify  requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficnotifyouts
        
        	This object reflects the total number of Notify  requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinfoins
        
        	This object reflects the total number of Info  requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinfoouts
        
        	This object reflects the total number of Info  requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficsubscribeins
        
        	This object reflects the total number of Subscribe requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficsubscribeouts
        
        	This object reflects the total number of Subscribe requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficupdateins
        
        	This object reflects the total number of Update requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficupdateouts
        
        	This object reflects the total number of Update requests sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatstraffic, self).__init__()

            self.yang_name = "cSipStatsTraffic"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatstrafficinviteins', YLeaf(YType.uint32, 'cSipStatsTrafficInviteIns')),
                ('csipstatstrafficinviteouts', YLeaf(YType.uint32, 'cSipStatsTrafficInviteOuts')),
                ('csipstatstrafficackins', YLeaf(YType.uint32, 'cSipStatsTrafficAckIns')),
                ('csipstatstrafficackouts', YLeaf(YType.uint32, 'cSipStatsTrafficAckOuts')),
                ('csipstatstrafficbyeins', YLeaf(YType.uint32, 'cSipStatsTrafficByeIns')),
                ('csipstatstrafficbyeouts', YLeaf(YType.uint32, 'cSipStatsTrafficByeOuts')),
                ('csipstatstrafficcancelins', YLeaf(YType.uint32, 'cSipStatsTrafficCancelIns')),
                ('csipstatstrafficcancelouts', YLeaf(YType.uint32, 'cSipStatsTrafficCancelOuts')),
                ('csipstatstrafficoptionsins', YLeaf(YType.uint32, 'cSipStatsTrafficOptionsIns')),
                ('csipstatstrafficoptionsouts', YLeaf(YType.uint32, 'cSipStatsTrafficOptionsOuts')),
                ('csipstatstrafficregisterins', YLeaf(YType.uint32, 'cSipStatsTrafficRegisterIns')),
                ('csipstatstrafficregisterouts', YLeaf(YType.uint32, 'cSipStatsTrafficRegisterOuts')),
                ('csipstatstrafficcometins', YLeaf(YType.uint32, 'cSipStatsTrafficCometIns')),
                ('csipstatstrafficcometouts', YLeaf(YType.uint32, 'cSipStatsTrafficCometOuts')),
                ('csipstatstrafficprackins', YLeaf(YType.uint32, 'cSipStatsTrafficPrackIns')),
                ('csipstatstrafficprackouts', YLeaf(YType.uint32, 'cSipStatsTrafficPrackOuts')),
                ('csipstatstrafficreferins', YLeaf(YType.uint32, 'cSipStatsTrafficReferIns')),
                ('csipstatstrafficreferouts', YLeaf(YType.uint32, 'cSipStatsTrafficReferOuts')),
                ('csipstatstrafficnotifyins', YLeaf(YType.uint32, 'cSipStatsTrafficNotifyIns')),
                ('csipstatstrafficnotifyouts', YLeaf(YType.uint32, 'cSipStatsTrafficNotifyOuts')),
                ('csipstatstrafficinfoins', YLeaf(YType.uint32, 'cSipStatsTrafficInfoIns')),
                ('csipstatstrafficinfoouts', YLeaf(YType.uint32, 'cSipStatsTrafficInfoOuts')),
                ('csipstatstrafficsubscribeins', YLeaf(YType.uint32, 'cSipStatsTrafficSubscribeIns')),
                ('csipstatstrafficsubscribeouts', YLeaf(YType.uint32, 'cSipStatsTrafficSubscribeOuts')),
                ('csipstatstrafficupdateins', YLeaf(YType.uint32, 'cSipStatsTrafficUpdateIns')),
                ('csipstatstrafficupdateouts', YLeaf(YType.uint32, 'cSipStatsTrafficUpdateOuts')),
            ])
            self.csipstatstrafficinviteins = None
            self.csipstatstrafficinviteouts = None
            self.csipstatstrafficackins = None
            self.csipstatstrafficackouts = None
            self.csipstatstrafficbyeins = None
            self.csipstatstrafficbyeouts = None
            self.csipstatstrafficcancelins = None
            self.csipstatstrafficcancelouts = None
            self.csipstatstrafficoptionsins = None
            self.csipstatstrafficoptionsouts = None
            self.csipstatstrafficregisterins = None
            self.csipstatstrafficregisterouts = None
            self.csipstatstrafficcometins = None
            self.csipstatstrafficcometouts = None
            self.csipstatstrafficprackins = None
            self.csipstatstrafficprackouts = None
            self.csipstatstrafficreferins = None
            self.csipstatstrafficreferouts = None
            self.csipstatstrafficnotifyins = None
            self.csipstatstrafficnotifyouts = None
            self.csipstatstrafficinfoins = None
            self.csipstatstrafficinfoouts = None
            self.csipstatstrafficsubscribeins = None
            self.csipstatstrafficsubscribeouts = None
            self.csipstatstrafficupdateins = None
            self.csipstatstrafficupdateouts = None
            self._segment_path = lambda: "cSipStatsTraffic"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatstraffic, ['csipstatstrafficinviteins', 'csipstatstrafficinviteouts', 'csipstatstrafficackins', 'csipstatstrafficackouts', 'csipstatstrafficbyeins', 'csipstatstrafficbyeouts', 'csipstatstrafficcancelins', 'csipstatstrafficcancelouts', 'csipstatstrafficoptionsins', 'csipstatstrafficoptionsouts', 'csipstatstrafficregisterins', 'csipstatstrafficregisterouts', 'csipstatstrafficcometins', 'csipstatstrafficcometouts', 'csipstatstrafficprackins', 'csipstatstrafficprackouts', 'csipstatstrafficreferins', 'csipstatstrafficreferouts', 'csipstatstrafficnotifyins', 'csipstatstrafficnotifyouts', 'csipstatstrafficinfoins', 'csipstatstrafficinfoouts', 'csipstatstrafficsubscribeins', 'csipstatstrafficsubscribeouts', 'csipstatstrafficupdateins', 'csipstatstrafficupdateouts'], name, value)


    class Csipstatsretry(Entity):
        """
        
        
        .. attribute:: csipstatsretryinvites
        
        	This object reflects the total number of INVITE retries that  have been sent by the user agent since system startup.   If the number of 'first  attempt' INVITES is of interest, subtract the value of this  object from cSipStatsTrafficInviteOut
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrybyes
        
        	This object reflects the total number of BYE retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycancels
        
        	This object reflects the total number of CANCEL retries that  have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryregisters
        
        	This object reflects the total number of REGISTER retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryresponses
        
        	This object reflects the total number of Response (while  expecting a ACK) retries that have been sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrypracks
        
        	This object reflects the total number of PRovisional ACKnowledgement retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycomets
        
        	This object reflects the total number of COndition MET retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryreliable1xxrsps
        
        	This object reflects the total number of Reliable 1xx Response retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrynotifys
        
        	This object reflects the total number of Notify  retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryrefers
        
        	This object reflects the total number of Refer retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryinfo
        
        	This object reflects the total number of Info retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrysubscribe
        
        	This object reflects the total number of Subscribe retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsretry, self).__init__()

            self.yang_name = "cSipStatsRetry"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsretryinvites', YLeaf(YType.uint32, 'cSipStatsRetryInvites')),
                ('csipstatsretrybyes', YLeaf(YType.uint32, 'cSipStatsRetryByes')),
                ('csipstatsretrycancels', YLeaf(YType.uint32, 'cSipStatsRetryCancels')),
                ('csipstatsretryregisters', YLeaf(YType.uint32, 'cSipStatsRetryRegisters')),
                ('csipstatsretryresponses', YLeaf(YType.uint32, 'cSipStatsRetryResponses')),
                ('csipstatsretrypracks', YLeaf(YType.uint32, 'cSipStatsRetryPracks')),
                ('csipstatsretrycomets', YLeaf(YType.uint32, 'cSipStatsRetryComets')),
                ('csipstatsretryreliable1xxrsps', YLeaf(YType.uint32, 'cSipStatsRetryReliable1xxRsps')),
                ('csipstatsretrynotifys', YLeaf(YType.uint32, 'cSipStatsRetryNotifys')),
                ('csipstatsretryrefers', YLeaf(YType.uint32, 'cSipStatsRetryRefers')),
                ('csipstatsretryinfo', YLeaf(YType.uint32, 'cSipStatsRetryInfo')),
                ('csipstatsretrysubscribe', YLeaf(YType.uint32, 'cSipStatsRetrySubscribe')),
            ])
            self.csipstatsretryinvites = None
            self.csipstatsretrybyes = None
            self.csipstatsretrycancels = None
            self.csipstatsretryregisters = None
            self.csipstatsretryresponses = None
            self.csipstatsretrypracks = None
            self.csipstatsretrycomets = None
            self.csipstatsretryreliable1xxrsps = None
            self.csipstatsretrynotifys = None
            self.csipstatsretryrefers = None
            self.csipstatsretryinfo = None
            self.csipstatsretrysubscribe = None
            self._segment_path = lambda: "cSipStatsRetry"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsretry, ['csipstatsretryinvites', 'csipstatsretrybyes', 'csipstatsretrycancels', 'csipstatsretryregisters', 'csipstatsretryresponses', 'csipstatsretrypracks', 'csipstatsretrycomets', 'csipstatsretryreliable1xxrsps', 'csipstatsretrynotifys', 'csipstatsretryrefers', 'csipstatsretryinfo', 'csipstatsretrysubscribe'], name, value)


    class Csipstatsmisc(Entity):
        """
        
        
        .. attribute:: csipstatsmisc3xxmappedto4xxrsps
        
        	This object reflects the total number of incoming Redirect  (3xx) response messages that have been mapped to Client  Error (4xx) response messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsmisc, self).__init__()

            self.yang_name = "cSipStatsMisc"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsmisc3xxmappedto4xxrsps', YLeaf(YType.uint32, 'cSipStatsMisc3xxMappedTo4xxRsps')),
            ])
            self.csipstatsmisc3xxmappedto4xxrsps = None
            self._segment_path = lambda: "cSipStatsMisc"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsmisc, ['csipstatsmisc3xxmappedto4xxrsps'], name, value)


    class Csipstatsconnection(Entity):
        """
        
        
        .. attribute:: csipstatsconntcpsendfailures
        
        	This object reflects the total number of TCP send failures since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpsendfailures
        
        	This object reflects the total number of UDP send failures since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpremoteclosures
        
        	This object reflects the total number of Remote Closures  for TCP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpcreatefailures
        
        	This object reflects the total number of connection create failures for UDP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpcreatefailures
        
        	This object reflects the total number of connection create failures for TCP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpinactivetimeouts
        
        	This object reflects the total number of UDP connections that  timed out due to inactivity since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpinactivetimeouts
        
        	This object reflects the total number of TCP connections that timed out due to inactivity since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsactiveudpconnections
        
        	This object reflects the total number of active UDP connections since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsactivetcpconnections
        
        	This object reflects the total number of active TCP connections since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatsconnection, self).__init__()

            self.yang_name = "cSipStatsConnection"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csipstatsconntcpsendfailures', YLeaf(YType.uint32, 'cSipStatsConnTCPSendFailures')),
                ('csipstatsconnudpsendfailures', YLeaf(YType.uint32, 'cSipStatsConnUDPSendFailures')),
                ('csipstatsconntcpremoteclosures', YLeaf(YType.uint32, 'cSipStatsConnTCPRemoteClosures')),
                ('csipstatsconnudpcreatefailures', YLeaf(YType.uint32, 'cSipStatsConnUDPCreateFailures')),
                ('csipstatsconntcpcreatefailures', YLeaf(YType.uint32, 'cSipStatsConnTCPCreateFailures')),
                ('csipstatsconnudpinactivetimeouts', YLeaf(YType.uint32, 'cSipStatsConnUDPInactiveTimeouts')),
                ('csipstatsconntcpinactivetimeouts', YLeaf(YType.uint32, 'cSipStatsConnTCPInactiveTimeouts')),
                ('csipstatsactiveudpconnections', YLeaf(YType.uint32, 'cSipStatsActiveUDPConnections')),
                ('csipstatsactivetcpconnections', YLeaf(YType.uint32, 'cSipStatsActiveTCPConnections')),
            ])
            self.csipstatsconntcpsendfailures = None
            self.csipstatsconnudpsendfailures = None
            self.csipstatsconntcpremoteclosures = None
            self.csipstatsconnudpcreatefailures = None
            self.csipstatsconntcpcreatefailures = None
            self.csipstatsconnudpinactivetimeouts = None
            self.csipstatsconntcpinactivetimeouts = None
            self.csipstatsactiveudpconnections = None
            self.csipstatsactivetcpconnections = None
            self._segment_path = lambda: "cSipStatsConnection"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatsconnection, ['csipstatsconntcpsendfailures', 'csipstatsconnudpsendfailures', 'csipstatsconntcpremoteclosures', 'csipstatsconnudpcreatefailures', 'csipstatsconntcpcreatefailures', 'csipstatsconnudpinactivetimeouts', 'csipstatsconntcpinactivetimeouts', 'csipstatsactiveudpconnections', 'csipstatsactivetcpconnections'], name, value)


    class Csipcfgearlymediatable(Entity):
        """
        This table contains configuration for Early
        Media Cut Through.  The configuration controls
        how the SIP user agent will process 1xx
        (Provisional) SIP response messages that contain 
        Session Definition Protocol (SDP) payloads.
        
        .. attribute:: csipcfgearlymediaentry
        
        	A row in the cSipCfgEarlyMediaTable. A row is accessible with a Provisional (1xx) status code value (eg, 180) and provides an object for the enabling or disabling of the Early Media Cut Through functionality
        	**type**\: list of  		 :py:class:`Csipcfgearlymediaentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgearlymediatable.Csipcfgearlymediaentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgearlymediatable, self).__init__()

            self.yang_name = "cSipCfgEarlyMediaTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipCfgEarlyMediaEntry", ("csipcfgearlymediaentry", CISCOSIPUAMIB.Csipcfgearlymediatable.Csipcfgearlymediaentry))])
            self._leafs = OrderedDict()

            self.csipcfgearlymediaentry = YList(self)
            self._segment_path = lambda: "cSipCfgEarlyMediaTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgearlymediatable, [], name, value)


        class Csipcfgearlymediaentry(Entity):
            """
            A row in the cSipCfgEarlyMediaTable.
            A row is accessible with a Provisional (1xx)
            status code value (eg, 180) and provides
            an object for the enabling or disabling of
            the Early Media Cut Through functionality.
            
            .. attribute:: csipcfgearlymediastatuscodeindex  (key)
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgearlymediacutthrudisabled
            
            	This object specifies whether Early Media  Cut Through is enabled or disabled for the  SIP response messages with status codes that  match cSipCfgEarlyMediaStatusCodeIndex.  If 'true', early media cut through is disabled, and the user agent will process the message as though it did not contain any SDP payload.  If 'false', early media cut through is enabled, and the user agent will process the message similar to a 183 (Session Progress) and cut through for early media.  The assumption being that the SDP is an indication that the far end is going to send early media
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipcfgearlymediatable.Csipcfgearlymediaentry, self).__init__()

                self.yang_name = "cSipCfgEarlyMediaEntry"
                self.yang_parent_name = "cSipCfgEarlyMediaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipcfgearlymediastatuscodeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipcfgearlymediastatuscodeindex', YLeaf(YType.int32, 'cSipCfgEarlyMediaStatusCodeIndex')),
                    ('csipcfgearlymediacutthrudisabled', YLeaf(YType.boolean, 'cSipCfgEarlyMediaCutThruDisabled')),
                ])
                self.csipcfgearlymediastatuscodeindex = None
                self.csipcfgearlymediacutthrudisabled = None
                self._segment_path = lambda: "cSipCfgEarlyMediaEntry" + "[cSipCfgEarlyMediaStatusCodeIndex='" + str(self.csipcfgearlymediastatuscodeindex) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgEarlyMediaTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgearlymediatable.Csipcfgearlymediaentry, ['csipcfgearlymediastatuscodeindex', 'csipcfgearlymediacutthrudisabled'], name, value)


    class Csipcfgbindsourceaddrtable(Entity):
        """
        This table contains configuration for binding
        the scope of packets to the particular ethernet
        interface. The scope for the packets can be
        specified as either 'signalling' or 'media'
        packets. The ethernet interface shall be
        specified by the interface index. The table
        shall be indexed based on the scope.
        
        .. attribute:: csipcfgbindsourceaddrentry
        
        	A row in the cSipCfgBindSourceAddrTable. A row is accessible with the scope of packets to which the source IP address of the interface designated by cSipCfgBindSourceAddrInterface will be bound
        	**type**\: list of  		 :py:class:`Csipcfgbindsourceaddrentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgbindsourceaddrtable, self).__init__()

            self.yang_name = "cSipCfgBindSourceAddrTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipCfgBindSourceAddrEntry", ("csipcfgbindsourceaddrentry", CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry))])
            self._leafs = OrderedDict()

            self.csipcfgbindsourceaddrentry = YList(self)
            self._segment_path = lambda: "cSipCfgBindSourceAddrTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgbindsourceaddrtable, [], name, value)


        class Csipcfgbindsourceaddrentry(Entity):
            """
            A row in the cSipCfgBindSourceAddrTable.
            A row is accessible with the scope of packets
            to which the source IP address of the interface
            designated by cSipCfgBindSourceAddrInterface
            will be bound.
            
            .. attribute:: csipcfgbindsourceaddrscope  (key)
            
            	A unique identifier of a row in this table and specifies the scope of packets to which the source IP address of the interface designated by cSipCfgBindSourceAddrInterface will be bound
            	**type**\:  :py:class:`Csipcfgbindsourceaddrscope <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry.Csipcfgbindsourceaddrscope>`
            
            .. attribute:: csipcfgbindsourceaddrinterface
            
            	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that there is no specific source address configured and in this case the best local IP address will be chosen by the system
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, self).__init__()

                self.yang_name = "cSipCfgBindSourceAddrEntry"
                self.yang_parent_name = "cSipCfgBindSourceAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipcfgbindsourceaddrscope']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipcfgbindsourceaddrscope', YLeaf(YType.enumeration, 'cSipCfgBindSourceAddrScope')),
                    ('csipcfgbindsourceaddrinterface', YLeaf(YType.int32, 'cSipCfgBindSourceAddrInterface')),
                ])
                self.csipcfgbindsourceaddrscope = None
                self.csipcfgbindsourceaddrinterface = None
                self._segment_path = lambda: "cSipCfgBindSourceAddrEntry" + "[cSipCfgBindSourceAddrScope='" + str(self.csipcfgbindsourceaddrscope) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgBindSourceAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, ['csipcfgbindsourceaddrscope', 'csipcfgbindsourceaddrinterface'], name, value)

            class Csipcfgbindsourceaddrscope(Enum):
                """
                Csipcfgbindsourceaddrscope (Enum Class)

                A unique identifier of a row in this table and

                specifies the scope of packets to which the

                source IP address of the interface

                designated by cSipCfgBindSourceAddrInterface

                will be bound.

                .. data:: media = 1

                .. data:: control = 2

                """

                media = Enum.YLeaf(1, "media")

                control = Enum.YLeaf(2, "control")



    class Csipcfgpeertable(Entity):
        """
        This table contains per dial\-peer SIP related 
        configuration.   
        
        The table is a sparse table of dial\-peer information.
        This means, it only reflects dial\-peers being used 
        for SIP.  A dial\-peer is being used for SIP if the 
        value of cvVoIPPeerCfgSessionProtocol 
        (CISCO\-VOICE\-DIAL\-CONTROL\-MIB) is 'sip'.
        
        Dial\-peers are not created or destroyed via this
        table.  Only SIP related configuration can be 
        performed via this table once the dial\-peer exists
        in the system and is visible in this table.
        
        .. attribute:: csipcfgpeerentry
        
        	A row in the cSipCfgPeerTable
        	**type**\: list of  		 :py:class:`Csipcfgpeerentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgpeertable, self).__init__()

            self.yang_name = "cSipCfgPeerTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipCfgPeerEntry", ("csipcfgpeerentry", CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry))])
            self._leafs = OrderedDict()

            self.csipcfgpeerentry = YList(self)
            self._segment_path = lambda: "cSipCfgPeerTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeertable, [], name, value)


        class Csipcfgpeerentry(Entity):
            """
            A row in the cSipCfgPeerTable.
            
            .. attribute:: csipcfgpeerindex  (key)
            
            	An arbitrary index that uniquely identifies a  dial\-peer configured for SIP
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpeeroutsessiontransport
            
            	This object specifies the session transport  protocol that will be used by this dial\-peer for outbound SIP messages.    The value 'system' is the default and indicates  that this dial\-peer should use the value set by  cSipCfgOutSessionTransport instead
            	**type**\:  :py:class:`Csipcfgpeeroutsessiontransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeeroutsessiontransport>`
            
            .. attribute:: csipcfgpeerreliable1xxrspstr
            
            	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgPeerReliable1xxRspHdr
            	**type**\: str
            
            .. attribute:: csipcfgpeerreliable1xxrsphdr
            
            	This object specifies behavior with respect to Support or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs.  The value 'system' is the default and indicates that this  dial\-peer should use the value of  cSipCfgReliable1xxRspHdr instead
            	**type**\:  :py:class:`Csipcfgpeerreliable1Xxrsphdr <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeerreliable1Xxrsphdr>`
            
            .. attribute:: csipcfgpeerurltype
            
            	This object specifies the URL type sent in outbound INVITES generated by this device.  The value 'system' is the default and indicates that this  dial\-peer should use the value of cSipCfgUrlType instead
            	**type**\:  :py:class:`Csipcfgpeerurltype <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeerurltype>`
            
            .. attribute:: csipcfgpeerswitchtransenabled
            
            	This object specifies if the functionality of switching between transports from UDP to TCP if the message size of a Request is greater than 1300 bytes is enabled or not
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry, self).__init__()

                self.yang_name = "cSipCfgPeerEntry"
                self.yang_parent_name = "cSipCfgPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipcfgpeerindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipcfgpeerindex', YLeaf(YType.int32, 'cSipCfgPeerIndex')),
                    ('csipcfgpeeroutsessiontransport', YLeaf(YType.enumeration, 'cSipCfgPeerOutSessionTransport')),
                    ('csipcfgpeerreliable1xxrspstr', YLeaf(YType.str, 'cSipCfgPeerReliable1xxRspStr')),
                    ('csipcfgpeerreliable1xxrsphdr', YLeaf(YType.enumeration, 'cSipCfgPeerReliable1xxRspHdr')),
                    ('csipcfgpeerurltype', YLeaf(YType.enumeration, 'cSipCfgPeerUrlType')),
                    ('csipcfgpeerswitchtransenabled', YLeaf(YType.boolean, 'cSipCfgPeerSwitchTransEnabled')),
                ])
                self.csipcfgpeerindex = None
                self.csipcfgpeeroutsessiontransport = None
                self.csipcfgpeerreliable1xxrspstr = None
                self.csipcfgpeerreliable1xxrsphdr = None
                self.csipcfgpeerurltype = None
                self.csipcfgpeerswitchtransenabled = None
                self._segment_path = lambda: "cSipCfgPeerEntry" + "[cSipCfgPeerIndex='" + str(self.csipcfgpeerindex) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgPeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry, ['csipcfgpeerindex', 'csipcfgpeeroutsessiontransport', 'csipcfgpeerreliable1xxrspstr', 'csipcfgpeerreliable1xxrsphdr', 'csipcfgpeerurltype', 'csipcfgpeerswitchtransenabled'], name, value)

            class Csipcfgpeeroutsessiontransport(Enum):
                """
                Csipcfgpeeroutsessiontransport (Enum Class)

                This object specifies the session transport 

                protocol that will be used by this dial\-peer

                for outbound SIP messages.  

                The value 'system' is the default and indicates 

                that this dial\-peer should use the value set by 

                cSipCfgOutSessionTransport instead.

                .. data:: system = 1

                .. data:: udp = 2

                .. data:: tcp = 3

                """

                system = Enum.YLeaf(1, "system")

                udp = Enum.YLeaf(2, "udp")

                tcp = Enum.YLeaf(3, "tcp")


            class Csipcfgpeerreliable1Xxrsphdr(Enum):
                """
                Csipcfgpeerreliable1Xxrsphdr (Enum Class)

                This object specifies behavior with respect to

                Support or Require headers in SIP messages sent

                and received via this dial\-peer.

                If the originating gateway is configured for 'require',

                the Require header is added to the outgoing INVITEs

                with the value of cSipCfgPeerReliable1xxStr.  This

                requires the use of reliable provisional responses by

                the terminating gateway.  Sessions will be torn down

                if this use cannot be supported by that gateway.

                If the originating gateway is configured for 'supported',

                the Supported header is added to the outgoing INVITEs

                with the value of cSipCfgPeerReliable1xxStr.  This 

                requires that an attempt to use reliable provisional

                responses be made, but sessions can continue without them.

                If the originating gateway is configured for 'disabled',

                the value of cSipCfgReliable1xxStr will NOT be added to

                either the Require or Supported headers of outgoing INVITEs.

                The value 'system' is the default and indicates that this 

                dial\-peer should use the value of  cSipCfgReliable1xxRspHdr

                instead.

                .. data:: system = 1

                .. data:: supported = 2

                .. data:: require = 3

                .. data:: disabled = 4

                """

                system = Enum.YLeaf(1, "system")

                supported = Enum.YLeaf(2, "supported")

                require = Enum.YLeaf(3, "require")

                disabled = Enum.YLeaf(4, "disabled")


            class Csipcfgpeerurltype(Enum):
                """
                Csipcfgpeerurltype (Enum Class)

                This object specifies the URL type sent in outbound

                INVITES generated by this device.

                The value 'system' is the default and indicates that this 

                dial\-peer should use the value of cSipCfgUrlType instead.

                .. data:: system = 1

                .. data:: sip = 2

                .. data:: tel = 3

                """

                system = Enum.YLeaf(1, "system")

                sip = Enum.YLeaf(2, "sip")

                tel = Enum.YLeaf(3, "tel")



    class Csipcfgstatuscausetable(Entity):
        """
        This table contains SIP status code to PSTN cause code
        mapping configuration.  Inbound SIP response messages 
        that will result in outbound PSTN signalling messages
        will have the SIP status codes transposed into the
        PSTN cause codes as prescribed by the contents of this 
        table.
        
        .. attribute:: csipcfgstatuscauseentry
        
        	A row in the cSipCfgStatusCauseTable.  Entries cannot be created or destroyed by the actions of any NMS
        	**type**\: list of  		 :py:class:`Csipcfgstatuscauseentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgstatuscausetable.Csipcfgstatuscauseentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgstatuscausetable, self).__init__()

            self.yang_name = "cSipCfgStatusCauseTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipCfgStatusCauseEntry", ("csipcfgstatuscauseentry", CISCOSIPUAMIB.Csipcfgstatuscausetable.Csipcfgstatuscauseentry))])
            self._leafs = OrderedDict()

            self.csipcfgstatuscauseentry = YList(self)
            self._segment_path = lambda: "cSipCfgStatusCauseTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgstatuscausetable, [], name, value)


        class Csipcfgstatuscauseentry(Entity):
            """
            A row in the cSipCfgStatusCauseTable.  Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgstatuscodeindex  (key)
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpstncause
            
            	The PSTN cause code to which the SIP status code given by cSipCfgStatusCodeIndex is to be mapped for outbound PSTN signalling messages
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgstatuscausestorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipcfgstatuscausetable.Csipcfgstatuscauseentry, self).__init__()

                self.yang_name = "cSipCfgStatusCauseEntry"
                self.yang_parent_name = "cSipCfgStatusCauseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipcfgstatuscodeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipcfgstatuscodeindex', YLeaf(YType.int32, 'cSipCfgStatusCodeIndex')),
                    ('csipcfgpstncause', YLeaf(YType.int32, 'cSipCfgPstnCause')),
                    ('csipcfgstatuscausestorestatus', YLeaf(YType.enumeration, 'cSipCfgStatusCauseStoreStatus')),
                ])
                self.csipcfgstatuscodeindex = None
                self.csipcfgpstncause = None
                self.csipcfgstatuscausestorestatus = None
                self._segment_path = lambda: "cSipCfgStatusCauseEntry" + "[cSipCfgStatusCodeIndex='" + str(self.csipcfgstatuscodeindex) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgStatusCauseTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgstatuscausetable.Csipcfgstatuscauseentry, ['csipcfgstatuscodeindex', 'csipcfgpstncause', 'csipcfgstatuscausestorestatus'], name, value)


    class Csipcfgcausestatustable(Entity):
        """
        This table contains PSTN cause code to SIP status code
        mapping configuration.   Inbound PSTN signalling messages
        that will result in outbound SIP response messages 
        will have the PSTN cause codes transposed into the
        SIP status codes as prescribed by the contents of this 
        table.
        
        .. attribute:: csipcfgcausestatusentry
        
        	A row in the cSipCfgCauseStatusTable. Entries cannot be created or destroyed by the actions of any NMS
        	**type**\: list of  		 :py:class:`Csipcfgcausestatusentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipcfgcausestatustable.Csipcfgcausestatusentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipcfgcausestatustable, self).__init__()

            self.yang_name = "cSipCfgCauseStatusTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipCfgCauseStatusEntry", ("csipcfgcausestatusentry", CISCOSIPUAMIB.Csipcfgcausestatustable.Csipcfgcausestatusentry))])
            self._leafs = OrderedDict()

            self.csipcfgcausestatusentry = YList(self)
            self._segment_path = lambda: "cSipCfgCauseStatusTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgcausestatustable, [], name, value)


        class Csipcfgcausestatusentry(Entity):
            """
            A row in the cSipCfgCauseStatusTable. Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgpstncauseindex  (key)
            
            	A unique identifier of a row in this table and a valid PSTN cause code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgstatuscode
            
            	The SIP status code to which the PSTN cause code given by cSipCfgPstnCauseIndex is to be mapped for outbound SIP response messages
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgcausestatusstorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipcfgcausestatustable.Csipcfgcausestatusentry, self).__init__()

                self.yang_name = "cSipCfgCauseStatusEntry"
                self.yang_parent_name = "cSipCfgCauseStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipcfgpstncauseindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipcfgpstncauseindex', YLeaf(YType.int32, 'cSipCfgPstnCauseIndex')),
                    ('csipcfgstatuscode', YLeaf(YType.int32, 'cSipCfgStatusCode')),
                    ('csipcfgcausestatusstorestatus', YLeaf(YType.enumeration, 'cSipCfgCauseStatusStoreStatus')),
                ])
                self.csipcfgpstncauseindex = None
                self.csipcfgstatuscode = None
                self.csipcfgcausestatusstorestatus = None
                self._segment_path = lambda: "cSipCfgCauseStatusEntry" + "[cSipCfgPstnCauseIndex='" + str(self.csipcfgpstncauseindex) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgCauseStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgcausestatustable.Csipcfgcausestatusentry, ['csipcfgpstncauseindex', 'csipcfgstatuscode', 'csipcfgcausestatusstorestatus'], name, value)


    class Csipstatssuccessoktable(Entity):
        """
        This table contains statistics for sent and
        received 200 Ok response messages.  The 
        statistics are kept on per SIP method basis.
        
        .. attribute:: csipstatssuccessokentry
        
        	A row in the cSipStatsSuccessOkTable.  There is  an entry for each SIP method for which 200 Ok  inbound and/or outbound statistics are kept
        	**type**\: list of  		 :py:class:`Csipstatssuccessokentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CISCOSIPUAMIB.Csipstatssuccessoktable, self).__init__()

            self.yang_name = "cSipStatsSuccessOkTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cSipStatsSuccessOkEntry", ("csipstatssuccessokentry", CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry))])
            self._leafs = OrderedDict()

            self.csipstatssuccessokentry = YList(self)
            self._segment_path = lambda: "cSipStatsSuccessOkTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipstatssuccessoktable, [], name, value)


        class Csipstatssuccessokentry(Entity):
            """
            A row in the cSipStatsSuccessOkTable.  There is 
            an entry for each SIP method for which 200 Ok 
            inbound and/or outbound statistics are kept.
            
            .. attribute:: csipstatssuccessokmethod  (key)
            
            	This object is used for instance identification of objects in this table.  The value reflects a SIP method
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: csipstatssuccessokinbounds
            
            	This object reflects the total number of Ok (200) responses sent by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csipstatssuccessokoutbounds
            
            	This object reflects the total number of Ok (200) responses received by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry, self).__init__()

                self.yang_name = "cSipStatsSuccessOkEntry"
                self.yang_parent_name = "cSipStatsSuccessOkTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csipstatssuccessokmethod']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csipstatssuccessokmethod', YLeaf(YType.str, 'cSipStatsSuccessOkMethod')),
                    ('csipstatssuccessokinbounds', YLeaf(YType.uint32, 'cSipStatsSuccessOkInbounds')),
                    ('csipstatssuccessokoutbounds', YLeaf(YType.uint32, 'cSipStatsSuccessOkOutbounds')),
                ])
                self.csipstatssuccessokmethod = None
                self.csipstatssuccessokinbounds = None
                self.csipstatssuccessokoutbounds = None
                self._segment_path = lambda: "cSipStatsSuccessOkEntry" + "[cSipStatsSuccessOkMethod='" + str(self.csipstatssuccessokmethod) + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipStatsSuccessOkTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry, ['csipstatssuccessokmethod', 'csipstatssuccessokinbounds', 'csipstatssuccessokoutbounds'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOSIPUAMIB()
        return self._top_entity

