


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoTap2Mib.Ctap2Mediationgroup' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Mediationgroup',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationCapabilities', REFERENCE_BITS, 'Ctap2Mediationcapabilities' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Mediationgroup.Ctap2Mediationcapabilities', 
                [], [], 
                '''                This object displays the device capabilities with respect to
                certain fields in Mediation Device table. This may be dependent
                on hardware capabilities, software capabilities.
                The following values may be supported:
                    ipV4SrcInterface:  SNMP ifIndex Value may be used to select
                                       the interface (denoted by
                                       cTap2MediationSrcInterface) on the
                                       intercepting device from which to
                                       transmit intercepted data to an IPv4
                                       address Mediation Device.
                
                
                    ipV6SrcInterface:  SNMP ifIndex Value may be used to select
                                       the interface (denoted by
                                       cTap2MediationSrcInterface) on the
                                       intercepting device from which to
                                       transmit intercepted data to an IPv6
                                       address Mediation Device.
                
                
                    udp:               UDP may be used as transport protocol
                                       (denoted by cTap2MediationTransport) in
                                       transferring intercepted data to the
                                       Mediation Device.
                
                
                    rtcpNack:          RTP with Nack resilience may be used
                                       as transport protocol (denoted by
                                       cTap2MediationTransport) in transferring
                                       intercepted data to the Mediation
                                       Device.
                
                    tcp:               TCP may be used as transport protocol
                                       (denoted by cTap2MediationTransport) in
                                       transferring intercepted data to the
                                       Mediation Device.
                
                
                    sctp:              SCTP may be used as transport protocol
                                       (denoted by cTap2MediationTransport) in
                                       transferring intercepted data to the
                                       Mediation Device.
                
                    rtp:               RTP may be used as transport protocol
                                       (denoted by cTap2MediationTransport) in
                                       transferring intercepted data to the
                                       Mediation Device. 
                
                    radius:            Radius may be used as transport protocol
                                       (denoted by cTap2MediationTransport) in
                                       transferring intercepted information to 
                                       the Mediation Device.
                ''',
                'ctap2mediationcapabilities',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object contains a value which may be used as an index
                value for a new cTap2MediationEntry. Whenever read, the agent
                will change the value to a new non-conflicting value.  This is
                to reduce the probability of errors during creation of new
                cTap2MediationTable entries.
                ''',
                'ctap2mediationnewindex',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2MediationGroup',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Debuggroup' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Debuggroup',
            False, 
            [
            _MetaInfoClassMember('cTap2DebugAge', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object contains the duration in minutes for which an
                entry in cTap2DebugTable is maintained by the implementing
                device after which the entry is deleted. The management
                station also has the option of deleting the entry itself
                by setting cTap2DebugStatus.
                ''',
                'ctap2debugage',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugMaxEntries', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object contains the maximum number of debug messages
                maintained by the implementing device at a time. If this 
                limit is crossed, most recent message will replace the
                least recent message.
                ''',
                'ctap2debugmaxentries',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2DebugGroup',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry.Ctap2MediationtransportEnum' : _MetaInfoEnum('Ctap2MediationtransportEnum', 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB',
        {
            'udp':'udp',
            'rtpNack':'rtpNack',
            'tcp':'tcp',
            'sctp':'sctp',
            'rtp':'rtp',
            'radius':'radius',
        }, 'CISCO-TAP2-MIB', _yang_ns._namespaces['CISCO-TAP2-MIB']),
    'CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationContentId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                cTap2MediationContentId is a session identifier, from the
                intercept application's perspective, and a content identifier
                from the Mediation Device's perspective. The Mediation Device
                is responsible for making sure these are unique, although the
                SNMP RowStatus row creation process will help by not allowing
                it to create conflicting entries. Before creating a new entry,
                a value for this variable may be obtained by reading
                cTap2MediationNewIndex to reduce the probability of a value
                collision.
                ''',
                'ctap2mediationcontentid',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2MediationDataType', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                If RTP with Ack/Nack resilience is selected as a transport,
                the mediation process requires an RTP payload type for data
                transmissions, and a second RTP payload type for
                retransmissions.  This is the RTP payload type for
                transmissions.
                
                
                This object is only effective when the value of
                cTap2MediationTransport is 'rtpNack'.
                ''',
                'ctap2mediationdatatype',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationDestAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP Address of the Mediation Device's network interface
                to which to direct intercepted traffic.
                ''',
                'ctap2mediationdestaddress',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationDestAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of cTap2MediationDestAddress.
                ''',
                'ctap2mediationdestaddresstype',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationDestPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number on the Mediation Device's network interface
                to which to direct intercepted traffic.
                ''',
                'ctap2mediationdestport',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The Differentiated Services Code Point the intercepting
                device applies to the IP packets encapsulating the
                intercepted traffic.
                ''',
                'ctap2mediationdscp',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable controls the generation of any notifications or
                informs by the MIB agent for this table entry.
                ''',
                'ctap2mediationnotificationenable',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationRadiusKey', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Radius Authentication Key is the shared secret key between 
                radius client and server.
                ''',
                'ctap2mediationradiuskey',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationRetransmitType', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                If RTP with Ack/Nack resilience is selected as a transport,
                the mediation process requires an RTP payload type for data
                transmissions, and a second RTP payload type for
                retransmissions.  This is the RTP payload type for
                retransmissions.
                
                
                This object is only effective when the value of
                cTap2MediationTransport is 'rtpNack'.
                ''',
                'ctap2mediationretransmittype',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationRtcpPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number on the intercepting device to which the
                Mediation Devices directs RTCP Receiver Reports and Nacks.
                This object is only relevant when the value of
                cTap2MediationTransport is 'rtpNack'.
                
                
                This port is assigned by the intercepting device, rather than
                by the Mediation Device or manager application.  The value of
                this MIB object has no effect before activating the
                cTap2MediationEntry.
                ''',
                'ctap2mediationrtcpport',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationSrcInterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The interface on the intercepting device from which to
                transmit intercepted data. If zero, any interface may be used
                according to normal IP practice.
                ''',
                'ctap2mediationsrcinterface',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. This object is used to
                manage creation, modification and deletion of rows in this
                table.
                
                
                cTap2MediationTimeout may be modified at any time (even while
                the row is active). But when the row is active, the other
                writable objects may not be modified without setting its value
                to 'notInService'.
                
                
                The entry may not be deleted or deactivated by setting its
                value to 'destroy' or 'notInService' if there is any associated
                entry in cTap2StreamTable.
                ''',
                'ctap2mediationstatus',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationTimeout', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The time at which this row and all related Stream Table rows
                should be automatically removed, and the intercept function
                cease. Since the initiating network manager may be the only
                device able to manage a specific intercept or know of its
                existence, this acts as a fail-safe for the failure or removal
                of the network manager. The object is only effective when the
                value of cTap2MediationStatus is 'active'.
                ''',
                'ctap2mediationtimeout',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationTransport', REFERENCE_ENUM_CLASS, 'Ctap2MediationtransportEnum' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry.Ctap2MediationtransportEnum', 
                [], [], 
                '''                The protocol used in transferring intercepted data to the
                Mediation Device. The following protocols may be supported:
                           udp:     PacketCable udp format
                           rtpNack: RTP with Nack resilience
                           tcp:     TCP with head of line blocking
                           sctp:    SCTP with head of line blocking 
                           rtp:     Realtime Transport Protocol(RTP)
                                    packet format
                           radius:  Use Radius, PacketCable1.5 Event Message
                                    to transport the intercepted information.
                ''',
                'ctap2mediationtransport',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2MediationEntry',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Mediationtable' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Mediationtable',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationEntry', REFERENCE_LIST, 'Ctap2Mediationentry' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry', 
                [], [], 
                '''                The entry describes a single session maintained with an
                application on a Mediation Device.
                ''',
                'ctap2mediationentry',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2MediationTable',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry.Ctap2StreamtypeEnum' : _MetaInfoEnum('Ctap2StreamtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB',
        {
            'ip':'ip',
            'mac':'mac',
            'userConnection':'userConnection',
            'msPdsn':'msPdsn',
            'mobility':'mobility',
            'voip':'voip',
        }, 'CISCO-TAP2-MIB', _yang_ns._namespaces['CISCO-TAP2-MIB']),
    'CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationContentId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ctap2mediationcontentid',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2StreamIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index of the stream itself.
                ''',
                'ctap2streamindex',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2StreamInterceptDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets matching this data stream specification
                that, having been intercepted, were dropped in the lawful
                intercept process.
                ''',
                'ctap2streaminterceptdrops',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamInterceptedHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets matching this data stream specification
                that have been intercepted. This object is a 64-bit version of
                cTap2StreamInterceptedPackets.
                ''',
                'ctap2streaminterceptedhcpackets',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamInterceptedPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets matching this data stream specification
                that have been intercepted.
                ''',
                'ctap2streaminterceptedpackets',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamInterceptEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If 'true', the tap should intercept matching traffic. The
                value for this object should be set to 'true' only after an 
                additional filter specification has been attached to this 
                stream.
                ''',
                'ctap2streaminterceptenable',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamInterceptHCDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets matching this data stream specification
                that, having been intercepted, were dropped in the lawful
                intercept process. This object is a 64-bit version of
                cTap2StreamInterceptDrops.
                ''',
                'ctap2streamintercepthcdrops',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. This object manages
                creation, modification, and deletion of rows in this table.
                cTap2StreamInterceptEnable may be modified any time even the
                value of this entry rowStatus object is 'active'.  When other
                rows must be changed, cTap2StreamStatus must be first set to
                'notInService'.
                ''',
                'ctap2streamstatus',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamType', REFERENCE_ENUM_CLASS, 'Ctap2StreamtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry.Ctap2StreamtypeEnum', 
                [], [], 
                '''                Identifies the type of intercept filter associated to this
                generic stream. The following types of streams are supported:
                       ip:             The specific filter is an IP filter 
                                       with same indices as that of this 
                                       table. The exact filter is a row in 
                                       citapStreamTable of CISCO-IP-TAP-MIB.
                       mac:            The specific filter is a MAC filter
                                       with same indices as that of this table.
                                       The exact filter is a row in 
                                       c8tapStreamTable of CISCO-802-TAP-MIB.
                       userConnecton:  The specific filter is a user connection
                                       filter with same indices as that of 
                                       this table. The exact filter is a row 
                                       in cuctTapStreamTable of 
                                       CISCO-USER-CONNECTION-TAP-MIB.
                       msPdsn:         The specific filter is a Mobile Sub
                                       connection filter with same indices as
                                       that of this table. The exact filter
                                       is a row in ccptapStreamTable of 
                                       CISCO-CDMA-PDSN-TAP-MIB.
                       mobility:       The specific filter is a Mobile 
                                       Subscriber connection filter with same
                                       indices as that of this table. The exact
                                       filter is a row in cmtapStreamTable of 
                                       CISCO-MOBILITY-TAP-MIB.
                       voip:           The specific filter is a VoIP
                                       Subscriber filter with same
                                       indices as that of this table. The exact
                                       filter is a row in cvoiptapStreamTable of
                                       CISCO-VOIP-TAP-MIB.
                ''',
                'ctap2streamtype',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2StreamEntry',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Streamtable' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Streamtable',
            False, 
            [
            _MetaInfoClassMember('cTap2StreamEntry', REFERENCE_LIST, 'Ctap2Streamentry' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry', 
                [], [], 
                '''                A stream entry indicates a single data stream to be
                intercepted to a Mediation Device. Many selected data
                streams may go to the same application interface, and many
                application interfaces are supported.
                ''',
                'ctap2streamentry',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2StreamTable',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Debugtable.Ctap2Debugentry' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Debugtable.Ctap2Debugentry',
            False, 
            [
            _MetaInfoClassMember('cTap2DebugIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Index to the debug table.
                ''',
                'ctap2debugindex',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2DebugMediationId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object is that of cTap2MediationContentId
                identifying an entry in cTap2MediationTable. Note this object
                may contain a value for which an entry in cTap2MediationTable
                does not exist. This happens when creation of an entry in
                cTap2MediationTable fails and this debug message conveys more
                detailed information regarding the failure.
                ''',
                'ctap2debugmediationid',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugMessage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A text string contains the debug message.
                ''',
                'ctap2debugmessage',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. A row in this table is
                created by the implementing device. A management station cannot
                modify any of the objects in this row, except deleting the row
                by setting this object to 'destroy'.
                ''',
                'ctap2debugstatus',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugStreamId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object is that of cTap2StreamIndex of an
                entry in cTap2StreamTable. This object along with
                cTap2DebugMediationId identifies an entry in cTap2StreamTable.
                The value of this object may be zero, in which this debug
                message is regarding a Mediation Device, but not a particular
                stream.  Note this object may contain a value for which an 
                entry in cTap2MediationTable does not exist. This happens 
                when creation of an entry in cTap2StreamTable fails.
                ''',
                'ctap2debugstreamid',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2DebugEntry',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Debugtable' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Debugtable',
            False, 
            [
            _MetaInfoClassMember('cTap2DebugEntry', REFERENCE_LIST, 'Ctap2Debugentry' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Debugtable.Ctap2Debugentry', 
                [], [], 
                '''                A list of the debug messages.
                ''',
                'ctap2debugentry',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2DebugTable',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Debugusertable.Ctap2Debuguserentry' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Debugusertable.Ctap2Debuguserentry',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationContentId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ctap2mediationcontentid',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2DebugUserName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A human readable string representing the name of debug user
                who will have access to Lawful Intercept commands.
                ''',
                'ctap2debugusername',
                'CISCO-TAP2-MIB', True),
            _MetaInfoClassMember('cTap2DebugUserStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. This object manages
                creation, modification, and deletion of rows in this table.
                cTap2DebugUserTimeout may be modified any time even when the
                value of this entry rowStatus object is 'active'.
                ''',
                'ctap2debuguserstatus',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugUserStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object specifies the storage type of this conceptual row.
                If it is set to 'nonVolatile', this entry can be saved into
                non-volatile memory.
                ''',
                'ctap2debuguserstoragetype',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugUserTimeout', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the time at which the row will be
                removed from the table by the system. The value of this object
                is only effective when the value of corresponding instance of
                cTap2DebugUserStatus is 'active'.
                ''',
                'ctap2debugusertimeout',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2DebugUserEntry',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib.Ctap2Debugusertable' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib.Ctap2Debugusertable',
            False, 
            [
            _MetaInfoClassMember('cTap2DebugUserEntry', REFERENCE_LIST, 'Ctap2Debuguserentry' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Debugusertable.Ctap2Debuguserentry', 
                [], [], 
                '''                A conceptual row in the cTap2DebugUserTable. Each row
                represents name of user on the router to whom Mediation Device
                with CCCid represented by cTap2MediationContentId has given
                access to Lawful Intercept commands and cTap2DebugUserTimeout
                represents the time when the entry will expire.
                ''',
                'ctap2debuguserentry',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'cTap2DebugUserTable',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
    'CiscoTap2Mib' : {
        'meta_info' : _MetaInfoClass('CiscoTap2Mib',
            False, 
            [
            _MetaInfoClassMember('cTap2DebugGroup', REFERENCE_CLASS, 'Ctap2Debuggroup' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Debuggroup', 
                [], [], 
                '''                ''',
                'ctap2debuggroup',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugTable', REFERENCE_CLASS, 'Ctap2Debugtable' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Debugtable', 
                [], [], 
                '''                A table that contains Lawful Intercept debug messages
                generated by the implementing device. This table is used 
                by ciscoTap2MediationDebug and ciscoTap2StreamDebug 
                notifications.
                
                An entry in this table contains a debug message which is
                regarding either a Mediation Device or a intercept stream 
                created by a Mediation Device. The Mediation device is 
                identified by cTap2DebugMediationId whose value is
                that of cTap2MediationContentId of cTapMediationEntry.
                The stream is identified by cTap2DebugMediationId and
                cTap2DebugStreamId whose values are that of 
                cTap2MediationContentId and cTap2StreamIndex of 
                the corresponding cTap2StreamEntry.
                
                Note that cTap2DebugStreamId may be zero for an entry,
                in which case the debug message is regarding a Medation
                Device.
                
                Entries are added to this table via cTap2DebugStatus in
                accordance with the RowStatus convention.
                ''',
                'ctap2debugtable',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2DebugUserTable', REFERENCE_CLASS, 'Ctap2Debugusertable' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Debugusertable', 
                [], [], 
                '''                The User Table lists information of all the users configured
                in the system who are given permission by different Mediation
                Devices to access Lawful Intercept CLIs.
                
                This table will have dependancy on cTap2MediationTable. When
                entry in cTap2MediationTable is deleted or moved to
                'notInService', entries corresponding cTap2MediationContentId
                in this table will be deleted.
                ''',
                'ctap2debugusertable',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationGroup', REFERENCE_CLASS, 'Ctap2Mediationgroup' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Mediationgroup', 
                [], [], 
                '''                ''',
                'ctap2mediationgroup',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2MediationTable', REFERENCE_CLASS, 'Ctap2Mediationtable' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Mediationtable', 
                [], [], 
                '''                This table lists the Mediation Devices with which the
                intercepting device communicates. These may be on the same or
                different Mediation Devices.
                
                
                This table is written by the Mediation Device, and is always
                volatile. This is because intercepts may disappear during a
                restart of the intercepting equipment.
                
                Entries are added to this table via cTap2MediationStatus in 
                accordance with the RowStatus convention.
                ''',
                'ctap2mediationtable',
                'CISCO-TAP2-MIB', False),
            _MetaInfoClassMember('cTap2StreamTable', REFERENCE_CLASS, 'Ctap2Streamtable' , 'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB', 'CiscoTap2Mib.Ctap2Streamtable', 
                [], [], 
                '''                The Intercept Stream Table lists the traffic streams to be
                intercepted. The same data stream may be required by multiple 
                taps, and one might assume that often the intercepted stream 
                is a small subset of the traffic that could be intercepted.
                
                
                The Table consists of generic fields that are independent
                of the type of intercept. It contains type of the specific 
                filter which is defined in an extension MIB and counters to 
                account for packets intercepted or dropped by the attached
                filter specification.
                
                Note that the Mediation Device must make sure there is 
                only one type of specific filter created with the same 
                indices as that of a row in this table, otherwise the 
                later creations will fail. For example, if there is a 
                row in this table with index 1.2, there can be a 
                corresponding row with the same index either in 
                citapStreamTable, c8tapStreamTable or cuctTapStreamTable,
                but not all. 
                
                
                The first index indicates which Mediation Device the
                intercepted traffic will be diverted to. The second index
                permits multiple classifiers to be used together. 
                
                Entries are added to this table via cTap2StreamStatus in
                accordance with the RowStatus convention.
                ''',
                'ctap2streamtable',
                'CISCO-TAP2-MIB', False),
            ],
            'CISCO-TAP2-MIB',
            'CISCO-TAP2-MIB',
            _yang_ns._namespaces['CISCO-TAP2-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_TAP2_MIB'
        ),
    },
}
_meta_table['CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry']['meta_info'].parent =_meta_table['CiscoTap2Mib.Ctap2Mediationtable']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry']['meta_info'].parent =_meta_table['CiscoTap2Mib.Ctap2Streamtable']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Debugtable.Ctap2Debugentry']['meta_info'].parent =_meta_table['CiscoTap2Mib.Ctap2Debugtable']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Debugusertable.Ctap2Debuguserentry']['meta_info'].parent =_meta_table['CiscoTap2Mib.Ctap2Debugusertable']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Mediationgroup']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Debuggroup']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Mediationtable']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Streamtable']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Debugtable']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
_meta_table['CiscoTap2Mib.Ctap2Debugusertable']['meta_info'].parent =_meta_table['CiscoTap2Mib']['meta_info']
