


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplntptoltypeEnum' : _MetaInfoEnum('CipslaudpjittertmplntptoltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB',
        {
            'percent':'percent',
            'absolute':'absolute',
        }, 'CISCO-IPSLA-JITTER-MIB', _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB']),
    'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplpktpriorityEnum' : _MetaInfoEnum('CipslaudpjittertmplpktpriorityEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB',
        {
            'normal':'normal',
            'high':'high',
        }, 'CISCO-IPSLA-JITTER-MIB', _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB']),
    'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplprecisionEnum' : _MetaInfoEnum('CipslaudpjittertmplprecisionEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB',
        {
            'milliseconds':'milliseconds',
            'microseconds':'microseconds',
        }, 'CISCO-IPSLA-JITTER-MIB', _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB']),
    'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry',
            False, 
            [
            _MetaInfoClassMember('cipslaUdpJitterTmplName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A string which specifies the UDP Jitter template name.
                ''',
                'cipslaudpjittertmplname',
                'CISCO-IPSLA-JITTER-MIB', True),
            _MetaInfoClassMember('cipslaUdpJitterTmplCodecInterval', ATTRIBUTE, 'int' , None, None, 
                [('4', '60000')], [], 
                '''                This field represents the inter-packet delay between
                packets and is in milliseconds. This object is applicable
                only to UDP jitter operation  which uses codec type.
                ''',
                'cipslaudpjittertmplcodecinterval',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplCodecNumPkts', ATTRIBUTE, 'int' , None, None, 
                [('1', '60000')], [], 
                '''                This value represents the number of packets that need to
                be transmitted. This value is used only for UDP jitter 
                operation which uses codec type.
                ''',
                'cipslaudpjittertmplcodecnumpkts',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplCodecPayload', ATTRIBUTE, 'int' , None, None, 
                [('0', '16384')], [], 
                '''                This object represents the number of octets that needs to be
                placed into the Data portion of the message. This value is
                used only for UDP jitter operation  which uses codec type.
                ''',
                'cipslaudpjittertmplcodecpayload',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplCodecType', REFERENCE_ENUM_CLASS, 'IpslacodectypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB', 'IpslacodectypeEnum', 
                [], [], 
                '''                Specifies the codec type to be used with UDP jitter operation.
                
                If codec-type is configured the following parameters cannot be 
                configured.
                cipslaUdpJitterReqDataSize
                cipslaUdpJitterInterval
                cipslaUdpJitterNumPkts
                ''',
                'cipslaudpjittertmplcodectype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplControlEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is enabled, then the IP SLA application
                will send control messages to a responder, residing on the
                target router to respond to the data request packets being
                sent by the source router.
                ''',
                'cipslaudpjittertmplcontrolenable',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string which provides description of UDP Jitter
                template.
                ''',
                'cipslaudpjittertmpldescription',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplDistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                The maximum number of statistical distribution
                buckets to accumulate.
                
                Since this index does not rollover, only the first
                cipslaUdpJitterTmplDistBuckets will be kept.
                
                The last bucket will contain all entries from its 
                distribution interval start point to infinity.
                ''',
                'cipslaudpjittertmpldistbuckets',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplDistInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The statistical distribution buckets interval.
                
                Distribution Bucket Example:
                
                cipslaUdpJitterTmplDistBuckets = 5 buckets
                cipslaUdpJitterTmplDistInterval = 10 milliseconds
                
                | Bucket 1 | Bucket 2 | Bucket 3 | Bucket 4 | Bucket 5  |
                |  0-9 ms  | 10-19 ms | 20-29 ms | 30-39 ms | 40-Inf ms |
                
                Odd Example:
                
                cipslaUdpJitterTmplDistBuckets = 1 buckets
                cipslaUdpJitterTmplDistInterval = 10 milliseconds
                
                | Bucket 1  |
                |  0-Inf ms |
                
                Thus, this odd example shows that the value of
                cipslaUdpJitterTmplDistInterval does not apply when
                cipslaUdpJitterTmplDistBuckets is one.
                ''',
                'cipslaudpjittertmpldistinterval',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplIcpifFactor', ATTRIBUTE, 'int' , None, None, 
                [('0', '20')], [], 
                '''                The advantage factor is dependant on the type of access and
                how the service is to be used.
                Conventional Wire-line     0
                Mobility within Building    5
                Mobility within geographic area  10
                Access to hard-to-reach location   20
                
                It is used when calculating the ICPIF value.
                ''',
                'cipslaudpjittertmplicpiffactor',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplInterval', ATTRIBUTE, 'int' , None, None, 
                [('4', '60000')], [], 
                '''                This value represents the inter-packet delay between packets
                and is in milliseconds.
                ''',
                'cipslaudpjittertmplinterval',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplNTPTolAbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000')], [], 
                '''                This object specifies the total clock synchronization error
                on source and responder that is considered tolerable for 
                oneway measurement when NTP is used as clock synchronization 
                mechanism.  The total clock synchronization error is sum of
                NTP offsets on source and responder. The value specified is 
                microseconds. This value can be set only for UDP jitter operation 
                with precision of microsecond.
                ''',
                'cipslaudpjittertmplntptolabs',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplNTPTolPct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This object specifies the total clock synchronization error
                on source and responder that is considered tolerable for 
                oneway measurement when NTP is used as clock synchronization 
                mechanism.  The total clock synchronization error is sum of 
                NTP offsets on source and responder. The value is expressed 
                as the percentage of actual oneway latency that is measured. 
                This value can be set only for UDP jitter operation with precision 
                of microsecond.
                ''',
                'cipslaudpjittertmplntptolpct',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplNTPTolType', REFERENCE_ENUM_CLASS, 'CipslaudpjittertmplntptoltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplntptoltypeEnum', 
                [], [], 
                '''                This object specifies whether the value specified for oneway
                NTP sync tolerance is absolute value or percent value.
                
                percent(1)  - The value for oneway NTP sync tolerance is 
                              absolute value.
                absolute(2) - The value for oneway NTP sync tolerance is 
                              percent value.
                ''',
                'cipslaudpjittertmplntptoltype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplNumPkts', ATTRIBUTE, 'int' , None, None, 
                [('1', '60000')], [], 
                '''                This value represents the number of packets that need to be
                transmitted.
                ''',
                'cipslaudpjittertmplnumpkts',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplPktPriority', REFERENCE_ENUM_CLASS, 'CipslaudpjittertmplpktpriorityEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplpktpriorityEnum', 
                [], [], 
                '''                This object specifies the priority that will be assigned
                to operation packet.
                
                normal(1) - The packet is of normal priority.
                high(2)   - The packet is of high priority.
                ''',
                'cipslaudpjittertmplpktpriority',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplPrecision', REFERENCE_ENUM_CLASS, 'CipslaudpjittertmplprecisionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry.CipslaudpjittertmplprecisionEnum', 
                [], [], 
                '''                This object specifies the accuracy of jitter statistics in
                rttMonJitterStatsTable that needs to be calculated.
                milliseconds(1) - The accuracy of stats will be of milliseconds.
                microseconds(2) - The accuracy of stats will be in microseconds.
                ''',
                'cipslaudpjittertmplprecision',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplReqDataSize', ATTRIBUTE, 'int' , None, None, 
                [('16', '65024')], [], 
                '''                This object represents the number of octets to be
                placed into the ARR Data portion of the request
                message, when using SNA protocols.
                
                For non-ARR protocols' IP SLA request/responses,
                this value represents the native payload size.
                
                REMEMBER:  The ARR Header overhead is not included
                           in this value.
                ''',
                'cipslaudpjittertmplreqdatasize',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual UDP Jitter template control row.
                When the status is active, all the read-create objects in that 
                row can be modified.
                ''',
                'cipslaudpjittertmplrowstatus',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This field specifies the IP address of the source.
                ''',
                'cipslaudpjittertmplsrcaddr',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplSrcAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                An enumerated value which specifies the IP address type
                of the source. It must be used along with the
                cipslaUdpJitterTmplSrcAddr object.
                ''',
                'cipslaudpjittertmplsrcaddrtype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplSrcPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the source's port number. If this
                object is not specified, the application will get a
                port allocated by the system.
                ''',
                'cipslaudpjittertmplsrcport',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplStatsHours', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                The maximum number of hours for which statistics are
                maintained. Specifically this is the number of hourly
                groups to keep before rolling over.
                
                The value of one is not advisable because the hourly
                group will close and immediately be deleted before
                the network management station will have the
                opportunity to retrieve the statistics.
                
                The value of zero will shut off data collection.
                ''',
                'cipslaudpjittertmplstatshours',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslaudpjittertmplstoragetype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object defines an administrative threshold limit.
                If the IP SLA operation time exceeds this limit, then
                one threshold crossing occurrence will be counted.
                ''',
                'cipslaudpjittertmplthreshold',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplTimeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800000')], [], 
                '''                Specifies the duration to wait for a IP SLA operation
                completion. 
                
                For connection oriented protocols, this may cause the
                connection to be closed by the operation.  Once closed, it
                will be assumed that the connection reestablishment
                will be performed.  To prevent unwanted closure of
                connections, be sure to set this value to a realistic
                connection timeout.
                ''',
                'cipslaudpjittertmpltimeout',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object represents the type of service octet in an
                IP header.
                ''',
                'cipslaudpjittertmpltos',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplVerifyData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, the resulting data in each IP SLA
                operation is compared with the expected data.  This
                includes checking header information (if possible) and
                exact packet size.
                ''',
                'cipslaudpjittertmplverifydata',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VRF name in
                which the IP SLA operation will be used. For regular IP SLA
                operation this field should not be configured. The agent
                will use this field to identify the VPN routing table for
                this operation.
                ''',
                'cipslaudpjittertmplvrfname',
                'CISCO-IPSLA-JITTER-MIB', False),
            ],
            'CISCO-IPSLA-JITTER-MIB',
            'cipslaUdpJitterTmplEntry',
            _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB'
        ),
    },
    'CiscoIpslaJitterMib.Cipslaudpjittertmpltable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaJitterMib.Cipslaudpjittertmpltable',
            False, 
            [
            _MetaInfoClassMember('cipslaUdpJitterTmplEntry', REFERENCE_LIST, 'Cipslaudpjittertmplentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry', 
                [], [], 
                '''                A row entry representing an IPSLA UDP jitter template.
                ''',
                'cipslaudpjittertmplentry',
                'CISCO-IPSLA-JITTER-MIB', False),
            ],
            'CISCO-IPSLA-JITTER-MIB',
            'cipslaUdpJitterTmplTable',
            _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB'
        ),
    },
    'CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpJitterTmplName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A string which specifies the ICMP jitter template name.
                ''',
                'cipslaicmpjittertmplname',
                'CISCO-IPSLA-JITTER-MIB', True),
            _MetaInfoClassMember('cipslaIcmpJitterTmplDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string which provides description of ICMP Jitter
                template.
                ''',
                'cipslaicmpjittertmpldescription',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplDistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                The maximum number of statistical distribution
                buckets to accumulate.
                
                Since this index does not rollover, only the first
                cipslaIcmpJitterTmplDistBuckets will be kept.
                
                The last bucket will contain all entries from its 
                distribution interval start point to infinity.
                ''',
                'cipslaicmpjittertmpldistbuckets',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplDistInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The statistical distribution buckets interval.
                
                Distribution Bucket Example:
                
                cipslaIcmpJitterTmplDistBuckets = 5 buckets
                cipslaIcmpJitterTmplDistInterval = 10 milliseconds
                
                | Bucket 1 | Bucket 2 | Bucket 3 | Bucket 4 | Bucket 5  |
                |  0-9 ms  | 10-19 ms | 20-29 ms | 30-39 ms | 40-Inf ms |
                
                Odd Example:
                
                cipslaIcmpJitterTmplDistBuckets = 1 buckets
                cipslaIcmpJitterTmplDistInterval = 10 milliseconds
                
                | Bucket 1  |
                |  0-Inf ms |
                
                Thus, this odd example shows that the value of
                cipslaIcmpJitterTmplDistInterval does not apply when
                cipslaIcmpJitterTmplDistBuckets is one.
                ''',
                'cipslaicmpjittertmpldistinterval',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplInterval', ATTRIBUTE, 'int' , None, None, 
                [('4', '60000')], [], 
                '''                This value represents the inter-packet delay between packets
                and is in milliseconds.
                ''',
                'cipslaicmpjittertmplinterval',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplNumPkts', ATTRIBUTE, 'int' , None, None, 
                [('1', '60000')], [], 
                '''                This value represents the number of packets that need to be
                transmitted.
                ''',
                'cipslaicmpjittertmplnumpkts',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual ICMP jitter template control row.
                When the status is active, all the read-create objects in 
                that row can be modified.
                ''',
                'cipslaicmpjittertmplrowstatus',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A string which specifies the IP address of the source.
                ''',
                'cipslaicmpjittertmplsrcaddr',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplSrcAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                An enumerated value which specifies the IP address type
                of the source. It must be used along with the
                cipslaIcmpJitterTmplSrcAddr object.
                ''',
                'cipslaicmpjittertmplsrcaddrtype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplStatsHours', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                The maximum number of hourss for which statistics are
                maintained. Specifically this is the number of hourly
                groups to keep before rolling over.
                
                The value of one is not advisable because the hourly
                group will close and immediately be deleted before
                the network management station will have the
                opportunity to retrieve the statistics.
                
                The value of zero will shut off data collection.
                ''',
                'cipslaicmpjittertmplstatshours',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslaicmpjittertmplstoragetype',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object defines an administrative threshold limit.
                If the IP SLA operation time exceeds this limit, then 
                one threshold crossing occurrence will be counted.
                ''',
                'cipslaicmpjittertmplthreshold',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplTimeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800000')], [], 
                '''                Specifies the duration to wait for a IP SLA operation
                completion.
                
                For connection oriented protocols, this may cause the
                connection to be closed by the operation.  Once closed, it
                will be assumed that the connection reestablishment
                will be performed.  To prevent unwanted closure of
                connections, be sure to set this value to a realistic
                connection timeout.
                ''',
                'cipslaicmpjittertmpltimeout',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object represents the type of service octet in an
                IP header.
                ''',
                'cipslaicmpjittertmpltos',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplVerifyData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, the resulting data in each IP SLA
                operation is compared with the expected data.  This
                includes checking header information (if possible) and
                exact packet size.
                ''',
                'cipslaicmpjittertmplverifydata',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaIcmpJitterTmplVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VRF name in
                which the IP SLA operation will be used. For regular IP SLA
                operation this field should not be configured. The agent
                will use this field to identify the VPN routing Table for
                this operation.
                ''',
                'cipslaicmpjittertmplvrfname',
                'CISCO-IPSLA-JITTER-MIB', False),
            ],
            'CISCO-IPSLA-JITTER-MIB',
            'cipslaIcmpJitterTmplEntry',
            _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB'
        ),
    },
    'CiscoIpslaJitterMib.Cipslaicmpjittertmpltable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaJitterMib.Cipslaicmpjittertmpltable',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpJitterTmplEntry', REFERENCE_LIST, 'Cipslaicmpjittertmplentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry', 
                [], [], 
                '''                A row entry representing an IP SLA ICMP Jitter template.
                ''',
                'cipslaicmpjittertmplentry',
                'CISCO-IPSLA-JITTER-MIB', False),
            ],
            'CISCO-IPSLA-JITTER-MIB',
            'cipslaIcmpJitterTmplTable',
            _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB'
        ),
    },
    'CiscoIpslaJitterMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaJitterMib',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpJitterTmplTable', REFERENCE_CLASS, 'Cipslaicmpjittertmpltable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaicmpjittertmpltable', 
                [], [], 
                '''                A table that contains ICMP jitter template specific definitions.
                ''',
                'cipslaicmpjittertmpltable',
                'CISCO-IPSLA-JITTER-MIB', False),
            _MetaInfoClassMember('cipslaUdpJitterTmplTable', REFERENCE_CLASS, 'Cipslaudpjittertmpltable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB', 'CiscoIpslaJitterMib.Cipslaudpjittertmpltable', 
                [], [], 
                '''                A table that contains UDP jitter template specific definitions.
                ''',
                'cipslaudpjittertmpltable',
                'CISCO-IPSLA-JITTER-MIB', False),
            ],
            'CISCO-IPSLA-JITTER-MIB',
            'CISCO-IPSLA-JITTER-MIB',
            _yang_ns._namespaces['CISCO-IPSLA-JITTER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_JITTER_MIB'
        ),
    },
}
_meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable.Cipslaudpjittertmplentry']['meta_info'].parent =_meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable']['meta_info']
_meta_table['CiscoIpslaJitterMib.Cipslaicmpjittertmpltable.Cipslaicmpjittertmplentry']['meta_info'].parent =_meta_table['CiscoIpslaJitterMib.Cipslaicmpjittertmpltable']['meta_info']
_meta_table['CiscoIpslaJitterMib.Cipslaudpjittertmpltable']['meta_info'].parent =_meta_table['CiscoIpslaJitterMib']['meta_info']
_meta_table['CiscoIpslaJitterMib.Cipslaicmpjittertmpltable']['meta_info'].parent =_meta_table['CiscoIpslaJitterMib']['meta_info']
