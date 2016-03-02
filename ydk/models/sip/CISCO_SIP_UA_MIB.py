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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity_Identity
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCOSIPUAMIB(object):
    """
    
    
    .. attribute:: csipcfgaaa
    
    	
    	**type**\: :py:class:`CSipCfgAaa <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgAaa>`
    
    .. attribute:: csipcfgbase
    
    	
    	**type**\: :py:class:`CSipCfgBase <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase>`
    
    .. attribute:: csipcfgbindsourceaddrtable
    
    	This table contains configuration for binding the scope of packets to the particular ethernet interface. The scope for the packets can be specified as either 'signalling' or 'media' packets. The ethernet interface shall be specified by the interface index. The table shall be indexed based on the scope
    	**type**\: :py:class:`CSipCfgBindSourceAddrTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBindSourceAddrTable>`
    
    .. attribute:: csipcfgcausestatustable
    
    	This table contains PSTN cause code to SIP status code mapping configuration.   Inbound PSTN signalling messages that will result in outbound SIP response messages  will have the PSTN cause codes transposed into the SIP status codes as prescribed by the contents of this  table
    	**type**\: :py:class:`CSipCfgCauseStatusTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgCauseStatusTable>`
    
    .. attribute:: csipcfgearlymediatable
    
    	This table contains configuration for Early Media Cut Through.  The configuration controls how the SIP user agent will process 1xx (Provisional) SIP response messages that contain  Session Definition Protocol (SDP) payloads
    	**type**\: :py:class:`CSipCfgEarlyMediaTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgEarlyMediaTable>`
    
    .. attribute:: csipcfgpeer
    
    	
    	**type**\: :py:class:`CSipCfgPeer <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeer>`
    
    .. attribute:: csipcfgpeertable
    
    	This table contains per dial\-peer SIP related  configuration.     The table is a sparse table of dial\-peer information. This means, it only reflects dial\-peers being used  for SIP.  A dial\-peer is being used for SIP if the  value of cvVoIPPeerCfgSessionProtocol  (CISCO\-VOICE\-DIAL\-CONTROL\-MIB) is 'sip'.  Dial\-peers are not created or destroyed via this table.  Only SIP related configuration can be  performed via this table once the dial\-peer exists in the system and is visible in this table
    	**type**\: :py:class:`CSipCfgPeerTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeerTable>`
    
    .. attribute:: csipcfgretry
    
    	
    	**type**\: :py:class:`CSipCfgRetry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgRetry>`
    
    .. attribute:: csipcfgstatuscausetable
    
    	This table contains SIP status code to PSTN cause code mapping configuration.  Inbound SIP response messages  that will result in outbound PSTN signalling messages will have the SIP status codes transposed into the PSTN cause codes as prescribed by the contents of this  table
    	**type**\: :py:class:`CSipCfgStatusCauseTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgStatusCauseTable>`
    
    .. attribute:: csipcfgtimer
    
    	
    	**type**\: :py:class:`CSipCfgTimer <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgTimer>`
    
    .. attribute:: csipcfgvoiceservicevoip
    
    	
    	**type**\: :py:class:`CSipCfgVoiceServiceVoip <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgVoiceServiceVoip>`
    
    .. attribute:: csipstatsconnection
    
    	
    	**type**\: :py:class:`CSipStatsConnection <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsConnection>`
    
    .. attribute:: csipstatserrclient
    
    	
    	**type**\: :py:class:`CSipStatsErrClient <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsErrClient>`
    
    .. attribute:: csipstatserrserver
    
    	
    	**type**\: :py:class:`CSipStatsErrServer <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsErrServer>`
    
    .. attribute:: csipstatsglobalfail
    
    	
    	**type**\: :py:class:`CSipStatsGlobalFail <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsGlobalFail>`
    
    .. attribute:: csipstatsinfo
    
    	
    	**type**\: :py:class:`CSipStatsInfo <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsInfo>`
    
    .. attribute:: csipstatsmisc
    
    	
    	**type**\: :py:class:`CSipStatsMisc <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsMisc>`
    
    .. attribute:: csipstatsredirect
    
    	
    	**type**\: :py:class:`CSipStatsRedirect <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsRedirect>`
    
    .. attribute:: csipstatsretry
    
    	
    	**type**\: :py:class:`CSipStatsRetry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsRetry>`
    
    .. attribute:: csipstatssuccess
    
    	
    	**type**\: :py:class:`CSipStatsSuccess <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsSuccess>`
    
    .. attribute:: csipstatssuccessoktable
    
    	This table contains statistics for sent and received 200 Ok response messages.  The  statistics are kept on per SIP method basis
    	**type**\: :py:class:`CSipStatsSuccessOkTable <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsSuccessOkTable>`
    
    .. attribute:: csipstatstraffic
    
    	
    	**type**\: :py:class:`CSipStatsTraffic <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsTraffic>`
    
    

    """

    _prefix = 'cisco-sip'
    _revision = '2004-02-19'

    def __init__(self):
        self.csipcfgaaa = CISCOSIPUAMIB.CSipCfgAaa()
        self.csipcfgaaa.parent = self
        self.csipcfgbase = CISCOSIPUAMIB.CSipCfgBase()
        self.csipcfgbase.parent = self
        self.csipcfgbindsourceaddrtable = CISCOSIPUAMIB.CSipCfgBindSourceAddrTable()
        self.csipcfgbindsourceaddrtable.parent = self
        self.csipcfgcausestatustable = CISCOSIPUAMIB.CSipCfgCauseStatusTable()
        self.csipcfgcausestatustable.parent = self
        self.csipcfgearlymediatable = CISCOSIPUAMIB.CSipCfgEarlyMediaTable()
        self.csipcfgearlymediatable.parent = self
        self.csipcfgpeer = CISCOSIPUAMIB.CSipCfgPeer()
        self.csipcfgpeer.parent = self
        self.csipcfgpeertable = CISCOSIPUAMIB.CSipCfgPeerTable()
        self.csipcfgpeertable.parent = self
        self.csipcfgretry = CISCOSIPUAMIB.CSipCfgRetry()
        self.csipcfgretry.parent = self
        self.csipcfgstatuscausetable = CISCOSIPUAMIB.CSipCfgStatusCauseTable()
        self.csipcfgstatuscausetable.parent = self
        self.csipcfgtimer = CISCOSIPUAMIB.CSipCfgTimer()
        self.csipcfgtimer.parent = self
        self.csipcfgvoiceservicevoip = CISCOSIPUAMIB.CSipCfgVoiceServiceVoip()
        self.csipcfgvoiceservicevoip.parent = self
        self.csipstatsconnection = CISCOSIPUAMIB.CSipStatsConnection()
        self.csipstatsconnection.parent = self
        self.csipstatserrclient = CISCOSIPUAMIB.CSipStatsErrClient()
        self.csipstatserrclient.parent = self
        self.csipstatserrserver = CISCOSIPUAMIB.CSipStatsErrServer()
        self.csipstatserrserver.parent = self
        self.csipstatsglobalfail = CISCOSIPUAMIB.CSipStatsGlobalFail()
        self.csipstatsglobalfail.parent = self
        self.csipstatsinfo = CISCOSIPUAMIB.CSipStatsInfo()
        self.csipstatsinfo.parent = self
        self.csipstatsmisc = CISCOSIPUAMIB.CSipStatsMisc()
        self.csipstatsmisc.parent = self
        self.csipstatsredirect = CISCOSIPUAMIB.CSipStatsRedirect()
        self.csipstatsredirect.parent = self
        self.csipstatsretry = CISCOSIPUAMIB.CSipStatsRetry()
        self.csipstatsretry.parent = self
        self.csipstatssuccess = CISCOSIPUAMIB.CSipStatsSuccess()
        self.csipstatssuccess.parent = self
        self.csipstatssuccessoktable = CISCOSIPUAMIB.CSipStatsSuccessOkTable()
        self.csipstatssuccessoktable.parent = self
        self.csipstatstraffic = CISCOSIPUAMIB.CSipStatsTraffic()
        self.csipstatstraffic.parent = self


    class CSipCfgAaa(object):
        """
        
        
        .. attribute:: csipcfgaaausername
        
        	This object specifies the source of the information used to populate the username attribute of AAA billing records
        	**type**\: :py:class:`CSipCfgAaaUsername_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgAaa.CSipCfgAaaUsername_Enum>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgaaausername = None

        class CSipCfgAaaUsername_Enum(Enum):
            """
            CSipCfgAaaUsername_Enum

            This object specifies the source of the information used to
            populate the username attribute of AAA billing records.

            """

            CALLINGNUMBER = 1

            PROXYAUTH = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgAaa.CSipCfgAaaUsername_Enum']


        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgAaa'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgaaausername is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgAaa']['meta_info']


    class CSipCfgBase(object):
        """
        
        
        .. attribute:: csipcfgbindsrcaddrinterface
        
        	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that  there is no specific source address configured and  in this case the best local IP address will be chosen  by the system
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: csipcfgbindsrcaddrscope
        
        	This object specifies the scope of packets to which the source IP address of the interface  designated by cSipCfgBindSrcAddrInterface will be bound.  A value of 'all' means the IP address  will be bound to both SIP signalling and media packets. A value of 'control' means the IP address will only be bound to SIP signalling packets.   If cSipCfgBindSrcAddrInterface is set to 0, the value of this object has no meaning
        	**type**\: :py:class:`CSipCfgBindSrcAddrScope_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase.CSipCfgBindSrcAddrScope_Enum>`
        
        .. attribute:: csipcfgdnssrvquerystringformat
        
        	This object specifies the format of the prefix used  by the system for DNS SRV queries.  v1  \:  RFC 2052 format \- 'protocol.transport.' v2  \:  RFC 2782 format \- '\_protocol.\_transport.'  This object allows backward compatibility with systems only supporting RFC 2052 format
        	**type**\: :py:class:`CSipCfgDnsSrvQueryStringFormat_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase.CSipCfgDnsSrvQueryStringFormat_Enum>`
        
        .. attribute:: csipcfgmaxforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\: int
        
        	**range:** 1..15
        
        .. attribute:: csipcfgmaximumforwards
        
        	This object may be used with any SIP method to limit the  number of proxies that can forward the request to the next  downstream server
        	**type**\: int
        
        	**range:** 1..70
        
        .. attribute:: csipcfgoffercallhold
        
        	This object specifies how the SIP gateway would initiate call hold requests.  directionAttr\: The user agent will use the direction                 attribute such as a=sendonly or a=inactive in                 the sdp to initiate call hold requests.                    connAddr\: The user agent will use 0.0.0.0 connection address            to specify Call Hold
        	**type**\: :py:class:`CSipCfgOfferCallHold_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase.CSipCfgOfferCallHold_Enum>`
        
        .. attribute:: csipcfgreasonheaderoveride
        
        	This object specifies that the Reason header overrides SIP  status code mapping table
        	**type**\: bool
        
        .. attribute:: csipcfgredirectiondisabled
        
        	This object specifies how call redirection (3xx) is handled by the user agent.    If 'false', the user agent's treatment of incoming  3xx class response messages is as defined in RFC 2543.   That is, the user agent uses the Contact header(s) from the 3xx response to reinitiate another INVITE transaction to the user's new location.  The call  is redirected.  If 'true', the user agent treats incoming 3xx  response messages as 4xx (client error) class  response messages.  In this case, the call is not redirected, instead it is released with the  appropriate PSTN cause code.  The mapping of SIP 3xx response status codes to 4xx response status codes is as follows\:  300 Multiple Choices \-> 410 Gone  301 Moved Permanently \-> 410 Gone  302 Moved Temporarily \-> 480 Temporarily Unavailable  305 User Proxy        \-> 410 Gone  380 Alternative Service \-> 410 Gone  Any other 3xx \-> 410 Gone
        	**type**\: bool
        
        .. attribute:: csipcfgsuspendresumeenabled
        
        	This object specifies if support for handling  Suspend/Resume events from the switch is enabled or not.  If 'true', the user agent on getting a Suspend will notify the remote agent by sending it a re\-invite with a hold SDP. Similarly, when the Gateway receives a Resume, it will initiate a re\-invite with the original SDP and unhold the call.  If 'false', the user agent will not initiate any re\-invites on receiving Suspend/Resume events, basically it won't be putting the call on hold or off hold
        	**type**\: bool
        
        .. attribute:: csipcfgsymnatdirectionrole
        
        	This object specifies the value of the 'a=direction\:<role>' SDP attribute supported by  the user agent.  The direction attribute is used  to describe the role of the user agent (as an  endpoint for a connection\-oriented media stream)  in the connection setup procedure.  none    \:  No role is specified. passive \:  The user agent will advertise itself            as a 'passive' entity (inside the NAT)            in the SDP. active  \:  The user agent will advertise itself            as a 'active' entity (outside the NAT)            in the SDP
        	**type**\: :py:class:`CSipCfgSymNatDirectionRole_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase.CSipCfgSymNatDirectionRole_Enum>`
        
        .. attribute:: csipcfgsymnatenabled
        
        	This object specifies whether remote media checks for Symmetric Network Address Translation (NAT)  is enabled or disabled.  If 'true', remote media checks are enabled.  The gateway will have the ability to open a Real Time  Transport Protocol (RTP) session with the remote end and then update (modify) the existing RTP session's remote address/port (raddr\:rport) with the source address and port of the actual media packet received.  This would be triggered for only those calls where the Session Description Protocol (SDP) received by the gateway has an indication to do so.  If 'false', remote media checks are disabled
        	**type**\: bool
        
        .. attribute:: csipcfgtransport
        
        	This object specifies the transport protocol the SIP user  agent will use to receive SIP messages.  A value of 'disabled' indicates that the UA will not receive any SIP messages
        	**type**\: :py:class:`CSipCfgTransport_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBase.CSipCfgTransport_Enum>`
        
        .. attribute:: csipcfguserlocationserveraddr
        
        	This object specifies address of the User Location  Server (ULS) being used to resolve the location of end  points.  This could be a Domain Name Server (DNS) or a  SIP proxy/redirect server.  The format of the address follows the IETF service location  protocol. The syntax is as follows\:     mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching  dial string to a target server. The type\-specific\-syntax is  exactly that, something that the particular mapping scheme can understand.  For example,    Session target           Meaning    ipv4\:171.68.13.55\:1006   The session target is the IP                              version 4 address of 171.68.13.55                              and port 1006.    dns\:pots.cisco.com       The session target is the IP host                              with dns name pots.cisco.com.  The valid Mapping type definitions for the peer follow\:    ipv4  \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z     dns   \- Syntax\: dns\:host.domain
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: csipcfgversion
        
        	This object will reflect the version of SIP supported by this  user agent.  It will follow the same format as SIP version  information contained in the SIP messages generated by this user agent.  For example, user agents supporting SIP version 2 will return 'SIP/2.0' as dictated by RFC 2543
        	**type**\: str
        
        	**range:** 0..255
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgbindsrcaddrinterface = None
            self.csipcfgbindsrcaddrscope = None
            self.csipcfgdnssrvquerystringformat = None
            self.csipcfgmaxforwards = None
            self.csipcfgmaximumforwards = None
            self.csipcfgoffercallhold = None
            self.csipcfgreasonheaderoveride = None
            self.csipcfgredirectiondisabled = None
            self.csipcfgsuspendresumeenabled = None
            self.csipcfgsymnatdirectionrole = None
            self.csipcfgsymnatenabled = None
            self.csipcfgtransport = None
            self.csipcfguserlocationserveraddr = None
            self.csipcfgversion = None

        class CSipCfgBindSrcAddrScope_Enum(Enum):
            """
            CSipCfgBindSrcAddrScope_Enum

            This object specifies the scope of packets to
            which the source IP address of the interface 
            designated by cSipCfgBindSrcAddrInterface
            will be bound.  A value of 'all' means the IP address 
            will be bound to both SIP signalling and media packets.
            A value of 'control' means the IP address will only
            be bound to SIP signalling packets.  
            If cSipCfgBindSrcAddrInterface is set to 0,
            the value of this object has no meaning.

            """

            ALL = 1

            CONTROL = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase.CSipCfgBindSrcAddrScope_Enum']


        class CSipCfgDnsSrvQueryStringFormat_Enum(Enum):
            """
            CSipCfgDnsSrvQueryStringFormat_Enum

            This object specifies the format of the prefix used 
            by the system for DNS SRV queries.
            
            v1  \:  RFC 2052 format \- 'protocol.transport.'
            v2  \:  RFC 2782 format \- '\_protocol.\_transport.'
            
            This object allows backward compatibility with systems
            only supporting RFC 2052 format.

            """

            V1 = 1

            V2 = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase.CSipCfgDnsSrvQueryStringFormat_Enum']


        class CSipCfgOfferCallHold_Enum(Enum):
            """
            CSipCfgOfferCallHold_Enum

            This object specifies how the SIP gateway would initiate call
            hold requests.
            
            directionAttr\: The user agent will use the direction
                            attribute such as a=sendonly or a=inactive in
                            the sdp to initiate call hold requests.
                              
            connAddr\: The user agent will use 0.0.0.0 connection address
                       to specify Call Hold.

            """

            DIRECTIONATTR = 1

            CONNADDR = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase.CSipCfgOfferCallHold_Enum']


        class CSipCfgSymNatDirectionRole_Enum(Enum):
            """
            CSipCfgSymNatDirectionRole_Enum

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

            """

            NONE = 1

            PASSIVE = 2

            ACTIVE = 3


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase.CSipCfgSymNatDirectionRole_Enum']


        class CSipCfgTransport_Enum(Enum):
            """
            CSipCfgTransport_Enum

            This object specifies the transport protocol the SIP user 
            agent will use to receive SIP messages.  A value of 'disabled'
            indicates that the UA will not receive any SIP messages.

            """

            UDP = 1

            TCP = 2

            UDPANDTCP = 3

            DISABLED = 4


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase.CSipCfgTransport_Enum']


        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgBase'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgbindsrcaddrinterface is not None:
                return True

            if self.csipcfgbindsrcaddrscope is not None:
                return True

            if self.csipcfgdnssrvquerystringformat is not None:
                return True

            if self.csipcfgmaxforwards is not None:
                return True

            if self.csipcfgmaximumforwards is not None:
                return True

            if self.csipcfgoffercallhold is not None:
                return True

            if self.csipcfgreasonheaderoveride is not None:
                return True

            if self.csipcfgredirectiondisabled is not None:
                return True

            if self.csipcfgsuspendresumeenabled is not None:
                return True

            if self.csipcfgsymnatdirectionrole is not None:
                return True

            if self.csipcfgsymnatenabled is not None:
                return True

            if self.csipcfgtransport is not None:
                return True

            if self.csipcfguserlocationserveraddr is not None:
                return True

            if self.csipcfgversion is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgBase']['meta_info']


    class CSipCfgBindSourceAddrTable(object):
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
        	**type**\: list of :py:class:`CSipCfgBindSourceAddrEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgbindsourceaddrentry = YList()
            self.csipcfgbindsourceaddrentry.parent = self
            self.csipcfgbindsourceaddrentry.name = 'csipcfgbindsourceaddrentry'


        class CSipCfgBindSourceAddrEntry(object):
            """
            A row in the cSipCfgBindSourceAddrTable.
            A row is accessible with the scope of packets
            to which the source IP address of the interface
            designated by cSipCfgBindSourceAddrInterface
            will be bound.
            
            .. attribute:: csipcfgbindsourceaddrscope
            
            	A unique identifier of a row in this table and specifies the scope of packets to which the source IP address of the interface designated by cSipCfgBindSourceAddrInterface will be bound
            	**type**\: :py:class:`CSipCfgBindSourceAddrScope_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry.CSipCfgBindSourceAddrScope_Enum>`
            
            .. attribute:: csipcfgbindsourceaddrinterface
            
            	This object may specify the interface where the source IP address used in SIP signalling or media packets is configured.  A value of 0 means that there is no specific source address configured and in this case the best local IP address will be chosen by the system
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipcfgbindsourceaddrscope = None
                self.csipcfgbindsourceaddrinterface = None

            class CSipCfgBindSourceAddrScope_Enum(Enum):
                """
                CSipCfgBindSourceAddrScope_Enum

                A unique identifier of a row in this table and
                specifies the scope of packets to which the
                source IP address of the interface
                designated by cSipCfgBindSourceAddrInterface
                will be bound.

                """

                MEDIA = 1

                CONTROL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                    return meta._meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry.CSipCfgBindSourceAddrScope_Enum']


            @property
            def _common_path(self):
                if self.csipcfgbindsourceaddrscope is None:
                    raise YPYDataValidationError('Key property csipcfgbindsourceaddrscope is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgBindSourceAddrTable/CISCO-SIP-UA-MIB:cSipCfgBindSourceAddrEntry[CISCO-SIP-UA-MIB:cSipCfgBindSourceAddrScope = ' + str(self.csipcfgbindsourceaddrscope) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipcfgbindsourceaddrscope is not None:
                    return True

                if self.csipcfgbindsourceaddrinterface is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgBindSourceAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgbindsourceaddrentry is not None:
                for child_ref in self.csipcfgbindsourceaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable']['meta_info']


    class CSipCfgCauseStatusTable(object):
        """
        This table contains PSTN cause code to SIP status code
        mapping configuration.   Inbound PSTN signalling messages
        that will result in outbound SIP response messages 
        will have the PSTN cause codes transposed into the
        SIP status codes as prescribed by the contents of this 
        table.
        
        .. attribute:: csipcfgcausestatusentry
        
        	A row in the cSipCfgCauseStatusTable. Entries cannot be created or destroyed by the actions of any NMS
        	**type**\: list of :py:class:`CSipCfgCauseStatusEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgcausestatusentry = YList()
            self.csipcfgcausestatusentry.parent = self
            self.csipcfgcausestatusentry.name = 'csipcfgcausestatusentry'


        class CSipCfgCauseStatusEntry(object):
            """
            A row in the cSipCfgCauseStatusTable. Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgpstncauseindex
            
            	A unique identifier of a row in this table and a valid PSTN cause code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgcausestatusstorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: csipcfgstatuscode
            
            	The SIP status code to which the PSTN cause code given by cSipCfgPstnCauseIndex is to be mapped for outbound SIP response messages
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipcfgpstncauseindex = None
                self.csipcfgcausestatusstorestatus = None
                self.csipcfgstatuscode = None

            @property
            def _common_path(self):
                if self.csipcfgpstncauseindex is None:
                    raise YPYDataValidationError('Key property csipcfgpstncauseindex is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgCauseStatusTable/CISCO-SIP-UA-MIB:cSipCfgCauseStatusEntry[CISCO-SIP-UA-MIB:cSipCfgPstnCauseIndex = ' + str(self.csipcfgpstncauseindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipcfgpstncauseindex is not None:
                    return True

                if self.csipcfgcausestatusstorestatus is not None:
                    return True

                if self.csipcfgstatuscode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgCauseStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgcausestatusentry is not None:
                for child_ref in self.csipcfgcausestatusentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgCauseStatusTable']['meta_info']


    class CSipCfgEarlyMediaTable(object):
        """
        This table contains configuration for Early
        Media Cut Through.  The configuration controls
        how the SIP user agent will process 1xx
        (Provisional) SIP response messages that contain 
        Session Definition Protocol (SDP) payloads.
        
        .. attribute:: csipcfgearlymediaentry
        
        	A row in the cSipCfgEarlyMediaTable. A row is accessible with a Provisional (1xx) status code value (eg, 180) and provides an object for the enabling or disabling of the Early Media Cut Through functionality
        	**type**\: list of :py:class:`CSipCfgEarlyMediaEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgearlymediaentry = YList()
            self.csipcfgearlymediaentry.parent = self
            self.csipcfgearlymediaentry.name = 'csipcfgearlymediaentry'


        class CSipCfgEarlyMediaEntry(object):
            """
            A row in the cSipCfgEarlyMediaTable.
            A row is accessible with a Provisional (1xx)
            status code value (eg, 180) and provides
            an object for the enabling or disabling of
            the Early Media Cut Through functionality.
            
            .. attribute:: csipcfgearlymediastatuscodeindex
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgearlymediacutthrudisabled
            
            	This object specifies whether Early Media  Cut Through is enabled or disabled for the  SIP response messages with status codes that  match cSipCfgEarlyMediaStatusCodeIndex.  If 'true', early media cut through is disabled, and the user agent will process the message as though it did not contain any SDP payload.  If 'false', early media cut through is enabled, and the user agent will process the message similar to a 183 (Session Progress) and cut through for early media.  The assumption being that the SDP is an indication that the far end is going to send early media
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipcfgearlymediastatuscodeindex = None
                self.csipcfgearlymediacutthrudisabled = None

            @property
            def _common_path(self):
                if self.csipcfgearlymediastatuscodeindex is None:
                    raise YPYDataValidationError('Key property csipcfgearlymediastatuscodeindex is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgEarlyMediaTable/CISCO-SIP-UA-MIB:cSipCfgEarlyMediaEntry[CISCO-SIP-UA-MIB:cSipCfgEarlyMediaStatusCodeIndex = ' + str(self.csipcfgearlymediastatuscodeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipcfgearlymediastatuscodeindex is not None:
                    return True

                if self.csipcfgearlymediacutthrudisabled is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgEarlyMediaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgearlymediaentry is not None:
                for child_ref in self.csipcfgearlymediaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgEarlyMediaTable']['meta_info']


    class CSipCfgPeer(object):
        """
        
        
        .. attribute:: csipcfgoutsessiontransport
        
        	This object specifies the session transport  protocol that will be used for outbound SIP  messages.  This configuration is applicable to all dial\-peers in the system having  cSipCfgPeerOutSessionTransport set to 'system'
        	**type**\: :py:class:`CSipCfgOutSessionTransport_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeer.CSipCfgOutSessionTransport_Enum>`
        
        .. attribute:: csipcfgreliable1xxrsphdr
        
        	This object specifies behavior with respect to Supported or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs
        	**type**\: :py:class:`CSipCfgReliable1xxRspHdr_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeer.CSipCfgReliable1xxRspHdr_Enum>`
        
        .. attribute:: csipcfgreliable1xxrspstr
        
        	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgReliable1xxRspHdr
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: csipcfgurltype
        
        	This object specifies the URL type sent in outbound INVITES generated by this device
        	**type**\: :py:class:`CSipCfgUrlType_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeer.CSipCfgUrlType_Enum>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgoutsessiontransport = None
            self.csipcfgreliable1xxrsphdr = None
            self.csipcfgreliable1xxrspstr = None
            self.csipcfgurltype = None

        class CSipCfgOutSessionTransport_Enum(Enum):
            """
            CSipCfgOutSessionTransport_Enum

            This object specifies the session transport 
            protocol that will be used for outbound SIP 
            messages.  This configuration is applicable
            to all dial\-peers in the system having 
            cSipCfgPeerOutSessionTransport set to 'system'.

            """

            UDP = 1

            TCP = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeer.CSipCfgOutSessionTransport_Enum']


        class CSipCfgReliable1xxRspHdr_Enum(Enum):
            """
            CSipCfgReliable1xxRspHdr_Enum

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

            """

            SUPPORTED = 1

            REQUIRE = 2

            DISABLED = 3


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeer.CSipCfgReliable1xxRspHdr_Enum']


        class CSipCfgUrlType_Enum(Enum):
            """
            CSipCfgUrlType_Enum

            This object specifies the URL type sent in outbound
            INVITES generated by this device.

            """

            SIP = 1

            TEL = 2


            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeer.CSipCfgUrlType_Enum']


        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgPeer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgoutsessiontransport is not None:
                return True

            if self.csipcfgreliable1xxrsphdr is not None:
                return True

            if self.csipcfgreliable1xxrspstr is not None:
                return True

            if self.csipcfgurltype is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeer']['meta_info']


    class CSipCfgPeerTable(object):
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
        	**type**\: list of :py:class:`CSipCfgPeerEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgpeerentry = YList()
            self.csipcfgpeerentry.parent = self
            self.csipcfgpeerentry.name = 'csipcfgpeerentry'


        class CSipCfgPeerEntry(object):
            """
            A row in the cSipCfgPeerTable.
            
            .. attribute:: csipcfgpeerindex
            
            	An arbitrary index that uniquely identifies a  dial\-peer configured for SIP
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpeeroutsessiontransport
            
            	This object specifies the session transport  protocol that will be used by this dial\-peer for outbound SIP messages.    The value 'system' is the default and indicates  that this dial\-peer should use the value set by  cSipCfgOutSessionTransport instead
            	**type**\: :py:class:`CSipCfgPeerOutSessionTransport_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerOutSessionTransport_Enum>`
            
            .. attribute:: csipcfgpeerreliable1xxrsphdr
            
            	This object specifies behavior with respect to Support or Require headers in SIP messages sent and received via this dial\-peer.  If the originating gateway is configured for 'require', the Require header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This requires the use of reliable provisional responses by the terminating gateway.  Sessions will be torn down if this use cannot be supported by that gateway.  If the originating gateway is configured for 'supported', the Supported header is added to the outgoing INVITEs with the value of cSipCfgPeerReliable1xxStr.  This  requires that an attempt to use reliable provisional responses be made, but sessions can continue without them.  If the originating gateway is configured for 'disabled', the value of cSipCfgReliable1xxStr will NOT be added to either the Require or Supported headers of outgoing INVITEs.  The value 'system' is the default and indicates that this  dial\-peer should use the value of  cSipCfgReliable1xxRspHdr instead
            	**type**\: :py:class:`CSipCfgPeerReliable1xxRspHdr_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerReliable1xxRspHdr_Enum>`
            
            .. attribute:: csipcfgpeerreliable1xxrspstr
            
            	This object specifies the string that will be  placed in either the Supported or Require SIP  header, as specified by cSipCfgPeerReliable1xxRspHdr
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csipcfgpeerswitchtransenabled
            
            	This object specifies if the functionality of switching between transports from UDP to TCP if the message size of a Request is greater than 1300 bytes is enabled or not
            	**type**\: bool
            
            .. attribute:: csipcfgpeerurltype
            
            	This object specifies the URL type sent in outbound INVITES generated by this device.  The value 'system' is the default and indicates that this  dial\-peer should use the value of cSipCfgUrlType instead
            	**type**\: :py:class:`CSipCfgPeerUrlType_Enum <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerUrlType_Enum>`
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipcfgpeerindex = None
                self.csipcfgpeeroutsessiontransport = None
                self.csipcfgpeerreliable1xxrsphdr = None
                self.csipcfgpeerreliable1xxrspstr = None
                self.csipcfgpeerswitchtransenabled = None
                self.csipcfgpeerurltype = None

            class CSipCfgPeerOutSessionTransport_Enum(Enum):
                """
                CSipCfgPeerOutSessionTransport_Enum

                This object specifies the session transport 
                protocol that will be used by this dial\-peer
                for outbound SIP messages.  
                
                The value 'system' is the default and indicates 
                that this dial\-peer should use the value set by 
                cSipCfgOutSessionTransport instead.

                """

                SYSTEM = 1

                UDP = 2

                TCP = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                    return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerOutSessionTransport_Enum']


            class CSipCfgPeerReliable1xxRspHdr_Enum(Enum):
                """
                CSipCfgPeerReliable1xxRspHdr_Enum

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

                """

                SYSTEM = 1

                SUPPORTED = 2

                REQUIRE = 3

                DISABLED = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                    return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerReliable1xxRspHdr_Enum']


            class CSipCfgPeerUrlType_Enum(Enum):
                """
                CSipCfgPeerUrlType_Enum

                This object specifies the URL type sent in outbound
                INVITES generated by this device.
                
                The value 'system' is the default and indicates that this 
                dial\-peer should use the value of cSipCfgUrlType instead.

                """

                SYSTEM = 1

                SIP = 2

                TEL = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                    return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerUrlType_Enum']


            @property
            def _common_path(self):
                if self.csipcfgpeerindex is None:
                    raise YPYDataValidationError('Key property csipcfgpeerindex is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgPeerTable/CISCO-SIP-UA-MIB:cSipCfgPeerEntry[CISCO-SIP-UA-MIB:cSipCfgPeerIndex = ' + str(self.csipcfgpeerindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipcfgpeerindex is not None:
                    return True

                if self.csipcfgpeeroutsessiontransport is not None:
                    return True

                if self.csipcfgpeerreliable1xxrsphdr is not None:
                    return True

                if self.csipcfgpeerreliable1xxrspstr is not None:
                    return True

                if self.csipcfgpeerswitchtransenabled is not None:
                    return True

                if self.csipcfgpeerurltype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgpeerentry is not None:
                for child_ref in self.csipcfgpeerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgPeerTable']['meta_info']


    class CSipCfgRetry(object):
        """
        
        
        .. attribute:: csipcfgretrybye
        
        	This object specifies the number of times a user agent  will retry sending a BYE request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycancel
        
        	This object specifies the number of times a user agent  will retry sending a CANCEL request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrycomet
        
        	This object specifies the number of times a user agent  will retry sending a COMET (COndition MET)
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryinfo
        
        	This object specifies the number of times a user agent will retry sending a Info request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryinvite
        
        	This object specifies the number of times a user agent  will retry sending a INVITE request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrynotify
        
        	This object specifies the number of times a user agent  will retry sending a Notify request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryprack
        
        	This object specifies the number of times a user agent  will retry sending a PRACK (PRovisional ACKnowledgement)
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryrefer
        
        	This object specifies the number of times a user agent  will retry sending a Refer request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryregister
        
        	This object specifies the number of times a user agent  will retry sending a REGISTER request
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryreliablersp
        
        	This object specifies the number of times a user agent  will retry sending a reliable response
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretryresponse
        
        	This object specifies the number of times a user agent  will retry sending a Response and expecting a ACK
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: csipcfgretrysubscribe
        
        	This object specifies the number of times a user agent will retry sending a Subscribe request
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgretrybye = None
            self.csipcfgretrycancel = None
            self.csipcfgretrycomet = None
            self.csipcfgretryinfo = None
            self.csipcfgretryinvite = None
            self.csipcfgretrynotify = None
            self.csipcfgretryprack = None
            self.csipcfgretryrefer = None
            self.csipcfgretryregister = None
            self.csipcfgretryreliablersp = None
            self.csipcfgretryresponse = None
            self.csipcfgretrysubscribe = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgRetry'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgretrybye is not None:
                return True

            if self.csipcfgretrycancel is not None:
                return True

            if self.csipcfgretrycomet is not None:
                return True

            if self.csipcfgretryinfo is not None:
                return True

            if self.csipcfgretryinvite is not None:
                return True

            if self.csipcfgretrynotify is not None:
                return True

            if self.csipcfgretryprack is not None:
                return True

            if self.csipcfgretryrefer is not None:
                return True

            if self.csipcfgretryregister is not None:
                return True

            if self.csipcfgretryreliablersp is not None:
                return True

            if self.csipcfgretryresponse is not None:
                return True

            if self.csipcfgretrysubscribe is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgRetry']['meta_info']


    class CSipCfgStatusCauseTable(object):
        """
        This table contains SIP status code to PSTN cause code
        mapping configuration.  Inbound SIP response messages 
        that will result in outbound PSTN signalling messages
        will have the SIP status codes transposed into the
        PSTN cause codes as prescribed by the contents of this 
        table.
        
        .. attribute:: csipcfgstatuscauseentry
        
        	A row in the cSipCfgStatusCauseTable.  Entries cannot be created or destroyed by the actions of any NMS
        	**type**\: list of :py:class:`CSipCfgStatusCauseEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgstatuscauseentry = YList()
            self.csipcfgstatuscauseentry.parent = self
            self.csipcfgstatuscauseentry.name = 'csipcfgstatuscauseentry'


        class CSipCfgStatusCauseEntry(object):
            """
            A row in the cSipCfgStatusCauseTable.  Entries cannot be
            created or destroyed by the actions of any NMS.
            
            .. attribute:: csipcfgstatuscodeindex
            
            	A unique identifier of a row in this table and a valid SIP status code
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgpstncause
            
            	The PSTN cause code to which the SIP status code given by cSipCfgStatusCodeIndex is to be mapped for outbound PSTN signalling messages
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: csipcfgstatuscausestorestatus
            
            	This object reflects the storage status of this table entry.  If the value is 'volatile', then this entry only exists in RAM and the information would be lost (reverting to defaults) on system reload.   If the value is 'nonVolatile' then this entry has been  written to NVRAM and will persist across system reloads
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipcfgstatuscodeindex = None
                self.csipcfgpstncause = None
                self.csipcfgstatuscausestorestatus = None

            @property
            def _common_path(self):
                if self.csipcfgstatuscodeindex is None:
                    raise YPYDataValidationError('Key property csipcfgstatuscodeindex is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgStatusCauseTable/CISCO-SIP-UA-MIB:cSipCfgStatusCauseEntry[CISCO-SIP-UA-MIB:cSipCfgStatusCodeIndex = ' + str(self.csipcfgstatuscodeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipcfgstatuscodeindex is not None:
                    return True

                if self.csipcfgpstncause is not None:
                    return True

                if self.csipcfgstatuscausestorestatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgStatusCauseTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgstatuscauseentry is not None:
                for child_ref in self.csipcfgstatuscauseentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgStatusCauseTable']['meta_info']


    class CSipCfgTimer(object):
        """
        
        
        .. attribute:: csipcfgtimerbufferinvite
        
        	This object specifies the amount of time to buffer the INVITE  while waiting for display name info in the Facility.  A value of 0 means that the INVITE wouldn't be buffered waiting for the display name info in the Facility
        	**type**\: int
        
        	**range:** 0 \| 50..5000
        
        .. attribute:: csipcfgtimercomet
        
        	This object specifies the time a user agent will wait  for a final response before retransmitting the COMET  (COndition MET)
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerconnect
        
        	This object specifies the time a user agent will wait to  receive an ACK confirmation a session is established
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerconnectionaging
        
        	This object specifies the amount of time to wait before  aging out a TCP/UDP connection
        	**type**\: int
        
        	**range:** 5..30
        
        .. attribute:: csipcfgtimerdisconnect
        
        	This object specifies the time a user agent will wait to  receive an BYE confirmation a session is disconnected
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerexpires
        
        	This object specifies the time a user agent will wait to  receive a final response to a INVITE before cancelling the  transaction
        	**type**\: int
        
        	**range:** 60000..300000
        
        .. attribute:: csipcfgtimerhold
        
        	This object specifies the amount of time to wait before  disconnecting a call already on hold. A value of 0 specifies that this functionality is disabled
        	**type**\: int
        
        	**range:** 0 \| 15..2880
        
        .. attribute:: csipcfgtimerinfo
        
        	This object specifies the amount of time to wait for a 200ok response before retransmitting the Info
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimernotify
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Notify
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerprack
        
        	This object specifies the time a user agent will wait for  a final response before retransmitting the PRACK (PRovisional ACKnowledgment)
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerrefer
        
        	This object specifies the amount of time to wait for a final response before retransmitting the Refer
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimerreliablersp
        
        	This object specifies the amount of time to wait for a PRACK before retransmitting the reliable 1xx response
        	**type**\: int
        
        	**range:** 100..1000
        
        .. attribute:: csipcfgtimersessiontimer
        
        	This object specifies the value of the Min\-SE  header for INVITE messages originated by this  user agent and the minimum value of the  Session\-Expires headers for INVITE messages  received by this user agent.  Any Session\-Expires headers received with a  value below this object's value will be rejected with a 422 client error response message.  Setting this object to a value less than 600 is valid, but the possibly of excessive re\-INVITES  and the impact of those messages should be fully  understood and considered an acceptable risk
        	**type**\: int
        
        	**range:** 60..86400
        
        .. attribute:: csipcfgtimertrying
        
        	This object specifies the time a user agent will wait to  receive a provisional response to a INVITE before resending  the INVITE
        	**type**\: int
        
        	**range:** 100..1000
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgtimerbufferinvite = None
            self.csipcfgtimercomet = None
            self.csipcfgtimerconnect = None
            self.csipcfgtimerconnectionaging = None
            self.csipcfgtimerdisconnect = None
            self.csipcfgtimerexpires = None
            self.csipcfgtimerhold = None
            self.csipcfgtimerinfo = None
            self.csipcfgtimernotify = None
            self.csipcfgtimerprack = None
            self.csipcfgtimerrefer = None
            self.csipcfgtimerreliablersp = None
            self.csipcfgtimersessiontimer = None
            self.csipcfgtimertrying = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgTimer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgtimerbufferinvite is not None:
                return True

            if self.csipcfgtimercomet is not None:
                return True

            if self.csipcfgtimerconnect is not None:
                return True

            if self.csipcfgtimerconnectionaging is not None:
                return True

            if self.csipcfgtimerdisconnect is not None:
                return True

            if self.csipcfgtimerexpires is not None:
                return True

            if self.csipcfgtimerhold is not None:
                return True

            if self.csipcfgtimerinfo is not None:
                return True

            if self.csipcfgtimernotify is not None:
                return True

            if self.csipcfgtimerprack is not None:
                return True

            if self.csipcfgtimerrefer is not None:
                return True

            if self.csipcfgtimerreliablersp is not None:
                return True

            if self.csipcfgtimersessiontimer is not None:
                return True

            if self.csipcfgtimertrying is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgTimer']['meta_info']


    class CSipCfgVoiceServiceVoip(object):
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

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipcfgheaderpassingenabled = None
            self.csipcfgmaxsubscriptionaccept = None
            self.csipcfgmaxsubscriptionoriginate = None
            self.csipcfgswitchtransportenabled = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipCfgVoiceServiceVoip'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipcfgheaderpassingenabled is not None:
                return True

            if self.csipcfgmaxsubscriptionaccept is not None:
                return True

            if self.csipcfgmaxsubscriptionoriginate is not None:
                return True

            if self.csipcfgswitchtransportenabled is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipCfgVoiceServiceVoip']['meta_info']


    class CSipStatsConnection(object):
        """
        
        
        .. attribute:: csipstatsactivetcpconnections
        
        	This object reflects the total number of active TCP connections since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsactiveudpconnections
        
        	This object reflects the total number of active UDP connections since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpcreatefailures
        
        	This object reflects the total number of connection create failures for TCP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpinactivetimeouts
        
        	This object reflects the total number of TCP connections that timed out due to inactivity since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpremoteclosures
        
        	This object reflects the total number of Remote Closures  for TCP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconntcpsendfailures
        
        	This object reflects the total number of TCP send failures since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpcreatefailures
        
        	This object reflects the total number of connection create failures for UDP since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpinactivetimeouts
        
        	This object reflects the total number of UDP connections that  timed out due to inactivity since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsconnudpsendfailures
        
        	This object reflects the total number of UDP send failures since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsactivetcpconnections = None
            self.csipstatsactiveudpconnections = None
            self.csipstatsconntcpcreatefailures = None
            self.csipstatsconntcpinactivetimeouts = None
            self.csipstatsconntcpremoteclosures = None
            self.csipstatsconntcpsendfailures = None
            self.csipstatsconnudpcreatefailures = None
            self.csipstatsconnudpinactivetimeouts = None
            self.csipstatsconnudpsendfailures = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsConnection'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsactivetcpconnections is not None:
                return True

            if self.csipstatsactiveudpconnections is not None:
                return True

            if self.csipstatsconntcpcreatefailures is not None:
                return True

            if self.csipstatsconntcpinactivetimeouts is not None:
                return True

            if self.csipstatsconntcpremoteclosures is not None:
                return True

            if self.csipstatsconntcpsendfailures is not None:
                return True

            if self.csipstatsconnudpcreatefailures is not None:
                return True

            if self.csipstatsconnudpinactivetimeouts is not None:
                return True

            if self.csipstatsconnudpsendfailures is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsConnection']['meta_info']


    class CSipStatsErrClient(object):
        """
        
        
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
        
        .. attribute:: csipstatsclientbadeventins
        
        	This object reflects the total number of BadEvent (489)  responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadeventouts
        
        	This object reflects the total number of BadEvent (489)  responses sent by the user agent since system startup
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
        
        .. attribute:: csipstatsclientbadrequestins
        
        	This object reflects the total number of Bad Request (400)  responses received by the user agent since system startup. Inbound Bad Request responses indicate that requests issued  by this system could not be understood due to malformed  syntax
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientbadrequestouts
        
        	This object reflects the total number of Bad Request (400)  responses sent by the user agent since system startup. Outbound Bad Request responses indicate that requests  received by this system could not be understood due to  malformed syntax
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
        
        .. attribute:: csipstatsclientcalllegnoexistins
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses received by the user agent since system startup. Inbound Call Leg/Transaction Does Not Exist responses indicate that either BYE or CANCEL requests issued by this system were  received by a server and not matching call leg or transaction  existed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientcalllegnoexistouts
        
        	This object reflects the total number of Call Leg/Transaction  Does Not Exist (481) responses sent by the user agent since system startup. Outbound Call Leg/Transaction Does Not Exist responses  indicate that BYE or CANCEL requests have been received by  this system and not call leg or transaction matching that  request exists
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
        
        .. attribute:: csipstatsclientforbiddenins
        
        	This object reflects the total number of Forbidden (403)  responses received by the user agent since system startup. Inbound Forbidden responses indicate that requests issued by this system are understood by the server but the server refuses to fulfill the request.  Authorization will not help and the requests should not be repeated
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientforbiddenouts
        
        	This object reflects the total number of Forbidden (403)  responses sent by the user agent since system startup. Outbound Forbidden responses indicate that requests received by this system are understood but this system is refusing to fulfill the requests
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
        
        .. attribute:: csipstatsclientlengthrequiredouts
        
        	This object reflects the total number of Length Required  (411) responses sent by the user agent since system startup. Outbound Length Required responses indicate that requests  received by this system are being refused because of no  defined Content\-Length header field
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
        
        .. attribute:: csipstatsclientmethnotallowedins
        
        	This object reflects the total number of Method Not Allowed  (405) received responses by the user agent. Inbound Method Not Allowed responses indicate that requests  issued by this system have specified a SIP method in the  Request\-Line that is not allowed for the address identified  by the Request\-URI
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientmethnotallowedouts
        
        	This object reflects the total number of Method Not Allowed  (405) received sent by the user agent since system startup. Outbound Method Not Allowed responses indicate that requests  received by this system have SIP methods specified in the  Request\-Line that are not allowed for the address identified  by the Request\-URI
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
        
        .. attribute:: csipstatsclientnosupmediatypeins
        
        	This object reflects the total number of Unsupported Media  Type (415) responses received by the user agent since system startup. Inbound Unsupported Media Type responses indicate that  requests issued by this system are being refused because the  message body of the request is in a format not supported by  the requested resource for the requested method
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnosupmediatypeouts
        
        	This object reflects the total number of Unsupported Media  Type (415) responses sent by the user agent since system startup. Outbound Unsupported Media Type responses indicate that the  body of requests received by this system are in a format not  supported by the requested resource for the requested method
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
        
        .. attribute:: csipstatsclientnotfoundins
        
        	This object reflects the total number of Not Found (404)  responses received by the user agent since system startup. Inbound Not Found responses indicate that the called party  does not exist at the domain specified in the Request\-URI  or the domain is not handled by the recipient of the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientnotfoundouts
        
        	This object reflects the total number of Not Found (404)  responses sent by the user agent since system startup. Outbound Not Found responses indicate that this system knows that the called party does not exist at the domain specified in the Request\-URI or the domain is not handled by this system
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
        
        .. attribute:: csipstatsclientproxyauthreqdins
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses received by the user agent since system startup. Inbound Proxy Authentication Required responses indicate that  this system must authenticate itself with the proxy before  gaining access to the requested resource
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientproxyauthreqdouts
        
        	This object reflects the total number of Proxy Authentication  Required (407) responses sent by the user agent since system startup. Outbound Proxy Authentication Required responses indicate that the systems issuing requests being processed by this system  must authenticate themselves with this system before gaining  access to requested resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqenttoolargeins
        
        	This object reflects the total number of Request Entity Too  Large (413) responses received by the user agent since system startup. Inbound Request Entity Too Large responses indicate that  requests issued by this system are being refused because  the request is larger than the server is willing or able to  process
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqenttoolargeouts
        
        	This object reflects the total number of Request Entity Too  Large (413) responses sent by the user agent since system startup. Outbound Request Entity Too Large responses indicate that  requests received by this system are larger than this system  is willing or able to process
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
        
        .. attribute:: csipstatsclientreqtermins
        
        	This object reflects the total number of Request Terminated  (487) responses received by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientreqtermouts
        
        	This object reflects the total number of Request Terminated  (487) responses sent by the user agent since system startup. Request Terminated responses are issued if the original  request was terminated via CANCEL or BYE
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
        
        .. attribute:: csipstatsclientrequritoolargeins
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses received by the user agent since system startup. Inbound Request\-URI Too Large responses indicate that  requests issued by this system are being refused because the  Request\-URI is longer than the server is willing or able to  interpret
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientrequritoolargeouts
        
        	This object reflects the total number of Request\-URI Too  Large (414) responses sent by the user agent since system startup. Outbound Request\-URI Too Large responses indicate that  Request\-URIs received by this system are longer than this  system is willing or able to interpret
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
        
        .. attribute:: csipstatsclienttempnotavailins
        
        	This object reflects the total number of Temporarily Not  Available (480) responses received by the user agent since system startup. Inbound Temporarily Not Available responses indicate that  the called party is currently unavailable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclienttempnotavailouts
        
        	This object reflects the total number of Temporarily Not  Available (480) responses sent by the user agent since system startup. Outbound Temporarily Not Available responses indicate that  the called party's end system was contacted successfully but  the called party is currently unavailable
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
        
        .. attribute:: csipstatsclientunauthorizedins
        
        	This object reflects the total number of Unauthorized (401)  responses received by the user agent since system startup.   Inbound Unauthorized responses indicate that requests issued  by this system require user authentication
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsclientunauthorizedouts
        
        	This object reflects the total number of Unauthorized (401)  responses sent by the user agent since system startup. Outbound Unauthorized responses indicate that requests  received by this system require user authentication
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsclientaddrincompleteins = None
            self.csipstatsclientaddrincompleteouts = None
            self.csipstatsclientambiguousins = None
            self.csipstatsclientambiguousouts = None
            self.csipstatsclientbadeventins = None
            self.csipstatsclientbadeventouts = None
            self.csipstatsclientbadextensionins = None
            self.csipstatsclientbadextensionouts = None
            self.csipstatsclientbadrequestins = None
            self.csipstatsclientbadrequestouts = None
            self.csipstatsclientbusyhereins = None
            self.csipstatsclientbusyhereouts = None
            self.csipstatsclientcalllegnoexistins = None
            self.csipstatsclientcalllegnoexistouts = None
            self.csipstatsclientconflictins = None
            self.csipstatsclientconflictouts = None
            self.csipstatsclientforbiddenins = None
            self.csipstatsclientforbiddenouts = None
            self.csipstatsclientgoneins = None
            self.csipstatsclientgoneouts = None
            self.csipstatsclientlengthrequiredins = None
            self.csipstatsclientlengthrequiredouts = None
            self.csipstatsclientloopdetectedins = None
            self.csipstatsclientloopdetectedouts = None
            self.csipstatsclientmethnotallowedins = None
            self.csipstatsclientmethnotallowedouts = None
            self.csipstatsclientnoaccepthereins = None
            self.csipstatsclientnoaccepthereouts = None
            self.csipstatsclientnosupmediatypeins = None
            self.csipstatsclientnosupmediatypeouts = None
            self.csipstatsclientnotacceptableins = None
            self.csipstatsclientnotacceptableouts = None
            self.csipstatsclientnotfoundins = None
            self.csipstatsclientnotfoundouts = None
            self.csipstatsclientpaymentreqdins = None
            self.csipstatsclientpaymentreqdouts = None
            self.csipstatsclientproxyauthreqdins = None
            self.csipstatsclientproxyauthreqdouts = None
            self.csipstatsclientreqenttoolargeins = None
            self.csipstatsclientreqenttoolargeouts = None
            self.csipstatsclientreqpendingins = None
            self.csipstatsclientreqpendingouts = None
            self.csipstatsclientreqtermins = None
            self.csipstatsclientreqtermouts = None
            self.csipstatsclientreqtimeoutins = None
            self.csipstatsclientreqtimeoutouts = None
            self.csipstatsclientrequritoolargeins = None
            self.csipstatsclientrequritoolargeouts = None
            self.csipstatsclientsttoosmallins = None
            self.csipstatsclientsttoosmallouts = None
            self.csipstatsclienttempnotavailins = None
            self.csipstatsclienttempnotavailouts = None
            self.csipstatsclienttoomanyhopsins = None
            self.csipstatsclienttoomanyhopsouts = None
            self.csipstatsclientunauthorizedins = None
            self.csipstatsclientunauthorizedouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsErrClient'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsclientaddrincompleteins is not None:
                return True

            if self.csipstatsclientaddrincompleteouts is not None:
                return True

            if self.csipstatsclientambiguousins is not None:
                return True

            if self.csipstatsclientambiguousouts is not None:
                return True

            if self.csipstatsclientbadeventins is not None:
                return True

            if self.csipstatsclientbadeventouts is not None:
                return True

            if self.csipstatsclientbadextensionins is not None:
                return True

            if self.csipstatsclientbadextensionouts is not None:
                return True

            if self.csipstatsclientbadrequestins is not None:
                return True

            if self.csipstatsclientbadrequestouts is not None:
                return True

            if self.csipstatsclientbusyhereins is not None:
                return True

            if self.csipstatsclientbusyhereouts is not None:
                return True

            if self.csipstatsclientcalllegnoexistins is not None:
                return True

            if self.csipstatsclientcalllegnoexistouts is not None:
                return True

            if self.csipstatsclientconflictins is not None:
                return True

            if self.csipstatsclientconflictouts is not None:
                return True

            if self.csipstatsclientforbiddenins is not None:
                return True

            if self.csipstatsclientforbiddenouts is not None:
                return True

            if self.csipstatsclientgoneins is not None:
                return True

            if self.csipstatsclientgoneouts is not None:
                return True

            if self.csipstatsclientlengthrequiredins is not None:
                return True

            if self.csipstatsclientlengthrequiredouts is not None:
                return True

            if self.csipstatsclientloopdetectedins is not None:
                return True

            if self.csipstatsclientloopdetectedouts is not None:
                return True

            if self.csipstatsclientmethnotallowedins is not None:
                return True

            if self.csipstatsclientmethnotallowedouts is not None:
                return True

            if self.csipstatsclientnoaccepthereins is not None:
                return True

            if self.csipstatsclientnoaccepthereouts is not None:
                return True

            if self.csipstatsclientnosupmediatypeins is not None:
                return True

            if self.csipstatsclientnosupmediatypeouts is not None:
                return True

            if self.csipstatsclientnotacceptableins is not None:
                return True

            if self.csipstatsclientnotacceptableouts is not None:
                return True

            if self.csipstatsclientnotfoundins is not None:
                return True

            if self.csipstatsclientnotfoundouts is not None:
                return True

            if self.csipstatsclientpaymentreqdins is not None:
                return True

            if self.csipstatsclientpaymentreqdouts is not None:
                return True

            if self.csipstatsclientproxyauthreqdins is not None:
                return True

            if self.csipstatsclientproxyauthreqdouts is not None:
                return True

            if self.csipstatsclientreqenttoolargeins is not None:
                return True

            if self.csipstatsclientreqenttoolargeouts is not None:
                return True

            if self.csipstatsclientreqpendingins is not None:
                return True

            if self.csipstatsclientreqpendingouts is not None:
                return True

            if self.csipstatsclientreqtermins is not None:
                return True

            if self.csipstatsclientreqtermouts is not None:
                return True

            if self.csipstatsclientreqtimeoutins is not None:
                return True

            if self.csipstatsclientreqtimeoutouts is not None:
                return True

            if self.csipstatsclientrequritoolargeins is not None:
                return True

            if self.csipstatsclientrequritoolargeouts is not None:
                return True

            if self.csipstatsclientsttoosmallins is not None:
                return True

            if self.csipstatsclientsttoosmallouts is not None:
                return True

            if self.csipstatsclienttempnotavailins is not None:
                return True

            if self.csipstatsclienttempnotavailouts is not None:
                return True

            if self.csipstatsclienttoomanyhopsins is not None:
                return True

            if self.csipstatsclienttoomanyhopsouts is not None:
                return True

            if self.csipstatsclientunauthorizedins is not None:
                return True

            if self.csipstatsclientunauthorizedouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsErrClient']['meta_info']


    class CSipStatsErrServer(object):
        """
        
        
        .. attribute:: csipstatsserverbadgatewayins
        
        	This object reflects the total number of Bad Gateway (502)  responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverbadgatewayouts
        
        	This object reflects the total number of Bad Gateway (502)  responses sent by the user agent since system startup
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
        
        .. attribute:: csipstatsservergatewaytimeoutins
        
        	This object reflects the total number of Gateway Time\-out  (504) responses received by the user agent since system startup. Inbound Gateway Time\-out responses indicate that the server attempting to complete this system's request did not receive a timely response from yet another system it was accessing to complete the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsservergatewaytimeoutouts
        
        	This object reflects the total number of Gateway Time\-out  (504) responses sent by the user agent since system startup. Outbound Gateway Time\-out responses indicate that this system did not receive a timely response from the system it had accessed to assist in completing a received request
        	**type**\: int
        
        	**range:** 0..4294967295
        
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
        
        .. attribute:: csipstatsserverprecondfailureins
        
        	This object reflects the total number of Precondition  Failure (580) responses received by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsserverprecondfailureouts
        
        	This object reflects the total number of Precondition  Failure (580) responses sent by the user agent since system startup. This response is returned by a UAS if it is unable to perform the mandatory preconditions for the session
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
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsserverbadgatewayins = None
            self.csipstatsserverbadgatewayouts = None
            self.csipstatsserverbadsipversionins = None
            self.csipstatsserverbadsipversionouts = None
            self.csipstatsservergatewaytimeoutins = None
            self.csipstatsservergatewaytimeoutouts = None
            self.csipstatsserverinterrorins = None
            self.csipstatsserverinterrorouts = None
            self.csipstatsservernotimplementedins = None
            self.csipstatsservernotimplementedouts = None
            self.csipstatsserverprecondfailureins = None
            self.csipstatsserverprecondfailureouts = None
            self.csipstatsserverserviceunavailins = None
            self.csipstatsserverserviceunavailouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsErrServer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsserverbadgatewayins is not None:
                return True

            if self.csipstatsserverbadgatewayouts is not None:
                return True

            if self.csipstatsserverbadsipversionins is not None:
                return True

            if self.csipstatsserverbadsipversionouts is not None:
                return True

            if self.csipstatsservergatewaytimeoutins is not None:
                return True

            if self.csipstatsservergatewaytimeoutouts is not None:
                return True

            if self.csipstatsserverinterrorins is not None:
                return True

            if self.csipstatsserverinterrorouts is not None:
                return True

            if self.csipstatsservernotimplementedins is not None:
                return True

            if self.csipstatsservernotimplementedouts is not None:
                return True

            if self.csipstatsserverprecondfailureins is not None:
                return True

            if self.csipstatsserverprecondfailureouts is not None:
                return True

            if self.csipstatsserverserviceunavailins is not None:
                return True

            if self.csipstatsserverserviceunavailouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsErrServer']['meta_info']


    class CSipStatsGlobalFail(object):
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
        
        .. attribute:: csipstatsglobalnotacceptableins
        
        	This object reflects the total number of Not Acceptable (606) responses received by the user agent since system startup. Inbound Not Acceptable responses indicate that the called party's end system was contacted successfully but some aspect of the session description is not acceptable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsglobalnotacceptableouts
        
        	This object reflects the total number of Not Acceptable (606) responses sent by the user agent since system startup. Outbound Not Acceptable responses indicate that the called party wishes to communicate, but cannot adequately support the session described in the request
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
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsglobalbusyeverywhereins = None
            self.csipstatsglobalbusyeverywhereouts = None
            self.csipstatsglobaldeclineins = None
            self.csipstatsglobaldeclineouts = None
            self.csipstatsglobalnotacceptableins = None
            self.csipstatsglobalnotacceptableouts = None
            self.csipstatsglobalnotanywhereins = None
            self.csipstatsglobalnotanywhereouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsGlobalFail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsglobalbusyeverywhereins is not None:
                return True

            if self.csipstatsglobalbusyeverywhereouts is not None:
                return True

            if self.csipstatsglobaldeclineins is not None:
                return True

            if self.csipstatsglobaldeclineouts is not None:
                return True

            if self.csipstatsglobalnotacceptableins is not None:
                return True

            if self.csipstatsglobalnotacceptableouts is not None:
                return True

            if self.csipstatsglobalnotanywhereins is not None:
                return True

            if self.csipstatsglobalnotanywhereouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsGlobalFail']['meta_info']


    class CSipStatsInfo(object):
        """
        
        
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
        
        .. attribute:: csipstatsinforingingins
        
        	This object reflects the total number of Ringing (180) responses received by the user agent since system startup. A inbound Ringing response indicates that the UAS processing a INVITE initiated by this system has  found a possible location where the desired end user  has registered recently and is trying to alert the user
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinforingingouts
        
        	This object reflects the total number of Ringing (180) responses sent by the user agent since system startup. A outbound Ringing response indicates that this system has processed an INVITE for a particular end user and found a possible location where that user has registered recently.  The system is trying to alert the end user and is conveying that status to the system that originated the INVITE
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
        
        .. attribute:: csipstatsinfotryingins
        
        	This object reflects the total number of Trying (100) responses received by the user agent since system startup.   Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Inbound Trying responses indicate that outbound INVITE request  sent out by this system have been received and are processed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsinfotryingouts
        
        	This object reflects the total number of Trying (100) responses sent by the user agent since system startup. Trying responses indicate that some unspecified action is being taken on behalf of this call, but the user has not yet been located.  Outbound Trying responses indicate this system is successfully  receiving INVITE requests and processing them on  behalf of the system initiating the INVITE
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsinfoforwardedins = None
            self.csipstatsinfoforwardedouts = None
            self.csipstatsinfoqueuedins = None
            self.csipstatsinfoqueuedouts = None
            self.csipstatsinforingingins = None
            self.csipstatsinforingingouts = None
            self.csipstatsinfosessionprogins = None
            self.csipstatsinfosessionprogouts = None
            self.csipstatsinfotryingins = None
            self.csipstatsinfotryingouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsinfoforwardedins is not None:
                return True

            if self.csipstatsinfoforwardedouts is not None:
                return True

            if self.csipstatsinfoqueuedins is not None:
                return True

            if self.csipstatsinfoqueuedouts is not None:
                return True

            if self.csipstatsinforingingins is not None:
                return True

            if self.csipstatsinforingingouts is not None:
                return True

            if self.csipstatsinfosessionprogins is not None:
                return True

            if self.csipstatsinfosessionprogouts is not None:
                return True

            if self.csipstatsinfotryingins is not None:
                return True

            if self.csipstatsinfotryingouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsInfo']['meta_info']


    class CSipStatsMisc(object):
        """
        
        
        .. attribute:: csipstatsmisc3xxmappedto4xxrsps
        
        	This object reflects the total number of incoming Redirect  (3xx) response messages that have been mapped to Client  Error (4xx) response messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsmisc3xxmappedto4xxrsps = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsMisc'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsmisc3xxmappedto4xxrsps is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsMisc']['meta_info']


    class CSipStatsRedirect(object):
        """
        
        
        .. attribute:: csipstatsrediraltservices
        
        	This object reflects the total number of Alternative Service (380) responses received by the user agent since system startup. Alternative Service responses indicate that the call was not successful, but alternative services are possible.  Those alternative services are described in the message body of the response
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
        
        .. attribute:: csipstatsredirmovedtempsins
        
        	This object reflects the total number of Moved Temporarily (302) responses received by the user agent since system startup.  Moved Temporarily responses indicate the UAC should retry the request directed at the new address(es)  given by the Contact header field of the response. The duration of this redirection can be indicated through the Expires header.  If no explicit expiration time is given, the new address(es) are only valid for this call
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmovedtempsouts
        
        	This object reflects the total number of Moved Temporarily (302) responses sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirmultiplechoices
        
        	This object reflects the total number of Multiple Choices (300) responses received by the user agent since system startup. Multiple Choices responses indicate that the called party can be reached at several different locations and the server cannot or prefers not to proxy the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsredirseeothers
        
        	This object reflects the total number of See Other  (303) responses received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsrediruseproxys
        
        	This object reflects the total number of Use Proxy  (305) responses received by the user agent since system startup. See Other responses indicate that requested resources must be accessed through the proxy given by the  Contact header field of the response.  The recipient of this response is expected to repeat this single request via the proxy
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsrediraltservices = None
            self.csipstatsredirmovedperms = None
            self.csipstatsredirmovedtemps = None
            self.csipstatsredirmovedtempsins = None
            self.csipstatsredirmovedtempsouts = None
            self.csipstatsredirmultiplechoices = None
            self.csipstatsredirseeothers = None
            self.csipstatsrediruseproxys = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsRedirect'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsrediraltservices is not None:
                return True

            if self.csipstatsredirmovedperms is not None:
                return True

            if self.csipstatsredirmovedtemps is not None:
                return True

            if self.csipstatsredirmovedtempsins is not None:
                return True

            if self.csipstatsredirmovedtempsouts is not None:
                return True

            if self.csipstatsredirmultiplechoices is not None:
                return True

            if self.csipstatsredirseeothers is not None:
                return True

            if self.csipstatsrediruseproxys is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsRedirect']['meta_info']


    class CSipStatsRetry(object):
        """
        
        
        .. attribute:: csipstatsretrybyes
        
        	This object reflects the total number of BYE retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycancels
        
        	This object reflects the total number of CANCEL retries that  have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrycomets
        
        	This object reflects the total number of COndition MET retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryinfo
        
        	This object reflects the total number of Info retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryinvites
        
        	This object reflects the total number of INVITE retries that  have been sent by the user agent since system startup.   If the number of 'first  attempt' INVITES is of interest, subtract the value of this  object from cSipStatsTrafficInviteOut
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrynotifys
        
        	This object reflects the total number of Notify  retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrypracks
        
        	This object reflects the total number of PRovisional ACKnowledgement retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryrefers
        
        	This object reflects the total number of Refer retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryregisters
        
        	This object reflects the total number of REGISTER retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryreliable1xxrsps
        
        	This object reflects the total number of Reliable 1xx Response retries sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretryresponses
        
        	This object reflects the total number of Response (while  expecting a ACK) retries that have been sent by the user agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatsretrysubscribe
        
        	This object reflects the total number of Subscribe retries that have been sent by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatsretrybyes = None
            self.csipstatsretrycancels = None
            self.csipstatsretrycomets = None
            self.csipstatsretryinfo = None
            self.csipstatsretryinvites = None
            self.csipstatsretrynotifys = None
            self.csipstatsretrypracks = None
            self.csipstatsretryrefers = None
            self.csipstatsretryregisters = None
            self.csipstatsretryreliable1xxrsps = None
            self.csipstatsretryresponses = None
            self.csipstatsretrysubscribe = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsRetry'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatsretrybyes is not None:
                return True

            if self.csipstatsretrycancels is not None:
                return True

            if self.csipstatsretrycomets is not None:
                return True

            if self.csipstatsretryinfo is not None:
                return True

            if self.csipstatsretryinvites is not None:
                return True

            if self.csipstatsretrynotifys is not None:
                return True

            if self.csipstatsretrypracks is not None:
                return True

            if self.csipstatsretryrefers is not None:
                return True

            if self.csipstatsretryregisters is not None:
                return True

            if self.csipstatsretryreliable1xxrsps is not None:
                return True

            if self.csipstatsretryresponses is not None:
                return True

            if self.csipstatsretrysubscribe is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsRetry']['meta_info']


    class CSipStatsSuccess(object):
        """
        
        
        .. attribute:: csipstatssuccessacceptedins
        
        	This object reflects the total number of Accepted (202) responses received by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessacceptedouts
        
        	This object reflects the total number of Accepted (202) responses sent by the user agent since system startup. The meaning of outbound 202 Ok responses depends on the method used in the associated request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessokins
        
        	This object reflects the total number of Ok (200) responses received by the user agent since system startup. The meaning of inbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatssuccessokouts
        
        	This object reflects the total number of Ok (200) responses sent by the user agent since system startup. The meaning of outbound Ok responses depends on the method used in the associated request.  BYE      \: The Ok response means the call has             been terminated.  CANCEL   \: The Ok response means the search for             the end user has been cancelled.  INVITE   \: The Ok response means the called party             has agreed to participate in the call.  OPTIONS  \: The Ok response means the called party             has agreed to share its capabilities.  REGISTER \: The Ok response means the registration            has succeeded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatssuccessacceptedins = None
            self.csipstatssuccessacceptedouts = None
            self.csipstatssuccessokins = None
            self.csipstatssuccessokouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsSuccess'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatssuccessacceptedins is not None:
                return True

            if self.csipstatssuccessacceptedouts is not None:
                return True

            if self.csipstatssuccessokins is not None:
                return True

            if self.csipstatssuccessokouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsSuccess']['meta_info']


    class CSipStatsSuccessOkTable(object):
        """
        This table contains statistics for sent and
        received 200 Ok response messages.  The 
        statistics are kept on per SIP method basis.
        
        .. attribute:: csipstatssuccessokentry
        
        	A row in the cSipStatsSuccessOkTable.  There is  an entry for each SIP method for which 200 Ok  inbound and/or outbound statistics are kept
        	**type**\: list of :py:class:`CSipStatsSuccessOkEntry <ydk.models.sip.CISCO_SIP_UA_MIB.CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry>`
        
        

        """

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatssuccessokentry = YList()
            self.csipstatssuccessokentry.parent = self
            self.csipstatssuccessokentry.name = 'csipstatssuccessokentry'


        class CSipStatsSuccessOkEntry(object):
            """
            A row in the cSipStatsSuccessOkTable.  There is 
            an entry for each SIP method for which 200 Ok 
            inbound and/or outbound statistics are kept.
            
            .. attribute:: csipstatssuccessokmethod
            
            	This object is used for instance identification of objects in this table.  The value reflects a SIP method
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: csipstatssuccessokinbounds
            
            	This object reflects the total number of Ok (200) responses sent by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csipstatssuccessokoutbounds
            
            	This object reflects the total number of Ok (200) responses received by the user agent, since system startup, that were associated with the SIP method as specified by cSipStatsSuccessOkMethod
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sip'
            _revision = '2004-02-19'

            def __init__(self):
                self.parent = None
                self.csipstatssuccessokmethod = None
                self.csipstatssuccessokinbounds = None
                self.csipstatssuccessokoutbounds = None

            @property
            def _common_path(self):
                if self.csipstatssuccessokmethod is None:
                    raise YPYDataValidationError('Key property csipstatssuccessokmethod is None')

                return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsSuccessOkTable/CISCO-SIP-UA-MIB:cSipStatsSuccessOkEntry[CISCO-SIP-UA-MIB:cSipStatsSuccessOkMethod = ' + str(self.csipstatssuccessokmethod) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csipstatssuccessokmethod is not None:
                    return True

                if self.csipstatssuccessokinbounds is not None:
                    return True

                if self.csipstatssuccessokoutbounds is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
                return meta._meta_table['CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsSuccessOkTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatssuccessokentry is not None:
                for child_ref in self.csipstatssuccessokentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsSuccessOkTable']['meta_info']


    class CSipStatsTraffic(object):
        """
        
        
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
        
        .. attribute:: csipstatstrafficcometins
        
        	This object reflects the total number of COndition MET  requests received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficcometouts
        
        	This object reflects the total number of COndition MET  requests sent by the user agent since system startup
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
        
        .. attribute:: csipstatstrafficinviteins
        
        	This object reflects the total number of INVITE requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficinviteouts
        
        	This object reflects the total number of INVITE requests sent by the user agent
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
        
        .. attribute:: csipstatstrafficoptionsins
        
        	This object reflects the total number of OPTIONS requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficoptionsouts
        
        	This object reflects the total number of OPTIONS requests sent by the user agent
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
        
        .. attribute:: csipstatstrafficregisterins
        
        	This object reflects the total number of REGISTER requests  received by the user agent since system startup
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: csipstatstrafficregisterouts
        
        	This object reflects the total number of REGISTER requests  sent by the user agent since system startup
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

        _prefix = 'cisco-sip'
        _revision = '2004-02-19'

        def __init__(self):
            self.parent = None
            self.csipstatstrafficackins = None
            self.csipstatstrafficackouts = None
            self.csipstatstrafficbyeins = None
            self.csipstatstrafficbyeouts = None
            self.csipstatstrafficcancelins = None
            self.csipstatstrafficcancelouts = None
            self.csipstatstrafficcometins = None
            self.csipstatstrafficcometouts = None
            self.csipstatstrafficinfoins = None
            self.csipstatstrafficinfoouts = None
            self.csipstatstrafficinviteins = None
            self.csipstatstrafficinviteouts = None
            self.csipstatstrafficnotifyins = None
            self.csipstatstrafficnotifyouts = None
            self.csipstatstrafficoptionsins = None
            self.csipstatstrafficoptionsouts = None
            self.csipstatstrafficprackins = None
            self.csipstatstrafficprackouts = None
            self.csipstatstrafficreferins = None
            self.csipstatstrafficreferouts = None
            self.csipstatstrafficregisterins = None
            self.csipstatstrafficregisterouts = None
            self.csipstatstrafficsubscribeins = None
            self.csipstatstrafficsubscribeouts = None
            self.csipstatstrafficupdateins = None
            self.csipstatstrafficupdateouts = None

        @property
        def _common_path(self):

            return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB/CISCO-SIP-UA-MIB:cSipStatsTraffic'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csipstatstrafficackins is not None:
                return True

            if self.csipstatstrafficackouts is not None:
                return True

            if self.csipstatstrafficbyeins is not None:
                return True

            if self.csipstatstrafficbyeouts is not None:
                return True

            if self.csipstatstrafficcancelins is not None:
                return True

            if self.csipstatstrafficcancelouts is not None:
                return True

            if self.csipstatstrafficcometins is not None:
                return True

            if self.csipstatstrafficcometouts is not None:
                return True

            if self.csipstatstrafficinfoins is not None:
                return True

            if self.csipstatstrafficinfoouts is not None:
                return True

            if self.csipstatstrafficinviteins is not None:
                return True

            if self.csipstatstrafficinviteouts is not None:
                return True

            if self.csipstatstrafficnotifyins is not None:
                return True

            if self.csipstatstrafficnotifyouts is not None:
                return True

            if self.csipstatstrafficoptionsins is not None:
                return True

            if self.csipstatstrafficoptionsouts is not None:
                return True

            if self.csipstatstrafficprackins is not None:
                return True

            if self.csipstatstrafficprackouts is not None:
                return True

            if self.csipstatstrafficreferins is not None:
                return True

            if self.csipstatstrafficreferouts is not None:
                return True

            if self.csipstatstrafficregisterins is not None:
                return True

            if self.csipstatstrafficregisterouts is not None:
                return True

            if self.csipstatstrafficsubscribeins is not None:
                return True

            if self.csipstatstrafficsubscribeouts is not None:
                return True

            if self.csipstatstrafficupdateins is not None:
                return True

            if self.csipstatstrafficupdateouts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
            return meta._meta_table['CISCOSIPUAMIB.CSipStatsTraffic']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-SIP-UA-MIB:CISCO-SIP-UA-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.csipcfgaaa is not None and self.csipcfgaaa._has_data():
            return True

        if self.csipcfgaaa is not None and self.csipcfgaaa.is_presence():
            return True

        if self.csipcfgbase is not None and self.csipcfgbase._has_data():
            return True

        if self.csipcfgbase is not None and self.csipcfgbase.is_presence():
            return True

        if self.csipcfgbindsourceaddrtable is not None and self.csipcfgbindsourceaddrtable._has_data():
            return True

        if self.csipcfgbindsourceaddrtable is not None and self.csipcfgbindsourceaddrtable.is_presence():
            return True

        if self.csipcfgcausestatustable is not None and self.csipcfgcausestatustable._has_data():
            return True

        if self.csipcfgcausestatustable is not None and self.csipcfgcausestatustable.is_presence():
            return True

        if self.csipcfgearlymediatable is not None and self.csipcfgearlymediatable._has_data():
            return True

        if self.csipcfgearlymediatable is not None and self.csipcfgearlymediatable.is_presence():
            return True

        if self.csipcfgpeer is not None and self.csipcfgpeer._has_data():
            return True

        if self.csipcfgpeer is not None and self.csipcfgpeer.is_presence():
            return True

        if self.csipcfgpeertable is not None and self.csipcfgpeertable._has_data():
            return True

        if self.csipcfgpeertable is not None and self.csipcfgpeertable.is_presence():
            return True

        if self.csipcfgretry is not None and self.csipcfgretry._has_data():
            return True

        if self.csipcfgretry is not None and self.csipcfgretry.is_presence():
            return True

        if self.csipcfgstatuscausetable is not None and self.csipcfgstatuscausetable._has_data():
            return True

        if self.csipcfgstatuscausetable is not None and self.csipcfgstatuscausetable.is_presence():
            return True

        if self.csipcfgtimer is not None and self.csipcfgtimer._has_data():
            return True

        if self.csipcfgtimer is not None and self.csipcfgtimer.is_presence():
            return True

        if self.csipcfgvoiceservicevoip is not None and self.csipcfgvoiceservicevoip._has_data():
            return True

        if self.csipcfgvoiceservicevoip is not None and self.csipcfgvoiceservicevoip.is_presence():
            return True

        if self.csipstatsconnection is not None and self.csipstatsconnection._has_data():
            return True

        if self.csipstatsconnection is not None and self.csipstatsconnection.is_presence():
            return True

        if self.csipstatserrclient is not None and self.csipstatserrclient._has_data():
            return True

        if self.csipstatserrclient is not None and self.csipstatserrclient.is_presence():
            return True

        if self.csipstatserrserver is not None and self.csipstatserrserver._has_data():
            return True

        if self.csipstatserrserver is not None and self.csipstatserrserver.is_presence():
            return True

        if self.csipstatsglobalfail is not None and self.csipstatsglobalfail._has_data():
            return True

        if self.csipstatsglobalfail is not None and self.csipstatsglobalfail.is_presence():
            return True

        if self.csipstatsinfo is not None and self.csipstatsinfo._has_data():
            return True

        if self.csipstatsinfo is not None and self.csipstatsinfo.is_presence():
            return True

        if self.csipstatsmisc is not None and self.csipstatsmisc._has_data():
            return True

        if self.csipstatsmisc is not None and self.csipstatsmisc.is_presence():
            return True

        if self.csipstatsredirect is not None and self.csipstatsredirect._has_data():
            return True

        if self.csipstatsredirect is not None and self.csipstatsredirect.is_presence():
            return True

        if self.csipstatsretry is not None and self.csipstatsretry._has_data():
            return True

        if self.csipstatsretry is not None and self.csipstatsretry.is_presence():
            return True

        if self.csipstatssuccess is not None and self.csipstatssuccess._has_data():
            return True

        if self.csipstatssuccess is not None and self.csipstatssuccess.is_presence():
            return True

        if self.csipstatssuccessoktable is not None and self.csipstatssuccessoktable._has_data():
            return True

        if self.csipstatssuccessoktable is not None and self.csipstatssuccessoktable.is_presence():
            return True

        if self.csipstatstraffic is not None and self.csipstatstraffic._has_data():
            return True

        if self.csipstatstraffic is not None and self.csipstatstraffic.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
        return meta._meta_table['CISCOSIPUAMIB']['meta_info']


class CiscoSipUaMIBNotificationPrefix_Identity(ObjectIdentity_Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'cisco-sip'
    _revision = '2004-02-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
        return meta._meta_table['CiscoSipUaMIBNotificationPrefix_Identity']['meta_info']


class CiscoSipUaMIBNotifications_Identity(ObjectIdentity_Identity):
    """
    Old style notification prefixing.  Being replaced by
    ciscoSipUaMIBNotifs.
    
    

    """

    _prefix = 'cisco-sip'
    _revision = '2004-02-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.sip._meta import _CISCO_SIP_UA_MIB as meta
        return meta._meta_table['CiscoSipUaMIBNotifications_Identity']['meta_info']


