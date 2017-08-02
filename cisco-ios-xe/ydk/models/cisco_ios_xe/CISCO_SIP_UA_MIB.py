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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ciscosipuamibnotifications(Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(Ciscosipuamibnotifications, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB:ciscoSipUaMIBNotifications")


class Ciscosipuamibnotificationprefix(Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(Ciscosipuamibnotificationprefix, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB", "CISCO-SIP-UA-MIB:ciscoSipUaMIBNotificationPrefix")


class CiscoSipUaMib(Entity):
    """
    
    
    .. attribute:: csipcfgaaa
    
    	
    	**type**\:   :py:class:`Csipcfgaaa <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgaaa>`
    
    .. attribute:: csipcfgbase
    
    	
    	**type**\:   :py:class:`Csipcfgbase <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase>`
    
    .. attribute:: csipcfgbindsourceaddrtable
    
    	This table contains configuration for binding the scope of packets to the particular ethernet interface. The scope for the packets can be specified as either 'signalling' or 'media' packets. The ethernet interface shall be specified by the interface index. The table shall be indexed based on the scope
    	**type**\:   :py:class:`Csipcfgbindsourceaddrtable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbindsourceaddrtable>`
    
    .. attribute:: csipcfgcausestatustable
    
    	This table contains PSTN cause code to SIP status code mapping configuration.   Inbound PSTN signalling messages that will result in outbound SIP response messages  will have the PSTN cause codes transposed into the SIP status codes as prescribed by the contents of this  table
    	**type**\:   :py:class:`Csipcfgcausestatustable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgcausestatustable>`
    
    .. attribute:: csipcfgearlymediatable
    
    	This table contains configuration for Early Media Cut Through.  The configuration controls how the SIP user agent will process 1xx (Provisional) SIP response messages that contain  Session Definition Protocol (SDP) payloads
    	**type**\:   :py:class:`Csipcfgearlymediatable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgearlymediatable>`
    
    .. attribute:: csipcfgpeer
    
    	
    	**type**\:   :py:class:`Csipcfgpeer <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeer>`
    
    .. attribute:: csipcfgpeertable
    
    	This table contains per dial\-peer SIP related  configuration.     The table is a sparse table of dial\-peer information. This means, it only reflects dial\-peers being used  for SIP.  A dial\-peer is being used for SIP if the  value of cvVoIPPeerCfgSessionProtocol  (CISCO\-VOICE\-DIAL\-CONTROL\-MIB) is 'sip'.  Dial\-peers are not created or destroyed via this table.  Only SIP related configuration can be  performed via this table once the dial\-peer exists in the system and is visible in this table
    	**type**\:   :py:class:`Csipcfgpeertable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeertable>`
    
    .. attribute:: csipcfgretry
    
    	
    	**type**\:   :py:class:`Csipcfgretry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgretry>`
    
    .. attribute:: csipcfgstatuscausetable
    
    	This table contains SIP status code to PSTN cause code mapping configuration.  Inbound SIP response messages  that will result in outbound PSTN signalling messages will have the SIP status codes transposed into the PSTN cause codes as prescribed by the contents of this  table
    	**type**\:   :py:class:`Csipcfgstatuscausetable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgstatuscausetable>`
    
    .. attribute:: csipcfgtimer
    
    	
    	**type**\:   :py:class:`Csipcfgtimer <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgtimer>`
    
    .. attribute:: csipcfgvoiceservicevoip
    
    	
    	**type**\:   :py:class:`Csipcfgvoiceservicevoip <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgvoiceservicevoip>`
    
    .. attribute:: csipstatsconnection
    
    	
    	**type**\:   :py:class:`Csipstatsconnection <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsconnection>`
    
    .. attribute:: csipstatserrclient
    
    	
    	**type**\:   :py:class:`Csipstatserrclient <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatserrclient>`
    
    .. attribute:: csipstatserrserver
    
    	
    	**type**\:   :py:class:`Csipstatserrserver <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatserrserver>`
    
    .. attribute:: csipstatsglobalfail
    
    	
    	**type**\:   :py:class:`Csipstatsglobalfail <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsglobalfail>`
    
    .. attribute:: csipstatsinfo
    
    	
    	**type**\:   :py:class:`Csipstatsinfo <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsinfo>`
    
    .. attribute:: csipstatsmisc
    
    	
    	**type**\:   :py:class:`Csipstatsmisc <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsmisc>`
    
    .. attribute:: csipstatsredirect
    
    	
    	**type**\:   :py:class:`Csipstatsredirect <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsredirect>`
    
    .. attribute:: csipstatsretry
    
    	
    	**type**\:   :py:class:`Csipstatsretry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatsretry>`
    
    .. attribute:: csipstatssuccess
    
    	
    	**type**\:   :py:class:`Csipstatssuccess <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatssuccess>`
    
    .. attribute:: csipstatssuccessoktable
    
    	This table contains statistics for sent and received 200 Ok response messages.  The  statistics are kept on per SIP method basis
    	**type**\:   :py:class:`Csipstatssuccessoktable <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatssuccessoktable>`
    
    .. attribute:: csipstatstraffic
    
    	
    	**type**\:   :py:class:`Csipstatstraffic <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatstraffic>`
    
    

    """

    _prefix = 'CISCO-SIP-UA-MIB'
    _revision = '2004-02-19'

    def __init__(self):
        super(CiscoSipUaMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SIP-UA-MIB"
        self.yang_parent_name = "CISCO-SIP-UA-MIB"

        self.csipcfgaaa = CiscoSipUaMib.Csipcfgaaa()
        self.csipcfgaaa.parent = self
        self._children_name_map["csipcfgaaa"] = "cSipCfgAaa"
        self._children_yang_names.add("cSipCfgAaa")

        self.csipcfgbase = CiscoSipUaMib.Csipcfgbase()
        self.csipcfgbase.parent = self
        self._children_name_map["csipcfgbase"] = "cSipCfgBase"
        self._children_yang_names.add("cSipCfgBase")

        self.csipcfgbindsourceaddrtable = CiscoSipUaMib.Csipcfgbindsourceaddrtable()
        self.csipcfgbindsourceaddrtable.parent = self
        self._children_name_map["csipcfgbindsourceaddrtable"] = "cSipCfgBindSourceAddrTable"
        self._children_yang_names.add("cSipCfgBindSourceAddrTable")

        self.csipcfgcausestatustable = CiscoSipUaMib.Csipcfgcausestatustable()
        self.csipcfgcausestatustable.parent = self
        self._children_name_map["csipcfgcausestatustable"] = "cSipCfgCauseStatusTable"
        self._children_yang_names.add("cSipCfgCauseStatusTable")

        self.csipcfgearlymediatable = CiscoSipUaMib.Csipcfgearlymediatable()
        self.csipcfgearlymediatable.parent = self
        self._children_name_map["csipcfgearlymediatable"] = "cSipCfgEarlyMediaTable"
        self._children_yang_names.add("cSipCfgEarlyMediaTable")

        self.csipcfgpeer = CiscoSipUaMib.Csipcfgpeer()
        self.csipcfgpeer.parent = self
        self._children_name_map["csipcfgpeer"] = "cSipCfgPeer"
        self._children_yang_names.add("cSipCfgPeer")

        self.csipcfgpeertable = CiscoSipUaMib.Csipcfgpeertable()
        self.csipcfgpeertable.parent = self
        self._children_name_map["csipcfgpeertable"] = "cSipCfgPeerTable"
        self._children_yang_names.add("cSipCfgPeerTable")

        self.csipcfgretry = CiscoSipUaMib.Csipcfgretry()
        self.csipcfgretry.parent = self
        self._children_name_map["csipcfgretry"] = "cSipCfgRetry"
        self._children_yang_names.add("cSipCfgRetry")

        self.csipcfgstatuscausetable = CiscoSipUaMib.Csipcfgstatuscausetable()
        self.csipcfgstatuscausetable.parent = self
        self._children_name_map["csipcfgstatuscausetable"] = "cSipCfgStatusCauseTable"
        self._children_yang_names.add("cSipCfgStatusCauseTable")

        self.csipcfgtimer = CiscoSipUaMib.Csipcfgtimer()
        self.csipcfgtimer.parent = self
        self._children_name_map["csipcfgtimer"] = "cSipCfgTimer"
        self._children_yang_names.add("cSipCfgTimer")

        self.csipcfgvoiceservicevoip = CiscoSipUaMib.Csipcfgvoiceservicevoip()
        self.csipcfgvoiceservicevoip.parent = self
        self._children_name_map["csipcfgvoiceservicevoip"] = "cSipCfgVoiceServiceVoip"
        self._children_yang_names.add("cSipCfgVoiceServiceVoip")

        self.csipstatsconnection = CiscoSipUaMib.Csipstatsconnection()
        self.csipstatsconnection.parent = self
        self._children_name_map["csipstatsconnection"] = "cSipStatsConnection"
        self._children_yang_names.add("cSipStatsConnection")

        self.csipstatserrclient = CiscoSipUaMib.Csipstatserrclient()
        self.csipstatserrclient.parent = self
        self._children_name_map["csipstatserrclient"] = "cSipStatsErrClient"
        self._children_yang_names.add("cSipStatsErrClient")

        self.csipstatserrserver = CiscoSipUaMib.Csipstatserrserver()
        self.csipstatserrserver.parent = self
        self._children_name_map["csipstatserrserver"] = "cSipStatsErrServer"
        self._children_yang_names.add("cSipStatsErrServer")

        self.csipstatsglobalfail = CiscoSipUaMib.Csipstatsglobalfail()
        self.csipstatsglobalfail.parent = self
        self._children_name_map["csipstatsglobalfail"] = "cSipStatsGlobalFail"
        self._children_yang_names.add("cSipStatsGlobalFail")

        self.csipstatsinfo = CiscoSipUaMib.Csipstatsinfo()
        self.csipstatsinfo.parent = self
        self._children_name_map["csipstatsinfo"] = "cSipStatsInfo"
        self._children_yang_names.add("cSipStatsInfo")

        self.csipstatsmisc = CiscoSipUaMib.Csipstatsmisc()
        self.csipstatsmisc.parent = self
        self._children_name_map["csipstatsmisc"] = "cSipStatsMisc"
        self._children_yang_names.add("cSipStatsMisc")

        self.csipstatsredirect = CiscoSipUaMib.Csipstatsredirect()
        self.csipstatsredirect.parent = self
        self._children_name_map["csipstatsredirect"] = "cSipStatsRedirect"
        self._children_yang_names.add("cSipStatsRedirect")

        self.csipstatsretry = CiscoSipUaMib.Csipstatsretry()
        self.csipstatsretry.parent = self
        self._children_name_map["csipstatsretry"] = "cSipStatsRetry"
        self._children_yang_names.add("cSipStatsRetry")

        self.csipstatssuccess = CiscoSipUaMib.Csipstatssuccess()
        self.csipstatssuccess.parent = self
        self._children_name_map["csipstatssuccess"] = "cSipStatsSuccess"
        self._children_yang_names.add("cSipStatsSuccess")

        self.csipstatssuccessoktable = CiscoSipUaMib.Csipstatssuccessoktable()
        self.csipstatssuccessoktable.parent = self
        self._children_name_map["csipstatssuccessoktable"] = "cSipStatsSuccessOkTable"
        self._children_yang_names.add("cSipStatsSuccessOkTable")

        self.csipstatstraffic = CiscoSipUaMib.Csipstatstraffic()
        self.csipstatstraffic.parent = self
        self._children_name_map["csipstatstraffic"] = "cSipStatsTraffic"
        self._children_yang_names.add("cSipStatsTraffic")


    class Csipcfgbase(Entity):
        """
        
        
        .. attribute:: csipcfgbindsrcaddrinterface
        
        	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that  there is no specific source address configured and  in this case the best local IP address will be chosen  by the system
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgbindsrcaddrscope
        
        	This object specifies the scope of packets to which the source IP address of the interface  designated by cSipCfgBindSrcAddrInterface will be bound.  A value of 'all' means the IP address  will be bound to both SIP signalling and media packets. A value of 'control' means the IP address will only be bound to SIP signalling packets.   If cSipCfgBindSrcAddrInterface is set to 0, the value of this object has no meaning
        	**type**\:   :py:class:`Csipcfgbindsrcaddrscope <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase.Csipcfgbindsrcaddrscope>`
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgdnssrvquerystringformat
        
        	This object specifies the format of the prefix used  by the system for DNS SRV queries.  v1  \:  RFC 2052 format \- 'protocol.transport.' v2  \:  RFC 2782 format \- '\_protocol.\_transport.'  This object allows backward compatibility with systems only supporting RFC 2052 format
        	**type**\:   :py:class:`Csipcfgdnssrvquerystringformat <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase.Csipcfgdnssrvquerystringformat>`
        
        .. attribute:: csipcfgmaxforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\:  int
        
        	**range:** 1..70
        
        	**status**\: deprecated
        
        .. attribute:: csipcfgmaximumforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\:  int
        
        	**range:** 1..70
        
        .. attribute:: csipcfgoffercallhold
        
        	This object specifies how the SIP gateway would initiate call hold requests.  directionAttr\: The user agent will use the direction                 attribute such as a=sendonly or a=inactive in                 the sdp to initiate call hold requests.                    connAddr\: The user agent will use 0.0.0.0 connection address            to specify Call Hold
        	**type**\:   :py:class:`Csipcfgoffercallhold <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase.Csipcfgoffercallhold>`
        
        .. attribute:: csipcfgreasonheaderoveride
        
        	This object specifies that the Reason header overrides SIP  status code mapping table
        	**type**\:  bool
        
        .. attribute:: csipcfgredirectiondisabled
        
        	This object specifies how call redirection (3xx) is handled by the user agent.    If 'false', the user agent's treatment of incoming  3xx class response messages is as defined in RFC 2543.   That is, the user agent uses the Contact header(s) from the 3xx response to reinitiate another INVITE transaction to the user's new location.  The call  is redirected.  If 'true', the user agent treats incoming 3xx  response messages as 4xx (client error) class  response messages.  In this case, the call is not redirected, instead it is released with the  appropriate PSTN cause code.  The mapping of SIP 3xx response status codes to 4xx response status codes is as follows\:  300 Multiple Choices \-> 410 Gone  301 Moved Permanently \-> 410 Gone  302 Moved Temporarily \-> 480 Temporarily Unavailable  305 User Proxy        \-> 410 Gone  380 Alternative Service \-> 410 Gone  Any other 3xx \-> 410 Gone
        	**type**\:  bool
        
        .. attribute:: csipcfgsuspendresumeenabled
        
        	This object specifies if support for handling  Suspend/Resume events from the switch is enabled or not.  If 'true', the user agent on getting a Suspend will notify the remote agent by sending it a re\-invite with a hold SDP. Similarly, when the Gateway receives a Resume, it will initiate a re\-invite with the original SDP and unhold the call.  If 'false', the user agent will not initiate any re\-invites on receiving Suspend/Resume events, basically it won't be putting the call on hold or off hold
        	**type**\:  bool
        
        .. attribute:: csipcfgsymnatdirectionrole
        
        	This object specifies the value of the 'a=direction\:<role>' SDP attribute supported by  the user agent.  The direction attribute is used  to describe the role of the user agent (as an  endpoint for a connection\-oriented media stream)  in the connection setup procedure.  none    \:  No role is specified. passive \:  The user agent will advertise itself            as a 'passive' entity (inside the NAT)            in the SDP. active  \:  The user agent will advertise itself            as a 'active' entity (outside the NAT)            in the SDP
        	**type**\:   :py:class:`Csipcfgsymnatdirectionrole <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase.Csipcfgsymnatdirectionrole>`
        
        .. attribute:: csipcfgsymnatenabled
        
        	This object specifies whether remote media checks for Symmetric Network Address Translation (NAT)  is enabled or disabled.  If 'true', remote media checks are enabled.  The gateway will have the ability to open a Real Time  Transport Protocol (RTP) session with the remote end and then update (modify) the existing RTP session's remote address/port (raddr\:rport) with the source address and port of the actual media packet received.  This would be triggered for only those calls where the Session Description Protocol (SDP) received by the gateway has an indication to do so.  If 'false', remote media checks are disabled
        	**type**\:  bool
        
        .. attribute:: csipcfgtransport
        
        	This object specifies the transport protocol the SIP user  agent will use to receive SIP messages.  A value of 'disabled' indicates that the UA will not receive any SIP messages
        	**type**\:   :py:class:`Csipcfgtransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbase.Csipcfgtransport>`
        
        .. attribute:: csipcfguserlocationserveraddr
        
        	This object specifies address of the User Location  Server (ULS) being used to resolve the location of end  points.  This could be a Domain Name Server (DNS) or a  SIP proxy/redirect server.  The format of the address follows the IETF service location  protocol. The syntax is as follows\:     mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching  dial string to a target server. The type\-specific\-syntax is  exactly that, something that the particular mapping scheme can understand.  For example,    Session target           Meaning    ipv4\:171.68.13.55\:1006   The session target is the IP                              version 4 address of 171.68.13.55                              and port 1006.    dns\:pots.cisco.com       The session target is the IP host                              with dns name pots.cisco.com.  The valid Mapping type definitions for the peer follow\:    ipv4  \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z     dns   \- Syntax\: dns\:host.domain
        	**type**\:  str
        
        .. attribute:: csipcfgversion
        
        	This object will reflect the version of SIP supported by this  user agent.  It will follow the same format as SIP version  information contained in the SIP messages generated by this user agent.  For example, user agents supporting SIP version 2 will return 'SIP/2.0' as dictated by RFC 2543
        	**type**\:  str
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgbase, self).__init__()

            self.yang_name = "cSipCfgBase"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgbindsrcaddrinterface = YLeaf(YType.int32, "cSipCfgBindSrcAddrInterface")

            self.csipcfgbindsrcaddrscope = YLeaf(YType.enumeration, "cSipCfgBindSrcAddrScope")

            self.csipcfgdnssrvquerystringformat = YLeaf(YType.enumeration, "cSipCfgDnsSrvQueryStringFormat")

            self.csipcfgmaxforwards = YLeaf(YType.int32, "cSipCfgMaxForwards")

            self.csipcfgmaximumforwards = YLeaf(YType.int32, "cSipCfgMaximumForwards")

            self.csipcfgoffercallhold = YLeaf(YType.enumeration, "cSipCfgOfferCallHold")

            self.csipcfgreasonheaderoveride = YLeaf(YType.boolean, "cSipCfgReasonHeaderOveride")

            self.csipcfgredirectiondisabled = YLeaf(YType.boolean, "cSipCfgRedirectionDisabled")

            self.csipcfgsuspendresumeenabled = YLeaf(YType.boolean, "cSipCfgSuspendResumeEnabled")

            self.csipcfgsymnatdirectionrole = YLeaf(YType.enumeration, "cSipCfgSymNatDirectionRole")

            self.csipcfgsymnatenabled = YLeaf(YType.boolean, "cSipCfgSymNatEnabled")

            self.csipcfgtransport = YLeaf(YType.enumeration, "cSipCfgTransport")

            self.csipcfguserlocationserveraddr = YLeaf(YType.str, "cSipCfgUserLocationServerAddr")

            self.csipcfgversion = YLeaf(YType.str, "cSipCfgVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgbindsrcaddrinterface",
                            "csipcfgbindsrcaddrscope",
                            "csipcfgdnssrvquerystringformat",
                            "csipcfgmaxforwards",
                            "csipcfgmaximumforwards",
                            "csipcfgoffercallhold",
                            "csipcfgreasonheaderoveride",
                            "csipcfgredirectiondisabled",
                            "csipcfgsuspendresumeenabled",
                            "csipcfgsymnatdirectionrole",
                            "csipcfgsymnatenabled",
                            "csipcfgtransport",
                            "csipcfguserlocationserveraddr",
                            "csipcfgversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgbase, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgbase, self).__setattr__(name, value)

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


        def has_data(self):
            return (
                self.csipcfgbindsrcaddrinterface.is_set or
                self.csipcfgbindsrcaddrscope.is_set or
                self.csipcfgdnssrvquerystringformat.is_set or
                self.csipcfgmaxforwards.is_set or
                self.csipcfgmaximumforwards.is_set or
                self.csipcfgoffercallhold.is_set or
                self.csipcfgreasonheaderoveride.is_set or
                self.csipcfgredirectiondisabled.is_set or
                self.csipcfgsuspendresumeenabled.is_set or
                self.csipcfgsymnatdirectionrole.is_set or
                self.csipcfgsymnatenabled.is_set or
                self.csipcfgtransport.is_set or
                self.csipcfguserlocationserveraddr.is_set or
                self.csipcfgversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgbindsrcaddrinterface.yfilter != YFilter.not_set or
                self.csipcfgbindsrcaddrscope.yfilter != YFilter.not_set or
                self.csipcfgdnssrvquerystringformat.yfilter != YFilter.not_set or
                self.csipcfgmaxforwards.yfilter != YFilter.not_set or
                self.csipcfgmaximumforwards.yfilter != YFilter.not_set or
                self.csipcfgoffercallhold.yfilter != YFilter.not_set or
                self.csipcfgreasonheaderoveride.yfilter != YFilter.not_set or
                self.csipcfgredirectiondisabled.yfilter != YFilter.not_set or
                self.csipcfgsuspendresumeenabled.yfilter != YFilter.not_set or
                self.csipcfgsymnatdirectionrole.yfilter != YFilter.not_set or
                self.csipcfgsymnatenabled.yfilter != YFilter.not_set or
                self.csipcfgtransport.yfilter != YFilter.not_set or
                self.csipcfguserlocationserveraddr.yfilter != YFilter.not_set or
                self.csipcfgversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgBase" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgbindsrcaddrinterface.is_set or self.csipcfgbindsrcaddrinterface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgbindsrcaddrinterface.get_name_leafdata())
            if (self.csipcfgbindsrcaddrscope.is_set or self.csipcfgbindsrcaddrscope.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgbindsrcaddrscope.get_name_leafdata())
            if (self.csipcfgdnssrvquerystringformat.is_set or self.csipcfgdnssrvquerystringformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgdnssrvquerystringformat.get_name_leafdata())
            if (self.csipcfgmaxforwards.is_set or self.csipcfgmaxforwards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgmaxforwards.get_name_leafdata())
            if (self.csipcfgmaximumforwards.is_set or self.csipcfgmaximumforwards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgmaximumforwards.get_name_leafdata())
            if (self.csipcfgoffercallhold.is_set or self.csipcfgoffercallhold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgoffercallhold.get_name_leafdata())
            if (self.csipcfgreasonheaderoveride.is_set or self.csipcfgreasonheaderoveride.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgreasonheaderoveride.get_name_leafdata())
            if (self.csipcfgredirectiondisabled.is_set or self.csipcfgredirectiondisabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgredirectiondisabled.get_name_leafdata())
            if (self.csipcfgsuspendresumeenabled.is_set or self.csipcfgsuspendresumeenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgsuspendresumeenabled.get_name_leafdata())
            if (self.csipcfgsymnatdirectionrole.is_set or self.csipcfgsymnatdirectionrole.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgsymnatdirectionrole.get_name_leafdata())
            if (self.csipcfgsymnatenabled.is_set or self.csipcfgsymnatenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgsymnatenabled.get_name_leafdata())
            if (self.csipcfgtransport.is_set or self.csipcfgtransport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtransport.get_name_leafdata())
            if (self.csipcfguserlocationserveraddr.is_set or self.csipcfguserlocationserveraddr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfguserlocationserveraddr.get_name_leafdata())
            if (self.csipcfgversion.is_set or self.csipcfgversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgBindSrcAddrInterface" or name == "cSipCfgBindSrcAddrScope" or name == "cSipCfgDnsSrvQueryStringFormat" or name == "cSipCfgMaxForwards" or name == "cSipCfgMaximumForwards" or name == "cSipCfgOfferCallHold" or name == "cSipCfgReasonHeaderOveride" or name == "cSipCfgRedirectionDisabled" or name == "cSipCfgSuspendResumeEnabled" or name == "cSipCfgSymNatDirectionRole" or name == "cSipCfgSymNatEnabled" or name == "cSipCfgTransport" or name == "cSipCfgUserLocationServerAddr" or name == "cSipCfgVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgBindSrcAddrInterface"):
                self.csipcfgbindsrcaddrinterface = value
                self.csipcfgbindsrcaddrinterface.value_namespace = name_space
                self.csipcfgbindsrcaddrinterface.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgBindSrcAddrScope"):
                self.csipcfgbindsrcaddrscope = value
                self.csipcfgbindsrcaddrscope.value_namespace = name_space
                self.csipcfgbindsrcaddrscope.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgDnsSrvQueryStringFormat"):
                self.csipcfgdnssrvquerystringformat = value
                self.csipcfgdnssrvquerystringformat.value_namespace = name_space
                self.csipcfgdnssrvquerystringformat.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgMaxForwards"):
                self.csipcfgmaxforwards = value
                self.csipcfgmaxforwards.value_namespace = name_space
                self.csipcfgmaxforwards.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgMaximumForwards"):
                self.csipcfgmaximumforwards = value
                self.csipcfgmaximumforwards.value_namespace = name_space
                self.csipcfgmaximumforwards.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgOfferCallHold"):
                self.csipcfgoffercallhold = value
                self.csipcfgoffercallhold.value_namespace = name_space
                self.csipcfgoffercallhold.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgReasonHeaderOveride"):
                self.csipcfgreasonheaderoveride = value
                self.csipcfgreasonheaderoveride.value_namespace = name_space
                self.csipcfgreasonheaderoveride.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRedirectionDisabled"):
                self.csipcfgredirectiondisabled = value
                self.csipcfgredirectiondisabled.value_namespace = name_space
                self.csipcfgredirectiondisabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgSuspendResumeEnabled"):
                self.csipcfgsuspendresumeenabled = value
                self.csipcfgsuspendresumeenabled.value_namespace = name_space
                self.csipcfgsuspendresumeenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgSymNatDirectionRole"):
                self.csipcfgsymnatdirectionrole = value
                self.csipcfgsymnatdirectionrole.value_namespace = name_space
                self.csipcfgsymnatdirectionrole.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgSymNatEnabled"):
                self.csipcfgsymnatenabled = value
                self.csipcfgsymnatenabled.value_namespace = name_space
                self.csipcfgsymnatenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTransport"):
                self.csipcfgtransport = value
                self.csipcfgtransport.value_namespace = name_space
                self.csipcfgtransport.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgUserLocationServerAddr"):
                self.csipcfguserlocationserveraddr = value
                self.csipcfguserlocationserveraddr.value_namespace = name_space
                self.csipcfguserlocationserveraddr.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgVersion"):
                self.csipcfgversion = value
                self.csipcfgversion.value_namespace = name_space
                self.csipcfgversion.value_namespace_prefix = name_space_prefix


    class Csipcfgtimer(Entity):
        """
        
        
        .. attribute:: csipcfgtimerbufferinvite
        
        	This object specifies the amount of time to buffer the INVITE  while waiting for display name info in the Facility.  A value of 0 means that the INVITE wouldn't be buffered waiting for the display name info in the Facility
        	**type**\:  int
        
        	**range:** 0..None \| 50..5000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimercomet
        
        	This object specifies the time a user agent will wait  for a final response before retransmitting the COMET  (COndition MET)
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerconnect
        
        	This object specifies the time a user agent will wait to  receive an ACK confirmation a session is established
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerconnectionaging
        
        	This object specifies the amount of time to wait before  aging out a TCP/UDP connection
        	**type**\:  int
        
        	**range:** 5..30
        
        	**units**\: minutes
        
        .. attribute:: csipcfgtimerdisconnect
        
        	This object specifies the time a user agent will wait to  receive an BYE confirmation a session is disconnected
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerexpires
        
        	This object specifies the time a user agent will wait to  receive a final response to a INVITE before cancelling the  transaction
        	**type**\:  int
        
        	**range:** 60000..300000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerhold
        
        	This object specifies the amount of time to wait before  disconnecting a call already on hold. A value of 0 specifies that this functionality is disabled
        	**type**\:  int
        
        	**range:** 0..None \| 15..2880
        
        	**units**\: minutes
        
        .. attribute:: csipcfgtimerinfo
        
        	This object specifies the amount of time to wait for a 200ok response before retransmitting the Info
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimernotify
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Notify
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerprack
        
        	This object specifies the time a user agent will wait for  a final response before retransmitting the PRACK (PRovisional ACKnowledgment)
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerrefer
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Refer
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimerreliablersp
        
        	This object specifies the amount of time to wait for a PRACK before retransmitting the reliable 1xx response
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        .. attribute:: csipcfgtimersessiontimer
        
        	This object specifies the value of the Min\-SE  header for INVITE messages originated by this  user agent and the minimum value of the  Session\-Expires headers for INVITE messages  received by this user agent.  Any Session\-Expires headers received with a  value below this object's value will be rejected with a 422 client error response message.  Setting this object to a value less than 600 is valid, but the possibly of excessive re\-INVITES  and the impact of those messages should be fully  understood and considered an acceptable risk
        	**type**\:  int
        
        	**range:** 60..86400
        
        	**units**\: seconds
        
        .. attribute:: csipcfgtimertrying
        
        	This object specifies the time a user agent will wait to  receive a provisional response to a INVITE before resending  the INVITE
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: milliseconds
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgtimer, self).__init__()

            self.yang_name = "cSipCfgTimer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgtimerbufferinvite = YLeaf(YType.int32, "cSipCfgTimerBufferInvite")

            self.csipcfgtimercomet = YLeaf(YType.int32, "cSipCfgTimerComet")

            self.csipcfgtimerconnect = YLeaf(YType.int32, "cSipCfgTimerConnect")

            self.csipcfgtimerconnectionaging = YLeaf(YType.int32, "cSipCfgTimerConnectionAging")

            self.csipcfgtimerdisconnect = YLeaf(YType.int32, "cSipCfgTimerDisconnect")

            self.csipcfgtimerexpires = YLeaf(YType.int32, "cSipCfgTimerExpires")

            self.csipcfgtimerhold = YLeaf(YType.int32, "cSipCfgTimerHold")

            self.csipcfgtimerinfo = YLeaf(YType.int32, "cSipCfgTimerInfo")

            self.csipcfgtimernotify = YLeaf(YType.int32, "cSipCfgTimerNotify")

            self.csipcfgtimerprack = YLeaf(YType.int32, "cSipCfgTimerPrack")

            self.csipcfgtimerrefer = YLeaf(YType.int32, "cSipCfgTimerRefer")

            self.csipcfgtimerreliablersp = YLeaf(YType.int32, "cSipCfgTimerReliableRsp")

            self.csipcfgtimersessiontimer = YLeaf(YType.int32, "cSipCfgTimerSessionTimer")

            self.csipcfgtimertrying = YLeaf(YType.int32, "cSipCfgTimerTrying")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgtimerbufferinvite",
                            "csipcfgtimercomet",
                            "csipcfgtimerconnect",
                            "csipcfgtimerconnectionaging",
                            "csipcfgtimerdisconnect",
                            "csipcfgtimerexpires",
                            "csipcfgtimerhold",
                            "csipcfgtimerinfo",
                            "csipcfgtimernotify",
                            "csipcfgtimerprack",
                            "csipcfgtimerrefer",
                            "csipcfgtimerreliablersp",
                            "csipcfgtimersessiontimer",
                            "csipcfgtimertrying") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgtimer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgtimer, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipcfgtimerbufferinvite.is_set or
                self.csipcfgtimercomet.is_set or
                self.csipcfgtimerconnect.is_set or
                self.csipcfgtimerconnectionaging.is_set or
                self.csipcfgtimerdisconnect.is_set or
                self.csipcfgtimerexpires.is_set or
                self.csipcfgtimerhold.is_set or
                self.csipcfgtimerinfo.is_set or
                self.csipcfgtimernotify.is_set or
                self.csipcfgtimerprack.is_set or
                self.csipcfgtimerrefer.is_set or
                self.csipcfgtimerreliablersp.is_set or
                self.csipcfgtimersessiontimer.is_set or
                self.csipcfgtimertrying.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgtimerbufferinvite.yfilter != YFilter.not_set or
                self.csipcfgtimercomet.yfilter != YFilter.not_set or
                self.csipcfgtimerconnect.yfilter != YFilter.not_set or
                self.csipcfgtimerconnectionaging.yfilter != YFilter.not_set or
                self.csipcfgtimerdisconnect.yfilter != YFilter.not_set or
                self.csipcfgtimerexpires.yfilter != YFilter.not_set or
                self.csipcfgtimerhold.yfilter != YFilter.not_set or
                self.csipcfgtimerinfo.yfilter != YFilter.not_set or
                self.csipcfgtimernotify.yfilter != YFilter.not_set or
                self.csipcfgtimerprack.yfilter != YFilter.not_set or
                self.csipcfgtimerrefer.yfilter != YFilter.not_set or
                self.csipcfgtimerreliablersp.yfilter != YFilter.not_set or
                self.csipcfgtimersessiontimer.yfilter != YFilter.not_set or
                self.csipcfgtimertrying.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgTimer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgtimerbufferinvite.is_set or self.csipcfgtimerbufferinvite.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerbufferinvite.get_name_leafdata())
            if (self.csipcfgtimercomet.is_set or self.csipcfgtimercomet.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimercomet.get_name_leafdata())
            if (self.csipcfgtimerconnect.is_set or self.csipcfgtimerconnect.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerconnect.get_name_leafdata())
            if (self.csipcfgtimerconnectionaging.is_set or self.csipcfgtimerconnectionaging.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerconnectionaging.get_name_leafdata())
            if (self.csipcfgtimerdisconnect.is_set or self.csipcfgtimerdisconnect.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerdisconnect.get_name_leafdata())
            if (self.csipcfgtimerexpires.is_set or self.csipcfgtimerexpires.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerexpires.get_name_leafdata())
            if (self.csipcfgtimerhold.is_set or self.csipcfgtimerhold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerhold.get_name_leafdata())
            if (self.csipcfgtimerinfo.is_set or self.csipcfgtimerinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerinfo.get_name_leafdata())
            if (self.csipcfgtimernotify.is_set or self.csipcfgtimernotify.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimernotify.get_name_leafdata())
            if (self.csipcfgtimerprack.is_set or self.csipcfgtimerprack.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerprack.get_name_leafdata())
            if (self.csipcfgtimerrefer.is_set or self.csipcfgtimerrefer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerrefer.get_name_leafdata())
            if (self.csipcfgtimerreliablersp.is_set or self.csipcfgtimerreliablersp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimerreliablersp.get_name_leafdata())
            if (self.csipcfgtimersessiontimer.is_set or self.csipcfgtimersessiontimer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimersessiontimer.get_name_leafdata())
            if (self.csipcfgtimertrying.is_set or self.csipcfgtimertrying.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgtimertrying.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgTimerBufferInvite" or name == "cSipCfgTimerComet" or name == "cSipCfgTimerConnect" or name == "cSipCfgTimerConnectionAging" or name == "cSipCfgTimerDisconnect" or name == "cSipCfgTimerExpires" or name == "cSipCfgTimerHold" or name == "cSipCfgTimerInfo" or name == "cSipCfgTimerNotify" or name == "cSipCfgTimerPrack" or name == "cSipCfgTimerRefer" or name == "cSipCfgTimerReliableRsp" or name == "cSipCfgTimerSessionTimer" or name == "cSipCfgTimerTrying"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgTimerBufferInvite"):
                self.csipcfgtimerbufferinvite = value
                self.csipcfgtimerbufferinvite.value_namespace = name_space
                self.csipcfgtimerbufferinvite.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerComet"):
                self.csipcfgtimercomet = value
                self.csipcfgtimercomet.value_namespace = name_space
                self.csipcfgtimercomet.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerConnect"):
                self.csipcfgtimerconnect = value
                self.csipcfgtimerconnect.value_namespace = name_space
                self.csipcfgtimerconnect.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerConnectionAging"):
                self.csipcfgtimerconnectionaging = value
                self.csipcfgtimerconnectionaging.value_namespace = name_space
                self.csipcfgtimerconnectionaging.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerDisconnect"):
                self.csipcfgtimerdisconnect = value
                self.csipcfgtimerdisconnect.value_namespace = name_space
                self.csipcfgtimerdisconnect.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerExpires"):
                self.csipcfgtimerexpires = value
                self.csipcfgtimerexpires.value_namespace = name_space
                self.csipcfgtimerexpires.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerHold"):
                self.csipcfgtimerhold = value
                self.csipcfgtimerhold.value_namespace = name_space
                self.csipcfgtimerhold.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerInfo"):
                self.csipcfgtimerinfo = value
                self.csipcfgtimerinfo.value_namespace = name_space
                self.csipcfgtimerinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerNotify"):
                self.csipcfgtimernotify = value
                self.csipcfgtimernotify.value_namespace = name_space
                self.csipcfgtimernotify.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerPrack"):
                self.csipcfgtimerprack = value
                self.csipcfgtimerprack.value_namespace = name_space
                self.csipcfgtimerprack.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerRefer"):
                self.csipcfgtimerrefer = value
                self.csipcfgtimerrefer.value_namespace = name_space
                self.csipcfgtimerrefer.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerReliableRsp"):
                self.csipcfgtimerreliablersp = value
                self.csipcfgtimerreliablersp.value_namespace = name_space
                self.csipcfgtimerreliablersp.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerSessionTimer"):
                self.csipcfgtimersessiontimer = value
                self.csipcfgtimersessiontimer.value_namespace = name_space
                self.csipcfgtimersessiontimer.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgTimerTrying"):
                self.csipcfgtimertrying = value
                self.csipcfgtimertrying.value_namespace = name_space
                self.csipcfgtimertrying.value_namespace_prefix = name_space_prefix


    class Csipcfgretry(Entity):
        """
        
        
        .. attribute:: csipcfgretrybye
        
        	This object specifies the number of times a user agent  will retry sending a BYE request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycancel
        
        	This object specifies the number of times a user agent  will retry sending a CANCEL request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycomet
        
        	This object specifies the number of times a user agent  will retry sending a COMET (COndition MET)
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryinfo
        
        	This object specifies the number of times a user agent will retry sending a Info request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryinvite
        
        	This object specifies the number of times a user agent  will retry sending a INVITE request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrynotify
        
        	This object specifies the number of times a user agent  will retry sending a Notify request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryprack
        
        	This object specifies the number of times a user agent  will retry sending a PRACK (PRovisional ACKnowledgement)
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryrefer
        
        	This object specifies the number of times a user agent  will retry sending a Refer request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryregister
        
        	This object specifies the number of times a user agent  will retry sending a REGISTER request
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryreliablersp
        
        	This object specifies the number of times a user agent  will retry sending a reliable response
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryresponse
        
        	This object specifies the number of times a user agent  will retry sending a Response and expecting a ACK
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrysubscribe
        
        	This object specifies the number of times a user agent will retry sending a Subscribe request
        	**type**\:  int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgretry, self).__init__()

            self.yang_name = "cSipCfgRetry"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgretrybye = YLeaf(YType.int32, "cSipCfgRetryBye")

            self.csipcfgretrycancel = YLeaf(YType.int32, "cSipCfgRetryCancel")

            self.csipcfgretrycomet = YLeaf(YType.int32, "cSipCfgRetryComet")

            self.csipcfgretryinfo = YLeaf(YType.int32, "cSipCfgRetryInfo")

            self.csipcfgretryinvite = YLeaf(YType.int32, "cSipCfgRetryInvite")

            self.csipcfgretrynotify = YLeaf(YType.int32, "cSipCfgRetryNotify")

            self.csipcfgretryprack = YLeaf(YType.int32, "cSipCfgRetryPrack")

            self.csipcfgretryrefer = YLeaf(YType.int32, "cSipCfgRetryRefer")

            self.csipcfgretryregister = YLeaf(YType.int32, "cSipCfgRetryRegister")

            self.csipcfgretryreliablersp = YLeaf(YType.int32, "cSipCfgRetryReliableRsp")

            self.csipcfgretryresponse = YLeaf(YType.int32, "cSipCfgRetryResponse")

            self.csipcfgretrysubscribe = YLeaf(YType.int32, "cSipCfgRetrySubscribe")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgretrybye",
                            "csipcfgretrycancel",
                            "csipcfgretrycomet",
                            "csipcfgretryinfo",
                            "csipcfgretryinvite",
                            "csipcfgretrynotify",
                            "csipcfgretryprack",
                            "csipcfgretryrefer",
                            "csipcfgretryregister",
                            "csipcfgretryreliablersp",
                            "csipcfgretryresponse",
                            "csipcfgretrysubscribe") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgretry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgretry, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipcfgretrybye.is_set or
                self.csipcfgretrycancel.is_set or
                self.csipcfgretrycomet.is_set or
                self.csipcfgretryinfo.is_set or
                self.csipcfgretryinvite.is_set or
                self.csipcfgretrynotify.is_set or
                self.csipcfgretryprack.is_set or
                self.csipcfgretryrefer.is_set or
                self.csipcfgretryregister.is_set or
                self.csipcfgretryreliablersp.is_set or
                self.csipcfgretryresponse.is_set or
                self.csipcfgretrysubscribe.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgretrybye.yfilter != YFilter.not_set or
                self.csipcfgretrycancel.yfilter != YFilter.not_set or
                self.csipcfgretrycomet.yfilter != YFilter.not_set or
                self.csipcfgretryinfo.yfilter != YFilter.not_set or
                self.csipcfgretryinvite.yfilter != YFilter.not_set or
                self.csipcfgretrynotify.yfilter != YFilter.not_set or
                self.csipcfgretryprack.yfilter != YFilter.not_set or
                self.csipcfgretryrefer.yfilter != YFilter.not_set or
                self.csipcfgretryregister.yfilter != YFilter.not_set or
                self.csipcfgretryreliablersp.yfilter != YFilter.not_set or
                self.csipcfgretryresponse.yfilter != YFilter.not_set or
                self.csipcfgretrysubscribe.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgRetry" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgretrybye.is_set or self.csipcfgretrybye.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretrybye.get_name_leafdata())
            if (self.csipcfgretrycancel.is_set or self.csipcfgretrycancel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretrycancel.get_name_leafdata())
            if (self.csipcfgretrycomet.is_set or self.csipcfgretrycomet.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretrycomet.get_name_leafdata())
            if (self.csipcfgretryinfo.is_set or self.csipcfgretryinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryinfo.get_name_leafdata())
            if (self.csipcfgretryinvite.is_set or self.csipcfgretryinvite.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryinvite.get_name_leafdata())
            if (self.csipcfgretrynotify.is_set or self.csipcfgretrynotify.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretrynotify.get_name_leafdata())
            if (self.csipcfgretryprack.is_set or self.csipcfgretryprack.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryprack.get_name_leafdata())
            if (self.csipcfgretryrefer.is_set or self.csipcfgretryrefer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryrefer.get_name_leafdata())
            if (self.csipcfgretryregister.is_set or self.csipcfgretryregister.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryregister.get_name_leafdata())
            if (self.csipcfgretryreliablersp.is_set or self.csipcfgretryreliablersp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryreliablersp.get_name_leafdata())
            if (self.csipcfgretryresponse.is_set or self.csipcfgretryresponse.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretryresponse.get_name_leafdata())
            if (self.csipcfgretrysubscribe.is_set or self.csipcfgretrysubscribe.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgretrysubscribe.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgRetryBye" or name == "cSipCfgRetryCancel" or name == "cSipCfgRetryComet" or name == "cSipCfgRetryInfo" or name == "cSipCfgRetryInvite" or name == "cSipCfgRetryNotify" or name == "cSipCfgRetryPrack" or name == "cSipCfgRetryRefer" or name == "cSipCfgRetryRegister" or name == "cSipCfgRetryReliableRsp" or name == "cSipCfgRetryResponse" or name == "cSipCfgRetrySubscribe"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgRetryBye"):
                self.csipcfgretrybye = value
                self.csipcfgretrybye.value_namespace = name_space
                self.csipcfgretrybye.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryCancel"):
                self.csipcfgretrycancel = value
                self.csipcfgretrycancel.value_namespace = name_space
                self.csipcfgretrycancel.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryComet"):
                self.csipcfgretrycomet = value
                self.csipcfgretrycomet.value_namespace = name_space
                self.csipcfgretrycomet.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryInfo"):
                self.csipcfgretryinfo = value
                self.csipcfgretryinfo.value_namespace = name_space
                self.csipcfgretryinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryInvite"):
                self.csipcfgretryinvite = value
                self.csipcfgretryinvite.value_namespace = name_space
                self.csipcfgretryinvite.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryNotify"):
                self.csipcfgretrynotify = value
                self.csipcfgretrynotify.value_namespace = name_space
                self.csipcfgretrynotify.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryPrack"):
                self.csipcfgretryprack = value
                self.csipcfgretryprack.value_namespace = name_space
                self.csipcfgretryprack.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryRefer"):
                self.csipcfgretryrefer = value
                self.csipcfgretryrefer.value_namespace = name_space
                self.csipcfgretryrefer.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryRegister"):
                self.csipcfgretryregister = value
                self.csipcfgretryregister.value_namespace = name_space
                self.csipcfgretryregister.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryReliableRsp"):
                self.csipcfgretryreliablersp = value
                self.csipcfgretryreliablersp.value_namespace = name_space
                self.csipcfgretryreliablersp.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetryResponse"):
                self.csipcfgretryresponse = value
                self.csipcfgretryresponse.value_namespace = name_space
                self.csipcfgretryresponse.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgRetrySubscribe"):
                self.csipcfgretrysubscribe = value
                self.csipcfgretrysubscribe.value_namespace = name_space
                self.csipcfgretrysubscribe.value_namespace_prefix = name_space_prefix


    class Csipcfgpeer(Entity):
        """
        
        
        .. attribute:: csipcfgoutsessiontransport
        
        	This object specifies the session transport  protocol that will be used for outbound SIP  messages.  This configuration is applicable to all dial\-peers in the system having  cSipCfgPeerOutSessionTransport set to 'system'
        	**type**\:   :py:class:`Csipcfgoutsessiontransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeer.Csipcfgoutsessiontransport>`
        
        .. attribute:: csipcfgreliable1xxrsphdr
        
        	This object specifies behavior with respect to Supported or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs
        	**type**\:   :py:class:`Csipcfgreliable1Xxrsphdr <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeer.Csipcfgreliable1Xxrsphdr>`
        
        .. attribute:: csipcfgreliable1xxrspstr
        
        	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgReliable1xxRspHdr
        	**type**\:  str
        
        .. attribute:: csipcfgurltype
        
        	This object specifies the URL type sent in outbound INVITES generated by this device
        	**type**\:   :py:class:`Csipcfgurltype <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeer.Csipcfgurltype>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgpeer, self).__init__()

            self.yang_name = "cSipCfgPeer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgoutsessiontransport = YLeaf(YType.enumeration, "cSipCfgOutSessionTransport")

            self.csipcfgreliable1xxrsphdr = YLeaf(YType.enumeration, "cSipCfgReliable1xxRspHdr")

            self.csipcfgreliable1xxrspstr = YLeaf(YType.str, "cSipCfgReliable1xxRspStr")

            self.csipcfgurltype = YLeaf(YType.enumeration, "cSipCfgUrlType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgoutsessiontransport",
                            "csipcfgreliable1xxrsphdr",
                            "csipcfgreliable1xxrspstr",
                            "csipcfgurltype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgpeer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgpeer, self).__setattr__(name, value)

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


        def has_data(self):
            return (
                self.csipcfgoutsessiontransport.is_set or
                self.csipcfgreliable1xxrsphdr.is_set or
                self.csipcfgreliable1xxrspstr.is_set or
                self.csipcfgurltype.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgoutsessiontransport.yfilter != YFilter.not_set or
                self.csipcfgreliable1xxrsphdr.yfilter != YFilter.not_set or
                self.csipcfgreliable1xxrspstr.yfilter != YFilter.not_set or
                self.csipcfgurltype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgPeer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgoutsessiontransport.is_set or self.csipcfgoutsessiontransport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgoutsessiontransport.get_name_leafdata())
            if (self.csipcfgreliable1xxrsphdr.is_set or self.csipcfgreliable1xxrsphdr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgreliable1xxrsphdr.get_name_leafdata())
            if (self.csipcfgreliable1xxrspstr.is_set or self.csipcfgreliable1xxrspstr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgreliable1xxrspstr.get_name_leafdata())
            if (self.csipcfgurltype.is_set or self.csipcfgurltype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgurltype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgOutSessionTransport" or name == "cSipCfgReliable1xxRspHdr" or name == "cSipCfgReliable1xxRspStr" or name == "cSipCfgUrlType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgOutSessionTransport"):
                self.csipcfgoutsessiontransport = value
                self.csipcfgoutsessiontransport.value_namespace = name_space
                self.csipcfgoutsessiontransport.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgReliable1xxRspHdr"):
                self.csipcfgreliable1xxrsphdr = value
                self.csipcfgreliable1xxrsphdr.value_namespace = name_space
                self.csipcfgreliable1xxrsphdr.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgReliable1xxRspStr"):
                self.csipcfgreliable1xxrspstr = value
                self.csipcfgreliable1xxrspstr.value_namespace = name_space
                self.csipcfgreliable1xxrspstr.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgUrlType"):
                self.csipcfgurltype = value
                self.csipcfgurltype.value_namespace = name_space
                self.csipcfgurltype.value_namespace_prefix = name_space_prefix


    class Csipcfgaaa(Entity):
        """
        
        
        .. attribute:: csipcfgaaausername
        
        	This object specifies the source of the information used to populate the username attribute of AAA billing records
        	**type**\:   :py:class:`Csipcfgaaausername <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgaaa.Csipcfgaaausername>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgaaa, self).__init__()

            self.yang_name = "cSipCfgAaa"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgaaausername = YLeaf(YType.enumeration, "cSipCfgAaaUsername")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgaaausername") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgaaa, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgaaa, self).__setattr__(name, value)

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


        def has_data(self):
            return self.csipcfgaaausername.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgaaausername.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgAaa" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgaaausername.is_set or self.csipcfgaaausername.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgaaausername.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgAaaUsername"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgAaaUsername"):
                self.csipcfgaaausername = value
                self.csipcfgaaausername.value_namespace = name_space
                self.csipcfgaaausername.value_namespace_prefix = name_space_prefix


    class Csipcfgvoiceservicevoip(Entity):
        """
        
        
        .. attribute:: csipcfgheaderpassingenabled
        
        	This object specifies if support for passing SIP headers from Invite, Subscribe, Notify Request to the application is enabled.  If 'true', the headers received in a message will be passed to the application.  If 'false', the headers received in a message will not be passed to the application
        	**type**\:  bool
        
        .. attribute:: csipcfgmaxsubscriptionaccept
        
        	This object specifies the maximum number of concurrent SIP subscriptions a SIP Gateway can accept
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipcfgmaxsubscriptionoriginate
        
        	This object specifies the maximum number of concurrent SIP subscriptions that a SIP Gateway can originate. Default is Max Dialpeers on platform. Maximum is 2\*Max Dialpeers on Platform
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipcfgswitchtransportenabled
        
        	This object specifies if the functionality of switching between transports from udp to tcp if the message size of a Request is greater than 1300 bytes is enabled or not.  This configuration is at the global level, and will only be  considered if there exists no voip dial\-peer
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgvoiceservicevoip, self).__init__()

            self.yang_name = "cSipCfgVoiceServiceVoip"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgheaderpassingenabled = YLeaf(YType.boolean, "cSipCfgHeaderPassingEnabled")

            self.csipcfgmaxsubscriptionaccept = YLeaf(YType.uint32, "cSipCfgMaxSubscriptionAccept")

            self.csipcfgmaxsubscriptionoriginate = YLeaf(YType.uint32, "cSipCfgMaxSubscriptionOriginate")

            self.csipcfgswitchtransportenabled = YLeaf(YType.boolean, "cSipCfgSwitchTransportEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipcfgheaderpassingenabled",
                            "csipcfgmaxsubscriptionaccept",
                            "csipcfgmaxsubscriptionoriginate",
                            "csipcfgswitchtransportenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipcfgvoiceservicevoip, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgvoiceservicevoip, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipcfgheaderpassingenabled.is_set or
                self.csipcfgmaxsubscriptionaccept.is_set or
                self.csipcfgmaxsubscriptionoriginate.is_set or
                self.csipcfgswitchtransportenabled.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipcfgheaderpassingenabled.yfilter != YFilter.not_set or
                self.csipcfgmaxsubscriptionaccept.yfilter != YFilter.not_set or
                self.csipcfgmaxsubscriptionoriginate.yfilter != YFilter.not_set or
                self.csipcfgswitchtransportenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgVoiceServiceVoip" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipcfgheaderpassingenabled.is_set or self.csipcfgheaderpassingenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgheaderpassingenabled.get_name_leafdata())
            if (self.csipcfgmaxsubscriptionaccept.is_set or self.csipcfgmaxsubscriptionaccept.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgmaxsubscriptionaccept.get_name_leafdata())
            if (self.csipcfgmaxsubscriptionoriginate.is_set or self.csipcfgmaxsubscriptionoriginate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgmaxsubscriptionoriginate.get_name_leafdata())
            if (self.csipcfgswitchtransportenabled.is_set or self.csipcfgswitchtransportenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipcfgswitchtransportenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgHeaderPassingEnabled" or name == "cSipCfgMaxSubscriptionAccept" or name == "cSipCfgMaxSubscriptionOriginate" or name == "cSipCfgSwitchTransportEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipCfgHeaderPassingEnabled"):
                self.csipcfgheaderpassingenabled = value
                self.csipcfgheaderpassingenabled.value_namespace = name_space
                self.csipcfgheaderpassingenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgMaxSubscriptionAccept"):
                self.csipcfgmaxsubscriptionaccept = value
                self.csipcfgmaxsubscriptionaccept.value_namespace = name_space
                self.csipcfgmaxsubscriptionaccept.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgMaxSubscriptionOriginate"):
                self.csipcfgmaxsubscriptionoriginate = value
                self.csipcfgmaxsubscriptionoriginate.value_namespace = name_space
                self.csipcfgmaxsubscriptionoriginate.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipCfgSwitchTransportEnabled"):
                self.csipcfgswitchtransportenabled = value
                self.csipcfgswitchtransportenabled.value_namespace = name_space
                self.csipcfgswitchtransportenabled.value_namespace_prefix = name_space_prefix


    class Csipstatsinfo(Entity):
        """
        
        
        .. attribute:: csipstatsinfoforwardedins
        
        	This object reflects the total number of Call Is Being Forwarded (181) responses received by the user agent since system startup. A proxy server may use a Forwarded status code to indicate that the call is being forwarded to a different set of destinations.  Inbound Forwarded responses indicate  to this system that forwarding actions are taking place  with regard to calls initiated by this system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoforwardedouts
        
        	This object reflects the total number of Call Is Being Forwarded (181) responses sent by the user agent since system startup. A proxy server may use a Forwarded status code to indicate that the call is being forwarded to a different set of destinations.  Outbound Forwarded responses indicate this system is taking some forwarding action for calls and conveying that status to the system that initiated the calls
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoqueuedins
        
        	This object reflects the total number of Queued (182) responses received by the user agent since system startup. Inbound Queued responses indicate that the users this system is attempting to call are temporarily unavailable but the SIP agents operating on behalf of those users wish to queue the calls rather than reject them.  When the called parties become available, this system can expect to receive the appropriate final status response.  The Reason\-Phrase from the Queued response messages Status\-Line may give further details about the status of the call.  Multiple  Queued responses to update this system about the status of the queued call my be received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfoqueuedouts
        
        	This object reflects the total number of Queued (182) responses sent by the user agent since system startup. Outbound Queued responses indicate this system has determined that the called party is temporarily unavailable but the call is not rejected.  Rather  the call is queued until the called party becomes available.  Queued responses messages are sent to the system originating the call request to convey the current status of a queued call
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinforingingins
        
        	This object reflects the total number of Ringing (180) responses received by the user agent since system startup. A inbound Ringing response indicates that the UAS processing a INVITE initiated by this system has  found a possible location where the desired end user  has registered recently and is trying to alert the user
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinforingingouts
        
        	This object reflects the total number of Ringing (180) responses sent by the user agent since system startup. A outbound Ringing response indicates that this system has processed an INVITE for a particular end user and found a possible location where that user has registered recently.  The system is trying to alert the end user and is conveying that status to the system that originated the INVITE
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfosessionprogins
        
        	This object reflects the total number of Session Progress (183) responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfosessionprogouts
        
        	This object reflects the total number of Session Progress (183) responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfotryingins
        
        	This object reflects the total number of Trying (100) responses received by the user agent since system startup.   Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Inbound Trying responses indicate that outbound INVITE request  sent out by this system have been received and are processed
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfotryingouts
        
        	This object reflects the total number of Trying (100) responses sent by the user agent since system startup. Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Outbound Trying responses indicate this system is successfully  receiving INVITE requests and processing them on  behalf of the system initiating the INVITE
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsinfo, self).__init__()

            self.yang_name = "cSipStatsInfo"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsinfoforwardedins = YLeaf(YType.uint32, "cSipStatsInfoForwardedIns")

            self.csipstatsinfoforwardedouts = YLeaf(YType.uint32, "cSipStatsInfoForwardedOuts")

            self.csipstatsinfoqueuedins = YLeaf(YType.uint32, "cSipStatsInfoQueuedIns")

            self.csipstatsinfoqueuedouts = YLeaf(YType.uint32, "cSipStatsInfoQueuedOuts")

            self.csipstatsinforingingins = YLeaf(YType.uint32, "cSipStatsInfoRingingIns")

            self.csipstatsinforingingouts = YLeaf(YType.uint32, "cSipStatsInfoRingingOuts")

            self.csipstatsinfosessionprogins = YLeaf(YType.uint32, "cSipStatsInfoSessionProgIns")

            self.csipstatsinfosessionprogouts = YLeaf(YType.uint32, "cSipStatsInfoSessionProgOuts")

            self.csipstatsinfotryingins = YLeaf(YType.uint32, "cSipStatsInfoTryingIns")

            self.csipstatsinfotryingouts = YLeaf(YType.uint32, "cSipStatsInfoTryingOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsinfoforwardedins",
                            "csipstatsinfoforwardedouts",
                            "csipstatsinfoqueuedins",
                            "csipstatsinfoqueuedouts",
                            "csipstatsinforingingins",
                            "csipstatsinforingingouts",
                            "csipstatsinfosessionprogins",
                            "csipstatsinfosessionprogouts",
                            "csipstatsinfotryingins",
                            "csipstatsinfotryingouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsinfo, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsinfo, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsinfoforwardedins.is_set or
                self.csipstatsinfoforwardedouts.is_set or
                self.csipstatsinfoqueuedins.is_set or
                self.csipstatsinfoqueuedouts.is_set or
                self.csipstatsinforingingins.is_set or
                self.csipstatsinforingingouts.is_set or
                self.csipstatsinfosessionprogins.is_set or
                self.csipstatsinfosessionprogouts.is_set or
                self.csipstatsinfotryingins.is_set or
                self.csipstatsinfotryingouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsinfoforwardedins.yfilter != YFilter.not_set or
                self.csipstatsinfoforwardedouts.yfilter != YFilter.not_set or
                self.csipstatsinfoqueuedins.yfilter != YFilter.not_set or
                self.csipstatsinfoqueuedouts.yfilter != YFilter.not_set or
                self.csipstatsinforingingins.yfilter != YFilter.not_set or
                self.csipstatsinforingingouts.yfilter != YFilter.not_set or
                self.csipstatsinfosessionprogins.yfilter != YFilter.not_set or
                self.csipstatsinfosessionprogouts.yfilter != YFilter.not_set or
                self.csipstatsinfotryingins.yfilter != YFilter.not_set or
                self.csipstatsinfotryingouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsInfo" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsinfoforwardedins.is_set or self.csipstatsinfoforwardedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfoforwardedins.get_name_leafdata())
            if (self.csipstatsinfoforwardedouts.is_set or self.csipstatsinfoforwardedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfoforwardedouts.get_name_leafdata())
            if (self.csipstatsinfoqueuedins.is_set or self.csipstatsinfoqueuedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfoqueuedins.get_name_leafdata())
            if (self.csipstatsinfoqueuedouts.is_set or self.csipstatsinfoqueuedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfoqueuedouts.get_name_leafdata())
            if (self.csipstatsinforingingins.is_set or self.csipstatsinforingingins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinforingingins.get_name_leafdata())
            if (self.csipstatsinforingingouts.is_set or self.csipstatsinforingingouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinforingingouts.get_name_leafdata())
            if (self.csipstatsinfosessionprogins.is_set or self.csipstatsinfosessionprogins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfosessionprogins.get_name_leafdata())
            if (self.csipstatsinfosessionprogouts.is_set or self.csipstatsinfosessionprogouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfosessionprogouts.get_name_leafdata())
            if (self.csipstatsinfotryingins.is_set or self.csipstatsinfotryingins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfotryingins.get_name_leafdata())
            if (self.csipstatsinfotryingouts.is_set or self.csipstatsinfotryingouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsinfotryingouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsInfoForwardedIns" or name == "cSipStatsInfoForwardedOuts" or name == "cSipStatsInfoQueuedIns" or name == "cSipStatsInfoQueuedOuts" or name == "cSipStatsInfoRingingIns" or name == "cSipStatsInfoRingingOuts" or name == "cSipStatsInfoSessionProgIns" or name == "cSipStatsInfoSessionProgOuts" or name == "cSipStatsInfoTryingIns" or name == "cSipStatsInfoTryingOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsInfoForwardedIns"):
                self.csipstatsinfoforwardedins = value
                self.csipstatsinfoforwardedins.value_namespace = name_space
                self.csipstatsinfoforwardedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoForwardedOuts"):
                self.csipstatsinfoforwardedouts = value
                self.csipstatsinfoforwardedouts.value_namespace = name_space
                self.csipstatsinfoforwardedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoQueuedIns"):
                self.csipstatsinfoqueuedins = value
                self.csipstatsinfoqueuedins.value_namespace = name_space
                self.csipstatsinfoqueuedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoQueuedOuts"):
                self.csipstatsinfoqueuedouts = value
                self.csipstatsinfoqueuedouts.value_namespace = name_space
                self.csipstatsinfoqueuedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoRingingIns"):
                self.csipstatsinforingingins = value
                self.csipstatsinforingingins.value_namespace = name_space
                self.csipstatsinforingingins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoRingingOuts"):
                self.csipstatsinforingingouts = value
                self.csipstatsinforingingouts.value_namespace = name_space
                self.csipstatsinforingingouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoSessionProgIns"):
                self.csipstatsinfosessionprogins = value
                self.csipstatsinfosessionprogins.value_namespace = name_space
                self.csipstatsinfosessionprogins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoSessionProgOuts"):
                self.csipstatsinfosessionprogouts = value
                self.csipstatsinfosessionprogouts.value_namespace = name_space
                self.csipstatsinfosessionprogouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoTryingIns"):
                self.csipstatsinfotryingins = value
                self.csipstatsinfotryingins.value_namespace = name_space
                self.csipstatsinfotryingins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsInfoTryingOuts"):
                self.csipstatsinfotryingouts = value
                self.csipstatsinfotryingouts.value_namespace = name_space
                self.csipstatsinfotryingouts.value_namespace_prefix = name_space_prefix


    class Csipstatssuccess(Entity):
        """
        
        
        .. attribute:: csipstatssuccessacceptedins
        
        	This object reflects the total number of Accepted (202) responses received by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessacceptedouts
        
        	This object reflects the total number of Accepted (202) responses sent by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessokins
        
        	This object reflects the total number of Ok (200) responses received by the user agent since system startup. The meaning of inbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: csipstatssuccessokouts
        
        	This object reflects the total number of Ok (200) responses sent by the user agent since system startup. The meaning of outbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatssuccess, self).__init__()

            self.yang_name = "cSipStatsSuccess"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatssuccessacceptedins = YLeaf(YType.uint32, "cSipStatsSuccessAcceptedIns")

            self.csipstatssuccessacceptedouts = YLeaf(YType.uint32, "cSipStatsSuccessAcceptedOuts")

            self.csipstatssuccessokins = YLeaf(YType.uint32, "cSipStatsSuccessOkIns")

            self.csipstatssuccessokouts = YLeaf(YType.uint32, "cSipStatsSuccessOkOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatssuccessacceptedins",
                            "csipstatssuccessacceptedouts",
                            "csipstatssuccessokins",
                            "csipstatssuccessokouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatssuccess, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatssuccess, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatssuccessacceptedins.is_set or
                self.csipstatssuccessacceptedouts.is_set or
                self.csipstatssuccessokins.is_set or
                self.csipstatssuccessokouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatssuccessacceptedins.yfilter != YFilter.not_set or
                self.csipstatssuccessacceptedouts.yfilter != YFilter.not_set or
                self.csipstatssuccessokins.yfilter != YFilter.not_set or
                self.csipstatssuccessokouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsSuccess" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatssuccessacceptedins.is_set or self.csipstatssuccessacceptedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatssuccessacceptedins.get_name_leafdata())
            if (self.csipstatssuccessacceptedouts.is_set or self.csipstatssuccessacceptedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatssuccessacceptedouts.get_name_leafdata())
            if (self.csipstatssuccessokins.is_set or self.csipstatssuccessokins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatssuccessokins.get_name_leafdata())
            if (self.csipstatssuccessokouts.is_set or self.csipstatssuccessokouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatssuccessokouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsSuccessAcceptedIns" or name == "cSipStatsSuccessAcceptedOuts" or name == "cSipStatsSuccessOkIns" or name == "cSipStatsSuccessOkOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsSuccessAcceptedIns"):
                self.csipstatssuccessacceptedins = value
                self.csipstatssuccessacceptedins.value_namespace = name_space
                self.csipstatssuccessacceptedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsSuccessAcceptedOuts"):
                self.csipstatssuccessacceptedouts = value
                self.csipstatssuccessacceptedouts.value_namespace = name_space
                self.csipstatssuccessacceptedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsSuccessOkIns"):
                self.csipstatssuccessokins = value
                self.csipstatssuccessokins.value_namespace = name_space
                self.csipstatssuccessokins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsSuccessOkOuts"):
                self.csipstatssuccessokouts = value
                self.csipstatssuccessokouts.value_namespace = name_space
                self.csipstatssuccessokouts.value_namespace_prefix = name_space_prefix


    class Csipstatsredirect(Entity):
        """
        
        
        .. attribute:: csipstatsrediraltservices
        
        	This object reflects the total number of Alternative Service (380) responses received by the user agent since system startup. Alternative Service responses indicate that the call was not successful, but alternative services are possible.  Those alternative services are described in the message body of the response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedperms
        
        	This object reflects the total number of Moved  Permanently (301) responses received by the user agent since system startup. Moved Permanently responses indicate that the called party  can no longer be found at the address offered in the request  and the requesting UAC should retry at the new address given  by the Contact header field of the response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtemps
        
        	This object reflects the total number of Moved  Temporarily (302) responses received by the user agent since system startup. Moved Temporarily responses indicate the UAC should retry the request directed at the new address(es) given by the Contact header field of the response. The duration of this redirection can be indicated through the Expires header.  If no explicit expiration time is given, the new address(es) are only valid for this call
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: csipstatsredirmovedtempsins
        
        	This object reflects the total number of Moved Temporarily (302) responses received by the user agent since system startup.  Moved Temporarily responses indicate the UAC should retry the request directed at the new address(es)  given by the Contact header field of the response. The duration of this redirection can be indicated through the Expires header.  If no explicit expiration time is given, the new address(es) are only valid for this call
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtempsouts
        
        	This object reflects the total number of Moved Temporarily (302) responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmultiplechoices
        
        	This object reflects the total number of Multiple Choices (300) responses received by the user agent since system startup. Multiple Choices responses indicate that the called party can be reached at several different locations and the server cannot or prefers not to proxy the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirseeothers
        
        	This object reflects the total number of See Other  (303) responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsrediruseproxys
        
        	This object reflects the total number of Use Proxy  (305) responses received by the user agent since system startup. See Other responses indicate that requested resources must be accessed through the proxy given by the  Contact header field of the response.  The recipient of this response is expected to repeat this single request via the proxy
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsredirect, self).__init__()

            self.yang_name = "cSipStatsRedirect"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsrediraltservices = YLeaf(YType.uint32, "cSipStatsRedirAltServices")

            self.csipstatsredirmovedperms = YLeaf(YType.uint32, "cSipStatsRedirMovedPerms")

            self.csipstatsredirmovedtemps = YLeaf(YType.uint32, "cSipStatsRedirMovedTemps")

            self.csipstatsredirmovedtempsins = YLeaf(YType.uint32, "cSipStatsRedirMovedTempsIns")

            self.csipstatsredirmovedtempsouts = YLeaf(YType.uint32, "cSipStatsRedirMovedTempsOuts")

            self.csipstatsredirmultiplechoices = YLeaf(YType.uint32, "cSipStatsRedirMultipleChoices")

            self.csipstatsredirseeothers = YLeaf(YType.uint32, "cSipStatsRedirSeeOthers")

            self.csipstatsrediruseproxys = YLeaf(YType.uint32, "cSipStatsRedirUseProxys")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsrediraltservices",
                            "csipstatsredirmovedperms",
                            "csipstatsredirmovedtemps",
                            "csipstatsredirmovedtempsins",
                            "csipstatsredirmovedtempsouts",
                            "csipstatsredirmultiplechoices",
                            "csipstatsredirseeothers",
                            "csipstatsrediruseproxys") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsredirect, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsredirect, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsrediraltservices.is_set or
                self.csipstatsredirmovedperms.is_set or
                self.csipstatsredirmovedtemps.is_set or
                self.csipstatsredirmovedtempsins.is_set or
                self.csipstatsredirmovedtempsouts.is_set or
                self.csipstatsredirmultiplechoices.is_set or
                self.csipstatsredirseeothers.is_set or
                self.csipstatsrediruseproxys.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsrediraltservices.yfilter != YFilter.not_set or
                self.csipstatsredirmovedperms.yfilter != YFilter.not_set or
                self.csipstatsredirmovedtemps.yfilter != YFilter.not_set or
                self.csipstatsredirmovedtempsins.yfilter != YFilter.not_set or
                self.csipstatsredirmovedtempsouts.yfilter != YFilter.not_set or
                self.csipstatsredirmultiplechoices.yfilter != YFilter.not_set or
                self.csipstatsredirseeothers.yfilter != YFilter.not_set or
                self.csipstatsrediruseproxys.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsRedirect" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsrediraltservices.is_set or self.csipstatsrediraltservices.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsrediraltservices.get_name_leafdata())
            if (self.csipstatsredirmovedperms.is_set or self.csipstatsredirmovedperms.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirmovedperms.get_name_leafdata())
            if (self.csipstatsredirmovedtemps.is_set or self.csipstatsredirmovedtemps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirmovedtemps.get_name_leafdata())
            if (self.csipstatsredirmovedtempsins.is_set or self.csipstatsredirmovedtempsins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirmovedtempsins.get_name_leafdata())
            if (self.csipstatsredirmovedtempsouts.is_set or self.csipstatsredirmovedtempsouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirmovedtempsouts.get_name_leafdata())
            if (self.csipstatsredirmultiplechoices.is_set or self.csipstatsredirmultiplechoices.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirmultiplechoices.get_name_leafdata())
            if (self.csipstatsredirseeothers.is_set or self.csipstatsredirseeothers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsredirseeothers.get_name_leafdata())
            if (self.csipstatsrediruseproxys.is_set or self.csipstatsrediruseproxys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsrediruseproxys.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsRedirAltServices" or name == "cSipStatsRedirMovedPerms" or name == "cSipStatsRedirMovedTemps" or name == "cSipStatsRedirMovedTempsIns" or name == "cSipStatsRedirMovedTempsOuts" or name == "cSipStatsRedirMultipleChoices" or name == "cSipStatsRedirSeeOthers" or name == "cSipStatsRedirUseProxys"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsRedirAltServices"):
                self.csipstatsrediraltservices = value
                self.csipstatsrediraltservices.value_namespace = name_space
                self.csipstatsrediraltservices.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirMovedPerms"):
                self.csipstatsredirmovedperms = value
                self.csipstatsredirmovedperms.value_namespace = name_space
                self.csipstatsredirmovedperms.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirMovedTemps"):
                self.csipstatsredirmovedtemps = value
                self.csipstatsredirmovedtemps.value_namespace = name_space
                self.csipstatsredirmovedtemps.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirMovedTempsIns"):
                self.csipstatsredirmovedtempsins = value
                self.csipstatsredirmovedtempsins.value_namespace = name_space
                self.csipstatsredirmovedtempsins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirMovedTempsOuts"):
                self.csipstatsredirmovedtempsouts = value
                self.csipstatsredirmovedtempsouts.value_namespace = name_space
                self.csipstatsredirmovedtempsouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirMultipleChoices"):
                self.csipstatsredirmultiplechoices = value
                self.csipstatsredirmultiplechoices.value_namespace = name_space
                self.csipstatsredirmultiplechoices.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirSeeOthers"):
                self.csipstatsredirseeothers = value
                self.csipstatsredirseeothers.value_namespace = name_space
                self.csipstatsredirseeothers.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRedirUseProxys"):
                self.csipstatsrediruseproxys = value
                self.csipstatsrediruseproxys.value_namespace = name_space
                self.csipstatsrediruseproxys.value_namespace_prefix = name_space_prefix


    class Csipstatserrclient(Entity):
        """
        
        
        .. attribute:: csipstatsclientaddrincompleteins
        
        	This object reflects the total number of Address Incomplete  (484) responses received by the user agent since system startup. Inbound Address Incomplete responses indicate that requests  issued by this system had To addresses or Request\-URIs that  were incomplete
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientaddrincompleteouts
        
        	This object reflects the total number of Address Incomplete  (484) responses sent by the user agent since system startup. Outbound Address Incomplete responses indicate that requests  received by this system had To addresses or Request\-URIs that  were incomplete
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientambiguousins
        
        	This object reflects the total number of Ambiguous (485)  responses received by the user agent since system startup. Inbound Ambiguous responses indicate that requests issued by this system provided ambiguous address information
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientambiguousouts
        
        	This object reflects the total number of Ambiguous (485)  responses sent by the user agent since system startup. Outbound Ambiguous responses indicate that requests received by this system contained ambiguous address information
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadeventins
        
        	This object reflects the total number of BadEvent (489)  responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadeventouts
        
        	This object reflects the total number of BadEvent (489)  responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadextensionins
        
        	This object reflects the total number of Bad Extension (420)  responses received by the user agent since system startup. Inbound Bad Extension responses indicate that the recipient  did not understand the protocol extension specified in a  Require header field
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadextensionouts
        
        	This object reflects the total number of Bad Extension (420)  responses sent by the user agent since system startup. Outbound Bad Extension responses indicate that this system did not understand the protocol extension specified in a Require header field of requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadrequestins
        
        	This object reflects the total number of Bad Request (400)  responses received by the user agent since system startup. Inbound Bad Request responses indicate that requests issued  by this system could not be understood due to malformed  syntax
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadrequestouts
        
        	This object reflects the total number of Bad Request (400)  responses sent by the user agent since system startup. Outbound Bad Request responses indicate that requests  received by this system could not be understood due to  malformed syntax
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbusyhereins
        
        	This object reflects the total number of Busy Here (486)  responses received by the user agent since system startup. Inbound Busy Here responses indicate that the called party is currently not willing or not able to take additional calls
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbusyhereouts
        
        	This object reflects the total number of Busy Here (486)  responses sent by the user agent since system startup. Outbound Busy Here responses indicate that the called party's end system was contacted successfully but the called party is currently not willing or able to take  additional calls
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientcalllegnoexistins
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses received by the user agent since system startup. Inbound Call Leg/Transaction Does Not Exist responses indicate that either BYE or CANCEL requests issued by this system were  received by a server and not matching call leg or transaction  existed
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientcalllegnoexistouts
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses sent by the user agent since system startup. Outbound Call Leg/Transaction Does Not Exist responses  indicate that BYE or CANCEL requests have been received by  this system and not call leg or transaction matching that  request exists
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientconflictins
        
        	This object reflects the total number of Conflict (409)  responses received by the user agent since system startup. Inbound Conflict responses indicate that requests issued by this system could not be completed due to a conflict with the current state of a requested resource
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientconflictouts
        
        	This object reflects the total number of Conflict (409)  responses sent by the user agent since system startup. Outbound Conflict responses indicate that requests received by this system could not be completed due to a conflict with the current state of a requested resource
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientforbiddenins
        
        	This object reflects the total number of Forbidden (403)  responses received by the user agent since system startup. Inbound Forbidden responses indicate that requests issued by this system are understood by the server but the server refuses to fulfill the request.  Authorization will not help and the requests should not be repeated
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientforbiddenouts
        
        	This object reflects the total number of Forbidden (403)  responses sent by the user agent since system startup. Outbound Forbidden responses indicate that requests received by this system are understood but this system is refusing to fulfill the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientgoneins
        
        	This object reflects the total number of Gone (410)  responses received by the user agent since system startup. Inbound Gone responses indicate that resources requested by this system are no longer available at the recipient server and no forwarding address is known
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientgoneouts
        
        	This object reflects the total number of Gone (410)  responses sent by the user agent since system startup. Outbound Gone responses indicate that the requested resources are no longer available at this system and no forwarding address is known
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientlengthrequiredins
        
        	This object reflects the total number of Length Required  (411) responses received by the user agent since system startup. Inbound Length Required responses indicate that requests  issued by this system are being refused by servers because  of no defined Content\-Length header field
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsclientlengthrequiredouts
        
        	This object reflects the total number of Length Required  (411) responses sent by the user agent since system startup. Outbound Length Required responses indicate that requests  received by this system are being refused because of no  defined Content\-Length header field
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: csipstatsclientloopdetectedins
        
        	This object reflects the total number of Loop Detected (482)  responses received by the user agent since system startup. Inbound Loop Detected responses indicate that requests issued by this system were received at servers and the server found  itself in the Via path more than once
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientloopdetectedouts
        
        	This object reflects the total number of Loop Detected (482)  responses sent by the user agent since system startup. Outbound Loop Detected responses indicate that requests  received by this system contain a Via path with this system  appearing more than once
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientmethnotallowedins
        
        	This object reflects the total number of Method Not Allowed  (405) received responses by the user agent. Inbound Method Not Allowed responses indicate that requests  issued by this system have specified a SIP method in the  Request\-Line that is not allowed for the address identified  by the Request\-URI
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientmethnotallowedouts
        
        	This object reflects the total number of Method Not Allowed  (405) received sent by the user agent since system startup. Outbound Method Not Allowed responses indicate that requests  received by this system have SIP methods specified in the  Request\-Line that are not allowed for the address identified  by the Request\-URI
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnoaccepthereins
        
        	This object reflects the total number of Not Acceptable Here (488) responses received by the user agent since system startup. The response has the same meaning as 606 (Not Acceptable),  but only applies to the specific entity addressed by the  Request\-URI and the request may succeed elsewhere
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnoaccepthereouts
        
        	This object reflects the total number of Not Acceptable Here (488) responses sent by the user agent since system startup. The response has the same meaning as 606 (Not Acceptable),  but only applies to the specific entity addressed by the  Request\-URI and the request may succeed elsewhere
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnosupmediatypeins
        
        	This object reflects the total number of Unsupported Media  Type (415) responses received by the user agent since system startup. Inbound Unsupported Media Type responses indicate that  requests issued by this system are being refused because the  message body of the request is in a format not supported by  the requested resource for the requested method
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnosupmediatypeouts
        
        	This object reflects the total number of Unsupported Media  Type (415) responses sent by the user agent since system startup. Outbound Unsupported Media Type responses indicate that the  body of requests received by this system are in a format not  supported by the requested resource for the requested method
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotacceptableins
        
        	This object reflects the total number of Not Acceptable  (406) responses received by the user agent since system startup. Inbound Not Acceptable responses indicate the resources  identified by requests issued by this system cannot generate  responses with content characteristics acceptable to this  system according to the accept headers sent in the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotacceptableouts
        
        	This object reflects the total number of Not Acceptable (406)  responses sent by the user agent since system startup. Outbound Not Acceptable responses indicate that the resources identified by requests received by this system cannot generate responses with content characteristics acceptable to the  system sending the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotfoundins
        
        	This object reflects the total number of Not Found (404)  responses received by the user agent since system startup. Inbound Not Found responses indicate that the called party  does not exist at the domain specified in the Request\-URI  or the domain is not handled by the recipient of the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotfoundouts
        
        	This object reflects the total number of Not Found (404)  responses sent by the user agent since system startup. Outbound Not Found responses indicate that this system knows that the called party does not exist at the domain specified in the Request\-URI or the domain is not handled by this system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientpaymentreqdins
        
        	This object reflects the total number of Payment Required  (402) responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientpaymentreqdouts
        
        	This object reflects the total number of Payment Required  (402) responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientproxyauthreqdins
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses received by the user agent since system startup. Inbound Proxy Authentication Required responses indicate that  this system must authenticate itself with the proxy before  gaining access to the requested resource
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientproxyauthreqdouts
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses sent by the user agent since system startup. Outbound Proxy Authentication Required responses indicate that the systems issuing requests being processed by this system  must authenticate themselves with this system before gaining  access to requested resources
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqenttoolargeins
        
        	This object reflects the total number of Request Entity Too  Large (413) responses received by the user agent since system startup. Inbound Request Entity Too Large responses indicate that  requests issued by this system are being refused because  the request is larger than the server is willing or able to  process
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqenttoolargeouts
        
        	This object reflects the total number of Request Entity Too  Large (413) responses sent by the user agent since system startup. Outbound Request Entity Too Large responses indicate that  requests received by this system are larger than this system  is willing or able to process
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqpendingins
        
        	This object reflects the total number of RequestPending (491) responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqpendingouts
        
        	This object reflects the total number of RequestPending (491) responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtermins
        
        	This object reflects the total number of Request Terminated  (487) responses received by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtermouts
        
        	This object reflects the total number of Request Terminated  (487) responses sent by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtimeoutins
        
        	This object reflects the total number of Request Timeout  (408) responses received by the user agent since system startup. Inbound Request Timeout responses indicate that requests  issued by this system are not being processed by the server  within the time indicated in the Expires header of the  request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtimeoutouts
        
        	This object reflects the total number of Request Timeout  (408) responses sent by the user agent since system startup. Outbound Request Timeout responses indicate that this  system is not able to produce an appropriate response within  the time indicated in the Expires header of the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientrequritoolargeins
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses received by the user agent since system startup. Inbound Request\-URI Too Large responses indicate that  requests issued by this system are being refused because the  Request\-URI is longer than the server is willing or able to  interpret
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientrequritoolargeouts
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses sent by the user agent since system startup. Outbound Request\-URI Too Large responses indicate that  Request\-URIs received by this system are longer than this  system is willing or able to interpret
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientsttoosmallins
        
        	This object reflects the total number of SessionTimerTooSmall (422) responses received by the user agent since system  startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientsttoosmallouts
        
        	This object reflects the total number of SessionTimerTooSmall (422) responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttempnotavailins
        
        	This object reflects the total number of Temporarily Not  Available (480) responses received by the user agent since system startup. Inbound Temporarily Not Available responses indicate that  the called party is currently unavailable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttempnotavailouts
        
        	This object reflects the total number of Temporarily Not  Available (480) responses sent by the user agent since system startup. Outbound Temporarily Not Available responses indicate that  the called party's end system was contacted successfully but  the called party is currently unavailable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttoomanyhopsins
        
        	This object reflects the total number of Too Many Hops (483)  responses received by the user agent since system startup. Inbound Too Many Hops responses indicate that requests issued by this system contain more Via entries (hops) than allowed by the Max\-Forwards header field of the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttoomanyhopsouts
        
        	This object reflects the total number of Too Many Hops (483)  responses sent by the user agent since system startup. Outbound Too Many Hops responses indicate that requests received by this system contain more Via entries (hops) than are allowed by the Max\-Forwards header field of the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientunauthorizedins
        
        	This object reflects the total number of Unauthorized (401)  responses received by the user agent since system startup.   Inbound Unauthorized responses indicate that requests issued  by this system require user authentication
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientunauthorizedouts
        
        	This object reflects the total number of Unauthorized (401)  responses sent by the user agent since system startup. Outbound Unauthorized responses indicate that requests  received by this system require user authentication
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatserrclient, self).__init__()

            self.yang_name = "cSipStatsErrClient"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsclientaddrincompleteins = YLeaf(YType.uint32, "cSipStatsClientAddrIncompleteIns")

            self.csipstatsclientaddrincompleteouts = YLeaf(YType.uint32, "cSipStatsClientAddrIncompleteOuts")

            self.csipstatsclientambiguousins = YLeaf(YType.uint32, "cSipStatsClientAmbiguousIns")

            self.csipstatsclientambiguousouts = YLeaf(YType.uint32, "cSipStatsClientAmbiguousOuts")

            self.csipstatsclientbadeventins = YLeaf(YType.uint32, "cSipStatsClientBadEventIns")

            self.csipstatsclientbadeventouts = YLeaf(YType.uint32, "cSipStatsClientBadEventOuts")

            self.csipstatsclientbadextensionins = YLeaf(YType.uint32, "cSipStatsClientBadExtensionIns")

            self.csipstatsclientbadextensionouts = YLeaf(YType.uint32, "cSipStatsClientBadExtensionOuts")

            self.csipstatsclientbadrequestins = YLeaf(YType.uint32, "cSipStatsClientBadRequestIns")

            self.csipstatsclientbadrequestouts = YLeaf(YType.uint32, "cSipStatsClientBadRequestOuts")

            self.csipstatsclientbusyhereins = YLeaf(YType.uint32, "cSipStatsClientBusyHereIns")

            self.csipstatsclientbusyhereouts = YLeaf(YType.uint32, "cSipStatsClientBusyHereOuts")

            self.csipstatsclientcalllegnoexistins = YLeaf(YType.uint32, "cSipStatsClientCallLegNoExistIns")

            self.csipstatsclientcalllegnoexistouts = YLeaf(YType.uint32, "cSipStatsClientCallLegNoExistOuts")

            self.csipstatsclientconflictins = YLeaf(YType.uint32, "cSipStatsClientConflictIns")

            self.csipstatsclientconflictouts = YLeaf(YType.uint32, "cSipStatsClientConflictOuts")

            self.csipstatsclientforbiddenins = YLeaf(YType.uint32, "cSipStatsClientForbiddenIns")

            self.csipstatsclientforbiddenouts = YLeaf(YType.uint32, "cSipStatsClientForbiddenOuts")

            self.csipstatsclientgoneins = YLeaf(YType.uint32, "cSipStatsClientGoneIns")

            self.csipstatsclientgoneouts = YLeaf(YType.uint32, "cSipStatsClientGoneOuts")

            self.csipstatsclientlengthrequiredins = YLeaf(YType.uint32, "cSipStatsClientLengthRequiredIns")

            self.csipstatsclientlengthrequiredouts = YLeaf(YType.uint32, "cSipStatsClientLengthRequiredOuts")

            self.csipstatsclientloopdetectedins = YLeaf(YType.uint32, "cSipStatsClientLoopDetectedIns")

            self.csipstatsclientloopdetectedouts = YLeaf(YType.uint32, "cSipStatsClientLoopDetectedOuts")

            self.csipstatsclientmethnotallowedins = YLeaf(YType.uint32, "cSipStatsClientMethNotAllowedIns")

            self.csipstatsclientmethnotallowedouts = YLeaf(YType.uint32, "cSipStatsClientMethNotAllowedOuts")

            self.csipstatsclientnoaccepthereins = YLeaf(YType.uint32, "cSipStatsClientNoAcceptHereIns")

            self.csipstatsclientnoaccepthereouts = YLeaf(YType.uint32, "cSipStatsClientNoAcceptHereOuts")

            self.csipstatsclientnosupmediatypeins = YLeaf(YType.uint32, "cSipStatsClientNoSupMediaTypeIns")

            self.csipstatsclientnosupmediatypeouts = YLeaf(YType.uint32, "cSipStatsClientNoSupMediaTypeOuts")

            self.csipstatsclientnotacceptableins = YLeaf(YType.uint32, "cSipStatsClientNotAcceptableIns")

            self.csipstatsclientnotacceptableouts = YLeaf(YType.uint32, "cSipStatsClientNotAcceptableOuts")

            self.csipstatsclientnotfoundins = YLeaf(YType.uint32, "cSipStatsClientNotFoundIns")

            self.csipstatsclientnotfoundouts = YLeaf(YType.uint32, "cSipStatsClientNotFoundOuts")

            self.csipstatsclientpaymentreqdins = YLeaf(YType.uint32, "cSipStatsClientPaymentReqdIns")

            self.csipstatsclientpaymentreqdouts = YLeaf(YType.uint32, "cSipStatsClientPaymentReqdOuts")

            self.csipstatsclientproxyauthreqdins = YLeaf(YType.uint32, "cSipStatsClientProxyAuthReqdIns")

            self.csipstatsclientproxyauthreqdouts = YLeaf(YType.uint32, "cSipStatsClientProxyAuthReqdOuts")

            self.csipstatsclientreqenttoolargeins = YLeaf(YType.uint32, "cSipStatsClientReqEntTooLargeIns")

            self.csipstatsclientreqenttoolargeouts = YLeaf(YType.uint32, "cSipStatsClientReqEntTooLargeOuts")

            self.csipstatsclientreqpendingins = YLeaf(YType.uint32, "cSipStatsClientReqPendingIns")

            self.csipstatsclientreqpendingouts = YLeaf(YType.uint32, "cSipStatsClientReqPendingOuts")

            self.csipstatsclientreqtermins = YLeaf(YType.uint32, "cSipStatsClientReqTermIns")

            self.csipstatsclientreqtermouts = YLeaf(YType.uint32, "cSipStatsClientReqTermOuts")

            self.csipstatsclientreqtimeoutins = YLeaf(YType.uint32, "cSipStatsClientReqTimeoutIns")

            self.csipstatsclientreqtimeoutouts = YLeaf(YType.uint32, "cSipStatsClientReqTimeoutOuts")

            self.csipstatsclientrequritoolargeins = YLeaf(YType.uint32, "cSipStatsClientReqURITooLargeIns")

            self.csipstatsclientrequritoolargeouts = YLeaf(YType.uint32, "cSipStatsClientReqURITooLargeOuts")

            self.csipstatsclientsttoosmallins = YLeaf(YType.uint32, "cSipStatsClientSTTooSmallIns")

            self.csipstatsclientsttoosmallouts = YLeaf(YType.uint32, "cSipStatsClientSTTooSmallOuts")

            self.csipstatsclienttempnotavailins = YLeaf(YType.uint32, "cSipStatsClientTempNotAvailIns")

            self.csipstatsclienttempnotavailouts = YLeaf(YType.uint32, "cSipStatsClientTempNotAvailOuts")

            self.csipstatsclienttoomanyhopsins = YLeaf(YType.uint32, "cSipStatsClientTooManyHopsIns")

            self.csipstatsclienttoomanyhopsouts = YLeaf(YType.uint32, "cSipStatsClientTooManyHopsOuts")

            self.csipstatsclientunauthorizedins = YLeaf(YType.uint32, "cSipStatsClientUnauthorizedIns")

            self.csipstatsclientunauthorizedouts = YLeaf(YType.uint32, "cSipStatsClientUnauthorizedOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsclientaddrincompleteins",
                            "csipstatsclientaddrincompleteouts",
                            "csipstatsclientambiguousins",
                            "csipstatsclientambiguousouts",
                            "csipstatsclientbadeventins",
                            "csipstatsclientbadeventouts",
                            "csipstatsclientbadextensionins",
                            "csipstatsclientbadextensionouts",
                            "csipstatsclientbadrequestins",
                            "csipstatsclientbadrequestouts",
                            "csipstatsclientbusyhereins",
                            "csipstatsclientbusyhereouts",
                            "csipstatsclientcalllegnoexistins",
                            "csipstatsclientcalllegnoexistouts",
                            "csipstatsclientconflictins",
                            "csipstatsclientconflictouts",
                            "csipstatsclientforbiddenins",
                            "csipstatsclientforbiddenouts",
                            "csipstatsclientgoneins",
                            "csipstatsclientgoneouts",
                            "csipstatsclientlengthrequiredins",
                            "csipstatsclientlengthrequiredouts",
                            "csipstatsclientloopdetectedins",
                            "csipstatsclientloopdetectedouts",
                            "csipstatsclientmethnotallowedins",
                            "csipstatsclientmethnotallowedouts",
                            "csipstatsclientnoaccepthereins",
                            "csipstatsclientnoaccepthereouts",
                            "csipstatsclientnosupmediatypeins",
                            "csipstatsclientnosupmediatypeouts",
                            "csipstatsclientnotacceptableins",
                            "csipstatsclientnotacceptableouts",
                            "csipstatsclientnotfoundins",
                            "csipstatsclientnotfoundouts",
                            "csipstatsclientpaymentreqdins",
                            "csipstatsclientpaymentreqdouts",
                            "csipstatsclientproxyauthreqdins",
                            "csipstatsclientproxyauthreqdouts",
                            "csipstatsclientreqenttoolargeins",
                            "csipstatsclientreqenttoolargeouts",
                            "csipstatsclientreqpendingins",
                            "csipstatsclientreqpendingouts",
                            "csipstatsclientreqtermins",
                            "csipstatsclientreqtermouts",
                            "csipstatsclientreqtimeoutins",
                            "csipstatsclientreqtimeoutouts",
                            "csipstatsclientrequritoolargeins",
                            "csipstatsclientrequritoolargeouts",
                            "csipstatsclientsttoosmallins",
                            "csipstatsclientsttoosmallouts",
                            "csipstatsclienttempnotavailins",
                            "csipstatsclienttempnotavailouts",
                            "csipstatsclienttoomanyhopsins",
                            "csipstatsclienttoomanyhopsouts",
                            "csipstatsclientunauthorizedins",
                            "csipstatsclientunauthorizedouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatserrclient, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatserrclient, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsclientaddrincompleteins.is_set or
                self.csipstatsclientaddrincompleteouts.is_set or
                self.csipstatsclientambiguousins.is_set or
                self.csipstatsclientambiguousouts.is_set or
                self.csipstatsclientbadeventins.is_set or
                self.csipstatsclientbadeventouts.is_set or
                self.csipstatsclientbadextensionins.is_set or
                self.csipstatsclientbadextensionouts.is_set or
                self.csipstatsclientbadrequestins.is_set or
                self.csipstatsclientbadrequestouts.is_set or
                self.csipstatsclientbusyhereins.is_set or
                self.csipstatsclientbusyhereouts.is_set or
                self.csipstatsclientcalllegnoexistins.is_set or
                self.csipstatsclientcalllegnoexistouts.is_set or
                self.csipstatsclientconflictins.is_set or
                self.csipstatsclientconflictouts.is_set or
                self.csipstatsclientforbiddenins.is_set or
                self.csipstatsclientforbiddenouts.is_set or
                self.csipstatsclientgoneins.is_set or
                self.csipstatsclientgoneouts.is_set or
                self.csipstatsclientlengthrequiredins.is_set or
                self.csipstatsclientlengthrequiredouts.is_set or
                self.csipstatsclientloopdetectedins.is_set or
                self.csipstatsclientloopdetectedouts.is_set or
                self.csipstatsclientmethnotallowedins.is_set or
                self.csipstatsclientmethnotallowedouts.is_set or
                self.csipstatsclientnoaccepthereins.is_set or
                self.csipstatsclientnoaccepthereouts.is_set or
                self.csipstatsclientnosupmediatypeins.is_set or
                self.csipstatsclientnosupmediatypeouts.is_set or
                self.csipstatsclientnotacceptableins.is_set or
                self.csipstatsclientnotacceptableouts.is_set or
                self.csipstatsclientnotfoundins.is_set or
                self.csipstatsclientnotfoundouts.is_set or
                self.csipstatsclientpaymentreqdins.is_set or
                self.csipstatsclientpaymentreqdouts.is_set or
                self.csipstatsclientproxyauthreqdins.is_set or
                self.csipstatsclientproxyauthreqdouts.is_set or
                self.csipstatsclientreqenttoolargeins.is_set or
                self.csipstatsclientreqenttoolargeouts.is_set or
                self.csipstatsclientreqpendingins.is_set or
                self.csipstatsclientreqpendingouts.is_set or
                self.csipstatsclientreqtermins.is_set or
                self.csipstatsclientreqtermouts.is_set or
                self.csipstatsclientreqtimeoutins.is_set or
                self.csipstatsclientreqtimeoutouts.is_set or
                self.csipstatsclientrequritoolargeins.is_set or
                self.csipstatsclientrequritoolargeouts.is_set or
                self.csipstatsclientsttoosmallins.is_set or
                self.csipstatsclientsttoosmallouts.is_set or
                self.csipstatsclienttempnotavailins.is_set or
                self.csipstatsclienttempnotavailouts.is_set or
                self.csipstatsclienttoomanyhopsins.is_set or
                self.csipstatsclienttoomanyhopsouts.is_set or
                self.csipstatsclientunauthorizedins.is_set or
                self.csipstatsclientunauthorizedouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsclientaddrincompleteins.yfilter != YFilter.not_set or
                self.csipstatsclientaddrincompleteouts.yfilter != YFilter.not_set or
                self.csipstatsclientambiguousins.yfilter != YFilter.not_set or
                self.csipstatsclientambiguousouts.yfilter != YFilter.not_set or
                self.csipstatsclientbadeventins.yfilter != YFilter.not_set or
                self.csipstatsclientbadeventouts.yfilter != YFilter.not_set or
                self.csipstatsclientbadextensionins.yfilter != YFilter.not_set or
                self.csipstatsclientbadextensionouts.yfilter != YFilter.not_set or
                self.csipstatsclientbadrequestins.yfilter != YFilter.not_set or
                self.csipstatsclientbadrequestouts.yfilter != YFilter.not_set or
                self.csipstatsclientbusyhereins.yfilter != YFilter.not_set or
                self.csipstatsclientbusyhereouts.yfilter != YFilter.not_set or
                self.csipstatsclientcalllegnoexistins.yfilter != YFilter.not_set or
                self.csipstatsclientcalllegnoexistouts.yfilter != YFilter.not_set or
                self.csipstatsclientconflictins.yfilter != YFilter.not_set or
                self.csipstatsclientconflictouts.yfilter != YFilter.not_set or
                self.csipstatsclientforbiddenins.yfilter != YFilter.not_set or
                self.csipstatsclientforbiddenouts.yfilter != YFilter.not_set or
                self.csipstatsclientgoneins.yfilter != YFilter.not_set or
                self.csipstatsclientgoneouts.yfilter != YFilter.not_set or
                self.csipstatsclientlengthrequiredins.yfilter != YFilter.not_set or
                self.csipstatsclientlengthrequiredouts.yfilter != YFilter.not_set or
                self.csipstatsclientloopdetectedins.yfilter != YFilter.not_set or
                self.csipstatsclientloopdetectedouts.yfilter != YFilter.not_set or
                self.csipstatsclientmethnotallowedins.yfilter != YFilter.not_set or
                self.csipstatsclientmethnotallowedouts.yfilter != YFilter.not_set or
                self.csipstatsclientnoaccepthereins.yfilter != YFilter.not_set or
                self.csipstatsclientnoaccepthereouts.yfilter != YFilter.not_set or
                self.csipstatsclientnosupmediatypeins.yfilter != YFilter.not_set or
                self.csipstatsclientnosupmediatypeouts.yfilter != YFilter.not_set or
                self.csipstatsclientnotacceptableins.yfilter != YFilter.not_set or
                self.csipstatsclientnotacceptableouts.yfilter != YFilter.not_set or
                self.csipstatsclientnotfoundins.yfilter != YFilter.not_set or
                self.csipstatsclientnotfoundouts.yfilter != YFilter.not_set or
                self.csipstatsclientpaymentreqdins.yfilter != YFilter.not_set or
                self.csipstatsclientpaymentreqdouts.yfilter != YFilter.not_set or
                self.csipstatsclientproxyauthreqdins.yfilter != YFilter.not_set or
                self.csipstatsclientproxyauthreqdouts.yfilter != YFilter.not_set or
                self.csipstatsclientreqenttoolargeins.yfilter != YFilter.not_set or
                self.csipstatsclientreqenttoolargeouts.yfilter != YFilter.not_set or
                self.csipstatsclientreqpendingins.yfilter != YFilter.not_set or
                self.csipstatsclientreqpendingouts.yfilter != YFilter.not_set or
                self.csipstatsclientreqtermins.yfilter != YFilter.not_set or
                self.csipstatsclientreqtermouts.yfilter != YFilter.not_set or
                self.csipstatsclientreqtimeoutins.yfilter != YFilter.not_set or
                self.csipstatsclientreqtimeoutouts.yfilter != YFilter.not_set or
                self.csipstatsclientrequritoolargeins.yfilter != YFilter.not_set or
                self.csipstatsclientrequritoolargeouts.yfilter != YFilter.not_set or
                self.csipstatsclientsttoosmallins.yfilter != YFilter.not_set or
                self.csipstatsclientsttoosmallouts.yfilter != YFilter.not_set or
                self.csipstatsclienttempnotavailins.yfilter != YFilter.not_set or
                self.csipstatsclienttempnotavailouts.yfilter != YFilter.not_set or
                self.csipstatsclienttoomanyhopsins.yfilter != YFilter.not_set or
                self.csipstatsclienttoomanyhopsouts.yfilter != YFilter.not_set or
                self.csipstatsclientunauthorizedins.yfilter != YFilter.not_set or
                self.csipstatsclientunauthorizedouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsErrClient" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsclientaddrincompleteins.is_set or self.csipstatsclientaddrincompleteins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientaddrincompleteins.get_name_leafdata())
            if (self.csipstatsclientaddrincompleteouts.is_set or self.csipstatsclientaddrincompleteouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientaddrincompleteouts.get_name_leafdata())
            if (self.csipstatsclientambiguousins.is_set or self.csipstatsclientambiguousins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientambiguousins.get_name_leafdata())
            if (self.csipstatsclientambiguousouts.is_set or self.csipstatsclientambiguousouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientambiguousouts.get_name_leafdata())
            if (self.csipstatsclientbadeventins.is_set or self.csipstatsclientbadeventins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadeventins.get_name_leafdata())
            if (self.csipstatsclientbadeventouts.is_set or self.csipstatsclientbadeventouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadeventouts.get_name_leafdata())
            if (self.csipstatsclientbadextensionins.is_set or self.csipstatsclientbadextensionins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadextensionins.get_name_leafdata())
            if (self.csipstatsclientbadextensionouts.is_set or self.csipstatsclientbadextensionouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadextensionouts.get_name_leafdata())
            if (self.csipstatsclientbadrequestins.is_set or self.csipstatsclientbadrequestins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadrequestins.get_name_leafdata())
            if (self.csipstatsclientbadrequestouts.is_set or self.csipstatsclientbadrequestouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbadrequestouts.get_name_leafdata())
            if (self.csipstatsclientbusyhereins.is_set or self.csipstatsclientbusyhereins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbusyhereins.get_name_leafdata())
            if (self.csipstatsclientbusyhereouts.is_set or self.csipstatsclientbusyhereouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientbusyhereouts.get_name_leafdata())
            if (self.csipstatsclientcalllegnoexistins.is_set or self.csipstatsclientcalllegnoexistins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientcalllegnoexistins.get_name_leafdata())
            if (self.csipstatsclientcalllegnoexistouts.is_set or self.csipstatsclientcalllegnoexistouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientcalllegnoexistouts.get_name_leafdata())
            if (self.csipstatsclientconflictins.is_set or self.csipstatsclientconflictins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientconflictins.get_name_leafdata())
            if (self.csipstatsclientconflictouts.is_set or self.csipstatsclientconflictouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientconflictouts.get_name_leafdata())
            if (self.csipstatsclientforbiddenins.is_set or self.csipstatsclientforbiddenins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientforbiddenins.get_name_leafdata())
            if (self.csipstatsclientforbiddenouts.is_set or self.csipstatsclientforbiddenouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientforbiddenouts.get_name_leafdata())
            if (self.csipstatsclientgoneins.is_set or self.csipstatsclientgoneins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientgoneins.get_name_leafdata())
            if (self.csipstatsclientgoneouts.is_set or self.csipstatsclientgoneouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientgoneouts.get_name_leafdata())
            if (self.csipstatsclientlengthrequiredins.is_set or self.csipstatsclientlengthrequiredins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientlengthrequiredins.get_name_leafdata())
            if (self.csipstatsclientlengthrequiredouts.is_set or self.csipstatsclientlengthrequiredouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientlengthrequiredouts.get_name_leafdata())
            if (self.csipstatsclientloopdetectedins.is_set or self.csipstatsclientloopdetectedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientloopdetectedins.get_name_leafdata())
            if (self.csipstatsclientloopdetectedouts.is_set or self.csipstatsclientloopdetectedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientloopdetectedouts.get_name_leafdata())
            if (self.csipstatsclientmethnotallowedins.is_set or self.csipstatsclientmethnotallowedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientmethnotallowedins.get_name_leafdata())
            if (self.csipstatsclientmethnotallowedouts.is_set or self.csipstatsclientmethnotallowedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientmethnotallowedouts.get_name_leafdata())
            if (self.csipstatsclientnoaccepthereins.is_set or self.csipstatsclientnoaccepthereins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnoaccepthereins.get_name_leafdata())
            if (self.csipstatsclientnoaccepthereouts.is_set or self.csipstatsclientnoaccepthereouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnoaccepthereouts.get_name_leafdata())
            if (self.csipstatsclientnosupmediatypeins.is_set or self.csipstatsclientnosupmediatypeins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnosupmediatypeins.get_name_leafdata())
            if (self.csipstatsclientnosupmediatypeouts.is_set or self.csipstatsclientnosupmediatypeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnosupmediatypeouts.get_name_leafdata())
            if (self.csipstatsclientnotacceptableins.is_set or self.csipstatsclientnotacceptableins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnotacceptableins.get_name_leafdata())
            if (self.csipstatsclientnotacceptableouts.is_set or self.csipstatsclientnotacceptableouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnotacceptableouts.get_name_leafdata())
            if (self.csipstatsclientnotfoundins.is_set or self.csipstatsclientnotfoundins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnotfoundins.get_name_leafdata())
            if (self.csipstatsclientnotfoundouts.is_set or self.csipstatsclientnotfoundouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientnotfoundouts.get_name_leafdata())
            if (self.csipstatsclientpaymentreqdins.is_set or self.csipstatsclientpaymentreqdins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientpaymentreqdins.get_name_leafdata())
            if (self.csipstatsclientpaymentreqdouts.is_set or self.csipstatsclientpaymentreqdouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientpaymentreqdouts.get_name_leafdata())
            if (self.csipstatsclientproxyauthreqdins.is_set or self.csipstatsclientproxyauthreqdins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientproxyauthreqdins.get_name_leafdata())
            if (self.csipstatsclientproxyauthreqdouts.is_set or self.csipstatsclientproxyauthreqdouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientproxyauthreqdouts.get_name_leafdata())
            if (self.csipstatsclientreqenttoolargeins.is_set or self.csipstatsclientreqenttoolargeins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqenttoolargeins.get_name_leafdata())
            if (self.csipstatsclientreqenttoolargeouts.is_set or self.csipstatsclientreqenttoolargeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqenttoolargeouts.get_name_leafdata())
            if (self.csipstatsclientreqpendingins.is_set or self.csipstatsclientreqpendingins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqpendingins.get_name_leafdata())
            if (self.csipstatsclientreqpendingouts.is_set or self.csipstatsclientreqpendingouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqpendingouts.get_name_leafdata())
            if (self.csipstatsclientreqtermins.is_set or self.csipstatsclientreqtermins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqtermins.get_name_leafdata())
            if (self.csipstatsclientreqtermouts.is_set or self.csipstatsclientreqtermouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqtermouts.get_name_leafdata())
            if (self.csipstatsclientreqtimeoutins.is_set or self.csipstatsclientreqtimeoutins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqtimeoutins.get_name_leafdata())
            if (self.csipstatsclientreqtimeoutouts.is_set or self.csipstatsclientreqtimeoutouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientreqtimeoutouts.get_name_leafdata())
            if (self.csipstatsclientrequritoolargeins.is_set or self.csipstatsclientrequritoolargeins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientrequritoolargeins.get_name_leafdata())
            if (self.csipstatsclientrequritoolargeouts.is_set or self.csipstatsclientrequritoolargeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientrequritoolargeouts.get_name_leafdata())
            if (self.csipstatsclientsttoosmallins.is_set or self.csipstatsclientsttoosmallins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientsttoosmallins.get_name_leafdata())
            if (self.csipstatsclientsttoosmallouts.is_set or self.csipstatsclientsttoosmallouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientsttoosmallouts.get_name_leafdata())
            if (self.csipstatsclienttempnotavailins.is_set or self.csipstatsclienttempnotavailins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclienttempnotavailins.get_name_leafdata())
            if (self.csipstatsclienttempnotavailouts.is_set or self.csipstatsclienttempnotavailouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclienttempnotavailouts.get_name_leafdata())
            if (self.csipstatsclienttoomanyhopsins.is_set or self.csipstatsclienttoomanyhopsins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclienttoomanyhopsins.get_name_leafdata())
            if (self.csipstatsclienttoomanyhopsouts.is_set or self.csipstatsclienttoomanyhopsouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclienttoomanyhopsouts.get_name_leafdata())
            if (self.csipstatsclientunauthorizedins.is_set or self.csipstatsclientunauthorizedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientunauthorizedins.get_name_leafdata())
            if (self.csipstatsclientunauthorizedouts.is_set or self.csipstatsclientunauthorizedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsclientunauthorizedouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsClientAddrIncompleteIns" or name == "cSipStatsClientAddrIncompleteOuts" or name == "cSipStatsClientAmbiguousIns" or name == "cSipStatsClientAmbiguousOuts" or name == "cSipStatsClientBadEventIns" or name == "cSipStatsClientBadEventOuts" or name == "cSipStatsClientBadExtensionIns" or name == "cSipStatsClientBadExtensionOuts" or name == "cSipStatsClientBadRequestIns" or name == "cSipStatsClientBadRequestOuts" or name == "cSipStatsClientBusyHereIns" or name == "cSipStatsClientBusyHereOuts" or name == "cSipStatsClientCallLegNoExistIns" or name == "cSipStatsClientCallLegNoExistOuts" or name == "cSipStatsClientConflictIns" or name == "cSipStatsClientConflictOuts" or name == "cSipStatsClientForbiddenIns" or name == "cSipStatsClientForbiddenOuts" or name == "cSipStatsClientGoneIns" or name == "cSipStatsClientGoneOuts" or name == "cSipStatsClientLengthRequiredIns" or name == "cSipStatsClientLengthRequiredOuts" or name == "cSipStatsClientLoopDetectedIns" or name == "cSipStatsClientLoopDetectedOuts" or name == "cSipStatsClientMethNotAllowedIns" or name == "cSipStatsClientMethNotAllowedOuts" or name == "cSipStatsClientNoAcceptHereIns" or name == "cSipStatsClientNoAcceptHereOuts" or name == "cSipStatsClientNoSupMediaTypeIns" or name == "cSipStatsClientNoSupMediaTypeOuts" or name == "cSipStatsClientNotAcceptableIns" or name == "cSipStatsClientNotAcceptableOuts" or name == "cSipStatsClientNotFoundIns" or name == "cSipStatsClientNotFoundOuts" or name == "cSipStatsClientPaymentReqdIns" or name == "cSipStatsClientPaymentReqdOuts" or name == "cSipStatsClientProxyAuthReqdIns" or name == "cSipStatsClientProxyAuthReqdOuts" or name == "cSipStatsClientReqEntTooLargeIns" or name == "cSipStatsClientReqEntTooLargeOuts" or name == "cSipStatsClientReqPendingIns" or name == "cSipStatsClientReqPendingOuts" or name == "cSipStatsClientReqTermIns" or name == "cSipStatsClientReqTermOuts" or name == "cSipStatsClientReqTimeoutIns" or name == "cSipStatsClientReqTimeoutOuts" or name == "cSipStatsClientReqURITooLargeIns" or name == "cSipStatsClientReqURITooLargeOuts" or name == "cSipStatsClientSTTooSmallIns" or name == "cSipStatsClientSTTooSmallOuts" or name == "cSipStatsClientTempNotAvailIns" or name == "cSipStatsClientTempNotAvailOuts" or name == "cSipStatsClientTooManyHopsIns" or name == "cSipStatsClientTooManyHopsOuts" or name == "cSipStatsClientUnauthorizedIns" or name == "cSipStatsClientUnauthorizedOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsClientAddrIncompleteIns"):
                self.csipstatsclientaddrincompleteins = value
                self.csipstatsclientaddrincompleteins.value_namespace = name_space
                self.csipstatsclientaddrincompleteins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientAddrIncompleteOuts"):
                self.csipstatsclientaddrincompleteouts = value
                self.csipstatsclientaddrincompleteouts.value_namespace = name_space
                self.csipstatsclientaddrincompleteouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientAmbiguousIns"):
                self.csipstatsclientambiguousins = value
                self.csipstatsclientambiguousins.value_namespace = name_space
                self.csipstatsclientambiguousins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientAmbiguousOuts"):
                self.csipstatsclientambiguousouts = value
                self.csipstatsclientambiguousouts.value_namespace = name_space
                self.csipstatsclientambiguousouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadEventIns"):
                self.csipstatsclientbadeventins = value
                self.csipstatsclientbadeventins.value_namespace = name_space
                self.csipstatsclientbadeventins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadEventOuts"):
                self.csipstatsclientbadeventouts = value
                self.csipstatsclientbadeventouts.value_namespace = name_space
                self.csipstatsclientbadeventouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadExtensionIns"):
                self.csipstatsclientbadextensionins = value
                self.csipstatsclientbadextensionins.value_namespace = name_space
                self.csipstatsclientbadextensionins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadExtensionOuts"):
                self.csipstatsclientbadextensionouts = value
                self.csipstatsclientbadextensionouts.value_namespace = name_space
                self.csipstatsclientbadextensionouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadRequestIns"):
                self.csipstatsclientbadrequestins = value
                self.csipstatsclientbadrequestins.value_namespace = name_space
                self.csipstatsclientbadrequestins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBadRequestOuts"):
                self.csipstatsclientbadrequestouts = value
                self.csipstatsclientbadrequestouts.value_namespace = name_space
                self.csipstatsclientbadrequestouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBusyHereIns"):
                self.csipstatsclientbusyhereins = value
                self.csipstatsclientbusyhereins.value_namespace = name_space
                self.csipstatsclientbusyhereins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientBusyHereOuts"):
                self.csipstatsclientbusyhereouts = value
                self.csipstatsclientbusyhereouts.value_namespace = name_space
                self.csipstatsclientbusyhereouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientCallLegNoExistIns"):
                self.csipstatsclientcalllegnoexistins = value
                self.csipstatsclientcalllegnoexistins.value_namespace = name_space
                self.csipstatsclientcalllegnoexistins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientCallLegNoExistOuts"):
                self.csipstatsclientcalllegnoexistouts = value
                self.csipstatsclientcalllegnoexistouts.value_namespace = name_space
                self.csipstatsclientcalllegnoexistouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientConflictIns"):
                self.csipstatsclientconflictins = value
                self.csipstatsclientconflictins.value_namespace = name_space
                self.csipstatsclientconflictins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientConflictOuts"):
                self.csipstatsclientconflictouts = value
                self.csipstatsclientconflictouts.value_namespace = name_space
                self.csipstatsclientconflictouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientForbiddenIns"):
                self.csipstatsclientforbiddenins = value
                self.csipstatsclientforbiddenins.value_namespace = name_space
                self.csipstatsclientforbiddenins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientForbiddenOuts"):
                self.csipstatsclientforbiddenouts = value
                self.csipstatsclientforbiddenouts.value_namespace = name_space
                self.csipstatsclientforbiddenouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientGoneIns"):
                self.csipstatsclientgoneins = value
                self.csipstatsclientgoneins.value_namespace = name_space
                self.csipstatsclientgoneins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientGoneOuts"):
                self.csipstatsclientgoneouts = value
                self.csipstatsclientgoneouts.value_namespace = name_space
                self.csipstatsclientgoneouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientLengthRequiredIns"):
                self.csipstatsclientlengthrequiredins = value
                self.csipstatsclientlengthrequiredins.value_namespace = name_space
                self.csipstatsclientlengthrequiredins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientLengthRequiredOuts"):
                self.csipstatsclientlengthrequiredouts = value
                self.csipstatsclientlengthrequiredouts.value_namespace = name_space
                self.csipstatsclientlengthrequiredouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientLoopDetectedIns"):
                self.csipstatsclientloopdetectedins = value
                self.csipstatsclientloopdetectedins.value_namespace = name_space
                self.csipstatsclientloopdetectedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientLoopDetectedOuts"):
                self.csipstatsclientloopdetectedouts = value
                self.csipstatsclientloopdetectedouts.value_namespace = name_space
                self.csipstatsclientloopdetectedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientMethNotAllowedIns"):
                self.csipstatsclientmethnotallowedins = value
                self.csipstatsclientmethnotallowedins.value_namespace = name_space
                self.csipstatsclientmethnotallowedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientMethNotAllowedOuts"):
                self.csipstatsclientmethnotallowedouts = value
                self.csipstatsclientmethnotallowedouts.value_namespace = name_space
                self.csipstatsclientmethnotallowedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNoAcceptHereIns"):
                self.csipstatsclientnoaccepthereins = value
                self.csipstatsclientnoaccepthereins.value_namespace = name_space
                self.csipstatsclientnoaccepthereins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNoAcceptHereOuts"):
                self.csipstatsclientnoaccepthereouts = value
                self.csipstatsclientnoaccepthereouts.value_namespace = name_space
                self.csipstatsclientnoaccepthereouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNoSupMediaTypeIns"):
                self.csipstatsclientnosupmediatypeins = value
                self.csipstatsclientnosupmediatypeins.value_namespace = name_space
                self.csipstatsclientnosupmediatypeins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNoSupMediaTypeOuts"):
                self.csipstatsclientnosupmediatypeouts = value
                self.csipstatsclientnosupmediatypeouts.value_namespace = name_space
                self.csipstatsclientnosupmediatypeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNotAcceptableIns"):
                self.csipstatsclientnotacceptableins = value
                self.csipstatsclientnotacceptableins.value_namespace = name_space
                self.csipstatsclientnotacceptableins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNotAcceptableOuts"):
                self.csipstatsclientnotacceptableouts = value
                self.csipstatsclientnotacceptableouts.value_namespace = name_space
                self.csipstatsclientnotacceptableouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNotFoundIns"):
                self.csipstatsclientnotfoundins = value
                self.csipstatsclientnotfoundins.value_namespace = name_space
                self.csipstatsclientnotfoundins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientNotFoundOuts"):
                self.csipstatsclientnotfoundouts = value
                self.csipstatsclientnotfoundouts.value_namespace = name_space
                self.csipstatsclientnotfoundouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientPaymentReqdIns"):
                self.csipstatsclientpaymentreqdins = value
                self.csipstatsclientpaymentreqdins.value_namespace = name_space
                self.csipstatsclientpaymentreqdins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientPaymentReqdOuts"):
                self.csipstatsclientpaymentreqdouts = value
                self.csipstatsclientpaymentreqdouts.value_namespace = name_space
                self.csipstatsclientpaymentreqdouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientProxyAuthReqdIns"):
                self.csipstatsclientproxyauthreqdins = value
                self.csipstatsclientproxyauthreqdins.value_namespace = name_space
                self.csipstatsclientproxyauthreqdins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientProxyAuthReqdOuts"):
                self.csipstatsclientproxyauthreqdouts = value
                self.csipstatsclientproxyauthreqdouts.value_namespace = name_space
                self.csipstatsclientproxyauthreqdouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqEntTooLargeIns"):
                self.csipstatsclientreqenttoolargeins = value
                self.csipstatsclientreqenttoolargeins.value_namespace = name_space
                self.csipstatsclientreqenttoolargeins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqEntTooLargeOuts"):
                self.csipstatsclientreqenttoolargeouts = value
                self.csipstatsclientreqenttoolargeouts.value_namespace = name_space
                self.csipstatsclientreqenttoolargeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqPendingIns"):
                self.csipstatsclientreqpendingins = value
                self.csipstatsclientreqpendingins.value_namespace = name_space
                self.csipstatsclientreqpendingins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqPendingOuts"):
                self.csipstatsclientreqpendingouts = value
                self.csipstatsclientreqpendingouts.value_namespace = name_space
                self.csipstatsclientreqpendingouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqTermIns"):
                self.csipstatsclientreqtermins = value
                self.csipstatsclientreqtermins.value_namespace = name_space
                self.csipstatsclientreqtermins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqTermOuts"):
                self.csipstatsclientreqtermouts = value
                self.csipstatsclientreqtermouts.value_namespace = name_space
                self.csipstatsclientreqtermouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqTimeoutIns"):
                self.csipstatsclientreqtimeoutins = value
                self.csipstatsclientreqtimeoutins.value_namespace = name_space
                self.csipstatsclientreqtimeoutins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqTimeoutOuts"):
                self.csipstatsclientreqtimeoutouts = value
                self.csipstatsclientreqtimeoutouts.value_namespace = name_space
                self.csipstatsclientreqtimeoutouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqURITooLargeIns"):
                self.csipstatsclientrequritoolargeins = value
                self.csipstatsclientrequritoolargeins.value_namespace = name_space
                self.csipstatsclientrequritoolargeins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientReqURITooLargeOuts"):
                self.csipstatsclientrequritoolargeouts = value
                self.csipstatsclientrequritoolargeouts.value_namespace = name_space
                self.csipstatsclientrequritoolargeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientSTTooSmallIns"):
                self.csipstatsclientsttoosmallins = value
                self.csipstatsclientsttoosmallins.value_namespace = name_space
                self.csipstatsclientsttoosmallins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientSTTooSmallOuts"):
                self.csipstatsclientsttoosmallouts = value
                self.csipstatsclientsttoosmallouts.value_namespace = name_space
                self.csipstatsclientsttoosmallouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientTempNotAvailIns"):
                self.csipstatsclienttempnotavailins = value
                self.csipstatsclienttempnotavailins.value_namespace = name_space
                self.csipstatsclienttempnotavailins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientTempNotAvailOuts"):
                self.csipstatsclienttempnotavailouts = value
                self.csipstatsclienttempnotavailouts.value_namespace = name_space
                self.csipstatsclienttempnotavailouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientTooManyHopsIns"):
                self.csipstatsclienttoomanyhopsins = value
                self.csipstatsclienttoomanyhopsins.value_namespace = name_space
                self.csipstatsclienttoomanyhopsins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientTooManyHopsOuts"):
                self.csipstatsclienttoomanyhopsouts = value
                self.csipstatsclienttoomanyhopsouts.value_namespace = name_space
                self.csipstatsclienttoomanyhopsouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientUnauthorizedIns"):
                self.csipstatsclientunauthorizedins = value
                self.csipstatsclientunauthorizedins.value_namespace = name_space
                self.csipstatsclientunauthorizedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsClientUnauthorizedOuts"):
                self.csipstatsclientunauthorizedouts = value
                self.csipstatsclientunauthorizedouts.value_namespace = name_space
                self.csipstatsclientunauthorizedouts.value_namespace_prefix = name_space_prefix


    class Csipstatserrserver(Entity):
        """
        
        
        .. attribute:: csipstatsserverbadgatewayins
        
        	This object reflects the total number of Bad Gateway (502)  responses received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadgatewayouts
        
        	This object reflects the total number of Bad Gateway (502)  responses sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadsipversionins
        
        	This object reflects the total number of SIP Version Not  Supported (505) responses received by the user agent since system startup. Inbound SIP Version Not Supported responses indicate that  the server does not support, or refuses to support, the SIP  protocol version that was used in the request message
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadsipversionouts
        
        	This object reflects the total number of SIP Version Not  Supported (505) responses sent by the user agent since system startup. Outbound SIP Version Not Supported responses indicate that  this system does not support, or refuses to support, the SIP  protocol version used in received requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservergatewaytimeoutins
        
        	This object reflects the total number of Gateway Time\-out  (504) responses received by the user agent since system startup. Inbound Gateway Time\-out responses indicate that the server attempting to complete this system's request did not receive a timely response from yet another system it was accessing to complete the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservergatewaytimeoutouts
        
        	This object reflects the total number of Gateway Time\-out  (504) responses sent by the user agent since system startup. Outbound Gateway Time\-out responses indicate that this system did not receive a timely response from the system it had accessed to assist in completing a received request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverinterrorins
        
        	This object reflects the total number of Internal Server Error (500) responses received by the user agent since system startup. Inbound Internal Server Error responses indicate that servers  to which this system is sending requests have encountered  unexpected conditions that prevent them from fulfilling the  requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverinterrorouts
        
        	This object reflects the total number of Internal Server Error (500) responses sent by the user agent since system startup. Outbound Internal Server Error responses indicate that this  system has encountered unexpected conditions that prevent it  from fulfilling received requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservernotimplementedins
        
        	This object reflects the total number of Not Implemented  (501) responses received by the user agent since system startup. Inbound Not Implemented responses indicate that servers to  which this system is sending requests do not support the  functionality required to fulfill the requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservernotimplementedouts
        
        	This object reflects the total number of Not Implemented  (501) responses sent by the user agent since system startup. Outbound Not Implemented responses indicate that this system does not support the functionality required to fulfill the  requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverprecondfailureins
        
        	This object reflects the total number of Precondition  Failure (580) responses received by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverprecondfailureouts
        
        	This object reflects the total number of Precondition  Failure (580) responses sent by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverserviceunavailins
        
        	This object reflects the total number of Service Unavailable  (503) responses received by the user agent since system startup. Inbound Service Unavailable responses indicate that the server servicing this system's request is temporarily unavailable to handle the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverserviceunavailouts
        
        	This object reflects the total number of Service Unavailable  (503) responses sent by the user agent since system startup. Outbound Service Unavailable responses indicate that this system is temporarily unable to handle received requests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatserrserver, self).__init__()

            self.yang_name = "cSipStatsErrServer"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsserverbadgatewayins = YLeaf(YType.uint32, "cSipStatsServerBadGatewayIns")

            self.csipstatsserverbadgatewayouts = YLeaf(YType.uint32, "cSipStatsServerBadGatewayOuts")

            self.csipstatsserverbadsipversionins = YLeaf(YType.uint32, "cSipStatsServerBadSipVersionIns")

            self.csipstatsserverbadsipversionouts = YLeaf(YType.uint32, "cSipStatsServerBadSipVersionOuts")

            self.csipstatsservergatewaytimeoutins = YLeaf(YType.uint32, "cSipStatsServerGatewayTimeoutIns")

            self.csipstatsservergatewaytimeoutouts = YLeaf(YType.uint32, "cSipStatsServerGatewayTimeoutOuts")

            self.csipstatsserverinterrorins = YLeaf(YType.uint32, "cSipStatsServerIntErrorIns")

            self.csipstatsserverinterrorouts = YLeaf(YType.uint32, "cSipStatsServerIntErrorOuts")

            self.csipstatsservernotimplementedins = YLeaf(YType.uint32, "cSipStatsServerNotImplementedIns")

            self.csipstatsservernotimplementedouts = YLeaf(YType.uint32, "cSipStatsServerNotImplementedOuts")

            self.csipstatsserverprecondfailureins = YLeaf(YType.uint32, "cSipStatsServerPrecondFailureIns")

            self.csipstatsserverprecondfailureouts = YLeaf(YType.uint32, "cSipStatsServerPrecondFailureOuts")

            self.csipstatsserverserviceunavailins = YLeaf(YType.uint32, "cSipStatsServerServiceUnavailIns")

            self.csipstatsserverserviceunavailouts = YLeaf(YType.uint32, "cSipStatsServerServiceUnavailOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsserverbadgatewayins",
                            "csipstatsserverbadgatewayouts",
                            "csipstatsserverbadsipversionins",
                            "csipstatsserverbadsipversionouts",
                            "csipstatsservergatewaytimeoutins",
                            "csipstatsservergatewaytimeoutouts",
                            "csipstatsserverinterrorins",
                            "csipstatsserverinterrorouts",
                            "csipstatsservernotimplementedins",
                            "csipstatsservernotimplementedouts",
                            "csipstatsserverprecondfailureins",
                            "csipstatsserverprecondfailureouts",
                            "csipstatsserverserviceunavailins",
                            "csipstatsserverserviceunavailouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatserrserver, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatserrserver, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsserverbadgatewayins.is_set or
                self.csipstatsserverbadgatewayouts.is_set or
                self.csipstatsserverbadsipversionins.is_set or
                self.csipstatsserverbadsipversionouts.is_set or
                self.csipstatsservergatewaytimeoutins.is_set or
                self.csipstatsservergatewaytimeoutouts.is_set or
                self.csipstatsserverinterrorins.is_set or
                self.csipstatsserverinterrorouts.is_set or
                self.csipstatsservernotimplementedins.is_set or
                self.csipstatsservernotimplementedouts.is_set or
                self.csipstatsserverprecondfailureins.is_set or
                self.csipstatsserverprecondfailureouts.is_set or
                self.csipstatsserverserviceunavailins.is_set or
                self.csipstatsserverserviceunavailouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsserverbadgatewayins.yfilter != YFilter.not_set or
                self.csipstatsserverbadgatewayouts.yfilter != YFilter.not_set or
                self.csipstatsserverbadsipversionins.yfilter != YFilter.not_set or
                self.csipstatsserverbadsipversionouts.yfilter != YFilter.not_set or
                self.csipstatsservergatewaytimeoutins.yfilter != YFilter.not_set or
                self.csipstatsservergatewaytimeoutouts.yfilter != YFilter.not_set or
                self.csipstatsserverinterrorins.yfilter != YFilter.not_set or
                self.csipstatsserverinterrorouts.yfilter != YFilter.not_set or
                self.csipstatsservernotimplementedins.yfilter != YFilter.not_set or
                self.csipstatsservernotimplementedouts.yfilter != YFilter.not_set or
                self.csipstatsserverprecondfailureins.yfilter != YFilter.not_set or
                self.csipstatsserverprecondfailureouts.yfilter != YFilter.not_set or
                self.csipstatsserverserviceunavailins.yfilter != YFilter.not_set or
                self.csipstatsserverserviceunavailouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsErrServer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsserverbadgatewayins.is_set or self.csipstatsserverbadgatewayins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverbadgatewayins.get_name_leafdata())
            if (self.csipstatsserverbadgatewayouts.is_set or self.csipstatsserverbadgatewayouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverbadgatewayouts.get_name_leafdata())
            if (self.csipstatsserverbadsipversionins.is_set or self.csipstatsserverbadsipversionins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverbadsipversionins.get_name_leafdata())
            if (self.csipstatsserverbadsipversionouts.is_set or self.csipstatsserverbadsipversionouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverbadsipversionouts.get_name_leafdata())
            if (self.csipstatsservergatewaytimeoutins.is_set or self.csipstatsservergatewaytimeoutins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsservergatewaytimeoutins.get_name_leafdata())
            if (self.csipstatsservergatewaytimeoutouts.is_set or self.csipstatsservergatewaytimeoutouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsservergatewaytimeoutouts.get_name_leafdata())
            if (self.csipstatsserverinterrorins.is_set or self.csipstatsserverinterrorins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverinterrorins.get_name_leafdata())
            if (self.csipstatsserverinterrorouts.is_set or self.csipstatsserverinterrorouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverinterrorouts.get_name_leafdata())
            if (self.csipstatsservernotimplementedins.is_set or self.csipstatsservernotimplementedins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsservernotimplementedins.get_name_leafdata())
            if (self.csipstatsservernotimplementedouts.is_set or self.csipstatsservernotimplementedouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsservernotimplementedouts.get_name_leafdata())
            if (self.csipstatsserverprecondfailureins.is_set or self.csipstatsserverprecondfailureins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverprecondfailureins.get_name_leafdata())
            if (self.csipstatsserverprecondfailureouts.is_set or self.csipstatsserverprecondfailureouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverprecondfailureouts.get_name_leafdata())
            if (self.csipstatsserverserviceunavailins.is_set or self.csipstatsserverserviceunavailins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverserviceunavailins.get_name_leafdata())
            if (self.csipstatsserverserviceunavailouts.is_set or self.csipstatsserverserviceunavailouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsserverserviceunavailouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsServerBadGatewayIns" or name == "cSipStatsServerBadGatewayOuts" or name == "cSipStatsServerBadSipVersionIns" or name == "cSipStatsServerBadSipVersionOuts" or name == "cSipStatsServerGatewayTimeoutIns" or name == "cSipStatsServerGatewayTimeoutOuts" or name == "cSipStatsServerIntErrorIns" or name == "cSipStatsServerIntErrorOuts" or name == "cSipStatsServerNotImplementedIns" or name == "cSipStatsServerNotImplementedOuts" or name == "cSipStatsServerPrecondFailureIns" or name == "cSipStatsServerPrecondFailureOuts" or name == "cSipStatsServerServiceUnavailIns" or name == "cSipStatsServerServiceUnavailOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsServerBadGatewayIns"):
                self.csipstatsserverbadgatewayins = value
                self.csipstatsserverbadgatewayins.value_namespace = name_space
                self.csipstatsserverbadgatewayins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerBadGatewayOuts"):
                self.csipstatsserverbadgatewayouts = value
                self.csipstatsserverbadgatewayouts.value_namespace = name_space
                self.csipstatsserverbadgatewayouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerBadSipVersionIns"):
                self.csipstatsserverbadsipversionins = value
                self.csipstatsserverbadsipversionins.value_namespace = name_space
                self.csipstatsserverbadsipversionins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerBadSipVersionOuts"):
                self.csipstatsserverbadsipversionouts = value
                self.csipstatsserverbadsipversionouts.value_namespace = name_space
                self.csipstatsserverbadsipversionouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerGatewayTimeoutIns"):
                self.csipstatsservergatewaytimeoutins = value
                self.csipstatsservergatewaytimeoutins.value_namespace = name_space
                self.csipstatsservergatewaytimeoutins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerGatewayTimeoutOuts"):
                self.csipstatsservergatewaytimeoutouts = value
                self.csipstatsservergatewaytimeoutouts.value_namespace = name_space
                self.csipstatsservergatewaytimeoutouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerIntErrorIns"):
                self.csipstatsserverinterrorins = value
                self.csipstatsserverinterrorins.value_namespace = name_space
                self.csipstatsserverinterrorins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerIntErrorOuts"):
                self.csipstatsserverinterrorouts = value
                self.csipstatsserverinterrorouts.value_namespace = name_space
                self.csipstatsserverinterrorouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerNotImplementedIns"):
                self.csipstatsservernotimplementedins = value
                self.csipstatsservernotimplementedins.value_namespace = name_space
                self.csipstatsservernotimplementedins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerNotImplementedOuts"):
                self.csipstatsservernotimplementedouts = value
                self.csipstatsservernotimplementedouts.value_namespace = name_space
                self.csipstatsservernotimplementedouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerPrecondFailureIns"):
                self.csipstatsserverprecondfailureins = value
                self.csipstatsserverprecondfailureins.value_namespace = name_space
                self.csipstatsserverprecondfailureins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerPrecondFailureOuts"):
                self.csipstatsserverprecondfailureouts = value
                self.csipstatsserverprecondfailureouts.value_namespace = name_space
                self.csipstatsserverprecondfailureouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerServiceUnavailIns"):
                self.csipstatsserverserviceunavailins = value
                self.csipstatsserverserviceunavailins.value_namespace = name_space
                self.csipstatsserverserviceunavailins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsServerServiceUnavailOuts"):
                self.csipstatsserverserviceunavailouts = value
                self.csipstatsserverserviceunavailouts.value_namespace = name_space
                self.csipstatsserverserviceunavailouts.value_namespace_prefix = name_space_prefix


    class Csipstatsglobalfail(Entity):
        """
        
        
        .. attribute:: csipstatsglobalbusyeverywhereins
        
        	This object reflects the total number of Busy Everywhere (600) responses received by the user agent since system startup. Inbound Busy Everywhere responses indicate that the  called party's end system was contacted successfully but the called party is busy and does not wish to take the call at this time
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalbusyeverywhereouts
        
        	This object reflects the total number of Busy Everywhere (600) responses sent by the user agent since system startup. Outbound Busy Everywhere responses indicate that  this system has successfully contacted a called party's end system and the called party does not wish to take the call at this time
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobaldeclineins
        
        	This object reflects the total number of Decline (603) responses received by the user agent since system startup. Decline responses indicate that the called party's end  system was contacted successfully but the called party  explicitly does not wish to, or cannot, participate
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobaldeclineouts
        
        	This object reflects the total number of Decline (603) responses sent by the user agent since system startup. Outbound Decline responses indicate that this system has successfully contacted a called party's end system and the called party explicitly does not wish to, or cannot, participate
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotacceptableins
        
        	This object reflects the total number of Not Acceptable (606) responses received by the user agent since system startup. Inbound Not Acceptable responses indicate that the called party's end system was contacted successfully but some aspect of the session description is not acceptable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotacceptableouts
        
        	This object reflects the total number of Not Acceptable (606) responses sent by the user agent since system startup. Outbound Not Acceptable responses indicate that the called party wishes to communicate, but cannot adequately support the session described in the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotanywhereins
        
        	This object reflects the total number of Does Not Exist Anywhere (604) responses received by the user agent since system startup. Inbound Does Not Exist Anywhere responses indicate that the server handling this system's request has authoritative information that the called party indicated in the To request field does not exist anywhere
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotanywhereouts
        
        	This object reflects the total number of Does Not Exist Anywhere (604) responses sent by the user agent since system startup. Outbound Does Not Exist Anywhere responses indicate that this system has authoritative information that the called party in the To field of received requests does not exist anywhere
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsglobalfail, self).__init__()

            self.yang_name = "cSipStatsGlobalFail"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsglobalbusyeverywhereins = YLeaf(YType.uint32, "cSipStatsGlobalBusyEverywhereIns")

            self.csipstatsglobalbusyeverywhereouts = YLeaf(YType.uint32, "cSipStatsGlobalBusyEverywhereOuts")

            self.csipstatsglobaldeclineins = YLeaf(YType.uint32, "cSipStatsGlobalDeclineIns")

            self.csipstatsglobaldeclineouts = YLeaf(YType.uint32, "cSipStatsGlobalDeclineOuts")

            self.csipstatsglobalnotacceptableins = YLeaf(YType.uint32, "cSipStatsGlobalNotAcceptableIns")

            self.csipstatsglobalnotacceptableouts = YLeaf(YType.uint32, "cSipStatsGlobalNotAcceptableOuts")

            self.csipstatsglobalnotanywhereins = YLeaf(YType.uint32, "cSipStatsGlobalNotAnywhereIns")

            self.csipstatsglobalnotanywhereouts = YLeaf(YType.uint32, "cSipStatsGlobalNotAnywhereOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsglobalbusyeverywhereins",
                            "csipstatsglobalbusyeverywhereouts",
                            "csipstatsglobaldeclineins",
                            "csipstatsglobaldeclineouts",
                            "csipstatsglobalnotacceptableins",
                            "csipstatsglobalnotacceptableouts",
                            "csipstatsglobalnotanywhereins",
                            "csipstatsglobalnotanywhereouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsglobalfail, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsglobalfail, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsglobalbusyeverywhereins.is_set or
                self.csipstatsglobalbusyeverywhereouts.is_set or
                self.csipstatsglobaldeclineins.is_set or
                self.csipstatsglobaldeclineouts.is_set or
                self.csipstatsglobalnotacceptableins.is_set or
                self.csipstatsglobalnotacceptableouts.is_set or
                self.csipstatsglobalnotanywhereins.is_set or
                self.csipstatsglobalnotanywhereouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsglobalbusyeverywhereins.yfilter != YFilter.not_set or
                self.csipstatsglobalbusyeverywhereouts.yfilter != YFilter.not_set or
                self.csipstatsglobaldeclineins.yfilter != YFilter.not_set or
                self.csipstatsglobaldeclineouts.yfilter != YFilter.not_set or
                self.csipstatsglobalnotacceptableins.yfilter != YFilter.not_set or
                self.csipstatsglobalnotacceptableouts.yfilter != YFilter.not_set or
                self.csipstatsglobalnotanywhereins.yfilter != YFilter.not_set or
                self.csipstatsglobalnotanywhereouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsGlobalFail" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsglobalbusyeverywhereins.is_set or self.csipstatsglobalbusyeverywhereins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalbusyeverywhereins.get_name_leafdata())
            if (self.csipstatsglobalbusyeverywhereouts.is_set or self.csipstatsglobalbusyeverywhereouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalbusyeverywhereouts.get_name_leafdata())
            if (self.csipstatsglobaldeclineins.is_set or self.csipstatsglobaldeclineins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobaldeclineins.get_name_leafdata())
            if (self.csipstatsglobaldeclineouts.is_set or self.csipstatsglobaldeclineouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobaldeclineouts.get_name_leafdata())
            if (self.csipstatsglobalnotacceptableins.is_set or self.csipstatsglobalnotacceptableins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalnotacceptableins.get_name_leafdata())
            if (self.csipstatsglobalnotacceptableouts.is_set or self.csipstatsglobalnotacceptableouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalnotacceptableouts.get_name_leafdata())
            if (self.csipstatsglobalnotanywhereins.is_set or self.csipstatsglobalnotanywhereins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalnotanywhereins.get_name_leafdata())
            if (self.csipstatsglobalnotanywhereouts.is_set or self.csipstatsglobalnotanywhereouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsglobalnotanywhereouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsGlobalBusyEverywhereIns" or name == "cSipStatsGlobalBusyEverywhereOuts" or name == "cSipStatsGlobalDeclineIns" or name == "cSipStatsGlobalDeclineOuts" or name == "cSipStatsGlobalNotAcceptableIns" or name == "cSipStatsGlobalNotAcceptableOuts" or name == "cSipStatsGlobalNotAnywhereIns" or name == "cSipStatsGlobalNotAnywhereOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsGlobalBusyEverywhereIns"):
                self.csipstatsglobalbusyeverywhereins = value
                self.csipstatsglobalbusyeverywhereins.value_namespace = name_space
                self.csipstatsglobalbusyeverywhereins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalBusyEverywhereOuts"):
                self.csipstatsglobalbusyeverywhereouts = value
                self.csipstatsglobalbusyeverywhereouts.value_namespace = name_space
                self.csipstatsglobalbusyeverywhereouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalDeclineIns"):
                self.csipstatsglobaldeclineins = value
                self.csipstatsglobaldeclineins.value_namespace = name_space
                self.csipstatsglobaldeclineins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalDeclineOuts"):
                self.csipstatsglobaldeclineouts = value
                self.csipstatsglobaldeclineouts.value_namespace = name_space
                self.csipstatsglobaldeclineouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalNotAcceptableIns"):
                self.csipstatsglobalnotacceptableins = value
                self.csipstatsglobalnotacceptableins.value_namespace = name_space
                self.csipstatsglobalnotacceptableins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalNotAcceptableOuts"):
                self.csipstatsglobalnotacceptableouts = value
                self.csipstatsglobalnotacceptableouts.value_namespace = name_space
                self.csipstatsglobalnotacceptableouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalNotAnywhereIns"):
                self.csipstatsglobalnotanywhereins = value
                self.csipstatsglobalnotanywhereins.value_namespace = name_space
                self.csipstatsglobalnotanywhereins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsGlobalNotAnywhereOuts"):
                self.csipstatsglobalnotanywhereouts = value
                self.csipstatsglobalnotanywhereouts.value_namespace = name_space
                self.csipstatsglobalnotanywhereouts.value_namespace_prefix = name_space_prefix


    class Csipstatstraffic(Entity):
        """
        
        
        .. attribute:: csipstatstrafficackins
        
        	This object reflects the total number of ACK requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficackouts
        
        	This object reflects the total number of ACK requests sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficbyeins
        
        	This object reflects the total number of BYE requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficbyeouts
        
        	This object reflects the total number of BYE requests sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcancelins
        
        	This object reflects the total number of CANCEL requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcancelouts
        
        	This object reflects the total number of CANCEL requests sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcometins
        
        	This object reflects the total number of COndition MET  requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcometouts
        
        	This object reflects the total number of COndition MET  requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinfoins
        
        	This object reflects the total number of Info  requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinfoouts
        
        	This object reflects the total number of Info  requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinviteins
        
        	This object reflects the total number of INVITE requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinviteouts
        
        	This object reflects the total number of INVITE requests sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficnotifyins
        
        	This object reflects the total number of Notify  requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficnotifyouts
        
        	This object reflects the total number of Notify  requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficoptionsins
        
        	This object reflects the total number of OPTIONS requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficoptionsouts
        
        	This object reflects the total number of OPTIONS requests sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficprackins
        
        	This object reflects the total number of PRovisonal  ACKnowledgement requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficprackouts
        
        	This object reflects the total number of PRovisonal  ACKnowledgement requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficreferins
        
        	This object reflects the total number of Refer requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficreferouts
        
        	This object reflects the total number of Refer requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficregisterins
        
        	This object reflects the total number of REGISTER requests  received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficregisterouts
        
        	This object reflects the total number of REGISTER requests  sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficsubscribeins
        
        	This object reflects the total number of Subscribe requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficsubscribeouts
        
        	This object reflects the total number of Subscribe requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficupdateins
        
        	This object reflects the total number of Update requests received by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficupdateouts
        
        	This object reflects the total number of Update requests sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatstraffic, self).__init__()

            self.yang_name = "cSipStatsTraffic"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatstrafficackins = YLeaf(YType.uint32, "cSipStatsTrafficAckIns")

            self.csipstatstrafficackouts = YLeaf(YType.uint32, "cSipStatsTrafficAckOuts")

            self.csipstatstrafficbyeins = YLeaf(YType.uint32, "cSipStatsTrafficByeIns")

            self.csipstatstrafficbyeouts = YLeaf(YType.uint32, "cSipStatsTrafficByeOuts")

            self.csipstatstrafficcancelins = YLeaf(YType.uint32, "cSipStatsTrafficCancelIns")

            self.csipstatstrafficcancelouts = YLeaf(YType.uint32, "cSipStatsTrafficCancelOuts")

            self.csipstatstrafficcometins = YLeaf(YType.uint32, "cSipStatsTrafficCometIns")

            self.csipstatstrafficcometouts = YLeaf(YType.uint32, "cSipStatsTrafficCometOuts")

            self.csipstatstrafficinfoins = YLeaf(YType.uint32, "cSipStatsTrafficInfoIns")

            self.csipstatstrafficinfoouts = YLeaf(YType.uint32, "cSipStatsTrafficInfoOuts")

            self.csipstatstrafficinviteins = YLeaf(YType.uint32, "cSipStatsTrafficInviteIns")

            self.csipstatstrafficinviteouts = YLeaf(YType.uint32, "cSipStatsTrafficInviteOuts")

            self.csipstatstrafficnotifyins = YLeaf(YType.uint32, "cSipStatsTrafficNotifyIns")

            self.csipstatstrafficnotifyouts = YLeaf(YType.uint32, "cSipStatsTrafficNotifyOuts")

            self.csipstatstrafficoptionsins = YLeaf(YType.uint32, "cSipStatsTrafficOptionsIns")

            self.csipstatstrafficoptionsouts = YLeaf(YType.uint32, "cSipStatsTrafficOptionsOuts")

            self.csipstatstrafficprackins = YLeaf(YType.uint32, "cSipStatsTrafficPrackIns")

            self.csipstatstrafficprackouts = YLeaf(YType.uint32, "cSipStatsTrafficPrackOuts")

            self.csipstatstrafficreferins = YLeaf(YType.uint32, "cSipStatsTrafficReferIns")

            self.csipstatstrafficreferouts = YLeaf(YType.uint32, "cSipStatsTrafficReferOuts")

            self.csipstatstrafficregisterins = YLeaf(YType.uint32, "cSipStatsTrafficRegisterIns")

            self.csipstatstrafficregisterouts = YLeaf(YType.uint32, "cSipStatsTrafficRegisterOuts")

            self.csipstatstrafficsubscribeins = YLeaf(YType.uint32, "cSipStatsTrafficSubscribeIns")

            self.csipstatstrafficsubscribeouts = YLeaf(YType.uint32, "cSipStatsTrafficSubscribeOuts")

            self.csipstatstrafficupdateins = YLeaf(YType.uint32, "cSipStatsTrafficUpdateIns")

            self.csipstatstrafficupdateouts = YLeaf(YType.uint32, "cSipStatsTrafficUpdateOuts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatstrafficackins",
                            "csipstatstrafficackouts",
                            "csipstatstrafficbyeins",
                            "csipstatstrafficbyeouts",
                            "csipstatstrafficcancelins",
                            "csipstatstrafficcancelouts",
                            "csipstatstrafficcometins",
                            "csipstatstrafficcometouts",
                            "csipstatstrafficinfoins",
                            "csipstatstrafficinfoouts",
                            "csipstatstrafficinviteins",
                            "csipstatstrafficinviteouts",
                            "csipstatstrafficnotifyins",
                            "csipstatstrafficnotifyouts",
                            "csipstatstrafficoptionsins",
                            "csipstatstrafficoptionsouts",
                            "csipstatstrafficprackins",
                            "csipstatstrafficprackouts",
                            "csipstatstrafficreferins",
                            "csipstatstrafficreferouts",
                            "csipstatstrafficregisterins",
                            "csipstatstrafficregisterouts",
                            "csipstatstrafficsubscribeins",
                            "csipstatstrafficsubscribeouts",
                            "csipstatstrafficupdateins",
                            "csipstatstrafficupdateouts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatstraffic, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatstraffic, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatstrafficackins.is_set or
                self.csipstatstrafficackouts.is_set or
                self.csipstatstrafficbyeins.is_set or
                self.csipstatstrafficbyeouts.is_set or
                self.csipstatstrafficcancelins.is_set or
                self.csipstatstrafficcancelouts.is_set or
                self.csipstatstrafficcometins.is_set or
                self.csipstatstrafficcometouts.is_set or
                self.csipstatstrafficinfoins.is_set or
                self.csipstatstrafficinfoouts.is_set or
                self.csipstatstrafficinviteins.is_set or
                self.csipstatstrafficinviteouts.is_set or
                self.csipstatstrafficnotifyins.is_set or
                self.csipstatstrafficnotifyouts.is_set or
                self.csipstatstrafficoptionsins.is_set or
                self.csipstatstrafficoptionsouts.is_set or
                self.csipstatstrafficprackins.is_set or
                self.csipstatstrafficprackouts.is_set or
                self.csipstatstrafficreferins.is_set or
                self.csipstatstrafficreferouts.is_set or
                self.csipstatstrafficregisterins.is_set or
                self.csipstatstrafficregisterouts.is_set or
                self.csipstatstrafficsubscribeins.is_set or
                self.csipstatstrafficsubscribeouts.is_set or
                self.csipstatstrafficupdateins.is_set or
                self.csipstatstrafficupdateouts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatstrafficackins.yfilter != YFilter.not_set or
                self.csipstatstrafficackouts.yfilter != YFilter.not_set or
                self.csipstatstrafficbyeins.yfilter != YFilter.not_set or
                self.csipstatstrafficbyeouts.yfilter != YFilter.not_set or
                self.csipstatstrafficcancelins.yfilter != YFilter.not_set or
                self.csipstatstrafficcancelouts.yfilter != YFilter.not_set or
                self.csipstatstrafficcometins.yfilter != YFilter.not_set or
                self.csipstatstrafficcometouts.yfilter != YFilter.not_set or
                self.csipstatstrafficinfoins.yfilter != YFilter.not_set or
                self.csipstatstrafficinfoouts.yfilter != YFilter.not_set or
                self.csipstatstrafficinviteins.yfilter != YFilter.not_set or
                self.csipstatstrafficinviteouts.yfilter != YFilter.not_set or
                self.csipstatstrafficnotifyins.yfilter != YFilter.not_set or
                self.csipstatstrafficnotifyouts.yfilter != YFilter.not_set or
                self.csipstatstrafficoptionsins.yfilter != YFilter.not_set or
                self.csipstatstrafficoptionsouts.yfilter != YFilter.not_set or
                self.csipstatstrafficprackins.yfilter != YFilter.not_set or
                self.csipstatstrafficprackouts.yfilter != YFilter.not_set or
                self.csipstatstrafficreferins.yfilter != YFilter.not_set or
                self.csipstatstrafficreferouts.yfilter != YFilter.not_set or
                self.csipstatstrafficregisterins.yfilter != YFilter.not_set or
                self.csipstatstrafficregisterouts.yfilter != YFilter.not_set or
                self.csipstatstrafficsubscribeins.yfilter != YFilter.not_set or
                self.csipstatstrafficsubscribeouts.yfilter != YFilter.not_set or
                self.csipstatstrafficupdateins.yfilter != YFilter.not_set or
                self.csipstatstrafficupdateouts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsTraffic" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatstrafficackins.is_set or self.csipstatstrafficackins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficackins.get_name_leafdata())
            if (self.csipstatstrafficackouts.is_set or self.csipstatstrafficackouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficackouts.get_name_leafdata())
            if (self.csipstatstrafficbyeins.is_set or self.csipstatstrafficbyeins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficbyeins.get_name_leafdata())
            if (self.csipstatstrafficbyeouts.is_set or self.csipstatstrafficbyeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficbyeouts.get_name_leafdata())
            if (self.csipstatstrafficcancelins.is_set or self.csipstatstrafficcancelins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficcancelins.get_name_leafdata())
            if (self.csipstatstrafficcancelouts.is_set or self.csipstatstrafficcancelouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficcancelouts.get_name_leafdata())
            if (self.csipstatstrafficcometins.is_set or self.csipstatstrafficcometins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficcometins.get_name_leafdata())
            if (self.csipstatstrafficcometouts.is_set or self.csipstatstrafficcometouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficcometouts.get_name_leafdata())
            if (self.csipstatstrafficinfoins.is_set or self.csipstatstrafficinfoins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficinfoins.get_name_leafdata())
            if (self.csipstatstrafficinfoouts.is_set or self.csipstatstrafficinfoouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficinfoouts.get_name_leafdata())
            if (self.csipstatstrafficinviteins.is_set or self.csipstatstrafficinviteins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficinviteins.get_name_leafdata())
            if (self.csipstatstrafficinviteouts.is_set or self.csipstatstrafficinviteouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficinviteouts.get_name_leafdata())
            if (self.csipstatstrafficnotifyins.is_set or self.csipstatstrafficnotifyins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficnotifyins.get_name_leafdata())
            if (self.csipstatstrafficnotifyouts.is_set or self.csipstatstrafficnotifyouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficnotifyouts.get_name_leafdata())
            if (self.csipstatstrafficoptionsins.is_set or self.csipstatstrafficoptionsins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficoptionsins.get_name_leafdata())
            if (self.csipstatstrafficoptionsouts.is_set or self.csipstatstrafficoptionsouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficoptionsouts.get_name_leafdata())
            if (self.csipstatstrafficprackins.is_set or self.csipstatstrafficprackins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficprackins.get_name_leafdata())
            if (self.csipstatstrafficprackouts.is_set or self.csipstatstrafficprackouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficprackouts.get_name_leafdata())
            if (self.csipstatstrafficreferins.is_set or self.csipstatstrafficreferins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficreferins.get_name_leafdata())
            if (self.csipstatstrafficreferouts.is_set or self.csipstatstrafficreferouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficreferouts.get_name_leafdata())
            if (self.csipstatstrafficregisterins.is_set or self.csipstatstrafficregisterins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficregisterins.get_name_leafdata())
            if (self.csipstatstrafficregisterouts.is_set or self.csipstatstrafficregisterouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficregisterouts.get_name_leafdata())
            if (self.csipstatstrafficsubscribeins.is_set or self.csipstatstrafficsubscribeins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficsubscribeins.get_name_leafdata())
            if (self.csipstatstrafficsubscribeouts.is_set or self.csipstatstrafficsubscribeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficsubscribeouts.get_name_leafdata())
            if (self.csipstatstrafficupdateins.is_set or self.csipstatstrafficupdateins.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficupdateins.get_name_leafdata())
            if (self.csipstatstrafficupdateouts.is_set or self.csipstatstrafficupdateouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatstrafficupdateouts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsTrafficAckIns" or name == "cSipStatsTrafficAckOuts" or name == "cSipStatsTrafficByeIns" or name == "cSipStatsTrafficByeOuts" or name == "cSipStatsTrafficCancelIns" or name == "cSipStatsTrafficCancelOuts" or name == "cSipStatsTrafficCometIns" or name == "cSipStatsTrafficCometOuts" or name == "cSipStatsTrafficInfoIns" or name == "cSipStatsTrafficInfoOuts" or name == "cSipStatsTrafficInviteIns" or name == "cSipStatsTrafficInviteOuts" or name == "cSipStatsTrafficNotifyIns" or name == "cSipStatsTrafficNotifyOuts" or name == "cSipStatsTrafficOptionsIns" or name == "cSipStatsTrafficOptionsOuts" or name == "cSipStatsTrafficPrackIns" or name == "cSipStatsTrafficPrackOuts" or name == "cSipStatsTrafficReferIns" or name == "cSipStatsTrafficReferOuts" or name == "cSipStatsTrafficRegisterIns" or name == "cSipStatsTrafficRegisterOuts" or name == "cSipStatsTrafficSubscribeIns" or name == "cSipStatsTrafficSubscribeOuts" or name == "cSipStatsTrafficUpdateIns" or name == "cSipStatsTrafficUpdateOuts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsTrafficAckIns"):
                self.csipstatstrafficackins = value
                self.csipstatstrafficackins.value_namespace = name_space
                self.csipstatstrafficackins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficAckOuts"):
                self.csipstatstrafficackouts = value
                self.csipstatstrafficackouts.value_namespace = name_space
                self.csipstatstrafficackouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficByeIns"):
                self.csipstatstrafficbyeins = value
                self.csipstatstrafficbyeins.value_namespace = name_space
                self.csipstatstrafficbyeins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficByeOuts"):
                self.csipstatstrafficbyeouts = value
                self.csipstatstrafficbyeouts.value_namespace = name_space
                self.csipstatstrafficbyeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficCancelIns"):
                self.csipstatstrafficcancelins = value
                self.csipstatstrafficcancelins.value_namespace = name_space
                self.csipstatstrafficcancelins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficCancelOuts"):
                self.csipstatstrafficcancelouts = value
                self.csipstatstrafficcancelouts.value_namespace = name_space
                self.csipstatstrafficcancelouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficCometIns"):
                self.csipstatstrafficcometins = value
                self.csipstatstrafficcometins.value_namespace = name_space
                self.csipstatstrafficcometins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficCometOuts"):
                self.csipstatstrafficcometouts = value
                self.csipstatstrafficcometouts.value_namespace = name_space
                self.csipstatstrafficcometouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficInfoIns"):
                self.csipstatstrafficinfoins = value
                self.csipstatstrafficinfoins.value_namespace = name_space
                self.csipstatstrafficinfoins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficInfoOuts"):
                self.csipstatstrafficinfoouts = value
                self.csipstatstrafficinfoouts.value_namespace = name_space
                self.csipstatstrafficinfoouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficInviteIns"):
                self.csipstatstrafficinviteins = value
                self.csipstatstrafficinviteins.value_namespace = name_space
                self.csipstatstrafficinviteins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficInviteOuts"):
                self.csipstatstrafficinviteouts = value
                self.csipstatstrafficinviteouts.value_namespace = name_space
                self.csipstatstrafficinviteouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficNotifyIns"):
                self.csipstatstrafficnotifyins = value
                self.csipstatstrafficnotifyins.value_namespace = name_space
                self.csipstatstrafficnotifyins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficNotifyOuts"):
                self.csipstatstrafficnotifyouts = value
                self.csipstatstrafficnotifyouts.value_namespace = name_space
                self.csipstatstrafficnotifyouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficOptionsIns"):
                self.csipstatstrafficoptionsins = value
                self.csipstatstrafficoptionsins.value_namespace = name_space
                self.csipstatstrafficoptionsins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficOptionsOuts"):
                self.csipstatstrafficoptionsouts = value
                self.csipstatstrafficoptionsouts.value_namespace = name_space
                self.csipstatstrafficoptionsouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficPrackIns"):
                self.csipstatstrafficprackins = value
                self.csipstatstrafficprackins.value_namespace = name_space
                self.csipstatstrafficprackins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficPrackOuts"):
                self.csipstatstrafficprackouts = value
                self.csipstatstrafficprackouts.value_namespace = name_space
                self.csipstatstrafficprackouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficReferIns"):
                self.csipstatstrafficreferins = value
                self.csipstatstrafficreferins.value_namespace = name_space
                self.csipstatstrafficreferins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficReferOuts"):
                self.csipstatstrafficreferouts = value
                self.csipstatstrafficreferouts.value_namespace = name_space
                self.csipstatstrafficreferouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficRegisterIns"):
                self.csipstatstrafficregisterins = value
                self.csipstatstrafficregisterins.value_namespace = name_space
                self.csipstatstrafficregisterins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficRegisterOuts"):
                self.csipstatstrafficregisterouts = value
                self.csipstatstrafficregisterouts.value_namespace = name_space
                self.csipstatstrafficregisterouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficSubscribeIns"):
                self.csipstatstrafficsubscribeins = value
                self.csipstatstrafficsubscribeins.value_namespace = name_space
                self.csipstatstrafficsubscribeins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficSubscribeOuts"):
                self.csipstatstrafficsubscribeouts = value
                self.csipstatstrafficsubscribeouts.value_namespace = name_space
                self.csipstatstrafficsubscribeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficUpdateIns"):
                self.csipstatstrafficupdateins = value
                self.csipstatstrafficupdateins.value_namespace = name_space
                self.csipstatstrafficupdateins.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsTrafficUpdateOuts"):
                self.csipstatstrafficupdateouts = value
                self.csipstatstrafficupdateouts.value_namespace = name_space
                self.csipstatstrafficupdateouts.value_namespace_prefix = name_space_prefix


    class Csipstatsretry(Entity):
        """
        
        
        .. attribute:: csipstatsretrybyes
        
        	This object reflects the total number of BYE retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycancels
        
        	This object reflects the total number of CANCEL retries that  have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycomets
        
        	This object reflects the total number of COndition MET retries sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryinfo
        
        	This object reflects the total number of Info retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryinvites
        
        	This object reflects the total number of INVITE retries that  have been sent by the user agent since system startup.   If the number of 'first  attempt' INVITES is of interest, subtract the value of this  object from cSipStatsTrafficInviteOut
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrynotifys
        
        	This object reflects the total number of Notify  retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrypracks
        
        	This object reflects the total number of PRovisional ACKnowledgement retries sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryrefers
        
        	This object reflects the total number of Refer retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryregisters
        
        	This object reflects the total number of REGISTER retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryreliable1xxrsps
        
        	This object reflects the total number of Reliable 1xx Response retries sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryresponses
        
        	This object reflects the total number of Response (while  expecting a ACK) retries that have been sent by the user agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrysubscribe
        
        	This object reflects the total number of Subscribe retries that have been sent by the user agent since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsretry, self).__init__()

            self.yang_name = "cSipStatsRetry"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsretrybyes = YLeaf(YType.uint32, "cSipStatsRetryByes")

            self.csipstatsretrycancels = YLeaf(YType.uint32, "cSipStatsRetryCancels")

            self.csipstatsretrycomets = YLeaf(YType.uint32, "cSipStatsRetryComets")

            self.csipstatsretryinfo = YLeaf(YType.uint32, "cSipStatsRetryInfo")

            self.csipstatsretryinvites = YLeaf(YType.uint32, "cSipStatsRetryInvites")

            self.csipstatsretrynotifys = YLeaf(YType.uint32, "cSipStatsRetryNotifys")

            self.csipstatsretrypracks = YLeaf(YType.uint32, "cSipStatsRetryPracks")

            self.csipstatsretryrefers = YLeaf(YType.uint32, "cSipStatsRetryRefers")

            self.csipstatsretryregisters = YLeaf(YType.uint32, "cSipStatsRetryRegisters")

            self.csipstatsretryreliable1xxrsps = YLeaf(YType.uint32, "cSipStatsRetryReliable1xxRsps")

            self.csipstatsretryresponses = YLeaf(YType.uint32, "cSipStatsRetryResponses")

            self.csipstatsretrysubscribe = YLeaf(YType.uint32, "cSipStatsRetrySubscribe")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsretrybyes",
                            "csipstatsretrycancels",
                            "csipstatsretrycomets",
                            "csipstatsretryinfo",
                            "csipstatsretryinvites",
                            "csipstatsretrynotifys",
                            "csipstatsretrypracks",
                            "csipstatsretryrefers",
                            "csipstatsretryregisters",
                            "csipstatsretryreliable1xxrsps",
                            "csipstatsretryresponses",
                            "csipstatsretrysubscribe") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsretry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsretry, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsretrybyes.is_set or
                self.csipstatsretrycancels.is_set or
                self.csipstatsretrycomets.is_set or
                self.csipstatsretryinfo.is_set or
                self.csipstatsretryinvites.is_set or
                self.csipstatsretrynotifys.is_set or
                self.csipstatsretrypracks.is_set or
                self.csipstatsretryrefers.is_set or
                self.csipstatsretryregisters.is_set or
                self.csipstatsretryreliable1xxrsps.is_set or
                self.csipstatsretryresponses.is_set or
                self.csipstatsretrysubscribe.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsretrybyes.yfilter != YFilter.not_set or
                self.csipstatsretrycancels.yfilter != YFilter.not_set or
                self.csipstatsretrycomets.yfilter != YFilter.not_set or
                self.csipstatsretryinfo.yfilter != YFilter.not_set or
                self.csipstatsretryinvites.yfilter != YFilter.not_set or
                self.csipstatsretrynotifys.yfilter != YFilter.not_set or
                self.csipstatsretrypracks.yfilter != YFilter.not_set or
                self.csipstatsretryrefers.yfilter != YFilter.not_set or
                self.csipstatsretryregisters.yfilter != YFilter.not_set or
                self.csipstatsretryreliable1xxrsps.yfilter != YFilter.not_set or
                self.csipstatsretryresponses.yfilter != YFilter.not_set or
                self.csipstatsretrysubscribe.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsRetry" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsretrybyes.is_set or self.csipstatsretrybyes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrybyes.get_name_leafdata())
            if (self.csipstatsretrycancels.is_set or self.csipstatsretrycancels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrycancels.get_name_leafdata())
            if (self.csipstatsretrycomets.is_set or self.csipstatsretrycomets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrycomets.get_name_leafdata())
            if (self.csipstatsretryinfo.is_set or self.csipstatsretryinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryinfo.get_name_leafdata())
            if (self.csipstatsretryinvites.is_set or self.csipstatsretryinvites.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryinvites.get_name_leafdata())
            if (self.csipstatsretrynotifys.is_set or self.csipstatsretrynotifys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrynotifys.get_name_leafdata())
            if (self.csipstatsretrypracks.is_set or self.csipstatsretrypracks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrypracks.get_name_leafdata())
            if (self.csipstatsretryrefers.is_set or self.csipstatsretryrefers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryrefers.get_name_leafdata())
            if (self.csipstatsretryregisters.is_set or self.csipstatsretryregisters.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryregisters.get_name_leafdata())
            if (self.csipstatsretryreliable1xxrsps.is_set or self.csipstatsretryreliable1xxrsps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryreliable1xxrsps.get_name_leafdata())
            if (self.csipstatsretryresponses.is_set or self.csipstatsretryresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretryresponses.get_name_leafdata())
            if (self.csipstatsretrysubscribe.is_set or self.csipstatsretrysubscribe.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsretrysubscribe.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsRetryByes" or name == "cSipStatsRetryCancels" or name == "cSipStatsRetryComets" or name == "cSipStatsRetryInfo" or name == "cSipStatsRetryInvites" or name == "cSipStatsRetryNotifys" or name == "cSipStatsRetryPracks" or name == "cSipStatsRetryRefers" or name == "cSipStatsRetryRegisters" or name == "cSipStatsRetryReliable1xxRsps" or name == "cSipStatsRetryResponses" or name == "cSipStatsRetrySubscribe"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsRetryByes"):
                self.csipstatsretrybyes = value
                self.csipstatsretrybyes.value_namespace = name_space
                self.csipstatsretrybyes.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryCancels"):
                self.csipstatsretrycancels = value
                self.csipstatsretrycancels.value_namespace = name_space
                self.csipstatsretrycancels.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryComets"):
                self.csipstatsretrycomets = value
                self.csipstatsretrycomets.value_namespace = name_space
                self.csipstatsretrycomets.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryInfo"):
                self.csipstatsretryinfo = value
                self.csipstatsretryinfo.value_namespace = name_space
                self.csipstatsretryinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryInvites"):
                self.csipstatsretryinvites = value
                self.csipstatsretryinvites.value_namespace = name_space
                self.csipstatsretryinvites.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryNotifys"):
                self.csipstatsretrynotifys = value
                self.csipstatsretrynotifys.value_namespace = name_space
                self.csipstatsretrynotifys.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryPracks"):
                self.csipstatsretrypracks = value
                self.csipstatsretrypracks.value_namespace = name_space
                self.csipstatsretrypracks.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryRefers"):
                self.csipstatsretryrefers = value
                self.csipstatsretryrefers.value_namespace = name_space
                self.csipstatsretryrefers.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryRegisters"):
                self.csipstatsretryregisters = value
                self.csipstatsretryregisters.value_namespace = name_space
                self.csipstatsretryregisters.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryReliable1xxRsps"):
                self.csipstatsretryreliable1xxrsps = value
                self.csipstatsretryreliable1xxrsps.value_namespace = name_space
                self.csipstatsretryreliable1xxrsps.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetryResponses"):
                self.csipstatsretryresponses = value
                self.csipstatsretryresponses.value_namespace = name_space
                self.csipstatsretryresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsRetrySubscribe"):
                self.csipstatsretrysubscribe = value
                self.csipstatsretrysubscribe.value_namespace = name_space
                self.csipstatsretrysubscribe.value_namespace_prefix = name_space_prefix


    class Csipstatsmisc(Entity):
        """
        
        
        .. attribute:: csipstatsmisc3xxmappedto4xxrsps
        
        	This object reflects the total number of incoming Redirect  (3xx) response messages that have been mapped to Client  Error (4xx) response messages
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsmisc, self).__init__()

            self.yang_name = "cSipStatsMisc"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsmisc3xxmappedto4xxrsps = YLeaf(YType.uint32, "cSipStatsMisc3xxMappedTo4xxRsps")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsmisc3xxmappedto4xxrsps") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsmisc, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsmisc, self).__setattr__(name, value)

        def has_data(self):
            return self.csipstatsmisc3xxmappedto4xxrsps.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsmisc3xxmappedto4xxrsps.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsMisc" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsmisc3xxmappedto4xxrsps.is_set or self.csipstatsmisc3xxmappedto4xxrsps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsmisc3xxmappedto4xxrsps.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsMisc3xxMappedTo4xxRsps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsMisc3xxMappedTo4xxRsps"):
                self.csipstatsmisc3xxmappedto4xxrsps = value
                self.csipstatsmisc3xxmappedto4xxrsps.value_namespace = name_space
                self.csipstatsmisc3xxmappedto4xxrsps.value_namespace_prefix = name_space_prefix


    class Csipstatsconnection(Entity):
        """
        
        
        .. attribute:: csipstatsactivetcpconnections
        
        	This object reflects the total number of active TCP connections since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsactiveudpconnections
        
        	This object reflects the total number of active UDP connections since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpcreatefailures
        
        	This object reflects the total number of connection create failures for TCP since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpinactivetimeouts
        
        	This object reflects the total number of TCP connections that timed out due to inactivity since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpremoteclosures
        
        	This object reflects the total number of Remote Closures  for TCP since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpsendfailures
        
        	This object reflects the total number of TCP send failures since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpcreatefailures
        
        	This object reflects the total number of connection create failures for UDP since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpinactivetimeouts
        
        	This object reflects the total number of UDP connections that  timed out due to inactivity since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpsendfailures
        
        	This object reflects the total number of UDP send failures since system startup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatsconnection, self).__init__()

            self.yang_name = "cSipStatsConnection"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatsactivetcpconnections = YLeaf(YType.uint32, "cSipStatsActiveTCPConnections")

            self.csipstatsactiveudpconnections = YLeaf(YType.uint32, "cSipStatsActiveUDPConnections")

            self.csipstatsconntcpcreatefailures = YLeaf(YType.uint32, "cSipStatsConnTCPCreateFailures")

            self.csipstatsconntcpinactivetimeouts = YLeaf(YType.uint32, "cSipStatsConnTCPInactiveTimeouts")

            self.csipstatsconntcpremoteclosures = YLeaf(YType.uint32, "cSipStatsConnTCPRemoteClosures")

            self.csipstatsconntcpsendfailures = YLeaf(YType.uint32, "cSipStatsConnTCPSendFailures")

            self.csipstatsconnudpcreatefailures = YLeaf(YType.uint32, "cSipStatsConnUDPCreateFailures")

            self.csipstatsconnudpinactivetimeouts = YLeaf(YType.uint32, "cSipStatsConnUDPInactiveTimeouts")

            self.csipstatsconnudpsendfailures = YLeaf(YType.uint32, "cSipStatsConnUDPSendFailures")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csipstatsactivetcpconnections",
                            "csipstatsactiveudpconnections",
                            "csipstatsconntcpcreatefailures",
                            "csipstatsconntcpinactivetimeouts",
                            "csipstatsconntcpremoteclosures",
                            "csipstatsconntcpsendfailures",
                            "csipstatsconnudpcreatefailures",
                            "csipstatsconnudpinactivetimeouts",
                            "csipstatsconnudpsendfailures") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSipUaMib.Csipstatsconnection, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatsconnection, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csipstatsactivetcpconnections.is_set or
                self.csipstatsactiveudpconnections.is_set or
                self.csipstatsconntcpcreatefailures.is_set or
                self.csipstatsconntcpinactivetimeouts.is_set or
                self.csipstatsconntcpremoteclosures.is_set or
                self.csipstatsconntcpsendfailures.is_set or
                self.csipstatsconnudpcreatefailures.is_set or
                self.csipstatsconnudpinactivetimeouts.is_set or
                self.csipstatsconnudpsendfailures.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csipstatsactivetcpconnections.yfilter != YFilter.not_set or
                self.csipstatsactiveudpconnections.yfilter != YFilter.not_set or
                self.csipstatsconntcpcreatefailures.yfilter != YFilter.not_set or
                self.csipstatsconntcpinactivetimeouts.yfilter != YFilter.not_set or
                self.csipstatsconntcpremoteclosures.yfilter != YFilter.not_set or
                self.csipstatsconntcpsendfailures.yfilter != YFilter.not_set or
                self.csipstatsconnudpcreatefailures.yfilter != YFilter.not_set or
                self.csipstatsconnudpinactivetimeouts.yfilter != YFilter.not_set or
                self.csipstatsconnudpsendfailures.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsConnection" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csipstatsactivetcpconnections.is_set or self.csipstatsactivetcpconnections.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsactivetcpconnections.get_name_leafdata())
            if (self.csipstatsactiveudpconnections.is_set or self.csipstatsactiveudpconnections.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsactiveudpconnections.get_name_leafdata())
            if (self.csipstatsconntcpcreatefailures.is_set or self.csipstatsconntcpcreatefailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconntcpcreatefailures.get_name_leafdata())
            if (self.csipstatsconntcpinactivetimeouts.is_set or self.csipstatsconntcpinactivetimeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconntcpinactivetimeouts.get_name_leafdata())
            if (self.csipstatsconntcpremoteclosures.is_set or self.csipstatsconntcpremoteclosures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconntcpremoteclosures.get_name_leafdata())
            if (self.csipstatsconntcpsendfailures.is_set or self.csipstatsconntcpsendfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconntcpsendfailures.get_name_leafdata())
            if (self.csipstatsconnudpcreatefailures.is_set or self.csipstatsconnudpcreatefailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconnudpcreatefailures.get_name_leafdata())
            if (self.csipstatsconnudpinactivetimeouts.is_set or self.csipstatsconnudpinactivetimeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconnudpinactivetimeouts.get_name_leafdata())
            if (self.csipstatsconnudpsendfailures.is_set or self.csipstatsconnudpsendfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csipstatsconnudpsendfailures.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsActiveTCPConnections" or name == "cSipStatsActiveUDPConnections" or name == "cSipStatsConnTCPCreateFailures" or name == "cSipStatsConnTCPInactiveTimeouts" or name == "cSipStatsConnTCPRemoteClosures" or name == "cSipStatsConnTCPSendFailures" or name == "cSipStatsConnUDPCreateFailures" or name == "cSipStatsConnUDPInactiveTimeouts" or name == "cSipStatsConnUDPSendFailures"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cSipStatsActiveTCPConnections"):
                self.csipstatsactivetcpconnections = value
                self.csipstatsactivetcpconnections.value_namespace = name_space
                self.csipstatsactivetcpconnections.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsActiveUDPConnections"):
                self.csipstatsactiveudpconnections = value
                self.csipstatsactiveudpconnections.value_namespace = name_space
                self.csipstatsactiveudpconnections.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnTCPCreateFailures"):
                self.csipstatsconntcpcreatefailures = value
                self.csipstatsconntcpcreatefailures.value_namespace = name_space
                self.csipstatsconntcpcreatefailures.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnTCPInactiveTimeouts"):
                self.csipstatsconntcpinactivetimeouts = value
                self.csipstatsconntcpinactivetimeouts.value_namespace = name_space
                self.csipstatsconntcpinactivetimeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnTCPRemoteClosures"):
                self.csipstatsconntcpremoteclosures = value
                self.csipstatsconntcpremoteclosures.value_namespace = name_space
                self.csipstatsconntcpremoteclosures.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnTCPSendFailures"):
                self.csipstatsconntcpsendfailures = value
                self.csipstatsconntcpsendfailures.value_namespace = name_space
                self.csipstatsconntcpsendfailures.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnUDPCreateFailures"):
                self.csipstatsconnudpcreatefailures = value
                self.csipstatsconnudpcreatefailures.value_namespace = name_space
                self.csipstatsconnudpcreatefailures.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnUDPInactiveTimeouts"):
                self.csipstatsconnudpinactivetimeouts = value
                self.csipstatsconnudpinactivetimeouts.value_namespace = name_space
                self.csipstatsconnudpinactivetimeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "cSipStatsConnUDPSendFailures"):
                self.csipstatsconnudpsendfailures = value
                self.csipstatsconnudpsendfailures.value_namespace = name_space
                self.csipstatsconnudpsendfailures.value_namespace_prefix = name_space_prefix


    class Csipcfgearlymediatable(Entity):
        """
        This table contains configuration for Early
        Media Cut Through.  The configuration controls
        how the SIP user agent will process 1xx
        (Provisional) SIP response messages that contain 
        Session Definition Protocol (SDP) payloads.
        
        .. attribute:: csipcfgearlymediaentry
        
        	A row in the cSipCfgEarlyMediaTable. A row is accessible with a Provisional (1xx) status code value (eg, 180) and provides an object for the enabling or disabling of the Early Media Cut Through functionality
        	**type**\: list of    :py:class:`Csipcfgearlymediaentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgearlymediatable.Csipcfgearlymediaentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgearlymediatable, self).__init__()

            self.yang_name = "cSipCfgEarlyMediaTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgearlymediaentry = YList(self)

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
                        super(CiscoSipUaMib.Csipcfgearlymediatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgearlymediatable, self).__setattr__(name, value)


        class Csipcfgearlymediaentry(Entity):
            """
            A row in the cSipCfgEarlyMediaTable.
            A row is accessible with a Provisional (1xx)
            status code value (eg, 180) and provides
            an object for the enabling or disabling of
            the Early Media Cut Through functionality.
            
            .. attribute:: csipcfgearlymediastatuscodeindex  <key>
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgearlymediacutthrudisabled
            
            	This object specifies whether Early Media  Cut Through is enabled or disabled for the  SIP response messages with status codes that  match cSipCfgEarlyMediaStatusCodeIndex.  If 'true', early media cut through is disabled, and the user agent will process the message as though it did not contain any SDP payload.  If 'false', early media cut through is enabled, and the user agent will process the message similar to a 183 (Session Progress) and cut through for early media.  The assumption being that the SDP is an indication that the far end is going to send early media
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipcfgearlymediatable.Csipcfgearlymediaentry, self).__init__()

                self.yang_name = "cSipCfgEarlyMediaEntry"
                self.yang_parent_name = "cSipCfgEarlyMediaTable"

                self.csipcfgearlymediastatuscodeindex = YLeaf(YType.int32, "cSipCfgEarlyMediaStatusCodeIndex")

                self.csipcfgearlymediacutthrudisabled = YLeaf(YType.boolean, "cSipCfgEarlyMediaCutThruDisabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipcfgearlymediastatuscodeindex",
                                "csipcfgearlymediacutthrudisabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipcfgearlymediatable.Csipcfgearlymediaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipcfgearlymediatable.Csipcfgearlymediaentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csipcfgearlymediastatuscodeindex.is_set or
                    self.csipcfgearlymediacutthrudisabled.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipcfgearlymediastatuscodeindex.yfilter != YFilter.not_set or
                    self.csipcfgearlymediacutthrudisabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipCfgEarlyMediaEntry" + "[cSipCfgEarlyMediaStatusCodeIndex='" + self.csipcfgearlymediastatuscodeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgEarlyMediaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipcfgearlymediastatuscodeindex.is_set or self.csipcfgearlymediastatuscodeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgearlymediastatuscodeindex.get_name_leafdata())
                if (self.csipcfgearlymediacutthrudisabled.is_set or self.csipcfgearlymediacutthrudisabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgearlymediacutthrudisabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipCfgEarlyMediaStatusCodeIndex" or name == "cSipCfgEarlyMediaCutThruDisabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipCfgEarlyMediaStatusCodeIndex"):
                    self.csipcfgearlymediastatuscodeindex = value
                    self.csipcfgearlymediastatuscodeindex.value_namespace = name_space
                    self.csipcfgearlymediastatuscodeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgEarlyMediaCutThruDisabled"):
                    self.csipcfgearlymediacutthrudisabled = value
                    self.csipcfgearlymediacutthrudisabled.value_namespace = name_space
                    self.csipcfgearlymediacutthrudisabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipcfgearlymediaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipcfgearlymediaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgEarlyMediaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipCfgEarlyMediaEntry"):
                for c in self.csipcfgearlymediaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipcfgearlymediatable.Csipcfgearlymediaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipcfgearlymediaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgEarlyMediaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csipcfgbindsourceaddrentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgbindsourceaddrtable, self).__init__()

            self.yang_name = "cSipCfgBindSourceAddrTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgbindsourceaddrentry = YList(self)

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
                        super(CiscoSipUaMib.Csipcfgbindsourceaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgbindsourceaddrtable, self).__setattr__(name, value)


        class Csipcfgbindsourceaddrentry(Entity):
            """
            A row in the cSipCfgBindSourceAddrTable.
            A row is accessible with the scope of packets
            to which the source IP address of the interface
            designated by cSipCfgBindSourceAddrInterface
            will be bound.
            
            .. attribute:: csipcfgbindsourceaddrscope  <key>
            
            	A unique identifier of a row in this table and specifies the scope of packets to which the source IP address of the interface designated by cSipCfgBindSourceAddrInterface will be bound
            	**type**\:   :py:class:`Csipcfgbindsourceaddrscope <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry.Csipcfgbindsourceaddrscope>`
            
            .. attribute:: csipcfgbindsourceaddrinterface
            
            	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that there is no specific source address configured and in this case the best local IP address will be chosen by the system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, self).__init__()

                self.yang_name = "cSipCfgBindSourceAddrEntry"
                self.yang_parent_name = "cSipCfgBindSourceAddrTable"

                self.csipcfgbindsourceaddrscope = YLeaf(YType.enumeration, "cSipCfgBindSourceAddrScope")

                self.csipcfgbindsourceaddrinterface = YLeaf(YType.int32, "cSipCfgBindSourceAddrInterface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipcfgbindsourceaddrscope",
                                "csipcfgbindsourceaddrinterface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.csipcfgbindsourceaddrscope.is_set or
                    self.csipcfgbindsourceaddrinterface.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipcfgbindsourceaddrscope.yfilter != YFilter.not_set or
                    self.csipcfgbindsourceaddrinterface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipCfgBindSourceAddrEntry" + "[cSipCfgBindSourceAddrScope='" + self.csipcfgbindsourceaddrscope.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgBindSourceAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipcfgbindsourceaddrscope.is_set or self.csipcfgbindsourceaddrscope.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgbindsourceaddrscope.get_name_leafdata())
                if (self.csipcfgbindsourceaddrinterface.is_set or self.csipcfgbindsourceaddrinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgbindsourceaddrinterface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipCfgBindSourceAddrScope" or name == "cSipCfgBindSourceAddrInterface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipCfgBindSourceAddrScope"):
                    self.csipcfgbindsourceaddrscope = value
                    self.csipcfgbindsourceaddrscope.value_namespace = name_space
                    self.csipcfgbindsourceaddrscope.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgBindSourceAddrInterface"):
                    self.csipcfgbindsourceaddrinterface = value
                    self.csipcfgbindsourceaddrinterface.value_namespace = name_space
                    self.csipcfgbindsourceaddrinterface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipcfgbindsourceaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipcfgbindsourceaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgBindSourceAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipCfgBindSourceAddrEntry"):
                for c in self.csipcfgbindsourceaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipcfgbindsourceaddrtable.Csipcfgbindsourceaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipcfgbindsourceaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgBindSourceAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csipcfgpeerentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgpeertable, self).__init__()

            self.yang_name = "cSipCfgPeerTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgpeerentry = YList(self)

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
                        super(CiscoSipUaMib.Csipcfgpeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgpeertable, self).__setattr__(name, value)


        class Csipcfgpeerentry(Entity):
            """
            A row in the cSipCfgPeerTable.
            
            .. attribute:: csipcfgpeerindex  <key>
            
            	An arbitrary index that uniquely identifies a  dial\-peer configured for SIP
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpeeroutsessiontransport
            
            	This object specifies the session transport  protocol that will be used by this dial\-peer for outbound SIP messages.    The value 'system' is the default and indicates  that this dial\-peer should use the value set by  cSipCfgOutSessionTransport instead
            	**type**\:   :py:class:`Csipcfgpeeroutsessiontransport <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeeroutsessiontransport>`
            
            .. attribute:: csipcfgpeerreliable1xxrsphdr
            
            	This object specifies behavior with respect to Support or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs.  The value 'system' is the default and indicates that this  dial\-peer should use the value of  cSipCfgReliable1xxRspHdr instead
            	**type**\:   :py:class:`Csipcfgpeerreliable1Xxrsphdr <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeerreliable1Xxrsphdr>`
            
            .. attribute:: csipcfgpeerreliable1xxrspstr
            
            	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgPeerReliable1xxRspHdr
            	**type**\:  str
            
            .. attribute:: csipcfgpeerswitchtransenabled
            
            	This object specifies if the functionality of switching between transports from UDP to TCP if the message size of a Request is greater than 1300 bytes is enabled or not
            	**type**\:  bool
            
            .. attribute:: csipcfgpeerurltype
            
            	This object specifies the URL type sent in outbound INVITES generated by this device.  The value 'system' is the default and indicates that this  dial\-peer should use the value of cSipCfgUrlType instead
            	**type**\:   :py:class:`Csipcfgpeerurltype <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry.Csipcfgpeerurltype>`
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry, self).__init__()

                self.yang_name = "cSipCfgPeerEntry"
                self.yang_parent_name = "cSipCfgPeerTable"

                self.csipcfgpeerindex = YLeaf(YType.int32, "cSipCfgPeerIndex")

                self.csipcfgpeeroutsessiontransport = YLeaf(YType.enumeration, "cSipCfgPeerOutSessionTransport")

                self.csipcfgpeerreliable1xxrsphdr = YLeaf(YType.enumeration, "cSipCfgPeerReliable1xxRspHdr")

                self.csipcfgpeerreliable1xxrspstr = YLeaf(YType.str, "cSipCfgPeerReliable1xxRspStr")

                self.csipcfgpeerswitchtransenabled = YLeaf(YType.boolean, "cSipCfgPeerSwitchTransEnabled")

                self.csipcfgpeerurltype = YLeaf(YType.enumeration, "cSipCfgPeerUrlType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipcfgpeerindex",
                                "csipcfgpeeroutsessiontransport",
                                "csipcfgpeerreliable1xxrsphdr",
                                "csipcfgpeerreliable1xxrspstr",
                                "csipcfgpeerswitchtransenabled",
                                "csipcfgpeerurltype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.csipcfgpeerindex.is_set or
                    self.csipcfgpeeroutsessiontransport.is_set or
                    self.csipcfgpeerreliable1xxrsphdr.is_set or
                    self.csipcfgpeerreliable1xxrspstr.is_set or
                    self.csipcfgpeerswitchtransenabled.is_set or
                    self.csipcfgpeerurltype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipcfgpeerindex.yfilter != YFilter.not_set or
                    self.csipcfgpeeroutsessiontransport.yfilter != YFilter.not_set or
                    self.csipcfgpeerreliable1xxrsphdr.yfilter != YFilter.not_set or
                    self.csipcfgpeerreliable1xxrspstr.yfilter != YFilter.not_set or
                    self.csipcfgpeerswitchtransenabled.yfilter != YFilter.not_set or
                    self.csipcfgpeerurltype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipCfgPeerEntry" + "[cSipCfgPeerIndex='" + self.csipcfgpeerindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipcfgpeerindex.is_set or self.csipcfgpeerindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeerindex.get_name_leafdata())
                if (self.csipcfgpeeroutsessiontransport.is_set or self.csipcfgpeeroutsessiontransport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeeroutsessiontransport.get_name_leafdata())
                if (self.csipcfgpeerreliable1xxrsphdr.is_set or self.csipcfgpeerreliable1xxrsphdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeerreliable1xxrsphdr.get_name_leafdata())
                if (self.csipcfgpeerreliable1xxrspstr.is_set or self.csipcfgpeerreliable1xxrspstr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeerreliable1xxrspstr.get_name_leafdata())
                if (self.csipcfgpeerswitchtransenabled.is_set or self.csipcfgpeerswitchtransenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeerswitchtransenabled.get_name_leafdata())
                if (self.csipcfgpeerurltype.is_set or self.csipcfgpeerurltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpeerurltype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipCfgPeerIndex" or name == "cSipCfgPeerOutSessionTransport" or name == "cSipCfgPeerReliable1xxRspHdr" or name == "cSipCfgPeerReliable1xxRspStr" or name == "cSipCfgPeerSwitchTransEnabled" or name == "cSipCfgPeerUrlType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipCfgPeerIndex"):
                    self.csipcfgpeerindex = value
                    self.csipcfgpeerindex.value_namespace = name_space
                    self.csipcfgpeerindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPeerOutSessionTransport"):
                    self.csipcfgpeeroutsessiontransport = value
                    self.csipcfgpeeroutsessiontransport.value_namespace = name_space
                    self.csipcfgpeeroutsessiontransport.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPeerReliable1xxRspHdr"):
                    self.csipcfgpeerreliable1xxrsphdr = value
                    self.csipcfgpeerreliable1xxrsphdr.value_namespace = name_space
                    self.csipcfgpeerreliable1xxrsphdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPeerReliable1xxRspStr"):
                    self.csipcfgpeerreliable1xxrspstr = value
                    self.csipcfgpeerreliable1xxrspstr.value_namespace = name_space
                    self.csipcfgpeerreliable1xxrspstr.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPeerSwitchTransEnabled"):
                    self.csipcfgpeerswitchtransenabled = value
                    self.csipcfgpeerswitchtransenabled.value_namespace = name_space
                    self.csipcfgpeerswitchtransenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPeerUrlType"):
                    self.csipcfgpeerurltype = value
                    self.csipcfgpeerurltype.value_namespace = name_space
                    self.csipcfgpeerurltype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipcfgpeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipcfgpeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipCfgPeerEntry"):
                for c in self.csipcfgpeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipcfgpeertable.Csipcfgpeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipcfgpeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csipcfgstatuscauseentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgstatuscausetable.Csipcfgstatuscauseentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgstatuscausetable, self).__init__()

            self.yang_name = "cSipCfgStatusCauseTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgstatuscauseentry = YList(self)

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
                        super(CiscoSipUaMib.Csipcfgstatuscausetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgstatuscausetable, self).__setattr__(name, value)


        class Csipcfgstatuscauseentry(Entity):
            """
            A row in the cSipCfgStatusCauseTable.  Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgstatuscodeindex  <key>
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpstncause
            
            	The PSTN cause code to which the SIP status code given by cSipCfgStatusCodeIndex is to be mapped for outbound PSTN signalling messages
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgstatuscausestorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipcfgstatuscausetable.Csipcfgstatuscauseentry, self).__init__()

                self.yang_name = "cSipCfgStatusCauseEntry"
                self.yang_parent_name = "cSipCfgStatusCauseTable"

                self.csipcfgstatuscodeindex = YLeaf(YType.int32, "cSipCfgStatusCodeIndex")

                self.csipcfgpstncause = YLeaf(YType.int32, "cSipCfgPstnCause")

                self.csipcfgstatuscausestorestatus = YLeaf(YType.enumeration, "cSipCfgStatusCauseStoreStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipcfgstatuscodeindex",
                                "csipcfgpstncause",
                                "csipcfgstatuscausestorestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipcfgstatuscausetable.Csipcfgstatuscauseentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipcfgstatuscausetable.Csipcfgstatuscauseentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csipcfgstatuscodeindex.is_set or
                    self.csipcfgpstncause.is_set or
                    self.csipcfgstatuscausestorestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipcfgstatuscodeindex.yfilter != YFilter.not_set or
                    self.csipcfgpstncause.yfilter != YFilter.not_set or
                    self.csipcfgstatuscausestorestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipCfgStatusCauseEntry" + "[cSipCfgStatusCodeIndex='" + self.csipcfgstatuscodeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgStatusCauseTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipcfgstatuscodeindex.is_set or self.csipcfgstatuscodeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgstatuscodeindex.get_name_leafdata())
                if (self.csipcfgpstncause.is_set or self.csipcfgpstncause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpstncause.get_name_leafdata())
                if (self.csipcfgstatuscausestorestatus.is_set or self.csipcfgstatuscausestorestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgstatuscausestorestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipCfgStatusCodeIndex" or name == "cSipCfgPstnCause" or name == "cSipCfgStatusCauseStoreStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipCfgStatusCodeIndex"):
                    self.csipcfgstatuscodeindex = value
                    self.csipcfgstatuscodeindex.value_namespace = name_space
                    self.csipcfgstatuscodeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgPstnCause"):
                    self.csipcfgpstncause = value
                    self.csipcfgpstncause.value_namespace = name_space
                    self.csipcfgpstncause.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgStatusCauseStoreStatus"):
                    self.csipcfgstatuscausestorestatus = value
                    self.csipcfgstatuscausestorestatus.value_namespace = name_space
                    self.csipcfgstatuscausestorestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipcfgstatuscauseentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipcfgstatuscauseentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgStatusCauseTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipCfgStatusCauseEntry"):
                for c in self.csipcfgstatuscauseentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipcfgstatuscausetable.Csipcfgstatuscauseentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipcfgstatuscauseentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgStatusCauseEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Csipcfgcausestatusentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipcfgcausestatustable.Csipcfgcausestatusentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipcfgcausestatustable, self).__init__()

            self.yang_name = "cSipCfgCauseStatusTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipcfgcausestatusentry = YList(self)

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
                        super(CiscoSipUaMib.Csipcfgcausestatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipcfgcausestatustable, self).__setattr__(name, value)


        class Csipcfgcausestatusentry(Entity):
            """
            A row in the cSipCfgCauseStatusTable. Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgpstncauseindex  <key>
            
            	A unique identifier of a row in this table and a valid PSTN cause code
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgcausestatusstorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: csipcfgstatuscode
            
            	The SIP status code to which the PSTN cause code given by cSipCfgPstnCauseIndex is to be mapped for outbound SIP response messages
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipcfgcausestatustable.Csipcfgcausestatusentry, self).__init__()

                self.yang_name = "cSipCfgCauseStatusEntry"
                self.yang_parent_name = "cSipCfgCauseStatusTable"

                self.csipcfgpstncauseindex = YLeaf(YType.int32, "cSipCfgPstnCauseIndex")

                self.csipcfgcausestatusstorestatus = YLeaf(YType.enumeration, "cSipCfgCauseStatusStoreStatus")

                self.csipcfgstatuscode = YLeaf(YType.int32, "cSipCfgStatusCode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipcfgpstncauseindex",
                                "csipcfgcausestatusstorestatus",
                                "csipcfgstatuscode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipcfgcausestatustable.Csipcfgcausestatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipcfgcausestatustable.Csipcfgcausestatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csipcfgpstncauseindex.is_set or
                    self.csipcfgcausestatusstorestatus.is_set or
                    self.csipcfgstatuscode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipcfgpstncauseindex.yfilter != YFilter.not_set or
                    self.csipcfgcausestatusstorestatus.yfilter != YFilter.not_set or
                    self.csipcfgstatuscode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipCfgCauseStatusEntry" + "[cSipCfgPstnCauseIndex='" + self.csipcfgpstncauseindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipCfgCauseStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipcfgpstncauseindex.is_set or self.csipcfgpstncauseindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgpstncauseindex.get_name_leafdata())
                if (self.csipcfgcausestatusstorestatus.is_set or self.csipcfgcausestatusstorestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgcausestatusstorestatus.get_name_leafdata())
                if (self.csipcfgstatuscode.is_set or self.csipcfgstatuscode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipcfgstatuscode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipCfgPstnCauseIndex" or name == "cSipCfgCauseStatusStoreStatus" or name == "cSipCfgStatusCode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipCfgPstnCauseIndex"):
                    self.csipcfgpstncauseindex = value
                    self.csipcfgpstncauseindex.value_namespace = name_space
                    self.csipcfgpstncauseindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgCauseStatusStoreStatus"):
                    self.csipcfgcausestatusstorestatus = value
                    self.csipcfgcausestatusstorestatus.value_namespace = name_space
                    self.csipcfgcausestatusstorestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipCfgStatusCode"):
                    self.csipcfgstatuscode = value
                    self.csipcfgstatuscode.value_namespace = name_space
                    self.csipcfgstatuscode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipcfgcausestatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipcfgcausestatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipCfgCauseStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipCfgCauseStatusEntry"):
                for c in self.csipcfgcausestatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipcfgcausestatustable.Csipcfgcausestatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipcfgcausestatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipCfgCauseStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csipstatssuccessoktable(Entity):
        """
        This table contains statistics for sent and
        received 200 Ok response messages.  The 
        statistics are kept on per SIP method basis.
        
        .. attribute:: csipstatssuccessokentry
        
        	A row in the cSipStatsSuccessOkTable.  There is  an entry for each SIP method for which 200 Ok  inbound and/or outbound statistics are kept
        	**type**\: list of    :py:class:`Csipstatssuccessokentry <ydk.models.cisco_ios_xe.CISCO_SIP_UA_MIB.CiscoSipUaMib.Csipstatssuccessoktable.Csipstatssuccessokentry>`
        
        

        """

        _prefix = 'CISCO-SIP-UA-MIB'
        _revision = '2004-02-19'

        def __init__(self):
            super(CiscoSipUaMib.Csipstatssuccessoktable, self).__init__()

            self.yang_name = "cSipStatsSuccessOkTable"
            self.yang_parent_name = "CISCO-SIP-UA-MIB"

            self.csipstatssuccessokentry = YList(self)

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
                        super(CiscoSipUaMib.Csipstatssuccessoktable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSipUaMib.Csipstatssuccessoktable, self).__setattr__(name, value)


        class Csipstatssuccessokentry(Entity):
            """
            A row in the cSipStatsSuccessOkTable.  There is 
            an entry for each SIP method for which 200 Ok 
            inbound and/or outbound statistics are kept.
            
            .. attribute:: csipstatssuccessokmethod  <key>
            
            	This object is used for instance identification of objects in this table.  The value reflects a SIP method
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: csipstatssuccessokinbounds
            
            	This object reflects the total number of Ok (200) responses sent by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csipstatssuccessokoutbounds
            
            	This object reflects the total number of Ok (200) responses received by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-SIP-UA-MIB'
            _revision = '2004-02-19'

            def __init__(self):
                super(CiscoSipUaMib.Csipstatssuccessoktable.Csipstatssuccessokentry, self).__init__()

                self.yang_name = "cSipStatsSuccessOkEntry"
                self.yang_parent_name = "cSipStatsSuccessOkTable"

                self.csipstatssuccessokmethod = YLeaf(YType.str, "cSipStatsSuccessOkMethod")

                self.csipstatssuccessokinbounds = YLeaf(YType.uint32, "cSipStatsSuccessOkInbounds")

                self.csipstatssuccessokoutbounds = YLeaf(YType.uint32, "cSipStatsSuccessOkOutbounds")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csipstatssuccessokmethod",
                                "csipstatssuccessokinbounds",
                                "csipstatssuccessokoutbounds") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSipUaMib.Csipstatssuccessoktable.Csipstatssuccessokentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSipUaMib.Csipstatssuccessoktable.Csipstatssuccessokentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csipstatssuccessokmethod.is_set or
                    self.csipstatssuccessokinbounds.is_set or
                    self.csipstatssuccessokoutbounds.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csipstatssuccessokmethod.yfilter != YFilter.not_set or
                    self.csipstatssuccessokinbounds.yfilter != YFilter.not_set or
                    self.csipstatssuccessokoutbounds.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cSipStatsSuccessOkEntry" + "[cSipStatsSuccessOkMethod='" + self.csipstatssuccessokmethod.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/cSipStatsSuccessOkTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csipstatssuccessokmethod.is_set or self.csipstatssuccessokmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipstatssuccessokmethod.get_name_leafdata())
                if (self.csipstatssuccessokinbounds.is_set or self.csipstatssuccessokinbounds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipstatssuccessokinbounds.get_name_leafdata())
                if (self.csipstatssuccessokoutbounds.is_set or self.csipstatssuccessokoutbounds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csipstatssuccessokoutbounds.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cSipStatsSuccessOkMethod" or name == "cSipStatsSuccessOkInbounds" or name == "cSipStatsSuccessOkOutbounds"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cSipStatsSuccessOkMethod"):
                    self.csipstatssuccessokmethod = value
                    self.csipstatssuccessokmethod.value_namespace = name_space
                    self.csipstatssuccessokmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipStatsSuccessOkInbounds"):
                    self.csipstatssuccessokinbounds = value
                    self.csipstatssuccessokinbounds.value_namespace = name_space
                    self.csipstatssuccessokinbounds.value_namespace_prefix = name_space_prefix
                if(value_path == "cSipStatsSuccessOkOutbounds"):
                    self.csipstatssuccessokoutbounds = value
                    self.csipstatssuccessokoutbounds.value_namespace = name_space
                    self.csipstatssuccessokoutbounds.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csipstatssuccessokentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csipstatssuccessokentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cSipStatsSuccessOkTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cSipStatsSuccessOkEntry"):
                for c in self.csipstatssuccessokentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSipUaMib.Csipstatssuccessoktable.Csipstatssuccessokentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csipstatssuccessokentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cSipStatsSuccessOkEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.csipcfgaaa is not None and self.csipcfgaaa.has_data()) or
            (self.csipcfgbase is not None and self.csipcfgbase.has_data()) or
            (self.csipcfgbindsourceaddrtable is not None and self.csipcfgbindsourceaddrtable.has_data()) or
            (self.csipcfgcausestatustable is not None and self.csipcfgcausestatustable.has_data()) or
            (self.csipcfgearlymediatable is not None and self.csipcfgearlymediatable.has_data()) or
            (self.csipcfgpeer is not None and self.csipcfgpeer.has_data()) or
            (self.csipcfgpeertable is not None and self.csipcfgpeertable.has_data()) or
            (self.csipcfgretry is not None and self.csipcfgretry.has_data()) or
            (self.csipcfgstatuscausetable is not None and self.csipcfgstatuscausetable.has_data()) or
            (self.csipcfgtimer is not None and self.csipcfgtimer.has_data()) or
            (self.csipcfgvoiceservicevoip is not None and self.csipcfgvoiceservicevoip.has_data()) or
            (self.csipstatsconnection is not None and self.csipstatsconnection.has_data()) or
            (self.csipstatserrclient is not None and self.csipstatserrclient.has_data()) or
            (self.csipstatserrserver is not None and self.csipstatserrserver.has_data()) or
            (self.csipstatsglobalfail is not None and self.csipstatsglobalfail.has_data()) or
            (self.csipstatsinfo is not None and self.csipstatsinfo.has_data()) or
            (self.csipstatsmisc is not None and self.csipstatsmisc.has_data()) or
            (self.csipstatsredirect is not None and self.csipstatsredirect.has_data()) or
            (self.csipstatsretry is not None and self.csipstatsretry.has_data()) or
            (self.csipstatssuccess is not None and self.csipstatssuccess.has_data()) or
            (self.csipstatssuccessoktable is not None and self.csipstatssuccessoktable.has_data()) or
            (self.csipstatstraffic is not None and self.csipstatstraffic.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.csipcfgaaa is not None and self.csipcfgaaa.has_operation()) or
            (self.csipcfgbase is not None and self.csipcfgbase.has_operation()) or
            (self.csipcfgbindsourceaddrtable is not None and self.csipcfgbindsourceaddrtable.has_operation()) or
            (self.csipcfgcausestatustable is not None and self.csipcfgcausestatustable.has_operation()) or
            (self.csipcfgearlymediatable is not None and self.csipcfgearlymediatable.has_operation()) or
            (self.csipcfgpeer is not None and self.csipcfgpeer.has_operation()) or
            (self.csipcfgpeertable is not None and self.csipcfgpeertable.has_operation()) or
            (self.csipcfgretry is not None and self.csipcfgretry.has_operation()) or
            (self.csipcfgstatuscausetable is not None and self.csipcfgstatuscausetable.has_operation()) or
            (self.csipcfgtimer is not None and self.csipcfgtimer.has_operation()) or
            (self.csipcfgvoiceservicevoip is not None and self.csipcfgvoiceservicevoip.has_operation()) or
            (self.csipstatsconnection is not None and self.csipstatsconnection.has_operation()) or
            (self.csipstatserrclient is not None and self.csipstatserrclient.has_operation()) or
            (self.csipstatserrserver is not None and self.csipstatserrserver.has_operation()) or
            (self.csipstatsglobalfail is not None and self.csipstatsglobalfail.has_operation()) or
            (self.csipstatsinfo is not None and self.csipstatsinfo.has_operation()) or
            (self.csipstatsmisc is not None and self.csipstatsmisc.has_operation()) or
            (self.csipstatsredirect is not None and self.csipstatsredirect.has_operation()) or
            (self.csipstatsretry is not None and self.csipstatsretry.has_operation()) or
            (self.csipstatssuccess is not None and self.csipstatssuccess.has_operation()) or
            (self.csipstatssuccessoktable is not None and self.csipstatssuccessoktable.has_operation()) or
            (self.csipstatstraffic is not None and self.csipstatstraffic.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB" + path_buffer

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

        if (child_yang_name == "cSipCfgAaa"):
            if (self.csipcfgaaa is None):
                self.csipcfgaaa = CiscoSipUaMib.Csipcfgaaa()
                self.csipcfgaaa.parent = self
                self._children_name_map["csipcfgaaa"] = "cSipCfgAaa"
            return self.csipcfgaaa

        if (child_yang_name == "cSipCfgBase"):
            if (self.csipcfgbase is None):
                self.csipcfgbase = CiscoSipUaMib.Csipcfgbase()
                self.csipcfgbase.parent = self
                self._children_name_map["csipcfgbase"] = "cSipCfgBase"
            return self.csipcfgbase

        if (child_yang_name == "cSipCfgBindSourceAddrTable"):
            if (self.csipcfgbindsourceaddrtable is None):
                self.csipcfgbindsourceaddrtable = CiscoSipUaMib.Csipcfgbindsourceaddrtable()
                self.csipcfgbindsourceaddrtable.parent = self
                self._children_name_map["csipcfgbindsourceaddrtable"] = "cSipCfgBindSourceAddrTable"
            return self.csipcfgbindsourceaddrtable

        if (child_yang_name == "cSipCfgCauseStatusTable"):
            if (self.csipcfgcausestatustable is None):
                self.csipcfgcausestatustable = CiscoSipUaMib.Csipcfgcausestatustable()
                self.csipcfgcausestatustable.parent = self
                self._children_name_map["csipcfgcausestatustable"] = "cSipCfgCauseStatusTable"
            return self.csipcfgcausestatustable

        if (child_yang_name == "cSipCfgEarlyMediaTable"):
            if (self.csipcfgearlymediatable is None):
                self.csipcfgearlymediatable = CiscoSipUaMib.Csipcfgearlymediatable()
                self.csipcfgearlymediatable.parent = self
                self._children_name_map["csipcfgearlymediatable"] = "cSipCfgEarlyMediaTable"
            return self.csipcfgearlymediatable

        if (child_yang_name == "cSipCfgPeer"):
            if (self.csipcfgpeer is None):
                self.csipcfgpeer = CiscoSipUaMib.Csipcfgpeer()
                self.csipcfgpeer.parent = self
                self._children_name_map["csipcfgpeer"] = "cSipCfgPeer"
            return self.csipcfgpeer

        if (child_yang_name == "cSipCfgPeerTable"):
            if (self.csipcfgpeertable is None):
                self.csipcfgpeertable = CiscoSipUaMib.Csipcfgpeertable()
                self.csipcfgpeertable.parent = self
                self._children_name_map["csipcfgpeertable"] = "cSipCfgPeerTable"
            return self.csipcfgpeertable

        if (child_yang_name == "cSipCfgRetry"):
            if (self.csipcfgretry is None):
                self.csipcfgretry = CiscoSipUaMib.Csipcfgretry()
                self.csipcfgretry.parent = self
                self._children_name_map["csipcfgretry"] = "cSipCfgRetry"
            return self.csipcfgretry

        if (child_yang_name == "cSipCfgStatusCauseTable"):
            if (self.csipcfgstatuscausetable is None):
                self.csipcfgstatuscausetable = CiscoSipUaMib.Csipcfgstatuscausetable()
                self.csipcfgstatuscausetable.parent = self
                self._children_name_map["csipcfgstatuscausetable"] = "cSipCfgStatusCauseTable"
            return self.csipcfgstatuscausetable

        if (child_yang_name == "cSipCfgTimer"):
            if (self.csipcfgtimer is None):
                self.csipcfgtimer = CiscoSipUaMib.Csipcfgtimer()
                self.csipcfgtimer.parent = self
                self._children_name_map["csipcfgtimer"] = "cSipCfgTimer"
            return self.csipcfgtimer

        if (child_yang_name == "cSipCfgVoiceServiceVoip"):
            if (self.csipcfgvoiceservicevoip is None):
                self.csipcfgvoiceservicevoip = CiscoSipUaMib.Csipcfgvoiceservicevoip()
                self.csipcfgvoiceservicevoip.parent = self
                self._children_name_map["csipcfgvoiceservicevoip"] = "cSipCfgVoiceServiceVoip"
            return self.csipcfgvoiceservicevoip

        if (child_yang_name == "cSipStatsConnection"):
            if (self.csipstatsconnection is None):
                self.csipstatsconnection = CiscoSipUaMib.Csipstatsconnection()
                self.csipstatsconnection.parent = self
                self._children_name_map["csipstatsconnection"] = "cSipStatsConnection"
            return self.csipstatsconnection

        if (child_yang_name == "cSipStatsErrClient"):
            if (self.csipstatserrclient is None):
                self.csipstatserrclient = CiscoSipUaMib.Csipstatserrclient()
                self.csipstatserrclient.parent = self
                self._children_name_map["csipstatserrclient"] = "cSipStatsErrClient"
            return self.csipstatserrclient

        if (child_yang_name == "cSipStatsErrServer"):
            if (self.csipstatserrserver is None):
                self.csipstatserrserver = CiscoSipUaMib.Csipstatserrserver()
                self.csipstatserrserver.parent = self
                self._children_name_map["csipstatserrserver"] = "cSipStatsErrServer"
            return self.csipstatserrserver

        if (child_yang_name == "cSipStatsGlobalFail"):
            if (self.csipstatsglobalfail is None):
                self.csipstatsglobalfail = CiscoSipUaMib.Csipstatsglobalfail()
                self.csipstatsglobalfail.parent = self
                self._children_name_map["csipstatsglobalfail"] = "cSipStatsGlobalFail"
            return self.csipstatsglobalfail

        if (child_yang_name == "cSipStatsInfo"):
            if (self.csipstatsinfo is None):
                self.csipstatsinfo = CiscoSipUaMib.Csipstatsinfo()
                self.csipstatsinfo.parent = self
                self._children_name_map["csipstatsinfo"] = "cSipStatsInfo"
            return self.csipstatsinfo

        if (child_yang_name == "cSipStatsMisc"):
            if (self.csipstatsmisc is None):
                self.csipstatsmisc = CiscoSipUaMib.Csipstatsmisc()
                self.csipstatsmisc.parent = self
                self._children_name_map["csipstatsmisc"] = "cSipStatsMisc"
            return self.csipstatsmisc

        if (child_yang_name == "cSipStatsRedirect"):
            if (self.csipstatsredirect is None):
                self.csipstatsredirect = CiscoSipUaMib.Csipstatsredirect()
                self.csipstatsredirect.parent = self
                self._children_name_map["csipstatsredirect"] = "cSipStatsRedirect"
            return self.csipstatsredirect

        if (child_yang_name == "cSipStatsRetry"):
            if (self.csipstatsretry is None):
                self.csipstatsretry = CiscoSipUaMib.Csipstatsretry()
                self.csipstatsretry.parent = self
                self._children_name_map["csipstatsretry"] = "cSipStatsRetry"
            return self.csipstatsretry

        if (child_yang_name == "cSipStatsSuccess"):
            if (self.csipstatssuccess is None):
                self.csipstatssuccess = CiscoSipUaMib.Csipstatssuccess()
                self.csipstatssuccess.parent = self
                self._children_name_map["csipstatssuccess"] = "cSipStatsSuccess"
            return self.csipstatssuccess

        if (child_yang_name == "cSipStatsSuccessOkTable"):
            if (self.csipstatssuccessoktable is None):
                self.csipstatssuccessoktable = CiscoSipUaMib.Csipstatssuccessoktable()
                self.csipstatssuccessoktable.parent = self
                self._children_name_map["csipstatssuccessoktable"] = "cSipStatsSuccessOkTable"
            return self.csipstatssuccessoktable

        if (child_yang_name == "cSipStatsTraffic"):
            if (self.csipstatstraffic is None):
                self.csipstatstraffic = CiscoSipUaMib.Csipstatstraffic()
                self.csipstatstraffic.parent = self
                self._children_name_map["csipstatstraffic"] = "cSipStatsTraffic"
            return self.csipstatstraffic

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cSipCfgAaa" or name == "cSipCfgBase" or name == "cSipCfgBindSourceAddrTable" or name == "cSipCfgCauseStatusTable" or name == "cSipCfgEarlyMediaTable" or name == "cSipCfgPeer" or name == "cSipCfgPeerTable" or name == "cSipCfgRetry" or name == "cSipCfgStatusCauseTable" or name == "cSipCfgTimer" or name == "cSipCfgVoiceServiceVoip" or name == "cSipStatsConnection" or name == "cSipStatsErrClient" or name == "cSipStatsErrServer" or name == "cSipStatsGlobalFail" or name == "cSipStatsInfo" or name == "cSipStatsMisc" or name == "cSipStatsRedirect" or name == "cSipStatsRetry" or name == "cSipStatsSuccess" or name == "cSipStatsSuccessOkTable" or name == "cSipStatsTraffic"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoSipUaMib()
        return self._top_entity

