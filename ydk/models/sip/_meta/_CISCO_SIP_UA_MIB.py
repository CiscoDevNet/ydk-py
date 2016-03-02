


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOSIPUAMIB.CSipCfgAaa.CSipCfgAaaUsername_Enum' : _MetaInfoEnum('CSipCfgAaaUsername_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'callingNumber':'CALLINGNUMBER',
            'proxyAuth':'PROXYAUTH',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgAaa' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgAaa',
            False, 
            [
            _MetaInfoClassMember('cSipCfgAaaUsername', REFERENCE_ENUM_CLASS, 'CSipCfgAaaUsername_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgAaa.CSipCfgAaaUsername_Enum', 
                [], [], 
                '''                This object specifies the source of the information used to
                populate the username attribute of AAA billing records.
                ''',
                'csipcfgaaausername',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgAaa',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgBase.CSipCfgBindSrcAddrScope_Enum' : _MetaInfoEnum('CSipCfgBindSrcAddrScope_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'all':'ALL',
            'control':'CONTROL',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBase.CSipCfgDnsSrvQueryStringFormat_Enum' : _MetaInfoEnum('CSipCfgDnsSrvQueryStringFormat_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'v1':'V1',
            'v2':'V2',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBase.CSipCfgOfferCallHold_Enum' : _MetaInfoEnum('CSipCfgOfferCallHold_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'directionAttr':'DIRECTIONATTR',
            'connAddr':'CONNADDR',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBase.CSipCfgSymNatDirectionRole_Enum' : _MetaInfoEnum('CSipCfgSymNatDirectionRole_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'none':'NONE',
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBase.CSipCfgTransport_Enum' : _MetaInfoEnum('CSipCfgTransport_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'udp':'UDP',
            'tcp':'TCP',
            'udpAndTcp':'UDPANDTCP',
            'disabled':'DISABLED',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBase' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgBase',
            False, 
            [
            _MetaInfoClassMember('cSipCfgBindSrcAddrInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object may specify the interface where the
                source IP address used in SIP signalling or media
                packets is configured.  A value of 0 means that 
                there is no specific source address configured and 
                in this case the best local IP address will be chosen 
                by the system.
                ''',
                'csipcfgbindsrcaddrinterface',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgBindSrcAddrScope', REFERENCE_ENUM_CLASS, 'CSipCfgBindSrcAddrScope_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase.CSipCfgBindSrcAddrScope_Enum', 
                [], [], 
                '''                This object specifies the scope of packets to
                which the source IP address of the interface 
                designated by cSipCfgBindSrcAddrInterface
                will be bound.  A value of 'all' means the IP address 
                will be bound to both SIP signalling and media packets.
                A value of 'control' means the IP address will only
                be bound to SIP signalling packets.  
                If cSipCfgBindSrcAddrInterface is set to 0,
                the value of this object has no meaning.
                ''',
                'csipcfgbindsrcaddrscope',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgDnsSrvQueryStringFormat', REFERENCE_ENUM_CLASS, 'CSipCfgDnsSrvQueryStringFormat_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase.CSipCfgDnsSrvQueryStringFormat_Enum', 
                [], [], 
                '''                This object specifies the format of the prefix used 
                by the system for DNS SRV queries.
                
                v1  :  RFC 2052 format - 'protocol.transport.'
                v2  :  RFC 2782 format - '_protocol._transport.'
                
                This object allows backward compatibility with systems
                only supporting RFC 2052 format.
                ''',
                'csipcfgdnssrvquerystringformat',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgMaxForwards', ATTRIBUTE, 'int' , None, None, 
                [(1, 15)], [], 
                '''                This object may be used with any SIP method to limit the 
                number of proxies that can forward the request to the next 
                downstream server.
                ''',
                'csipcfgmaxforwards',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgMaximumForwards', ATTRIBUTE, 'int' , None, None, 
                [(1, 70)], [], 
                '''                This object may be used with any SIP method to limit the 
                number of proxies that can forward the request to the next 
                downstream server.
                ''',
                'csipcfgmaximumforwards',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgOfferCallHold', REFERENCE_ENUM_CLASS, 'CSipCfgOfferCallHold_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase.CSipCfgOfferCallHold_Enum', 
                [], [], 
                '''                This object specifies how the SIP gateway would initiate call
                hold requests.
                
                directionAttr: The user agent will use the direction
                                attribute such as a=sendonly or a=inactive in
                                the sdp to initiate call hold requests.
                                  
                connAddr: The user agent will use 0.0.0.0 connection address
                           to specify Call Hold.
                ''',
                'csipcfgoffercallhold',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgReasonHeaderOveride', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies that the Reason header overrides SIP 
                status code mapping table.
                ''',
                'csipcfgreasonheaderoveride',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRedirectionDisabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies how call redirection (3xx)
                is handled by the user agent.  
                
                If 'false', the user agent's treatment of incoming 
                3xx class response messages is as defined in RFC 2543.  
                That is, the user agent uses the Contact header(s)
                from the 3xx response to reinitiate another INVITE
                transaction to the user's new location.  The call 
                is redirected.
                
                If 'true', the user agent treats incoming 3xx 
                response messages as 4xx (client error) class 
                response messages.  In this case, the call is not
                redirected, instead it is released with the 
                appropriate PSTN cause code.
                
                The mapping of SIP 3xx response status codes to
                4xx response status codes is as follows:
                 300 Multiple Choices -> 410 Gone
                 301 Moved Permanently -> 410 Gone
                 302 Moved Temporarily -> 480 Temporarily Unavailable
                 305 User Proxy        -> 410 Gone
                 380 Alternative Service -> 410 Gone
                 Any other 3xx -> 410 Gone
                ''',
                'csipcfgredirectiondisabled',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgSuspendResumeEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies if support for handling 
                Suspend/Resume events from the switch is enabled or not.
                
                If 'true', the user agent on getting a Suspend will
                notify the remote agent by sending it a re-invite with
                a hold SDP. Similarly, when the Gateway receives a Resume, it
                will initiate a re-invite with the original SDP and unhold the
                call.
                
                If 'false', the user agent will not initiate any re-invites
                on receiving Suspend/Resume events, basically it won't be
                putting the call on hold or off hold.
                ''',
                'csipcfgsuspendresumeenabled',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgSymNatDirectionRole', REFERENCE_ENUM_CLASS, 'CSipCfgSymNatDirectionRole_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase.CSipCfgSymNatDirectionRole_Enum', 
                [], [], 
                '''                This object specifies the value of the
                'a=direction:<role>' SDP attribute supported by 
                the user agent.  The direction attribute is used 
                to describe the role of the user agent (as an 
                endpoint for a connection-oriented media stream) 
                in the connection setup procedure.
                
                none    :  No role is specified.
                passive :  The user agent will advertise itself
                           as a 'passive' entity (inside the NAT)
                           in the SDP.
                active  :  The user agent will advertise itself
                           as a 'active' entity (outside the NAT)
                           in the SDP.
                ''',
                'csipcfgsymnatdirectionrole',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgSymNatEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether remote media checks
                for Symmetric Network Address Translation (NAT) 
                is enabled or disabled.
                
                If 'true', remote media checks are enabled.  The
                gateway will have the ability to open a Real Time 
                Transport Protocol (RTP) session with the remote
                end and then update (modify) the existing RTP
                session's remote address/port (raddr:rport) with
                the source address and port of the actual media
                packet received.  This would be triggered for only
                those calls where the Session Description Protocol
                (SDP) received by the gateway has an indication to
                do so.
                
                If 'false', remote media checks are disabled.
                ''',
                'csipcfgsymnatenabled',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTransport', REFERENCE_ENUM_CLASS, 'CSipCfgTransport_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase.CSipCfgTransport_Enum', 
                [], [], 
                '''                This object specifies the transport protocol the SIP user 
                agent will use to receive SIP messages.  A value of 'disabled'
                indicates that the UA will not receive any SIP messages.
                ''',
                'csipcfgtransport',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgUserLocationServerAddr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object specifies address of the User Location 
                Server (ULS) being used to resolve the location of end 
                points.  This could be a Domain Name Server (DNS) or a 
                SIP proxy/redirect server.
                
                The format of the address follows the IETF service location 
                protocol. The syntax is as follows:
                
                   mapping-type:type-specific-syntax
                
                the mapping-type specifies a scheme for mapping the matching 
                dial string to a target server. The type-specific-syntax is 
                exactly that, something that the particular mapping scheme can
                understand.  For example,
                   Session target           Meaning
                   ipv4:171.68.13.55:1006   The session target is the IP 
                                            version 4 address of 171.68.13.55 
                                            and port 1006.
                   dns:pots.cisco.com       The session target is the IP host 
                                            with dns name pots.cisco.com.
                
                The valid Mapping type definitions for the peer follow:
                   ipv4  - Syntax: ipv4:w.x.y.z:port or  ipv4:w.x.y.z 
                   dns   - Syntax: dns:host.domain.
                ''',
                'csipcfguserlocationserveraddr',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgVersion', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object will reflect the version of SIP supported by this 
                user agent.  It will follow the same format as SIP version 
                information contained in the SIP messages generated by this
                user agent.  For example, user agents supporting SIP version 2
                will return 'SIP/2.0' as dictated by RFC 2543.
                ''',
                'csipcfgversion',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgBase',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry.CSipCfgBindSourceAddrScope_Enum' : _MetaInfoEnum('CSipCfgBindSourceAddrScope_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'media':'MEDIA',
            'control':'CONTROL',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgBindSourceAddrScope', REFERENCE_ENUM_CLASS, 'CSipCfgBindSourceAddrScope_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry.CSipCfgBindSourceAddrScope_Enum', 
                [], [], 
                '''                A unique identifier of a row in this table and
                specifies the scope of packets to which the
                source IP address of the interface
                designated by cSipCfgBindSourceAddrInterface
                will be bound.
                ''',
                'csipcfgbindsourceaddrscope',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipCfgBindSourceAddrInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object may specify the interface where the
                source IP address used in SIP signalling or media
                packets is configured.  A value of 0 means that
                there is no specific source address configured and
                in this case the best local IP address will be chosen
                by the system.
                ''',
                'csipcfgbindsourceaddrinterface',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgBindSourceAddrEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgBindSourceAddrTable',
            False, 
            [
            _MetaInfoClassMember('cSipCfgBindSourceAddrEntry', REFERENCE_LIST, 'CSipCfgBindSourceAddrEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry', 
                [], [], 
                '''                A row in the cSipCfgBindSourceAddrTable.
                A row is accessible with the scope of packets
                to which the source IP address of the interface
                designated by cSipCfgBindSourceAddrInterface
                will be bound.
                ''',
                'csipcfgbindsourceaddrentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgBindSourceAddrTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgPstnCauseIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A unique identifier of a row in this table and
                a valid PSTN cause code.
                ''',
                'csipcfgpstncauseindex',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipCfgCauseStatusStoreStatus', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object reflects the storage status of this
                table entry.  If the value is 'volatile', then
                this entry only exists in RAM and the information
                would be lost (reverting to defaults) on system reload.  
                If the value is 'nonVolatile' then this entry has been 
                written to NVRAM and will persist across system reloads.
                ''',
                'csipcfgcausestatusstorestatus',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgStatusCode', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The SIP status code to which the PSTN cause code
                given by cSipCfgPstnCauseIndex is to be mapped
                for outbound SIP response messages.
                ''',
                'csipcfgstatuscode',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgCauseStatusEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgCauseStatusTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgCauseStatusTable',
            False, 
            [
            _MetaInfoClassMember('cSipCfgCauseStatusEntry', REFERENCE_LIST, 'CSipCfgCauseStatusEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry', 
                [], [], 
                '''                A row in the cSipCfgCauseStatusTable. Entries cannot be
                created or destroyed by the actions of any NMS.
                ''',
                'csipcfgcausestatusentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgCauseStatusTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgEarlyMediaStatusCodeIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A unique identifier of a row in this table and
                a valid SIP status code.
                ''',
                'csipcfgearlymediastatuscodeindex',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipCfgEarlyMediaCutThruDisabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether Early Media 
                Cut Through is enabled or disabled for the 
                SIP response messages with status codes that 
                match cSipCfgEarlyMediaStatusCodeIndex.
                
                If 'true', early media cut through is disabled,
                and the user agent will process the message as
                though it did not contain any SDP payload.
                
                If 'false', early media cut through is enabled,
                and the user agent will process the message
                similar to a 183 (Session Progress) and cut
                through for early media.  The assumption being
                that the SDP is an indication that the far end
                is going to send early media.
                ''',
                'csipcfgearlymediacutthrudisabled',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgEarlyMediaEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgEarlyMediaTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgEarlyMediaTable',
            False, 
            [
            _MetaInfoClassMember('cSipCfgEarlyMediaEntry', REFERENCE_LIST, 'CSipCfgEarlyMediaEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry', 
                [], [], 
                '''                A row in the cSipCfgEarlyMediaTable.
                A row is accessible with a Provisional (1xx)
                status code value (eg, 180) and provides
                an object for the enabling or disabling of
                the Early Media Cut Through functionality.
                ''',
                'csipcfgearlymediaentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgEarlyMediaTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgOutSessionTransport_Enum' : _MetaInfoEnum('CSipCfgOutSessionTransport_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'udp':'UDP',
            'tcp':'TCP',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgReliable1xxRspHdr_Enum' : _MetaInfoEnum('CSipCfgReliable1xxRspHdr_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'supported':'SUPPORTED',
            'require':'REQUIRE',
            'disabled':'DISABLED',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgUrlType_Enum' : _MetaInfoEnum('CSipCfgUrlType_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'sip':'SIP',
            'tel':'TEL',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeer' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgPeer',
            False, 
            [
            _MetaInfoClassMember('cSipCfgOutSessionTransport', REFERENCE_ENUM_CLASS, 'CSipCfgOutSessionTransport_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgOutSessionTransport_Enum', 
                [], [], 
                '''                This object specifies the session transport 
                protocol that will be used for outbound SIP 
                messages.  This configuration is applicable
                to all dial-peers in the system having 
                cSipCfgPeerOutSessionTransport set to 'system'.
                ''',
                'csipcfgoutsessiontransport',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgReliable1xxRspHdr', REFERENCE_ENUM_CLASS, 'CSipCfgReliable1xxRspHdr_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgReliable1xxRspHdr_Enum', 
                [], [], 
                '''                This object specifies behavior with respect to
                Supported or Require headers in SIP messages sent
                and received via this dial-peer.
                
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
                ''',
                'csipcfgreliable1xxrsphdr',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgReliable1xxRspStr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object specifies the string that will be 
                placed in either the Supported or Require SIP 
                header, as specified by cSipCfgReliable1xxRspHdr.
                ''',
                'csipcfgreliable1xxrspstr',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgUrlType', REFERENCE_ENUM_CLASS, 'CSipCfgUrlType_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeer.CSipCfgUrlType_Enum', 
                [], [], 
                '''                This object specifies the URL type sent in outbound
                INVITES generated by this device.
                ''',
                'csipcfgurltype',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgPeer',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerOutSessionTransport_Enum' : _MetaInfoEnum('CSipCfgPeerOutSessionTransport_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'system':'SYSTEM',
            'udp':'UDP',
            'tcp':'TCP',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerReliable1xxRspHdr_Enum' : _MetaInfoEnum('CSipCfgPeerReliable1xxRspHdr_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'system':'SYSTEM',
            'supported':'SUPPORTED',
            'require':'REQUIRE',
            'disabled':'DISABLED',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerUrlType_Enum' : _MetaInfoEnum('CSipCfgPeerUrlType_Enum', 'ydk.models.sip.CISCO_SIP_UA_MIB',
        {
            'system':'SYSTEM',
            'sip':'SIP',
            'tel':'TEL',
        }, 'CISCO-SIP-UA-MIB', _yang_ns._namespaces['CISCO-SIP-UA-MIB']),
    'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgPeerIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                An arbitrary index that uniquely identifies a 
                dial-peer configured for SIP.
                ''',
                'csipcfgpeerindex',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipCfgPeerOutSessionTransport', REFERENCE_ENUM_CLASS, 'CSipCfgPeerOutSessionTransport_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerOutSessionTransport_Enum', 
                [], [], 
                '''                This object specifies the session transport 
                protocol that will be used by this dial-peer
                for outbound SIP messages.  
                
                The value 'system' is the default and indicates 
                that this dial-peer should use the value set by 
                cSipCfgOutSessionTransport instead.
                ''',
                'csipcfgpeeroutsessiontransport',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeerReliable1xxRspHdr', REFERENCE_ENUM_CLASS, 'CSipCfgPeerReliable1xxRspHdr_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerReliable1xxRspHdr_Enum', 
                [], [], 
                '''                This object specifies behavior with respect to
                Support or Require headers in SIP messages sent
                and received via this dial-peer.
                
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
                dial-peer should use the value of  cSipCfgReliable1xxRspHdr
                instead.
                ''',
                'csipcfgpeerreliable1xxrsphdr',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeerReliable1xxRspStr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object specifies the string that will be 
                placed in either the Supported or Require SIP 
                header, as specified by cSipCfgPeerReliable1xxRspHdr.
                ''',
                'csipcfgpeerreliable1xxrspstr',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeerSwitchTransEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies if the functionality of switching
                between transports from UDP to TCP if the message size of a
                Request is greater than 1300 bytes is enabled or not.
                ''',
                'csipcfgpeerswitchtransenabled',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeerUrlType', REFERENCE_ENUM_CLASS, 'CSipCfgPeerUrlType_Enum' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry.CSipCfgPeerUrlType_Enum', 
                [], [], 
                '''                This object specifies the URL type sent in outbound
                INVITES generated by this device.
                
                The value 'system' is the default and indicates that this 
                dial-peer should use the value of cSipCfgUrlType instead.
                ''',
                'csipcfgpeerurltype',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgPeerEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgPeerTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgPeerTable',
            False, 
            [
            _MetaInfoClassMember('cSipCfgPeerEntry', REFERENCE_LIST, 'CSipCfgPeerEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry', 
                [], [], 
                '''                A row in the cSipCfgPeerTable.
                ''',
                'csipcfgpeerentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgPeerTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgRetry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgRetry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgRetryBye', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a BYE request.
                ''',
                'csipcfgretrybye',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryCancel', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a CANCEL request.
                ''',
                'csipcfgretrycancel',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryComet', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a COMET (COndition MET).
                ''',
                'csipcfgretrycomet',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryInfo', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent
                will retry sending a Info request.
                ''',
                'csipcfgretryinfo',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryInvite', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a INVITE request.
                ''',
                'csipcfgretryinvite',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryNotify', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a Notify request.
                ''',
                'csipcfgretrynotify',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryPrack', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a PRACK (PRovisional ACKnowledgement).
                ''',
                'csipcfgretryprack',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryRefer', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a Refer request.
                ''',
                'csipcfgretryrefer',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryRegister', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a REGISTER request.
                ''',
                'csipcfgretryregister',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryReliableRsp', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a reliable response.
                ''',
                'csipcfgretryreliablersp',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetryResponse', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent 
                will retry sending a Response and expecting a ACK.
                ''',
                'csipcfgretryresponse',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetrySubscribe', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This object specifies the number of times a user agent
                will retry sending a Subscribe request.
                ''',
                'csipcfgretrysubscribe',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgRetry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry',
            False, 
            [
            _MetaInfoClassMember('cSipCfgStatusCodeIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A unique identifier of a row in this table and
                a valid SIP status code.
                ''',
                'csipcfgstatuscodeindex',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipCfgPstnCause', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The PSTN cause code to which the SIP status code
                given by cSipCfgStatusCodeIndex is to be mapped
                for outbound PSTN signalling messages.
                ''',
                'csipcfgpstncause',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgStatusCauseStoreStatus', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object reflects the storage status of this
                table entry.  If the value is 'volatile', then
                this entry only exists in RAM and the information
                would be lost (reverting to defaults) on system reload.  
                If the value is 'nonVolatile' then this entry has been 
                written to NVRAM and will persist across system reloads.
                ''',
                'csipcfgstatuscausestorestatus',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgStatusCauseEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgStatusCauseTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgStatusCauseTable',
            False, 
            [
            _MetaInfoClassMember('cSipCfgStatusCauseEntry', REFERENCE_LIST, 'CSipCfgStatusCauseEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry', 
                [], [], 
                '''                A row in the cSipCfgStatusCauseTable.  Entries cannot be
                created or destroyed by the actions of any NMS.
                ''',
                'csipcfgstatuscauseentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgStatusCauseTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgTimer' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgTimer',
            False, 
            [
            _MetaInfoClassMember('cSipCfgTimerBufferInvite', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (50, 5000)], [], 
                '''                This object specifies the amount of time to buffer the INVITE 
                while waiting for display name info in the Facility.
                
                A value of 0 means that the INVITE wouldn't be buffered
                waiting for the display name info in the Facility.
                ''',
                'csipcfgtimerbufferinvite',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerComet', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the time a user agent will wait 
                for a final response before retransmitting the COMET 
                (COndition MET).
                ''',
                'csipcfgtimercomet',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerConnect', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the time a user agent will wait to 
                receive an ACK confirmation a session is established.
                ''',
                'csipcfgtimerconnect',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerConnectionAging', ATTRIBUTE, 'int' , None, None, 
                [(5, 30)], [], 
                '''                This object specifies the amount of time to wait before 
                aging out a TCP/UDP connection.
                ''',
                'csipcfgtimerconnectionaging',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerDisconnect', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the time a user agent will wait to 
                receive an BYE confirmation a session is disconnected.
                ''',
                'csipcfgtimerdisconnect',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerExpires', ATTRIBUTE, 'int' , None, None, 
                [(60000, 300000)], [], 
                '''                This object specifies the time a user agent will wait to 
                receive a final response to a INVITE before cancelling the 
                transaction.
                ''',
                'csipcfgtimerexpires',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerHold', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (15, 2880)], [], 
                '''                This object specifies the amount of time to wait before 
                disconnecting a call already on hold. A value of 0 specifies
                that this functionality is disabled.
                ''',
                'csipcfgtimerhold',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerInfo', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the amount of time to wait for a
                200ok response before retransmitting the Info.
                ''',
                'csipcfgtimerinfo',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerNotify', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the amount of time to wait for a
                final response before retransmitting the Notify.
                ''',
                'csipcfgtimernotify',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerPrack', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the time a user agent will wait for 
                a final response before retransmitting the PRACK (PRovisional
                ACKnowledgment).
                ''',
                'csipcfgtimerprack',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerRefer', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the amount of time to wait for a
                final response before retransmitting the Refer.
                ''',
                'csipcfgtimerrefer',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerReliableRsp', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the amount of time to wait for a
                PRACK before retransmitting the reliable 1xx response.
                ''',
                'csipcfgtimerreliablersp',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerSessionTimer', ATTRIBUTE, 'int' , None, None, 
                [(60, 86400)], [], 
                '''                This object specifies the value of the Min-SE 
                header for INVITE messages originated by this 
                user agent and the minimum value of the 
                Session-Expires headers for INVITE messages 
                received by this user agent.
                
                Any Session-Expires headers received with a 
                value below this object's value will be rejected
                with a 422 client error response message.
                
                Setting this object to a value less than 600 is
                valid, but the possibly of excessive re-INVITES 
                and the impact of those messages should be fully 
                understood and considered an acceptable risk.
                ''',
                'csipcfgtimersessiontimer',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimerTrying', ATTRIBUTE, 'int' , None, None, 
                [(100, 1000)], [], 
                '''                This object specifies the time a user agent will wait to 
                receive a provisional response to a INVITE before resending 
                the INVITE.
                ''',
                'csipcfgtimertrying',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgTimer',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipCfgVoiceServiceVoip' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipCfgVoiceServiceVoip',
            False, 
            [
            _MetaInfoClassMember('cSipCfgHeaderPassingEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies if support for passing
                SIP headers from Invite, Subscribe, Notify Request to the
                application is enabled.
                
                If 'true', the headers received in a message will be passed
                to the application.
                
                If 'false', the headers received in a message will not be
                passed to the application.
                ''',
                'csipcfgheaderpassingenabled',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgMaxSubscriptionAccept', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the maximum number of concurrent SIP
                subscriptions a SIP Gateway can accept.
                ''',
                'csipcfgmaxsubscriptionaccept',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgMaxSubscriptionOriginate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the maximum number of concurrent SIP
                subscriptions that a SIP Gateway can originate. Default is Max
                Dialpeers on platform. Maximum is 2*Max Dialpeers on
                Platform.
                ''',
                'csipcfgmaxsubscriptionoriginate',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgSwitchTransportEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies if the functionality of switching
                between transports from udp to tcp if the message size of a
                Request is greater than 1300 bytes is enabled or not.
                
                This configuration is at the global level, and will only be 
                considered if there exists no voip dial-peer.
                ''',
                'csipcfgswitchtransportenabled',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipCfgVoiceServiceVoip',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsConnection' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsConnection',
            False, 
            [
            _MetaInfoClassMember('cSipStatsActiveTCPConnections', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of active TCP
                connections since system startup.
                ''',
                'csipstatsactivetcpconnections',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsActiveUDPConnections', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of active UDP
                connections since system startup.
                ''',
                'csipstatsactiveudpconnections',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnTCPCreateFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of connection create
                failures for TCP since system startup.
                ''',
                'csipstatsconntcpcreatefailures',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnTCPInactiveTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of TCP connections that
                timed out due to inactivity since system startup.
                ''',
                'csipstatsconntcpinactivetimeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnTCPRemoteClosures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Remote Closures 
                for TCP since system startup.
                ''',
                'csipstatsconntcpremoteclosures',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnTCPSendFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of TCP send failures
                since system startup.
                ''',
                'csipstatsconntcpsendfailures',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnUDPCreateFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of connection create
                failures for UDP since system startup.
                ''',
                'csipstatsconnudpcreatefailures',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnUDPInactiveTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of UDP connections that 
                timed out due to inactivity since system startup.
                ''',
                'csipstatsconnudpinactivetimeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnUDPSendFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of UDP send failures
                since system startup.
                ''',
                'csipstatsconnudpsendfailures',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsConnection',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsErrClient' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsErrClient',
            False, 
            [
            _MetaInfoClassMember('cSipStatsClientAddrIncompleteIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Address Incomplete 
                (484) responses received by the user agent since system startup.
                Inbound Address Incomplete responses indicate that requests 
                issued by this system had To addresses or Request-URIs that 
                were incomplete.
                ''',
                'csipstatsclientaddrincompleteins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientAddrIncompleteOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Address Incomplete 
                (484) responses sent by the user agent since system startup.
                Outbound Address Incomplete responses indicate that requests 
                received by this system had To addresses or Request-URIs that 
                were incomplete.
                ''',
                'csipstatsclientaddrincompleteouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientAmbiguousIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ambiguous (485) 
                responses received by the user agent since system startup.
                Inbound Ambiguous responses indicate that requests issued
                by this system provided ambiguous address information.
                ''',
                'csipstatsclientambiguousins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientAmbiguousOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ambiguous (485) 
                responses sent by the user agent since system startup.
                Outbound Ambiguous responses indicate that requests received
                by this system contained ambiguous address information.
                ''',
                'csipstatsclientambiguousouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadEventIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of BadEvent (489) 
                responses received by the user agent since system startup.
                ''',
                'csipstatsclientbadeventins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadEventOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of BadEvent (489) 
                responses sent by the user agent since system startup.
                ''',
                'csipstatsclientbadeventouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadExtensionIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Extension (420) 
                responses received by the user agent since system startup.
                Inbound Bad Extension responses indicate that the recipient 
                did not understand the protocol extension specified in a 
                Require header field.
                ''',
                'csipstatsclientbadextensionins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadExtensionOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Extension (420) 
                responses sent by the user agent since system startup.
                Outbound Bad Extension responses indicate that this system
                did not understand the protocol extension specified in a
                Require header field of requests.
                ''',
                'csipstatsclientbadextensionouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadRequestIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Request (400) 
                responses received by the user agent since system startup.
                Inbound Bad Request responses indicate that requests issued 
                by this system could not be understood due to malformed 
                syntax.
                ''',
                'csipstatsclientbadrequestins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBadRequestOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Request (400) 
                responses sent by the user agent since system startup.
                Outbound Bad Request responses indicate that requests 
                received by this system could not be understood due to 
                malformed syntax.
                ''',
                'csipstatsclientbadrequestouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBusyHereIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Busy Here (486) 
                responses received by the user agent since system startup.
                Inbound Busy Here responses indicate that the
                called party is currently not willing or not able to
                take additional calls.
                ''',
                'csipstatsclientbusyhereins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientBusyHereOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Busy Here (486) 
                responses sent by the user agent since system startup.
                Outbound Busy Here responses indicate that the
                called party's end system was contacted successfully but the
                called party is currently not willing or able to take 
                additional calls.
                ''',
                'csipstatsclientbusyhereouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientCallLegNoExistIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Call Leg/Transaction 
                Does Not Exist (481) responses received by the user agent since system startup.
                Inbound Call Leg/Transaction Does Not Exist responses indicate
                that either BYE or CANCEL requests issued by this system were 
                received by a server and not matching call leg or transaction 
                existed.
                ''',
                'csipstatsclientcalllegnoexistins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientCallLegNoExistOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Call Leg/Transaction 
                Does Not Exist (481) responses sent by the user agent since system startup.
                Outbound Call Leg/Transaction Does Not Exist responses 
                indicate that BYE or CANCEL requests have been received by 
                this system and not call leg or transaction matching that 
                request exists.
                ''',
                'csipstatsclientcalllegnoexistouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientConflictIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Conflict (409) 
                responses received by the user agent since system startup.
                Inbound Conflict responses indicate that requests issued
                by this system could not be completed due to a conflict
                with the current state of a requested resource.
                ''',
                'csipstatsclientconflictins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientConflictOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Conflict (409) 
                responses sent by the user agent since system startup.
                Outbound Conflict responses indicate that requests received
                by this system could not be completed due to a conflict
                with the current state of a requested resource.
                ''',
                'csipstatsclientconflictouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientForbiddenIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Forbidden (403) 
                responses received by the user agent since system startup.
                Inbound Forbidden responses indicate that requests issued
                by this system are understood by the server but the server
                refuses to fulfill the request.  Authorization will not help
                and the requests should not be repeated.
                ''',
                'csipstatsclientforbiddenins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientForbiddenOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Forbidden (403) 
                responses sent by the user agent since system startup.
                Outbound Forbidden responses indicate that requests received
                by this system are understood but this system is refusing to
                fulfill the requests.
                ''',
                'csipstatsclientforbiddenouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientGoneIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Gone (410) 
                responses received by the user agent since system startup.
                Inbound Gone responses indicate that resources requested
                by this system are no longer available at the recipient server
                and no forwarding address is known.
                ''',
                'csipstatsclientgoneins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientGoneOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Gone (410) 
                responses sent by the user agent since system startup.
                Outbound Gone responses indicate that the requested
                resources are no longer available at this system and
                no forwarding address is known.
                ''',
                'csipstatsclientgoneouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientLengthRequiredIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Length Required 
                (411) responses received by the user agent since system startup.
                Inbound Length Required responses indicate that requests 
                issued by this system are being refused by servers because 
                of no defined Content-Length header field.
                ''',
                'csipstatsclientlengthrequiredins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientLengthRequiredOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Length Required 
                (411) responses sent by the user agent since system startup.
                Outbound Length Required responses indicate that requests 
                received by this system are being refused because of no 
                defined Content-Length header field.
                ''',
                'csipstatsclientlengthrequiredouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientLoopDetectedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Loop Detected (482) 
                responses received by the user agent since system startup.
                Inbound Loop Detected responses indicate that requests issued
                by this system were received at servers and the server found 
                itself in the Via path more than once.
                ''',
                'csipstatsclientloopdetectedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientLoopDetectedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Loop Detected (482) 
                responses sent by the user agent since system startup.
                Outbound Loop Detected responses indicate that requests 
                received by this system contain a Via path with this system 
                appearing more than once.
                ''',
                'csipstatsclientloopdetectedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientMethNotAllowedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Method Not Allowed 
                (405) received responses by the user agent.
                Inbound Method Not Allowed responses indicate that requests 
                issued by this system have specified a SIP method in the 
                Request-Line that is not allowed for the address identified 
                by the Request-URI.
                ''',
                'csipstatsclientmethnotallowedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientMethNotAllowedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Method Not Allowed 
                (405) received sent by the user agent since system startup.
                Outbound Method Not Allowed responses indicate that requests 
                received by this system have SIP methods specified in the 
                Request-Line that are not allowed for the address identified 
                by the Request-URI.
                ''',
                'csipstatsclientmethnotallowedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNoAcceptHereIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable Here
                (488) responses received by the user agent since system startup.
                The response has the same meaning as 606 (Not Acceptable), 
                but only applies to the specific entity addressed by the 
                Request-URI and the request may succeed elsewhere.
                ''',
                'csipstatsclientnoaccepthereins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNoAcceptHereOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable Here
                (488) responses sent by the user agent since system startup.
                The response has the same meaning as 606 (Not Acceptable), 
                but only applies to the specific entity addressed by the 
                Request-URI and the request may succeed elsewhere.
                ''',
                'csipstatsclientnoaccepthereouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNoSupMediaTypeIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Unsupported Media 
                Type (415) responses received by the user agent since system startup.
                Inbound Unsupported Media Type responses indicate that 
                requests issued by this system are being refused because the 
                message body of the request is in a format not supported by 
                the requested resource for the requested method.
                ''',
                'csipstatsclientnosupmediatypeins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNoSupMediaTypeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Unsupported Media 
                Type (415) responses sent by the user agent since system startup.
                Outbound Unsupported Media Type responses indicate that the 
                body of requests received by this system are in a format not 
                supported by the requested resource for the requested method.
                ''',
                'csipstatsclientnosupmediatypeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNotAcceptableIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable 
                (406) responses received by the user agent since system startup.
                Inbound Not Acceptable responses indicate the resources 
                identified by requests issued by this system cannot generate 
                responses with content characteristics acceptable to this 
                system according to the accept headers sent in the requests.
                ''',
                'csipstatsclientnotacceptableins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNotAcceptableOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable (406) 
                responses sent by the user agent since system startup.
                Outbound Not Acceptable responses indicate that the resources
                identified by requests received by this system cannot generate
                responses with content characteristics acceptable to the 
                system sending the requests.
                ''',
                'csipstatsclientnotacceptableouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNotFoundIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Found (404) 
                responses received by the user agent since system startup.
                Inbound Not Found responses indicate that the called party 
                does not exist at the domain specified in the Request-URI 
                or the domain is not handled by the recipient of the request.
                ''',
                'csipstatsclientnotfoundins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientNotFoundOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Found (404) 
                responses sent by the user agent since system startup.
                Outbound Not Found responses indicate that this system
                knows that the called party does not exist at the domain
                specified in the Request-URI or the domain is not handled
                by this system.
                ''',
                'csipstatsclientnotfoundouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientPaymentReqdIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Payment Required 
                (402) responses received by the user agent since system startup.
                ''',
                'csipstatsclientpaymentreqdins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientPaymentReqdOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Payment Required 
                (402) responses sent by the user agent since system startup.
                ''',
                'csipstatsclientpaymentreqdouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientProxyAuthReqdIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Proxy Authentication 
                Required (407) responses received by the user agent since system startup.
                Inbound Proxy Authentication Required responses indicate that 
                this system must authenticate itself with the proxy before 
                gaining access to the requested resource.
                ''',
                'csipstatsclientproxyauthreqdins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientProxyAuthReqdOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Proxy Authentication 
                Required (407) responses sent by the user agent since system startup.
                Outbound Proxy Authentication Required responses indicate that
                the systems issuing requests being processed by this system 
                must authenticate themselves with this system before gaining 
                access to requested resources.
                ''',
                'csipstatsclientproxyauthreqdouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqEntTooLargeIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Entity Too 
                Large (413) responses received by the user agent since system startup.
                Inbound Request Entity Too Large responses indicate that 
                requests issued by this system are being refused because 
                the request is larger than the server is willing or able to 
                process.
                ''',
                'csipstatsclientreqenttoolargeins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqEntTooLargeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Entity Too 
                Large (413) responses sent by the user agent since system startup.
                Outbound Request Entity Too Large responses indicate that 
                requests received by this system are larger than this system 
                is willing or able to process.
                ''',
                'csipstatsclientreqenttoolargeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqPendingIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of RequestPending
                (491) responses received by the user agent since system
                startup.
                ''',
                'csipstatsclientreqpendingins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqPendingOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of RequestPending
                (491) responses sent by the user agent since system startup.
                ''',
                'csipstatsclientreqpendingouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqTermIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Terminated 
                (487) responses received by the user agent since system startup.
                Request Terminated responses are issued if the original 
                request was terminated via CANCEL or BYE.
                ''',
                'csipstatsclientreqtermins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqTermOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Terminated 
                (487) responses sent by the user agent since system startup.
                Request Terminated responses are issued if the original 
                request was terminated via CANCEL or BYE.
                ''',
                'csipstatsclientreqtermouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqTimeoutIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Timeout 
                (408) responses received by the user agent since system startup.
                Inbound Request Timeout responses indicate that requests 
                issued by this system are not being processed by the server 
                within the time indicated in the Expires header of the 
                request.
                ''',
                'csipstatsclientreqtimeoutins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqTimeoutOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request Timeout 
                (408) responses sent by the user agent since system startup.
                Outbound Request Timeout responses indicate that this 
                system is not able to produce an appropriate response within 
                the time indicated in the Expires header of the request.
                ''',
                'csipstatsclientreqtimeoutouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqURITooLargeIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request-URI Too 
                Large (414) responses received by the user agent since system startup.
                Inbound Request-URI Too Large responses indicate that 
                requests issued by this system are being refused because the 
                Request-URI is longer than the server is willing or able to 
                interpret.
                ''',
                'csipstatsclientrequritoolargeins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientReqURITooLargeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Request-URI Too 
                Large (414) responses sent by the user agent since system startup.
                Outbound Request-URI Too Large responses indicate that 
                Request-URIs received by this system are longer than this 
                system is willing or able to interpret.
                ''',
                'csipstatsclientrequritoolargeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientSTTooSmallIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of SessionTimerTooSmall
                (422) responses received by the user agent since system 
                startup.
                ''',
                'csipstatsclientsttoosmallins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientSTTooSmallOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of SessionTimerTooSmall
                (422) responses sent by the user agent since system startup.
                ''',
                'csipstatsclientsttoosmallouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientTempNotAvailIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Temporarily Not 
                Available (480) responses received by the user agent since system startup.
                Inbound Temporarily Not Available responses indicate that 
                the called party is currently unavailable.
                ''',
                'csipstatsclienttempnotavailins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientTempNotAvailOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Temporarily Not 
                Available (480) responses sent by the user agent since system startup.
                Outbound Temporarily Not Available responses indicate that 
                the called party's end system was contacted successfully but 
                the called party is currently unavailable.
                ''',
                'csipstatsclienttempnotavailouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientTooManyHopsIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Too Many Hops (483) 
                responses received by the user agent since system startup.
                Inbound Too Many Hops responses indicate that requests issued
                by this system contain more Via entries (hops) than allowed by
                the Max-Forwards header field of the requests.
                ''',
                'csipstatsclienttoomanyhopsins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientTooManyHopsOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Too Many Hops (483) 
                responses sent by the user agent since system startup.
                Outbound Too Many Hops responses indicate that requests
                received by this system contain more Via entries (hops) than
                are allowed by the Max-Forwards header field of the requests.
                ''',
                'csipstatsclienttoomanyhopsouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientUnauthorizedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Unauthorized (401) 
                responses received by the user agent since system startup.  
                Inbound Unauthorized responses indicate that requests issued 
                by this system require user authentication.
                ''',
                'csipstatsclientunauthorizedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsClientUnauthorizedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Unauthorized (401) 
                responses sent by the user agent since system startup.
                Outbound Unauthorized responses indicate that requests 
                received by this system require user authentication.
                ''',
                'csipstatsclientunauthorizedouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsErrClient',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsErrServer' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsErrServer',
            False, 
            [
            _MetaInfoClassMember('cSipStatsServerBadGatewayIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Gateway (502) 
                responses received by the user agent since system startup.
                ''',
                'csipstatsserverbadgatewayins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerBadGatewayOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Bad Gateway (502) 
                responses sent by the user agent since system startup.
                ''',
                'csipstatsserverbadgatewayouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerBadSipVersionIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of SIP Version Not 
                Supported (505) responses received by the user agent since system startup.
                Inbound SIP Version Not Supported responses indicate that 
                the server does not support, or refuses to support, the SIP 
                protocol version that was used in the request message.
                ''',
                'csipstatsserverbadsipversionins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerBadSipVersionOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of SIP Version Not 
                Supported (505) responses sent by the user agent since system startup.
                Outbound SIP Version Not Supported responses indicate that 
                this system does not support, or refuses to support, the SIP 
                protocol version used in received requests.
                ''',
                'csipstatsserverbadsipversionouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerGatewayTimeoutIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Gateway Time-out 
                (504) responses received by the user agent since system startup.
                Inbound Gateway Time-out responses indicate that the server
                attempting to complete this system's request did not receive
                a timely response from yet another system it was accessing to
                complete the request.
                ''',
                'csipstatsservergatewaytimeoutins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerGatewayTimeoutOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Gateway Time-out 
                (504) responses sent by the user agent since system startup.
                Outbound Gateway Time-out responses indicate that this system
                did not receive a timely response from the system it had
                accessed to assist in completing a received request.
                ''',
                'csipstatsservergatewaytimeoutouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerIntErrorIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Internal Server Error
                (500) responses received by the user agent since system startup.
                Inbound Internal Server Error responses indicate that servers 
                to which this system is sending requests have encountered 
                unexpected conditions that prevent them from fulfilling the 
                requests.
                ''',
                'csipstatsserverinterrorins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerIntErrorOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Internal Server Error
                (500) responses sent by the user agent since system startup.
                Outbound Internal Server Error responses indicate that this 
                system has encountered unexpected conditions that prevent it 
                from fulfilling received requests.
                ''',
                'csipstatsserverinterrorouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerNotImplementedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Implemented 
                (501) responses received by the user agent since system startup.
                Inbound Not Implemented responses indicate that servers to 
                which this system is sending requests do not support the 
                functionality required to fulfill the requests.
                ''',
                'csipstatsservernotimplementedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerNotImplementedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Implemented 
                (501) responses sent by the user agent since system startup.
                Outbound Not Implemented responses indicate that this system
                does not support the functionality required to fulfill the 
                requests.
                ''',
                'csipstatsservernotimplementedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerPrecondFailureIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Precondition 
                Failure (580) responses received by the user agent since system startup.
                This response is returned by a UAS if it is unable to
                perform the mandatory preconditions for the session.
                ''',
                'csipstatsserverprecondfailureins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerPrecondFailureOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Precondition 
                Failure (580) responses sent by the user agent since system startup.
                This response is returned by a UAS if it is unable to
                perform the mandatory preconditions for the session.
                ''',
                'csipstatsserverprecondfailureouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerServiceUnavailIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Service Unavailable 
                (503) responses received by the user agent since system startup.
                Inbound Service Unavailable responses indicate that the server
                servicing this system's request is temporarily unavailable to
                handle the request.
                ''',
                'csipstatsserverserviceunavailins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsServerServiceUnavailOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Service Unavailable 
                (503) responses sent by the user agent since system startup.
                Outbound Service Unavailable responses indicate that this
                system is temporarily unable to handle received requests.
                ''',
                'csipstatsserverserviceunavailouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsErrServer',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsGlobalFail' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsGlobalFail',
            False, 
            [
            _MetaInfoClassMember('cSipStatsGlobalBusyEverywhereIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Busy
                Everywhere (600) responses received by the user agent since system startup.
                Inbound Busy Everywhere responses indicate that the 
                called party's end system was contacted successfully
                but the called party is busy and does not wish to take
                the call at this time.
                ''',
                'csipstatsglobalbusyeverywhereins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalBusyEverywhereOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Busy
                Everywhere (600) responses sent by the user agent since system startup.
                Outbound Busy Everywhere responses indicate that 
                this system has successfully contacted a called party's
                end system and the called party does not wish to take
                the call at this time.
                ''',
                'csipstatsglobalbusyeverywhereouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalDeclineIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Decline
                (603) responses received by the user agent since system startup.
                Decline responses indicate that the called party's end 
                system was contacted successfully but the called party 
                explicitly does not wish to, or cannot, participate.
                ''',
                'csipstatsglobaldeclineins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalDeclineOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Decline
                (603) responses sent by the user agent since system startup.
                Outbound Decline responses indicate that this system
                has successfully contacted a called party's end system
                and the called party explicitly does not wish to, or
                cannot, participate.
                ''',
                'csipstatsglobaldeclineouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalNotAcceptableIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable
                (606) responses received by the user agent since system startup.
                Inbound Not Acceptable responses indicate that the called
                party's end system was contacted successfully but some
                aspect of the session description is not acceptable.
                ''',
                'csipstatsglobalnotacceptableins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalNotAcceptableOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Not Acceptable
                (606) responses sent by the user agent since system startup.
                Outbound Not Acceptable responses indicate that the called
                party wishes to communicate, but cannot adequately support
                the session described in the request.
                ''',
                'csipstatsglobalnotacceptableouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalNotAnywhereIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Does Not
                Exist Anywhere (604) responses received by the user agent since system startup.
                Inbound Does Not Exist Anywhere responses indicate that
                the server handling this system's request has authoritative
                information that the called party indicated in the To
                request field does not exist anywhere.
                ''',
                'csipstatsglobalnotanywhereins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalNotAnywhereOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Does Not
                Exist Anywhere (604) responses sent by the user agent since system startup.
                Outbound Does Not Exist Anywhere responses indicate that
                this system has authoritative information that the called
                party in the To field of received requests does not exist
                anywhere.
                ''',
                'csipstatsglobalnotanywhereouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsGlobalFail',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsInfo' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsInfo',
            False, 
            [
            _MetaInfoClassMember('cSipStatsInfoForwardedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Call Is Being
                Forwarded (181) responses received by the user agent since system startup.
                A proxy server may use a Forwarded status code to
                indicate that the call is being forwarded to a different
                set of destinations.  Inbound Forwarded responses indicate 
                to this system that forwarding actions are taking place 
                with regard to calls initiated by this system.
                ''',
                'csipstatsinfoforwardedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoForwardedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Call Is Being
                Forwarded (181) responses sent by the user agent since system startup.
                A proxy server may use a Forwarded status code to
                indicate that the call is being forwarded to a different
                set of destinations.  Outbound Forwarded responses
                indicate this system is taking some forwarding action
                for calls and conveying that status to the system that
                initiated the calls.
                ''',
                'csipstatsinfoforwardedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoQueuedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Queued
                (182) responses received by the user agent since system startup.
                Inbound Queued responses indicate that the users
                this system is attempting to call are temporarily
                unavailable but the SIP agents operating on behalf
                of those users wish to queue the calls rather than
                reject them.  When the called parties become available,
                this system can expect to receive the appropriate
                final status response.  The Reason-Phrase from the
                Queued response messages Status-Line may give further
                details about the status of the call.  Multiple 
                Queued responses to update this system about the status
                of the queued call my be received.
                ''',
                'csipstatsinfoqueuedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoQueuedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Queued
                (182) responses sent by the user agent since system startup.
                Outbound Queued responses indicate this system
                has determined that the called party is temporarily
                unavailable but the call is not rejected.  Rather 
                the call is queued until the called party becomes
                available.  Queued responses messages are sent to
                the system originating the call request to convey
                the current status of a queued call.
                ''',
                'csipstatsinfoqueuedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoRingingIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ringing
                (180) responses received by the user agent since system startup.
                A inbound Ringing response indicates that the UAS
                processing a INVITE initiated by this system has 
                found a possible location where the desired end user 
                has registered recently and is trying to alert the user.
                ''',
                'csipstatsinforingingins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoRingingOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ringing
                (180) responses sent by the user agent since system startup.
                A outbound Ringing response indicates that this
                system has processed an INVITE for a particular
                end user and found a possible location where that
                user has registered recently.  The system is trying
                to alert the end user and is conveying that status
                to the system that originated the INVITE.
                ''',
                'csipstatsinforingingouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoSessionProgIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Session
                Progress (183) responses received by the user agent since system startup.
                ''',
                'csipstatsinfosessionprogins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoSessionProgOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Session
                Progress (183) responses sent by the user agent since system startup.
                ''',
                'csipstatsinfosessionprogouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoTryingIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Trying
                (100) responses received by the user agent since system startup.  
                Trying responses indicate that some unspecified
                action is being taken on behalf of this call, but
                the user has not yet been located.  Inbound Trying
                responses indicate that outbound INVITE request 
                sent out by this system have been received and
                are processed.
                ''',
                'csipstatsinfotryingins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfoTryingOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Trying
                (100) responses sent by the user agent since system startup.
                Trying responses indicate that some unspecified
                action is being taken on behalf of this call, but
                the user has not yet been located.  Outbound Trying
                responses indicate this system is successfully 
                receiving INVITE requests and processing them on 
                behalf of the system initiating the INVITE.
                ''',
                'csipstatsinfotryingouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsInfo',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsMisc' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsMisc',
            False, 
            [
            _MetaInfoClassMember('cSipStatsMisc3xxMappedTo4xxRsps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of incoming Redirect 
                (3xx) response messages that have been mapped to Client 
                Error (4xx) response messages.
                ''',
                'csipstatsmisc3xxmappedto4xxrsps',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsMisc',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsRedirect' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsRedirect',
            False, 
            [
            _MetaInfoClassMember('cSipStatsRedirAltServices', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Alternative
                Service (380) responses received by the user agent since system startup.
                Alternative Service responses indicate that the call
                was not successful, but alternative services are
                possible.  Those alternative services are described
                in the message body of the response.
                ''',
                'csipstatsrediraltservices',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirMovedPerms', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Moved 
                Permanently (301) responses received by the user agent since system startup.
                Moved Permanently responses indicate that the called party 
                can no longer be found at the address offered in the request 
                and the requesting UAC should retry at the new address given 
                by the Contact header field of the response.
                ''',
                'csipstatsredirmovedperms',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirMovedTemps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Moved 
                Temporarily (302) responses received by the user agent since system startup.
                Moved Temporarily responses indicate the UAC should
                retry the request directed at the new address(es)
                given by the Contact header field of the response.
                The duration of this redirection can be indicated
                through the Expires header.  If no explicit expiration
                time is given, the new address(es) are only valid
                for this call.
                ''',
                'csipstatsredirmovedtemps',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirMovedTempsIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Moved
                Temporarily (302) responses received by the user agent since
                system startup. 
                Moved Temporarily responses indicate the UAC should
                retry the request directed at the new address(es) 
                given by the Contact header field of the response.
                The duration of this redirection can be indicated
                through the Expires header.  If no explicit expiration
                time is given, the new address(es) are only valid
                for this call.
                ''',
                'csipstatsredirmovedtempsins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirMovedTempsOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Moved
                Temporarily (302) responses sent by the user agent since
                system startup.
                ''',
                'csipstatsredirmovedtempsouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirMultipleChoices', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Multiple
                Choices (300) responses received by the user agent since system startup.
                Multiple Choices responses indicate that the called
                party can be reached at several different locations
                and the server cannot or prefers not to proxy the request.
                ''',
                'csipstatsredirmultiplechoices',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirSeeOthers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of See Other 
                (303) responses received by the user agent since system startup.
                ''',
                'csipstatsredirseeothers',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirUseProxys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Use Proxy 
                (305) responses received by the user agent since system startup.
                See Other responses indicate that requested resources
                must be accessed through the proxy given by the 
                Contact header field of the response.  The recipient
                of this response is expected to repeat this single
                request via the proxy.
                ''',
                'csipstatsrediruseproxys',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsRedirect',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsRetry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsRetry',
            False, 
            [
            _MetaInfoClassMember('cSipStatsRetryByes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of BYE retries that have
                been sent by the user agent since system startup.
                ''',
                'csipstatsretrybyes',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryCancels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of CANCEL retries that 
                have been sent by the user agent since system startup.
                ''',
                'csipstatsretrycancels',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryComets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of COndition
                MET retries sent by the user agent since system startup.
                ''',
                'csipstatsretrycomets',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryInfo', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Info
                retries that have been sent by the user agent since system
                startup.
                ''',
                'csipstatsretryinfo',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryInvites', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of INVITE retries that 
                have been sent by the user agent since system startup.   If the number of 'first 
                attempt' INVITES is of interest, subtract the value of this 
                object from cSipStatsTrafficInviteOut.
                ''',
                'csipstatsretryinvites',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Notify 
                retries that have been sent by the user agent since system startup.
                ''',
                'csipstatsretrynotifys',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryPracks', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of PRovisional
                ACKnowledgement retries sent by the user agent since system startup.
                ''',
                'csipstatsretrypracks',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryRefers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Refer
                retries that have been sent by the user agent since system startup.
                ''',
                'csipstatsretryrefers',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryRegisters', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of REGISTER retries that
                have been sent by the user agent since system startup.
                ''',
                'csipstatsretryregisters',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryReliable1xxRsps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Reliable
                1xx Response retries sent by the user agent since system startup.
                ''',
                'csipstatsretryreliable1xxrsps',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetryResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Response (while 
                expecting a ACK) retries that have been sent by the user
                agent.
                ''',
                'csipstatsretryresponses',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetrySubscribe', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Subscribe
                retries that have been sent by the user agent since system
                startup.
                ''',
                'csipstatsretrysubscribe',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsRetry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsSuccess' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsSuccess',
            False, 
            [
            _MetaInfoClassMember('cSipStatsSuccessAcceptedIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Accepted
                (202) responses received by the user agent since system startup.
                The meaning of outbound 202 Ok responses depends
                on the method used in the associated request.
                ''',
                'csipstatssuccessacceptedins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccessAcceptedOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Accepted
                (202) responses sent by the user agent since system startup.
                The meaning of outbound 202 Ok responses depends
                on the method used in the associated request.
                ''',
                'csipstatssuccessacceptedouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccessOkIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ok
                (200) responses received by the user agent since system startup.
                The meaning of inbound Ok responses depends
                on the method used in the associated request.
                
                BYE      : The Ok response means the call has 
                           been terminated.
                
                CANCEL   : The Ok response means the search for 
                           the end user has been cancelled.
                
                INVITE   : The Ok response means the called party 
                           has agreed to participate in the call.
                
                OPTIONS  : The Ok response means the called party 
                           has agreed to share its capabilities.
                
                REGISTER : The Ok response means the registration
                           has succeeded.
                ''',
                'csipstatssuccessokins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccessOkOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ok
                (200) responses sent by the user agent since system startup.
                The meaning of outbound Ok responses depends
                on the method used in the associated request.
                
                BYE      : The Ok response means the call has 
                           been terminated.
                
                CANCEL   : The Ok response means the search for 
                           the end user has been cancelled.
                
                INVITE   : The Ok response means the called party 
                           has agreed to participate in the call.
                
                OPTIONS  : The Ok response means the called party 
                           has agreed to share its capabilities.
                
                REGISTER : The Ok response means the registration
                           has succeeded.
                ''',
                'csipstatssuccessokouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsSuccess',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry',
            False, 
            [
            _MetaInfoClassMember('cSipStatsSuccessOkMethod', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                This object is used for instance identification
                of objects in this table.  The value reflects a
                SIP method.
                ''',
                'csipstatssuccessokmethod',
                'CISCO-SIP-UA-MIB', True),
            _MetaInfoClassMember('cSipStatsSuccessOkInbounds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ok
                (200) responses sent by the user agent, since
                system startup, that were associated with the
                SIP method as specified by cSipStatsSuccessOkMethod.
                ''',
                'csipstatssuccessokinbounds',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccessOkOutbounds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Ok
                (200) responses received by the user agent, since
                system startup, that were associated with the
                SIP method as specified by cSipStatsSuccessOkMethod.
                ''',
                'csipstatssuccessokoutbounds',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsSuccessOkEntry',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsSuccessOkTable' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsSuccessOkTable',
            False, 
            [
            _MetaInfoClassMember('cSipStatsSuccessOkEntry', REFERENCE_LIST, 'CSipStatsSuccessOkEntry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry', 
                [], [], 
                '''                A row in the cSipStatsSuccessOkTable.  There is 
                an entry for each SIP method for which 200 Ok 
                inbound and/or outbound statistics are kept.
                ''',
                'csipstatssuccessokentry',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsSuccessOkTable',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB.CSipStatsTraffic' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB.CSipStatsTraffic',
            False, 
            [
            _MetaInfoClassMember('cSipStatsTrafficAckIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of ACK requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficackins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficAckOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of ACK requests sent
                by the user agent.
                ''',
                'csipstatstrafficackouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficByeIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of BYE requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficbyeins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficByeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of BYE requests sent
                by the user agent.
                ''',
                'csipstatstrafficbyeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficCancelIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of CANCEL requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficcancelins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficCancelOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of CANCEL requests sent
                by the user agent.
                ''',
                'csipstatstrafficcancelouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficCometIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of COndition MET 
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficcometins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficCometOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of COndition MET 
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficcometouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficInfoIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Info 
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficinfoins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficInfoOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Info 
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficinfoouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficInviteIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of INVITE requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficinviteins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficInviteOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of INVITE requests sent
                by the user agent.
                ''',
                'csipstatstrafficinviteouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficNotifyIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Notify 
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficnotifyins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficNotifyOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Notify 
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficnotifyouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficOptionsIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of OPTIONS requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficoptionsins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficOptionsOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of OPTIONS requests sent
                by the user agent.
                ''',
                'csipstatstrafficoptionsouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficPrackIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of PRovisonal 
                ACKnowledgement requests received by the user agent since system startup.
                ''',
                'csipstatstrafficprackins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficPrackOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of PRovisonal 
                ACKnowledgement requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficprackouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficReferIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Refer
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficreferins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficReferOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Refer
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficreferouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficRegisterIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of REGISTER requests 
                received by the user agent since system startup.
                ''',
                'csipstatstrafficregisterins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficRegisterOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of REGISTER requests 
                sent by the user agent since system startup.
                ''',
                'csipstatstrafficregisterouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficSubscribeIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Subscribe
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficsubscribeins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficSubscribeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Subscribe
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficsubscribeouts',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficUpdateIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Update
                requests received by the user agent since system startup.
                ''',
                'csipstatstrafficupdateins',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTrafficUpdateOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object reflects the total number of Update
                requests sent by the user agent since system startup.
                ''',
                'csipstatstrafficupdateouts',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'cSipStatsTraffic',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CISCOSIPUAMIB' : {
        'meta_info' : _MetaInfoClass('CISCOSIPUAMIB',
            False, 
            [
            _MetaInfoClassMember('cSipCfgAaa', REFERENCE_CLASS, 'CSipCfgAaa' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgAaa', 
                [], [], 
                '''                ''',
                'csipcfgaaa',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgBase', REFERENCE_CLASS, 'CSipCfgBase' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBase', 
                [], [], 
                '''                ''',
                'csipcfgbase',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgBindSourceAddrTable', REFERENCE_CLASS, 'CSipCfgBindSourceAddrTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgBindSourceAddrTable', 
                [], [], 
                '''                This table contains configuration for binding
                the scope of packets to the particular ethernet
                interface. The scope for the packets can be
                specified as either 'signalling' or 'media'
                packets. The ethernet interface shall be
                specified by the interface index. The table
                shall be indexed based on the scope.
                ''',
                'csipcfgbindsourceaddrtable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgCauseStatusTable', REFERENCE_CLASS, 'CSipCfgCauseStatusTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgCauseStatusTable', 
                [], [], 
                '''                This table contains PSTN cause code to SIP status code
                mapping configuration.   Inbound PSTN signalling messages
                that will result in outbound SIP response messages 
                will have the PSTN cause codes transposed into the
                SIP status codes as prescribed by the contents of this 
                table.
                ''',
                'csipcfgcausestatustable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgEarlyMediaTable', REFERENCE_CLASS, 'CSipCfgEarlyMediaTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgEarlyMediaTable', 
                [], [], 
                '''                This table contains configuration for Early
                Media Cut Through.  The configuration controls
                how the SIP user agent will process 1xx
                (Provisional) SIP response messages that contain 
                Session Definition Protocol (SDP) payloads.
                ''',
                'csipcfgearlymediatable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeer', REFERENCE_CLASS, 'CSipCfgPeer' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeer', 
                [], [], 
                '''                ''',
                'csipcfgpeer',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgPeerTable', REFERENCE_CLASS, 'CSipCfgPeerTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgPeerTable', 
                [], [], 
                '''                This table contains per dial-peer SIP related 
                configuration.   
                
                The table is a sparse table of dial-peer information.
                This means, it only reflects dial-peers being used 
                for SIP.  A dial-peer is being used for SIP if the 
                value of cvVoIPPeerCfgSessionProtocol 
                (CISCO-VOICE-DIAL-CONTROL-MIB) is 'sip'.
                
                Dial-peers are not created or destroyed via this
                table.  Only SIP related configuration can be 
                performed via this table once the dial-peer exists
                in the system and is visible in this table.
                ''',
                'csipcfgpeertable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgRetry', REFERENCE_CLASS, 'CSipCfgRetry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgRetry', 
                [], [], 
                '''                ''',
                'csipcfgretry',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgStatusCauseTable', REFERENCE_CLASS, 'CSipCfgStatusCauseTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgStatusCauseTable', 
                [], [], 
                '''                This table contains SIP status code to PSTN cause code
                mapping configuration.  Inbound SIP response messages 
                that will result in outbound PSTN signalling messages
                will have the SIP status codes transposed into the
                PSTN cause codes as prescribed by the contents of this 
                table.
                ''',
                'csipcfgstatuscausetable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgTimer', REFERENCE_CLASS, 'CSipCfgTimer' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgTimer', 
                [], [], 
                '''                ''',
                'csipcfgtimer',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipCfgVoiceServiceVoip', REFERENCE_CLASS, 'CSipCfgVoiceServiceVoip' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipCfgVoiceServiceVoip', 
                [], [], 
                '''                ''',
                'csipcfgvoiceservicevoip',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsConnection', REFERENCE_CLASS, 'CSipStatsConnection' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsConnection', 
                [], [], 
                '''                ''',
                'csipstatsconnection',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsErrClient', REFERENCE_CLASS, 'CSipStatsErrClient' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsErrClient', 
                [], [], 
                '''                ''',
                'csipstatserrclient',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsErrServer', REFERENCE_CLASS, 'CSipStatsErrServer' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsErrServer', 
                [], [], 
                '''                ''',
                'csipstatserrserver',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsGlobalFail', REFERENCE_CLASS, 'CSipStatsGlobalFail' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsGlobalFail', 
                [], [], 
                '''                ''',
                'csipstatsglobalfail',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsInfo', REFERENCE_CLASS, 'CSipStatsInfo' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsInfo', 
                [], [], 
                '''                ''',
                'csipstatsinfo',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsMisc', REFERENCE_CLASS, 'CSipStatsMisc' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsMisc', 
                [], [], 
                '''                ''',
                'csipstatsmisc',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRedirect', REFERENCE_CLASS, 'CSipStatsRedirect' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsRedirect', 
                [], [], 
                '''                ''',
                'csipstatsredirect',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsRetry', REFERENCE_CLASS, 'CSipStatsRetry' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsRetry', 
                [], [], 
                '''                ''',
                'csipstatsretry',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccess', REFERENCE_CLASS, 'CSipStatsSuccess' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsSuccess', 
                [], [], 
                '''                ''',
                'csipstatssuccess',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsSuccessOkTable', REFERENCE_CLASS, 'CSipStatsSuccessOkTable' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsSuccessOkTable', 
                [], [], 
                '''                This table contains statistics for sent and
                received 200 Ok response messages.  The 
                statistics are kept on per SIP method basis.
                ''',
                'csipstatssuccessoktable',
                'CISCO-SIP-UA-MIB', False),
            _MetaInfoClassMember('cSipStatsTraffic', REFERENCE_CLASS, 'CSipStatsTraffic' , 'ydk.models.sip.CISCO_SIP_UA_MIB', 'CISCOSIPUAMIB.CSipStatsTraffic', 
                [], [], 
                '''                ''',
                'csipstatstraffic',
                'CISCO-SIP-UA-MIB', False),
            ],
            'CISCO-SIP-UA-MIB',
            'CISCO-SIP-UA-MIB',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CiscoSipUaMIBNotificationPrefix_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoSipUaMIBNotificationPrefix_Identity',
            False, 
            [
            ],
            'CISCO-SIP-UA-MIB',
            'ciscoSipUaMIBNotificationPrefix',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
    'CiscoSipUaMIBNotifications_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoSipUaMIBNotifications_Identity',
            False, 
            [
            ],
            'CISCO-SIP-UA-MIB',
            'ciscoSipUaMIBNotifications',
            _yang_ns._namespaces['CISCO-SIP-UA-MIB'],
        'ydk.models.sip.CISCO_SIP_UA_MIB'
        ),
    },
}
_meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable.CSipCfgBindSourceAddrEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgCauseStatusTable.CSipCfgCauseStatusEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipCfgCauseStatusTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgEarlyMediaTable.CSipCfgEarlyMediaEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipCfgEarlyMediaTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgPeerTable.CSipCfgPeerEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipCfgPeerTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgStatusCauseTable.CSipCfgStatusCauseEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipCfgStatusCauseTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsSuccessOkTable.CSipStatsSuccessOkEntry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB.CSipStatsSuccessOkTable']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgAaa']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgBase']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgBindSourceAddrTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgCauseStatusTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgEarlyMediaTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgPeer']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgPeerTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgRetry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgStatusCauseTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgTimer']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipCfgVoiceServiceVoip']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsConnection']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsErrClient']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsErrServer']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsGlobalFail']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsInfo']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsMisc']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsRedirect']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsRetry']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsSuccess']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsSuccessOkTable']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
_meta_table['CISCOSIPUAMIB.CSipStatsTraffic']['meta_info'].parent =_meta_table['CISCOSIPUAMIB']['meta_info']
