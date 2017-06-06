


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A group name which is used by a management application
                to identify the group.
                ''',
                'cipslaautogroupname',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupADDestIPAgeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                This object represents the ageout time for the discovered
                end point.  If the end point becomes inactive for the period 
                of ageout time, the end point will be removed from the 
                discovered end point list.
                
                When the value of cipslaAutoGroupDestIPADEnable is 
                'false', the value of this object has no effect.
                ''',
                'cipslaautogroupaddestipageout',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupADDestPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the destination port number
                for auto discovery use.
                ''',
                'cipslaautogroupaddestport',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupADMeasureRetry', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                This object specifies number of measurement retries to
                be attempted for the discovered end point after the 
                connection to the end point is broken. If there is no 
                re-registration message received, the end point will be 
                in inactive state.
                
                When the value of cipslaAutoGroupDestIPADEnable is 
                'false', the value of this object has no effect.
                ''',
                'cipslaautogroupadmeasureretry',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This field is used to provide description for the group.
                ''',
                'cipslaautogroupdescription',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupDestinationName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object refers to the cipslaAutoGroupDestName
                in cipslaAutoGroupDestTable. If the name entered 
                is not present in cipslaAutoGroupDestTable, then when 
                group is scheduled, no ip sla operations will be created.
                ''',
                'cipslaautogroupdestinationname',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupDestIPADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When this object is set to true, destination IP address
                is populated through auto-discovery.
                ''',
                'cipslaautogroupdestipadenable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupOperTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                A string which is used by a management application to
                identify the template which is associated with the group.
                Depends on cipslaAutoGroupOperType, this object refers to
                cipslaIcmpEchoTmplName in cipslaIcmpEchoTmplTable, or
                cipslaUdpEchoTmplName in cipslaUdpEchoTmplTable, or
                cipslaTcpConnTmplName in cipslaTcpConnTmplTable, or
                cipslaIcmpJitterTmplName in cipslaIcmpJitterTmplTable, or
                ciscoIpSlaUdpJitterTmplName in ciscoIpSlaUdpJitterTmplTable.
                ''',
                'cipslaautogroupopertemplatename',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupOperType', REFERENCE_ENUM_CLASS, 'IpslaopertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB', 'IpslaopertypeEnum', 
                [], [], 
                '''                This object specifies the type of IP SLA operation.
                When operation type is not ICMP jitter, then 
                cipslaAutoGroupOperTemplateName must be specified.
                ''',
                'cipslaautogroupopertype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupQoSEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When this object is set to true, QoS is enabled for this
                group and this group is linked to policy map. The 
                restriction is that after QoS is enabled, it can not be 
                disabled for this group.
                ''',
                'cipslaautogroupqosenable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual group control row.
                
                When the status is active, the other writable objects
                may be modified unless the scheduler with name 
                specified by cipslaAutoGroupSchedulerId is scheduled.
                ''',
                'cipslaautogrouprowstatus',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedulerId', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object refers to the cipslaAutoGroupSchedId in
                cipslaAutoGroupSchedTable, and is used to schedule 
                this group.
                ''',
                'cipslaautogroupschedulerid',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'cipslaautogroupstoragetype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupEntry',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslaautogrouptable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogrouptable',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupEntry', REFERENCE_LIST, 'Cipslaautogroupentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry', 
                [], [], 
                '''                An entry containing the configurations for a particular
                auto measure group.
                ''',
                'cipslaautogroupentry',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupTable',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupDestName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This is the name for an auto measure group destination.
                ''',
                'cipslaautogroupdestname',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupDestIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of the internet address of a destination
                for an auto measure group.
                ''',
                'cipslaautogroupdestipaddrtype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupDestIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The internet address of a destination for an auto
                measure group. The type of this address is determined
                by the value of cipslaAutoGroupDestIpAddrType.
                ''',
                'cipslaautogroupdestipaddr',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupDestPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the destination port number.
                For ICMP echo and ICMP jitter, the suggested value is 
                '0'.
                ''',
                'cipslaautogroupdestport',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupDestRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual destination table control row.
                No other objects in this row need to be set before this object
                can become active.
                
                During 'destroy', when cipslaAutoGroupDestIpAddr is specified 
                as '0.0.0.0' and cipslaAutoGroupDestPort is specified as '0', 
                then all the rows with same cipslaAutoGroupDestName will be 
                deleted.
                ''',
                'cipslaautogroupdestrowstatus',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupDestStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                
                By default the entry will be saved into non-volatile
                memory.
                ''',
                'cipslaautogroupdeststoragetype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupDestEntry',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupDestEntry', REFERENCE_LIST, 'Cipslaautogroupdestentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry', 
                [], [], 
                '''                An entry containing the destination IP addresses
                and port configurations associated to auto measure
                group destination name.
                ''',
                'cipslaautogroupdestentry',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupDestTable',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactactiontypeEnum' : _MetaInfoEnum('CipslareactactiontypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB',
        {
            'none':'none',
            'notificationOnly':'notificationOnly',
        }, 'CISCO-IPSLA-AUTOMEASURE-MIB', _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB']),
    'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactthresholdtypeEnum' : _MetaInfoEnum('CipslareactthresholdtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB',
        {
            'never':'never',
            'immediate':'immediate',
            'consecutive':'consecutive',
            'xOfy':'xOfy',
            'average':'average',
        }, 'CISCO-IPSLA-AUTOMEASURE-MIB', _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB']),
    'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupOperType', REFERENCE_ENUM_CLASS, 'IpslaopertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB', 'IpslaopertypeEnum', 
                [], [], 
                '''                ''',
                'cipslaautogroupopertype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaReactConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object along with cipslaAutoGroupOperType and
                cipslaAutoGroupOperTemplateName identifies
                a particular reaction-configuration for one IP SLA 
                template.
                
                This number is persistent across reboots.
                ''',
                'cipslareactconfigindex',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupOperTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                ''',
                'cipslaautogroupopertemplatename',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaReactActionType', REFERENCE_ENUM_CLASS, 'CipslareactactiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactactiontypeEnum', 
                [], [], 
                '''                Specifies what type, if any, of reaction to
                generate if one of the watched
                (reaction-configuration ) conditions is satisfied:
                
                none(1)                - no reaction is generated
                notificationOnly(2)    - a notification is generated
                ''',
                'cipslareactactiontype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This objects indicates the status of the conceptual
                Reaction Control Row. 
                
                When this object moves to active state, the conceptual row 
                is monitored and notifications are generated when threshold 
                violation takes place.
                
                In order for this object to become active cipslaReactVar must
                be defined. All other objects assume default values.  When the 
                status is active, the following objects in that row can be 
                modified.
                 cipslaReactThresholdType,
                 cipslaReactActionType,
                 cipslaReactThresholdRising,
                 cipslaReactThresholdFalling,
                 cipslaReactThresholdCountX,
                 cipslaReactThresholdCountY,
                 cipslaReactStorageType
                
                This object can be set to 'destroy' from any value at any time.
                When this object is set to 'destroy' no reaction configuration
                would exist. The reaction configuration for the template is 
                removed.
                ''',
                'cipslareactrowstatus',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                
                By default the entry will be saved into non-volatile
                memory.
                ''',
                'cipslareactstoragetype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactThresholdCountX', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                If cipslaReactThresholdType value is 'xOfy', this object
                defines the 'x' value.
                
                If cipslaReactThresholdType value is 'consecutive'
                this object defines the number of consecutive occurrences
                that needs threshold violation before setting 
                cipslaReactOccurred as true.
                
                If cipslaReactThresholdType value is 'average' this object
                defines the number of samples that needs be considered for
                calculating average.
                
                This object has no meaning if cipslaReactThresholdType has
                value of 'never' and 'immediate'.
                ''',
                'cipslareactthresholdcountx',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactThresholdCountY', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                This object defines the 'y' value of the xOfy condition
                if cipslaReactThresholdType is 'xOfy'. The default for the 
                'y' value is 5.
                
                For other values of cipslaReactThresholdType, this object
                is not applicable.
                ''',
                'cipslareactthresholdcounty',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactThresholdFalling', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object defines a lower threshold limit. If the
                value ( e.g rtt, jitterAvg, packetLossSD etc ) falls
                below this limit and if the condition specified in
                cipslaReactThresholdType is satisfied, a notification 
                is generated. This object value can not bigger than
                cipslaReactThresholdRising value.
                
                Default value of cipslaReactThresholdFalling
                   'rtt' is 3000
                   'jitterAvg' is 100.
                   'jitterSDAvg' is 100.
                   'jitterDSAvg' 100.
                   'packetLossSD' is 10000.
                   'packetLossDS' is 10000.
                   'mos' is 500.
                   'icpif' is 93.
                   'packetMIA' is 10000.
                   'packetLateArrival' is 10000.
                   'packetOutOfSequence' is 10000.
                   'maxOfPositiveSD' is 10000.
                   'maxOfNegativeSD' is 10000.
                   'maxOfPositiveDS' is 10000.
                   'maxOfNegativeDS' is 10000.
                   'successivePacketLoss' is 1000.
                   'maxOfLatencyDS' is 3000.
                   'maxOfLatencySD' is 3000.
                   'latencyDSAvg' is 3000.
                   'latencySDAvg' is 3000.
                   'packetLoss' is 10000.
                
                This object is not applicable if the cipslaReactVar is
                'timeout', 'connectionLoss' or 'verifyError'. For 'timeout',
                'connectionLoss' and 'verifyError', default value of
                cipslaReactThresholdFalling will be 0.
                ''',
                'cipslareactthresholdfalling',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactThresholdRising', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object defines the higher threshold limit.
                If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises
                above this limit and if the condition specified in
                cipslaReactThresholdType is satisfied, a notification is 
                generated.
                
                Default value of cipslaReactThresholdRising for
                   'rtt' is 5000
                   'jitterAvg' is 100.
                   'jitterSDAvg' is 100.
                   'jitterDSAvg' 100.
                   'packetLossSD' is 10000.
                   'packetLossDS' is 10000.
                   'mos' is 500.
                   'icpif' is 93.
                   'packetMIA' is 10000.
                   'packetLateArrival' is 10000.
                   'packetOutOfSequence' is 10000.
                   'maxOfPositiveSD' is 10000.
                   'maxOfNegativeSD' is 10000.
                   'maxOfPositiveDS' is 10000.
                   'maxOfNegativeDS' is 10000.
                   'successivePacketLoss' is 1000.
                   'maxOfLatencyDS' is 5000.
                   'maxOfLatencySD' is 5000.
                   'latencyDSAvg' is 5000.
                   'latencySDAvg' is 5000.
                   'packetLoss' is 10000.
                
                This object is not applicable if the cipslaReactVar is
                'timeout', 'connectionLoss' or 'verifyError'. For 'timeout',
                'connectionLoss' and 'verifyError' default value of 
                cipslaReactThresholdRising will be 0.
                ''',
                'cipslareactthresholdrising',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactThresholdType', REFERENCE_ENUM_CLASS, 'CipslareactthresholdtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.CipslareactthresholdtypeEnum', 
                [], [], 
                '''                This object specifies the conditions under which
                a notification ( trap ) is sent. The rttMonReactOccurred
                object defined in rttMonReactTable in CISCO-RTTMON-MIB will
                change accordingly:
                
                never(1)       - rttMonReactOccurred is never set
                
                immediate(2)   - rttMonReactOccurred is set to 'true' when the
                                 value of parameter for which reaction is
                                 configured ( e.g rtt, jitterAvg, packetLossSD,
                                 mos etc ) violates the threshold.
                                 Conversely, rttMonReactOccurred is set to 'false'
                                 when the parameter ( e.g rtt, jitterAvg,
                                 packetLossSD, mos etc ) is below the threshold
                                 limits.
                
                consecutive(3) - rttMonReactOccurred is set to true when the value
                                 of parameter for which reaction is configured
                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )
                                 violates the threshold for configured consecutive
                                 times.
                                 Conversely, rttMonReactOccurred is set to false
                                 when the value of parameter ( e.g rtt, jitterAvg
                                 packetLossSD, mos etc ) is below the threshold
                                 limits for the same number of consecutive
                                 operations.
                
                xOfy(4)        - rttMonReactOccurred is set to true when x
                                 ( as specified by cipslaReactThresholdCountX )
                                 out of the last y ( as specified by
                                 cipslaReacthresholdCountY ) times the value of
                                 parameter for which the reaction is configured
                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )
                                 violates the threshold.
                                 Conversely, it is set to false when x, out of the
                                 last y times the value of parameter
                                 ( e.g rtt, jitterAvg, packetLossSD, mos ) is
                                 below the threshold limits.
                                 NOTE: If x > y, this will never
                                      generate a reaction.
                
                average(5)    - rttMonReactOccurred is set to true when the
                                average ( cipslaReactThresholdCountX times )
                                value of parameter for which reaction is 
                                configured ( e.g rtt, jitterAvg, packetLossSD,
                                mos etc ) violates the threshold condition.
                                Conversely, it is set to false when the
                                average value of parameter ( e.g rtt, jitterAvg,
                                packetLossSD, mos etc ) is below the threshold
                                limits.
                
                If this value is changed by a management station,
                rttMonReactOccurred is set to false, but
                no reaction is generated if the prior value of
                rttMonReactOccurred was true.
                ''',
                'cipslareactthresholdtype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactVar', REFERENCE_ENUM_CLASS, 'IpslareactvarEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB', 'IpslareactvarEnum', 
                [], [], 
                '''                This object specifies the type of reaction configured for an
                IP SLA template. Default value is 'rtt' for ICMP echo, UDP echo
                and TCP connect. Default value is 'jitterAvg' for UDP jitter and 
                ICMP jitter.
                
                The reaction types 'rtt', 'timeout', 'connectionLoss' and
                'verifyError' can be configured for all template types.
                
                The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg', 
                'packetLateArrival', 'packetOutOfSequence', 
                'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS'
                'maxOfNegativeDS', 'mos' and 'icpif' can be configured for 
                UDP jitter and ICMP jitter types only.
                
                The reaction types 'packetLossDS', 'packetLossSD' and 
                'packetMIA' can be configured for UDP jitter type only.
                
                The reaction types 'successivePacketLoss', 'maxOfLatencyDS', 
                'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and 
                'packetLoss' can be configured for ICMP jitter type only.
                ''',
                'cipslareactvar',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaReactEntry',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslareacttable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslareacttable',
            False, 
            [
            _MetaInfoClassMember('cipslaReactEntry', REFERENCE_LIST, 'Cipslareactentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry', 
                [], [], 
                '''                A base list of objects that define a conceptual reaction
                configuration control row.
                ''',
                'cipslareactentry',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaReactTable',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupSchedId', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This string uniquely identifies a row in the
                cipslaAutoGroupSchedTable.
                ''',
                'cipslaautogroupschedid',
                'CISCO-IPSLA-AUTOMEASURE-MIB', True),
            _MetaInfoClassMember('cipslaAutoGroupSchedAgeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '2073600')], [], 
                '''                This object specifies the ageout value of the operations that are
                getting group scheduled. This value will be placed into
                rttMonSchedAdminConceptRowAgeout object for each of the
                operations in the group when this conceptual control row becomes 
                'active'.
                
                When this value is set to zero, the operations will never ageout.
                ''',
                'cipslaautogroupschedageout',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specifies the duration between initiating each RTT
                operation for one IP SLA operation generated via the auto 
                measure group.
                
                The value of this object is only effective when both
                cipslaAutoGroupSchedMaxInterval and 
                cipslaAutoGroupSchedMinInterval have zero values.
                ''',
                'cipslaautogroupschedinterval',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedLife', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object specifies the life of all the operations that are
                getting group scheduled. This value will be placed into
                cipslaAutoGroupSchedRttLife object when this conceptual control
                row becomes 'active'.
                
                The value 2147483647 has a special meaning. When this object is
                set to 2147483647, the rttMonCtrlOperRttLife object for all the
                operations will not decrement, and thus the life time of the 
                operation will never end.
                ''',
                'cipslaautogroupschedlife',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedMaxInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specifies the max duration between initiating each RTT
                operation for one IP SLA operation in the group.
                ''',
                'cipslaautogroupschedmaxinterval',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedMinInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specifies the min duration between initiating each RTT
                operation for one IP SLA operation in the group.
                
                The value of this object should be lower than the value of
                cipslaAutoGroupSchedMaxInterval.
                ''',
                'cipslaautogroupschedmininterval',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedPeriod', ATTRIBUTE, 'int' , None, None, 
                [('100', '99000')], [], 
                '''                Specifies the time duration between initiating two
                IP SLA operations generated via the auto measure group.
                ''',
                'cipslaautogroupschedperiod',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the conceptual group schedule control row.
                
                When the status is active and the value of 
                cipslaAutoGroupSchedStartTime is '1', the other writable 
                objects may be modified.
                
                This object can be set to 'destroy' from any value at any time.
                When this object is set to 'destroy' it will stop all the 
                operations which had been group scheduled by it earlier, 
                before destroying the group schedule control row.
                ''',
                'cipslaautogroupschedrowstatus',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedStartTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                This is the time in seconds after which the operations of
                the associated groups  will take transition to active state.
                When set to the value other than '1' (pending), then all 
                objects in this row cannot be modified.
                ''',
                'cipslaautogroupschedstarttime',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                
                By default the entry will be saved into non-volatile
                memory.
                ''',
                'cipslaautogroupschedstoragetype',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupSchedEntry',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupSchedEntry', REFERENCE_LIST, 'Cipslaautogroupschedentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry', 
                [], [], 
                '''                A list of objects that define specific configuration for
                group scheduling.
                ''',
                'cipslaautogroupschedentry',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'cipslaAutoGroupSchedTable',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
    'CiscoIpslaAutomeasureMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpslaAutomeasureMib',
            False, 
            [
            _MetaInfoClassMember('cipslaAutoGroupDestTable', REFERENCE_CLASS, 'Cipslaautogroupdesttable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable', 
                [], [], 
                '''                A table contains the list of destination IP
                addresses and ports associated to the auto measure
                group destination name.
                ''',
                'cipslaautogroupdesttable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupSchedTable', REFERENCE_CLASS, 'Cipslaautogroupschedtable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable', 
                [], [], 
                '''                A table of group scheduling definitions.
                ''',
                'cipslaautogroupschedtable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaAutoGroupTable', REFERENCE_CLASS, 'Cipslaautogrouptable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslaautogrouptable', 
                [], [], 
                '''                A table that contains IP SLA auto measure group definitions.
                ''',
                'cipslaautogrouptable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            _MetaInfoClassMember('cipslaReactTable', REFERENCE_CLASS, 'Cipslareacttable' , 'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB', 'CiscoIpslaAutomeasureMib.Cipslareacttable', 
                [], [], 
                '''                A table that contains reaction configurations for templates.
                Each conceptual row in cipslaReactTable corresponds 
                to a reaction configured for one template.
                
                Each template can have multiple reactions and hence there can be 
                multiple rows for a particular template. Different template
                types can have different reactions. The reaction type is 
                specified as cipslaReactVar based upon template type as some 
                reaction types are applicable just for specific template types.
                ''',
                'cipslareacttable',
                'CISCO-IPSLA-AUTOMEASURE-MIB', False),
            ],
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            'CISCO-IPSLA-AUTOMEASURE-MIB',
            _yang_ns._namespaces['CISCO-IPSLA-AUTOMEASURE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB'
        ),
    },
}
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogrouptable']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogrouptable']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslareacttable']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib']['meta_info']
_meta_table['CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable']['meta_info'].parent =_meta_table['CiscoIpslaAutomeasureMib']['meta_info']
