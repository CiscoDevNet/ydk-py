


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'QosinterfacequeuetypeEnum' : _MetaInfoEnum('QosinterfacequeuetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'oneQ1t':'oneQ1t',
            'oneQ2t':'oneQ2t',
            'oneQ4t':'oneQ4t',
            'oneQ8t':'oneQ8t',
            'twoQ1t':'twoQ1t',
            'twoQ2t':'twoQ2t',
            'twoQ4t':'twoQ4t',
            'twoQ8t':'twoQ8t',
            'threeQ1t':'threeQ1t',
            'threeQ2t':'threeQ2t',
            'threeQ4t':'threeQ4t',
            'threeQ8t':'threeQ8t',
            'fourQ1t':'fourQ1t',
            'fourQ2t':'fourQ2t',
            'fourQ4t':'fourQ4t',
            'fourQ8t':'fourQ8t',
            'eightQ1t':'eightQ1t',
            'eightQ2t':'eightQ2t',
            'eightQ4t':'eightQ4t',
            'eightQ8t':'eightQ8t',
            'sixteenQ1t':'sixteenQ1t',
            'sixteenQ2t':'sixteenQ2t',
            'sixteenQ4t':'sixteenQ4t',
            'sixtyfourQ1t':'sixtyfourQ1t',
            'sixtyfourQ2t':'sixtyfourQ2t',
            'sixtyfourQ4t':'sixtyfourQ4t',
            'oneP1Q0t':'oneP1Q0t',
            'oneP1Q4t':'oneP1Q4t',
            'oneP1Q8t':'oneP1Q8t',
            'oneP2Q1t':'oneP2Q1t',
            'oneP2Q2t':'oneP2Q2t',
            'oneP3Q1t':'oneP3Q1t',
            'oneP7Q8t':'oneP7Q8t',
            'oneP3Q8t':'oneP3Q8t',
            'sixteenQ8t':'sixteenQ8t',
            'oneP15Q8t':'oneP15Q8t',
            'oneP15Q1t':'oneP15Q1t',
            'oneP7Q1t':'oneP7Q1t',
            'oneP31Q1t':'oneP31Q1t',
            'thirtytwoQ1t':'thirtytwoQ1t',
            'thirtytwoQ8t':'thirtytwoQ8t',
            'oneP31Q8t':'oneP31Q8t',
            'oneP7Q4t':'oneP7Q4t',
            'oneP3Q4t':'oneP3Q4t',
            'oneP7Q2t':'oneP7Q2t',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'ThresholdsetrangeEnum' : _MetaInfoEnum('ThresholdsetrangeEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'zeroT':'zeroT',
            'oneT':'oneT',
            'twoT':'twoT',
            'fourT':'fourT',
            'eightT':'eightT',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'QueuerangeEnum' : _MetaInfoEnum('QueuerangeEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'oneQ':'oneQ',
            'twoQ':'twoQ',
            'threeQ':'threeQ',
            'fourQ':'fourQ',
            'eightQ':'eightQ',
            'sixteenQ':'sixteenQ',
            'thirtyTwoQ':'thirtyTwoQ',
            'sixtyFourQ':'sixtyFourQ',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry',
            False, 
            [
            _MetaInfoClassMember('qosDeviceIncarnationId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosdeviceincarnationid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDevicePdpName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the PDP that installed the current incarnation of
                the PIB into the device.  By default it is the zero length
                string.
                ''',
                'qosdevicepdpname',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePibIncarnation', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                An octet string to identify the current incarnation.  It has
                meaning to the PDP that installed the PIB and perhaps its
                standby PDPs. By default the empty string.
                ''',
                'qosdevicepibincarnation',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePibTtl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of seconds after a client close or TCP timeout for
                which the PEP continues to enforce the policy in the PIB.
                After this interval, the PIB is consired expired and the
                device no longer enforces the policy installed in the PIB.
                ''',
                'qosdevicepibttl',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDevicePibIncarnationEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosdevicepibincarnationtable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdevicepibincarnationtable',
            False, 
            [
            _MetaInfoClassMember('qosDevicePibIncarnationEntry', REFERENCE_LIST, 'Qosdevicepibincarnationentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry', 
                [], [], 
                '''                The single policy instance of this class identifies the
                current incarnation of the PIB and the PDP that installed
                this incarnation.
                ''',
                'qosdevicepibincarnationentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDevicePibIncarnationTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry',
            False, 
            [
            _MetaInfoClassMember('qosDeviceAttributeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosdeviceattributeid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDeviceCapabilities', REFERENCE_BITS, 'Qosdevicecapabilities' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry.Qosdevicecapabilities', 
                [], [], 
                '''                An enumeration of device capabilities.  Used by the PDP to
                select policies and configuration to push to the PEP.
                ''',
                'qosdevicecapabilities',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceMaxMessageSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum size message that this PEP is capable of
                receiving in bytes.  A value of zero means that the maximum
                message size is unspecified (but does not mean it is
                unlimited).  A message greater than this maximum results in a
                MessageTooBig error on a 'no commit' REP.
                ''',
                'qosdevicemaxmessagesize',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePepDomain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The QoS domain that this device belongs to.  This is
                configured locally on the device (perhaps by some management
                protocol such as SNMP).  By default, it is the zero-length
                string.
                ''',
                'qosdevicepepdomain',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePrimaryPdp', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the PDP configured to be the primary PDP for
                the device.
                ''',
                'qosdeviceprimarypdp',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceSecondaryPdp', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the PDP configured to be the secondary PDP for
                the device.  An address of zero indicates no secondary is
                configured.
                ''',
                'qosdevicesecondarypdp',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDeviceAttributeEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosdeviceattributetable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdeviceattributetable',
            False, 
            [
            _MetaInfoClassMember('qosDeviceAttributeEntry', REFERENCE_LIST, 'Qosdeviceattributeentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry', 
                [], [], 
                '''                The single instance of this class indicates specific
                attributes of the device.
                ''',
                'qosdeviceattributeentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDeviceAttributeTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry',
            False, 
            [
            _MetaInfoClassMember('qosInterfaceTypeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosinterfacetypeid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosInterfaceQueueType', REFERENCE_ENUM_CLASS, 'QosinterfacequeuetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'QosinterfacequeuetypeEnum', 
                [], [], 
                '''                The interface type in terms of number of queues and
                thresholds.
                ''',
                'qosinterfacequeuetype',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosInterfaceTypeCapabilities', REFERENCE_BITS, 'Qosinterfacetypecapabilities' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'Qosinterfacetypecapabilities', 
                [], [], 
                '''                An enumeration of interface capabilities.  Used by the PDP to
                select policies and configuration to push to the PEP.
                ''',
                'qosinterfacetypecapabilities',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosInterfaceTypeRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A combination of roles on at least one interface of type
                qosInterfaceType.
                ''',
                'qosinterfacetyperoles',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosInterfaceTypeEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosinterfacetypetable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosinterfacetypetable',
            False, 
            [
            _MetaInfoClassMember('qosInterfaceTypeEntry', REFERENCE_LIST, 'Qosinterfacetypeentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry', 
                [], [], 
                '''                An instance of this class describes a role combination for
                an interface type of an interface that exists on the device.
                ''',
                'qosinterfacetypeentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosInterfaceTypeTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry',
            False, 
            [
            _MetaInfoClassMember('qosDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                A DSCP for which this entry contains mappings.
                ''',
                'qosdscp',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosL2Cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The L2 CoS value to use when mapping this DSCP to layer 2
                CoS.
                ''',
                'qosl2cos',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosMarkedDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP to use instead of the qosDscp when the packet is out
                of profile and hence marked as such.
                ''',
                'qosmarkeddscp',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDiffServMappingEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosdiffservmappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosdiffservmappingtable',
            False, 
            [
            _MetaInfoClassMember('qosDiffServMappingEntry', REFERENCE_LIST, 'Qosdiffservmappingentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry', 
                [], [], 
                '''                An instance of this class represents mappings from a DSCP.
                ''',
                'qosdiffservmappingentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDiffServMappingTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry',
            False, 
            [
            _MetaInfoClassMember('qosCosToDscpCos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The L2 CoS value that is being mapped.
                ''',
                'qoscostodscpcos',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosCosToDscpDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value to use when mapping the L2 CoS to a DSCP.
                ''',
                'qoscostodscpdscp',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosCosToDscpEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qoscostodscptable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qoscostodscptable',
            False, 
            [
            _MetaInfoClassMember('qosCosToDscpEntry', REFERENCE_LIST, 'Qoscostodscpentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry', 
                [], [], 
                '''                An instance of this class maps a CoS value to a DSCP.
                ''',
                'qoscostodscpentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosCosToDscpTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.QosunmatchedpolicydirectionEnum' : _MetaInfoEnum('QosunmatchedpolicydirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'in':'in_',
            'out':'out',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry',
            False, 
            [
            _MetaInfoClassMember('qosUnmatchedPolicyId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosunmatchedpolicyid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosUnmatchedPolicyAggregateId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index identifying the aggregate that the packet belongs
                to.  It must correspond to the integer index of an instance of
                class qosAggregateTable or be zero.  If zero, the microflow
                does not belong to any aggregate and is not policed as part of
                any aggregate.
                ''',
                'qosunmatchedpolicyaggregateid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyDirection', REFERENCE_ENUM_CLASS, 'QosunmatchedpolicydirectionEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry.QosunmatchedpolicydirectionEnum', 
                [], [], 
                '''                The direction of packet flow at the interface in question to
                which this instance applies.
                ''',
                'qosunmatchedpolicydirection',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP to classify the unmatched packet with.  This must be
                specified even if qosUnmatchedPolicyDscpTrusted is true.
                ''',
                'qosunmatchedpolicydscp',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyDscpTrusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this attribute is true, then the Dscp associated with the
                packet is trusted, i.e., it is assumed to have already been
                set.  In this case, the Dscp is not rewritten with
                qosUnmatchedPolicyDscp (qosUnmatchedPolicyDscp is ignored)
                unless this is a non-IP packet and arrives untagged.  The
                packet is still policed as part of its micro flow and its
                aggregate flow.
                
                When a trusted action is applied to an input interface, the
                Dscp (for an IP packet) or CoS (for a non-IP packet)
                associated with the packet is the one contained in the packet.
                When a trusted action is applied to an output interface, the
                Dscp associated with the packet is the one that is the result
                of the input classification and policing.
                ''',
                'qosunmatchedpolicydscptrusted',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyRole', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Role combination for which this instance applies.
                ''',
                'qosunmatchedpolicyrole',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchPolMicroFlowPolicerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index identifying the instance of policer to apply to
                unmatched packets.  It must correspond to the integer index of
                an instance of class qosPolicerTable or be zero.  If zero, the
                microflow is not policed.
                ''',
                'qosunmatchpolmicroflowpolicerid',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosUnmatchedPolicyEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosunmatchedpolicytable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosunmatchedpolicytable',
            False, 
            [
            _MetaInfoClassMember('qosUnmatchedPolicyEntry', REFERENCE_LIST, 'Qosunmatchedpolicyentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry', 
                [], [], 
                '''                An instance of this class specifies the unmatched policy
                for a particular role combination for incoming or outgoing
                traffic.
                ''',
                'qosunmatchedpolicyentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosUnmatchedPolicyTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qospolicertable.Qospolicerentry.QospoliceractionEnum' : _MetaInfoEnum('QospoliceractionEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'drop':'drop',
            'mark':'mark',
            'shape':'shape',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qospolicertable.Qospolicerentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qospolicertable.Qospolicerentry',
            False, 
            [
            _MetaInfoClassMember('qosPolicerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qospolicerid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosPolicerAction', REFERENCE_ENUM_CLASS, 'QospoliceractionEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qospolicertable.Qospolicerentry.QospoliceractionEnum', 
                [], [], 
                '''                An indication of how to handle out of profile packets.  When
                the shape action is chosen then traffic is shaped to the rate
                specified by qosPolicerRate.
                ''',
                'qospoliceraction',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerExcessBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The excess size of a burst in terms of bits.
                ''',
                'qospolicerexcessburst',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerNormalBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The normal size of a burst in terms of bits.
                ''',
                'qospolicernormalburst',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The token rate.  It is specified in units of bit/s. A rate of
                zero means that all packets will be out of profile.  If the
                qosPolicerAction is set to drop then this effectively
                denies any service to packets policed by this policer.
                ''',
                'qospolicerrate',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosPolicerEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qospolicertable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qospolicertable',
            False, 
            [
            _MetaInfoClassMember('qosPolicerEntry', REFERENCE_LIST, 'Qospolicerentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qospolicertable.Qospolicerentry', 
                [], [], 
                '''                An instance of this class specifies a set of policing
                parameters.
                ''',
                'qospolicerentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosPolicerTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry',
            False, 
            [
            _MetaInfoClassMember('qosAggregateId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosaggregateid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosAggregatePolicerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index identifying the instance of policer to apply to the
                aggregate.  It must correspond to the integer index of an
                instance of class qosPolicerTable.
                ''',
                'qosaggregatepolicerid',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosAggregateEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosaggregatetable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosaggregatetable',
            False, 
            [
            _MetaInfoClassMember('qosAggregateEntry', REFERENCE_LIST, 'Qosaggregateentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry', 
                [], [], 
                '''                An instance of this class specifies the policer to apply to
                an aggregate flow.
                ''',
                'qosaggregateentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosAggregateTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry',
            False, 
            [
            _MetaInfoClassMember('qosMacClassificationId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosmacclassificationid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDstMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address of the L2 frame.
                ''',
                'qosdstmacaddress',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDstMacCos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The CoS to assign the packet with the associated MAC/VLAN
                tuple.  Note that this CoS is overridden by the policies to
                classify the frame at layer 3 if there are any.
                ''',
                'qosdstmaccos',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDstMacVlan', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                The VLAN of the destination MAC address of the L2 frame.
                ''',
                'qosdstmacvlan',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosMacClassificationEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosmacclassificationtable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosmacclassificationtable',
            False, 
            [
            _MetaInfoClassMember('qosMacClassificationEntry', REFERENCE_LIST, 'Qosmacclassificationentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry', 
                [], [], 
                '''                An instance of this class specifies the mapping of a VLAN
                and a MAC address to a CoS value.
                ''',
                'qosmacclassificationentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosMacClassificationTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipacetable.Qosipaceentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipacetable.Qosipaceentry',
            False, 
            [
            _MetaInfoClassMember('qosIpAceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipaceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAceDscpMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The maximum value that the DSCP in the packet can have and
                match this ACE.
                ''',
                'qosipacedscpmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDscpMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The minimum value that the DSCP in the packet can have and
                match this ACE.
                ''',
                'qosipacedscpmin',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address to match against the packet's destination IP
                address.
                ''',
                'qosipacedstaddr',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstAddrMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A mask for the matching of the destination IP address.
                ''',
                'qosipacedstaddrmask',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the packet's layer 4 dest port number
                can have and match this ACE.
                ''',
                'qosipacedstl4portmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the packet's layer 4 dest port number
                can have and match this ACE.
                ''',
                'qosipacedstl4portmin',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAcePermit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the packet matches this ACE and the value of this attribute
                is true, then the matching process terminates and the QoS
                associated with this ACE (indirectly through the ACL) is
                applied to the packet.  If the value of this attribute is false,
                then no more ACEs in this ACL are compared to this packet and
                matching continues with the first ACE of the next ACL.
                ''',
                'qosipacepermit',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceProtocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The IP protocol to match against the packet's protocol.
                A value of zero means match all.
                ''',
                'qosipaceprotocol',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address to match against the packet's source IP
                address.
                ''',
                'qosipacesrcaddr',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcAddrMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A mask for the matching of the source IP address.
                ''',
                'qosipacesrcaddrmask',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the packet's layer 4 source port
                number can have and match this ACE.
                ''',
                'qosipacesrcl4portmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the packet's layer 4 source port
                number can have and match this ACE.
                ''',
                'qosipacesrcl4portmin',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAceEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipacetable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipacetable',
            False, 
            [
            _MetaInfoClassMember('qosIpAceEntry', REFERENCE_LIST, 'Qosipaceentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipacetable.Qosipaceentry', 
                [], [], 
                '''                An instance of this class specifies an ACE.
                ''',
                'qosipaceentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAceTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry',
            False, 
            [
            _MetaInfoClassMember('qosIpAclDefinitionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipacldefinitionid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAceOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer that determines the position of this ACE in the ACL.
                An ACE with a given order is positioned in the access contol
                list before one with a higher order.
                ''',
                'qosipaceorder',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDefAceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This attribute specifies the ACE in the qosIpAceTable that is
                in the ACL specified by qosIpAclId at the position specified
                by qosIpAceOrder.
                ''',
                'qosipacldefaceid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index for this ACL.  There will be one instance of
                policy class qosIpAclDefinition with this integer index for
                each ACE in the ACL per role combination.
                ''',
                'qosipaclid',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAclDefinitionEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipacldefinitiontable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipacldefinitiontable',
            False, 
            [
            _MetaInfoClassMember('qosIpAclDefinitionEntry', REFERENCE_LIST, 'Qosipacldefinitionentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry', 
                [], [], 
                '''                An instance of this class specifies an ACE in an ACL and its
                order with respect to other ACEs in the same ACL.
                ''',
                'qosipacldefinitionentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAclDefinitionTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry.QosipaclinterfacedirectionEnum' : _MetaInfoEnum('QosipaclinterfacedirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'in':'in_',
            'out':'out',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry',
            False, 
            [
            _MetaInfoClassMember('qosIpAclActionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipaclactionid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAclActAclId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The ACL associated with this action.
                ''',
                'qosipaclactaclid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclAggregateId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index identifying the aggregate that the packet belongs
                to.  It must correspond to the integer index of an instance of
                class qosAggregateTable or be zero.  If zero, the microflow
                does not belong to any aggregate and is not policed as part of
                any aggregate.
                ''',
                'qosipaclaggregateid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP to classify the packet with in the event that the
                packet matches an ACE in this ACL and the ACE is a permit.
                ''',
                'qosipacldscp',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDscpTrusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this attribute is true, then the Dscp associated with
                the packet is trusted, i.e., it is assumed to have already
                been set.  In this case, the Dscp is not rewritten with
                qosIpAclDscp (qosIpAclDscp is ignored).  The packet is still
                policed as part of its micro flow and its aggregate flow.
                
                When a trusted action is applied to an input interface, the
                Dscp associated with the packet is the one contained in the
                packet.  When a trusted action is applied to an output
                interface, the Dscp associated with the packet is the one that
                is the result of the input classification and policing.
                ''',
                'qosipacldscptrusted',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclInterfaceDirection', REFERENCE_ENUM_CLASS, 'QosipaclinterfacedirectionEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry.QosipaclinterfacedirectionEnum', 
                [], [], 
                '''                The direction of packet flow at the interface in question to
                which this ACL applies.
                ''',
                'qosipaclinterfacedirection',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclInterfaceRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The interfaces to which this ACL applies specified in terms
                of a set of roles.
                ''',
                'qosipaclinterfaceroles',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclMicroFlowPolicerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An index identifying the instance of policer to apply to the
                microflow.  It must correspond to the integer index of an
                instance of class qosPolicerTableor be zero.  If zero, the
                microflow is not policed.
                ''',
                'qosipaclmicroflowpolicerid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer that determines the order of this ACL in the list
                of ACLs applied to interfaces of the specified role
                combination. An ACL with a given order is positioned in the
                list before one with a higher order.
                ''',
                'qosipaclorder',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAclActionEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosipaclactiontable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosipaclactiontable',
            False, 
            [
            _MetaInfoClassMember('qosIpAclActionEntry', REFERENCE_LIST, 'Qosipaclactionentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry', 
                [], [], 
                '''                An instance of this class applies an ACL to traffic in a
                particular direction on an interface with a particular role
                combination, and specifies the action for packets which match
                the ACL.
                ''',
                'qosipaclactionentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAclActionTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.QosifschedulingdisciplineEnum' : _MetaInfoEnum('QosifschedulingdisciplineEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'weightedFairQueueing':'weightedFairQueueing',
            'weightedRoundRobin':'weightedRoundRobin',
            'customQueueing':'customQueueing',
            'priorityQueueing':'priorityQueueing',
            'classBasedWFQ':'classBasedWFQ',
            'fifo':'fifo',
            'pqWrr':'pqWrr',
            'pqCbwfq':'pqCbwfq',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry',
            False, 
            [
            _MetaInfoClassMember('qosIfSchedulingPreferenceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifschedulingpreferenceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfSchedulingDiscipline', REFERENCE_ENUM_CLASS, 'QosifschedulingdisciplineEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry.QosifschedulingdisciplineEnum', 
                [], [], 
                '''                An enumerate type for all the known scheduling disciplines.
                ''',
                'qosifschedulingdiscipline',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingPreference', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                The preference to use this scheduling discipline and queue
                type.  A higher value means a higher preference.  If two
                disciplines have the same preference the choice is a local
                decision.
                ''',
                'qosifschedulingpreference',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingQueueType', REFERENCE_ENUM_CLASS, 'QosinterfacequeuetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'QosinterfacequeuetypeEnum', 
                [], [], 
                '''                The queue type of this preference.
                ''',
                'qosifschedulingqueuetype',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The combination of roles the interface must have for this
                policy instance to apply to that interface.
                ''',
                'qosifschedulingroles',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfSchedulingPreferenceEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifschedulingpreferencestable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifschedulingpreferencestable',
            False, 
            [
            _MetaInfoClassMember('qosIfSchedulingPreferenceEntry', REFERENCE_LIST, 'Qosifschedulingpreferenceentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry', 
                [], [], 
                '''                An instance of this class specifies a scheduling preference
                for a queue-type on an interface with a particular role
                combination.
                ''',
                'qosifschedulingpreferenceentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfSchedulingPreferencesTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry.QosifdropdisciplineEnum' : _MetaInfoEnum('QosifdropdisciplineEnum', 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB',
        {
            'qosIfDropWRED':'qosIfDropWRED',
            'qosIfDropTailDrop':'qosIfDropTailDrop',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry',
            False, 
            [
            _MetaInfoClassMember('qosIfDropPreferenceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifdroppreferenceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfDropDiscipline', REFERENCE_ENUM_CLASS, 'QosifdropdisciplineEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry.QosifdropdisciplineEnum', 
                [], [], 
                '''                An enumerate type for all the known drop mechanisms.
                ''',
                'qosifdropdiscipline',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDropPreference', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                The preference to use this drop mechanism.  A higher value
                means a higher preference.  If two mechanisms have the same
                preference the choice is a local decision.
                ''',
                'qosifdroppreference',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDropRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The combination of roles the interface must have for this
                policy instance to apply to that interface.
                ''',
                'qosifdroproles',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfDropPreferenceEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifdroppreferencetable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifdroppreferencetable',
            False, 
            [
            _MetaInfoClassMember('qosIfDropPreferenceEntry', REFERENCE_LIST, 'Qosifdroppreferenceentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry', 
                [], [], 
                '''                An instance of this class specifies a drop preference for
                a drop mechanism on an interface with a particular role
                combination.
                ''',
                'qosifdroppreferenceentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfDropPreferenceTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry',
            False, 
            [
            _MetaInfoClassMember('qosIfDscpAssignmentId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifdscpassignmentid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP to which this row applies.
                ''',
                'qosifdscp',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDscpRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The role combination the interface must be configured with.
                ''',
                'qosifdscproles',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfQueue', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                The queue to which the DSCP applies for the given interface
                type.
                ''',
                'qosifqueue',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfQueueType', REFERENCE_ENUM_CLASS, 'QosinterfacequeuetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'QosinterfacequeuetypeEnum', 
                [], [], 
                '''                The interface queue type to which this row applies.
                ''',
                'qosifqueuetype',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfThresholdSet', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                The threshold set of the specified queue to which the DSCP
                applies for the given interface type.
                ''',
                'qosifthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfDscpAssignmentEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifdscpassignmenttable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifdscpassignmenttable',
            False, 
            [
            _MetaInfoClassMember('qosIfDscpAssignmentEntry', REFERENCE_LIST, 'Qosifdscpassignmententry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry', 
                [], [], 
                '''                An instance of this class specifies the queue and threshold
                set for a packet with a particular DSCP on an interface of
                a particular type with a particular role combination.
                ''',
                'qosifdscpassignmententry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfDscpAssignmentTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifredtable.Qosifredentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifredtable.Qosifredentry',
            False, 
            [
            _MetaInfoClassMember('qosIfRedId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifredid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfRedNumThresholdSets', REFERENCE_ENUM_CLASS, 'ThresholdsetrangeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'ThresholdsetrangeEnum', 
                [], [], 
                '''                The values in this entry apply only to queues with the number
                of thresholds specified by this attribute.
                ''',
                'qosifrednumthresholdsets',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The role combination the interface must be configured with.
                ''',
                'qosifredroles',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedThresholdSet', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                The threshold set to which the lower and upper values apply.
                It must be in the range 1 through qosIfRedNumThresholdSets.
                There must be exactly one PRI for each value in this range.
                ''',
                'qosifredthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedThresholdSetLower', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The threshold value below which no packets are dropped.
                ''',
                'qosifredthresholdsetlower',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedThresholdSetUpper', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The threshold value above which all packets are dropped.
                ''',
                'qosifredthresholdsetupper',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfRedEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifredtable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifredtable',
            False, 
            [
            _MetaInfoClassMember('qosIfRedEntry', REFERENCE_LIST, 'Qosifredentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifredtable.Qosifredentry', 
                [], [], 
                '''                An instance of this class specifies threshold limits for a
                particular RED threshold of a given threshold set on an
                interface and with a particular role combination.
                ''',
                'qosifredentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfRedTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry',
            False, 
            [
            _MetaInfoClassMember('qosIfTailDropId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosiftaildropid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfTailDropNumThresholdSets', REFERENCE_ENUM_CLASS, 'ThresholdsetrangeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'ThresholdsetrangeEnum', 
                [], [], 
                '''                The value in this entry applies only to queues with the
                number of thresholds specified by this attribute.
                ''',
                'qosiftaildropnumthresholdsets',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The role combination the interface must be configured with.
                ''',
                'qosiftaildroproles',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropThresholdSet', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                The threshold set to which the threshold value applies
                ''',
                'qosiftaildropthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropThresholdSetValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The threshold value above which packets are dropped.
                ''',
                'qosiftaildropthresholdsetvalue',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfTailDropEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosiftaildroptable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosiftaildroptable',
            False, 
            [
            _MetaInfoClassMember('qosIfTailDropEntry', REFERENCE_LIST, 'Qosiftaildropentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry', 
                [], [], 
                '''                An instance of this class specifies the queue depth for a
                particular tail-drop threshold set on an interface with a
                particular role combination.
                ''',
                'qosiftaildropentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfTailDropTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifweightstable.Qosifweightsentry' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifweightstable.Qosifweightsentry',
            False, 
            [
            _MetaInfoClassMember('qosIfWeightsId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifweightsid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfWeightsDrainSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of bytes that may be drained from the
                queue in one cycle.  The percentage of the bandwith allocated
                to this queue can be calculated from this attribute and the
                sum of the drain sizes of all the non-priority queues of the
                interface.
                ''',
                'qosifweightsdrainsize',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsNumQueues', REFERENCE_ENUM_CLASS, 'QueuerangeEnum' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'QueuerangeEnum', 
                [], [], 
                '''                The value of the weight in this instance applies only to
                interfaces with the number of queues specified by this
                attribute.
                ''',
                'qosifweightsnumqueues',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsQueue', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                The queue to which the weight applies.
                ''',
                'qosifweightsqueue',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsQueueSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The size of the queue in bytes.  Some devices set queue size
                in terms of packets.  These devices must calculate the queue
                size in packets by assuming an average packet size suitable
                for the particular interface.
                
                Some devices have a fixed size buffer to be shared among all
                queues.  These devices must allocate a fraction of the
                total buffer space to this queue calculated as the the ratio
                of the queue size to the sum of the queue sizes for the
                interface.
                ''',
                'qosifweightsqueuesize',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsRoles', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The role combination the interface must be configured with.
                ''',
                'qosifweightsroles',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfWeightsEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib.Qosifweightstable' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib.Qosifweightstable',
            False, 
            [
            _MetaInfoClassMember('qosIfWeightsEntry', REFERENCE_LIST, 'Qosifweightsentry' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifweightstable.Qosifweightsentry', 
                [], [], 
                '''                An instance of this class specifies the scheduling weight for
                a particular queue of an interface with a particular number
                of queues and with a particular role combination.
                ''',
                'qosifweightsentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfWeightsTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
    'CiscoQosPibMib' : {
        'meta_info' : _MetaInfoClass('CiscoQosPibMib',
            False, 
            [
            _MetaInfoClassMember('qosAggregateTable', REFERENCE_CLASS, 'Qosaggregatetable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosaggregatetable', 
                [], [], 
                '''                Instances of this class identify aggregate flows and the
                policer to apply to each.
                ''',
                'qosaggregatetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosCosToDscpTable', REFERENCE_CLASS, 'Qoscostodscptable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qoscostodscptable', 
                [], [], 
                '''                Maps each of eight CoS values to a DSCP.  When configured for
                the first time, all 8 entries of the table must be
                specified. Thereafter, instances may be modified (with a
                delete and install in a single decision) but not deleted
                unless all instances are deleted.
                ''',
                'qoscostodscptable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceAttributeTable', REFERENCE_CLASS, 'Qosdeviceattributetable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdeviceattributetable', 
                [], [], 
                '''                The single instance of this class indicates specific
                attributes of the device.  These include configuration values
                such as the configured PDP addresses, the maximum message
                size, and specific device capabilities.  The latter include
                input port-based and output port-based classification and/or
                policing, support for flow based policing, aggregate based
                policing, traffic shaping capabilities, etc.
                ''',
                'qosdeviceattributetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePibIncarnationTable', REFERENCE_CLASS, 'Qosdevicepibincarnationtable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdevicepibincarnationtable', 
                [], [], 
                '''                This class contains a single policy instance that identifies
                the current incarnation of the PIB and the PDP that installed
                this incarnation.  The instance of this class is reported to
                the PDP at client connect time so that the PDP can (attempt
                to) ascertain the current state of the PIB.
                ''',
                'qosdevicepibincarnationtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDiffServMappingTable', REFERENCE_CLASS, 'Qosdiffservmappingtable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosdiffservmappingtable', 
                [], [], 
                '''                Maps each DSCP to a marked-down DSCP.  Also maps each DSCP to
                an IP precedence and QosLayer2Cos.  When configured for the
                first time, all 64 entries of the table must be
                specified. Thereafter, instances may be modified (with a
                delete and install in a single decision) but not deleted
                unless all instances are deleted.
                ''',
                'qosdiffservmappingtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDropPreferenceTable', REFERENCE_CLASS, 'Qosifdroppreferencetable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifdroppreferencetable', 
                [], [], 
                '''                This class specifies the preference of the drop mechanism an
                interface chooses if it supports multiple drop mechanisms.
                Higher values are preferred over lower values.
                ''',
                'qosifdroppreferencetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDscpAssignmentTable', REFERENCE_CLASS, 'Qosifdscpassignmenttable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifdscpassignmenttable', 
                [], [], 
                '''                The assignment of each DSCP to a queue and threshold for each
                interface queue type.
                ''',
                'qosifdscpassignmenttable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedTable', REFERENCE_CLASS, 'Qosifredtable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifredtable', 
                [], [], 
                '''                A class of lower and upper values for each threshold set in a
                queue supporting WRED.  If the size of the queue for a given
                threshold is below the lower value then packets assigned to
                that threshold are always accepted into the queue.  If the
                size of the queue is above upper value then packets are always
                dropped.  If the size of the queue is between the lower and
                the upper then packets are randomly dropped.
                ''',
                'qosifredtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingPreferencesTable', REFERENCE_CLASS, 'Qosifschedulingpreferencestable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifschedulingpreferencestable', 
                [], [], 
                '''                This class specifies the scheduling preference an interface
                chooses if it supports multiple scheduling types.  Higher
                values are preferred over lower values.
                ''',
                'qosifschedulingpreferencestable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropTable', REFERENCE_CLASS, 'Qosiftaildroptable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosiftaildroptable', 
                [], [], 
                '''                A class for threshold sets in a queue supporting tail drop.
                If the size of the queue for a given threshold set is at or
                below the specified value then packets assigned to that
                threshold set are always accepted into the queue.  If the size
                of the queue is above the specified value then packets are
                always dropped.
                ''',
                'qosiftaildroptable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsTable', REFERENCE_CLASS, 'Qosifweightstable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosifweightstable', 
                [], [], 
                '''                A class of scheduling weights for each queue of an interface
                that supports weighted round robin scheduling or a mix of
                priority queueing and weighted round robin.  For a queue with
                N priority queues, the N highest queue numbers are the
                priority queues with the highest queue number having the
                highest priority.  WRR is applied to the non-priority queues.
                ''',
                'qosifweightstable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosInterfaceTypeTable', REFERENCE_CLASS, 'Qosinterfacetypetable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosinterfacetypetable', 
                [], [], 
                '''                This class describes the interface types of the interfaces
                that exist on the device.  It includes the queue type, role
                combination and capabilities of interfaces.  The PEP does not
                report which specific interfaces have which characteristics.
                ''',
                'qosinterfacetypetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceTable', REFERENCE_CLASS, 'Qosipacetable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipacetable', 
                [], [], 
                '''                ACE definitions.
                ''',
                'qosipacetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclActionTable', REFERENCE_CLASS, 'Qosipaclactiontable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipaclactiontable', 
                [], [], 
                '''                A class that applies a set of ACLs to interfaces specifying,
                for each interface the order of the ACL with respect to other
                ACLs applied to the same interface and, for each ACL the
                action to take for a packet that matches a permit ACE in that
                ACL.  Interfaces are specified abstractly in terms of
                interface role combinations.
                ''',
                'qosipaclactiontable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDefinitionTable', REFERENCE_CLASS, 'Qosipacldefinitiontable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosipacldefinitiontable', 
                [], [], 
                '''                A class that defines a set of ACLs each being an ordered list
                of ACEs.
                ''',
                'qosipacldefinitiontable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosMacClassificationTable', REFERENCE_CLASS, 'Qosmacclassificationtable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosmacclassificationtable', 
                [], [], 
                '''                A class of MAC/Vlan tuples and their associated CoS values.
                ''',
                'qosmacclassificationtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerTable', REFERENCE_CLASS, 'Qospolicertable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qospolicertable', 
                [], [], 
                '''                A class specifying policing parameters for both microflows
                and aggregate flows.  This table is designed for policing
                according to a token bucket scheme where an average rate and
                burst size is specified.
                ''',
                'qospolicertable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyTable', REFERENCE_CLASS, 'Qosunmatchedpolicytable' , 'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB', 'CiscoQosPibMib.Qosunmatchedpolicytable', 
                [], [], 
                '''                A policy class that specifies what QoS to apply to a packet
                that does not match any other policy configured for this role
                combination for a particular direction of traffic.
                ''',
                'qosunmatchedpolicytable',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'CISCO-QOS-PIB-MIB',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_QOS_PIB_MIB'
        ),
    },
}
_meta_table['CiscoQosPibMib.Qosdevicepibincarnationtable.Qosdevicepibincarnationentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosdevicepibincarnationtable']['meta_info']
_meta_table['CiscoQosPibMib.Qosdeviceattributetable.Qosdeviceattributeentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosdeviceattributetable']['meta_info']
_meta_table['CiscoQosPibMib.Qosinterfacetypetable.Qosinterfacetypeentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosinterfacetypetable']['meta_info']
_meta_table['CiscoQosPibMib.Qosdiffservmappingtable.Qosdiffservmappingentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosdiffservmappingtable']['meta_info']
_meta_table['CiscoQosPibMib.Qoscostodscptable.Qoscostodscpentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qoscostodscptable']['meta_info']
_meta_table['CiscoQosPibMib.Qosunmatchedpolicytable.Qosunmatchedpolicyentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosunmatchedpolicytable']['meta_info']
_meta_table['CiscoQosPibMib.Qospolicertable.Qospolicerentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qospolicertable']['meta_info']
_meta_table['CiscoQosPibMib.Qosaggregatetable.Qosaggregateentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosaggregatetable']['meta_info']
_meta_table['CiscoQosPibMib.Qosmacclassificationtable.Qosmacclassificationentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosmacclassificationtable']['meta_info']
_meta_table['CiscoQosPibMib.Qosipacetable.Qosipaceentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosipacetable']['meta_info']
_meta_table['CiscoQosPibMib.Qosipacldefinitiontable.Qosipacldefinitionentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosipacldefinitiontable']['meta_info']
_meta_table['CiscoQosPibMib.Qosipaclactiontable.Qosipaclactionentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosipaclactiontable']['meta_info']
_meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable.Qosifschedulingpreferenceentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable']['meta_info']
_meta_table['CiscoQosPibMib.Qosifdroppreferencetable.Qosifdroppreferenceentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosifdroppreferencetable']['meta_info']
_meta_table['CiscoQosPibMib.Qosifdscpassignmenttable.Qosifdscpassignmententry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosifdscpassignmenttable']['meta_info']
_meta_table['CiscoQosPibMib.Qosifredtable.Qosifredentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosifredtable']['meta_info']
_meta_table['CiscoQosPibMib.Qosiftaildroptable.Qosiftaildropentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosiftaildroptable']['meta_info']
_meta_table['CiscoQosPibMib.Qosifweightstable.Qosifweightsentry']['meta_info'].parent =_meta_table['CiscoQosPibMib.Qosifweightstable']['meta_info']
_meta_table['CiscoQosPibMib.Qosdevicepibincarnationtable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosdeviceattributetable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosinterfacetypetable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosdiffservmappingtable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qoscostodscptable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosunmatchedpolicytable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qospolicertable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosaggregatetable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosmacclassificationtable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosipacetable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosipacldefinitiontable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosipaclactiontable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosifschedulingpreferencestable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosifdroppreferencetable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosifdscpassignmenttable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosifredtable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosiftaildroptable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
_meta_table['CiscoQosPibMib.Qosifweightstable']['meta_info'].parent =_meta_table['CiscoQosPibMib']['meta_info']
