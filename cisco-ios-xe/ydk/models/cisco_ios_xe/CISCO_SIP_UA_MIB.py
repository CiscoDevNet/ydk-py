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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
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
        self._child_container_classes = {"cSipCfgBase" : ("csipcfgbase", CISCOSIPUAMIB.Csipcfgbase), "cSipCfgTimer" : ("csipcfgtimer", CISCOSIPUAMIB.Csipcfgtimer), "cSipCfgRetry" : ("csipcfgretry", CISCOSIPUAMIB.Csipcfgretry), "cSipCfgPeer" : ("csipcfgpeer", CISCOSIPUAMIB.Csipcfgpeer), "cSipCfgAaa" : ("csipcfgaaa", CISCOSIPUAMIB.Csipcfgaaa), "cSipCfgVoiceServiceVoip" : ("csipcfgvoiceservicevoip", CISCOSIPUAMIB.Csipcfgvoiceservicevoip), "cSipStatsInfo" : ("csipstatsinfo", CISCOSIPUAMIB.Csipstatsinfo), "cSipStatsSuccess" : ("csipstatssuccess", CISCOSIPUAMIB.Csipstatssuccess), "cSipStatsRedirect" : ("csipstatsredirect", CISCOSIPUAMIB.Csipstatsredirect), "cSipStatsErrClient" : ("csipstatserrclient", CISCOSIPUAMIB.Csipstatserrclient), "cSipStatsErrServer" : ("csipstatserrserver", CISCOSIPUAMIB.Csipstatserrserver), "cSipStatsGlobalFail" : ("csipstatsglobalfail", CISCOSIPUAMIB.Csipstatsglobalfail), "cSipStatsTraffic" : ("csipstatstraffic", CISCOSIPUAMIB.Csipstatstraffic), "cSipStatsRetry" : ("csipstatsretry", CISCOSIPUAMIB.Csipstatsretry), "cSipStatsMisc" : ("csipstatsmisc", CISCOSIPUAMIB.Csipstatsmisc), "cSipStatsConnection" : ("csipstatsconnection", CISCOSIPUAMIB.Csipstatsconnection), "cSipCfgEarlyMediaTable" : ("csipcfgearlymediatable", CISCOSIPUAMIB.Csipcfgearlymediatable), "cSipCfgBindSourceAddrTable" : ("csipcfgbindsourceaddrtable", CISCOSIPUAMIB.Csipcfgbindsourceaddrtable), "cSipCfgPeerTable" : ("csipcfgpeertable", CISCOSIPUAMIB.Csipcfgpeertable), "cSipCfgStatusCauseTable" : ("csipcfgstatuscausetable", CISCOSIPUAMIB.Csipcfgstatuscausetable), "cSipCfgCauseStatusTable" : ("csipcfgcausestatustable", CISCOSIPUAMIB.Csipcfgcausestatustable), "cSipStatsSuccessOkTable" : ("csipstatssuccessoktable", CISCOSIPUAMIB.Csipstatssuccessoktable)}
        self._child_list_classes = {}

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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgversion = YLeaf(YType.str, "cSipCfgVersion")

            self.csipcfgtransport = YLeaf(YType.enumeration, "cSipCfgTransport")

            self.csipcfguserlocationserveraddr = YLeaf(YType.str, "cSipCfgUserLocationServerAddr")

            self.csipcfgmaxforwards = YLeaf(YType.int32, "cSipCfgMaxForwards")

            self.csipcfgbindsrcaddrinterface = YLeaf(YType.int32, "cSipCfgBindSrcAddrInterface")

            self.csipcfgbindsrcaddrscope = YLeaf(YType.enumeration, "cSipCfgBindSrcAddrScope")

            self.csipcfgdnssrvquerystringformat = YLeaf(YType.enumeration, "cSipCfgDnsSrvQueryStringFormat")

            self.csipcfgredirectiondisabled = YLeaf(YType.boolean, "cSipCfgRedirectionDisabled")

            self.csipcfgsymnatenabled = YLeaf(YType.boolean, "cSipCfgSymNatEnabled")

            self.csipcfgsymnatdirectionrole = YLeaf(YType.enumeration, "cSipCfgSymNatDirectionRole")

            self.csipcfgsuspendresumeenabled = YLeaf(YType.boolean, "cSipCfgSuspendResumeEnabled")

            self.csipcfgoffercallhold = YLeaf(YType.enumeration, "cSipCfgOfferCallHold")

            self.csipcfgreasonheaderoveride = YLeaf(YType.boolean, "cSipCfgReasonHeaderOveride")

            self.csipcfgmaximumforwards = YLeaf(YType.int32, "cSipCfgMaximumForwards")
            self._segment_path = lambda: "cSipCfgBase"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgbase, ['csipcfgversion', 'csipcfgtransport', 'csipcfguserlocationserveraddr', 'csipcfgmaxforwards', 'csipcfgbindsrcaddrinterface', 'csipcfgbindsrcaddrscope', 'csipcfgdnssrvquerystringformat', 'csipcfgredirectiondisabled', 'csipcfgsymnatenabled', 'csipcfgsymnatdirectionrole', 'csipcfgsuspendresumeenabled', 'csipcfgoffercallhold', 'csipcfgreasonheaderoveride', 'csipcfgmaximumforwards'], name, value)

        class Csipcfgbindsrcaddrscope(Enum):
            """
            Csipcfgbindsrcaddrscope

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
            Csipcfgdnssrvquerystringformat

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
            Csipcfgoffercallhold

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
            Csipcfgsymnatdirectionrole

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
            Csipcfgtransport

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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgtimertrying = YLeaf(YType.int32, "cSipCfgTimerTrying")

            self.csipcfgtimerexpires = YLeaf(YType.int32, "cSipCfgTimerExpires")

            self.csipcfgtimerconnect = YLeaf(YType.int32, "cSipCfgTimerConnect")

            self.csipcfgtimerdisconnect = YLeaf(YType.int32, "cSipCfgTimerDisconnect")

            self.csipcfgtimerprack = YLeaf(YType.int32, "cSipCfgTimerPrack")

            self.csipcfgtimercomet = YLeaf(YType.int32, "cSipCfgTimerComet")

            self.csipcfgtimerreliablersp = YLeaf(YType.int32, "cSipCfgTimerReliableRsp")

            self.csipcfgtimernotify = YLeaf(YType.int32, "cSipCfgTimerNotify")

            self.csipcfgtimerrefer = YLeaf(YType.int32, "cSipCfgTimerRefer")

            self.csipcfgtimersessiontimer = YLeaf(YType.int32, "cSipCfgTimerSessionTimer")

            self.csipcfgtimerhold = YLeaf(YType.int32, "cSipCfgTimerHold")

            self.csipcfgtimerinfo = YLeaf(YType.int32, "cSipCfgTimerInfo")

            self.csipcfgtimerconnectionaging = YLeaf(YType.int32, "cSipCfgTimerConnectionAging")

            self.csipcfgtimerbufferinvite = YLeaf(YType.int32, "cSipCfgTimerBufferInvite")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgretryinvite = YLeaf(YType.int32, "cSipCfgRetryInvite")

            self.csipcfgretrybye = YLeaf(YType.int32, "cSipCfgRetryBye")

            self.csipcfgretrycancel = YLeaf(YType.int32, "cSipCfgRetryCancel")

            self.csipcfgretryregister = YLeaf(YType.int32, "cSipCfgRetryRegister")

            self.csipcfgretryresponse = YLeaf(YType.int32, "cSipCfgRetryResponse")

            self.csipcfgretryprack = YLeaf(YType.int32, "cSipCfgRetryPrack")

            self.csipcfgretrycomet = YLeaf(YType.int32, "cSipCfgRetryComet")

            self.csipcfgretryreliablersp = YLeaf(YType.int32, "cSipCfgRetryReliableRsp")

            self.csipcfgretrynotify = YLeaf(YType.int32, "cSipCfgRetryNotify")

            self.csipcfgretryrefer = YLeaf(YType.int32, "cSipCfgRetryRefer")

            self.csipcfgretryinfo = YLeaf(YType.int32, "cSipCfgRetryInfo")

            self.csipcfgretrysubscribe = YLeaf(YType.int32, "cSipCfgRetrySubscribe")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgoutsessiontransport = YLeaf(YType.enumeration, "cSipCfgOutSessionTransport")

            self.csipcfgreliable1xxrspstr = YLeaf(YType.str, "cSipCfgReliable1xxRspStr")

            self.csipcfgreliable1xxrsphdr = YLeaf(YType.enumeration, "cSipCfgReliable1xxRspHdr")

            self.csipcfgurltype = YLeaf(YType.enumeration, "cSipCfgUrlType")
            self._segment_path = lambda: "cSipCfgPeer"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeer, ['csipcfgoutsessiontransport', 'csipcfgreliable1xxrspstr', 'csipcfgreliable1xxrsphdr', 'csipcfgurltype'], name, value)

        class Csipcfgoutsessiontransport(Enum):
            """
            Csipcfgoutsessiontransport

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
            Csipcfgreliable1Xxrsphdr

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
            Csipcfgurltype

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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgaaausername = YLeaf(YType.enumeration, "cSipCfgAaaUsername")
            self._segment_path = lambda: "cSipCfgAaa"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgaaa, ['csipcfgaaausername'], name, value)

        class Csipcfgaaausername(Enum):
            """
            Csipcfgaaausername

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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipcfgheaderpassingenabled = YLeaf(YType.boolean, "cSipCfgHeaderPassingEnabled")

            self.csipcfgmaxsubscriptionaccept = YLeaf(YType.uint32, "cSipCfgMaxSubscriptionAccept")

            self.csipcfgmaxsubscriptionoriginate = YLeaf(YType.uint32, "cSipCfgMaxSubscriptionOriginate")

            self.csipcfgswitchtransportenabled = YLeaf(YType.boolean, "cSipCfgSwitchTransportEnabled")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsinfotryingins = YLeaf(YType.uint32, "cSipStatsInfoTryingIns")

            self.csipstatsinfotryingouts = YLeaf(YType.uint32, "cSipStatsInfoTryingOuts")

            self.csipstatsinforingingins = YLeaf(YType.uint32, "cSipStatsInfoRingingIns")

            self.csipstatsinforingingouts = YLeaf(YType.uint32, "cSipStatsInfoRingingOuts")

            self.csipstatsinfoforwardedins = YLeaf(YType.uint32, "cSipStatsInfoForwardedIns")

            self.csipstatsinfoforwardedouts = YLeaf(YType.uint32, "cSipStatsInfoForwardedOuts")

            self.csipstatsinfoqueuedins = YLeaf(YType.uint32, "cSipStatsInfoQueuedIns")

            self.csipstatsinfoqueuedouts = YLeaf(YType.uint32, "cSipStatsInfoQueuedOuts")

            self.csipstatsinfosessionprogins = YLeaf(YType.uint32, "cSipStatsInfoSessionProgIns")

            self.csipstatsinfosessionprogouts = YLeaf(YType.uint32, "cSipStatsInfoSessionProgOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatssuccessokins = YLeaf(YType.uint32, "cSipStatsSuccessOkIns")

            self.csipstatssuccessokouts = YLeaf(YType.uint32, "cSipStatsSuccessOkOuts")

            self.csipstatssuccessacceptedins = YLeaf(YType.uint32, "cSipStatsSuccessAcceptedIns")

            self.csipstatssuccessacceptedouts = YLeaf(YType.uint32, "cSipStatsSuccessAcceptedOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsredirmultiplechoices = YLeaf(YType.uint32, "cSipStatsRedirMultipleChoices")

            self.csipstatsredirmovedperms = YLeaf(YType.uint32, "cSipStatsRedirMovedPerms")

            self.csipstatsredirmovedtemps = YLeaf(YType.uint32, "cSipStatsRedirMovedTemps")

            self.csipstatsredirseeothers = YLeaf(YType.uint32, "cSipStatsRedirSeeOthers")

            self.csipstatsrediruseproxys = YLeaf(YType.uint32, "cSipStatsRedirUseProxys")

            self.csipstatsrediraltservices = YLeaf(YType.uint32, "cSipStatsRedirAltServices")

            self.csipstatsredirmovedtempsins = YLeaf(YType.uint32, "cSipStatsRedirMovedTempsIns")

            self.csipstatsredirmovedtempsouts = YLeaf(YType.uint32, "cSipStatsRedirMovedTempsOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsclientbadrequestins = YLeaf(YType.uint32, "cSipStatsClientBadRequestIns")

            self.csipstatsclientbadrequestouts = YLeaf(YType.uint32, "cSipStatsClientBadRequestOuts")

            self.csipstatsclientunauthorizedins = YLeaf(YType.uint32, "cSipStatsClientUnauthorizedIns")

            self.csipstatsclientunauthorizedouts = YLeaf(YType.uint32, "cSipStatsClientUnauthorizedOuts")

            self.csipstatsclientpaymentreqdins = YLeaf(YType.uint32, "cSipStatsClientPaymentReqdIns")

            self.csipstatsclientpaymentreqdouts = YLeaf(YType.uint32, "cSipStatsClientPaymentReqdOuts")

            self.csipstatsclientforbiddenins = YLeaf(YType.uint32, "cSipStatsClientForbiddenIns")

            self.csipstatsclientforbiddenouts = YLeaf(YType.uint32, "cSipStatsClientForbiddenOuts")

            self.csipstatsclientnotfoundins = YLeaf(YType.uint32, "cSipStatsClientNotFoundIns")

            self.csipstatsclientnotfoundouts = YLeaf(YType.uint32, "cSipStatsClientNotFoundOuts")

            self.csipstatsclientmethnotallowedins = YLeaf(YType.uint32, "cSipStatsClientMethNotAllowedIns")

            self.csipstatsclientmethnotallowedouts = YLeaf(YType.uint32, "cSipStatsClientMethNotAllowedOuts")

            self.csipstatsclientnotacceptableins = YLeaf(YType.uint32, "cSipStatsClientNotAcceptableIns")

            self.csipstatsclientnotacceptableouts = YLeaf(YType.uint32, "cSipStatsClientNotAcceptableOuts")

            self.csipstatsclientproxyauthreqdins = YLeaf(YType.uint32, "cSipStatsClientProxyAuthReqdIns")

            self.csipstatsclientproxyauthreqdouts = YLeaf(YType.uint32, "cSipStatsClientProxyAuthReqdOuts")

            self.csipstatsclientreqtimeoutins = YLeaf(YType.uint32, "cSipStatsClientReqTimeoutIns")

            self.csipstatsclientreqtimeoutouts = YLeaf(YType.uint32, "cSipStatsClientReqTimeoutOuts")

            self.csipstatsclientconflictins = YLeaf(YType.uint32, "cSipStatsClientConflictIns")

            self.csipstatsclientconflictouts = YLeaf(YType.uint32, "cSipStatsClientConflictOuts")

            self.csipstatsclientgoneins = YLeaf(YType.uint32, "cSipStatsClientGoneIns")

            self.csipstatsclientgoneouts = YLeaf(YType.uint32, "cSipStatsClientGoneOuts")

            self.csipstatsclientlengthrequiredins = YLeaf(YType.uint32, "cSipStatsClientLengthRequiredIns")

            self.csipstatsclientlengthrequiredouts = YLeaf(YType.uint32, "cSipStatsClientLengthRequiredOuts")

            self.csipstatsclientreqenttoolargeins = YLeaf(YType.uint32, "cSipStatsClientReqEntTooLargeIns")

            self.csipstatsclientreqenttoolargeouts = YLeaf(YType.uint32, "cSipStatsClientReqEntTooLargeOuts")

            self.csipstatsclientrequritoolargeins = YLeaf(YType.uint32, "cSipStatsClientReqURITooLargeIns")

            self.csipstatsclientrequritoolargeouts = YLeaf(YType.uint32, "cSipStatsClientReqURITooLargeOuts")

            self.csipstatsclientnosupmediatypeins = YLeaf(YType.uint32, "cSipStatsClientNoSupMediaTypeIns")

            self.csipstatsclientnosupmediatypeouts = YLeaf(YType.uint32, "cSipStatsClientNoSupMediaTypeOuts")

            self.csipstatsclientbadextensionins = YLeaf(YType.uint32, "cSipStatsClientBadExtensionIns")

            self.csipstatsclientbadextensionouts = YLeaf(YType.uint32, "cSipStatsClientBadExtensionOuts")

            self.csipstatsclienttempnotavailins = YLeaf(YType.uint32, "cSipStatsClientTempNotAvailIns")

            self.csipstatsclienttempnotavailouts = YLeaf(YType.uint32, "cSipStatsClientTempNotAvailOuts")

            self.csipstatsclientcalllegnoexistins = YLeaf(YType.uint32, "cSipStatsClientCallLegNoExistIns")

            self.csipstatsclientcalllegnoexistouts = YLeaf(YType.uint32, "cSipStatsClientCallLegNoExistOuts")

            self.csipstatsclientloopdetectedins = YLeaf(YType.uint32, "cSipStatsClientLoopDetectedIns")

            self.csipstatsclientloopdetectedouts = YLeaf(YType.uint32, "cSipStatsClientLoopDetectedOuts")

            self.csipstatsclienttoomanyhopsins = YLeaf(YType.uint32, "cSipStatsClientTooManyHopsIns")

            self.csipstatsclienttoomanyhopsouts = YLeaf(YType.uint32, "cSipStatsClientTooManyHopsOuts")

            self.csipstatsclientaddrincompleteins = YLeaf(YType.uint32, "cSipStatsClientAddrIncompleteIns")

            self.csipstatsclientaddrincompleteouts = YLeaf(YType.uint32, "cSipStatsClientAddrIncompleteOuts")

            self.csipstatsclientambiguousins = YLeaf(YType.uint32, "cSipStatsClientAmbiguousIns")

            self.csipstatsclientambiguousouts = YLeaf(YType.uint32, "cSipStatsClientAmbiguousOuts")

            self.csipstatsclientbusyhereins = YLeaf(YType.uint32, "cSipStatsClientBusyHereIns")

            self.csipstatsclientbusyhereouts = YLeaf(YType.uint32, "cSipStatsClientBusyHereOuts")

            self.csipstatsclientreqtermins = YLeaf(YType.uint32, "cSipStatsClientReqTermIns")

            self.csipstatsclientreqtermouts = YLeaf(YType.uint32, "cSipStatsClientReqTermOuts")

            self.csipstatsclientnoaccepthereins = YLeaf(YType.uint32, "cSipStatsClientNoAcceptHereIns")

            self.csipstatsclientnoaccepthereouts = YLeaf(YType.uint32, "cSipStatsClientNoAcceptHereOuts")

            self.csipstatsclientbadeventins = YLeaf(YType.uint32, "cSipStatsClientBadEventIns")

            self.csipstatsclientbadeventouts = YLeaf(YType.uint32, "cSipStatsClientBadEventOuts")

            self.csipstatsclientsttoosmallins = YLeaf(YType.uint32, "cSipStatsClientSTTooSmallIns")

            self.csipstatsclientsttoosmallouts = YLeaf(YType.uint32, "cSipStatsClientSTTooSmallOuts")

            self.csipstatsclientreqpendingins = YLeaf(YType.uint32, "cSipStatsClientReqPendingIns")

            self.csipstatsclientreqpendingouts = YLeaf(YType.uint32, "cSipStatsClientReqPendingOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsserverinterrorins = YLeaf(YType.uint32, "cSipStatsServerIntErrorIns")

            self.csipstatsserverinterrorouts = YLeaf(YType.uint32, "cSipStatsServerIntErrorOuts")

            self.csipstatsservernotimplementedins = YLeaf(YType.uint32, "cSipStatsServerNotImplementedIns")

            self.csipstatsservernotimplementedouts = YLeaf(YType.uint32, "cSipStatsServerNotImplementedOuts")

            self.csipstatsserverbadgatewayins = YLeaf(YType.uint32, "cSipStatsServerBadGatewayIns")

            self.csipstatsserverbadgatewayouts = YLeaf(YType.uint32, "cSipStatsServerBadGatewayOuts")

            self.csipstatsserverserviceunavailins = YLeaf(YType.uint32, "cSipStatsServerServiceUnavailIns")

            self.csipstatsserverserviceunavailouts = YLeaf(YType.uint32, "cSipStatsServerServiceUnavailOuts")

            self.csipstatsservergatewaytimeoutins = YLeaf(YType.uint32, "cSipStatsServerGatewayTimeoutIns")

            self.csipstatsservergatewaytimeoutouts = YLeaf(YType.uint32, "cSipStatsServerGatewayTimeoutOuts")

            self.csipstatsserverbadsipversionins = YLeaf(YType.uint32, "cSipStatsServerBadSipVersionIns")

            self.csipstatsserverbadsipversionouts = YLeaf(YType.uint32, "cSipStatsServerBadSipVersionOuts")

            self.csipstatsserverprecondfailureins = YLeaf(YType.uint32, "cSipStatsServerPrecondFailureIns")

            self.csipstatsserverprecondfailureouts = YLeaf(YType.uint32, "cSipStatsServerPrecondFailureOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsglobalbusyeverywhereins = YLeaf(YType.uint32, "cSipStatsGlobalBusyEverywhereIns")

            self.csipstatsglobalbusyeverywhereouts = YLeaf(YType.uint32, "cSipStatsGlobalBusyEverywhereOuts")

            self.csipstatsglobaldeclineins = YLeaf(YType.uint32, "cSipStatsGlobalDeclineIns")

            self.csipstatsglobaldeclineouts = YLeaf(YType.uint32, "cSipStatsGlobalDeclineOuts")

            self.csipstatsglobalnotanywhereins = YLeaf(YType.uint32, "cSipStatsGlobalNotAnywhereIns")

            self.csipstatsglobalnotanywhereouts = YLeaf(YType.uint32, "cSipStatsGlobalNotAnywhereOuts")

            self.csipstatsglobalnotacceptableins = YLeaf(YType.uint32, "cSipStatsGlobalNotAcceptableIns")

            self.csipstatsglobalnotacceptableouts = YLeaf(YType.uint32, "cSipStatsGlobalNotAcceptableOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatstrafficinviteins = YLeaf(YType.uint32, "cSipStatsTrafficInviteIns")

            self.csipstatstrafficinviteouts = YLeaf(YType.uint32, "cSipStatsTrafficInviteOuts")

            self.csipstatstrafficackins = YLeaf(YType.uint32, "cSipStatsTrafficAckIns")

            self.csipstatstrafficackouts = YLeaf(YType.uint32, "cSipStatsTrafficAckOuts")

            self.csipstatstrafficbyeins = YLeaf(YType.uint32, "cSipStatsTrafficByeIns")

            self.csipstatstrafficbyeouts = YLeaf(YType.uint32, "cSipStatsTrafficByeOuts")

            self.csipstatstrafficcancelins = YLeaf(YType.uint32, "cSipStatsTrafficCancelIns")

            self.csipstatstrafficcancelouts = YLeaf(YType.uint32, "cSipStatsTrafficCancelOuts")

            self.csipstatstrafficoptionsins = YLeaf(YType.uint32, "cSipStatsTrafficOptionsIns")

            self.csipstatstrafficoptionsouts = YLeaf(YType.uint32, "cSipStatsTrafficOptionsOuts")

            self.csipstatstrafficregisterins = YLeaf(YType.uint32, "cSipStatsTrafficRegisterIns")

            self.csipstatstrafficregisterouts = YLeaf(YType.uint32, "cSipStatsTrafficRegisterOuts")

            self.csipstatstrafficcometins = YLeaf(YType.uint32, "cSipStatsTrafficCometIns")

            self.csipstatstrafficcometouts = YLeaf(YType.uint32, "cSipStatsTrafficCometOuts")

            self.csipstatstrafficprackins = YLeaf(YType.uint32, "cSipStatsTrafficPrackIns")

            self.csipstatstrafficprackouts = YLeaf(YType.uint32, "cSipStatsTrafficPrackOuts")

            self.csipstatstrafficreferins = YLeaf(YType.uint32, "cSipStatsTrafficReferIns")

            self.csipstatstrafficreferouts = YLeaf(YType.uint32, "cSipStatsTrafficReferOuts")

            self.csipstatstrafficnotifyins = YLeaf(YType.uint32, "cSipStatsTrafficNotifyIns")

            self.csipstatstrafficnotifyouts = YLeaf(YType.uint32, "cSipStatsTrafficNotifyOuts")

            self.csipstatstrafficinfoins = YLeaf(YType.uint32, "cSipStatsTrafficInfoIns")

            self.csipstatstrafficinfoouts = YLeaf(YType.uint32, "cSipStatsTrafficInfoOuts")

            self.csipstatstrafficsubscribeins = YLeaf(YType.uint32, "cSipStatsTrafficSubscribeIns")

            self.csipstatstrafficsubscribeouts = YLeaf(YType.uint32, "cSipStatsTrafficSubscribeOuts")

            self.csipstatstrafficupdateins = YLeaf(YType.uint32, "cSipStatsTrafficUpdateIns")

            self.csipstatstrafficupdateouts = YLeaf(YType.uint32, "cSipStatsTrafficUpdateOuts")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsretryinvites = YLeaf(YType.uint32, "cSipStatsRetryInvites")

            self.csipstatsretrybyes = YLeaf(YType.uint32, "cSipStatsRetryByes")

            self.csipstatsretrycancels = YLeaf(YType.uint32, "cSipStatsRetryCancels")

            self.csipstatsretryregisters = YLeaf(YType.uint32, "cSipStatsRetryRegisters")

            self.csipstatsretryresponses = YLeaf(YType.uint32, "cSipStatsRetryResponses")

            self.csipstatsretrypracks = YLeaf(YType.uint32, "cSipStatsRetryPracks")

            self.csipstatsretrycomets = YLeaf(YType.uint32, "cSipStatsRetryComets")

            self.csipstatsretryreliable1xxrsps = YLeaf(YType.uint32, "cSipStatsRetryReliable1xxRsps")

            self.csipstatsretrynotifys = YLeaf(YType.uint32, "cSipStatsRetryNotifys")

            self.csipstatsretryrefers = YLeaf(YType.uint32, "cSipStatsRetryRefers")

            self.csipstatsretryinfo = YLeaf(YType.uint32, "cSipStatsRetryInfo")

            self.csipstatsretrysubscribe = YLeaf(YType.uint32, "cSipStatsRetrySubscribe")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsmisc3xxmappedto4xxrsps = YLeaf(YType.uint32, "cSipStatsMisc3xxMappedTo4xxRsps")
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.csipstatsconntcpsendfailures = YLeaf(YType.uint32, "cSipStatsConnTCPSendFailures")

            self.csipstatsconnudpsendfailures = YLeaf(YType.uint32, "cSipStatsConnUDPSendFailures")

            self.csipstatsconntcpremoteclosures = YLeaf(YType.uint32, "cSipStatsConnTCPRemoteClosures")

            self.csipstatsconnudpcreatefailures = YLeaf(YType.uint32, "cSipStatsConnUDPCreateFailures")

            self.csipstatsconntcpcreatefailures = YLeaf(YType.uint32, "cSipStatsConnTCPCreateFailures")

            self.csipstatsconnudpinactivetimeouts = YLeaf(YType.uint32, "cSipStatsConnUDPInactiveTimeouts")

            self.csipstatsconntcpinactivetimeouts = YLeaf(YType.uint32, "cSipStatsConnTCPInactiveTimeouts")

            self.csipstatsactiveudpconnections = YLeaf(YType.uint32, "cSipStatsActiveUDPConnections")

            self.csipstatsactivetcpconnections = YLeaf(YType.uint32, "cSipStatsActiveTCPConnections")
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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipCfgEarlyMediaEntry" : ("csipcfgearlymediaentry", CISCOSIPUAMIB.Csipcfgearlymediatable.Csipcfgearlymediaentry)}

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
            
            .. attribute:: csipcfgearlymediastatuscodeindex  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipcfgearlymediastatuscodeindex = YLeaf(YType.int32, "cSipCfgEarlyMediaStatusCodeIndex")

                self.csipcfgearlymediacutthrudisabled = YLeaf(YType.boolean, "cSipCfgEarlyMediaCutThruDisabled")
                self._segment_path = lambda: "cSipCfgEarlyMediaEntry" + "[cSipCfgEarlyMediaStatusCodeIndex='" + self.csipcfgearlymediastatuscodeindex.get() + "']"
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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipCfgBindSourceAddrEntry" : ("csipcfgbindsourceaddrentry", CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry)}

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
            
            .. attribute:: csipcfgbindsourceaddrscope  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipcfgbindsourceaddrscope = YLeaf(YType.enumeration, "cSipCfgBindSourceAddrScope")

                self.csipcfgbindsourceaddrinterface = YLeaf(YType.int32, "cSipCfgBindSourceAddrInterface")
                self._segment_path = lambda: "cSipCfgBindSourceAddrEntry" + "[cSipCfgBindSourceAddrScope='" + self.csipcfgbindsourceaddrscope.get() + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgBindSourceAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, ['csipcfgbindsourceaddrscope', 'csipcfgbindsourceaddrinterface'], name, value)

            class Csipcfgbindsourceaddrscope(Enum):
                """
                Csipcfgbindsourceaddrscope

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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipCfgPeerEntry" : ("csipcfgpeerentry", CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry)}

            self.csipcfgpeerentry = YList(self)
            self._segment_path = lambda: "cSipCfgPeerTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeertable, [], name, value)


        class Csipcfgpeerentry(Entity):
            """
            A row in the cSipCfgPeerTable.
            
            .. attribute:: csipcfgpeerindex  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipcfgpeerindex = YLeaf(YType.int32, "cSipCfgPeerIndex")

                self.csipcfgpeeroutsessiontransport = YLeaf(YType.enumeration, "cSipCfgPeerOutSessionTransport")

                self.csipcfgpeerreliable1xxrspstr = YLeaf(YType.str, "cSipCfgPeerReliable1xxRspStr")

                self.csipcfgpeerreliable1xxrsphdr = YLeaf(YType.enumeration, "cSipCfgPeerReliable1xxRspHdr")

                self.csipcfgpeerurltype = YLeaf(YType.enumeration, "cSipCfgPeerUrlType")

                self.csipcfgpeerswitchtransenabled = YLeaf(YType.boolean, "cSipCfgPeerSwitchTransEnabled")
                self._segment_path = lambda: "cSipCfgPeerEntry" + "[cSipCfgPeerIndex='" + self.csipcfgpeerindex.get() + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgPeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipcfgpeertable.Csipcfgpeerentry, ['csipcfgpeerindex', 'csipcfgpeeroutsessiontransport', 'csipcfgpeerreliable1xxrspstr', 'csipcfgpeerreliable1xxrsphdr', 'csipcfgpeerurltype', 'csipcfgpeerswitchtransenabled'], name, value)

            class Csipcfgpeeroutsessiontransport(Enum):
                """
                Csipcfgpeeroutsessiontransport

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
                Csipcfgpeerreliable1Xxrsphdr

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
                Csipcfgpeerurltype

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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipCfgStatusCauseEntry" : ("csipcfgstatuscauseentry", CISCOSIPUAMIB.Csipcfgstatuscausetable.Csipcfgstatuscauseentry)}

            self.csipcfgstatuscauseentry = YList(self)
            self._segment_path = lambda: "cSipCfgStatusCauseTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgstatuscausetable, [], name, value)


        class Csipcfgstatuscauseentry(Entity):
            """
            A row in the cSipCfgStatusCauseTable.  Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgstatuscodeindex  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipcfgstatuscodeindex = YLeaf(YType.int32, "cSipCfgStatusCodeIndex")

                self.csipcfgpstncause = YLeaf(YType.int32, "cSipCfgPstnCause")

                self.csipcfgstatuscausestorestatus = YLeaf(YType.enumeration, "cSipCfgStatusCauseStoreStatus")
                self._segment_path = lambda: "cSipCfgStatusCauseEntry" + "[cSipCfgStatusCodeIndex='" + self.csipcfgstatuscodeindex.get() + "']"
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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipCfgCauseStatusEntry" : ("csipcfgcausestatusentry", CISCOSIPUAMIB.Csipcfgcausestatustable.Csipcfgcausestatusentry)}

            self.csipcfgcausestatusentry = YList(self)
            self._segment_path = lambda: "cSipCfgCauseStatusTable"
            self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSIPUAMIB.Csipcfgcausestatustable, [], name, value)


        class Csipcfgcausestatusentry(Entity):
            """
            A row in the cSipCfgCauseStatusTable. Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgpstncauseindex  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipcfgpstncauseindex = YLeaf(YType.int32, "cSipCfgPstnCauseIndex")

                self.csipcfgstatuscode = YLeaf(YType.int32, "cSipCfgStatusCode")

                self.csipcfgcausestatusstorestatus = YLeaf(YType.enumeration, "cSipCfgCauseStatusStoreStatus")
                self._segment_path = lambda: "cSipCfgCauseStatusEntry" + "[cSipCfgPstnCauseIndex='" + self.csipcfgpstncauseindex.get() + "']"
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
            self._child_container_classes = {}
            self._child_list_classes = {"cSipStatsSuccessOkEntry" : ("csipstatssuccessokentry", CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry)}

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
            
            .. attribute:: csipstatssuccessokmethod  <key>
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csipstatssuccessokmethod = YLeaf(YType.str, "cSipStatsSuccessOkMethod")

                self.csipstatssuccessokinbounds = YLeaf(YType.uint32, "cSipStatsSuccessOkInbounds")

                self.csipstatssuccessokoutbounds = YLeaf(YType.uint32, "cSipStatsSuccessOkOutbounds")
                self._segment_path = lambda: "cSipStatsSuccessOkEntry" + "[cSipStatsSuccessOkMethod='" + self.csipstatssuccessokmethod.get() + "']"
                self._absolute_path = lambda: "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipStatsSuccessOkTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSIPUAMIB.Csipstatssuccessoktable.Csipstatssuccessokentry, ['csipstatssuccessokmethod', 'csipstatssuccessokinbounds', 'csipstatssuccessokoutbounds'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOSIPUAMIB()
        return self._top_entity

