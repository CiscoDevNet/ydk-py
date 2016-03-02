


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'QueueRange_Enum' : _MetaInfoEnum('QueueRange_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'oneQ':'ONEQ',
            'twoQ':'TWOQ',
            'threeQ':'THREEQ',
            'fourQ':'FOURQ',
            'eightQ':'EIGHTQ',
            'sixteenQ':'SIXTEENQ',
            'thirtyTwoQ':'THIRTYTWOQ',
            'sixtyFourQ':'SIXTYFOURQ',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'QosInterfaceQueueType_Enum' : _MetaInfoEnum('QosInterfaceQueueType_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'oneQ1t':'ONEQ1T',
            'oneQ2t':'ONEQ2T',
            'oneQ4t':'ONEQ4T',
            'oneQ8t':'ONEQ8T',
            'twoQ1t':'TWOQ1T',
            'twoQ2t':'TWOQ2T',
            'twoQ4t':'TWOQ4T',
            'twoQ8t':'TWOQ8T',
            'threeQ1t':'THREEQ1T',
            'threeQ2t':'THREEQ2T',
            'threeQ4t':'THREEQ4T',
            'threeQ8t':'THREEQ8T',
            'fourQ1t':'FOURQ1T',
            'fourQ2t':'FOURQ2T',
            'fourQ4t':'FOURQ4T',
            'fourQ8t':'FOURQ8T',
            'eightQ1t':'EIGHTQ1T',
            'eightQ2t':'EIGHTQ2T',
            'eightQ4t':'EIGHTQ4T',
            'eightQ8t':'EIGHTQ8T',
            'sixteenQ1t':'SIXTEENQ1T',
            'sixteenQ2t':'SIXTEENQ2T',
            'sixteenQ4t':'SIXTEENQ4T',
            'sixtyfourQ1t':'SIXTYFOURQ1T',
            'sixtyfourQ2t':'SIXTYFOURQ2T',
            'sixtyfourQ4t':'SIXTYFOURQ4T',
            'oneP1Q0t':'ONEP1Q0T',
            'oneP1Q4t':'ONEP1Q4T',
            'oneP1Q8t':'ONEP1Q8T',
            'oneP2Q1t':'ONEP2Q1T',
            'oneP2Q2t':'ONEP2Q2T',
            'oneP3Q1t':'ONEP3Q1T',
            'oneP7Q8t':'ONEP7Q8T',
            'oneP3Q8t':'ONEP3Q8T',
            'sixteenQ8t':'SIXTEENQ8T',
            'oneP15Q8t':'ONEP15Q8T',
            'oneP15Q1t':'ONEP15Q1T',
            'oneP7Q1t':'ONEP7Q1T',
            'oneP31Q1t':'ONEP31Q1T',
            'thirtytwoQ1t':'THIRTYTWOQ1T',
            'thirtytwoQ8t':'THIRTYTWOQ8T',
            'oneP31Q8t':'ONEP31Q8T',
            'oneP7Q4t':'ONEP7Q4T',
            'oneP3Q4t':'ONEP3Q4T',
            'oneP7Q2t':'ONEP7Q2T',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'ThresholdSetRange_Enum' : _MetaInfoEnum('ThresholdSetRange_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'zeroT':'ZEROT',
            'oneT':'ONET',
            'twoT':'TWOT',
            'fourT':'FOURT',
            'eightT':'EIGHTT',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry',
            False, 
            [
            _MetaInfoClassMember('qosAggregateId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosaggregateid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosAggregatePolicerId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosAggregateTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosAggregateTable',
            False, 
            [
            _MetaInfoClassMember('qosAggregateEntry', REFERENCE_LIST, 'QosAggregateEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry',
            False, 
            [
            _MetaInfoClassMember('qosCosToDscpCos', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The L2 CoS value that is being mapped.
                ''',
                'qoscostodscpcos',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosCosToDscpDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The DSCP value to use when mapping the L2 CoS to a DSCP.
                ''',
                'qoscostodscpdscp',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosCosToDscpEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosCosToDscpTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosCosToDscpTable',
            False, 
            [
            _MetaInfoClassMember('qosCosToDscpEntry', REFERENCE_LIST, 'QosCosToDscpEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry', 
                [], [], 
                '''                An instance of this class maps a CoS value to a DSCP.
                ''',
                'qoscostodscpentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosCosToDscpTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry',
            False, 
            [
            _MetaInfoClassMember('qosDeviceAttributeId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosdeviceattributeid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDeviceCapabilities', REFERENCE_BITS, 'QosDeviceCapabilities_Bits' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry.QosDeviceCapabilities_Bits', 
                [], [], 
                '''                An enumeration of device capabilities.  Used by the PDP to
                select policies and configuration to push to the PEP.
                ''',
                'qosdevicecapabilities',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceMaxMessageSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum size message that this PEP is capable of
                receiving in bytes.  A value of zero means that the maximum
                message size is unspecified (but does not mean it is
                unlimited).  A message greater than this maximum results in a
                MessageTooBig error on a 'no commit' REP.
                ''',
                'qosdevicemaxmessagesize',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePepDomain', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The QoS domain that this device belongs to.  This is
                configured locally on the device (perhaps by some management
                protocol such as SNMP).  By default, it is the zero-length
                string.
                ''',
                'qosdevicepepdomain',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDevicePrimaryPdp', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the PDP configured to be the primary PDP for
                the device.
                ''',
                'qosdeviceprimarypdp',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceSecondaryPdp', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDeviceAttributeTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDeviceAttributeTable',
            False, 
            [
            _MetaInfoClassMember('qosDeviceAttributeEntry', REFERENCE_LIST, 'QosDeviceAttributeEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry',
            False, 
            [
            _MetaInfoClassMember('qosDeviceIncarnationId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosdeviceincarnationid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDevicePdpName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
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
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDevicePibIncarnationTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDevicePibIncarnationTable',
            False, 
            [
            _MetaInfoClassMember('qosDevicePibIncarnationEntry', REFERENCE_LIST, 'QosDevicePibIncarnationEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry',
            False, 
            [
            _MetaInfoClassMember('qosDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                A DSCP for which this entry contains mappings.
                ''',
                'qosdscp',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosL2Cos', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The L2 CoS value to use when mapping this DSCP to layer 2
                CoS.
                ''',
                'qosl2cos',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosMarkedDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The DSCP to use instead of the qosDscp when the packet is out
                of profile and hence marked as such.
                ''',
                'qosmarkeddscp',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDiffServMappingEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosDiffServMappingTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosDiffServMappingTable',
            False, 
            [
            _MetaInfoClassMember('qosDiffServMappingEntry', REFERENCE_LIST, 'QosDiffServMappingEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry', 
                [], [], 
                '''                An instance of this class represents mappings from a DSCP.
                ''',
                'qosdiffservmappingentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosDiffServMappingTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry.QosIfDropDiscipline_Enum' : _MetaInfoEnum('QosIfDropDiscipline_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'qosIfDropWRED':'QOSIFDROPWRED',
            'qosIfDropTailDrop':'QOSIFDROPTAILDROP',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfDropPreferenceId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifdroppreferenceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfDropDiscipline', REFERENCE_ENUM_CLASS, 'QosIfDropDiscipline_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry.QosIfDropDiscipline_Enum', 
                [], [], 
                '''                An enumerate type for all the known drop mechanisms.
                ''',
                'qosifdropdiscipline',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDropPreference', ATTRIBUTE, 'int' , None, None, 
                [(1, 16)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfDropPreferenceTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfDropPreferenceTable',
            False, 
            [
            _MetaInfoClassMember('qosIfDropPreferenceEntry', REFERENCE_LIST, 'QosIfDropPreferenceEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfDscpAssignmentId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifdscpassignmentid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
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
                [(1, 64)], [], 
                '''                The queue to which the DSCP applies for the given interface
                type.
                ''',
                'qosifqueue',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfQueueType', REFERENCE_ENUM_CLASS, 'QosInterfaceQueueType_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'QosInterfaceQueueType_Enum', 
                [], [], 
                '''                The interface queue type to which this row applies.
                ''',
                'qosifqueuetype',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfThresholdSet', ATTRIBUTE, 'int' , None, None, 
                [(1, 8)], [], 
                '''                The threshold set of the specified queue to which the DSCP
                applies for the given interface type.
                ''',
                'qosifthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfDscpAssignmentEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfDscpAssignmentTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfDscpAssignmentTable',
            False, 
            [
            _MetaInfoClassMember('qosIfDscpAssignmentEntry', REFERENCE_LIST, 'QosIfDscpAssignmentEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfRedId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifredid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfRedNumThresholdSets', REFERENCE_ENUM_CLASS, 'ThresholdSetRange_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'ThresholdSetRange_Enum', 
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
                [(1, 8)], [], 
                '''                The threshold set to which the lower and upper values apply.
                It must be in the range 1 through qosIfRedNumThresholdSets.
                There must be exactly one PRI for each value in this range.
                ''',
                'qosifredthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedThresholdSetLower', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The threshold value below which no packets are dropped.
                ''',
                'qosifredthresholdsetlower',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedThresholdSetUpper', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The threshold value above which all packets are dropped.
                ''',
                'qosifredthresholdsetupper',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfRedEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfRedTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfRedTable',
            False, 
            [
            _MetaInfoClassMember('qosIfRedEntry', REFERENCE_LIST, 'QosIfRedEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry.QosIfSchedulingDiscipline_Enum' : _MetaInfoEnum('QosIfSchedulingDiscipline_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'weightedFairQueueing':'WEIGHTEDFAIRQUEUEING',
            'weightedRoundRobin':'WEIGHTEDROUNDROBIN',
            'customQueueing':'CUSTOMQUEUEING',
            'priorityQueueing':'PRIORITYQUEUEING',
            'classBasedWFQ':'CLASSBASEDWFQ',
            'fifo':'FIFO',
            'pqWrr':'PQWRR',
            'pqCbwfq':'PQCBWFQ',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfSchedulingPreferenceId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifschedulingpreferenceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfSchedulingDiscipline', REFERENCE_ENUM_CLASS, 'QosIfSchedulingDiscipline_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry.QosIfSchedulingDiscipline_Enum', 
                [], [], 
                '''                An enumerate type for all the known scheduling disciplines.
                ''',
                'qosifschedulingdiscipline',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingPreference', ATTRIBUTE, 'int' , None, None, 
                [(1, 16)], [], 
                '''                The preference to use this scheduling discipline and queue
                type.  A higher value means a higher preference.  If two
                disciplines have the same preference the choice is a local
                decision.
                ''',
                'qosifschedulingpreference',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfSchedulingQueueType', REFERENCE_ENUM_CLASS, 'QosInterfaceQueueType_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'QosInterfaceQueueType_Enum', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable',
            False, 
            [
            _MetaInfoClassMember('qosIfSchedulingPreferenceEntry', REFERENCE_LIST, 'QosIfSchedulingPreferenceEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfTailDropId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosiftaildropid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfTailDropNumThresholdSets', REFERENCE_ENUM_CLASS, 'ThresholdSetRange_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'ThresholdSetRange_Enum', 
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
                [(1, 8)], [], 
                '''                The threshold set to which the threshold value applies
                ''',
                'qosiftaildropthresholdset',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropThresholdSetValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The threshold value above which packets are dropped.
                ''',
                'qosiftaildropthresholdsetvalue',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIfTailDropEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfTailDropTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfTailDropTable',
            False, 
            [
            _MetaInfoClassMember('qosIfTailDropEntry', REFERENCE_LIST, 'QosIfTailDropEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry',
            False, 
            [
            _MetaInfoClassMember('qosIfWeightsId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosifweightsid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIfWeightsDrainSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of bytes that may be drained from the
                queue in one cycle.  The percentage of the bandwith allocated
                to this queue can be calculated from this attribute and the
                sum of the drain sizes of all the non-priority queues of the
                interface.
                ''',
                'qosifweightsdrainsize',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsNumQueues', REFERENCE_ENUM_CLASS, 'QueueRange_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'QueueRange_Enum', 
                [], [], 
                '''                The value of the weight in this instance applies only to
                interfaces with the number of queues specified by this
                attribute.
                ''',
                'qosifweightsnumqueues',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsQueue', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                The queue to which the weight applies.
                ''',
                'qosifweightsqueue',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfWeightsQueueSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIfWeightsTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIfWeightsTable',
            False, 
            [
            _MetaInfoClassMember('qosIfWeightsEntry', REFERENCE_LIST, 'QosIfWeightsEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry',
            False, 
            [
            _MetaInfoClassMember('qosInterfaceTypeId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosinterfacetypeid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosInterfaceQueueType', REFERENCE_ENUM_CLASS, 'QosInterfaceQueueType_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'QosInterfaceQueueType_Enum', 
                [], [], 
                '''                The interface type in terms of number of queues and
                thresholds.
                ''',
                'qosinterfacequeuetype',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosInterfaceTypeCapabilities', REFERENCE_BITS, 'QosInterfaceTypeCapabilities_Bits' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'QosInterfaceTypeCapabilities_Bits', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosInterfaceTypeTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosInterfaceTypeTable',
            False, 
            [
            _MetaInfoClassMember('qosInterfaceTypeEntry', REFERENCE_LIST, 'QosInterfaceTypeEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry',
            False, 
            [
            _MetaInfoClassMember('qosIpAceId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipaceid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAceDscpMax', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The maximum value that the DSCP in the packet can have and
                match this ACE.
                ''',
                'qosipacedscpmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDscpMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The minimum value that the DSCP in the packet can have and
                match this ACE.
                ''',
                'qosipacedscpmin',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address to match against the packet's destination IP
                address.
                ''',
                'qosipacedstaddr',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstAddrMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A mask for the matching of the destination IP address.
                ''',
                'qosipacedstaddrmask',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The maximum value that the packet's layer 4 dest port number
                can have and match this ACE.
                ''',
                'qosipacedstl4portmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceDstL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
                [(0, 255)], [], 
                '''                The IP protocol to match against the packet's protocol.
                A value of zero means match all.
                ''',
                'qosipaceprotocol',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address to match against the packet's source IP
                address.
                ''',
                'qosipacesrcaddr',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcAddrMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A mask for the matching of the source IP address.
                ''',
                'qosipacesrcaddrmask',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The maximum value that the packet's layer 4 source port
                number can have and match this ACE.
                ''',
                'qosipacesrcl4portmax',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceSrcL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The minimum value that the packet's layer 4 source port
                number can have and match this ACE.
                ''',
                'qosipacesrcl4portmin',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAceEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAceTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAceTable',
            False, 
            [
            _MetaInfoClassMember('qosIpAceEntry', REFERENCE_LIST, 'QosIpAceEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry', 
                [], [], 
                '''                An instance of this class specifies an ACE.
                ''',
                'qosipaceentry',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosIpAceTable',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry.QosIpAclInterfaceDirection_Enum' : _MetaInfoEnum('QosIpAclInterfaceDirection_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'in':'IN',
            'out':'OUT',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry',
            False, 
            [
            _MetaInfoClassMember('qosIpAclActionId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipaclactionid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAclActAclId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The ACL associated with this action.
                ''',
                'qosipaclactaclid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclAggregateId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An index identifying the aggregate that the packet belongs
                to.  It must correspond to the integer index of an instance of
                class qosAggregateTable or be zero.  If zero, the microflow
                does not belong to any aggregate and is not policed as part of
                any aggregate.
                ''',
                'qosipaclaggregateid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
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
            _MetaInfoClassMember('qosIpAclInterfaceDirection', REFERENCE_ENUM_CLASS, 'QosIpAclInterfaceDirection_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry.QosIpAclInterfaceDirection_Enum', 
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
                [(0, 4294967295)], [], 
                '''                An index identifying the instance of policer to apply to the
                microflow.  It must correspond to the integer index of an
                instance of class qosPolicerTableor be zero.  If zero, the
                microflow is not policed.
                ''',
                'qosipaclmicroflowpolicerid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclOrder', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAclActionTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAclActionTable',
            False, 
            [
            _MetaInfoClassMember('qosIpAclActionEntry', REFERENCE_LIST, 'QosIpAclActionEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry',
            False, 
            [
            _MetaInfoClassMember('qosIpAclDefinitionId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosipacldefinitionid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosIpAceOrder', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer that determines the position of this ACE in the ACL.
                An ACE with a given order is positioned in the access contol
                list before one with a higher order.
                ''',
                'qosipaceorder',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclDefAceId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This attribute specifies the ACE in the qosIpAceTable that is
                in the ACL specified by qosIpAclId at the position specified
                by qosIpAceOrder.
                ''',
                'qosipacldefaceid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosIpAclDefinitionTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosIpAclDefinitionTable',
            False, 
            [
            _MetaInfoClassMember('qosIpAclDefinitionEntry', REFERENCE_LIST, 'QosIpAclDefinitionEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry',
            False, 
            [
            _MetaInfoClassMember('qosMacClassificationId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosmacclassificationid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosDstMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address of the L2 frame.
                ''',
                'qosdstmacaddress',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDstMacCos', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The CoS to assign the packet with the associated MAC/VLAN
                tuple.  Note that this CoS is overridden by the policies to
                classify the frame at layer 3 if there are any.
                ''',
                'qosdstmaccos',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDstMacVlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4095)], [], 
                '''                The VLAN of the destination MAC address of the L2 frame.
                ''',
                'qosdstmacvlan',
                'CISCO-QOS-PIB-MIB', False),
            ],
            'CISCO-QOS-PIB-MIB',
            'qosMacClassificationEntry',
            _yang_ns._namespaces['CISCO-QOS-PIB-MIB'],
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosMacClassificationTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosMacClassificationTable',
            False, 
            [
            _MetaInfoClassMember('qosMacClassificationEntry', REFERENCE_LIST, 'QosMacClassificationEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry.QosPolicerAction_Enum' : _MetaInfoEnum('QosPolicerAction_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'drop':'DROP',
            'mark':'MARK',
            'shape':'SHAPE',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry',
            False, 
            [
            _MetaInfoClassMember('qosPolicerId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qospolicerid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosPolicerAction', REFERENCE_ENUM_CLASS, 'QosPolicerAction_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry.QosPolicerAction_Enum', 
                [], [], 
                '''                An indication of how to handle out of profile packets.  When
                the shape action is chosen then traffic is shaped to the rate
                specified by qosPolicerRate.
                ''',
                'qospoliceraction',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerExcessBurst', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The excess size of a burst in terms of bits.
                ''',
                'qospolicerexcessburst',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerNormalBurst', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The normal size of a burst in terms of bits.
                ''',
                'qospolicernormalburst',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosPolicerTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosPolicerTable',
            False, 
            [
            _MetaInfoClassMember('qosPolicerEntry', REFERENCE_LIST, 'QosPolicerEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry.QosUnmatchedPolicyDirection_Enum' : _MetaInfoEnum('QosUnmatchedPolicyDirection_Enum', 'ydk.models.qos.CISCO_QOS_PIB_MIB',
        {
            'in':'IN',
            'out':'OUT',
        }, 'CISCO-QOS-PIB-MIB', _yang_ns._namespaces['CISCO-QOS-PIB-MIB']),
    'CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry',
            False, 
            [
            _MetaInfoClassMember('qosUnmatchedPolicyId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An integer index to identify the instance of the policy class.
                ''',
                'qosunmatchedpolicyid',
                'CISCO-QOS-PIB-MIB', True),
            _MetaInfoClassMember('qosUnmatchedPolicyAggregateId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An index identifying the aggregate that the packet belongs
                to.  It must correspond to the integer index of an instance of
                class qosAggregateTable or be zero.  If zero, the microflow
                does not belong to any aggregate and is not policed as part of
                any aggregate.
                ''',
                'qosunmatchedpolicyaggregateid',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyDirection', REFERENCE_ENUM_CLASS, 'QosUnmatchedPolicyDirection_Enum' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry.QosUnmatchedPolicyDirection_Enum', 
                [], [], 
                '''                The direction of packet flow at the interface in question to
                which this instance applies.
                ''',
                'qosunmatchedpolicydirection',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyDscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
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
                [(0, 4294967295)], [], 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB.QosUnmatchedPolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB.QosUnmatchedPolicyTable',
            False, 
            [
            _MetaInfoClassMember('qosUnmatchedPolicyEntry', REFERENCE_LIST, 'QosUnmatchedPolicyEntry' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
    'CISCOQOSPIBMIB' : {
        'meta_info' : _MetaInfoClass('CISCOQOSPIBMIB',
            False, 
            [
            _MetaInfoClassMember('qosAggregateTable', REFERENCE_CLASS, 'QosAggregateTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosAggregateTable', 
                [], [], 
                '''                Instances of this class identify aggregate flows and the
                policer to apply to each.
                ''',
                'qosaggregatetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosCosToDscpTable', REFERENCE_CLASS, 'QosCosToDscpTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosCosToDscpTable', 
                [], [], 
                '''                Maps each of eight CoS values to a DSCP.  When configured for
                the first time, all 8 entries of the table must be
                specified. Thereafter, instances may be modified (with a
                delete and install in a single decision) but not deleted
                unless all instances are deleted.
                ''',
                'qoscostodscptable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDeviceAttributeTable', REFERENCE_CLASS, 'QosDeviceAttributeTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDeviceAttributeTable', 
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
            _MetaInfoClassMember('qosDevicePibIncarnationTable', REFERENCE_CLASS, 'QosDevicePibIncarnationTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDevicePibIncarnationTable', 
                [], [], 
                '''                This class contains a single policy instance that identifies
                the current incarnation of the PIB and the PDP that installed
                this incarnation.  The instance of this class is reported to
                the PDP at client connect time so that the PDP can (attempt
                to) ascertain the current state of the PIB.
                ''',
                'qosdevicepibincarnationtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosDiffServMappingTable', REFERENCE_CLASS, 'QosDiffServMappingTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosDiffServMappingTable', 
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
            _MetaInfoClassMember('qosIfDropPreferenceTable', REFERENCE_CLASS, 'QosIfDropPreferenceTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfDropPreferenceTable', 
                [], [], 
                '''                This class specifies the preference of the drop mechanism an
                interface chooses if it supports multiple drop mechanisms.
                Higher values are preferred over lower values.
                ''',
                'qosifdroppreferencetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfDscpAssignmentTable', REFERENCE_CLASS, 'QosIfDscpAssignmentTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfDscpAssignmentTable', 
                [], [], 
                '''                The assignment of each DSCP to a queue and threshold for each
                interface queue type.
                ''',
                'qosifdscpassignmenttable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfRedTable', REFERENCE_CLASS, 'QosIfRedTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfRedTable', 
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
            _MetaInfoClassMember('qosIfSchedulingPreferencesTable', REFERENCE_CLASS, 'QosIfSchedulingPreferencesTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable', 
                [], [], 
                '''                This class specifies the scheduling preference an interface
                chooses if it supports multiple scheduling types.  Higher
                values are preferred over lower values.
                ''',
                'qosifschedulingpreferencestable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIfTailDropTable', REFERENCE_CLASS, 'QosIfTailDropTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfTailDropTable', 
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
            _MetaInfoClassMember('qosIfWeightsTable', REFERENCE_CLASS, 'QosIfWeightsTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIfWeightsTable', 
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
            _MetaInfoClassMember('qosInterfaceTypeTable', REFERENCE_CLASS, 'QosInterfaceTypeTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosInterfaceTypeTable', 
                [], [], 
                '''                This class describes the interface types of the interfaces
                that exist on the device.  It includes the queue type, role
                combination and capabilities of interfaces.  The PEP does not
                report which specific interfaces have which characteristics.
                ''',
                'qosinterfacetypetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAceTable', REFERENCE_CLASS, 'QosIpAceTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAceTable', 
                [], [], 
                '''                ACE definitions.
                ''',
                'qosipacetable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosIpAclActionTable', REFERENCE_CLASS, 'QosIpAclActionTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAclActionTable', 
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
            _MetaInfoClassMember('qosIpAclDefinitionTable', REFERENCE_CLASS, 'QosIpAclDefinitionTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosIpAclDefinitionTable', 
                [], [], 
                '''                A class that defines a set of ACLs each being an ordered list
                of ACEs.
                ''',
                'qosipacldefinitiontable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosMacClassificationTable', REFERENCE_CLASS, 'QosMacClassificationTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosMacClassificationTable', 
                [], [], 
                '''                A class of MAC/Vlan tuples and their associated CoS values.
                ''',
                'qosmacclassificationtable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosPolicerTable', REFERENCE_CLASS, 'QosPolicerTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosPolicerTable', 
                [], [], 
                '''                A class specifying policing parameters for both microflows
                and aggregate flows.  This table is designed for policing
                according to a token bucket scheme where an average rate and
                burst size is specified.
                ''',
                'qospolicertable',
                'CISCO-QOS-PIB-MIB', False),
            _MetaInfoClassMember('qosUnmatchedPolicyTable', REFERENCE_CLASS, 'QosUnmatchedPolicyTable' , 'ydk.models.qos.CISCO_QOS_PIB_MIB', 'CISCOQOSPIBMIB.QosUnmatchedPolicyTable', 
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
        'ydk.models.qos.CISCO_QOS_PIB_MIB'
        ),
    },
}
_meta_table['CISCOQOSPIBMIB.QosAggregateTable.QosAggregateEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosAggregateTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosCosToDscpTable.QosCosToDscpEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosCosToDscpTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDeviceAttributeTable.QosDeviceAttributeEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosDeviceAttributeTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDevicePibIncarnationTable.QosDevicePibIncarnationEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosDevicePibIncarnationTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDiffServMappingTable.QosDiffServMappingEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosDiffServMappingTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfDropPreferenceTable.QosIfDropPreferenceEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfDropPreferenceTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfDscpAssignmentTable.QosIfDscpAssignmentEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfDscpAssignmentTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfRedTable.QosIfRedEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfRedTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable.QosIfSchedulingPreferenceEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfTailDropTable.QosIfTailDropEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfTailDropTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfWeightsTable.QosIfWeightsEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIfWeightsTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosInterfaceTypeTable.QosInterfaceTypeEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosInterfaceTypeTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAceTable.QosIpAceEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIpAceTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAclActionTable.QosIpAclActionEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIpAclActionTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAclDefinitionTable.QosIpAclDefinitionEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosIpAclDefinitionTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosMacClassificationTable.QosMacClassificationEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosMacClassificationTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosPolicerTable.QosPolicerEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosPolicerTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosUnmatchedPolicyTable.QosUnmatchedPolicyEntry']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB.QosUnmatchedPolicyTable']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosAggregateTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosCosToDscpTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDeviceAttributeTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDevicePibIncarnationTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosDiffServMappingTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfDropPreferenceTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfDscpAssignmentTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfRedTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfSchedulingPreferencesTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfTailDropTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIfWeightsTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosInterfaceTypeTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAceTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAclActionTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosIpAclDefinitionTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosMacClassificationTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosPolicerTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
_meta_table['CISCOQOSPIBMIB.QosUnmatchedPolicyTable']['meta_info'].parent =_meta_table['CISCOQOSPIBMIB']['meta_info']
