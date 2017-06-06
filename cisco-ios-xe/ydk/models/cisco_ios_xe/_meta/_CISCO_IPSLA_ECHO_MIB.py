


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.CipslaicmpechotmplhistfilterEnum' : _MetaInfoEnum('CipslaicmpechotmplhistfilterEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB',
        {
            'none':'none',
            'all':'all',
            'overThreshold':'overThreshold',
            'failures':'failures',
        }, 'CISCO-IPSLA-ECHO-MIB', _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB']),
    'CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpEchoTmplName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This field is used to specify the ICMP echo template name.
                ''',
                'cipslaicmpechotmplname',
                'CISCO-IPSLA-ECHO-MIB', True),
            _MetaInfoClassMember('cipslaIcmpEchoTmplDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This field is used to provide description for the ICMP echo
                template.
                ''',
                'cipslaicmpechotmpldescription',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplDistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                The maximum number of statistical distribution
                buckets to accumulate.
                
                Since this index does not rollover, only the first
                cipslaIcmpEchoTmplStatsNumDistBuckets will be kept.
                
                The last cipslaIcmpEchoTmplStatsNumDistBucket will
                contain all entries from its distribution interval
                start point to infinity.
                ''',
                'cipslaicmpechotmpldistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplDistInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The statistical distribution buckets interval.
                
                Distribution Bucket Example:
                
                cipslaIcmpEchoTmplDistBuckets = 5 buckets
                cipslaIcmpEchoTmplDistInterval = 10 milliseconds
                
                | Bucket 1 | Bucket 2 | Bucket 3 | Bucket 4 | Bucket 5  |
                |  0-9 ms  | 10-19 ms | 20-29 ms | 30-39 ms | 40-Inf ms |
                
                Odd Example:
                
                cipslaIcmpEchoTmplDistBuckets = 1 buckets
                cipslaIcmpEchoTmplDistInterval = 10 milliseconds
                
                | Bucket 1  |
                |  0-Inf ms |
                
                Thus, this odd example shows that the value of
                cipslaIcmpEchoTmplDistInterval does not apply when
                cipslaIcmpEchoTmplDistBuckets is one.
                ''',
                'cipslaicmpechotmpldistinterval',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplHistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                The maximum number of history buckets to record.
                This value is set to the number of operations 
                to keep per lifetime.
                
                After cipslaIcmpEchoTmplHistBuckets are filled, the 
                oldest entries are deleted and the most recent
                cipslaIcmpEchoTmplHistBuckets buckets are retained.
                ''',
                'cipslaicmpechotmplhistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplHistFilter', REFERENCE_ENUM_CLASS, 'CipslaicmpechotmplhistfilterEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry.CipslaicmpechotmplhistfilterEnum', 
                [], [], 
                '''                Defines a filter for adding RTT results to the history
                buffer:
                
                none(1)          - no history is recorded
                all(2)           - the results of all completion times 
                                   and failed completions are recorded
                overThreshold(3) - the results of completion times
                                   over cipslaIcmpEchoTmplThreshold are 
                                   recorded.
                failures(4)      - the results of failed operations (only) 
                                   are recorded.
                ''',
                'cipslaicmpechotmplhistfilter',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplHistLives', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                The maximum number of history lives to record.  A life
                is defined by the countdown (or transition) to zero 
                by the cipslaAutoGroupScheduleLife object.  A new life is
                created when the same conceptual control row is
                restarted via the transition of the 
                cipslaAutoGroupScheduleLife object and its subsequent 
                countdown.
                
                The value of zero will shut off all data collection.
                ''',
                'cipslaicmpechotmplhistlives',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplReqDataSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '16384')], [], 
                '''                This object represents the number of octets to be
                placed into the ARR Data portion of the request
                message, when using SNA protocols.
                
                For non-ARR protocols' IP SLA request/responses,
                this value represents the native payload size.
                
                REMEMBER:  The ARR Header overhead is not included
                           in this value.
                ''',
                'cipslaicmpechotmplreqdatasize',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual ICMP echo template control row.
                When the status is active, all the read-create objects in that 
                row can be modified.
                ''',
                'cipslaicmpechotmplrowstatus',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A string which specifies the IP address of the source.
                ''',
                'cipslaicmpechotmplsrcaddr',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplSrcAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                An enumerated value which specifies the IP address type
                of the source. It must be used along with the
                cipslaIcmpEchoTmplSrcAddr object.
                ''',
                'cipslaicmpechotmplsrcaddrtype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplStatsHours', ATTRIBUTE, 'int' , None, None, 
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
                'cipslaicmpechotmplstatshours',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslaicmpechotmplstoragetype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object defines an administrative threshold limit.
                If the IP SLA operation time exceeds this limit and if the
                condition specified in cipslaIcmpEchoTmplHistFilter is
                satisfied, one threshold crossing occurrence will be counted.
                ''',
                'cipslaicmpechotmplthreshold',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplTimeOut', ATTRIBUTE, 'int' , None, None, 
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
                'cipslaicmpechotmpltimeout',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object represents the type of service octet in an
                IP header.
                ''',
                'cipslaicmpechotmpltos',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplVerifyData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, the resulting data in each IP SLA
                operation is compared with the expected data.  This
                includes checking header information (if possible) and
                exact packet size.
                ''',
                'cipslaicmpechotmplverifydata',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaIcmpEchoTmplVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VRF name with
                which the IP SLA operation will be used. For regular IP SLA
                operation this field should not be configured. The agent
                will use this field to identify the VRF routing table for
                this operation.
                ''',
                'cipslaicmpechotmplvrfname',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaIcmpEchoTmplEntry',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib.Cipslaicmpechotmpltable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslaicmpechotmpltable',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpEchoTmplEntry', REFERENCE_LIST, 'Cipslaicmpechotmplentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry', 
                [], [], 
                '''                A row entry representing an IPSLA ICMP echo template.
                ''',
                'cipslaicmpechotmplentry',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaIcmpEchoTmplTable',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry.CipslaudpechotmplhistfilterEnum' : _MetaInfoEnum('CipslaudpechotmplhistfilterEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB',
        {
            'none':'none',
            'all':'all',
            'overThreshold':'overThreshold',
            'failures':'failures',
        }, 'CISCO-IPSLA-ECHO-MIB', _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB']),
    'CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry',
            False, 
            [
            _MetaInfoClassMember('cipslaUdpEchoTmplName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A string which specifies the UDP echo template name.
                ''',
                'cipslaudpechotmplname',
                'CISCO-IPSLA-ECHO-MIB', True),
            _MetaInfoClassMember('cipslaUdpEchoTmplControlEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is enabled, then the IP SLA application
                will send control messages to a responder, residing on the
                target router to respond to the data request packets being
                sent by the source router.
                ''',
                'cipslaudpechotmplcontrolenable',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string which provides description to the UDP echo template.
                ''',
                'cipslaudpechotmpldescription',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplDistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                The maximum number of statistical distribution
                buckets to accumulate.
                
                Since this index does not rollover, only the first
                cipslaUdpEchoTmplStatsNumDistBuckets will be kept.
                
                The last cipslaUdpEchoTmplStatsNumDistBuckets will
                contain all entries from its distribution interval
                start point to infinity.
                ''',
                'cipslaudpechotmpldistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplDistInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The statistical distribution buckets interval.
                
                Distribution Bucket Example:
                
                cipslaUdpEchoTmplDistBuckets = 5 buckets
                cipslaUdpEchoTmplDistInterval = 10 milliseconds
                
                | Bucket 1 | Bucket 2 | Bucket 3 | Bucket 4 | Bucket 5  |
                |  0-9 ms  | 10-19 ms | 20-29 ms | 30-39 ms | 40-Inf ms |
                
                Odd Example:
                
                cipslaUdpEchoTmplDistBuckets = 1 buckets
                cipslaUdpEchoTmplDistInterval = 10 milliseconds
                
                | Bucket 1  |
                |  0-Inf ms |
                
                Thus, this odd example shows that the value of
                cipslaUdpEchoTmplDistInterval does not apply when
                cipslaUdpEchoTmplDistBuckets is one.
                ''',
                'cipslaudpechotmpldistinterval',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplHistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                The maximum number of history buckets to record.
                This value should be set to the number of operations 
                to keep per lifetime.
                
                After cipslaUdpEchoTmplHistBuckets are filled, the 
                oldest entries are deleted and the most recent
                cipslaUdpEchoTmplHistBuckets buckets are retained.
                ''',
                'cipslaudpechotmplhistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplHistFilter', REFERENCE_ENUM_CLASS, 'CipslaudpechotmplhistfilterEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry.CipslaudpechotmplhistfilterEnum', 
                [], [], 
                '''                Defines a filter for adding RTT results to the history
                buffer:
                
                none(1)          - no history is recorded
                all(2)           - the results of all completion times 
                                   and failed completions are recorded
                overThreshold(3) - the results of completion times
                                   over cipslaUdpEchoTmplThreshold are 
                                   recorded.
                failures(4)      - the results of failed operations (only) 
                                   are recorded.
                ''',
                'cipslaudpechotmplhistfilter',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplHistLives', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                The maximum number of history lives to record.  A life
                is defined by the countdown (or transition) to zero 
                by the cipslaAutoGroupScheduleLife object.  A new life is
                created when the same conceptual control row is
                restarted via the transition of the 
                cipslaAutoGroupScheduleLife object and its subsequent 
                countdown.
                
                The value of zero will shut off all data collection.
                ''',
                'cipslaudpechotmplhistlives',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplReqDataSize', ATTRIBUTE, 'int' , None, None, 
                [('4', '1500')], [], 
                '''                This object represents the number of octets to be
                placed into the ARR Data portion of the request
                message, when using SNA protocols.
                
                For non-ARR protocols' RTT request/responses,
                this value represents the native payload size.
                
                REMEMBER:  The ARR Header overhead is not included
                           in this value.
                ''',
                'cipslaudpechotmplreqdatasize',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual UDP echo template control row.
                When the status is active, all the read-create objects in 
                that row can be modified.
                ''',
                'cipslaudpechotmplrowstatus',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A string which specifies the IP address of the source.
                ''',
                'cipslaudpechotmplsrcaddr',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplSrcAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                An enumerated value which specifies the IP address type
                of the source. It must be used along with the
                cipslaUdpEchoTmplSrcAddr object.
                ''',
                'cipslaudpechotmplsrcaddrtype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplSrcPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the source's port number. If this
                object is not specified, the application will get a
                port allocated by the system.
                ''',
                'cipslaudpechotmplsrcport',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplStatsHours', ATTRIBUTE, 'int' , None, None, 
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
                'cipslaudpechotmplstatshours',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslaudpechotmplstoragetype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object defines an administrative threshold limit.
                If the IP SLA operation time exceeds this limit and if the
                condition specified in cipslaUdpEchoTmplHistFilter is 
                satisfied, one threshold crossing occurrence will be counted.
                ''',
                'cipslaudpechotmplthreshold',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplTimeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800000')], [], 
                '''                Specifies the duration to wait for an IP SLA operation
                completion.
                
                For connection oriented protocols, this may cause the
                connection to be closed by the operation.  Once closed, it
                will be assumed that the connection reestablishment
                will be performed.  To prevent unwanted closure of
                connections, be sure to set this value to a realistic
                connection timeout.
                ''',
                'cipslaudpechotmpltimeout',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object represents the type of service octet in an
                IP header.
                ''',
                'cipslaudpechotmpltos',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplVerifyData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, the resulting data in each IP SLA
                operation is compared with the expected data.  This
                includes checking header information (if possible) and
                exact packet size.
                ''',
                'cipslaudpechotmplverifydata',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VRF name with
                which the IP SLA operation will be used. For regular IP SLA
                operation this field should not be configured. The agent
                will use this field to identify the VRF routing Table for
                this operation.
                ''',
                'cipslaudpechotmplvrfname',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaUdpEchoTmplEntry',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib.Cipslaudpechotmpltable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslaudpechotmpltable',
            False, 
            [
            _MetaInfoClassMember('cipslaUdpEchoTmplEntry', REFERENCE_LIST, 'Cipslaudpechotmplentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry', 
                [], [], 
                '''                A row entry representing an IPSLA UDP echo template.
                ''',
                'cipslaudpechotmplentry',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaUdpEchoTmplTable',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry.CipslatcpconntmplhistfilterEnum' : _MetaInfoEnum('CipslatcpconntmplhistfilterEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB',
        {
            'none':'none',
            'all':'all',
            'overThreshold':'overThreshold',
            'failures':'failures',
        }, 'CISCO-IPSLA-ECHO-MIB', _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB']),
    'CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry',
            False, 
            [
            _MetaInfoClassMember('cipslaTcpConnTmplName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A string which specifies the TCP connect template name.
                ''',
                'cipslatcpconntmplname',
                'CISCO-IPSLA-ECHO-MIB', True),
            _MetaInfoClassMember('cipslaTcpConnTmplControlEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is enabled, then the IP SLA application
                will send control messages to a responder, residing on the
                target router to respond to the data request packets being
                sent by the source router.
                ''',
                'cipslatcpconntmplcontrolenable',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string which provides description for the TCP connect template.
                ''',
                'cipslatcpconntmpldescription',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplDistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                The maximum number of statistical distribution
                buckets to accumulate.
                
                Since this index does not rollover, only the first
                cipslaTcpConnTmplDistBuckets will be kept.
                
                The last cipslaTcpConnTmplDistBuckets will
                contain all entries from its distribution interval
                start point to infinity.
                ''',
                'cipslatcpconntmpldistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplDistInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The statistical distribution buckets interval.
                
                Distribution Bucket Example:
                
                cipslaTcpConnTmplDistBuckets = 5 buckets
                cipslaTcpConnTmplDistInterval = 10 milliseconds
                
                | Bucket 1 | Bucket 2 | Bucket 3 | Bucket 4 | Bucket 5  |
                |  0-9 ms  | 10-19 ms | 20-29 ms | 30-39 ms | 40-Inf ms |
                
                Odd Example:
                
                cipslaTcpConnTmplDistBuckets = 1 buckets
                cipslaTcpConnTmplDistInterval = 10 milliseconds
                
                | Bucket 1  |
                |  0-Inf ms |
                
                Thus, this odd example shows that the value of
                cipslaTcpConnTmplDistInterval does not apply when
                cipslaTcpConnTmplDistBuckets is one.
                ''',
                'cipslatcpconntmpldistinterval',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplHistBuckets', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                The maximum number of history buckets to record.
                This value should be set to the number of operations 
                to keep per lifetime.
                
                After cipslaTcpConnTmplHistBuckets are filled, the 
                oldest entries are deleted and the most recent
                cipslaTcpConnTmplHistBuckets buckets are retained.
                ''',
                'cipslatcpconntmplhistbuckets',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplHistFilter', REFERENCE_ENUM_CLASS, 'CipslatcpconntmplhistfilterEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry.CipslatcpconntmplhistfilterEnum', 
                [], [], 
                '''                Defines a filter for adding RTT results to the history
                buffer:
                
                none(1)          - no history is recorded
                all(2)           - the results of all completion times 
                                   and failed completions are recorded
                overThreshold(3) - the results of completion times
                                   over cipslaTcpConnTmplThreshold are 
                                   recorded.
                failures(4)      - the results of failed operations (only) 
                                   are recorded.
                ''',
                'cipslatcpconntmplhistfilter',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplHistLives', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                The maximum number of history lives to record.  A life
                is defined by the countdown (or transition) to zero 
                by the cipslaAutoGroupScheduleLife object.  A new life is
                created when the same conceptual control row is
                restarted via the transition of the 
                cipslaAutoGroupScheduleLife object and its subsequent 
                countdown.
                
                The value of zero will shut off all data collection.
                ''',
                'cipslatcpconntmplhistlives',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual tcp connect control row.
                When the status is active, all the read-create objects 
                in that row can be modified.
                ''',
                'cipslatcpconntmplrowstatus',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A string which specifies the IP address of the source.
                ''',
                'cipslatcpconntmplsrcaddr',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplSrcAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                An enumerated value which specifies the IP address type
                of the source. It must be used along with the
                cipslaTcpConnTmplSrcAddr object.
                ''',
                'cipslatcpconntmplsrcaddrtype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplSrcPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the source's port number. If this
                object is not specified, the application will get a
                port allocated by the system.
                ''',
                'cipslatcpconntmplsrcport',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplStatsHours', ATTRIBUTE, 'int' , None, None, 
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
                'cipslatcpconntmplstatshours',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslatcpconntmplstoragetype',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object defines an administrative threshold limit.
                If the IP SLA operation time exceeds this limit and if the
                condition specified in cipslaTcpConnTmplHistFilter is 
                satisfied, one threshold crossing occurrence will be counted.
                ''',
                'cipslatcpconntmplthreshold',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplTimeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800000')], [], 
                '''                Specifies the duration to wait for an IP SLA operation
                completion.
                
                For connection oriented protocols, this may cause the
                connection to be closed by the operation.  Once closed, it
                will be assumed that the connection reestablishment
                will be performed.  To prevent unwanted closure of
                connections, be sure to set this value to a realistic
                connection timeout.
                ''',
                'cipslatcpconntmpltimeout',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object represents the type of service octet in an
                IP header.
                ''',
                'cipslatcpconntmpltos',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplVerifyData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, the resulting data in each IP SLA
                operation is compared with the expected data.  This
                includes checking header information (if possible) and
                exact packet size.
                ''',
                'cipslatcpconntmplverifydata',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaTcpConnTmplEntry',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib.Cipslatcpconntmpltable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib.Cipslatcpconntmpltable',
            False, 
            [
            _MetaInfoClassMember('cipslaTcpConnTmplEntry', REFERENCE_LIST, 'Cipslatcpconntmplentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry', 
                [], [], 
                '''                A row entry representing an IPSLA TCP connect template.
                ''',
                'cipslatcpconntmplentry',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'cipslaTcpConnTmplTable',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
    'CiscoIpslaEchoMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaEchoMib',
            False, 
            [
            _MetaInfoClassMember('cipslaIcmpEchoTmplTable', REFERENCE_CLASS, 'Cipslaicmpechotmpltable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaicmpechotmpltable', 
                [], [], 
                '''                A table that contains ICMP echo template definitions.
                ''',
                'cipslaicmpechotmpltable',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaTcpConnTmplTable', REFERENCE_CLASS, 'Cipslatcpconntmpltable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslatcpconntmpltable', 
                [], [], 
                '''                A table that contains TCP connect template specific definitions.
                ''',
                'cipslatcpconntmpltable',
                'CISCO-IPSLA-ECHO-MIB', False),
            _MetaInfoClassMember('cipslaUdpEchoTmplTable', REFERENCE_CLASS, 'Cipslaudpechotmpltable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB', 'CiscoIpslaEchoMib.Cipslaudpechotmpltable', 
                [], [], 
                '''                A table that contains UDP echo template specific definitions.
                ''',
                'cipslaudpechotmpltable',
                'CISCO-IPSLA-ECHO-MIB', False),
            ],
            'CISCO-IPSLA-ECHO-MIB',
            'CISCO-IPSLA-ECHO-MIB',
            _yang_ns._namespaces['CISCO-IPSLA-ECHO-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_ECHO_MIB'
        ),
    },
}
_meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable.Cipslaicmpechotmplentry']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable']['meta_info']
_meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable.Cipslaudpechotmplentry']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable']['meta_info']
_meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable.Cipslatcpconntmplentry']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable']['meta_info']
_meta_table['CiscoIpslaEchoMib.Cipslaicmpechotmpltable']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib']['meta_info']
_meta_table['CiscoIpslaEchoMib.Cipslaudpechotmpltable']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib']['meta_info']
_meta_table['CiscoIpslaEchoMib.Cipslatcpconntmpltable']['meta_info'].parent =_meta_table['CiscoIpslaEchoMib']['meta_info']
