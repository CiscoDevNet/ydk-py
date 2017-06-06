


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoRadiusExtMib.Creclientglobal' : {
        'meta_info' : _MetaInfoClass('CiscoRadiusExtMib.Creclientglobal',
            False, 
            [
            _MetaInfoClassMember('creClientLastUsedSourceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This MIB object indicates the last source identifier that was
                used to send out a RADIUS packet when 'extended RADIUS source
                ports' is configured.  The source identifier is a counter that
                is incremented everytime a RADIUS authentication or an
                accounting packet is sent.
                ''',
                'creclientlastusedsourceid',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientLastUsedSourcePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If the 'extended RADIUS source ports' is configured, multiple
                source ports are used for sending out RADIUS authentication or
                accounting requests.  This MIB object indicates the last source
                port that was used to send out a RADIUS authentication or
                accounting request.
                ''',
                'creclientlastusedsourceport',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientSourcePortRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If the 'extended RADIUS source port' is configured, multiple
                source ports are used for sending out RADIUS authentication or
                accounting requests.  This MIB object indicates the port value
                where this range ends.
                ''',
                'creclientsourceportrangeend',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientSourcePortRangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If the 'extended RADIUS source ports' is configured, multiple
                source ports are used for sending out RADIUS authentication or
                accounting requests.  This MIB object indicates the port value
                from where this range starts.
                ''',
                'creclientsourceportrangestart',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientTotalAccessRejects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of access reject packets
                received by the RADIUS client.
                ''',
                'creclienttotalaccessrejects',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientTotalAverageResponseDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the overall response delay experienced
                by RADIUS packets (both authentication and accounting).
                ''',
                'creclienttotalaverageresponsedelay',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientTotalMaxDoneQLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum length of the queue which
                stores those RADIUS packets for which the responses are
                received.
                ''',
                'creclienttotalmaxdoneqlength',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientTotalMaxInQLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum length of the queue which
                stores the incoming RADIUS packets.
                ''',
                'creclienttotalmaxinqlength',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientTotalMaxWaitQLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum length of the queue which
                stores the pending RADIUS packets for which the responses are
                outstanding.
                ''',
                'creclienttotalmaxwaitqlength',
                'CISCO-RADIUS-EXT-MIB', False),
            ],
            'CISCO-RADIUS-EXT-MIB',
            'creClientGlobal',
            _yang_ns._namespaces['CISCO-RADIUS-EXT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB'
        ),
    },
    'CiscoRadiusExtMib.Creclientauthentication' : {
        'meta_info' : _MetaInfoClass('CiscoRadiusExtMib.Creclientauthentication',
            False, 
            [
            _MetaInfoClassMember('creAuthClientAverageResponseDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the average response delay experienced
                for RADIUS authentication requests.
                ''',
                'creauthclientaverageresponsedelay',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientBadAuthenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS authentication
                response packets received which contained invalid
                authenticators.
                ''',
                'creauthclientbadauthenticators',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientBufferAllocFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of buffer allocation
                failures encountered during RADIUS request formation.
                ''',
                'creauthclientbufferallocfailures',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientDupIDs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of times client has received
                duplicate authentication responses with the same identifier. 
                Out of these two packets, the later packet is considered as a
                true match.
                ''',
                'creauthclientdupids',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientLastUsedSourceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This MIB object indicates the last source identifier that was
                used to send out a RADIUS authentication request when 'extended
                RADIUS source ports' is configured.  The source identifier is a
                counter that is incremented everytime a RADIUS authentication
                request is sent.
                ''',
                'creauthclientlastusedsourceid',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientMalformedResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of malformed RADIUS
                authentication responses received.  Malformed packets include
                packets with an invalid length.
                ''',
                'creauthclientmalformedresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientMaxBufferSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum buffer size for RADIUS
                authentication packet.
                ''',
                'creauthclientmaxbuffersize',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientMaxResponseDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the maximum delay experienced for RADIUS
                authentication requests.
                ''',
                'creauthclientmaxresponsedelay',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of timeouts that have occurred
                for RADIUS authentication.  After a timeout the client may
                retry sending the request to the same server or to a different
                server or give up depending on the configuration.
                ''',
                'creauthclienttimeouts',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientTotalPacketsWithoutResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS authentication
                packets that never received a response.
                ''',
                'creauthclienttotalpacketswithoutresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientTotalPacketsWithResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS authentication
                packets that received responses.
                ''',
                'creauthclienttotalpacketswithresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientTotalResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS authentication
                response packets received by the RADIUS client.
                ''',
                'creauthclienttotalresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAuthClientUnknownResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of unknown RADIUS
                authentication responses received.
                ''',
                'creauthclientunknownresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            ],
            'CISCO-RADIUS-EXT-MIB',
            'creClientAuthentication',
            _yang_ns._namespaces['CISCO-RADIUS-EXT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB'
        ),
    },
    'CiscoRadiusExtMib.Creclientaccounting' : {
        'meta_info' : _MetaInfoClass('CiscoRadiusExtMib.Creclientaccounting',
            False, 
            [
            _MetaInfoClassMember('creAcctClientAverageResponseDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the average response delay experienced
                for RADIUS accounting.
                ''',
                'creacctclientaverageresponsedelay',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientBadAuthenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS Accounting-Response
                packets received with invalid authenticators.
                ''',
                'creacctclientbadauthenticators',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientBufferAllocFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of buffer allocation failures
                encountered for RADIUS accounting request.
                ''',
                'creacctclientbufferallocfailures',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientDupIDs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of times client has received
                duplicate accounting responses with the same identifier.  Out
                of these two packets, the later packet is considered as a true
                match.
                ''',
                'creacctclientdupids',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientLastUsedSourceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This MIB object indicates the last source identifier that was
                used to send out a RADIUS accounting request when 'extended
                RADIUS source ports' is configured.  The source identifier is a
                counter that is incremented everytime a RADIUS accounting
                request is sent.
                ''',
                'creacctclientlastusedsourceid',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientMalformedResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of malformed RADIUS accounting
                responses received.  Malformed packets include packets with an
                invalid length.
                ''',
                'creacctclientmalformedresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientMaxBufferSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum buffer size for RADIUS
                accounting packets.
                ''',
                'creacctclientmaxbuffersize',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientMaxResponseDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the maximum delay experienced for RADIUS
                accounting.
                ''',
                'creacctclientmaxresponsedelay',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of timeouts that have occurred
                for RADIUS accounting.  After a timeout the client may retry
                sending the request to the same server or to a different
                server or give up depending on the configuration.
                ''',
                'creacctclienttimeouts',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientTotalPacketsWithoutResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS accounting packets
                that never received a response.
                ''',
                'creacctclienttotalpacketswithoutresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientTotalPacketsWithResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS accounting packets
                that received responses.
                ''',
                'creacctclienttotalpacketswithresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientTotalResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of RADIUS accounting response
                packets received by the RADIUS client.
                ''',
                'creacctclienttotalresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creAcctClientUnknownResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of unknown RADIUS accounting
                responses received.
                ''',
                'creacctclientunknownresponses',
                'CISCO-RADIUS-EXT-MIB', False),
            ],
            'CISCO-RADIUS-EXT-MIB',
            'creClientAccounting',
            _yang_ns._namespaces['CISCO-RADIUS-EXT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB'
        ),
    },
    'CiscoRadiusExtMib' : {
        'meta_info' : _MetaInfoClass('CiscoRadiusExtMib',
            False, 
            [
            _MetaInfoClassMember('creClientAccounting', REFERENCE_CLASS, 'Creclientaccounting' , 'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB', 'CiscoRadiusExtMib.Creclientaccounting', 
                [], [], 
                '''                ''',
                'creclientaccounting',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientAuthentication', REFERENCE_CLASS, 'Creclientauthentication' , 'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB', 'CiscoRadiusExtMib.Creclientauthentication', 
                [], [], 
                '''                ''',
                'creclientauthentication',
                'CISCO-RADIUS-EXT-MIB', False),
            _MetaInfoClassMember('creClientGlobal', REFERENCE_CLASS, 'Creclientglobal' , 'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB', 'CiscoRadiusExtMib.Creclientglobal', 
                [], [], 
                '''                ''',
                'creclientglobal',
                'CISCO-RADIUS-EXT-MIB', False),
            ],
            'CISCO-RADIUS-EXT-MIB',
            'CISCO-RADIUS-EXT-MIB',
            _yang_ns._namespaces['CISCO-RADIUS-EXT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB'
        ),
    },
}
_meta_table['CiscoRadiusExtMib.Creclientglobal']['meta_info'].parent =_meta_table['CiscoRadiusExtMib']['meta_info']
_meta_table['CiscoRadiusExtMib.Creclientauthentication']['meta_info'].parent =_meta_table['CiscoRadiusExtMib']['meta_info']
_meta_table['CiscoRadiusExtMib.Creclientaccounting']['meta_info'].parent =_meta_table['CiscoRadiusExtMib']['meta_info']
