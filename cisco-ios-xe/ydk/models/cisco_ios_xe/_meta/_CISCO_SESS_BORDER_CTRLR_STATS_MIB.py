


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscosbcsipmethodEnum' : _MetaInfoEnum('CiscosbcsipmethodEnum', 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB',
        {
            'unknown':'unknown',
            'ack':'ack',
            'bye':'bye',
            'cancel':'cancel',
            'info':'info',
            'invite':'invite',
            'message':'message',
            'notify':'notify',
            'options':'options',
            'prack':'prack',
            'refer':'refer',
            'register':'register',
            'subscribe':'subscribe',
            'update':'update',
        }, 'CISCO-SESS-BORDER-CTRLR-STATS-MIB', _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB']),
    'CiscosbcradiusclienttypeEnum' : _MetaInfoEnum('CiscosbcradiusclienttypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB',
        {
            'authentication':'authentication',
            'accounting':'accounting',
        }, 'CISCO-SESS-BORDER-CTRLR-STATS-MIB', _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB']),
    'CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbRadiusStatsEntIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the index of the RADIUS client entity
                that this server is configured on. This index is assigned 
                arbitrarily by the engine and is not saved over reboots.
                ''',
                'csbradiusstatsentindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbRadiusStatsAcsAccpts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Access-Accept
                packets (valid or invalid) received from this server.
                ''',
                'csbradiusstatsacsaccpts',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsAcsChalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Access-Challenge
                packets (valid or invalid) received from this server.
                ''',
                'csbradiusstatsacschalls',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsAcsRejects', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Access-Reject
                packets (valid or invalid) received from this server.
                ''',
                'csbradiusstatsacsrejects',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsAcsReqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Access-Request
                packets sent to this server.  This does not include
                retransmissions.
                ''',
                'csbradiusstatsacsreqs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsAcsRtrns', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Access-Request
                packets retransmitted to this RADIUS server.
                ''',
                'csbradiusstatsacsrtrns',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsActReqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Accounting-Request
                packets sent to this server. This does not include
                retransmissions.
                ''',
                'csbradiusstatsactreqs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsActRetrans', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Accounting-Request
                packets retransmitted to this RADIUS server.
                ''',
                'csbradiusstatsactretrans',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsActRsps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS Accounting-Response
                packets (valid or invalid) received from this server.
                ''',
                'csbradiusstatsactrsps',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsBadAuths', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS response packets
                containing invalid authenticators or Signature attributes
                received from this server.
                ''',
                'csbradiusstatsbadauths',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsClientName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the client name of the RADIUS client to
                which that these statistics apply.
                ''',
                'csbradiusstatsclientname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsClientType', REFERENCE_ENUM_CLASS, 'CiscosbcradiusclienttypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscosbcradiusclienttypeEnum', 
                [], [], 
                '''                This object indicates the type(authentication or accounting)
                of the RADIUS clients configured on SBC.
                ''',
                'csbradiusstatsclienttype',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS packets which were
                received from this server and dropped for some other reason.
                ''',
                'csbradiusstatsdropped',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsMalformedRsps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of malformed RADIUS response
                packets received from this server.  Malformed packets include
                packets with an invalid length. Bad authenticators, Signature
                attributes and unknown types are not included as malformed
                access responses.
                ''',
                'csbradiusstatsmalformedrsps',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsPending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS request packets
                destined for this server that have not yet timed out or received
                a response. This variable is incremented when a request is sent
                and decremented on receipt of the response or on a timeout or
                retransmission.
                ''',
                'csbradiusstatspending',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsSrvrName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the server name of the RADIUS server to
                which that these statistics apply.
                ''',
                'csbradiusstatssrvrname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS request timeouts to
                this server.  After a timeout the client may retry to a
                different server or give up. A retry to a different server is
                counted as a request as well as a timeout.
                ''',
                'csbradiusstatstimeouts',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRadiusStatsUnknownType', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RADIUS packets of unknown
                type which were received from this server.
                ''',
                'csbradiusstatsunknowntype',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbRadiusStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable',
            False, 
            [
            _MetaInfoClassMember('csbRadiusStatsEntry', REFERENCE_LIST, 'Csbradiusstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry', 
                [], [], 
                '''                A conceptual row in the csbRadiusStatsTable. There is an
                entry in this table for each RADIUS server, as identified by a 
                value of csbRadiusStatsEntIndex. The other indices of this 
                table are csbCallStatsInstanceIndex defined in 
                csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
                in csbCallStatsTable.
                ''',
                'csbradiusstatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbRadiusStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbRfBillRealmStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '31')], [], 
                '''                This object indicates the billing method instance index. The
                range of valid values for this field is 0 - 31.
                ''',
                'csbrfbillrealmstatsindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbRfBillRealmStatsRealmName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the realm for which these statistics are
                collected. The length of this object is zero when value is not
                assigned to it.
                ''',
                'csbrfbillrealmstatsrealmname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbRfBillRealmStatsFailEventAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of failed Event ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatsfaileventacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsFailInterimAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of failed Interim ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatsfailinterimacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsFailStartAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of failed Start ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatsfailstartacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsFailStopAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of failed Stop ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatsfailstopacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsSuccEventAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of successful Event ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatssucceventacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsSuccInterimAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of successful Interim
                ACRs since start of day or the last time the statistics were
                reset.
                ''',
                'csbrfbillrealmstatssuccinterimacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsSuccStartAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of successful Start ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatssuccstartacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsSuccStopAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of successful Stop ACRs
                since start of day or the last time the statistics were reset.
                ''',
                'csbrfbillrealmstatssuccstopacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsTotalEventAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the combined sum of successful and failed
                Event ACRs since start of day or the last time the statistics
                were reset.
                ''',
                'csbrfbillrealmstatstotaleventacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsTotalInterimAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the combined sum of successful and failed
                Interim ACRs since start of day or the last time the statistics
                were reset.
                ''',
                'csbrfbillrealmstatstotalinterimacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsTotalStartAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the combined sum of successful and failed
                Start ACRs since start of day or the last time the statistics
                were reset.
                ''',
                'csbrfbillrealmstatstotalstartacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsTotalStopAcrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the combined sum of successful and failed
                Stop ACRs since start of day or the last time the statistics
                were reset.
                ''',
                'csbrfbillrealmstatstotalstopacrs',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbRfBillRealmStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable',
            False, 
            [
            _MetaInfoClassMember('csbRfBillRealmStatsEntry', REFERENCE_LIST, 'Csbrfbillrealmstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry', 
                [], [], 
                '''                A conceptual row in the csbRfBillRealmStatsTable. There
                is an entry in this table for each realm, as identified by a 
                value of csbRfBillRealmStatsIndex and 
                csbRfBillRealmStatsRealmName. The other indices of this
                table are csbCallStatsInstanceIndex defined in
                csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
                in csbCallStatsTable.
                ''',
                'csbrfbillrealmstatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbRfBillRealmStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsAdjName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the name of the SIP adjacency for which
                stats related with SIP request and all kind of corresponding SIP
                responses are reported. The object acts as an index of the
                table.
                ''',
                'csbsipmthdcurrentstatsadjname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsMethod', REFERENCE_ENUM_CLASS, 'CiscosbcsipmethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscosbcsipmethodEnum', 
                [], [], 
                '''                This object indicates the SIP method Request. The object acts
                as an index of the table.
                ''',
                'csbsipmthdcurrentstatsmethod',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object indicates the interval for which the periodic
                statistics information is to be displayed. The interval
                values can be 5 minutes, 15 minutes, 1 hour , 1 Day. This 
                object acts as an index for the table.
                ''',
                'csbsipmthdcurrentstatsinterval',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsMethodName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the text representation of the SIP
                method request. E.g. INVITE, ACK, BYE etc.
                ''',
                'csbsipmthdcurrentstatsmethodname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsReqIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total incoming SIP message requests
                of this type on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsreqin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsReqOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total outgoing SIP message requests
                of this type on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsreqout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp1xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 1xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp1xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp1xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 1xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp1xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp2xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 2xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp2xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp2xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 2xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp2xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp3xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 3xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp3xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp3xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 3xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp3xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp4xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 4xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp4xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp4xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 4xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp4xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp5xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 5xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp5xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp5xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 5xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp5xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp6xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 6xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp6xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsResp6xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 6xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdcurrentstatsresp6xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdCurrentStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable',
            False, 
            [
            _MetaInfoClassMember('csbSIPMthdCurrentStatsEntry', REFERENCE_LIST, 'Csbsipmthdcurrentstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry', 
                [], [], 
                '''                A conceptual row in the csbSIPMthdCurrentStatsTable. Each row
                describes a SIP method and various responses count for this
                method on a given SIP adjacency and given interval. This table
                is indexed on csbSIPMthdCurrentStatsAdjName,
                csbSIPMthdCurrentStatsMethod and 
                csbSIPMthdCurrentStatsInterval. The other indices of this
                table are csbCallStatsInstanceIndex defined in 
                csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
                in csbCallStatsTable.
                ''',
                'csbsipmthdcurrentstatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdCurrentStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsAdjName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the name of the SIP adjacency for which
                stats related with SIP request and all kind of corresponding SIP
                responses are reported. The object acts as an index of the
                table.
                ''',
                'csbsipmthdhistorystatsadjname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsMethod', REFERENCE_ENUM_CLASS, 'CiscosbcsipmethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscosbcsipmethodEnum', 
                [], [], 
                '''                This object indicates the SIP method Request. The object acts
                as an index of the table.
                ''',
                'csbsipmthdhistorystatsmethod',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object indicates the interval for which the historical
                statistics information is to be displayed. The interval
                values can be previous 5 minutes, previous 15 minutes, 
                previous 1 hour and previous 1 Day. This object acts as an 
                index for the table.
                ''',
                'csbsipmthdhistorystatsinterval',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsMethodName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the text representation of the SIP
                method request. E.g. INVITE, ACK, BYE etc.
                ''',
                'csbsipmthdhistorystatsmethodname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsReqIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total incoming SIP message requests
                of this type on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsreqin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsReqOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total outgoing SIP message requests
                of this type on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsreqout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp1xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 1xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp1xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp1xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 1xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp1xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp2xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 2xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp2xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp2xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 2xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp2xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp3xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 3xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp3xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp3xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 3xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp3xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp4xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 4xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp4xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp4xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 4xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp4xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp5xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 5xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp5xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp5xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 5xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp5xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp6xxIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 6xx responses for this method
                received on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp6xxin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsResp6xxOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total 6xx responses for this method
                sent on this SIP adjacency.
                ''',
                'csbsipmthdhistorystatsresp6xxout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdHistoryStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable',
            False, 
            [
            _MetaInfoClassMember('csbSIPMthdHistoryStatsEntry', REFERENCE_LIST, 'Csbsipmthdhistorystatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry', 
                [], [], 
                '''                A conceptual row in the csbSIPMthdHistoryStatsTable. The
                entries in this table are updated as interval completes in
                the csbSIPMthdCurrentStatsTable table and the data is 
                moved from that table to this one.
                This table is indexed on csbSIPMthdHistoryStatsAdjName,
                csbSIPMthdHistoryStatsMethod and
                csbSIPMthdHistoryStatsInterval. The other indices of this 
                table are csbCallStatsInstanceIndex defined in
                csbCallStatsInstanceTable and csbCallStatsServiceIndex
                defined in csbCallStatsTable.
                ''',
                'csbsipmthdhistorystatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdHistoryStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsAdjName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This identifies the name of the adjacency for which statistics
                are reported. This object acts as an index for the table.
                ''',
                'csbsipmthdrccurrentstatsadjname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsMethod', REFERENCE_ENUM_CLASS, 'CiscosbcsipmethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscosbcsipmethodEnum', 
                [], [], 
                '''                This object indicates the SIP method request. This object acts
                as an index for the table.
                ''',
                'csbsipmthdrccurrentstatsmethod',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsRespCode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the response code for the SIP message
                request. The range of valid values for SIP response codes is 100
                - 999. This object acts as an index for the table.
                ''',
                'csbsipmthdrccurrentstatsrespcode',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object identifies the interval for which the periodic
                statistics information is to be displayed. The interval
                values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts
                as an index for the table.
                ''',
                'csbsipmthdrccurrentstatsinterval',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsMethodName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the text representation of the SIP
                method request. E.g. INVITE, ACK, BYE etc.
                ''',
                'csbsipmthdrccurrentstatsmethodname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsRespIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total SIP messages with this response
                code this method received on this SIP adjacency.
                ''',
                'csbsipmthdrccurrentstatsrespin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsRespOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total SIP messages with this response
                code for this method sent on this SIP adjacency.
                ''',
                'csbsipmthdrccurrentstatsrespout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdRCCurrentStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable',
            False, 
            [
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsEntry', REFERENCE_LIST, 'Csbsipmthdrccurrentstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry', 
                [], [], 
                '''                A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each
                entry in this table represents a method and response code
                combination. Each entry in this table is identified by a value
                of csbSIPMthdRCCurrentStatsAdjName,
                csbSIPMthdRCCurrentStatsMethod,
                csbSIPMthdRCCurrentStatsRespCode and
                csbSIPMthdRCCurrentStatsInterval. The other indices of this
                table are csbCallStatsInstanceIndex defined in
                csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
                in csbCallStatsTable.
                ''',
                'csbsipmthdrccurrentstatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdRCCurrentStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsAdjName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This identifies the name of the adjacency for which statistics
                are reported. This object acts as an index for the table.
                ''',
                'csbsipmthdrchistorystatsadjname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsMethod', REFERENCE_ENUM_CLASS, 'CiscosbcsipmethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscosbcsipmethodEnum', 
                [], [], 
                '''                This object indicates the SIP method request. This object acts
                as an index for the table.
                ''',
                'csbsipmthdrchistorystatsmethod',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsRespCode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the response code for the SIP message
                request. The range of valid values for SIP response codes is 100
                - 999. This object acts as an index for the table.
                ''',
                'csbsipmthdrchistorystatsrespcode',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object identifies the interval for which the periodic
                statistics information is to be displayed. The interval
                values can be previous 5 min, previous 15 mins, previous 1 
                hour , previous 1 Day. This object acts as an index for the
                table.
                ''',
                'csbsipmthdrchistorystatsinterval',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', True),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsMethodName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the text representation of the SIP
                method request. E.g. INVITE, ACK, BYE etc.
                ''',
                'csbsipmthdrchistorystatsmethodname',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsRespIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total SIP messages with this response
                code this method received on this SIP adjacency.
                ''',
                'csbsipmthdrchistorystatsrespin',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsRespOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total SIP messages with this response
                code for this method sent on this SIP adjacency.
                ''',
                'csbsipmthdrchistorystatsrespout',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdRCHistoryStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable',
            False, 
            [
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsEntry', REFERENCE_LIST, 'Csbsipmthdrchistorystatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry', 
                [], [], 
                '''                A conceptual row in the csbSIPMthdRCHistoryStatsTable. The
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
                ''',
                'csbsipmthdrchistorystatsentry',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'csbSIPMthdRCHistoryStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrStatsMib' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrStatsMib',
            False, 
            [
            _MetaInfoClassMember('csbRadiusStatsTable', REFERENCE_CLASS, 'Csbradiusstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable', 
                [], [], 
                '''                This table has the reporting statistics of various RADIUS
                messages for RADIUS servers with which the client (SBC) shares a
                secret. Each entry in this table is identified by a 
                value of csbRadiusStatsEntIndex. The other indices of this table
                are csbCallStatsInstanceIndex defined in 
                csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
                in csbCallStatsTable.
                ''',
                'csbradiusstatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbRfBillRealmStatsTable', REFERENCE_CLASS, 'Csbrfbillrealmstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable', 
                [], [], 
                '''                This table describes the Rf billing statistics information
                which monitors the messages sent per-realm by Rf billing 
                manager(SBC). SBC sends Rf billing data using Diameter as a
                transport protocol. Rf billing uses only ACR and ACA Diameter
                messages for the transport of billing data. The
                Accounting-Record-Type AVP on the ACR message labels the type 
                of the accounting request. The following types are used by Rf
                billing.
                1.   For session-based charging, the types Start (session
                begins), Interim (session is modified) and Stop (session ends)
                are used.
                2.   For event-based charging, the type Event is used when a
                chargeable event occurs outside the scope of a session.
                
                Each row of this table is identified by a value of
                csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName.
                The other indices of this table are csbCallStatsInstanceIndex
                defined in csbCallStatsInstanceTable and 
                csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbrfbillrealmstatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdCurrentStatsTable', REFERENCE_CLASS, 'Csbsipmthdcurrentstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable', 
                [], [], 
                '''                This table reports count of SIP request and various SIP
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
                ''',
                'csbsipmthdcurrentstatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdHistoryStatsTable', REFERENCE_CLASS, 'Csbsipmthdhistorystatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable', 
                [], [], 
                '''                This table provide historical count of SIP request and various
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
                ''',
                'csbsipmthdhistorystatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCCurrentStatsTable', REFERENCE_CLASS, 'Csbsipmthdrccurrentstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable', 
                [], [], 
                '''                This table reports SIP method request and response code
                statistics for each method and response code combination on
                given SIP adjacency in a given interval. To understand the 
                meaning of interval please refer <Periodic Statistics> section
                in description of ciscoSbcStatsMIB. An exact lookup will return
                a row only  if -
                1) detailed response code statistics are turned on in SBC
                2) response code  messages sent or received is non zero for 
                   given SIP adjacency, method and interval.
                Also an inexact lookup will only return rows for messages with
                non-zero counts, to protect the user from large numbers of rows 
                for response codes which have not been received or sent.
                ''',
                'csbsipmthdrccurrentstatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            _MetaInfoClassMember('csbSIPMthdRCHistoryStatsTable', REFERENCE_CLASS, 'Csbsipmthdrchistorystatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB', 'CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable', 
                [], [], 
                '''                This table reports historical data for SIP method request and
                response code statistics for each method and response code 
                combination in a given past interval. The possible values of 
                interval will be previous 5 minutes, previous 15 minutes, 
                previous 1 hour and previous day. To understand the 
                meaning of interval please refer <Periodic Statistics> section
                in description of ciscoSbcStatsMIB. An exact lookup will return
                a row only  if -
                1) detailed response code statistics are turned on in SBC
                2) response code  messages sent or received is non zero for 
                   given SIP adjacency, method and interval.
                Also an inexact lookup will only return rows for messages with
                non-zero counts, to protect the user from large numbers of rows
                for response codes which have not been received or sent.
                ''',
                'csbsipmthdrchistorystatstable',
                'CISCO-SESS-BORDER-CTRLR-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            'CISCO-SESS-BORDER-CTRLR-STATS-MIB',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB'
        ),
    },
}
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable.Csbradiusstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbradiusstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbrfbillrealmstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdcurrentstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdhistorystatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrccurrentstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrStatsMib.Csbsipmthdrchistorystatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrStatsMib']['meta_info']
