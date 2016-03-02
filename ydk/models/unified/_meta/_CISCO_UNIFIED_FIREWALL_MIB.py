


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOUNIFIEDFIREWALLMIB.CuFwApplInspectionGrp' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CuFwApplInspectionGrp',
            False, 
            [
            _MetaInfoClassMember('cufwAIAlertEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value identifies if application inspection alerts
                have been globally enabled or disabled.
                ''',
                'cufwaialertenabled',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAIAuditTrailEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value identifies if audit trail in application 
                inspection has been globally enabled or disabled.
                ''',
                'cufwaiaudittrailenabled',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cuFwApplInspectionGrp',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionGlobals' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CuFwConnectionGlobals',
            False, 
            [
            _MetaInfoClassMember('cufwConnGlobalConnSetupRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The averaged number of connections which the firewall 
                establishing per second, averaged over the last 60 
                seconds.
                ''',
                'cufwconnglobalconnsetuprate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalConnSetupRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The averaged number of connections which the firewall 
                establishing per second, averaged over the last 300
                seconds.
                ''',
                'cufwconnglobalconnsetuprate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections which were active but
                which were aborted by the firewall due to reasons
                of policy or resource rationing.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections which are currently active.
                ''',
                'cufwconnglobalnumactive',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumAttempted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                
                Connection Statistics Aggregation
                
                Connection 1  +-----------+ 
                ------------->|           |-------> Global Connection Summary
                Connection 2  |           |
                ------------->|           |
                Connection 3  |           |
                ------------->|   First   |------------> ConnSummary 
                  |   Level   |            (i.e, L-3/4 Protocol
                Connection 4  |Aggregation|             Connection Summary)
                ------------->|           |
                .    |           |
                .    |           |---------------> PolicyConnSummary 
                Connection N  |           |       (i.e, L-3/4 Policy Target based
                ------------->|           |        Protocol Connection Summary)
                  +-----------+
                
                
                  +-----------+ 
                L-3/4 Protocol   |           |
                Connection Summary |           |
                ------------------>|           |---------> AppConnSummary 
                  |           |         (i.e, L-7 Protocol 
                  |  Second   |          Connection Summary)
                  |---Level---|
                L-3/4 Policy Target |Aggregation|
                based Protocol    |           |
                Connection Summary  |           |
                ------------------>|           |---------------> PolicyAppConnSummary
                  |           |       (i.e, L-7 Policy Target based
                  |           |        Protocol Connection Summary)
                  +-----------+
                
                
                Specifically, the object 
                'cufwConnGlobalNumAttempted' models
                the number of connections which are attempted to
                be set up through the firewall.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumattempted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumEmbryonic', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of embryonic application layer connections 
                (that is, connections in which the signaling channel
                has been established while the data channel is awaiting
                setup).
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumembryonic',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumExpired', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections which were active but
                which were since normally terminated.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumexpired',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumHalfOpen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections which are in the process
                of being setup but which have not yet reached the
                established state in the connection table.
                ''',
                'cufwconnglobalnumhalfopen',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumPolicyDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections which were attempted to
                be setup but which were declined due to reasons of
                security policy.
                
                This includes the connections that failed 
                authentication.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumpolicydeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumRemoteAccess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of active connections which correspond
                to remote access applications. Specifically, the
                protocol for which the connection is established
                must be one of PPP, PPTP, L2TP or remote access IPsec
                (IPsec connections employing extended authentication).
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumremoteaccess',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumResDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections which were attempted to
                be setup but which were declined due to 
                non-availability of required resources.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumresdeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnGlobalNumSetupsAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection setup attempts that
                were aborted before the connection could proceed
                to completion. The counter includes setup
                attempts aborted by the firewall as well as 
                those aborted by the initiator and/or the 
                responder(s) of/to the connection setup attempt.
                
                Consequently, this value subsumes the values of
                objects 'cufwConnGlobalNumPolicyDeclined' and 
                'cufwConnGlobalNumResDeclined'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnglobalnumsetupsaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cuFwConnectionGlobals',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionReportSettings' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CuFwConnectionReportSettings',
            False, 
            [
            _MetaInfoClassMember('cufwConnReptAppStats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Setting this object to 'true' enables the MIB to
                report connection activity statistics pertaining
                to application protocols.
                
                If this object is set to 'false', the agent
                should stop updating the objects defined in this
                module pertaining to application protocols.
                
                Application monitoring could be a resource intensive
                operation. It is expected that the administrators 
                would use this control to disable application 
                monitoring when the performance of the firewall is 
                degrading.
                ''',
                'cufwconnreptappstats',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnReptAppStatsLastChanged', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time at which the value of cufwConnReptAppStats 
                was last changed.
                ''',
                'cufwconnreptappstatslastchanged',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cuFwConnectionReportSettings',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionResources' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CuFwConnectionResources',
            False, 
            [
            _MetaInfoClassMember('cufwConnResActiveConnMemoryUsage', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all structures
                required to maintain the state of all active
                connections.
                ''',
                'cufwconnresactiveconnmemoryusage',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnResEmbrConnMemoryUsage', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all structures
                required to maintain the state of all embryonic
                connections.
                ''',
                'cufwconnresembrconnmemoryusage',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnResHOConnMemoryUsage', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all structures
                required to maintain the state of all half
                open connections.
                ''',
                'cufwconnreshoconnmemoryusage',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnResMemoryUsage', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all structures
                required to maintain the state of all connections
                which are either being established or are active.
                ''',
                'cufwconnresmemoryusage',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cuFwConnectionResources',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CuFwNotifCntlGrp' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CuFwNotifCntlGrp',
            False, 
            [
            _MetaInfoClassMember('cufwCntlL2StaticMacAddressMoved', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object defines the administrative state of
                sending the SNMP notification to signal the move
                of a statically configured MAC address to a new 
                port.
                
                Such a change could occur either as a result of physical
                move of the device with the MAC Address to the new port
                or due to MAC address spoofing.
                ''',
                'cufwcntll2staticmacaddressmoved',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwCntlUrlfServerStatusChange', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object defines the administrative state of
                sending the SNMP notification to signal the election
                of a new primary URL filtering server by this
                firewall.
                
                Such a change could occur either as a result of 
                the current primary server becoming unavailable or
                as a result of explicit management action in 
                nominating a filtering server the primary server.
                ''',
                'cufwcntlurlfserverstatuschange',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cuFwNotifCntlGrp',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwAaicGlobals' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwAaicGlobals',
            False, 
            [
            _MetaInfoClassMember('cufwAaicGlobalNumBadPDUSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This MIB object records the number of application 
                protocol data units (PDU) that had either an invalid
                header size or an invalid payload size, as determined 
                by the local security policy.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                application traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaicglobalnumbadpdusize',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicGlobalNumBadPortRange', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of application protocol units that attempted 
                to advertise illegal port ranges for secondary 
                connections. An example of such an occurrence
                would be a passive FTP connection, where the 
                server advertises a disallowed port range for data
                connection.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                application traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaicglobalnumbadportrange',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicGlobalNumBadProtocolOps', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                'Protocol Operation' is the application protocol
                specific operation that the PDU is intended to 
                perform. An example of 'protocol operation' is the 
                HELO command of SMTP protocol.
                
                This MIB object records the number of application 
                protocol data units that contained a protocol operation
                which was disallowed by the local security policy. 
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                application traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaicglobalnumbadprotocolops',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwAaicGlobals',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwAaicHttpProtocolStats' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwAaicHttpProtocolStats',
            False, 
            [
            _MetaInfoClassMember('cufwAaicHttpNumBadContent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                which were detected to be containing content whose
                type disallowed by the local security policy.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumbadcontent',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumBadPDUSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                that had either an invalid header size or an invalid 
                payload size, as determined by the local security
                policy.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumbadpdusize',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumBadProtocolOps', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                which were detected to be containing HTTP protocol
                methods which are disallowed by the local security 
                policy.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumbadprotocolops',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumDoubleEncodedPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                which were detected to be containing double encoding.
                Double encoding is a mechanism to obfuscate content 
                in which a encoded data is re-encoded so as to evade 
                deep packet inspections.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumdoubleencodedpkts',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumLargeURIs', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                which were detected to be containing a URI of
                size not permitted by the local security policy.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumlargeuris',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumMismatchContent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of PDUs corresponding to HTTP protocol 
                which were detected to be containing content whose
                type was different from the content type specified 
                in the header of the PDU.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnummismatchcontent',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpNumTunneledConns', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections corresponding to HTTP
                protocol which were detected to be tunneling other 
                application traffic streams. An instance of this 
                would be InstantMessenger traffic running on HTTP.
                
                For this MIB to be implemented, the managed firewall 
                must be implementing deep packet inspection of 
                HTTP traffic payloads.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwaaichttpnumtunneledconns',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwAaicHttpProtocolStats',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable.CufwAppConnSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable.CufwAppConnSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('cufwAppConnProtocol', REFERENCE_ENUM_CLASS, 'CFWApplicationProtocol_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWApplicationProtocol_Enum', 
                [], [], 
                '''                The layer7 protocol for which this conceptual 
                row summarizes the connection activity for this 
                firewall.
                ''',
                'cufwappconnprotocol',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwAppConnNumAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections that were terminated by the 
                firewall successful establishment, corresponding 
                to the protocol denoted by 'cufwAppConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwappconnnumaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently active,
                corresponding to the protocol denoted by 
                'cufwAppConnProtocol'.
                ''',
                'cufwappconnnumactive',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumAttempted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections attempted since the last
                reboot of the firewall, corresponding to the protocol
                denoted by 'cufwAppConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwappconnnumattempted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumHalfOpen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently in the
                process of being established, corresponding to the 
                protocol denoted by 'cufwAppConnProtocol'.
                ''',
                'cufwappconnnumhalfopen',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumPolicyDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to security policy, corresponding to the protocol 
                denoted by 'cufwAppConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwappconnnumpolicydeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumResDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to resource unavailability, corresponding to the 
                protocol denoted by 'cufwAppConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwappconnnumresdeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnNumSetupsAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection setup attempts,
                corresponding to the protocol denoted by 
                'cufwAppConnProtocol', that were aborted before
                the connection could proceed to completion. The 
                counter includes setup attempts aborted by the 
                firewall as well as those aborted by the initiator 
                and/or the responder(s) of/to the connection setup 
                attempt.
                
                Consequently, this value subsumes the values of
                objects 'cufwAppConnNumPolicyDeclined' and 
                'cufwAppConnNumResDeclined'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwappconnnumsetupsaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnSetupRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The connection setup rate averaged over the last
                60 seconds corresponding to the protocol denoted by 
                'cufwAppConnProtocol'.
                ''',
                'cufwappconnsetuprate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnSetupRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The connection setup rate averaged over the last
                300 seconds corresponding to the protocol denoted by 
                'cufwAppConnProtocol'.
                ''',
                'cufwappconnsetuprate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwAppConnSummaryEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable',
            False, 
            [
            _MetaInfoClassMember('cufwAppConnSummaryEntry', REFERENCE_LIST, 'CufwAppConnSummaryEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable.CufwAppConnSummaryEntry', 
                [], [], 
                '''                Each entry contains the summary of connection
                activity for a distinct layer 7 protocol identified
                by the index element 'cufwAppConnProtocol'.
                ''',
                'cufwappconnsummaryentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwAppConnSummaryTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable.CufwConnSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable.CufwConnSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('cufwConnProtocol', REFERENCE_ENUM_CLASS, 'CFWNetworkProtocol_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWNetworkProtocol_Enum', 
                [], [], 
                '''                The (L3-L4) protocol for which this conceptual 
                row summarizes the connection activity on the
                managed entity.
                ''',
                'cufwconnprotocol',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwConnNumAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections that were abnormally 
                terminated after successful establishment, 
                corresponding to the protocol denoted by 
                'cufwConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnnumaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently active,
                corresponding to the protocol denoted by 
                'cufwConnProtocol'.
                ''',
                'cufwconnnumactive',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumAttempted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections attempted since the last
                reboot of the firewall, corresponding to the protocol
                denoted by 'cufwConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnnumattempted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumHalfOpen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently in the
                process of being established, corresponding to the 
                protocol denoted by 'cufwConnProtocol'.
                ''',
                'cufwconnnumhalfopen',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumPolicyDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to security policy, corresponding to the protocol 
                denoted by 'cufwConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnnumpolicydeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumResDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to resource unavailability, corresponding to the 
                protocol denoted by 'cufwConnProtocol'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnnumresdeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnNumSetupsAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection setup attempts,
                corresponding to the protocol denoted by 
                'cufwConnProtocol', that were aborted before the 
                connection could proceed to completion. The 
                counter includes setup attempts aborted by the 
                firewall as well as those aborted by the initiator 
                and/or the responder(s) of/to the connection setup 
                attempt.
                
                Consequently, this value subsumes the values of
                objects 'cufwConnNumPolicyDeclined' and 
                'cufwConnNumResDeclined'.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwconnnumsetupsaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnSetupRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The connection setup rate averaged over the last
                60 seconds corresponding to the protocol denoted by 
                'cufwConnProtocol'.
                ''',
                'cufwconnsetuprate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnSetupRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The connection setup rate averaged over the last
                300 seconds corresponding to the protocol denoted by 
                'cufwConnProtocol'.
                ''',
                'cufwconnsetuprate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwConnSummaryEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable',
            False, 
            [
            _MetaInfoClassMember('cufwConnSummaryEntry', REFERENCE_LIST, 'CufwConnSummaryEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable.CufwConnSummaryEntry', 
                [], [], 
                '''                Each entry contains the summary of connection
                activity for a layer3-layer4 network protocol.
                ''',
                'cufwconnsummaryentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwConnSummaryTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable.CufwInspectionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable.CufwInspectionEntry',
            False, 
            [
            _MetaInfoClassMember('cufwInspectionPolicyName', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The name of the policy that configures the device
                inspect the protocol specified by 
                  'cufwInspectionProtocol'.
                ''',
                'cufwinspectionpolicyname',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwInspectionProtocol', REFERENCE_ENUM_CLASS, 'CFWApplicationProtocol_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWApplicationProtocol_Enum', 
                [], [], 
                '''                The application protocol that is configured for 
                inspection.
                ''',
                'cufwinspectionprotocol',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwInspectionStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This MIB object identifies if the directive to inspect
                the protocol specified by 'cufwInspectionProtocol' by
                the policy corresponding to this conceptual row is
                enabled or disabled.
                ''',
                'cufwinspectionstatus',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwInspectionEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable',
            False, 
            [
            _MetaInfoClassMember('cufwInspectionEntry', REFERENCE_LIST, 'CufwInspectionEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable.CufwInspectionEntry', 
                [], [], 
                '''                Each entry contains the configuration of
                a specific application inspection element.
                ''',
                'cufwinspectionentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwInspectionTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwL2FwGlobals' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwL2FwGlobals',
            False, 
            [
            _MetaInfoClassMember('cufwL2GlobalArpCacheSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The value indicates the configured maximum size of
                the ARP cache used for management traffic.
                ''',
                'cufwl2globalarpcachesize',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalArpOverflowRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an existing entry from the ARP
                cache had to be ejected in order to insert a new entry
                in the last 300 seconds.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalarpoverflowrate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalEnableArpInspection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value indicates if ARP inspection, which is a
                security feature, is enabled globally on the
                managed firewall.
                ''',
                'cufwl2globalenablearpinspection',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalEnableStealthMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value indicates if the firewall is operating
                in transparent (layer 2) mode or not.
                
                When operating in transparent mode, the firewall
                operates as a bridge while performing firewalling
                functions.
                ''',
                'cufwl2globalenablestealthmode',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumArpRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of ARP requests issued by the transparent
                firewall to resolve a destination IP address.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumarprequests',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumBadArpResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of malformed ARP responses received by the
                firewall in trying to resolve the MAC address of the
                destination IP address in an incoming frame.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumbadarpresponses',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of times the firewall dropped an incoming
                frame because the destination MAC address is missing 
                in the bridge table.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumdrops',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumFloods', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of times the firewall floods a frame to be 
                forwarded to the egress interfaces because the 
                destination MAC address is missing in the bridge table.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumfloods',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumIcmpRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of ICMP traceroute requests issued by the 
                transparent firewall to resolve a destination IP 
                address.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumicmprequests',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2GlobalNumSpoofedArpResps', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of spoofed ARP responses received by the
                firewall. Such an event would occur when the firewall
                encounters an ARP response mapping an IP address to
                a different MAC Address from the one present in the
                local ARP cache.
                
                This counter is accumulated since the last reboot of 
                the firewall.
                ''',
                'cufwl2globalnumspoofedarpresps',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwL2FwGlobals',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable.CufwPolicyAppConnSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable.CufwPolicyAppConnSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('cufwPolAppConnPolicy', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The identity of the firewall policy for which
                this conceptual row contains the connection 
                activity summary.
                ''',
                'cufwpolappconnpolicy',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolAppConnPolicyTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The identity of the entity to which the firewall 
                policy 'cufwPolAppProtocol' refers. This could be an 
                interface object (most commonly), another object or
                group of objects defined in the firewall configuration.
                ''',
                'cufwpolappconnpolicytarget',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolAppConnPolicyTargetType', REFERENCE_ENUM_CLASS, 'CFWPolicyTargetType_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWPolicyTargetType_Enum', 
                [], [], 
                '''                The type of the entity to which the firewall policy
                'cufwPolAppConnPolicy' has been applied. This could be
                an interface type (most commonly), the type of another
                object or a group of objects defined in the firewall
                configuration.
                
                When this object is set to 'targetALL', the value of
                index object cufwAppConnPolicyTarget is ignored.
                ''',
                'cufwpolappconnpolicytargettype',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolAppConnProtocol', REFERENCE_ENUM_CLASS, 'CFWApplicationProtocol_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWApplicationProtocol_Enum', 
                [], [], 
                '''                The layer7 protocol for which this conceptual 
                row summarizes the connection activity for this 
                firewall.
                ''',
                'cufwpolappconnprotocol',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolAppConnNumAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections that were abnormally 
                terminated after successful establishment, corresponding
                to the protocol denoted by 'cufwPolAppConnProtocol', in
                the policy 'cufwPolAppConnPolicy' applied to the entity
                identified by 'cufwPolAppConnPolicyTarget'.
                ''',
                'cufwpolappconnnumaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently active,
                corresponding to the protocol denoted by 
                'cufwPolAppConnProtocol', in the policy 
                'cufwPolAppConnPolicy' applied to the entity identified
                by 'cufwPolAppConnPolicyTarget'.
                ''',
                'cufwpolappconnnumactive',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumAttempted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections attempted since the last
                reboot of the firewall, corresponding to the protocol
                denoted by 'cufwPolAppConnProtocol', in the policy 
                'cufwPolAppConnPolicy' applied to the entity identified
                by 'cufwPolAppConnPolicyTarget'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwpolappconnnumattempted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumHalfOpen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently in the
                process of being established, corresponding to the 
                protocol
                denoted by 'cufwPolAppConnProtocol', in the policy 
                'cufwPolAppConnPolicy' applied to the entity identified
                by 'cufwPolAppConnPolicyTarget'.
                ''',
                'cufwpolappconnnumhalfopen',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumPolicyDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to security policy, corresponding to the protocol 
                denoted by 'cufwPolAppConnProtocol', in the policy 
                'cufwPolAppConnPolicy' applied to the entity identified
                by 'cufwPolAppConnPolicyTarget'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwpolappconnnumpolicydeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumResDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to resource unavailability, corresponding to the 
                protocol denoted by 'cufwPolAppConnProtocol', in the
                policy 'cufwPolAppConnPolicy' applied to the entity
                identified by 'cufwPolAppConnPolicyTarget'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwpolappconnnumresdeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolAppConnNumSetupsAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection setup attempts,
                corresponding to the protocol denoted by 
                'cufwPolAppConnProtocol', associated with the policy
                'cufwPolAppConnPolicy' applied to the entity 
                identified by 'cufwPolAppConnPolicyTarget',
                that were aborted before the connections could 
                proceed to completion. The counter includes setup 
                attempts aborted by the firewall as well as those 
                aborted by the initiator and/or the responder(s) 
                of/to the connection setup attempt.
                
                Consequently, this value subsumes the values of
                objects 'cufwPolAppConnNumPolicyDeclined' and 
                'cufwPolAppConnNumResDeclined'.
                
                This value is accumulated from the last reboot of
                the firewall subject to the control exercised by
                cufwConnReptAppStats.
                ''',
                'cufwpolappconnnumsetupsaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwPolicyAppConnSummaryEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable',
            False, 
            [
            _MetaInfoClassMember('cufwPolicyAppConnSummaryEntry', REFERENCE_LIST, 'CufwPolicyAppConnSummaryEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable.CufwPolicyAppConnSummaryEntry', 
                [], [], 
                '''                Each entry contains the summary of connection
                activity for a specific layer 7 protocol in a
                specific policy applied to the specified policy 
                target.
                ''',
                'cufwpolicyappconnsummaryentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwPolicyAppConnSummaryTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable.CufwPolicyConnSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable.CufwPolicyConnSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('cufwPolConnPolicy', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The identity of the firewall policy for which
                this conceptual row contains the connection 
                activity summary.
                ''',
                'cufwpolconnpolicy',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolConnPolicyTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The identity of the entity to which the firewall 
                policy 'cufwPolConnPolicy' is applied. This could be an
                interface object (most commonly), another object or
                group of objects defined in the firewall configuration.
                ''',
                'cufwpolconnpolicytarget',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolConnPolicyTargetType', REFERENCE_ENUM_CLASS, 'CFWPolicyTargetType_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWPolicyTargetType_Enum', 
                [], [], 
                '''                The type of the entity to which the firewall policy
                'cufwPolConnPolicy' has been applied. This could be
                an interface type (most commonly), the type of another
                object or a group of objects defined in the firewall
                configuration.
                
                When this object is set to 'targetALL', the value of
                index object cufwConnPolicyTarget is ignored.
                ''',
                'cufwpolconnpolicytargettype',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolConnProtocol', REFERENCE_ENUM_CLASS, 'CFWNetworkProtocol_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWNetworkProtocol_Enum', 
                [], [], 
                '''                The (L3-L4) protocol corresponding to which this 
                conceptual row summarizes the connection activity
                on the firewall.
                ''',
                'cufwpolconnprotocol',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwPolConnNumAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections that were abnormally 
                terminated after successful establishment, corresponding
                to the protocol denoted by 'cufwPolConnProtocol', 
                in the policy 'cufwPolConnPolicy' applied to the entity
                identified by 'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently active,
                corresponding to the protocol denoted by 
                'cufwPolConnProtocol', in the policy 
                'cufwPolConnPolicy' applied to the entity identified
                by 'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumactive',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumAttempted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connections attempted since the last
                reboot of the firewall, corresponding to the protocol
                denoted by 'cufwPolConnProtocol', in the policy 
                'cufwPolConnPolicy' applied to the entity identified
                by 'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumattempted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumHalfOpen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of connections that are currently in the
                process of being established, corresponding to the 
                protocol denoted by 'cufwPolConnProtocol', in the 
                policy 'cufwPolConnPolicy' applied to the entity
                identified by 'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumhalfopen',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumPolicyDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to security policy, corresponding to the protocol 
                denoted by 'cufwPolConnProtocol', in the policy 
                'cufwPolConnPolicy' applied to the entity identified by
                'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumpolicydeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumResDeclined', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection attempts that were declined
                due to resource unavailability, corresponding to the 
                protocol denoted by 'cufwPolConnProtocol', in the policy
                'cufwPolConnPolicy' applied to the entity identified by
                'cufwPolConnPolicyTarget'.
                ''',
                'cufwpolconnnumresdeclined',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolConnNumSetupsAborted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of connection setup attempts,
                corresponding to the protocol denoted by 
                'cufwPolConnProtocol', associated with the policy 
                'cufwPolConnPolicy' applied to the entity
                identified by 'cufwPolConnPolicyTarget',
                that were aborted before the connection could 
                proceed to completion. The counter includes 
                setup attempts aborted by the firewall as well 
                as those aborted by the initiator and/or the 
                responder(s) of/to the connection setup attempt.
                
                Consequently, this value subsumes the values of
                objects 'cufwPolConnNumPolicyDeclined' and
                'cufwPolConnNumResDeclined'.
                ''',
                'cufwpolconnnumsetupsaborted',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwPolicyConnSummaryEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable',
            False, 
            [
            _MetaInfoClassMember('cufwPolicyConnSummaryEntry', REFERENCE_LIST, 'CufwPolicyConnSummaryEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable.CufwPolicyConnSummaryEntry', 
                [], [], 
                '''                Each entry contains the summary of connection
                activity for a specific protocol in a specific
                policy applied to the specified policy target.
                ''',
                'cufwpolicyconnsummaryentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwPolicyConnSummaryTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterGlobals' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterGlobals',
            False, 
            [
            _MetaInfoClassMember('cufwUrlfAllowModeReqNumAllowed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests that were allowed
                by the firewall when the URL filtering server was not
                available.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfallowmodereqnumallowed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfAllowModeReqNumDenied', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests that were declined
                by the firewall when the URL filtering server was not
                available.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfallowmodereqnumdenied',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfFunctionEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                
                URL Filtering Operation
                
                                                _________
                                 2.2 Request   |         |
                                   |---------->| Server  |
                                   |           |         |
                _________                      __|_          |_________|
                |         |<--(5. Response )---|    | 3. Response  |  
                |         |                    |    |<-------------| 
                | Client  |---(1. Request )--->|FW  |
                |_________|                    |____|<--------------|
                                  | 4. URLF Resp ____|______
                                  |             |           |
                                  |------------>|URLF Server|
                                 2.1 URLF Req   |___________|
                
                1)  Client sends a Request containing a URL to the Server
                
                2.1)  FW extracts the URL from the Request and sends it to 
                URL Filtering Server (or Verifies the URL locally)
                
                2.2)  FW also forwards the original Request from the Client to 
                the Server
                
                3)  Any Responses from the Server received before receiving
                a response from URLF Server are cached by the FW
                
                4)  URLF Response indicates whether the URL access should be 
                allowed or denied
                
                5)  If the URLF Response allows the URL, FW forwards the
                URL Access responses from the Server to the Client
                
                6)  If the URLF Response indicates that the URL access should be
                denied, FW drops all the cached URL responses and forces the
                connection between the Client and the Server to be terminated
                
                Specifically, the object cufwUrlfFunctionEnabled 
                indicates if the URL filtering function
                is enabled.
                
                When this MIB object contains the value 'false',
                the firewall device will not perform URL filtering
                function, even if it contains configuration pertaining
                to other aspects of URL filtering.
                ''',
                'cufwurlffunctionenabled',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfNumServerRetries', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access authorization requests 
                re-sent by the firewall to the URL Filtering Servers 
                because a response was not received within the 
                configured time interval.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfnumserverretries',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfNumServerTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of times the firewall failed to receive
                a response from the configured URL filtering servers 
                for a request to authorize a URL access request.
                
                This is equal to the number of times a firewall removed
                a URL access request from the queue of pending requests
                because no response was received from the URL filtering
                server(s).
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfnumservertimeouts',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsDeniedRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The rate at which URL access requests were denied
                by this firewall, due to a directive from a URL 
                filtering server, a static policy configured on 
                the firewall, due to resource constraints or
                any other reason, averaged over the last 60 seconds.
                ''',
                'cufwurlfrequestsdeniedrate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsDeniedRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The rate at which URL access requests were denied
                by this firewall, due to a directive from a URL 
                filtering server, a static policy configured on 
                the firewall, due to resource constraints or
                any other reason, averaged over the last 300 seconds.
                ''',
                'cufwurlfrequestsdeniedrate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumAllowed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests allowed by
                this firewall, due to a directive from a URL 
                filtering server or a static policy configured on 
                the firewall.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfrequestsnumallowed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumCacheAllowed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests allowed by
                the firewall because of a cached entry holding the
                result from a previous URL access request that was
                handled either by a URLF Server or exclusive domain
                configuration. 
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfrequestsnumcacheallowed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumCacheDenied', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests denied by
                the firewall because of a cached entry holding the
                result from a previous URL access request that was
                handled either by a URLF Server or exclusive domain
                configuration. 
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfrequestsnumcachedenied',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumDenied', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests declined by
                this firewall, due to a directive from a URL 
                filtering server, a static policy configured on 
                the firewall, due to resource constraints or
                any other reason.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwurlfrequestsnumdenied',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumProcessed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests processed by 
                this firewall.
                
                This value is accumulated from the last reboot of
                the firewall.
                ''',
                'cufwurlfrequestsnumprocessed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsNumResDropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of incoming URL access requests that
                were dropped by the firewall because of resource
                constraints.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfrequestsnumresdropped',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsProcRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of URL access requests processed per 
                seconds by this firewall averaged over the last 60 
                seconds.
                ''',
                'cufwurlfrequestsprocrate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsProcRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of URL access requests processed per second
                by this firewall averaged over the last 300 seconds.
                ''',
                'cufwurlfrequestsprocrate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsResDropRate1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The rate at which incoming URL access requests 
                were dropped by the firewall because of resource
                constraints, averaged over the last 60 seconds.
                ''',
                'cufwurlfrequestsresdroprate1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfRequestsResDropRate5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The rate at which incoming URL access requests 
                were dropped by the firewall because of resource
                constraints, averaged over the last 300 seconds.
                ''',
                'cufwurlfrequestsresdroprate5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfResponsesNumLate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of responses from URL filtering servers
                which were received after the original URL access
                request was removed from the queue of pending
                requests.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfresponsesnumlate',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfUrlAccRespsNumResDropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of transport packets constituting responses
                to URL access requests that were dropped by the firewall
                due to resource constraints waiting for a response from
                the filtering server.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfurlaccrespsnumresdropped',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwUrlFilterGlobals',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterResourceUsage' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterResourceUsage',
            False, 
            [
            _MetaInfoClassMember('cufwUrlfResTotalRequestCacheSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all the caches
                used in the firewall to cache pending URL access
                requests.
                ''',
                'cufwurlfrestotalrequestcachesize',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfResTotalRespCacheSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of memory occupied by all the caches
                used in the firewall to cache responses for URL 
                requests received from servers while awaiting a
                response from URL filter server.
                ''',
                'cufwurlfrestotalrespcachesize',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwUrlFilterResourceUsage',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable.CufwUrlfServerEntry' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable.CufwUrlfServerEntry',
            False, 
            [
            _MetaInfoClassMember('cufwUrlfServerAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of the IP address of the URL filtering
                server.
                ''',
                'cufwurlfserveraddress',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwUrlfServerAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of the IP address of the URL filtering
                server.
                ''',
                'cufwurlfserveraddrtype',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwUrlfServerPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The value of the port at which the URL filtering
                server listens for incoming requests.
                ''',
                'cufwurlfserverport',
                'CISCO-UNIFIED-FIREWALL-MIB', True),
            _MetaInfoClassMember('cufwUrlfServerAvgRespTime1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The average round-trip response time of the
                URL filtering server computed over the last
                60 seconds.
                
                A value of zero indicates that there was 
                insufficient data to compute this value over the 
                last time interval.
                ''',
                'cufwurlfserveravgresptime1',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerAvgRespTime5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The average round-trip response time of the
                URL filtering server computed over the last
                300 seconds.
                
                A value of zero indicates that there was 
                insufficient data to compute this value over the 
                last time interval.
                ''',
                'cufwurlfserveravgresptime5',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerNumRetries', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access authorization requests 
                re-sent by the firewall to the URL Filtering Server 
                corresponding to this conceptual row, because a response
                was not received within the configured time interval
                from the server.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfservernumretries',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerNumTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of times the firewall failed to receive
                a response from the URL filtering server corresponding 
                to this conceptual row, for a request to authorize a 
                URL access request.
                
                This is equal to the number of times a firewall removed
                a URL access request from the queue of pending requests
                because no response was received from the URL filtering
                server.
                
                This value is accumulated from the last reboot of the
                firewall.
                ''',
                'cufwurlfservernumtimeouts',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerReqsNumAllowed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests allowed by the
                URL filtering server corresponding to this conceptual 
                row. This counter does not include late responses.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfserverreqsnumallowed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerReqsNumDenied', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests denied by the
                URL filtering server corresponding to this conceptual 
                row. This counter does not include late responses.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfserverreqsnumdenied',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerReqsNumProcessed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access requests forwarded by
                the managed firewall device to the URL filtering
                server corresponding to this conceptual row.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfserverreqsnumprocessed',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerRespsNumLate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access responses received by
                the managed firewall from the URL filtering server 
                corresponding to this conceptual row after the 
                original URL access request was removed from the 
                queue of pending requests.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfserverrespsnumlate',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerRespsNumReceived', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of URL access responses received by the
                firewall from the URL filtering server corresponding 
                to this conceptual row. This counter does not include 
                late responses.
                
                This value is counted from the last reboot of
                the managed device.
                ''',
                'cufwurlfserverrespsnumreceived',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerStatus', REFERENCE_ENUM_CLASS, 'CFWUrlServerStatus_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWUrlServerStatus_Enum', 
                [], [], 
                '''                The status of the URL filtering server
                corresponding to this conceptual row.
                ''',
                'cufwurlfserverstatus',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerVendor', REFERENCE_ENUM_CLASS, 'CFWUrlfVendorId_Enum' , 'ydk.models.firewall.CISCO_FIREWALL_TC', 'CFWUrlfVendorId_Enum', 
                [], [], 
                '''                The vendor type of the URL filtering server.
                ''',
                'cufwurlfservervendor',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwUrlfServerEntry',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable',
            False, 
            [
            _MetaInfoClassMember('cufwUrlfServerEntry', REFERENCE_LIST, 'CufwUrlfServerEntry' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable.CufwUrlfServerEntry', 
                [], [], 
                '''                Each entry contains the configuration of
                a specific URL filtering server.
                ''',
                'cufwurlfserverentry',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'cufwUrlfServerTable',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
    'CISCOUNIFIEDFIREWALLMIB' : {
        'meta_info' : _MetaInfoClass('CISCOUNIFIEDFIREWALLMIB',
            False, 
            [
            _MetaInfoClassMember('cufwAaicGlobals', REFERENCE_CLASS, 'CufwAaicGlobals' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwAaicGlobals', 
                [], [], 
                '''                ''',
                'cufwaaicglobals',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAaicHttpProtocolStats', REFERENCE_CLASS, 'CufwAaicHttpProtocolStats' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwAaicHttpProtocolStats', 
                [], [], 
                '''                ''',
                'cufwaaichttpprotocolstats',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwAppConnSummaryTable', REFERENCE_CLASS, 'CufwAppConnSummaryTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable', 
                [], [], 
                '''                This table lists the summary of firewall 
                connections pertaining to Layer 7 protocols,
                catalogued by distinct application protocols.
                
                Each entry in the table lists the connection
                summary corresponding to a distinct application 
                protocol.
                
                For instance, to obtain the connection summary 
                for SMTP on the firewall since the last reboot 
                of the device, use the conceptual row 
                corresponding to 
                
                   cufwAppConnProtocol = fwApSmtp
                ''',
                'cufwappconnsummarytable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cuFwApplInspectionGrp', REFERENCE_CLASS, 'CuFwApplInspectionGrp' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CuFwApplInspectionGrp', 
                [], [], 
                '''                ''',
                'cufwapplinspectiongrp',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cuFwConnectionGlobals', REFERENCE_CLASS, 'CuFwConnectionGlobals' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionGlobals', 
                [], [], 
                '''                ''',
                'cufwconnectionglobals',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cuFwConnectionReportSettings', REFERENCE_CLASS, 'CuFwConnectionReportSettings' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionReportSettings', 
                [], [], 
                '''                ''',
                'cufwconnectionreportsettings',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cuFwConnectionResources', REFERENCE_CLASS, 'CuFwConnectionResources' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CuFwConnectionResources', 
                [], [], 
                '''                ''',
                'cufwconnectionresources',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwConnSummaryTable', REFERENCE_CLASS, 'CufwConnSummaryTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable', 
                [], [], 
                '''                This table summarizes the connection activity on
                the firewall per layer3-layer 4 protocol instance.
                
                Each entry in the table lists the connection
                summary of a distinct network protocol.
                
                For instance, the conceptual row corresponding to the
                index
                
                     cufwConnProtocol = fwpTcp
                
                yields the summary of TCP connection activity on the 
                firewall since its reboot.
                ''',
                'cufwconnsummarytable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwInspectionTable', REFERENCE_CLASS, 'CufwInspectionTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable', 
                [], [], 
                '''                This table identifies if an application protocol has
                been configured for inspection and if so, the name of 
                the firewall policy or the inspection configuration
                that configures the specified protocol for inspection.
                The table also identifies if the specified protocol is
                actively being inspected.
                
                This table may be used by an administrator to quickly
                identify if a protocol is being subjected to application
                inspection by the managed firewall.
                ''',
                'cufwinspectiontable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwL2FwGlobals', REFERENCE_CLASS, 'CufwL2FwGlobals' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwL2FwGlobals', 
                [], [], 
                '''                ''',
                'cufwl2fwglobals',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cuFwNotifCntlGrp', REFERENCE_CLASS, 'CuFwNotifCntlGrp' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CuFwNotifCntlGrp', 
                [], [], 
                '''                ''',
                'cufwnotifcntlgrp',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolicyAppConnSummaryTable', REFERENCE_CLASS, 'CufwPolicyAppConnSummaryTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable', 
                [], [], 
                '''                This table lists the summary of firewall 
                connections pertaining to Layer 7 protocols,
                catalogued on a per policy basis
                
                Each entry in the table lists the connection
                summary of a distinct application protocol, 
                configured on the specified policy on the firewall, 
                and pertaining to a specified target to which the
                policy has been applied.
                
                If a policy is bound to a target, it would have one
                or more entries in this table. If the policy is
                detached from the target, all entries corresponding
                to the association between the policy and the target
                are elminated from this table.
                
                Although the information is indexed by policy targets
                as well, one may aggregate the connection summary for
                a specific policy across all the target to which the
                policy is currently applied by setting
                
                      cufwAppConnPolicyTargetType = 'targetALL'
                ''',
                'cufwpolicyappconnsummarytable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwPolicyConnSummaryTable', REFERENCE_CLASS, 'CufwPolicyConnSummaryTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable', 
                [], [], 
                '''                This table lists the summary of firewall 
                connections for layer3-layer 4 protocols catalogued 
                on a per policy basis.
                
                Each entry in the table lists the connection summary of
                a distinct network protocol, configured on the specified
                policy on the firewall, and pertaining to a specified 
                target to which the policy is currently applied. 
                
                If a policy is bound to a target, it would have one
                or more entries in this table. If the policy is 
                detached from the target, all entries corresponding 
                to the association between the policy and the target 
                are elminated from this table.
                
                Although the information is indexed by policy targets
                as well, one may aggregate the connection summary for
                a specific policy across all the target to which the 
                policy is currently applied by setting
                
                      cufwConnPolicyTargetType =  'targetAll'
                ''',
                'cufwpolicyconnsummarytable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlFilterGlobals', REFERENCE_CLASS, 'CufwUrlFilterGlobals' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterGlobals', 
                [], [], 
                '''                ''',
                'cufwurlfilterglobals',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlFilterResourceUsage', REFERENCE_CLASS, 'CufwUrlFilterResourceUsage' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterResourceUsage', 
                [], [], 
                '''                ''',
                'cufwurlfilterresourceusage',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            _MetaInfoClassMember('cufwUrlfServerTable', REFERENCE_CLASS, 'CufwUrlfServerTable' , 'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB', 'CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable', 
                [], [], 
                '''                This table lists the URL filtering servers
                configured on the managed device and their
                performance statistics.
                
                This table is not meant as a device to 
                configure URL filtering servers.
                ''',
                'cufwurlfservertable',
                'CISCO-UNIFIED-FIREWALL-MIB', False),
            ],
            'CISCO-UNIFIED-FIREWALL-MIB',
            'CISCO-UNIFIED-FIREWALL-MIB',
            _yang_ns._namespaces['CISCO-UNIFIED-FIREWALL-MIB'],
        'ydk.models.unified.CISCO_UNIFIED_FIREWALL_MIB'
        ),
    },
}
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable.CufwAppConnSummaryEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable.CufwConnSummaryEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable.CufwInspectionEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable.CufwPolicyAppConnSummaryEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable.CufwPolicyConnSummaryEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable.CufwUrlfServerEntry']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CuFwApplInspectionGrp']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CuFwConnectionGlobals']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CuFwConnectionReportSettings']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CuFwConnectionResources']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CuFwNotifCntlGrp']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwAaicGlobals']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwAaicHttpProtocolStats']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwAppConnSummaryTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwConnSummaryTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwInspectionTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwL2FwGlobals']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyAppConnSummaryTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwPolicyConnSummaryTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterGlobals']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwUrlFilterResourceUsage']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
_meta_table['CISCOUNIFIEDFIREWALLMIB.CufwUrlfServerTable']['meta_info'].parent =_meta_table['CISCOUNIFIEDFIREWALLMIB']['meta_info']
